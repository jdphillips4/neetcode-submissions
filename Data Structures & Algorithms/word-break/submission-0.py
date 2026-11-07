class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s can be broken into words in worDict
        # return true or false
        # include first char s, expand until find word
        # or for each word in dict look for it
        #max size wordDict < s so more efficient n*m*n

        # tree: start i=0 check each word, recurse on i + len(word)
        # want to get to i = len(s) just out of bounds
        # so base case dp[len(s)] = True
        dp = [False]*(len(s)+1)
        dp[len(s)] = True # base case

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s) and 
                    s[i : i + len(word)] == word):
                    dp[i] = dp[i + len(word)]
                if dp[i] == True:
                    break
        return dp[0]




