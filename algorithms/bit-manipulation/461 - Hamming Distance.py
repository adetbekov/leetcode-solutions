"""
Author:  Adetbekov
Problem: 461. Hamming Distance
Link:    https://leetcode.com/problems/hamming-distance/description/
"""


class Solution:
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')
    