#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Virus():
    def __init__(self, grid, initial_coords, inital_direction):
        self.grid = grid
        self.coords = initial_coords
        self.direction = initial_direction
        self.infection_count = 0

    _turn_left = {
        'n' : 'w',
        'w' : 's',
        's' : 'e',
        'e' : 'n'
    }
    
    _turn_right  = {
        'n' : 'w',
        'w' : 's',
        's' : 'e',
        'e' : 'n'
    }
        
    def turn_left(self):
        self.direction = self._turn_left[self.direction]

    def turn_right(self):
        self.direction = self._turn_right[self.direction]

    def burst(self):
        pass

    def burst_times(self, times):
        for __ in range(times):
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
    Day(22).main()
