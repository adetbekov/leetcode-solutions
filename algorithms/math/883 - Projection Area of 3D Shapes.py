"""
Author:  Adetbekov
Problem: 883. Projection Area of 3D Shapes
Link:    https://leetcode.com/problems/projection-area-of-3d-shapes/description/
"""


class Solution:
    def deep_len(self, lst):
        return sum(self.deep_len(el) if isinstance(el, list) else el != 0 for el in lst)
    
    def projectionArea(self, grid):
        xy = self.deep_len(grid)
        zx = sum([max(x) for x in grid])
        max_x = max([len(x) for x in grid])
        yz = []
        for y in range(max_x):
            temp_xy = []
            for x in grid:
                try:
                    temp_xy.append(x[y])
                except:
                    temp_xy.append(0)
            yz.append(max(temp_xy))
        yz = sum(yz)
        return xy + zx + yz
    