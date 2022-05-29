'''
Problem Url:- https://leetcode.com/problems/missing-number
'''
'''
Using Gaus Formula
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)+1))//2 - sum(nums)
      
'''
Using O(N) space
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = [0]*(len(nums)+1)
        for i in range(len(nums)):
            l[nums[i]] = 1
        for i in range(len(l)):
            if l[i]==0:
                return i
            
