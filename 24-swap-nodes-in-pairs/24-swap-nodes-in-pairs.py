# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0,head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next
            
          
            curr.next = nxtPair
            prev.next = second
            second.next = curr
            
            
            prev = curr
            curr = curr.next 
        
        return dummy.next 
        