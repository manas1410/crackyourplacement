'''
Problem Url:- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                max_profit+= (prices[i+1]-prices[i])
        return max_profit
