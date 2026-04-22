class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        s = s.lower()
        for i,c in enumerate(s):
            if s[i].isalnum():
                newString = newString + s[i]
        return newString == newString[::-1]
        