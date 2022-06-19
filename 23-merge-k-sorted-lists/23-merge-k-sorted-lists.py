# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
   
        h = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h,(l.val,i))
        
        dummy = current = ListNode()
        
        while h:
            val, i = heapq.heappop(h)
            current.next = lists[i]
            if lists[i].next:
                heapq.heappush(h,(lists[i].next.val,i))
                lists[i] = lists[i].next
            current = current.next
        
        return dummy.next