class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        preReqs = collections.defaultdict(list)
        for x,y in prerequisites:
            preReqs[x].append(y)
        
        visited = set()
        memo = {}
        def dfs(course):
            if course in memo:
                return memo[course]
            if course in visited:
                return False
      
            visited.add(course)
            for x in preReqs[course]:
                if not dfs(x):
                    return False
            visited.remove(course)
            memo[course] = True
            return True
        
        
        for x in range(numCourses):
            if not dfs(x):
                print(x)
                return False
        return True