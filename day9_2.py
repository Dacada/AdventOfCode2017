#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day9

def run(input):
    assert input[0] == '{' and input[-1] == '}'
    input = input[1:-1]
    
    stack = [[]]
    state = 'read'

    count = 0
    
    for c in input:
        if state == 'read':
            if c == '{':
                stack.append([])
            elif c == '}':
                current_group = stack.pop()
                stack[-1].append(current_group)
            elif c == '<':
                state = 'garbage'
        elif state == 'garbage':
            if c == '>':
                state = 'read'
            elif c == '!':
                state = 'ignore'
            else:
                count += 1
        elif state == 'ignore':
            state = 'garbage'

    return count

day9.run = run

if __name__ == '__main__':
    day9.main()
