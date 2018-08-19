"""
Author:  Adetbekov
Problem: 771. Jewels and Stones
Link:    https://leetcode.com/problems/jewels-and-stones/description/
"""


import re

# Array greedy search
class Solution:
    def numJewelsInStones(self, J, S):
        return sum([s in set(J) for s in S])
    
# Regular expression
class Solution:
    def numJewelsInStones(self, J, S):
        return len(re.findall("|".join(J), S))
   