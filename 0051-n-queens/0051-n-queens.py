from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.queen(n, res, [], 0, set(), set(), set())
        return res

    def queen(self, n, res, sub, row, cols, diagonals1, diagonals2):
        if row == n:
            res.append(sub.copy())
            return 
        for col in range(n):
            diag1 = row - col
            diag2 = row + col
            if col in cols or diag1 in diagonals1 or diag2 in diagonals2:
                continue
            sub.append("." * col + "Q" + "." * (n - col - 1))
            cols.add(col)
            diagonals1.add(diag1)
            diagonals2.add(diag2)
            self.queen(n, res, sub, row + 1, cols, diagonals1, diagonals2)
            sub.pop()
            cols.remove(col)
            diagonals1.remove(diag1)
            diagonals2.remove(diag2)
        return