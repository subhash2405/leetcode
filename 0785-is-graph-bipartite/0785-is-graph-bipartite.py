class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        col=[-1]*n
        for i in range(n):
            if col[i]==-1:
                st = [(i,0)]
                while st:
                    node,color = st.pop(0)
                    if col[node]==-1:
                        col[node] = color
                        for neigh in graph[node]:
                            st.append((neigh, (1-color)))
                    elif col[node]!=color:
                        return False

        return True 






