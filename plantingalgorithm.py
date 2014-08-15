#!/usr/bin/env python
'''
This is a python planting algorithm which takes into account the size of the mature 
plants and their companion planting preferences.
You can also use it directly as a Python module in your code.

usage:

 $ python plantingalgorithm.py -a "Oranienstrasse 3, Berlin"
 $ python plantingalgorithm.py -u "7a"
 $ python plantingalgorithm.py -l "54.34234234, -34.23423423"

sample output:
'''

'''
1. Get list of plants that grow well (with block size, companion plants, plants they don't grow well with)
'''

'''
2. Filter companion plants and plants they don't grow well with to only include plants in list from 1. Or pull in companions of plants in the primary set.
'''

'''
3. Get plot size and determine how many hexagonal blocks fit. For particularly large plots, consider splitting into multiple smaller repeating plots too.
'''

'''
4. For each block, pick a plant using the following criteria (for three possible situations)-

    1. If it is the first block or there are no neighbours, pick at random from list

    2. If there is a plant in a neighbouring block, choose one of the plants it grows well with

    3. If there is a plant in more than one neighbouring block-

    Take intersection of plants all the neighbouring plants grow well with

    Exclude plants any don't grow well with
'''