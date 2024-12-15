class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        sum = 0
        for (u,v) in classes:
            avg = (u/v)
            sum+=avg
            newavg = (u+1)/(v+1)
            diff = newavg-avg
            pq.append((-diff, u,v))

        heapify(pq)

        
        i = 0
        while i<extraStudents:
            x,a,b = heappop(pq)
            if x==0:
                break
            sum-=(a/b)
            diff = (a+2)/(b+2) - (a+1)/(b+1)
            sum+=(a+1)/(b+1)
            heappush(pq,(-diff,a+1,b+1))
            i+=1
        return sum/len(classes)