class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                maxP = max(p, maxP)
            else:
                l = r
            r += 1
        return maxP