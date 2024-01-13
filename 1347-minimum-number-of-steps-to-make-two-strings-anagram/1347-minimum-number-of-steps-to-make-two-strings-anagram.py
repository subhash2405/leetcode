class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr1 = Counter(s)
        arr2 = Counter(t)
        count = 0
        for i in arr1:
            if i not in t:
                count += arr1[i]
            else:
                if arr1[i] > arr2[i]:
                    count += (arr1[i] - arr2[i])
        return count
