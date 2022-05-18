'''
problem url :- https://leetcode.com/problems/minimum-moves-to-equal-array-elements/submissions/
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (min(nums)*len(nums))
