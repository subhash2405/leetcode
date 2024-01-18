class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=candy:
                res.append(True)
            else:
                res.append(False)
        return res
        