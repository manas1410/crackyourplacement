'''
problem url:- https://leetcode.com/problems/integer-to-roman/
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i = 0
        while(num!=0):
            while(num>=nums[i]):
                num-=nums[i]
                res+=romans[i]
            i+=1
        return res
