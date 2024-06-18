class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = sorted(zip(difficulty, profit))
        worker.sort()
        n = len(worker)
        i = maxp = count = k = 0
        while k<len(arr):
            if i == n:
                return count
            if arr[k][0]<=worker[i]:
                maxp = max(maxp, arr[k][1])
            else:
                count+=maxp
                k-=1
                i+=1
            k+=1
        if i<n:
            count += max(profit)*(n-i)
        return count

        