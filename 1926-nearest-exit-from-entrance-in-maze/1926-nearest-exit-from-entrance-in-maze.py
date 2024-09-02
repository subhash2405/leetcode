class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        count = 0
        m = len(maze)
        n = len(maze[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]


        st = [[entrance[0], entrance[1], 0]]
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]
        while st:
            [x,y, count] = st.pop(0)
            if (x in [0,m-1] or y in [0,n-1]) and ([x,y]!=entrance):
                return count
            if visited[x][y]==1:
                continue
            visited[x][y] = 1
            for i in range(4):
                a = x+nx[i]
                b = y+ny[i]
                if 0 <= a < m and 0 <= b < n and maze[a][b] == '.' :
                    st.append([a, b, count + 1])
        return -1