class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxLength = 0
        #can just do set(nums)
        # for num in nums: 
        #     if num not in hashset: 
        #         hashset.add(num)
        
        
        for num in hashset: 
            if num - 1 not in hashset: 
                length = 1
                while num + length in hashset:
                    length +=1
                maxLength = max(length, maxLength)
        return maxLength


        
        
        
        
        
        # #nlogn sort then loop through, can do better
        # maxSeq = 0
        # count = 1 #should start at 1 since each find only adds 1
        # nums = sorted(nums)
        # # this approach doesnt work because there can be duplicates that reset the count
        # for i in range(len(nums)-1): 
        #     if nums[i]+1 == nums[i+1]:
        #         count = count + 1
        #     else: 
        #         maxSeq = max(maxSeq, count)
        #         count = 1
        #     maxSeq = max(maxSeq, count)
        # return maxSeq