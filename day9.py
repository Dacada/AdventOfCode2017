#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = open("input9.txt").read()

def parse(input):
    assert input[0] == '{' and input[-1] == '}'
    input = input[1:-1]
    
    stack = [[]]
    
    for c in input:
        if c == '{':
            stack.append([])
        else if c == '}':
            stack[-1].append(stack.pop())

    return stack.pop()

def run(input):
    groups = parse(input)
    return score(groups)

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == "__main__":
    main()
