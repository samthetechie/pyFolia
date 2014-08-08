#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

#from lxml import etree


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
