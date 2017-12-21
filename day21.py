#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import math
import base

def empty_matrix(side):
    return [[None]*side for __ in range(side)]

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
    if len(matrix) == 2:
        r[0][0] = matrix[0][1]
        r[0][1] = matrix[0][0]
        r[1][0] = matrix[1][1]
        r[1][1] = matrix[1][0]
    elif len(matrix) == 3:
        r[0][0] = matrix[0][2]
        r[0][1] = matrix[0][1]
        r[0][2] = matrix[0][0]
        r[1][0] = matrix[1][2]
        r[1][1] = matrix[1][1]
        r[1][2] = matrix[1][0]
        r[2][0] = matrix[2][2]
        r[2][1] = matrix[2][1]
        r[2][2] = matrix[2][0]
    return r
    
def vflip(matrix):
    r = empty_matrix(len(matrix))
    if len(matrix) == 2:
        r[0][0] = matrix[1][0]
        r[0][1] = matrix[1][1]
        r[1][0] = matrix[0][0]
        r[1][1] = matrix[0][1]
    elif len(matrix) == 3:
        r[0][0] = matrix[2][0]
        r[0][1] = matrix[2][1]
        r[0][2] = matrix[2][2]
        r[1][0] = matrix[1][0]
        r[1][1] = matrix[1][1]
        r[1][2] = matrix[1][2]
        r[2][0] = matrix[0][0]
        r[2][1] = matrix[0][1]
        r[2][2] = matrix[0][2]
    return r

def div_in_2(matrix):
    return div_in_N(matrix, 2)
def div_in_3(matrix):
    return div_in_N(matrix, 3)

def div_in_N(matrix, n):
    result = {}
    k=0
    for i in range(len(matrix)//n):
        for j in range(len(matrix)//n):
            result[k] = [l[j*n:j*n+n] for l in matrix[i*n:i*n+n]]
            k+=1
    return result

def lists_to_tuples(matrix):
    return tuple([tuple(l) for l in matrix])

def rejoin(quadrants):
    m = max(quadrants.keys())+1
    side = int(math.sqrt(m))
    in_side = len(quadrants[0])

    result = []
    for i in range(side*in_side):
        result.append([])
        for j in range(i//in_side*side, i//in_side*side+side):
            result[i] += quadrants[j][i%in_side]
            #print("result["+str(i)+"] += quadrants["+str(j)+"]["+str(i%in_side)+"]")
  
    #print(quadrants)
    #print(result)
    #input()
    return result

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

class Rule():
    def __init__(self, pattern, result):
        self._match = set()
        for p in flip_and_turn(pattern):
            self._match.add(lists_to_tuples(p))
        self._result = result

    def match(self, pattern):
        if lists_to_tuples(pattern) in self._match:
            return self._result
        else:
            return None

class Art():
    def __init__(self, start):
        self._image = to_grid(start)
        self._rules = []

    def rule(self, pattern, grid):
        self._rules.append(Rule(to_grid(pattern), to_grid(grid)))

    def size(self):
        return len(self._image)

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

    def __str__(self):
        return '\n'.join('.'.join(l) for l in self._image)

class Day(base.Base):
    def parse(self, input):
        art = Art('.#./..#/###')
        for enhancement in input.split('\n'):
            if enhancement:
                s = enhancement.split('=>')
                art.rule(s[0].strip(), s[1].strip())
        return art
        
    def run(self, art):
        for __ in range(5):
            art.improve()
        return count_char(str(art), '#')

if __name__ == '__main__':
    Day(21).main()
