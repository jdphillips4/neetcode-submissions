class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window containing one character and k others

        # find longest consecutive chars with <= k others

        # find heighest frequency char replace nearby chars
        # hashmap of counts
        # windowlength - count of most frequent char <= k
        # update longest to max windowlength
        # result only changes when max frequency increases O(n)
        longest_string = 0
        counts = {} # hashmap of counts
        l= 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0) # increment counts

            while (r-l+1) - max(counts.values()) > k: #invalid
                counts[s[l]] -= 1
                l += 1 #shift l ptr

            longest_string = max(longest_string, r-l+1)

        return longest_string