class Solution:
    def findAllRecipes(self, recipes,ingredients,supplies):
        map1 = {}
        res = []
        for i in range(len(recipes)):
                map1[recipes[i]] = ingredients[i]
        visited = set()
		
        recipe_set = set(recipes)
        supplies_set= set(supplies)
        def dfs(food):
           
            if food in supplies or map1.get(food,[])==[]:
                return True
            elif food in visited:
                return False
         
            visited.add(food)
            for i in map1[food]:
                if (i not in supplies_set and i not in recipe_set ) or not dfs(i):
                    return False
            res.append(food)
            map1[food] = []
            return True
             
       
        for i in recipes:
            dfs(i)
        return res