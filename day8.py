#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class RegisterBank(object):
    def __init__(self):
        self._registers = {}

    def get(self, register_name):
        if register_name not in self._registers:
            self._registers[register_name] = 0
        return self._registers[register_name]

    def set(self, register_name, value):
        self._registers[register_name] = value

    def max(self):
        return max(self._registers.values())

class Instruction(object):
    def __init__(self, line):
        tokens = line.split()
        self.register_name = tokens[0]
        self.action = tokens[1]
        self.action_value = int(tokens[2])
        self.condition_name = tokens[4]
        self.condition_type = tokens[5]
        self.condition_value = int(tokens[6])
        
    def run(self, register_bank):
        condition_value = register_bank.get(self.condition_name)
        if self.condition_type == '>':
            condition = condition_value > self.condition_value
        if self.condition_type == '<':
            condition = condition_value < self.condition_value
        if self.condition_type == '>=':
            condition = condition_value >= self.condition_value
        if self.condition_type == '<=':
            condition = condition_value <= self.condition_value
        if self.condition_type == '!=':
            condition = condition_value != self.condition_value
        if self.condition_type == '==':
            condition = condition_value == self.condition_value

        if condition:
            current_value = register_bank.get(self.register_name)
            if (self.action == 'inc'):
                current_value += self.action_value
            else:
                current_value -= self.action_value
            register_bank.set(self.register_name, current_value)

class Day(base.Base):
    def parse(self, input):
        program = []
        for line in input.split('\n'):
            if line:
                program.append(Instruction(line))
        return program

    def run(self, program):
        register_bank = RegisterBank()
        for instruction in program:
            instruction.run(register_bank)
        return register_bank.max()

if __name__ == '__main__':
    Day(8).main()
