'''
problem url:- https://leetcode.com/problems/add-binary/submissions/
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2::]
