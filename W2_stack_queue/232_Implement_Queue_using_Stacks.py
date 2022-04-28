from collections import deque

class MyQueue:

    def __init__(self):
        self.st0 = deque()
        self.st1 = deque()

        
    def push(self, x: int) -> None:
        self.st0.append(x)
        
    def pop(self) -> int:
        if(len(self.st0)<2):
            pop = self.st0.pop()
        else:
            while(len(self.st0) > 1):
                self.st1.append(self.st0.pop())
            pop = self.st0.pop()
            while(len(self.st1) > 0):
                self.st0.append(self.st1.pop())
        return pop
        
    def peek(self) -> int:
        if(len(self.st0)<2):
            peek = self.st0.pop()
            self.st0.append(peek)
        else:
            while(len(self.st0) > 1):
                self.st1.append(self.st0.pop())
            peek = self.st0.pop()
            self.st0.append(peek)
            while(len(self.st1) > 0):
                self.st0.append(self.st1.pop())
        return peek
    
    def empty(self) -> bool:
        if(len(self.st0) == 0):
            return True
        else:
            return False
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()