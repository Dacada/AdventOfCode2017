#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day11

def run(input):
    directions = input.split(',')
    xdir = 0
    ydir = 0

    maxdist = 0

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

        distance = day11.distance(xdir, ydir)
        if distance > maxdist:
            maxdist = distance
            
    return maxdist
    
day11.run = run

if __name__ == '__main__':
    day11.main()
