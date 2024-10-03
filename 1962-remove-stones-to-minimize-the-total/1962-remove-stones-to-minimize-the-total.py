class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negative = [-x for x in piles]
        add = sum(piles)
        heapq.heapify(negative)
        for _ in range(k):
            maxc = heapq.heappop(negative)
            sub = math.floor(-maxc/2)
            add-=sub
            heapq.heappush(negative, maxc+sub)
        
        return add
