"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        clone = {}
        clone[node] = Node(node.val)
        queue = [node]
        
        while queue:
            copy = queue.pop(0)
            for nei in copy.neighbors:
                if nei not in clone:
                    queue.append(nei)
                    clone[nei] = Node(nei.val)
                clone[copy].neighbors.append(clone[nei])
        
        return clone[node]
                