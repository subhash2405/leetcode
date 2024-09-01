class Solution:
    def countPairs(self, nums: List[int]) -> int:
        possiblepair = {}
       
        res = 0
        nums = [str(n) for n in nums]
        m = max([len(s) for s in nums])
        for i in range(len(nums)):
            if len(nums[i])!=m:
                nums[i] = '0'*(m-len(nums[i]))+nums[i]
    
        def swap(s):
            m = len(s)
            res = set([])
            for i in range(m):
                for j in range(i+1,m):
                    res.add(s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:])
            return res
 
        freq = Counter(nums)
        for s in set(nums):
            res += freq[s]*(freq[s]-1) 
            change1 = swap(s)
            changes = set([])
            for c in change1:
                change2=swap(c)
                changes.add(c)
                for cc in change2:
                    changes.add(cc)
            for c in changes:
                if c in freq and c!=s:
                    res += freq[c]*freq[s]
        return res // 2
            
        