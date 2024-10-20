class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for s in expression:
            if s==',' or s=='(':
                continue
            if s in ['t','f','!','&','|']:
                st.append(s)
            elif s == ')':
                flag1 = 0
                flag2 = 0
                while st[-1] not in ["!","&","|"]:
                    var = st.pop()
                    if var=='t':
                        flag1 = 1
                    elif var == 'f':
                        flag2 = 1
                op = st.pop()
                if op=='!':
                    st.append('t' if not flag1 else 'f')
                elif op=='&':
                    st.append('f' if flag2 else 't')
                else:
                    st.append('t' if flag1 else 'f')
        return st[-1]=='t'

                
