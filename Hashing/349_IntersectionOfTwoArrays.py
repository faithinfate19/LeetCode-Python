#349. Intersection of Two Arrays
"""
Given two integer arrays nums1 and nums2, return an array of their .
Each element in the result must be unique and you may return the result in any order.
"""
class Solution:
    @staticmethod
    def intersection(nums1, nums2):
        seen = {}
        result = []

        for num in nums1:
            seen[num] = True

        for num in nums2:
            if num in seen:
                result.append(num)
                del seen[num]

        return result
