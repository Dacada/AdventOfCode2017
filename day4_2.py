#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day4

def is_anagram(word1, word2):
    return ''.join(sorted(word1)) == ''.join(sorted(word2))

def is_valid(sentence):
    words = sentence.split()
    for i in range(len(words)):
        for j in range(len(words)):
            if (i != j):
                if is_anagram(words[i], words[j]):
                    return False
    return True

day4.is_valid = is_valid

if __name__ == '__main__':
    day4.main()
