#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = open('input4.txt').read()

def is_valid(sentence):
    words = sentence.split()
    s = set()
    for word in words:
        if word in s:
            return False
        s.add(word)
    return True

def valid_count(input):
    input_list = [s for s in input.split('\n') if s]
    count = 0
    for sentence in input_list:
        if is_valid(sentence):
            count += 1
    return count

def main():
    new_input = raw_input("> ")
    if new_input:
        print is_valid(new_input)
    else:
        print valid_count(input)

if __name__ == "__main__":
    main()
