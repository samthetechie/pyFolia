#!/usr/bin/python
# coding: utf8

from .base import Base


class Osm(Base):
    provider = 'OSM'
    api = 'Nominatim'
    url = 'http://nominatim.openstreetmap.org/search'
    _description = 'Nominatim (from the Latin, \'by name\') is a tool to search OSM data by name \n'
    _description += 'and address and to generate synthetic addresses of OSM points (reverse geocoding).'
    _api_reference = ['[{0}](http://wiki.openstreetmap.org/wiki/Nominatim)'.format(api)]
    _api_parameter  = []

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['format'] = 'json'
        self.params['limit'] = 1
        self.params['addressdetails'] = 1
        self.params['q'] = location

        # Initialize
        self._connect()
        self._parse(self.content)
        self._test()
        self._json()

    @property
    def lat(self):
        return self._get_json_float('lat')

    @property
    def lng(self):
        return self._get_json_float('lon')

    @property
    def quality(self):
        return self._get_json_str('type')

    """
    >>>>>>>>>>>>>>>>>>>>>>>>>>>
    TO-DO
    Regex on Postal Code
    >>>>>>>>>>>>>>>>>>>>>>>>>>>
    """
    @property
    def postal(self):
        return self._get_json_str('address-postcode')

    @property
    def bbox(self):
        south = self._get_json_float('boundingbox-0')
        west = self._get_json_float('boundingbox-2')
        north = self._get_json_float('boundingbox-1')
        east = self._get_json_float('boundingbox-3')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self._get_json_str('display_name')

    @property
    def street_number(self):
        return self._get_json_str('address-house_number')

    @property
    def route(self):
        return self._get_json_str('address-road')

    @property
    def neighborhood(self):
        return self._get_json_str('address-neighbourhood')

    @property
    def suburb(self):
        return self._get_json_str('address-suburb')

    @property
    def locality(self):
        return self._get_json_str('address-city')

    @property
    def state(self):
        return self._get_json_str('address-state')

    @property
    def country(self):
        return self._get_json_str('address-country')

if __name__ == '__main__':
    g = Osm('453 Booth Street, Ottawa')
    g.help()
    g.debug()