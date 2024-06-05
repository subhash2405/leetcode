class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr=[1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1]:
                arr[i+1]=arr[i]+1
        j=len(ratings)-1
        while j>0:
            if ratings[j-1]>ratings[j] and arr[j-1]<=arr[j]:
                arr[j-1]=arr[j]+1
            j-=1
        
        return sum(arr)