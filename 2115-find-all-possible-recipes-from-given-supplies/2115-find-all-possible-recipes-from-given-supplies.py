class Solution:
    def findAllRecipes(self, recipes,ingredients,supplies):
        graph = collections.defaultdict()
        for x,y in zip(recipes,ingredients):
            graph[x] = y 
        suppliesSet, recipesSet = set(supplies), set(recipes)
        
        res = []
        completeFoods = set()
        visited = set()
        def dfs(food):
            
            if food in supplies or food in completeFoods:
                return True
            if food in visited or (food not in suppliesSet and food not in recipesSet):
                return False
            
             
            visited.add(food)
            temp = True
            for x in graph[food]:
                if not dfs(x):
                    temp = False
                    break 
            if temp:
                res.append(food)
                completeFoods.add(food)
                return True
            else:
                return False
        
        for x in recipes:
            dfs(x)
      
        return res 
        

        