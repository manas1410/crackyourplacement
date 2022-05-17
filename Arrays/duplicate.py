'''
Problem url: https://leetcode.com/problems/find-the-duplicate-number/
'''
#Naive Approach
def findDuplicate(self, nums: List[int]) -> int:
  d = {}
  for i in range(len(nums)):
      try:
          d[nums[i]]+=1
          if d[nums[i]]>=1:
              break
      except:
          d[nums[i]] = 1
  return nums[i]

#Turtoise and hare method
def findDuplicate(self, nums: List[int]) -> int:
  slow = nums[0]
  fast = nums[0]
  while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if slow == fast:
          break
  fast = nums[0]
  while slow!=fast:
      slow = nums[slow]
      fast = nums[fast]
  return slow
