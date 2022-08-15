class Solution(object):
    def getDirections(self, root, startValue, destValue):
        startPath, destPath = deque(), deque()
        
        def findTarget(node,val,path):
            if not node:
                return 
            if node.val == val:
                return True 
            if findTarget(node.left,val,path):
                path.appendleft("L")
                return True 
            if findTarget(node.right,val,path):
                path.appendleft("R")
                return True 
        
        findTarget(root,startValue, startPath)
        findTarget(root,destValue, destPath)
        
        while startPath and destPath and startPath[0] == destPath[0]:
            startPath.popleft()
            destPath.popleft()
        
        return "U" * len(startPath) + "".join(destPath)