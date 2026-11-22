class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[v] = i
        return