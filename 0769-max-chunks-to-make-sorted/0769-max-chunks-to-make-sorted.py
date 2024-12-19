class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        end = 0
        count = 0
        while end<len(arr):
            maxnum = arr[end]
            point = end
            while point<=maxnum:
                if arr[point]>maxnum:
                    maxnum = arr[point]
                point+=1
            count+=1
            end = maxnum+1
        return count