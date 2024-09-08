# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = [None] * k  
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        size = length // k  
        extra = length % k  
        
        current = head
        for i in range(k):
            if not current:
                result[i] = None 
            else:
                result[i] = current  
                part_size = size + (1 if extra > 0 else 0) 
                extra -= 1
                
                for j in range(1, part_size):
                    if current:
                        current = current.next
                
                if current:
                    next_part = current.next
                    current.next = None
                    current = next_part
        
        return result