class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # different lengths? yes any location? yes
        
        # always will include all elements 
        # look for complements
        # could go after possible sums (targets)
        # set of all possible targets

        # actually there is only one possibility sum/2 
        #

        if sum(nums) %2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2 # starting target

        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                # for each num adding t to it an caching that as a possible sum
                nextDP.add(t + nums[i]) 
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False