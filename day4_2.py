#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day4

class Day(day4.Day):
    def is_anagram(self, word1, word2):
        return ''.join(sorted(word1)) == ''.join(sorted(word2))

    def is_valid(self, sentence):
        words = sentence.split()
        for i in range(len(words)):
            for j in range(len(words)):
                if (i != j):
                    if self.is_anagram(words[i], words[j]):
                        return False
        return True

if __name__ == '__main__':
    Day(4).main()
