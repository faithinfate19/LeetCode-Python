#977. Squares of a Sorted Array

"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    @staticmethod
    def sortedSquares(nums):
        res = []
        for i in range(len(nums)):
            sqr = nums[i] * nums[i]
            res.append(sqr)

        res.sort()
        return res