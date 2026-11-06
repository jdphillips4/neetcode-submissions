class Solution:
    def rob(self, nums: List[int]) -> int:
        # same but now 1st and last 0 and len(nums) - 1 are adjacent
        # if select first cant include last and vice versa is new

        # run hr1 on all but first and again on on but last

        def hr1(nums):
            rob1 = 0
            rob2 = 0
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
    # edge case of only 1 would be nums[0]
    # in strings start at 0 arbitrary and len(nums) arbitrary end
        return max(nums[0], hr1(nums[:-1]), hr1(nums[1:]))