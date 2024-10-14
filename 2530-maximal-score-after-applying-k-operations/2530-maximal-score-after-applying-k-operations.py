class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        pq = [-num for num in nums]
        heapify(pq)
        i = 0
        while i<k:
            x = -heappop(pq)
            score+=x
            heappush(pq, -ceil(x/3))
            i+=1        
        return score
