class Solution(object):
    def distanceK(self, root, target, k):
        parentsMap = {}
        
        def mapParents(node, parent):
            if not node:
                return 
            parentsMap[node] = parent
            mapParents(node.left,node)
            mapParents(node.right,node)
        
        mapParents(root,None)
        
        visited = set()
        queue = deque()
        queue.append((target,0))
        res = []
        while queue:
            node, distance = queue.popleft()
            visited.add(node)
            if distance == k:
                res.append(node.val)
                continue
            neighbors = [parentsMap[node],node.left,node.right]
            for x in neighbors:
                if x and x not in visited:
                    queue.append((x,distance+1))
        return res
        
        
        
            
            
        