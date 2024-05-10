class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        num = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                num.append([float(arr[i]/arr[j]), (arr[i], arr[j])])
        sorted_arr = sorted(num, key=lambda x: x[0])
        return [sorted_arr[k-1][1][0], sorted_arr[k-1][1][1]]
