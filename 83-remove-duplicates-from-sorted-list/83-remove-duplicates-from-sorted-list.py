# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return 
        curr = head 
        lst = []
        while curr:
            if curr.val not in lst:
                lst.append(curr.val)
            curr = curr.next 
        dummy = head = ListNode(lst[0])
        for x in range (1,len(lst)):
            head.next = ListNode(lst[x])
            head = head.next
        return dummy 
            
    