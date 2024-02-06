class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        a='123456789'
        for i in range(len(a)):
            for j in range(i+1,len(a)+1):
                curr=int(a[i:j])
                if low<=curr<=high:
                    res.append(curr)
                if curr>high:
                    break
        res.sort()
        return res
        

        