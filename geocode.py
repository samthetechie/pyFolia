#!/usr/bin/python
'''
This is a python geocoder with a cli wrapper. It simple yet powerful command line address to lat/lng lookup.
It has the following providers to choose from: OSM, Bing, Nokia, Yahoo, Google, ArcGIS, TomTom, Geonames, MapQuest, Geocoder.ca.
You can also use it directly as a Python module in your code.
'''

# pip install geocoder

import geocoder

def __init__(self, input_address='Oranienstraße 183'):
	self.input_address = input_address

def main():
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('address', metavar='text', nargs='+',
                   help='an address to lookup (use "" when it\'s a sentence / more than one word)')
    args = parser.parse_args()

    location = geocoder.google(args.address)
    
    sys.stdout.write(bcolors.OKBLUE + location.lat + bcolors.ENDC)
    sys.stdout.write(bcolors.OKBLUE + location.lng + bcolors.ENDC)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()