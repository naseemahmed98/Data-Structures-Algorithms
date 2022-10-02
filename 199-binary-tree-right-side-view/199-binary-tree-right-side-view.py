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
        
        res = [[root]]
        def levelTraversal(q):
            if not q:
                return
            lst = []
            while q:
                node = q.popleft()
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)
            if lst:
                res.append(lst)
            levelTraversal(deque(lst))
            
                
        
    
        levelTraversal(deque([root]))
    
        for x in range(len(res)):
            res[x] = res[x][-1].val
        
        return res
               