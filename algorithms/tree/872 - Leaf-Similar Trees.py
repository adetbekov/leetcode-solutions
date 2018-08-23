"""
Author:  Adetbekov
Problem: 872. Leaf-Similar Trees
Link:    https://leetcode.com/problems/leaf-similar-trees/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.t1 = []
        self.t2 = []
        
    def find_leaf(self, node, tree):
        if not node.left and not node.right:
            tree.append(node.val)
        if node.left:
            self.find_leaf(node.left, tree)
        if node.right:
            self.find_leaf(node.right, tree)
        
    def leafSimilar(self, root1, root2):
        self.find_leaf(root1, self.t1)
        self.find_leaf(root2, self.t2)
        return self.t1 == self.t2
        