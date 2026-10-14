class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force:
        # profit = 0
        # for i in range (len(prices)): 
        #     for j in range (i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        # return profit
        
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]: # profitable
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else: # neg profit
                l = r # price at r is small need to slide window
            r += 1 # move r no matter what
        return maxProfit