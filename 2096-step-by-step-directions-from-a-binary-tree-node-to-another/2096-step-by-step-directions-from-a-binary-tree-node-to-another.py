class Solution(object):
    def getDirections(self, root, startValue, destValue):
        left_path = deque()
        right_path = deque()
        def helper(node, path, targetnode):
            if node.val == targetnode:
                return True 
            if node.left:
                if helper(node.left, path, targetnode):
                    path.appendleft("L")
                    return True
            if node.right:
                if helper(node.right, path, targetnode):
                    path.appendleft("R")
                    return True 
        helper(root, left_path,  startValue)
        helper(root, right_path,  destValue)
        while left_path and right_path and left_path[0] == right_path[0]:
            left_path.popleft()
            right_path.popleft()
        return "U"*len(left_path) + ''.join(right_path)
        
        
        
        