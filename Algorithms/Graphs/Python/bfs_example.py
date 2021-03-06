#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath(os.path.join("../../../", os.path.dirname(__file__))))

import Algorithms.Graphs.Python.graph as graph

"""
   3--7
   |
1--2--4--5
      |
      6
"""

if __name__ == "__main__":
    g = graph.Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)

    #TODO add an exception when the input is not
    # a node
    g.add_edge(1,2)
    g.add_edge(2,1)
    g.add_edge(2,3)
    g.add_edge(3,2)
    g.add_edge(2,4)
    g.add_edge(4,2)
    g.add_edge(4,6)
    g.add_edge(6,4)
    g.add_edge(4,5)
    g.add_edge(5,4)
    g.add_edge(7,3)
    g.add_edge(3,7)

    def p(x):
        print x

    g.bfs(2, p)

    print "\n"

    g.dfs(2, p)

    print "\n"
    print "Is connected:", g.is_connected()

    g2 = graph.Graph()
    g2.add_edge(1,2)
    g2.add_edge(2,3)
    g2.add_edge(2,4)
    g2.add_edge(4,5)
    g2.add_edge(-1,1)
    g2.add_edge(6,-1)
    print "g2 Weakly connected:", g2.is_connected()
    print "g2 Strongly connected:", g2.is_strongly_connected()
