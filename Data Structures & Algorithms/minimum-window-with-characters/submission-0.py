class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # every char in t should be in smalles sub of s
        # smallest possible would be size of t 
        # like previous problem except doesnt have to be exact

        # make hashmap of t detecting freqs of chars
        # sliding window starts at size of t

        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t: # frequencies of chars in t
            countT[c] = 1 + countT.get(c, 0) # returns 0 if doesnt exist
        
        have = 0 # 0 of chars we need
        need = len(countT) # need all unique chars
        
        l = 0
        res = [-1,-1]
        resLen = float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have +=1 # found a char
            
            while have == need:
                # update our result
                if (r - l + 1) < resLen: # size of current window < resLen upda
                    res = [l, r]
                    resLen = (r - l + 1)
                # keep shrinking to make it as small
                # pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # if by removing character made it less tahn needed
                    have -= 1
                l+=1
        # extract result into l and r
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        