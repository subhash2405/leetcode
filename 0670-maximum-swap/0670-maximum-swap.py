class Solution:
    def maximumSwap(self, num: int) -> int:
        var = str(num)
        arr = [int(i) for i in var]
        temp = arr.copy()
        dic = {}
        for i in range(len(temp)):
            dic[temp[i]] = i
        arr.sort(reverse = True)
        for i in range(len(temp)):
            if temp[i] != arr[i]:
                j = dic[arr[i]]
                temp[i],temp[j] = temp[j], temp[i]
                break
        res = ""
        for i in temp:
            res+=str(i)
        return int(res)