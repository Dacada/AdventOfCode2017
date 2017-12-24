#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day24

class Day(day24.Day):
    def run(self, pieces_by_port):
        bridges = []
        for piece in pieces_by_port[0]:
            bridges.append(day24.Bridge(piece))
        while bridges:
            m = max(([b.value for b in bridges]))
            #input()
            newbridges = []
            for bridge in bridges:
                for piece in pieces_by_port[bridge.port]:
                    newbridge = bridge.append_if_possible(piece)
                    if newbridge is not None:
                        newbridges.append(newbridge)
            bridges = newbridges
        return m

if __name__ == '__main__':
    Day(24).main()
