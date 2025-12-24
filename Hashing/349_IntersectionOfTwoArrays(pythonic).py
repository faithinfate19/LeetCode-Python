#349.Intersection of Two Arrays

"""
Given two integer arrays nums1 and nums2, return an array of their .
Each element in the result must be unique and you may return the result in any order.
"""

#PYTHONINC VERSION:
class Solution:
    def intersection(self, nums1, nums2):
        set3 = set(nums1).intersection(set(nums2))
        set3 = list(set3)
        return set3

