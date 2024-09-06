# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count+=1
        
        arr = [0]*(count//2)
        track = 0
        var = head
        while var:
            if track>=len(arr):
                arr[count-1-track]+=var.val
            else:
                arr[track]+=var.val
            track+=1
            var = var.next
        print(arr)
        return max(arr)
