class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is cost of stepping, can go 1 or 2 ahead
        # want to minimize(prefer pay 1 since both allow same steps)

        # base start at i=0 or 1
        # at each step can choose to move forward 1 or 2
        n = len(cost)
        if n<= 1:
            return cost[n]

        dp = [0] * n

        dp[0] = cost[0] # cost to be in these states
        dp[1] = cost[1]
        

        # minimizing cost, distance doesnt matter
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        
        # goes until end of array so dp[i] or dp[i-1] should be the correct output since its the cost to be in that state
        return min(dp[n-1], dp[n-2])
        # did this wout solution nice
