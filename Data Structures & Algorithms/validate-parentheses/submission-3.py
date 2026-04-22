class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: 
            if c == '{' or c=='(' or c=='[':
                stack.append(c)
            if len(stack) == 0:
                return False
            if c == '}':
                if not stack.pop() == '{':
                    return False
            if c == ')':
                if not stack.pop() == '(':
                    return False
            if c == ']':
                if not stack.pop() == '[':
                    return False
        if not (len(stack) == 0):
            return False
        return True
        