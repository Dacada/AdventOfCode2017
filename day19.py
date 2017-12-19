#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = 'input19.txt'

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
