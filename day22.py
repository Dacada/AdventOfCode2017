#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class InfiniteGrid():
    def __init__(self, initial): # Asume initial is a square
        self._grid = {}
        zero = len(initial)//2+1
        for y,row in enumerate(initial):
            for x,cell in enumerate(row):
                self._grid[(x-zero,y-zero)] = cell

    def get(self, coords):
        return self._grid.get(coords, '.')

    def set(self, coords, val):
        self._grid[coords] = val

    def getstr(self, size, mark):
        offset = size//2-1
        s = [[' . ']*size for __ in range(size)]
        for coord,cell in self._grid.items():
            if coord == mark:
                cell = '['+cell+']'
            else:
                cell = ' '+cell+' '
                
            x,y = coord
            x += offset
            y += offset
            
            if x < size and y < size:
                s[y][x] = cell

        return '\n'.join(''.join(l) for l in s)

class Virus():
    def __init__(self, grid, initial_coords, initial_direction):
        self.grid = grid
        self.coords = initial_coords
        self.direction = initial_direction
        self.infection_count = 0
        self._current_node = grid.get(initial_coords)

    _turn_left = {
        'n' : 'w',
        'w' : 's',
        's' : 'e',
        'e' : 'n'
    }
    
    _turn_right  = {
        'n' : 'e',
        'e' : 's',
        's' : 'w',
        'w' : 'n'
    }

    _advance = {
        'n' : (+1, 0),
        's' : (-1, 0),
        'w' : (0, -1),
        'e' : (0, +1)
    }
        
    def turn_left(self):
        self.direction = self._turn_left[self.direction]

    def turn_right(self):
        self.direction = self._turn_right[self.direction]

    def advance(self):
        add_coords = self._advance[self.direction]
        self.coords = (self.coords[0]+add_coords[0], self.coords[1]+add_coords[1])
        self._current_node = self.grid.get(self.coords)

    def burst(self):
        if self._current_node == '#':
            self.turn_right()
            self._current_node = '.'
        else:
            self.turn_left()
            self._current_node = '#'
            self.infection_count += 1
        self.grid.set(self.coords, self._current_node)
        self.advance()

    def burst_times(self, times):
        for __ in range(times):
            print(self.grid.getstr(11,self.coords))
            input()
            self.burst()

class Day(base.Base):
    def parse(self, input):
        grid = InfiniteGrid([[c for c in row if c] for row in input.split('\n') if row])
        virus = Virus(grid, (0,0), 'n')
        return virus        
        
    def run(self, virus):
        virus.burst_times(10000)
        return virus.infection_count

if __name__ == '__main__':
    Day(22, test=True).main()
