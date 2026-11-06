class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fewest coins to make exact amount
        # can do top down subtracting from amount
        # bottom up start at dp[0] go up to dp[amount], 
        # would have to find many combinations that could sum up to it
        # take minimum
        dp = [amount + 1] * (amount + 1) # 0...amount, each set to a max
        dp[0] = 0 # base case
        for amnt in range(1, amount + 1):
            for coin in coins:
            # for each coin we check ways amount - coin
            # can add 1 to that since tracking # ways
                if amnt - coin >= 0: # if coin fits in amount
                    dp[amnt] = min(dp[amnt], 1 + dp[amnt-coin])
                    # starts at a max but then modified for each coin
        if dp[amount] != amount + 1: 
            return dp[amount]
        else:
            return -1
        # O(amount + len coins) time
        # O(amount) space
                        
        
        

