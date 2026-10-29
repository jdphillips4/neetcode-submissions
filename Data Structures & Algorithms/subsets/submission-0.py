class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #"all possible" subsets nums = backtracking
        # no duplicates

        #what defines a subset? 
        # always empty set

        # when creating tree how to avoid duplicates? 

        # each element have choice: include or dont include
        res = []

        subset = []
        def dfs(i):
            # Base Case, if i out of bounds
            if i>= len(nums):
                res.append(subset.copy())
                return

            # choice to include nums[i] (left branch)
            subset.append(nums[i])
            dfs(i+1) # has subset given to it
            
            # choice to exclude nums[i]
            subset.pop()
            dfs(i+1) # has empty subset given to it
        
        dfs(0)
        return res
