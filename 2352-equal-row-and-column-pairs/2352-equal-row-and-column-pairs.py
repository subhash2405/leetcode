class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = [0]
        a = set()
        for i in range(len(grid)):
            for j in range(i,len(grid)):
                if (i,j) not in a:
                    self.equal(i, j, count, grid)
                    a.add((i,j))
                if (j,i) not in a:
                    self.equal(j, i, count, grid)
                    a.add((j,i))
        return count[0]

    def equal(self, row, col, count, grid):
        for i in range(len(grid)):
            if grid[row][i] != grid[i][col]:
                return
        count[0] += 1
