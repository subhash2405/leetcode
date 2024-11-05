class Solution:
    def minChanges(self, s: str) -> int:
        temp = 0
        count = 1
        res = 0
        arr = list(s)
        for i in range(1, len(arr)):
            if arr[i] != arr[temp]:
                if (temp-i)%2==0:
                    temp = i
                    count = 1
                    continue
                else:
                    count+=1
                    res+=1
                    arr[i] = arr[temp]
            else:
                count+=1
        
        return res
            
