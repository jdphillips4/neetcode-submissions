class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # list all combinations = backtracking
        # all combos sum to target, can be target, can use same num

        # pop if go over target

        #choice: include this number?
        # return if subset sums to target

        res = []

        def dfs(i, subset, total):
            #base case: return if tot sums to target
            if total == target:
                res.append(subset.copy()) 
                return
            
            if total > target or i>= len(nums):
                return

            #choice to use nums[i] again
            subset.append(nums[i])
            total += nums[i]
            dfs(i, subset, total)

            popped = subset.pop()
            total -= popped
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return res

        # O(2^height tree)

        # I got the choices for the tree right
        # needed 2nd base case at top instead of in choice logic
        # needed to use subset and total in the dfs instead of global




