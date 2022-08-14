# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return root
        res = []
        def add_children(stack):
            
            if not stack:
                return res
            vals = []
            for x in range(len(stack)):
                vals.append(stack[0].val)
                if stack[0].left:
                    stack.append(stack[0].left)
                if stack[0].right:
                    stack.append(stack[0].right)
                stack.pop(0)
            res.append(vals)
            add_children(stack)
            return res 
        return add_children([root])
        
        
        