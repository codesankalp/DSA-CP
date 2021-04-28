from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = deque()
        

    def push(self, x: int) -> None:
        if len(self.stack)>=self.n:
            return
        self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        print(k, self.n, self.stack)
        k = min(k, len(self.stack))
        for i in range(k):
            self.stack[i] += val
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
