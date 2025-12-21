"""Given an array of integers nums which is sorted in ascending order,"""
"""and an integer target, write a function to search target in nums."""
"""If target exists, then return its index. Otherwise, return -1."""

"""You must write an algorithm with O(log n) runtime complexity."""

class Solution(object):
    @staticmethod
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid =( low + high ) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid -1
        return -1