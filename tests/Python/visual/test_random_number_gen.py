#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import png
from Algorithms.NumericalAlgorithms.Python.random_numbers import fair_generator, random_generator

f = fair_generator(0, 2)

s = []
for i in xrange(512):
    row = []
    for j in xrange(512):
        row.append(next(f))
    s.append(row)

f = open('random.png', 'wb')
w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
w.write(f, s)
f.close()


#Colored picture
f = fair_generator(0, 256)
s = []
for i in xrange(512):
    row = []
    for j in xrange(512):
        row.append(next(f))
        row.append(next(f))
        row.append(next(f))
        #row.append(0)
    s.append(row)

f = open('random_color.png', 'wb')
w = png.Writer(width=512, height=512, background=(0, 0, 0), bitdepth=8)
w.write(f, s)
f.close()
