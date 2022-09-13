class Solution(object):
    def findCircleNum(self, isConnected):
        isVisited = set()        
        
        def bfs(i):
            q = deque()
            isVisited.add(i)
            q.append(i)
            while q:
                curCity = q.popleft()
                for adjacendCity, connected in enumerate(isConnected[curCity]):
                    if connected == 1 and adjacendCity not in isVisited:
                        isVisited.add(adjacendCity)
                        q.append(adjacendCity)
                  
        ans = 0
        for i in range(len(isConnected)):
            if i not in isVisited:
                ans += 1
                bfs(i)
                
        return ans
        