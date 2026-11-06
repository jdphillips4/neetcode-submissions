class Solution:
    def countSubstrings(self, s: str) -> int:
        # could use 2 ptr, dp
        # same code as before, palindromes contain many palindromes
        # 2 ptr best, dp would be 2d
       
        res = 0 
        

        # treat each char as center:
        for i in range(len(s)):
            # odds
            l, r = i, i
            while(l>=0 and r<len(s) and s[l] == s[r]):
                res +=1 
                l -=1
                r +=1
            
            # evens
            l, r = i, i+1
            while(l>=0 and r<len(s) and s[l] == s[r]):
                res +=1
                l -=1
                r +=1
        
        return res
            

            



