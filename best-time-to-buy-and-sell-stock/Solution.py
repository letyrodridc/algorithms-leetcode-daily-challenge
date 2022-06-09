class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        n = len(prices)
        
        profits = [0]*n
        buyprice = prices[0]
        
        for i in range(1,n):
            profits[i] = max(profits[i-1], max(0,prices[i]-buyprice))
            
            if prices[i] < buyprice:
                buyprice = prices[i]
                
        return profits[n-1]
        