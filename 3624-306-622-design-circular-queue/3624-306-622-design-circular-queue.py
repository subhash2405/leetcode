class MyCircularQueue:

    def __init__(self, k: int):
        self.count = 0
        self.start = 0
        self.arr = [-1]*k
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        x = (self.start+self.count)%self.size
        self.arr[x] = value
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start+1)%self.size
        self.count-=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        x = (self.start+self.count-1)%self.size
        return self.arr[x]

    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count==self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()