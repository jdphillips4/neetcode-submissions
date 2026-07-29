class Solution:
    def climbStairs(self, n: int) -> int:
        # would be 2^n, but bcome O(n) when only solve 
        # each sub problem once using memoization

        # Bottom up DP approach, start at base case

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one