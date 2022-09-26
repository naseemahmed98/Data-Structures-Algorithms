class Solution(object):
    def letterCombinations(self, digits):
        letterHashMap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if not digits:
            return []
       
        res = []
        def dfs(index,lst):
            if index == len(digits):
                string = ''.join(lst)
                res.append(string)
                return
            for x in letterHashMap[digits[index]]:
                lst.append(x)
                dfs(index+1,lst)
                lst.pop()
              

        dfs(0,[])
        return res 