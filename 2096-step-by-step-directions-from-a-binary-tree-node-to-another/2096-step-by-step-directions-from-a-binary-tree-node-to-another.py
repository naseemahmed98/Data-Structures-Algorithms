class Solution(object):
    def getDirections(self, root, startValue, destValue):
        
        startDirections, destDirections = deque(),deque()
        def findTarget(node, value, directions):
            if not node:
                return False
            if node.val == value:
                return True
            if findTarget(node.left,value,directions):
                directions.appendleft("L")
                return True
            if findTarget(node.right,value,directions):
                directions.appendleft("R")
                return True
       
    
        findTarget(root,startValue,startDirections)
        findTarget(root,destValue,destDirections)
        
        while startDirections and destDirections and startDirections[0] == destDirections[0]:
            startDirections.popleft()
            destDirections.popleft()
        
        return "U" * len(startDirections) + ''.join(destDirections)
            
            