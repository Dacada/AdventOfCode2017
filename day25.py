#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Tape():
    def __init__(self):
        self._tape = {}

    def get(self, i):
        return self._tape.get(i, 0)

    def set(self, i, value):
        self._tape[i] = value

    def count(self, num):
        return len([v for v in self._tape.values() if v == num])

class Rules():
    def __init__(self, rules):
        self.rules = rules

    def advance(self, value, state):
        return self.rules[state][value]

class TuringMachine():
    def __init__(self, tape, cursor, states, initial_state):
        self.tape = tape
        self.cursor = cursor
        self.states = states
        self.state = initial_state

    def run(self, steps):
        for __ in range(steps):
            """
            print('state:',self.state)
            print('value:',self.tape.get(self.cursor))
            print('cursor:',self.cursor)
            input()
            """
            new_value,direction,new_state = self.states.advance(self.tape.get(self.cursor), self.state)
            
            self.tape.set(self.cursor, new_value)
            
            if direction == 'l':
                self.cursor -= 1
            elif direction == 'r':
                self.cursor += 1
                
            self.state = new_state

    def diagnostic_checksum(self):
        return self.tape.count(1)

class Day(base.Base):
    def parse(self, input):
        """
        Sure, I'll parse this.
        """
        lines = input.split('\n')
        
        initial_state = lines[0].split()[-1][:-1]
        steps = int(lines[1].split()[-2])

        rules = {}
        for line in lines[2:]:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("In state"):
                state = line.split()[-1][:-1]
                rules[state] = {}
            elif line.startswith("If the current value is"):
                cond_value = int(line.split()[-1][:-1])
                rules[state][cond_value] = []
            elif line.startswith("- Write"):
                write_value = int(line.split()[-1][:-1])
                rules[state][cond_value].append(write_value)
            elif line.startswith("- Move one"):
                direction = line.split()[-1][0]
                rules[state][cond_value].append(direction)
            elif line.startswith("- Continue with"):
                next_state = line.split()[-1][0]
                rules[state][cond_value].append(next_state)
            else:
                raise Exception("Unexpected line: " + line)

        r = Rules(rules)
        machine = TuringMachine(Tape(), 0, r, initial_state)
        
        return (machine, steps)
        
    def run(self, input):
        machine,steps = input
        machine.run(steps)
        return machine.diagnostic_checksum()

if __name__ == '__main__':
    Day(25).main()
