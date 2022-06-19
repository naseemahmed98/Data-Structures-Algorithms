class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        dct = {}
        dct['('], dct['{'], dct['['] = ')', '}', ']'
        queue = []
        for x in s: 
            if x in dct:
                queue.append(x)
            else:
                if len(queue) == 0 or dct[queue[-1]] != x:
                    return False
                else:
                    queue.pop(-1)
                
                
        return True if len(queue) == 0 else False