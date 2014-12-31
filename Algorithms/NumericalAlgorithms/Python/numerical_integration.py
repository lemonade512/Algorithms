#!/usr/bin/python

import math

def rectangle_rule(function, xmin, xmax, num_intervals):
    """ Integrates over a function using Riemann Sums with rectangles.

    Args:
        function: The function to integrate over
        xmin: The starting value of the range to integrate over
        xmax: The ending value of the range to integrate over
        num_intervals: How many intervals to use.
                       More intervals = higher precision
    """
    dx = float(xmax - xmin) / num_intervals

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + dx * function(x)
        x = x + dx

    return total_area

def trapezoid_rule(function, xmin, xmax, num_intervals):
    """ Integrates over a function using Riemann Sums with trapezoids.

    Args:
        function: The function to integrate over
        xmin: The starting value of the range to integrate over
        xmax: The ending value of the range to integrate over
        num_intervals: How many intervals to use.
                       More intervals = higher precision
    """
    dx = float(xmax - xmin) / num_intervals

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + dx * (function(x) + function(x+dx)) / 2
        x = x + dx

    return total_area

def adaptive_trapezoid_rule(function, xmin, xmax, num_intervals, max_err):
    """ Integrates over a function using Riemann Sums with adaptive trapezoids.

    Args:
        function: The function to integrate over
        xmin: The starting value of the range to integrate over
        xmax: The ending value of the range to integrate over
        num_intervals: How many intervals to use.
                       More intervals = higher precision
        max_err: The maximum error tolerance for each interval. A lower tolerance
                 gives higher precision results
    """
    dx = float(xmax - xmin) / num_intervals
    total = 0.0

    total_area = 0.0
    x = float(xmin)
    for i in range(num_intervals):
        total_area = total_area + slice_area(function, x, x+dx, max_err)
        x = x + dx

    return total_area

def slice_area(function, x1, x2, max_err):
    """ Recursively slices a function given a range and max error.

    This is used by the adaptive trapezoid rule.
    """
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
    """ A function to test with. """
    return 1+x+math.sin(2*x)

