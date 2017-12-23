#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day18
import base
import operator

class Program(day18.Program):
    def __init__(self, instructions):
        super(Program, self).__init__(instructions)
        self.mul_count = 0
        
    def _sub(self, x, y):
        self._operation(x, y, operator.sub)
        
    def _mul(self, x, y):
        self.mul_count += 1
        self._operation(x, y, operator.mul)
        
    def _jmp(self, x): # general jump instruction, unnecesary but nice to have
        val = self._get_value(x)
        self.program_counter += val - 1
        
    def _jgz(self, x, y): # wouldn't be able to sleep knowing I implement an unnecessary jump instruction that doesn't use my unnecesary general jump instruction
        val = self._get_value(x)
        if val > 0:
            self._jmp(y)
            
    def _jnz(self, x, y):
        val = self._get_value(x)
        if val != 0:
            self._jmp(y)

class Day(base.Base):
    def parse(self, input):
        return Program(day18.to_lists(input.strip()))
        
    def run(self, program):
        program.run()
        return program.mul_count

if __name__ == '__main__':
    Day(23).main()
