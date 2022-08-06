# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 2 3 4 5 6 7 8 

class Solution(object):
    def pairSum(self, head):
        if not head.next.next:
            return head.val + head.next.val
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        max_sum = float("-inf")
        new_curr = head
        while prev:
            max_sum = max(max_sum, prev.val + new_curr.val)
            prev = prev.next
            new_curr = new_curr.next
        
        return max_sum
        
        
            
            
            