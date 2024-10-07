class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for var in s:
            if len(st)==0:
                st.append(var)
            else:
                if (var == 'B' and st[-1] == 'A') or (var == 'D' and st[-1] == 'C'):
                    st.pop()
                else:
                    st.append(var)
        
        
        return len(st)