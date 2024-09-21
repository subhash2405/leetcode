class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        
        for i in range(1, 10):
            self.dfs(i, n, result)
        
        return result
    
    def dfs(self, curr, n, result):
        if curr > n:
            return  
        result.append(curr)  
        
        for i in range(10):
            if curr * 10 + i > n:
                return  
            self.dfs(curr * 10 + i, n, result)  