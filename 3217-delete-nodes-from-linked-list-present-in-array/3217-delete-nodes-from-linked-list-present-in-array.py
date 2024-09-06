# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        set1 = set(nums)
        temp, prev = head, head
        while temp and temp.next:
            if temp.val in set1 and temp == head:
                var = temp.next
                temp.next = None
                temp = var
                head = var
                prev = var
            elif temp.val in set1:
                prev.next = temp.next
                # prev = temp
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
                
        if temp.val in nums:
            prev.next = None

        return head