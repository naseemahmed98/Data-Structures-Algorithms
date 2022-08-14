# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return 
        levels = []
        queue = [root]
        res = []
        def bfs(queue):
            if not queue:
                return 
            lst = []
            for x in range(len(queue)):
                lst.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)  
                queue.pop(0)
            levels.append(lst)
            bfs(queue)
            #return levels
    
        bfs(queue)
        for x in range(len(levels)):
            res.append(levels[x][-1])
        return res
     
      