#!/usr/bin/env python

import graph
from graph import Node

"""
   3--7
   |
1--2--4--5
      |
      6
"""

if __name__ == "__main__":
    g = graph.Graph()
    n1 = g.add_node(Node(1))
    n2 = g.add_node(Node(2))
    n3 = g.add_node(Node(3))
    n4 = g.add_node(Node(4))
    n5 = g.add_node(Node(5))
    n6 = g.add_node(Node(6))
    n7 = g.add_node(Node(7))

    #TODO add an exception when the input is not
    # a node
    g.add_edge(n1,n2)
    g.add_edge(n2,n1)
    g.add_edge(n2,n3)
    g.add_edge(n3,n2)
    g.add_edge(n2,n4)
    g.add_edge(n4,n2)
    g.add_edge(n4,n6)
    g.add_edge(n6,n4)
    g.add_edge(n4,n5)
    g.add_edge(n5,n4)
    g.add_edge(n7,n3)
    g.add_edge(n3,n7)

    for n in g.bfs(n2):
        print n

    print "\n"

    for n in g.dfs(n2):
        print n

    print "\n"
    print "Is connected:", g.is_connected()

    g2 = graph.Graph()
    g2.add_edge(1,2)
    g2.add_edge(2,3)
    g2.add_edge(2,4)
    g2.add_edge(4,5)
    g2.add_edge(-1,1)
    g2.add_edge(6,-1)
    print "g2 Strongly connected:", g2.is_connected()
    print "g2 Weakly connected:", g2.is_weakly_connected()
