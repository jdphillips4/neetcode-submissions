class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours to eat bananas
        # piles[i] = num bananas in ith pile
        # return minimum rate k to eat all banas in h hours
        # if pile <k bananas finish eating pile but cant move on

        # Can you always only eat from one pile on a turn? Yes it seems

        # if h == len(piles): return max pile size
        # higher h gets smaller k can be

        # sort piles to know max
        # range of k from 1 to max pile size, can use h as heurstic to estimate
        # BST on possible k values

        l, r = 1, max(piles)
        min_k = r
        
        while (l <= r):
            k = (l + r) // 2
            
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
                
            if hours > h: # k is too small, move left better range
                l =  k + 1
            elif hours <= h: # k is valid but need to find smallest
                min_k = k
                r = k - 1
                
        return min_k

        # stopping condition if k-1 doesnt work found minimum, 
        # or just track minimum

        # had right idea just didnt implement BS correctly
        # use l r ptrs


