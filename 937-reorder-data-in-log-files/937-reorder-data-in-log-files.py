class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        digList, strList = [],[]
        
        for x in logs:
            split = x.split()
            if split[1].isalpha():
                strList.append(x)
            else:
                digList.append(x)
       
        lst = []
        for x in strList:
            words = x.split()
            identifier = words.pop(0)
            words = (identifier,words)
            lst.append(words)
        lst.sort(key = lambda x: (x[1], x[0]))
        
        res = []
        for x in lst:
            x[1].insert(0,x[0])
            new = [" ".join(x[1])]
            res += new
           
        res += digList
        return res 
    