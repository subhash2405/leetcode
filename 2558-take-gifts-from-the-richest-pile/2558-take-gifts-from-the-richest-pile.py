class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts) 
        i = 0
        while i<k:
            var = -heappop(gifts)
            temp = isqrt(var)
            heappush(gifts,-temp)       
            i+=1
        return -sum(gifts)