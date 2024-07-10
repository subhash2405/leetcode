class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in range(len(logs)):
            if logs[i][0]!='.':
                count+=1
            elif logs[i][1]=='.':
                if count>0:
                    count-=1
        if count<0:
            return 0
        return count