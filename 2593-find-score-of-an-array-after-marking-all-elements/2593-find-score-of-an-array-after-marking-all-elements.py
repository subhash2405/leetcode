class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        count = 0
        ele = list(set(nums))
        ele.sort()
        for i in ele:
            for j in dic[i]:
                if arr[j] == 1:
                    continue
                else:
                    count+=i
                    if j-1>=0:
                        arr[j-1]=1
                    if j+1<len(nums):
                        arr[j+1] = 1
        return count