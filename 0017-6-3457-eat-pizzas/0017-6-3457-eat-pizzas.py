class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort()
        days = n//4
        odd = days//2 + days%2
        even = days-odd
        res = 0
        ptr = n-1
        for i in range(odd):
            res+=pizzas[ptr]
            ptr-=1
        for i in range(even):
            res+=pizzas[ptr-1]
            ptr-=2
        return res