"""
Author:  Adetbekov
Problem: 557. Reverse Words in a String III
Link:    https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""


class Solution:
    def reverseWords(self, s):
        return " ".join(map(lambda x: x[::-1], s.split()))
        