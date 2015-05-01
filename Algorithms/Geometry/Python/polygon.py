#!/usr/bin/env python


import sys

class Polygon(object):

    def __init__(self, points):
        """ Create a polygon in the cartesian plane.

        Args:
            points (list of Point): The points making up the polygon
                in the cartesian plane.
        """
        self.points = points

    @property
    def edges(self):
        """ Returns a list of tuples that each contain 2 points of an edge. """
        edge_list = []
        for i,p in enumerate(self.points):
            p1 = p
            p2 = self.points[(i+1) % len(self.points)]
            edge_list.append((p1,p2))

        return edge_list

    def contains(self, point):
        """ Checks if point is inside of polygon.

        Args:
            point (Point): The point to check.

        Returns:
            True if the point is inside the polygon and
            False otherwise.
        """
        # _huge is used to act as infinity if we divide by 0
        _huge = sys.float_info.max
        # _eps is used to make sure points are not on the same line as vertexes
        _eps = 0.00001

        # We start on the outside of the polygon
        inside = False
        for edge in self.edges:
            # Make sure A is the lower point of the edge
            A, B = edge[0], edge[1]
            if A.y > B.y:
                A, B = B, A

            # Make sure point is not at same height as vertex
            if point.y == A.y or point.y == B.y:
                point.y += _eps

            if point.y > B.y or point.y < A.y or point.x > max(A.x, B.x):
                # The horizontal ray does not intersect with the edge
                continue

            if point.x < min(A.x, B.x):
                # The ray intersects with the edge
                inside = not inside
                continue

            try:
                m_edge = (B.y - A.y) / (B.x - A.x)
            except ZeroDivisionError:
                m_edge = _huge

            try:
                m_point = (point.y - A.y) / (point.x - A.x)
            except ZeroDivisionError:
                m_point = _huge

            if m_point >= m_edge:
                # The ray intersects with the edge
                inside = not inside
                continue

        return inside
