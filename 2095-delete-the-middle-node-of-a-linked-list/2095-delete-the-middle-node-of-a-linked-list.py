# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        # if head.next.next is None:
        #     return head.next
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count+=1
        mid = count//2
        var = head
        i = 0
        prev = head
        while var and i<mid:
            prev = var
            var = var.next
            i+=1
        prev.next = var.next
        return head
        