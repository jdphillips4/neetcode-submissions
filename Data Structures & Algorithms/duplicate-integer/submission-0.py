class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #go through list adding to hash set and immediately 
         #when finds duplicate return true else false
        hashset = set()
        for num in nums: 
            if (num in hashset): return True
            hashset.add(num)
        return False