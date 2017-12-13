#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = open("input9.txt").read().strip()

def parse(input):
    assert input[0] == '{' and input[-1] == '}'
    input = input[1:-1]
    
    stack = [[]]
    state = 'read'
    
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
        elif state == 'ignore':
            state = 'garbage'

    return stack.pop()

def score(group, acc):
    return 1 + acc + sum(score(g, acc+1) for g in group)

def run(input):
    groups = parse(input)
    return score(groups, 0)

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == "__main__":
    main()
