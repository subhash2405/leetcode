class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        arr = [[]for _ in range(n)]
        res = []
        for i in range(len(edges)):
            arr[edges[i][1]].append(edges[i][0])
        for i in range(n):
            st = [i]
            visited = []
            while st:
                edge = st.pop()
                if edge not in visited and edge!=i:
                    visited.append(edge)
                st = list(set(st + arr[edge]))
            visited.sort()
            res.append(visited)
        return res