# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        if head.next == None:
            return head
        lst = []
        current = head 
        while current.next:
            lst.append(current)
            current = current.next
        lst.append(current)
        print(len(lst))
        l, r = 0, len(lst)-1
        while l < r:
            lst[l].next = lst[r]
            l += 1 
            lst[r].next = lst[l]
            r -= 1 
        lst[l].next = None 
        
        return lst[0]
    
  