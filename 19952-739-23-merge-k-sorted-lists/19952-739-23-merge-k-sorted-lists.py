# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        heapify(pq)
        for l  in lists:
            while l!=None:
                heapq.heappush(pq,l.val)
                l = l.next
        head = ListNode()
        prev = head
        while pq:
            val = heapq.heappop(pq)
            temp  = ListNode(val=val,next=None)
            prev.next = temp
            prev = prev.next
        
        return head.next