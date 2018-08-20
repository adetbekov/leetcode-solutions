"""
Author:  Adetbekov
Problem: 832. Flipping an Image
Link:    https://leetcode.com/problems/flipping-an-image/description/
"""


class Solution:
    def flipAndInvertImage(self, A):
        return [[i^1 for i in r[::-1]] for r in A]
    