#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys
import day7

input = open('input12.txt').read()

class Program(object):
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, other):
        self.connections.append(other)

    def connects_to(self, name):
        return self._connects_to(name, set())

    def _connects_to(self, name, seen):
        print name
        if self.name == name:
            return True
        else:
            seen.add(self.name)
            for program in self.connections:
                if program not in seen:
                    if program._connects_to(name, seen):
                        return True
            return False

def parse(input):
    result = {}
    
    for line in input.split('\n'):
        tokens = line.split()
        program = int(tokens[0])
        connections = [day7.remove_char(t,',') for t in tokens[2:]]
        result[program] = (Program(program), connections)
        
    for program,connections in result.values():
        for connection in connections:
            program.add_connection(result[program.name][0])

    for program in result:
        result[program] = result[program][0]
            
    return result

def run(input):
    programs = parse(input.strip())
    count = 0
    for program in programs.values():
        if program.connects_to(0):
            count += 1
    return count

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()
    
    if new_input:
        run(new_input)
    else:
        run(input)

if __name__ == '__main__':
    main()
