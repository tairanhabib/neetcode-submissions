class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max = 0

        for i in range(len(prices)): 
            for next_price in prices[i:]:
                if next_price - prices[i] > max:
                    max = next_price - prices[i]

        return max

        

        