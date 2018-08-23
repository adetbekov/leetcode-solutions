"""
Author:  Adetbekov
Problem: 561. Array Partition I
Link:    https://leetcode.com/problems/array-partition-i/description/
"""


class Solution:
    def arrayPairSum(self, nums):
        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i+1])
        return result

class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
        