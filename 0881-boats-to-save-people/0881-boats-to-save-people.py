class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        if people[-1]>=limit:
            while people[-1]<limit:
                people.pop()
                count+=1
        start = 0
        end = len(people)-1
        while start<=end:
            if people[start]+people[end]<=limit:
                start+=1
            count+=1
            end-=1
        return count