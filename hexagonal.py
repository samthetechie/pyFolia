#!/usr/bin/env python

radius = 4
for r in range(radius):
    print "radius %d" % r
    x = 0
    y = -r
    z = +r
    print x,y,z
    for i in range(r):
        x = x+1
        z = z-1
        print x,y,z
    for i in range(r):
        y = y+1
        z = z-1
        print x,y,z
    for i in range(r):
        x = x-1
        y = y+1
        print x,y,z
    for i in range(r):
        x = x-1
        z = z+1
        print x,y,z
    for i in range(r):
        y = y-1
        z = z+1
        print x,y,z
    for i in range(r-1):
        x = x+1
        y = y-1
        print x,y,z