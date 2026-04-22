class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store val:index in hashmap {key:val, ...}
        hashmap = {}
        #check if target-value in hashmap, else add it

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[diff], index]
            #else add to hashmap
            hashmap[value] = index
        return #just in case