class Solution:
    def longestPalindrome(self, s: str) -> str:
        # detect palindrome n, check n^2, O(n^3) brute
        # check palindrome: edges in or middle out
        # middle out easier, can choose for it to be dead middle or even middle 
        # character n, expand outwards n so O(n^2)

        res = ""
        resLength= 0

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            while (l>=0 and r<len(s) and s[l] == s[r]):
                if (r-l+1 > resLength):
                    resLength = r-l+1
                    res = s[l:r+1] # end not inclusive, -1 doesnt include last
                l -=1
                r +=1 
            
            # even length
            l, r = i, i+1
            
            while (l>=0 and r<len(s) and s[l] == s[r]):
                if (r-l+1 > resLength):
                    resLength = r-l+1
                    res = s[l:r+1]
                l -=1
                r+=1
        return res