class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        mid = len(nums) //2
        #edge cases: flooring problematic, could never reach other mid
        while (l<=r):
            if (nums[mid]==target):
                return mid
            elif (nums[mid]<target):
                l = mid + 1 #we know mid <target, so add 1
                mid = ((r-l) //2) + l
            elif (nums[mid]>target):
                r = mid -1
                mid = ((r-l) //2) + l
        return -1
