class Solution(object):
    def maxProfit(self, prices):
        min=prices[0]
        profit=0
        for i in prices:
            if i < min:
                min=i
            cur_profit=i-min
            if cur_profit>profit:
                profit=cur_profit
        return profit
            
        