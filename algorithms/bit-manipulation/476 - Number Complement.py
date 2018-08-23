"""
Author:  Adetbekov
Problem: 476. Number Complement
Link:    https://leetcode.com/problems/number-complement/description/
"""


class Solution:
    def findComplement(self, num):
        # bin(0) = 0..000000
        # ~bin(0) = -1 or 1..111111
        mask = ~0
        
        # 1..111111 & 0..000101 = 0..000101 which is not Zero(0..000000)
        while mask & num:
            # mask << 1 = 1..111110
            # mask << 2 = 1..111100
            # mask << 1 = 1..111000
            mask <<= 1
        # 1..111000 & 0..000101 = 0..000000 is Zero, then break loop
        
        # ~1..111000 = 0..000111 and ~0..000101 = 1..111010
        # 0..000111 & 1..111010 = 0..000010 = 010
        return ~mask & ~num