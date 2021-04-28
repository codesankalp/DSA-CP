from collections import deque
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        n = len(ops)
        for i in range(n):
            if ops[i] == '+':
                ops.append(ops[-1]+ops[-2])
            elif ops[i]=='C':
                ops.pop()
            elif ops[i]=='D':
                ops.append(2*ops[-1])
            else:
                ops.append(int(ops[i]))
        return sum(ops[n:])
