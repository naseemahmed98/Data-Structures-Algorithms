class Solution(object):
    def findCircleNum(self, isConnected):
        isVisited = set()        
        
        def bfs(i):
            q = deque()
            isVisited.add(i)
            q.append(i)
            while q:
                curCity = q.popleft()
                for x in range(len(isConnected[curCity])):
                    if isConnected[curCity][x] == 1 and x not in isVisited:
                        isVisited.add(x)
                        q.append(x)
                  
        ans = 0
        for i in range(len(isConnected)):
            if i not in isVisited:
                ans += 1
                bfs(i)
                
        return ans
        