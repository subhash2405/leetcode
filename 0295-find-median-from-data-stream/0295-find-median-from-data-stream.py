import statistics
class MedianFinder:

    def __init__(self):
        self.minarr = []
        self.maxarr = []
        
    def addNum(self, num: int) -> None:
        if len(self.minarr)==0 or -self.minarr[0]>=num:
            heapq.heappush(self.minarr, -num)
        else:
            heapq.heappush(self.maxarr, num)

        if len(self.minarr)>len(self.maxarr)+1:
            heapq.heappush(self.maxarr, -heapq.heappop(self.minarr))
        elif len(self.minarr)<len(self.maxarr):
            heapq.heappush(self.minarr, -heapq.heappop(self.maxarr))
                
        

    def findMedian(self) -> float:
        if len(self.minarr)==len(self.maxarr):
            return (self.maxarr[0]-self.minarr[0])/2
        return -self.minarr[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()