class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        cur_lowest = 100
        for price in prices:
            profit = max(profit, price - cur_lowest)
            cur_lowest = min(cur_lowest, price)

        return profit
