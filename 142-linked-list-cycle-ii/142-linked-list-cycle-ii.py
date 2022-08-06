# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                break
        
        if not fast or not fast.next:
                return None
        
        slow2 = head 
        while True:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
        
          
          
        