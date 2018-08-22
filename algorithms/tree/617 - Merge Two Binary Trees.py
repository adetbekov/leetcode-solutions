"""
Author:  Adetbekov
Problem: 617. Merge Two Binary Trees
Link:    https://leetcode.com/problems/merge-two-binary-trees/description/
Method:  Recursion
"""


class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    