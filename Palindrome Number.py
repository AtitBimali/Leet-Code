#Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x==x[::-1]
