class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp  = arr.copy()
        temp.sort()
        dic = {}
        count = 1
        for i in temp:
            if i not in dic:
                dic[i] = count
                count+=1

        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr