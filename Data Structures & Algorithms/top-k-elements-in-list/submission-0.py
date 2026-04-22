class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap num,freq then switch to freq, num and link collisions
        #O(klogn) better solution: instead of sorting add to max heap and pop k times
        

        #even better O(n) Bucket Sort: array of vals. only useful if bounded
        #Doesnt work: make array from 0 to max element in nums so accessing is instantaneous
        #trick: index is frequency/count so bounded by size nums, have list for values
        counts = {} #hashmap 
        freqs = [[] for i in range(len(nums)+1)] # array of arrays, index = frequency, array of vals with that freq
        # iterate nums and store num, frequency in hashmap
        for num in nums:
            counts[num] = 1 + counts.get(num, 0) #counts[num] +=1
        # move from hashmap to array
        for num, count in counts.items():
            freqs[count].append(num)

        output = []
        #output k elements starting from back. i represents count of each value
        for i in range(len(freqs)-1, 0, -1): #last index, until 0, decrement by 1 each time
            for val in freqs[i]:
                output.append(val)
                if len(output) == k:
                    return output
        return


        # #naive solution
        # #store num, frequency
        # freqs = {}
        # for i in nums:
        #     if i in freqs:
        #         freqs[i] += 1
        #     else:
        #         freqs[i] = 1
        #     #can be done as freqs[i] = 1 + freqs.get(i, 0) 
        #     #0 is whats returned when nothing there

        # #sort worst case: nlogn
        # array = []

        # #output
        # output = []
        # for i in range(k):
        #     output.append(array[i])
        # return output


        