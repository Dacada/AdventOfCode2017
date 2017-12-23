#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def distance(x, y):
    moveXY = abs(x)
    moveY = (abs(y) - moveXY) // 2
    return moveXY + moveY

class Day(base.Base):
    def parse(self, input):
        return input.strip().split(',')
    
    def run(self, directions):
        xdir = 0
        ydir = 0

        for dir in directions:
            if dir == "n":
                ydir += 2
            elif dir == "ne":
                xdir += 1
                ydir += 1
            elif dir == "se":
                xdir += 1
                ydir -= 1
            elif dir == "s":
                ydir -= 2
            elif dir == "sw":
                xdir -= 1
                ydir -= 1
            elif dir == "nw":
                xdir -= 1
                ydir += 1

        return distance(xdir, ydir)

if __name__ == '__main__':
    Day(11).main()
