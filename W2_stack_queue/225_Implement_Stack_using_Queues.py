from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        if(self.q1.qsize() == 1):
            self.q2.put(self.q1.get())
        self.q1.put(x)

    def pop(self) -> int:
        if(not self.q1.empty()):
            p = self.q1.get()
        else:
            p = None
        
        # fill in the q1
        while(not self.q2.empty()):
            self.q1.put(self.q2.get())
        # move from q1 to q1 except one
        while((self.q1.qsize() != 1) and (not self.q1.empty())):
            self.q2.put(self.q1.get())
        
        return p

    def top(self) -> int:
        if (not self.q1.empty()):
            tmp = self.q1.get()
            self.q1.put(tmp)
            return tmp
        else:
            return None

    def empty(self) -> bool:
        if (self.q1.empty() and self.q2.empty()):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()