class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for [u,v] in prerequisites:
            adj_list[v].append(u)
        visited  = [-1]*numCourses
        
        def dfs(node):
            if visited[node] == 0:
                return False
            if visited[node] == 1:
                return True
            visited[node]=0
            for ele in adj_list[node]:
                if not dfs(ele):
                    return False
            visited[node] = 1
            return True

        for i in range(numCourses):
            if visited[i]==-1:
                if not dfs(i):
                    return False
        return True

        