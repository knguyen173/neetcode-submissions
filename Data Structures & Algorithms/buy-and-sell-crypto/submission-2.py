class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy = 0
        sell = 1
        profit = -1

        while sell < len(prices):
            if prices[sell] - prices[buy] > profit:
                print(profit)
                profit = prices[sell] - prices[buy]
            elif prices[buy] > prices[sell]:
                buy = sell
            sell += 1
            
        return max(profit, 0)