#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
import base
import day7

class Program(object):
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, other):
        self.connections.append(other)

    def connects_to(self, name):
        return self._connects_to(name, set())

    def _connects_to(self, name, seen):
        if self.name == name:
            return True
        else:
            seen.add(self.name)
            for program in self.connections:
                if program.name not in seen:
                    if program._connects_to(name, seen):
                        return True
            return False

class Day(base.Base):
    def parse(self, input):
        input = input.strip()
        result = {}
    
        for line in input.split('\n'):
            tokens = line.split()
            program = int(tokens[0])
            connections = [int(day7.remove_char(t,',')) for t in tokens[2:]]
            result[program] = (Program(program), connections)
        
        for program,connections in result.values():
            for connection in connections:
                program.add_connection(result[connection][0])

        for program in result:
            result[program] = result[program][0]

        return result

    def run(self, programs):
        count = 0
        for program in programs.values():
            if program.connects_to(0):
                count += 1
        return count

if __name__ == '__main__':
    Day(12).main()
