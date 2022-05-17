'''
Problem url:- https://leetcode.com/problems/sort-colors/submissions/
'''
'''
swapping the elements and bringing the 0 first and 1 second and 2 third
'''
def sortColors(self, nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  v = 0
  l = 0 
  for i in range(3):
      j=0
      while(j<len(nums)):
          if nums[j]==l:
              nums[j],nums[v] = nums[v],nums[j]
              v+=1 
          j+=1
      l+=1
