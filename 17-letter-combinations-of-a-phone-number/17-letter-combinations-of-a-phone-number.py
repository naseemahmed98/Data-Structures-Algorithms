class Solution:
    def letterCombinations(self, digits):
        letter = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        i=0
        combo=[]
        res=[]
        if not digits:
            return []
        def solve(i,combo):
            if i==len(digits):
                res.append("".join(combo))
                return
            temp=letter[digits[i]]
            for k in temp:
                combo.append(k)
                solve(i+1,combo)
                combo.pop()
            
    
        
        solve(i,combo)
        return res