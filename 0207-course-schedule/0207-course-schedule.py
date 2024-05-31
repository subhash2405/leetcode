class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for [u,v] in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = []
        while queue:
            index = queue.pop(0)
            if index in visited:
                continue
            visited.append(index)
        
            for node in adj[index]:
                indegree[node]-=1
                if indegree[node] == 0:
                    queue.append(node)
        return len(visited) == numCourses
