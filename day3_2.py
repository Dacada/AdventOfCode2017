#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day3

class Spiral(object):
    def __init__(self, size):
        self.size = size
        self._reserved = [[0]*self.size for __ in xrange(self.size)]

    def set(self, x, y, item):
        self._reserved[self.size/2+y][self.size/2+x] = item

    def get(self, x, y):
        return self._reserved[self.size/2+y][self.size/2+x]

    def run(self, until):
        x = 0
        y = 0

        xdir = +1
        ydir = 0
        
        prev_xdir = +1
        prev_ydir = +1

        count = 1

        while True:
            for i in range(2):
                for c in range(count):
                    x += xdir
                    y += ydir
                    total = self.get(x,y+1)
                    total += self.get(x,y-1)
                    total += self.get(x+1,y)
                    total += self.get(x-1,y)
                    total += self.get(x+1,y-1)
                    total += self.get(x-1,y+1)
                    total += self.get(x+1,y+1)
                    total += self.get(x-1,y-1)
                    self.set(x,y,total)
                    if total > until:
                        return total
                    
                if xdir == 0:
                    xdir = prev_xdir * (-1)
                    prev_ydir = ydir
                    ydir = 0
                else:
                    ydir = prev_ydir * (-1)
                    prev_xdir = xdir
                    xdir = 0

            count += 1

def run(input):
    spiral = Spiral(100)
    spiral.set(0,0,1)
    return spiral.run(int(input))

day3.run = run

if __name__ == '__main__':
    day3.main()
