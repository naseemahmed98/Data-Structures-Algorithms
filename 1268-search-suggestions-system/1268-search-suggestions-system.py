class Solution(object):
    def suggestedProducts(self, products, searchWord):

        res = []
        products.sort()
        
        
        for i in range(len(searchWord)):
            temp = []
            
            for product in products:
                if i < len(product) and product[i] == searchWord[i]:
                    temp.append(product)
                    
            res.append(temp[:3])
            products = temp
            
        return res
                
                
                    
                    
        