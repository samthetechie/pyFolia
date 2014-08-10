#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
This is a python USDA growing zone lookup tool with a cli wrapper. It simple yet powerful command line address to USDA growing zone lookup.
It has the following providers to choose from: OSM, Bing, Nokia, Yahoo, Google, ArcGIS, TomTom, Geonames, MapQuest, Geocoder.ca.
You can also use it directly as a Python module in your code.

usage:

$ usda.py "Oranienstraße 184, 10999 Berlin, Germany"
#D145, 47410 Saint-Colomb-de-Lauzun, France

sample output: 

7a

test cases:
working:
./usda.py "Oranienstraße 184, 10999 Berlin, Germany"

not working:
./usda.py "D145, 47410 Saint-Colomb-de-Lauzun, France"
'''

import re
import csv
import reverse
#import Levenshtein #giving false positives, stick with the 'dumb' way

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def __init__(self, input_address=''):
     self.input_address = input_address

def main():
    reverse.reverse_looku
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('address', metavar='text', nargs='+',
                   help='an address to lookup (use "" when it\'s a sentence / more than one word)')
    args = parser.parse_args()

    #print args.address

    addressTokens = str(args.address).split(",")
    #print addressTokens
    numTokens = len(addressTokens)
    city = str(re.sub("[^a-zA-Z]", " ", addressTokens[numTokens-2].lower()).strip()) #'berlin'
    country = str(re.sub("[^a-zA-Z0-9]", " ", addressTokens[numTokens-1].lower()).strip()) #'germany'
    #print city
    #print country

    with open('usda.csv', 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         for row in reader:
              if row[0].lower() == city.lower().strip(): #this could be improved with Levenshtein.ratio(row[0].lower().strip(), city) > 0.5 gives a false result!
                   #print "city match: "
                   #print row[0].lower().strip() #city
                   #print row[1].lower().strip() #country
                   print row[2].lower().strip() #usda zone
                   f.close()
                   break #this break prevents country matching from occuring if city matching is successful
              else:
                   #print row[1].lower().strip()
                   if row[1].lower().strip() == country.lower().strip(): #this could be improved with Levenshtein.ratio(string1, string2) and compared to a threshold if required
                        #print "country match"
                        print row[2].lower().strip()
                        f.close()
                        break #this break prevents multiple hits
    #location = geocoder.osm(args.address)
   #sys.stdout.write(bcolors.OKBLUE + str(location.lat) + ", " + str(location.lng) + bcolors.ENDC)
   #sys.stdout.write("\n")

if __name__ == "__main__":
    main()
