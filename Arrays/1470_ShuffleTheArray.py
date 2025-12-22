#1470. Shuffle the array

"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0
        j = n

        while i < n:
            res.append(nums[i])
            res.append(nums[j])

            i += 1
            j += 1

        return res