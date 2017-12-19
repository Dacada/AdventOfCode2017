#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = 'input19.txt'

class Router(object):
    class __init__(self, grid):
        self._grid = [[cell for cell in row] for row in grid.split('\n')]
        self.letters = ""
        x = self._grid[0].index('|')
        self.coords = (x,0)
        self._direction = 's'
        self._direction_meanings = {
            'n' : ( 0,-1),
            's' : ( 0, 1),
            'e' : (-1, 0),
            'w' : ( 1, 0)
        }

    def traverse(self):
        next = self.next_direction()
        while next is not None:
            self.advance(next)
            next = self.next_direction,()

    def next_direction(self):
        

def run(input):
    router = Router(open(input).read().strip())
    router.traverse()
    return router.letters

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
