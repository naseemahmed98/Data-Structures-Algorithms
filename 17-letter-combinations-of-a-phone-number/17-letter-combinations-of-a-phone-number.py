class Solution(object):
    def letterCombinations(self, digits):
        letterHashMap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if not digits:
            return []
       
        res = []
        def dfs(index,string):
            if index == len(digits):
                res.append(string)
                return
            for x in letterHashMap[digits[index]]:
                combo = string + x 
                dfs(index+1,combo)
              

        dfs(0,'')
        return res 