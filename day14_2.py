#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day10_2
import day14

class Cell(object):
    def __init__(self, coords):
        self.neighbors = []
        self.coords = coords
    def neighbor(self, other):
        self.neighbors.append(other)
    def connects_to(self, other):
        return self._connects_to(other, set())
    def _connects_to(self, other, seen):
        if self is other:
            return True
        else:
            seen.add(self)
            for cell in self.neighbors:
                if cell not in seen:
                    if cell._connects_to(other, seen):
                        return True
            return False
    def __hash__(self):
        return hash(self.coords)

class Memory(object):
    def __init__(self, bits):
        self._cells = {}
        for y in range(128):
            for x in range(128):
                if bits[y][x] == '1':
                    self._cells[(x,y)] = Cell((x,y))

    def link_up(self):
        for coord,cell in self._cells.items():
            up_coord = (coord[0], coord[1] - 1) if coord[1] - 1 >= 0 else None
            down_coord = (coord[0], coord[1] + 1) if coord[1] + 1 < 128 else None
            left_coord = (coord[0] - 1, coord[1]) if coord[0] - 1 >= 0 else None
            right_coord = (coord[0] + 1, coord[1]) if coord[0] + 1 < 128 else None

            if up_coord in self._cells:
                cell.neighbor(self._cells[up_coord])
            if down_coord in self._cells:
                cell.neighbor(self._cells[down_coord])
            if left_coord in self._cells:
                cell.neighbor(self._cells[left_coord])
            if right_coord in self._cells:
                cell.neighbor(self._cells[right_coord])

    def count_regions(self):
        seen = set()
        count = 0
        for coord,cell in self._cells.items():
            if coord not in seen:
                empty = True
                for coord2,cell2 in self._cells.items():
                    if coord2 not in seen:
                        if cell.connects_to(cell2):
                            seen.add(coord2)
                            empty = False
                if not empty:
                    count += 1

        return count

class Day(day14.Day):
    def run(self, input):
        day = day10_2.Day(14)
        bits = []
    
        for i in range(128):
            hash_input = input + '-' + str(i)
            hash = day.run(day.parse(hash_input))
            bits.append([b for b in bin(int('1'+hash,16))[3:]])
            day.list = [__ for __ in range(256)]
        
        memory = Memory(bits)
        memory.link_up()
        return memory.count_regions()

if __name__ == '__main__':
    Day(14).main()
