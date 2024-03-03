# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        prev=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        rem=count-n+1
        if rem==1:
            return head.next
        i=1
        new=head
        prev=None
        while i<rem:
            prev=new
            new=new.next
            i+=1

        prev.next=new.next
        return head
        


