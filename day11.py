#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = open('input11.txt').read().strip()

def distance(x, y):
    moveXY = abs(x)
    moveY = (abs(y) - moveXY) / 2
    return moveXY + moveY

def run(input):
    directions = input.split(',')
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

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
