class Solution:
    def hammingWeight(self, n: int) -> int:
        # optimized: use n = n & (n - 1)
        # when subtract 1 gets rid of a bit, 
        # when anding, rest of number is the same
        # any ones to right wont matter and cancel out

        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res