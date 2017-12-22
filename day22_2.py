#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day22

class Virus(day22.Virus):
    def turn_around(self):
        self.turn_left()
        self.turn_left()
    def burst(self):
        if self._current_node == '.':
            self.turn_left()
            self._current_node = 'W'
            self.infection_count += 1
        elif self._current_node == 'W':
            self._current_node = '#'
        elif self._current_node == '#':
            self.turn_right()
            self._current_node = 'F'
        elif self._current_node == 'F':
            self.turn_around()
            self._current_node = '.'
        self.grid.set(self.coords, self._current_node)
        self.advance()

class Day(day22.Day):
    def parse(self, input):
        grid = day22.InfiniteGrid([[c for c in row if c] for row in input.split('\n') if row])
        virus = Virus(grid, (0,0), 'n')
        return virus
        
    def run(self, virus):
        virus.burst_times(100)
        return virus.infection_count

if __name__ == '__main__':
    Day(22, True).main()
