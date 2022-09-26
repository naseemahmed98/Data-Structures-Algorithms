class Solution:
    def letterCombinations(self, A):
        letter = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        i=0
        STR=[]
        ans=[]
        
        def solve(A,i,STR,ans):
            if i>=len(A):
                ans.append("".join(STR))
                return
            temp=letter[A[i]]
            for k in temp:
                STR.append(k)
                solve(A,i+1,STR,ans)
                STR.pop()
            
            return ans
        
        return solve(A,i,STR,ans)