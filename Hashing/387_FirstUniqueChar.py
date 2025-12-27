"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s):
        seen = {}
        for char in s:
            seen[char] = seen.get(char , 0) + 1

        for k,v in seen.items():
            if v == 1:
                return s.index(k)
        return -1