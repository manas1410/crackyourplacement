'''
Problem url - https://leetcode.com/problems/two-sum/solution/
'''
#Brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] ==target:
                    ans.append(i)
                    ans.append(j)
            if len(ans)>0:
                break
        return ans
      
#using one pass hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[nums[i]] = i
            
