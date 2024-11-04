class Solution:
    def compressedString(self, word: str) -> str:
        temp = word[0]
        count = 1
        res = ""
        for i in range(1,len(word)):
            if temp!=word[i]:
                var = count//9
                while var>0:
                    res+=str(9) + temp
                    var-=1
                x = count%9
                if x!=0:
                    res+=str(x) + temp
                count = 1
                temp = word[i]
            else:
                count+=1

        if count!=0:
            var = count//9
            while var>0:
                res+=str(9) + word[-1]
                var-=1
            x = count%9
            if x!=0:
                res+=str(x) + word[-1]
        return res
                
