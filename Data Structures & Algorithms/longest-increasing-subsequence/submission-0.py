class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # increasing, in order but can ignore some, find longest
        # brute force: include this or not 2^n
        # decisions: start index i, try decision after i+1 to len
        # next must be > last of current subsequence
        # start at end
        N = len(nums)
        dp = [1]* N
        #dp[N - 1] = 1 # base case at end 
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j]) # ignore or include it
        
        return max(dp)