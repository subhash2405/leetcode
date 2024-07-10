class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {}
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.val not in mapping:
                mapping[curr.val] = Node(curr.val)
            if curr.neighbors != []:
                for neighbor in curr.neighbors:
                    if neighbor.val not in mapping:
                        mapping[neighbor.val] = Node(neighbor.val)
                        stack.append(neighbor)
                    mapping[curr.val].neighbors.append(mapping[neighbor.val])
        return mapping[node.val]