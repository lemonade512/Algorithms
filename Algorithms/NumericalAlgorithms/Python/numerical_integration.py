#!/usr/bin/python

import math

def rectangle_rule(function, xmin, xmax, num_intervals):
    dx = float(xmax - xmin) / num_intervals

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + dx * function(x)
        x = x + dx

    return total_area

def trapezoid_rule(function, xmin, xmax, num_intervals):
    dx = float(xmax - xmin) / num_intervals

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + dx * (function(x) + function(x+dx)) / 2
        x = x + dx

    return total_area

def adaptive_trapezoid_rule(function, xmin, xmax, num_intervals, max_err):
    dx = float(xmax - xmin) / num_intervals
    total = 0.0

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + slice_area(function, x, x+dx, max_err)
        x = x + dx

    return total_area

def slice_area(function, x1, x2, max_err):
    y1 = function(float(x1))
    y2 = function(float(x2))
    xm = float(x1 + x2) / 2
    ym = function(float(xm))

    area12 = (x2 - x1) * (y1 + y2) / 2.0
    area1m = (xm - x1) * (y1 + ym) / 2.0
    aream2 = (x2 - xm) * (ym + y2) / 2.0
    area1m2 = area1m + aream2

    error = (area1m2 - area12) / area12

    if(abs(error) < max_err):
        return area1m2
    else:
        a1 = slice_area(function, x1, xm, max_err)
        a2 = slice_area(function, xm, x2, max_err)
        return a1 + a2

def my_func(x):
    return 1+x+math.sin(2*x)

if __name__ == "__main__":
    print "Rectangles"
    print "Area under (1+x+sin(2x)) from 0 to 5 with 10 intervals::"
    print "    " + str(rectangle_rule(my_func, 0, 5, 10))
    print "Area under (1+x+sin(2x)) from 0 to 5 with 50 intervals::"
    print "    " + str(rectangle_rule(my_func, 0, 5, 50))
    print ""
    print "Trapezoids"
    print "Area under (1+x+sin(2x)) from 0 to 5 with 10 intervals::"
    print "    " + str(trapezoid_rule(my_func, 0, 5, 10))
    print ""
    print "Adaptive"
    print "Area under (1+x+sin(2x)) from 0 to 5 with 2 initial intervals"
    print "and a max error of 1%::"
    print "    " + str(adaptive_trapezoid_rule(my_func, 0, 5, 2, 0.01))
    print "    " + str(adaptive_trapezoid_rule(my_func, 0, ))
