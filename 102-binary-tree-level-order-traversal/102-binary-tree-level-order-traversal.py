# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        new_queue = []
        level = []
        result = []
        while queue != []:
            for x in queue:
                level.append(x.val)
                if x.left:
                    new_queue.append(x.left)
                if x.right:
                    new_queue.append(x.right)
            result.append(level)
            level = []
            queue = new_queue
            new_queue = []
        return result 