class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        count = sorted(count.items(), key=lambda x: x[1])
        while k > 0 and count:
            if count[0][1] <= k:
                k -= count[0][1]
                count.pop(0)
            else:
                count[0] = (count[0][0], count[0][1] - k)
                k = 0
        return len(count)
