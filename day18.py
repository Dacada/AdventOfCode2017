#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys

input = open("input18.txt").read()

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()

    if new_input:
        run(new_input)
    else:
        run(input)

if __name__ == "__main__":
    main()
