#!/usr/bin/env python
'''
This is a python myFolia scraper with a cli wrapper.
You can also use it directly as a Python module in your code.

usage:

 $ python myFolia.py carrot

sample output:

[[u'Category', u'Biennial'],
 [u'Difficulty', u'Easy 2/5'],
 [u'Lifecycle', u'Biennial'],
 [u'Growth Habit', u'Erect'],
 [u'Hardiness', u'Very Hardy'],
 [u'Country of Origin', u'Afghanistan'],
 [u'Mature Height', u'15.0 cm / 5.85 inches'],
 [u'Mature Spread', u'2.5 cm / 0.98 inches'],
 [u'USDA Zone Range',
  u'Zone 3\n          \n          to\n          \n          Zone 11'],
 [u'pH Range', u'6.0 - 6.5'],
 [u'Water Requirements', u'High'],
 [u'Nitrogen Requirements', u'Medium'],
 [u'Soil', u'Loam'],
 [u'Sun', u'Full Sun'],
 [u'Can Sow Direct?', u'Yes'],
 [u'Sowing Depth', u'0.6 cm / 0.23 inches'],
 [u'Sowing Distance Apart', u'1.0 cm / 0.39 inches'],
 [u'Sowing Row Distance Apart', u'Help build our wiki!'],
 [u'Ideal Germination Temperature Range', u'16\xb0C / 61\xb0F'],
 [u'Growing Temperatures', u'Help build our wiki!'],
 [u'Planting Distance Apart', u'5.0 cm / 1.95 inches'],
 [u'Planting Row Distance Apart', u'5.0 cm / 1.95 inches'],
 [u'Bloom Time', u'Help build our wiki!'],
 [u'Harvest Time', u'Late Spring'],
 [u'Pruning Time', u'Late Spring']]
'''

import requests
from bs4 import BeautifulSoup


class ENotFound(Exception):
    def __init__(self, plant):
        super(ENotFound, self).__init__()
        self.plant = plant

    def __repr__(self):
        return 'Plant %s not found' % self.plant


class myFolia(object):

    BASE_URL = 'http://myfolia.com'
    SEARCH_URL = 'http://myfolia.com/plants/search'
    NOT_FOUND = 'No plants found for your search.'

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

    def get_data(self, plant):
        link = self.__search(plant)
        html = self.__get(myFolia.BASE_URL + link)
        soup = BeautifulSoup(html)

        care = soup.find('form', attrs={'class': 'display clearfix wiki-table'})
        data = []
        for label in care.findAll('label'):
            data.append([label.contents[0].strip(), label.find('span').text.strip()])

        return data


if __name__ == '__main__':
    import sys
    from pprint import pprint
    mf = myFolia()
    pprint(mf.get_data(sys.argv[1]))
