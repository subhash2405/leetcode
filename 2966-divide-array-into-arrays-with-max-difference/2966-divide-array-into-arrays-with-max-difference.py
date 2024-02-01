class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        if n%3!=0:
            return []
        nums.sort()
        res=[]
        for i in range(0,n,3):
            if i+2<n and nums[i+2]-nums[i]<=k:
                res.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
        return res
       
        