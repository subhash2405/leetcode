class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums=Counter(arr)
        count=list(nums.values())
        count.sort()
        for i in range(len(count)-1):
            if count[i]==count[i+1]:
                return False
        return True


        