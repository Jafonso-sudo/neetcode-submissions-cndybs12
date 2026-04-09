class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_lowest = prices[0]
        for price in prices:
            profit = max(profit, price - cur_lowest)
            cur_lowest = min(cur_lowest, price)

        return profit
