import heapq
from collections import Counter
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = []
        for i in range(len(roads)):
            arr.append(roads[i][0])
            arr.append(roads[i][1])
        count = Counter(arr)
        print(count)
        temp = list(set(arr))
        heap = []
        for i in range(len(temp)):
            heapq.heappush(heap, -count[temp[i]])  
        res = 0
        importance = n
        while heap:
            res += importance * (-heapq.heappop(heap))  
            importance -= 1
        return res
