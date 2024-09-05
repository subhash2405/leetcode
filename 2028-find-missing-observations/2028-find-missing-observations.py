class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ans = mean*(n+len(rolls))
        res = ans-sum(rolls)
        if res>6*n or res<0:
            return []

        min_val = res//n
        left = res%n
        if min_val==0 or (min_val == 6 and left>0):
            return []

        arr = [min_val]*n
        for i in range(left):
            arr[i]+=1

    

        return arr

        
            