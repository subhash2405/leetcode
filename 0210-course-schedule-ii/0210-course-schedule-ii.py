class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        flag = [0]*numCourses
        for [u,v] in prerequisites:
            adj_list[v].append(u)
            flag[u]+=1
        queue = []
        visited = []
        for i in range(numCourses):
            if flag[i] == 0:
                queue.append(i)
        while queue:
            index = queue.pop(0)
            if index in visited:
                continue
            visited.append(index)
          
            for node in adj_list[index]:
                flag[node]-=1
                if flag[node] == 0:
                    queue.append(node)
        if len(visited)!=numCourses:
            return []
        return visited
