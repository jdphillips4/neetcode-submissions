class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            # sorting is nlogn
            # if not len(s)  == len(t):
            #     return False
            # return sorted(s) == sorted(t)
            

            # hashmap solution O(n+m), O(1) space
            if len(s) != len(t):
                return False

            #hashmap = set(s) # set doesnt have freqs
            freqs = {}
            for c in s:
                freqs[c] = freqs.get(c, 0) + 1

            for c in t:
                if c not in freqs:
                    return False
                
                freqs[c] -= 1
                
                if freqs[c] < 0:
                    return False

            return True
        # even easier just make 2 hashmaps and add each element then 
        # check if equal