class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bui=prices[0]
        profit=0
        for i in prices:
            if i < bui:
                bui=i
            else:
                profit = max(profit,i-bui)
        return profit
        
