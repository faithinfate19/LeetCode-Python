#1. Two Sum
"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""


def twoSum(nums, target):
    numsWithIndex = [(num, i) for i, num in enumerate(nums)]
    numsWithIndex.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        num_sum = numsWithIndex[left][0] + numsWithIndex[right][0]
        if num_sum == target:
            return [numsWithIndex[left][1], numsWithIndex[right][1]]
        elif num_sum < target:
            left += 1
        else:
            right -= 1
    return []