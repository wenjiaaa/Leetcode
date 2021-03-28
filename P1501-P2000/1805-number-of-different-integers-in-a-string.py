# https://leetcode.com/problems/number-of-different-integers-in-a-string/
from typing import List


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(len(word)):
            if word[i].isalpha():
                word = word.replace(word[i], " ")
        word_list = word.split()
        res = []
        for word in word_list:
            if int(word) not in res:
                res.append(int(word))
        return len(res)
