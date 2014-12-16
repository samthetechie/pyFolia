#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
This is a python geocoder reverse lookup with a cli wrapper. It simple yet powerful command line address to lat/lng to address lookup.
It has the following providers to choose from: OSM, Bing, Nokia, Yahoo, Google, ArcGIS, TomTom, Geonames, MapQuest, Geocoder.ca.
You can also use it directly as a Python module in your code.

usage:

$ reverse.py "oranienstrasse 183"

sample output: 

Oranienstraße 184, 10999 Berlin, Germany
'''

#>>> import geocoder # pip install geocoder
#>>> g = geocoder.osm('<address>')
#>>> g = geocoder.google('<address>')
#>>> g.lat, g.lng
#45.413140 -75.656703

# pip install geocoder
import geocoder
import argparse
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def __init__(self, input_address='Oranienstrasse 183'):
	self.input_address = input_address

def reverse_lookup(address):    # write Fibonacci series up to n
    location = geocoder.google(address)
    #location = geocoder.osm(address)
    g = geocoder.reverse([location.lat,location.lng])
    #g.address
    
    #sys.stdout.write(bcolors.OKBLUE + str(location.lat) + ", " + str(location.lng) + bcolors.ENDC)
    #sys.stdout.write("\n")
    sys.stdout.write(bcolors.OKGREEN + str(g.address) + bcolors.ENDC)
    sys.stdout.write("\n")

def main():
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('address', metavar='text', nargs='+',
                   help='an address to lookup (use "" when it\'s a sentence / more than one word)')
    args = parser.parse_args()

    location = geocoder.osm(args.address)
    g = geocoder.reverse([location.lat,location.lng])
    g.address
    
    #sys.stdout.write(bcolors.OKBLUE + str(location.lat) + ", " + str(location.lng) + bcolors.ENDC)
    #sys.stdout.write("\n")
    sys.stdout.write(bcolors.OKGREEN + str(g.address) + bcolors.ENDC)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
