class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        boughtPrice = 0
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                boughtPrice = prices[i]
                continue
            if prices[i] < boughtPrice:
                boughtPrice = prices[i]
            else:
                if prices[i] - boughtPrice > profit:
                    profit = prices[i] - boughtPrice
        return profit