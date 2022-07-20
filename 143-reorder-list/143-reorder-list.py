# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next
        #get to middle of list 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse second half of list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp
        
        
        #merge half of first list and reversed second half of list
        
        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
        
        return head
        
        
        
        