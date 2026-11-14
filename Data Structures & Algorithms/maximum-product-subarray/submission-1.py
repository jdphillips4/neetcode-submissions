class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # subarray is contiguous
        # subarray largest product
        # bf would check every subarray n^3
        # pre and suffix product

        # contiguous could be dp
        # 2, 4, -3
        # if all positive product incresing
        # all negatives alternates, can track max and min to allow maximization 
        # ignore 0s, reset to 1 
        # its a product so want to include alot

        res = max(nums) 
        current_max = 1
        current_min = 1

        for n in nums:
            if n == 0:
                current_max = 1
                current_min = 1
                continue
            
            # n*max, n*min, n*1
            tmp = current_max*n
            current_max = max(n*current_max, n*current_min, n)
            current_min = min(tmp, n*current_min, n)
            res = max(res, current_max) # need to save bc curmax could go down
        return res
