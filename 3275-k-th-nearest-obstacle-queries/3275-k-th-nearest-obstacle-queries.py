class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        n = len(queries)
        res = [-1]*n
        heap = []
        for i in range(n):
            temp = abs(queries[i][0]) + abs(queries[i][1])
            if len(heap)>=k:
                heapq.heappushpop(heap, -temp)
            else:
                heapq.heappush(heap, -temp)
            if len(heap)==k:
                temp = heapq.heappop(heap)
                res[i] = -temp
                heapq.heappush(heap, temp)
        return res        