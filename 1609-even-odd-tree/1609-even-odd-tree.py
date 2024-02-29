class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root, 0)])  
        prev_val = None
        level = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, curr_level = queue.popleft()
                
                if curr_level % 2 == 0:
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else: 
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False
                
                prev_val = node.val
                
                if node.left:
                    queue.append((node.left, curr_level + 1))
                if node.right:
                    queue.append((node.right, curr_level + 1))
                    
            level += 1
            prev_val = None  
        
        return True
