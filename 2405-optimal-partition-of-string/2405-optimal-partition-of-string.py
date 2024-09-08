class Solution:
    def partitionString(self, s: str) -> int:
        arr = set()
        count = 0
        for var in s:  
            if var in arr:
                count+=1
                arr = set(var)
            else:
                arr.add(var)
        if arr:
            return count+1
        return count