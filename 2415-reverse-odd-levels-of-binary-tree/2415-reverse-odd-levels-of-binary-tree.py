# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None


        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                if level % 2 == 1:  # Only reverse values at odd levels
                    level_values.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                values = [node.val for node in level_values]
                values.reverse()
                for i, node in enumerate(level_values):
                    node.val = values[i]

            level += 1

        return root
