class Solution(object):
    def letterCombinations(self, digits):
        letterHashMap = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if not digits:
            return []
       
        res = []
        def dfs(number,index,string):
            if index == len(digits)-1:
                for x in (letterHashMap[number]):
                    combo = string + x 
                    res.append(combo)
                return
            for x in letterHashMap[number]:
                combo = string + x 
                if index < len(digits)-1:
                    dfs(digits[index+1],index+1,combo)
              

        dfs(digits[0],0,'')
        return res 