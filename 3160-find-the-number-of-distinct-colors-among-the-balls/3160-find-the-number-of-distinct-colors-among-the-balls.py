class Solution:
    def queryResults(self, _: int, queries: List[List[int]]) -> List[int]:
        ballColor, colorBalls = {}, defaultdict(set)
        result = []
        for x,y in queries:
            if x in ballColor:
                oldColor = ballColor[x]
                colorBalls[oldColor].remove(x)
                if not colorBalls[oldColor]:
                    del colorBalls[oldColor]

            ballColor[x] = y
            colorBalls[y].add(x)
            result.append(len(colorBalls))
            
        return result