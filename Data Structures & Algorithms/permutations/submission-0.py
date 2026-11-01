class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, already_picked):
            #base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if not already_picked[i]:
                    path.append(nums[i])
                    already_picked[i] = True
                
                    dfs(path, already_picked)
                    path.pop()
                    already_picked[i] = False

        already_picked = [False] * len(nums)
        dfs([], already_picked)
        return res

 # my initial allowed repeats of samenumber instead of w/out replacement