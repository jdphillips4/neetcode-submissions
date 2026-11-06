class Solution:
    def numDecodings(self, s: str) -> int:
        # number of ways = dp
        # can include 1 or 2 digits if valid

        cache = {len(s) : 1}

        def dp(i):
            if i in cache:
                return cache[i]
            # A goes to 1 so cant have single 0s
            if s[i] == "0":
                return 0
            
            #only looking for number of decodings
            res = dp(i + 1)
            # if in bounds and starts w 1 or (2 and then 0-6)
            if (i + 1 < len(s) and (s[i] == "1" 
                or s[i] == "2" and s[i+1] in "0123456")):
                res += dp(i + 2)
            cache[i] = res
            return res
        
        return dp(0)