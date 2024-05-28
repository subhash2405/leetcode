class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        st = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i==0 or j==0 or i==m-1 or j==n-1):
                    st.append((i,j))
        while st:
            (u,v) = st.pop()
            if visited[u][v] == 1:
                continue
            visited[u][v]=1
            if board[u][v] == 'O':
                visited[u][v] = 1
                nx = [-1,1,0,0]
                ny = [0,0,1,-1]
                for i in range(4):
                    if 0<=u+nx[i]<m and 0<=v+ny[i]<n:
                        st.append((u+nx[i],v+ny[i]))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and visited[i][j]==0:
                    board[i][j]='X'