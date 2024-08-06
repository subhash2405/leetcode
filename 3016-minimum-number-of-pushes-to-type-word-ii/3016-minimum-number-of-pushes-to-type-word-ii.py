class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        arr = []
        for i in range(len(word)):
            if word[i] not in count:
                arr.append(word[i])
                count[word[i]] = 1
            else:
                count[word[i]]+=1
        if len(arr)<=8:
            return len(word)
        sort = sorted(count.items(), key = lambda x:x[1], reverse = True)
        res = 0
        for i in range(len(sort)):
            if i<8:
                res+=sort[i][1]
            elif i>=8 and i<16:
                res+=2*sort[i][1]
            elif i>=16 and i<24:
                res+=3*sort[i][1]
            else:
                res+=4*sort[i][1]
        return res