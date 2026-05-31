class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1
        max_profit = 0
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit)
            if profit < 0:
                buy_day = sell_day
                sell_day += 1
            else:
                sell_day += 1

        return max_profit