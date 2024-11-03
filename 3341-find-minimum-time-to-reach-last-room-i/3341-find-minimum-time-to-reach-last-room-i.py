class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        st = [(0,0,0)]
        visited = [[float('inf') for _ in range(m)]for _ in range(n)]
        while st:
            x,y,time = st.pop(0)
            if visited[x][y] <= time:
                continue
            visited[x][y] = time
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            for i in range(4):
                a = dx[i] + x
                b = dy[i] + y
                if 0<=a<n and 0<=b<m:
                    if moveTime[a][b]>time:
                        st.append((a,b,moveTime[a][b]+1))
                    else:
                        st.append((a,b,time+1))

        return visited[-1][-1]
        


