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
        if self.ahead(self._direction) == ' ':
            dir = self.turn_left(self._direction)
            if self.ahead(dir) == ' ':
                dir = self.turn_right(self._direction)
                if self.ahead(dir) == ' ':
                    return None
                else:
                    return dir
            else:
                return dir
        else:
            return self._direction

    def ahead(self, direction):
        newcoords = self._sum_coords(self.coords, self._direction_meanings[direction])
        return self._char_at(newcoords)

    def turn_left(self, direction):
        if direction == 'n':
            return 'w'
        elif direction == 'w':
            return 's'
        elif direction == 's':
            return 'e'
        else:
            return 'n'

    def turn_right(self, direction):
        if direction == 'n':
            return 'e'
        elif direction == 'e':
            return 's'
        elif direction == 's':
            return 'w'
        else:
            return 'n'

    def _sum_coords(self, coord1, coord2):
        return (coord1[0] + coord2[0], coord1[1] + coord2[1])

    def _char_at(self, coord):
        return self._grid[coord[1]][coord[0]]

def run(input):
    router = Router(open(input).read())
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
