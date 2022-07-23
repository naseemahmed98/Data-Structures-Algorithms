# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_digits = ""
        l2_digits = ""
        while l1 or l2:
            if l1:
                l1_digits += str(l1.val)
                l1 = l1.next
            if l2:
                l2_digits+= str(l2.val)
                l2 = l2.next 
        new_digits = str(int(l1_digits[: :-1]) + int(l2_digits[: :-1]))[: :-1]
        
        dummyNode = curr = ListNode()
        for x in range(len(new_digits)):
            curr.next = ListNode(val=int(new_digits[x])) #curr.next = 7
            curr = curr.next 
        return dummyNode.next
            
        