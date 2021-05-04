from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.counter = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # cnt = 0
        self.counter.append(t)
        while self.counter[0]<t-3000:
            self.counter.popleft()
        return len(self.counter)
        # for i in self.counter[::-1]:
        #     if i>=t-3000 and i<=t:
        #         cnt+=1
        #     else:
        #         break
        # return cnt
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
