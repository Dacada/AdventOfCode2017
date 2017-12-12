#!/usr/bin/python
# -*- encoding:utf-8 -*-

import math

input = '368078'

def solve_quadratic_equation(a, b, c):
    """
    Give the two solutions of an equation of the type a*x^2 + b*x + c = 0
    """
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return None
    else:
        numerator = 2*a
        if discriminant == 0:
            return -b/numerator
        else:
            square_root = math.sqrt(discriminant)
            return ( (square_root - b)/numerator , (-b - square_root)/numerator )

def right_result(n):
    if n is not None and type(n) is not int:
        i = int(n[0])
        if (i == n[0]):
            return i - 1
    else:
        return None

def get_ring(coord):
    # n: coord | r: ring
    
    s1 = right_result(solve_quadratic_equation(4, -6, 3 - coord))  # n = 4*r**2 - 6*r + 3
    if s1 is not None:
        return s1
    
    s2 = right_result(solve_quadratic_equation(4, -4, 1 - coord))  # n = 4*r**2 - 4*r + 1
    if s2 is not None:
        return s2
    
    s3 = right_result(solve_quadratic_equation(4, -8, 5 - coord))  # n = 4*r**2 - 8*r + 5
    if s3 is not None:
        return s3
    
    s4 = right_result(solve_quadratic_equation(4, -10, 7 - coord)) # n = 4*r**2 - 10*r + 7
    if s4 is not None:
        return s4

    return None
        
def corner_distance(coord):
    distance_pos = 0
    ring_pos = get_ring(coord)
    while ring_pos is None:
        distance_pos += 1
        ring_pos = get_ring(coord + distance_pos)

    distance_neg = 0
    ring_neg = None
    while ring_neg is None:
        distance_neg += 1
        ring_neg = get_ring(coord - distance_neg)

    if distance_pos <= distance_neg:
        return distance_pos,ring_pos
    else:
        return distance_neg,ring_neg

def run(input):
    """
    6 5 4 3 4 5 6
    5 4 3 2 3 4 5
    4 3 2 1 2 3 4
    3 2 1 0 1 2 3
    4 3 2 1 2 3 4
    5 4 3 2 3 4 5
    6 5 4 3 4 5 6

    Asuming input is not 1 or in a diagonal, the steps are the following:

    1.- Find the closest diagonal by going backwards and forwards and
    finding the minimum distance.

    2.- Get the distance for that diagonal, 2*r where r is the "ring"
    it's at.

    3.- Substract the distance between the input and the diagonal from
    the distance between the diagonal the middle. That's the manhattan
    distance between the input and the middle.
    """
    coord = int(input)

    if coord == 1:
        return 0
    else:
        distance,ring = corner_distance(coord)
        return ring*2 - distance

def main():
    new_input = raw_input('> ')
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
