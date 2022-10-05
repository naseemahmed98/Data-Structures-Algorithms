class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        preReqs = collections.defaultdict(list)
        for x,y in prerequisites:
            preReqs[x].append(y)
        
        memo = {}
        def dfs(course,visited):
            if course in memo:
                return memo[course]
            if course in visited:
                return False
            if not preReqs[course]:
                return True
            visited.add(course)
            for x in preReqs[course]:
                if not dfs(x,visited):
                    return False
            #visited.remove(course)
            memo[course] = True
            return True
        
        
        for x in range(numCourses):
            if not dfs(x,set()):
                print(x)
                return False
        return True