from collections import deque
class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = deque()
        self.size = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue.append(value)
            return True
        return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue.popleft()
            return True
        return False
        

    def Front(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[-1]
        return -1
        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue)>=self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
