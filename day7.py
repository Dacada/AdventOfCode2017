#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def remove_char(s, c):
    while c in s:
        s = s[:s.index(c)] + s[s.index(c)+1:]
    return s

class Day(base.Base):
    def parse(self, input):
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

    def run(self, input):
        programs = set(input.keys())
        not_bottom_programs = set(sum((v[0] for v in input.values()), ()))
        return programs.difference(not_bottom_programs).pop()

if __name__ == '__main__':
    Day(7).main()
