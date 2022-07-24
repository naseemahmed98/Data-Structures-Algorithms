# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode()
        carry = 0 
        
        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            node_val = val1 + val2 + carry
            carry = 1 if node_val >= 10 else 0
            node_val = node_val % 10
            curr.next = ListNode(node_val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            
        