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
        res = deque()
        res.append([root.val])
        def zigzag(q,k):
            if not q:
                return 
            lst,newQ = deque(),deque()
            while q:
                node = q.popleft()
                if k % 2 == 0:
                    if node.right:
                        lst.append(node.right.val)
                        newQ.appendleft(node.right)  
                    if node.left:
                        lst.append(node.left.val) 
                        newQ.appendleft(node.left)
                else:
                    if node.left:
                        lst.append(node.left.val) 
                        newQ.appendleft(node.left)
                    if node.right:   
                        lst.append(node.right.val) 
                        newQ.appendleft(node.right)
            if lst:
                res.append(lst)
            zigzag(newQ, k+1)

                
        
        zigzag(deque([root]),0)
        return res           