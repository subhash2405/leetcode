class Solution:
    def countPairs(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                a = str(nums[i])
                b = str(nums[j])
                if len(a)<len(b):
                    a = '0'*(len(b)-len(a)) + a
                elif len(a)>len(b):
                    b = '0'*(len(a)-len(b)) + b
                count = 0
                for k in range(len(a)):
                    if a[k]!=b[k]:
                        count+=1
                if count<=2 and sorted(a)==sorted(b):
                    # print(a,b)
                    res+=1

        return res