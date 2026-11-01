class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # all possible = backtracking
        # no dups in solution, nums may have dups
        nums.sort()
        res = []
        subset = []
        def backtrack(i):
            # return case
            if i>= len(nums):
                res.append(subset.copy())
                return
            
            #choices: include i or not, avoid dups
            # to avoid dups need to account for using same one while also being able to use multiple when possible

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            # all subset that dont include nums[i]
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res


            
