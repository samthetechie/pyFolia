#!/usr/bin/python
# coding: utf8

from .base import Base
import re
import requests


class Canadapost(Base):
    provider = 'CanadaPost'
    api = 'Addres Complete API'
    url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
    url += '/Interactive/RetrieveFormatted/v2.00/json3ex.ws'
    _description = 'The next generation of address finders, AddressComplete uses intelligent, fast\n'
    _description += 'searching to improve data accuracy and relevancy. Simply start typing a business\n'
    _description += 'name, address or Postal Code and AddressComplete will suggest results as you go.'
    _api_reference = ['[{0}](https://www.canadapost.ca/pca/)'.format(api)]
    _api_parameter = [':param ``country``: (default=\'CAN\') biase the search on a selected country.']
    _api_parameter  = [':param ``key``: (optional) use your own API Key from CanadaPost Address Complete.']
    _example = ['>>> g = geocoder.canadapost(\'<address>\')',
                '>>> g.postal',
                '\'K1R 7K9\'']

    def __init__(self, location, country='CAN', key=''):
        self.location = location
        self._country = country
        self.key = key
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['Key'] = self._retrieve_key()
        if self.key:
            self.params['Id'] = self._retrieve_id()

        # Initialize
        if bool(self.key and self.id):
            self._connect()
            self._parse(self.content)
            self._test()
            self._json()

    def __repr__(self):
        return "<[{0}] {1} [{2} - {3}]>".format(self.status, self.provider, self.postal, self.address)

    def _retrieve_key(self):
        if self.key:
            return self.key
        else:
            url = 'http://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf'
            try:
                r = requests.get(url, timeout=self._timeout)
                text = r.text
            except:
                text = str('')
                self.status = 'ERROR - URL Connection'

            expression = r'key=(....-....-....-....)'
            pattern = re.compile(expression)
            match = pattern.search(text)
            if match:
                self.key = match.group(1)
                return self.key
            else:
                self.status = 'ERROR - No API Key'

    def _retrieve_id(self):
        params = dict()
        params['Key'] = self.key
        params['SearchTerm'] = self.location
        params['Country'] = self._country

        url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
        url += '/Interactive/Find/v2.00/json3ex.ws'
        try:
            r = requests.get(url, params=params, timeout=self._timeout)
            json = r.json()
        except:
            json = dict()
            self.status = 'ERROR - URL Connection'

        if 'Items' in json:
            items = json['Items'][0]
            description = items.get('Description')
            if 'Error' in items:
                self.status = 'ERROR - {0}'.format(items.get('Description'))
            elif description:
                self.status = 'ERROR - Too many results, {0}'.format(items.get('Description'))
            elif 'Id' in items:
                self.id = items['Id']
                return self.id

    @property
    def ok(self):
        return bool(self.postal)

    @property
    def status_description(self):
        if self.ok:
            return 'OK'

    @property
    def quality(self):
        return self._get_json_str('Type')

    @property
    def address(self):
        return self._get_json_str('Line1')

    @property
    def postal(self):
        return self._get_json_str('PostalCode')

    @property
    def street_number(self):
        return self._get_json_str('BuildingNumber')

    @property
    def route(self):
        return self._get_json_str('Street')

    @property
    def locality(self):
        return self._get_json_str('City')

    @property
    def state(self):
        return self._get_json_str('ProvinceName')

    @property
    def country(self):
        return self._get_json_str('CountryName')

if __name__ == '__main__':
    g = Canadapost("453 Booth Street, Ottawa")
    g.help()
    g.debug()