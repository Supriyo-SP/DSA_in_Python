#122. Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0 
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                m += prices[i] - prices[i-1]
        return m
            