class Solution:
    def findAllRecipes(self, recipes,ingredients,supplies):
        graph = collections.defaultdict()
        for x,y in zip(recipes,ingredients):
            graph[x] = y 
        supplySet, recipeSet = set(supplies), set(recipes)
        
        res = []
        completeFoods = set()
        visited = set()
        def dfs(food):
        
            if food in supplySet or food in completeFoods:
                return True
            if food in visited or (food not in supplySet and food not in recipeSet):
                return False  
            
            visited.add(food)
            temp = True
            for x in graph[food]:
                if not dfs(x):
                    print(x)
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
        

        