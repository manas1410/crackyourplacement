'''
problem url :-https://leetcode.com/problems/move-zeroes/submissions/
apprach:- firstly move all the elements except zero to the front and then fill left palces to zeroes
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[n]=nums[i]
                n+=1
        for i in range(n,len(nums)):
            nums[i]=0
