class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] != ')':
                st.append(s[i])
            else:
                string = ''
                while st and st[-1]!='(':
                    ch = st.pop()
                    string = string + ch
                st.pop()
                for i in range(len(string)):
                    st.append(string[i])
        res = ''
        while st:
            res = st.pop() + res
        return res