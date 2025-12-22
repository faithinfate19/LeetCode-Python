#34. Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchRange(self, nums, target):

        def findfirst():
            low, high = 0, len(nums) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return first

        def findlast():
            low, high = 0, len(nums) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return last

        return [findfirst(), findlast()]
