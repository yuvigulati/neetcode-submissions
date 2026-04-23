class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        profit = 0
        while j < len(prices) :
            temp_profit = 0
            if prices[i] >= prices[j]:
                i = j  
                j += 1  
            else:       
                temp_profit = prices[j] - prices[i]
                profit = max(temp_profit, profit)
                j += 1

        return profit 
