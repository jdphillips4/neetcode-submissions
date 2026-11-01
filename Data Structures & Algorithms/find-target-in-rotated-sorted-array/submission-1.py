class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #bs while also accounting for if l > or < r
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (l + r) // 2
            if target == nums[m]: 
                return m

            # in left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]: # move to right
                    l = m + 1
                else: # in that left section
                    r = m - 1
            else: # in right sorted portion
                if target < nums[m] or target > nums[r]: # move to left
                    r = m -1 
                else: # in right portion
                    l = m + 1
        return -1
        # my og approach had to many cases, easy way to organize is
        # if in left sorted check this else in right sorted do this
