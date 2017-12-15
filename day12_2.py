#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day12

def run(input):
    programs = day12.parse(input.strip())
    
    count = 0
    seen = set()
    
    for group in programs:
        if group not in seen:
            empty = True
            for program in programs:
                if program not in seen:
                    if programs[program].connects_to(group):
                        seen.add(program)
                        empty = False
            if not empty:
                count += 1
                
    return count
        
day12.run = run

if __name__ == '__main__':
    day12.main()
