class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        #brute force check every substring
        #have a fixed length and look for one then move on 
        substring = set()
        l = 0 # left ptr



        for r in range (len(s)):
            while s[r] in substring: # found duplicate
                substring.remove(s[l]) #keep popping this off
                l+=1 #shrink window until no more duplicate   
            substring.add(s[r]) # can add now
            longest_length = max(longest_length, r-l+1)
        
        return longest_length
        