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
            return 
        
        curr = head 
        hashMap = {}
        hashMap[curr] = Node(curr.val)
        while curr:
            if curr.next and curr.next not in hashMap:
                hashMap[curr.next] = Node(curr.next.val)
            if curr.random and curr.random not in hashMap:
                hashMap[curr.random] = Node(curr.random.val)
            hashMap[curr].next = hashMap[curr.next] if curr.next else None
            hashMap[curr].random = hashMap[curr.random] if curr.random else None 
            curr = curr.next
        
        return hashMap[head]
            
            
        