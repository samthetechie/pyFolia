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

todo, compare strings with the ratio function. Decide on threshold.
https://stackoverflow.com/questions/682367/good-python-modules-for-fuzzy-string-comparison
'''

import re
import csv
import levenshtein

address = "Oranienstraße 184, 10999 Berlin, Germany"
addressTokens = address.split(",")
numTokens = len(addressTokens)
city = re.sub(" \d+", " ", addressTokens[numTokens-2].lower()).strip() #'berlin'
country = addressTokens[numTokens-1].lower().strip() #'germany'

with open('usda.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',')
     for row in reader:
     	#print row[1].lower() #country
     	#print row[0].lower() #city
     	    	
     	if row[0].lower() == city:
     		#print "match"
     		print row[2].lower().strip()

     	else:
     		if row[1].lower() == country:
				#print "match"
     			print row[2].lower().strip()
'''
