#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day16

def permutate(programs, changes):
    """
    programs is a string of length n
    changes is a list of integers of length n
    for each index i in changes, put programs[i] into index changes[i]
    return the resulting string
    """
    r = [c for c in programs]
    for i,j in enumerate(changes):
        programs[i] = r[j]

def run(input):
    movements = input.strip().split(',')
    original = [chr(ord('a') + i) for i in range(16)]
    programs = day16.Programs(original)
    
    for move in movements:
        programs.dance(move)
    current_state = [c for c in str(programs)]
    changes = [int(ord(n) - ord('a')) for n in current_state]

    # Huh. Turns out the thing repeats.
    # After n dances they're back at their original position.
    
    dances = 1
    programs = day16.Programs(current_state)
    original_str = ''.join(original)
    while True:
        for move in movements:
            programs.dance(move)
        dances += 1
        if str(programs) == original_str:
            break
    
    # Therefore they'll be in the same position after a billion dances
    # as in after a billion % dances dances.

    programs = day16.Programs(original)
    for i in xrange(1000000000 % dances):
        for move in movements:
            programs.dance(move)

    return str(programs)
    
day16.run = run

if __name__ == '__main__':
    day16.main()
