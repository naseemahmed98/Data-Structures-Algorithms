class Solution(object):
    def decodeString(self, s):
        stack = []
        result = ''
        num = 0
        for c in s:
            if c == ']':
                if num > 0:
                    stack.append(num)
                    num = 0
                present = ''
                while stack[-1] != '[':
                    present = stack.pop(-1) + present
                stack.pop(-1)
                present = stack.pop(-1) * present
                stack.append(present)
            elif c.isnumeric():
                num = num * 10 + int(c)
            else:
                if num > 0:
                    stack.append(num)
                    num = 0
                stack.append(c)
        return ''.join(stack)