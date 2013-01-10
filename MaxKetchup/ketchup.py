# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
Filename   : SUNRISE_SUNSET.py
Date       : 2012-11-27
Author     : Joe Lotz
Purpose    : My attempt at recreating the results from one of my favorite blogs
                using Python.
Sources    : http://datagenetics.com/blog/august12012/index.html

-------------------------------------------------------------------------------
'''
import math
import matplotlib.pyplot as plt
import csv

global LENGTH
global DIAMETER
global PI


'''
FROSTUM
            b
   -------------------   -
    \               /    |
   l \             /     | h
      \___________/      |
            d            -

Volume_frostum = (pi h)/12 (d^2+db+b^2)
'''

PI = math.pi
# height = 42
DIAMETER = 53
# base = 75
LENGTH = 43.5
#angle_deg = 15

#L = HEIGHT / mycos(calc_angle)
#length = 42/mycos(angle_deg)


#sin(calc_angle)*length

#sin()= opp/l -> opp = sin() * l
#cos()= h/l -> l = h/cos()

def height(angle) :
    return mycos(angle) * LENGTH

def base(angle) :
    return 2 * opp(angle) + DIAMETER

def opp(angle) :
    return mysin(angle) * LENGTH

def mycos(angle_degrees):
    return math.cos(math.radians(angle_degrees))

def mysin(angle_degrees):
    return math.sin(math.radians(angle_degrees))

def volume(angle) :
    volume = ((PI*height(angle))/12) * ( math.pow(DIAMETER,2) + (DIAMETER * base(angle)) + \
        math.pow(base(angle),2))
    return volume


angle_list = range(0,95,1)
vol_list = map(volume,angle_list)


plt.plot(angle_list,vol_list)
plt.grid()
plt.show()


ndx = vol_list.index(max(vol_list))
print 'The max volume is ' + str(int(vol_list[ndx])) + 'mm^3 at ' + str(angle_list[ndx]) + ' degrees'
#######################################


#outpath = '/home/joe/Python/ketchup.tsv'
#outf = open(outpath, 'w')
#
#
#with open(outpath, 'wb') as f:
#    writer = csv.writer(f)
#    writer.writerows(vol_list)    
#
