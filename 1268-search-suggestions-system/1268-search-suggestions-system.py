class Solution(object):
    def suggestedProducts(self, products, searchWord):

        res = []
        products.sort()
        
        
        for i in range(len(searchWord)):
            temp = []
            
            for x in products:
                if i < len(x) and x[i] == searchWord[i]:
                    temp.append(x)
                    
            res.append(temp[:3])
            products = temp
            
        return res
                
                
                    
                    
        