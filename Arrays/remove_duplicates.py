'''
Problem Url:- https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
'''
'''
Approach:-
bring all the integer to the front like
0011122334 --> 0123422334
then pop from the lasat index of the integer
'''
def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=1
        while(j<len(nums)):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i+=1
            j+=1
        for k in range(i,len(nums)):
            nums.pop()
        return i+1
