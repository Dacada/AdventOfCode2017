#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
import operator
import base
import day8

class EndProgram(Exception):
    pass

class Program(object):
    def __init__(self, instructions):
        self._registers = day8.RegisterBank()
        self.instructions = instructions
        self.program_counter = 0
        self.last_snd = None

    def run(self):
        while True:
            try:
                instr = self.instructions[self.program_counter]
            except IndexError:
                break

            try:
                getattr(self, '_'+instr[0])(*instr[1:])
            except EndProgram:
                break
            
            self.program_counter += 1

    def _snd(self, x):
        val = self._get_value(x)
        self.last_snd = val
        
    def _set(self, x, y):
        val = self._get_value(y)
        self._registers.set(x, val)

    def _add(self, x, y):
        self._operation(x, y, operator.add)

    def _mul(self, x, y):
        self._operation(x, y, operator.mul)

    def _mod(self, x, y):
        self._operation(x, y, operator.mod)

    def _rcv(self, x):
        val = self._get_value(x)
        if val != 0:
            raise EndProgram

    def _jgz(self, x, y):
        valx = self._get_value(x)
        if valx > 0:
            valy = self._get_value(y)
            self.program_counter += valy - 1

    def _get_value(self, n):
        try:
            return int(n)
        except ValueError:
            return self._registers.get(n)

    def _operation(self, x, y, op):
        valy = self._get_value(y)
        valx = self._registers.get(x)
        result = op(valx, valy)
        self._registers.set(x, result)

def to_lists(input):
    return [instr.split() for instr in input.split('\n')]

class Day(base.Base):
    def parse(self, input):
        return Program(to_lists(input))

    def run(self, program):
        program.run()
        return program.last_snd

if __name__ == "__main__":
    Day(18).main()
