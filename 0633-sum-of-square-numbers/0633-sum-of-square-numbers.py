class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(c**0.5)
        
        while low <= high:
            current_sum = low**2 + high**2
            if current_sum == c:
                return True
            elif current_sum > c:
                high -= 1
            else:
                low += 1
                
        return False
