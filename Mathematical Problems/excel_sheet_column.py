'''
Problem Url :- https://leetcode.com/problems/excel-sheet-column-title/
'''
class Solution:
    def getstring(self,val):
        return chr(val+64)
    def convertToTitle(self, n: int) -> str:
        res = ""
        while(n>0):
            val = n%26
            if val == 0:
                val = 26
            res+= self.getstring(val)
            if n%26 == 0:
                n//=26
                n-=1
            else:
                n//=26
        return res[::-1]
