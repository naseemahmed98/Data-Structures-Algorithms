class Solution(object):
    def suggestedProducts(self, products, searchWord):
        
        res = []
        products.sort()
        
        for x in range(len(searchWord)):
            temp = []
            for y in products:
                if x < len(y) and searchWord[x] == y[x]:
                    temp.append(y)
                
            res.append(temp[:3])
            products = temp   
        
        return res
        