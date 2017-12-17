#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = open("input16.txt").read()

class Programs(object):
    def __init__(self, starting_positions):
        self.length = 0
        
        self._name_from_position = {}
        self._position_from_name = {}
        
        for i,name in enumerate(starting_positions):
            self._name_from_position[i] = name
            self._position_from_name[name] = i
            self.length += 1

    def dance(self, move):
        if move[0] == 's':
            self.spin(int(move[1:]))
        elif move[0] == 'x':
            n1,n2 = move[1:].split('/')
            self.exchange(int(n1), int(n2))
        elif move[0] == 'p':
            n1,n2 = move[1:].split('/')
            self.partner(n1, n2)
            
    def spin(self, amount):
        new_name_from_position = {}
        new_position_from_name = {}
        
        for pos in self._name_from_position:
            if pos < (self.length - amount):
                new_pos = pos + amount
            else:
                new_pos = pos - (self.length - amount)
                
            name = self._name_from_position[pos]
            
            new_name_from_position[new_pos] = name
            new_position_from_name[name] = new_pos

        self._name_from_position = new_name_from_position
        self._position_from_name = new_position_from_name
        
    def exchange(self, pos1, pos2):
        name1 = self._name_from_position[pos1]
        name2 = self._name_from_position[pos2]
        self._swap(name1, name2, pos1, pos2)

    def partner(self, name1, name2):
        pos1 = self._position_from_name[name1]
        pos2 = self._position_from_name[name2]
        self._swap(name1, name2, pos1, pos2)

    def _swap(self, name1, name2, pos1, pos2):
        self._name_from_position[pos1] = name2
        self._name_from_position[pos2] = name1
        self._position_from_name[name1] = pos2
        self._position_from_name[name2] = pos1

    def _get_list(self):
        return [i[1] for i in sorted((item for item in self._name_from_position.items()), key=lambda i: i[0])]

    def __str__(self):
        return ''.join(self._get_list())

def run(input):
    movements = input.strip().split(',')
    programs = Programs(chr(ord('a') + i) for i in range(16))

    for move in movements:
        programs.dance(move)

    return str(programs)

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
