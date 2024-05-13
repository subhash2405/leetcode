class Solution:
    def reverseWords(self, s: str) -> str:
        st = ''
        ans = ''
        for i in range(len(s)-1, -1, -1):
            if s[i]!=' ':
                st =  s[i] + st
            else:
                if st!='':
                    ans = ans + st + " "
                    st = ''
        if st!='':
            ans = ans+st
        else:
            ans = ans.rstrip()
        return ans