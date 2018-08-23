"""
Author:  Adetbekov
Problem: 852. Peak Index in a Mountain Array
Link:    https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""


class Solution:
    def peakIndexInMountainArray(self, A):
        return A.index(max(A))
        