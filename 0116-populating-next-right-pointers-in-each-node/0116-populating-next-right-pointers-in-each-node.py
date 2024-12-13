"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        st = [(root,0)]
        dic = {}
        while st:
            (temp, lvl) = st.pop(0)
            if not temp:
                continue
            if lvl not in dic:
                dic[lvl] = [temp]
            else:
                dic[lvl].append(temp)
            if temp.left:
                st.append((temp.left,lvl+1))
            if temp.right:
                st.append((temp.right, lvl+1))
        
        keys = list(dic.keys())
        for key in keys:
            for i in range(len(dic[key])-1):
                dic[key][i].next = dic[key][i+1]
        
        return root