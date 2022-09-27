"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        
        cur = head
        m = {}
        m[head] = Node(head.val)
        
        while cur:
            if cur not in m:
                m[cur] = Node(cur.val)
            
            if cur.next and cur.next not in m:
                m[cur.next] = Node(cur.next.val)
            
            if cur.random and cur.random not in m:
                    m[cur.random] = Node(cur.random.val)

            m[cur].next = m[cur.next] if cur.next in m else None
            m[cur].random = m[cur.random] if cur.random in m else None
			
            cur = cur.next
        return m[head]