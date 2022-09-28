class Solution(object):
    def generateParenthesis(self, n):
        stack, res = [],[]
        
        def backTracking(openN,closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return 
            if openN < n:
                stack.append('(')
                backTracking(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backTracking(openN,closedN+1)
                stack.pop()
        
        backTracking(0,0)
        return res