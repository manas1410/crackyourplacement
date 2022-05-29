'''
Probelm url :- https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n = len(str(x))
        for i in range(n//2):
            if str(x)[i]!=str(x)[n-1-i]:
                return False
        return True
