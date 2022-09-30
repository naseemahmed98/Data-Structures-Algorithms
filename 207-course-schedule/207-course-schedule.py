class Solution(object): #BFS
    def canFinish(self, numCourses, prerequisites):
        numPreqs = [0] * numCourses
        preMap = []
        for x in range(numCourses):
            preMap.append([])
        
        for y,x in prerequisites:
            numPreqs[y] += 1 
            preMap[x].append(y)
        
        noPreReqs = collections.deque()
        for x in range(numCourses):
            if numPreqs[x] == 0:
                noPreReqs.append(x)
        
        counter = 0 
        while noPreReqs:
            course = noPreReqs.popleft()
            counter += 1 
            for x in preMap[course]:
                numPreqs[x] -= 1 
                if numPreqs[x] == 0:
                    noPreReqs.append(x)
        
        return True if counter == numCourses else False
        
            
        