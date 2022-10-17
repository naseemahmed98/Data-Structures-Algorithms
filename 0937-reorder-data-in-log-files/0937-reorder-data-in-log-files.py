class Solution:
    #T=O(m*nlgn),S=O(mn)
    #m=len(log),n=number of logs
    def reorderLogFiles(self, logs):
        digList, strList = [],[]
        for x in logs:
            lst = x.split()
            if lst[1].isnumeric():
                digList.append(x)
            else:
                strList.append(lst)
        
        strList.sort(key = lambda x:(x[1:],x[0]))
        newString = []
        for x in strList:
            newString.append(" ".join(x))
        
        return newString + digList