class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key= lambda x:x[0])

        suffix = [0]*n
        suffix[-1] = events[-1][2]

        for i in range(n-2,-1,-1):
            suffix[i] = max(events[i][2], suffix[i+1])

        maxSum = 0

        for i in range(n):
            left, right = i + 1, n - 1
            nextEventIndex = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    nextEventIndex = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            if nextEventIndex != -1:
                maxSum = max(maxSum, events[i][2] + suffix[nextEventIndex])
            
            maxSum = max(maxSum, events[i][2])
        
        return maxSum