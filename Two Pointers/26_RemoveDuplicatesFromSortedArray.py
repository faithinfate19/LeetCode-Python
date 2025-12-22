#26.Remove Duplicates From Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.
"""


class Solution:
    @staticmethod
    def removeDuplicates(nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


"""
nums = [1, 1, 2, 2, 3]

k = 1
i = 1
[1, 1, 2, 2, 3]
 ^  ^

i=1: nums[1] == nums[0] → skip
i=2: nums[2] != nums[0] → write nums[2] to nums[1]

so array now looks like: [1 , 2 , 2 , 2 ,3 ]

i=3: nums[3] == nums[1] → skip
i=4: nums[4] != nums[1] → write nums[4] to nums[2]

so array now looks like: [1 , 2 , 3 , 2 ,3 ]
k = 3


Leet only checks for the first 3 elements
"""