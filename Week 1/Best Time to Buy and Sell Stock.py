class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0 #buy
        right = 1 #sell
        maxProfit = 0
        
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, currentProfit)
            else:
                left = right
  
            right += 1
            
        return maxProfit