class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in range(len(tokens)):
            # if (tokens[i]=="+" or tokens[i]=="-" or tokens[i]=="*" or tokens[i]=="/") :
            if tokens[i] in {"+","-","*","/"}:
                x=int(st.pop())
                y=int(st.pop())
                if tokens[i]=="+":
                    st.append(x+y)
                    # print("+"+""+str(st[-1]))
                if tokens[i]=="-":
                    st.append(y-x)
                    # print("-"+""+str(st[-1]))
                if tokens[i]=="*":
                    st.append(x*y)
                    # print("*"+""+str(st[-1]))
                if tokens[i]=="/":
                    st.append(int(y/x))
                    # print("/"+""+str(st[-1]))
            else:
                st.append(int(tokens[i]))
        return st[-1]
                

        