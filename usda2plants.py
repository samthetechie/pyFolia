#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
This is a python usda growing zone to plant lookup tool with a cli wrapper.
You can also use it directly as a Python module in your code.

usage:

$ usda2plants.py "8a"

sample output:

["Tomato","Sweet pepper","Onion","Lettuce","Potato","Cucumber","Carrot,"Rose","Bean","Chili pepper"]

'''

import requests
import re
from bs4 import BeautifulSoup


class ENotFound(Exception):
    def __init__(self, plant):
        super(ENotFound, self).__init__()
        self.plant = plant

    def __repr__(self):
        return 'Plant %s not found' % self.plant


class usda2plants(object):

    BASE_URL = 'http://myfolia.com/zones/'
    URL_SUFFIXES = ["1","2","2a","2b","3","3a","3b","4","4a","4b","5","5a","5b","6","6a","6b","7","7a","7b","8","8a","8b","9","9a","9b","10","10a","10b","11","11a","11b","12","12a","12b","13","13a","13b","14"]
    NOT_FOUND = 'Looks like something has gone wrong.'

    def __init__(self):
        pass

    def __get(self, url, data={}):
        try:
            r = requests.request('GET',
                                 url,
                                 data=data,
                                 )
            if r.status_code == 200:
                return r.content
        except requests.exceptions.ConnectionError as e:
            print('Connection to server %s failed: %s', myFolia.SEARCH_URL, e)
        except requests.exceptions.Timeout as e:
            print('Connection to server %s timed out: %s', myFolia.SEARCH_URL, e)
        except requests.exceptions.HTTPError as e:
            print('Got HTTPError from server %s: %s', myFolia.SEARCH_URL, e)

    def __search(self, plant):
        """
        get link to <plant>

        Input:
            plant   plant name e.g. tomato
        """

        html = self.__get(myFolia.SEARCH_URL, data={'query': plant})
        soup = BeautifulSoup(html)

        if soup.body.findAll(text=myFolia.NOT_FOUND):
            raise ENotFound(plant)

        div = soup.find('div', {'id': 'main'})
        link = div.find('a')
        return link['href']

    def __get_numbers(self, data):
        nums = map(float, re.findall(r"[-+]?\d*\.\d+|\d+", data))
        return nums

    def parse_Difficulty(self, data):
        desc, num = data.split()
        score, scale = map(int, num.split('/'))
        return [desc, [score, scale]]

    def parse_Can_Sow_Direct(self, data):
        return data == 'Yes'

    def get_data(self, plant):
        link = self.__search(plant)
        html = self.__get(myFolia.BASE_URL + link)
        soup = BeautifulSoup(html)

        data = {'link': link}
        for pref in ['like', 'love', 'dislike']:
            data[pref] = []
            span_prefs = soup.findAll('span', attrs={'class': pref})
            for p in span_prefs:
                data[pref].append(p.findNext('a')['href'])

        care = soup.find('form', attrs={'class': 'display clearfix wiki-table'})
        for label in care.findAll('label'):
            key = label.contents[0].strip().replace(' ', '_').replace('?', '')
            val = label.find('span').text.strip()
            if val == 'Help build our wiki!':
                continue
            try:
                parser = getattr(self, 'parse_' + key)
                data[key] = parser(val)
            except AttributeError:
                nums = self.__get_numbers(val)
                if nums:
                    data[key] = nums
                else:
                    data[key] = val
            except Exception:
                data[key] = val

        return data


if __name__ == '__main__':
    import sys
    from pprint import pprint
    mf = myFolia()
    pprint(mf.get_data(sys.argv[1]))
