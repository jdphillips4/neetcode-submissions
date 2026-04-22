class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            new = s
            if (s == '+'):
                new = stack.pop() + stack.pop()
            elif (s == '-'):
                a, b = stack.pop(), stack.pop()
                new = b-a
            elif (s == '*'):
                new = stack.pop() * stack.pop()
            elif (s == '/'):
                a, b = stack.pop(), stack.pop()
                new = b / a
            stack.append(int(new))

        return stack.pop()
