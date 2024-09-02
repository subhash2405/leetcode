class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = Counter(s)
        res = []
        l = 0
        r = 0
        st = set()
        while r<len(s):
            st.add(s[r])
            arr[s[r]]-=1
            if arr[s[r]]==0:
                st.remove(s[r])
            if len(st)==0:
                res.append(r-l+1)
                l = r+1
            r+=1
        return res

        # print(arr)
        # res = []
        # partition = set()
        # index = 1
        # for var in s:
        #     partition.add(var)
        #     flag = 0  
        #     arr[var]-=1     
        #     for j in partition:
        #         if arr[j]!=0:
        #             flag=1
        #     if flag==0:
        #         res.append(index)
        #         partition  = set()
        #         index=0
        #     index+=1
        # return res