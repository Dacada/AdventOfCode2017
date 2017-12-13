#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys

input = open('input7.txt').read()

def remove_char(s, c):
    while c in s:
        s = s[:s.index(c)] + s[s.index(c)+1:]
    return s

def parse_input(input):
    result = {}
    
    for line in input.split('\n'):
        if line:
            tokens = line.split()
            name = tokens[0]
            weight = tokens[1][1:-1]
            if len(tokens) > 2:
                on_top = tuple([remove_char(s,',') for s in tokens[3:]])
            else:
                on_top = ()
            result[name] = (on_top, weight)
        
    return result

def run(input):
    parsed = parse_input(input)
    programs = set(parsed.keys())
    not_bottom_programs = set(sum((v[0] for v in parsed.values()), ()))
    return programs.difference(not_bottom_programs).pop()

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()
    
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
