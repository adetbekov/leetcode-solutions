"""
Author:  Adetbekov
Problem: 876. Middle of the Linked List
Link:    https://leetcode.com/problems/middle-of-the-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l[(len(l)//2):]
    