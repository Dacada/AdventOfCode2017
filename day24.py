#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import itertools
import copy
import base

class Node():
    _get_id = itertools.count().__next__
    
    def __init__(self, port1, port2):
        self.port1 = port1
        self.port2 = port2
        self.value = port1 + port2
        self.id = self._get_id()
        
    def __hash__(self):
        return hash(self.id * self.value)

    def __str__(self):
        return '{0}/{1}'.format(self.port1,self.port2)

    __repr__ = __str__

class Bridge():
    def __init__(self, start):
        self.nodes = set((start,))
        self.port = start.port1 if start.port1 != 0 else start.port2
        self.value = start.value

    def append_if_possible(self, node):
        """
        Try to append node to bridge, return new copy of bridge with node
        if successful, otherwise return None.
        """
        if node in self.nodes:
            return None

        newbridge = copy.copy(self)
        newbridge.nodes = copy.copy(newbridge.nodes)
        
        if self.port == node.port1:
            newbridge.port = node.port2
        elif self.port == node.port2:
            newbridge.port = node.port1
        else:
            return None
        
        newbridge.nodes.add(node)
        newbridge.value += node.value
        return newbridge

    def __str__(self):
        return ' -- '.join(str(n) for n in self.nodes)

    __repr__ = __str__

class Day(base.Base):
    def parse(self, input):
        pieces_by_port = {}
        for piece in input.split('\n'):
            if piece:
                p1,p2 = piece.split('/')
                p1 = int(p1)
                p2 = int(p2)
                n = Node(p1,p2)
                pieces_by_port.setdefault(p1,[]).append(n)
                pieces_by_port.setdefault(p2,[]).append(n)
        return pieces_by_port
        
    def run(self, pieces_by_port):
        max = 0
        bridges = []
        for piece in pieces_by_port[0]:
            bridges.append(Bridge(piece))
        while bridges:
            #print(bridges)
            #input()
            newbridges = []
            for bridge in bridges:
                if bridge.value > max:
                    max = bridge.value
                for piece in pieces_by_port[bridge.port]:
                    newbridge = bridge.append_if_possible(piece)
                    if newbridge is not None:
                        newbridges.append(newbridge)
            bridges = newbridges
        return max
            
if __name__ == '__main__':
    Day(24).main()
