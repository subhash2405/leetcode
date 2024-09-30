class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.st)<self.size:
            self.st.append(x)

    def pop(self) -> int:
        # print(self.st)
        return self.st.pop() if len(self.st)!=0 else -1

    def increment(self, k: int, val: int) -> None:
        if len(self.st)>=k:
            for i in range(k):
                self.st[i]+=val
        else:
            for i in range(len(self.st)):
                self.st[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)