"""
Author:  Adetbekov
Problem: 728. Self Dividing Numbers
Link:    https://leetcode.com/problems/self-dividing-numbers/description/
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for digit in range(left, right + 1):
            inner_digits = map(int, list(str(digit)))
            validness = [inner_digit != 0 and digit % inner_digit == 0 for inner_digit in inner_digits]
            if all(validness):
                result.append(digit)
        return result
    