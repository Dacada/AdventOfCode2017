#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def empty_matrix(side):
    return [[None]*side for __ in side]

def to_grid(s):
    return [[c for c in line if c] for line in s.split('/') if line]

def flip_and_turn(grid):
    for __ in range(4):
        grid = turn90(grid)
        yield grid
        yield hflip(grid)
        yield vflip(grid)

def turn90(matrix):
    """
    abc    cfi
    def => beh
    ghi    adg

    ab    bd
    cd => ac
    """
    r = empty_matrix(len(matrix))
    
    if len(matrix) == 2: #I'm
        r[0][0] = matrix[0][1]
        r[0][1] = matrix[1][1]
        r[1][0] = matrix[0][0]
        r[1][1] = matrix[1][0]
    elif len(matrix) == 3: #Lazy
        r[0][0] = matrix[0][2]
        r[0][1] = matrix[1][2]
        r[0][2] = matrix[2][2]
        r[1][0] = matrix[0][1]
        r[1][1] = matrix[1][1]
        r[1][2] = matrix[2][1]
        r[2][0] = matrix[0][0]
        r[2][1] = matrix[1][0]
        r[2][2] = matrix[2][0]
    # And thinking is hard
    
    return r

def hflip(matrix):
    r = empty_matrix(len(matrix))
    for i in range(len(matrix)):
        r[i][i] = matrix[i][len(matrix) - 1 - i]
    return r

def vflip(matrix):
    r = empty_matrix(len(matrix))
    for i in range(len(matrix)):
        r[i][i] = matrix[len(matrix) - 1 - i][i]
    return r

def div_in_2(matrix):
    result = {}
    

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
