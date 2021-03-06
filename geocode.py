#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
This is a python geocoder with a cli wrapper. It simple yet powerful command line address to lat/lng lookup.
It has the following providers to choose from: OSM, Bing, Nokia, Yahoo, Google, ArcGIS, TomTom, Geonames, MapQuest, Geocoder.ca.
You can also use it directly as a Python module in your code.

usage:

$ python geocode.py "oranienstrasse 183"

sample output: 52.50035, 13.42055
'''

#>>> import geocoder # pip install geocoder
#>>> g = geocoder.osm('<address>')
#>>> g.lat, g.lng
#45.413140 -75.656703

# pip install geocoder
import geocoder

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class geocoder_coords:
    def __init__(self, input_address='Oranienstrasse 183'):
	self.input_address = input_address

def main():
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('address', metavar='text', nargs='+',
                   help='an address to lookup (use "" when it\'s a sentence / more than one word)')
    args = parser.parse_args()

    location = geocoder.osm(args.address)
    
    sys.stdout.write(bcolors.OKBLUE + str(location.lat) + ", " + str(location.lng) + bcolors.ENDC)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()