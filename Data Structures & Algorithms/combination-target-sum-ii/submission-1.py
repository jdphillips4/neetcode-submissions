class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # can only choose once this time but list now had dups
        # base case: append when total = target
        # stop branch if go over
        # choices include this element or not
        res = []
        candidates.sort() #nlogn
        
        def dfs(i, subset, total):
            #base case
            if(total == target):
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # choices
            # use i move on
            subset.append(candidates[i])
            total += candidates[i]
            dfs(i+1, subset, total)

            # dont use i move on
            # fails because can move on but still be the same

            popped = subset.pop()
            total -= popped
            #fix duplicates by checking
            while(i+1 < len(candidates) 
                and candidates[i] == candidates[i+1]):
                i += 1
            
            dfs(i+1, subset, total)
        
        dfs(0, [], 0)
        return res

        # just needed to think of edge case of duplicates
        # also to sort candidates before to make that work
