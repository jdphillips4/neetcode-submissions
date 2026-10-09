class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sum to 0, all unique sets
        # sort then keep leftmost unique (skip duplicates)
        # remainder of problem is 2sum for the complement
        # since sorted, use l r ptr and move window based on sum > or < 

        res = [] # list of lists
        nums = sorted(nums) # O(nlogn)
        for i in range (len(nums)):
            if i>0 and nums[i] == nums[i - 1]: #repeat value
                continue

            l = i+1 
            r = len(nums) -1 # last index
        
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0: # needs to be bigger
                    l +=1
                elif threeSum > 0: # smaller
                    r -=1
                else: # sum ==0 append
                    res.append([nums[i], nums[l], nums[r]])
                    #update one ptr
                    l +=1 
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
