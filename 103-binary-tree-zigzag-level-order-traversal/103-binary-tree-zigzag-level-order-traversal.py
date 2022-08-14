# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return 
        res = []
        queue = [root]
        
        def bfs(queue, level):
            if not queue:
                return 
            vals = []
            queue.reverse()
            for x in range(len(queue)):
                vals.append(queue[0].val)
                if level % 2 == 1:
                    if queue[0].right:
                        queue.append(queue[0].right)
                    if queue[0].left:
                        queue.append(queue[0].left)
                elif level % 2 == 0:
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)
                queue.pop(0)
            res.append(vals)
            bfs(queue,level+1)
            
            
        bfs(queue,0)
        return res
        
        