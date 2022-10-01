class Solution:
    def findAllRecipes(self, recipes,ingredients,supplies):
        graph = collections.defaultdict(list)
        numIng = collections.defaultdict(int)
        
        for x in range(len(ingredients)):
            for y in range(len(ingredients[x])):
                numIng[recipes[x]] += 1 
                graph[ingredients[x][y]].append(recipes[x])
        
        queue = collections.deque()
        for x in supplies:
            queue.append(x)
        
        res = []
        while queue: 
            node = queue.popleft()
            for x in graph[node]:
                numIng[x] -= 1 
                if not numIng[x]:
                    res.append(x)
                    queue.append(x)
        return res
            