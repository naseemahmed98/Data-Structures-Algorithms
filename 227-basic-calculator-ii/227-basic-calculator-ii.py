class Solution:
    def calculate(self, s):
        
        numbers = set("0123456789")
        s = "0+%s+" % s.replace(" ", "")
        op, val, stack = "+", 0, deque()
        
        ops = {}
        ops["+"] = lambda x: x
        ops["-"] = lambda x: -x
        ops["*"] = lambda x: x * stack.pop()
        ops["/"] = lambda x: int(1.0 * stack.pop() / x)
        
        for c in s:
            if c in numbers:
                val = 10 * val + int(c)
            else:
                stack.append(ops[op](val))
                op, val = c, 0
                
        return sum(stack)