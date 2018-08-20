"""
Author:  Adetbekov
Problem: 657. Judge Route Circle
Link:    https://leetcode.com/problems/judge-route-circle/description/
"""


class Solution:
    def judgeCircle(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')
    