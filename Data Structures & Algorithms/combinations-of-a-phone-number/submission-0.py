class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # map each digit to what it could be
        # backtrack with a for loop and do every combo
        # O(n * 4^n) if all 9s
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # recursive call
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
        
        if digits:
                dfs(0, "")
        return res