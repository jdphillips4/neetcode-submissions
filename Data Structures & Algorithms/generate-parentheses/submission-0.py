class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n=1: ()
        # n=2: ()(), (())
        # cant start with closed )
        # need n open n closed
        # only add closed if closed< open
        stack = [] # hold parnetheses
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN +1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0)
        return res