#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = '367'

def run(input):
    steps = int(input)
    
    buff = [0]
    current_position = 0

    for n in range(1,2018):
        # we need to add 1 before inserting because list.insert inserts
        # before the given index, not after
        current_position = (current_position + steps + 1) % len(buff)
        buff.insert(current_position, n)

    return buff[buff.index(2017)+1]

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
