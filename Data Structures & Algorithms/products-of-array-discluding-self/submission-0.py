class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force: O(n^2) loop through multiplying all but i to get total 
        #finding product then dividing doesnt work because 0 ruins product
        # store prefix and suffix arrays to do less work
        # to optimize storage to pass to store prefixes then do pass to multiply postfixes in result
        n = len(nums)
        res = [0]*n
        prefix = [0]*n # use identity to start
        suffix = [0]*n # end with 1, prepend rest
        prefix[0] = 1
        suffix[n-1] = 1

        for i in range (1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range (n-2, -1, -1): #start,end,increment
            suffix[i] = suffix[i+1] * nums[i+1] # prepend
        
        for i in range (n):
            res[i] = (prefix[i]*suffix[i])
        
        return res

            
        
        
        #brute force:
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             product = product * nums[j]
        #     res.append(product)
        # return res