class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        temp = 3 ** (n // 3)
        var = n % 3

        if var == 0:
            return temp
        elif var == 1:
            return temp // 3 * 4  
        else:
            return temp * 2  
