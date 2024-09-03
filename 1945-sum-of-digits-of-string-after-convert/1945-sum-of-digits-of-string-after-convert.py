class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ''
        for i in range(len(s)):
            num = ord(s[i])-96
            st+=str(num)
        var = 0
        add = 0
        while var<k:
            for j in range(len(st)):
                add+=int(st[j])
            st = str(add)
            temp = add
            add = 0
            var+=1
        return temp