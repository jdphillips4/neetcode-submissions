class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if permutation of s1 in (even substring) s2 return true 

        # hashmap of s1 then sliding window to find it in s2
        # would have to delete values as go so need master hash to reset
        # compare them once, then track matches as go

        # window size len(s1), track freq of chars in window
        # return true if freqs match s1
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26 # a-z
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # counts of each char s1
            s2Count[ord(s2[i]) - ord('a')] += 1 # create initial window
        
        # initial number of matches
        matches = 0
        for i in range(26): 
            if s1Count[i] == s2Count[i]:
                matches += 1

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # right ptr stuff
            index = ord(s2[r]) - ord('a') # ascii to index
            s2Count[index] += 1 #increment freq
            # update matches
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -=1
                
            #left ptr stuff
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 #leave behind left value
            if s1Count[index] == s2Count[index]:
                matches +=1 # left ptr now matches
            elif s1Count[index] -1 == s2Count[index]:
                matches -=1 # case where weve left a match behind
            l += 1
        return matches == 26

        
            