class Solution:
    def rob(self, nums: List[int]) -> int:
        # if choose i, cant choose i+1 or i-1
        # every other might not always be efficient
        # want to choose max of every 3 basically but then depends  
        # return total

        # when you start at the end you decide if you want to include n or n-1, and you do that based on the previous ones
         # is there a case you wouldnt go every other?

         # [100, 0, 1, 100] yes here you can get both 100s if you gloss over middle 2, not sure

    # start 1st skip 2nd then choose rest of array
    # or start 2nd skip 3rd then rest of array

    # rob = max(nums[0] + max(nums[2:n]), nums[1] + max(3:n))
    # maintain last 2 values could rob from
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2) # include n or not best total
            rob1 = rob2
            rob2 = temp
        
        return rob2
    # [100, 0, 1, 100]
    # i=0: r1 = 0, r2 = 100
    # i=1: r1 = 100, r2 = 100
    # i =2: r1 = 100, r2 = 101
    # i = 3: r1 = 101, r2 = 200
