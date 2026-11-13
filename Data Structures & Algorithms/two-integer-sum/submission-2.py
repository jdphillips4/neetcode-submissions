class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, val in enumerate(nums):
            comp = target - val
            if comp in hashMap:
                return [hashMap[comp], i] # i,j
            hashMap[val] = i
        return