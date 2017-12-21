#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def to_grid(s):
    return [[c for c in line if c] for line in s.split('/') if line]

def flip_and_turn(grid):
    for __ in range(4):
        grid = turn90(grid)
        yield grid
        yield hflip(grid)
        yield vflip(grid)

def turn90(matrix):
    

class Rule():
    def __init__(self, pattern, result):
        self._match = set()
        for p in flip_and_turn(pattern):
            self._match.add(p)
        self._result = result

    def match(self, pattern):
        if pattern in self._match:
            return result
        else:
            return None

class Art():
    def __init__(self, start):
        self._image = to_grid(start)
        self._rules = []

    def rule(self, pattern, grid):
        self._rules.append(Rule(to_grid(pattern), to_grid(grid)))

    def improve(self):
        if self.size() % 2 == 0:
            quadrants = div_in_2(self._image)
        elif self.size() % 3 == 0:
            quadrants = div_in_3(self._image)
        else:
            raise Exception("Something went wrong...")

        for q in quadrants:
            for rule in self._rules:
                match = rule.match(quadrants[q])
                if match is not None:
                    quadrants[q] = match
                    break

        self._image = rejoin(quadrants)

class Day(base.Base):
    def parse(self, input):
        art = Art('.#./..#/###')
        for enhancment in input.split('\n'):
            s = enhancement.split('=>')
            art.rule(s[0].strip(), s[1].strip())
        return art
        
    def run(self, art):
        for __ in range(5):
            art.improve()
        return count_char(str(art), '#')

if __name__ == '__main__':
    Day(21).main()
