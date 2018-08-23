"""
Author:  Adetbekov
Problem: 867. Transpose Matrix
Link:    https://leetcode.com/problems/transpose-matrix/description/
"""


class Solution:
    def transpose(self, A):
        return list(zip(*A))
    