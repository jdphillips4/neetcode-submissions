class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR: a^a=0, a^0 = a all would cancel except one
        res = 0
        for num in nums:
            res = num ^ res
        return res