#!/usr/bin/env python

import nose
import unittest

from Algorithms.Geometry.Python.polygon import Polygon
from Algorithms.Geometry.Python.point import Point


class TestPolygon(unittest.TestCase):

    def test_polygon_contains_point(self):
        p = Point(0, 0)
        poly = Polygon([Point(1, 1),
                        Point(-1, 1),
                        Point(-1, -1),
                        Point(1, -1)])
        self.assertTrue(poly.contains(p))

    def test_point_outside_polygon(self):
        p = Point(200, 50)
        poly = Polygon([Point(20, 10),
                        Point(50, 125),
                        Point(125, 90),
                        Point(150, 10)])
        self.assertFalse(poly.contains(p))

    def test_point_same_height_as_vertex(self):
        p = Point(35, 90)
        poly = Polygon([Point(20, 10),
                        Point(50, 125),
                        Point(125, 90),
                        Point(150, 10)])
        self.assertFalse(poly.contains(p))

    def test_point_on_bottom_line(self):
        p = Point(50, 10)
        poly = Polygon([Point(20, 10),
                        Point(50, 125),
                        Point(125, 90),
                        Point(150, 10)])
        self.assertTrue(poly.contains(p))


if __name__ == "__main__":
    nose.run(argv=["--tests=", __file__, "--verbosity=2"])
