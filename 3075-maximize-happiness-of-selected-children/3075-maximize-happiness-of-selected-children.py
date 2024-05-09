class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        if k==1:
            return happiness[0]
        sum = happiness[0]
        for i in range(1,k):
            sum+=max(happiness[i]-i,0)
        return sum