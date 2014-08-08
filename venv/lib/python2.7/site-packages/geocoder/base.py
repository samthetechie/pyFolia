#!/usr/bin/python
# coding: utf8

from __future__ import print_function
import requests


class Base(object):
    _base_parameter  = [':param ``location``: Your search location you want geocoded.']
    _base_reference = ['[GitHub Repo](https://github.com/DenisCarriere/geocoder)',
                       '[GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)']
    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug', 'short_name',
                'api', 'description', 'content', 'params', 'status_code', 'headers',
                'status_description', 'api_key', 'ok', 'key', 'id']
    _example = []
    _timeout = None
    attributes = []
    headers = {}

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.address)

    def __getattr__(self, item):
        return str('')

    def debug(self):
        print('# Debug')
        print('## Connection')
        print('* URL: [{0}]({1})'.format(self.provider.title(), self.url))
        print('* Status: {0}'.format(self.status))
        print('* Status Code: {0}'.format(self.status_code))
        for key, value in self.params.items():
            print('* Parameter [{0}]: {1}'.format(key, value))
        print('')
        print('## JSON Attributes')
        for key, value in self.json.items():
            print('* {0}: {1}'.format(key, value))
        print('')
        print('## Provider\'s Attributes')
        if self.parse:
            for key, value in self.parse.items():
                if value:
                    try:
                        value = value.encode('utf-8')
                    except:
                        pass
                    print('* {0}: {1}'.format(key, value))
        else:
            print(self.content)

    def help(self):
        print('# {0}'.format(self.provider))
        print('')
        print(self._description)
        print('Using Geocoder you can retrieve {0}\'s geocoded data from {1}.'.format(self.provider, self.api))
        print('')
        print('## Python Example')
        print('')
        print('```python')
        print('>>> import geocoder # pip install geocoder')
        if self._example:
            for line in self._example:
                print(line)
        else:
            print('>>> g = geocoder.{0}(\'<address>\')'.format(self.provider.lower()))
            print('>>> g.lat, g.lng')
            print('45.413140 -75.656703')
        print('...')
        print('```')
        print('')
        print('## Geocoder Attributes')
        print('')
        for attribute in self.attributes:
            print('* {0}'.format(attribute))
        print('')
        print('## Parameters')
        print('')
        for parameter in self._base_parameter + self._api_parameter:
            print('* {0}'.format(parameter))
        print('')

        print('## References')
        print('')
        for reference in self._base_reference + self._api_reference:
            print('* {0}'.format(reference))
        print('')

    def _json(self):
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                self.attributes.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value

    def _connect(self):
        self.status_code = 404
        self.status = 'Connecting...'
        try:
            r = requests.get(self.url, params=self.params, headers=self.headers, timeout=self._timeout)
            self.status_code = r.status_code
            self.url = r.url
            self.status = 'OK'
        except KeyboardInterrupt:
            self.status = 'ERROR - User Quit'
            sys.exit()
        except:
            self.status = 'ERROR - URL Connection'

        # Open JSON content from Request connection
        if self.status == 'OK':
            try:
                self.content = r.json()
            except:
                self.status = 'ERROR - JSON Corrupted'
                self.content = r.content

    def _parse(self, content, last=''):
        # DICTIONARY
        if isinstance(content, dict):
            for key, value in content.items():
                # NOKIA EXCEPTION
                if key == 'AdditionalData':
                    for item in value:
                        key = item.get('key')
                        value = item.get('value')
                        self.parse[key] = value

                # Only return the first result
                elif key == 'Items':
                    if value:
                        self._parse(value[0])

                # YAHOO EXCEPTION
                # Only return the first result
                elif key == 'Result':
                    if value:
                        # Value is a Dictionary
                        self._parse(value)

                # GOOGLE EXCEPTION 1 (For Reverse Geocoding)
                # Only return the first result
                elif key == 'results':
                    if value:
                        # Value is a List
                        self._parse(value[0])

                # GOOGLE EXCEPTION 2
                elif key == 'address_components':
                    for item in value:
                        short_name = item.get('short_name')
                        long_name = item.get('long_name')
                        all_types = item.get('types')
                        for types in all_types:
                            self.parse[types] = short_name
                            self.parse[types + '-long_name'] = long_name

                # GOOGLE EXCEPTION 3
                elif key == 'types':
                    self.parse['types'] = value[0]
                    for item in value:
                        name = 'types_{0}'.format(item)
                        self.parse[name] = True

                # MAXMIND EXCEPTION
                elif 'names' == key:
                    if 'en' in value:
                        name = value.get('en')
                        self.parse[last] = name

                # GEONAMES EXCEPTION
                elif 'geonames' == key:
                    self._parse(value)

                # STANDARD DICTIONARY
                elif isinstance(value, (list, dict)):
                    self._parse(value, key)
                else:
                    if last:
                        key = '{0}-{1}'.format(last, key)
                    self.parse[key] = value

        # LIST
        elif isinstance(content, list):
            if len(content) == 1:
                self._parse(content[0], last)
            elif len(content) > 1:
                for num, value in enumerate(content):

                    # BING EXCEPTION
                    if last not in ['geocodePoints']:
                        key = '{0}-{1}'.format(last, num)
                    else:
                        key = last
                    if isinstance(value, (list, dict)):
                        self._parse(value, key)
                    else:
                        self.parse[key] = value

        # STRING
        else:
            self.parse[last] = content

    def _test(self):
        if self.status_code == 200:
            if not self.address:
                self.status = 'ERROR - No results found'
            elif not bool(self.lng and self.lat):
                self.status = 'ERROR - No Geometry'
            elif self.status_description:
                self.status = self.status_description.decode()
            else:
                self.status = 'OK'
        elif self.status_code == 404:
            self.status = 'ERROR - URL Connection'


    def _get_json_str(self, item):
        result = self.parse.get(item)
        try:
            return result.encode('utf-8')
        except:
            return str('')

    def _get_json_float(self, item):
        result = self.parse.get(item)
        try:
            return float(result)
        except:
            return 0.0

    def _get_json_int(self, item):
        result = self.parse.get(item)
        try:
            return int(result)
        except:
            return 0

    def _get_bbox(self, south, west, north, east):
        # South Latitude, West Longitude, North Latitude, East Longitude
        self.south = south
        self.west = west
        self.north = north
        self.east = east

        if bool(south and east and north and west):
            self.southwest = {'lat': south, 'lng': west}
            self.southeast = {'lat': south, 'lng': east}
            self.northeast = {'lat': north, 'lng': east}
            self.northwest = {'lat': north, 'lng': west}
            bbox = {'southwest': self.southwest, 'northeast': self.northeast}
            return bbox
        return str('')

    @property
    def ok(self):
        if bool(self.lng and self.lat):
            return True
        else:
            return False

    @property
    def wkt(self):
        wkt = dict()
        if bool(self.lng and self.lat):
            schema = 'POINT({x} {y})'
            wkt['point'] = schema.format(x=self.lng, y=self.lat)

        if bool(self.east and self.west and self.north and self.south):
            schema = 'POLYGON(({east} {north}, {east} {south}, {west} {south}, {west} {north}, {east} {north}))'
            wkt['polygon'] = schema.format(north=self.north, east=self.east, south=self.south, west=self.west)

        return wkt
