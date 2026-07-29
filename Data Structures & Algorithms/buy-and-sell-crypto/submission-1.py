class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        while sell <= len(prices) - 1:
            if prices[buy] < prices[sell]:
                current_profit = prices[sell] - prices[buy]
                if current_profit > max_profit:
                    max_profit = current_profit
                else:
                    sell += 1
            else:
                sell += 1
                buy = sell-1
        return max_profit