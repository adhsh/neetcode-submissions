class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                new_profit = prices[r] - prices[l]
                if new_profit > 0 and new_profit > profit:
                    profit = new_profit
            else:
                l =r
            r += 1
        return profit