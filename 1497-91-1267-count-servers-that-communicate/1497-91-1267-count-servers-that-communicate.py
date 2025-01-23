class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        
        self.rows = {}
        self.cols = {}

        for i in range(m):
            self.rows[i] = 0
            for j in range(n):
                if j not in self.cols:
                    self.cols[j] = 0  
                if grid[i][j]==1:
                    self.rows[i]+=1
                    self.cols[j]+=1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (self.rows[i]>1 or self.cols[j]>1):
                    self.res+=1
                    
        return self.res