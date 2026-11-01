class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l and r ptrs, if l < r return l
        # if start on opposite ends when 

        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r: 
            if nums[l] < nums[r]:
                return min(nums[l], res)
            
            mid = (r + l) // 2
            res = min(res, nums[mid])

            if (nums[mid] >= nums[l]):
                l = mid + 1
            else: #in right sorted portion so want to searchto the left
                r = mid - 1 

        return res