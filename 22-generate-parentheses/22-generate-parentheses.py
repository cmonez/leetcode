class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        
        
        def backtrack(openParens, closedParens):
            if openParens == closedParens == n:
                res.append("".join(stack))
                return
            if openParens < n:
                stack.append("(")
                backtrack(openParens+1, closedParens)
                stack.pop()
            if closedParens < openParens:
                stack.append(")")
                backtrack(openParens, closedParens + 1)
                stack.pop()
        backtrack(0, 0)
        return res
        