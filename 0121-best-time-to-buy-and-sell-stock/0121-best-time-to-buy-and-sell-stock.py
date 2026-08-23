class Solution:
    def maxProfit(self, p: List[int]) -> int:
        min_profit = p[0]
        max_profit = 0
        for i in range(1,len(p)):
            min_profit = min(p[i],min_profit)
            profit = p[i] - min_profit
            max_profit = max(max_profit, profit)

        return max_profit