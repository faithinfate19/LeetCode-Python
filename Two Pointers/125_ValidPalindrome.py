#125. Valid Palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lcs = s.lower()
        lcs = re.sub(r'[^a-zA-Z0-9]', '', lcs)
        if lcs == lcs[::-1]:
            return True
        else:
            return False