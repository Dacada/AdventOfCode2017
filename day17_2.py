#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = '367'

def run(input):
    """
    Asuming the value after 0 will always be the first one
    (0 always ends up at the end)
    """
    steps = int(input)
    current_position = 0
    solution = None

    for n in range(1,50000000+1): 
        current_position = (current_position + steps + 1) % n
        if current_position == 0:
            solution = n

    return solution

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
