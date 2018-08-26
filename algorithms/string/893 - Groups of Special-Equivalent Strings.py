"""
Author:  Adetbekov
Problem: 893. Groups of Special-Equivalent Strings
Link:    https://leetcode.com/problems/groups-of-special-equivalent-strings/description/
"""


import collections


class Solution:
    def numSpecialEquivGroups(self, A):
        d = collections.defaultdict(int)
        for w in A:
            even = ''.join(sorted(w[0::2]))
            odd = ''.join(sorted(w[1::2]))
            d[(even, odd)] += 1
            
        return len(d)