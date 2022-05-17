class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = math.inf
        maxProfit = 0
        for idx, price in enumerate(prices):
            if price < minVal:
                minVal = price
            elif price - minVal > maxProfit:
                maxProfit = price - minVal
        return maxProfit