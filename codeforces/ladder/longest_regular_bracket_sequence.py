from collections import deque

s = input()
stack = deque()
ls = [0]*1000000
ans = -1

for i in range(len(s)):
    if s[i] == ')':
        if stack:
            r = stack.pop()
            ls[i] = ls[r-1] + (i-r+1)
    else:
        stack.append(i)
    # print(ls, stack)

f_ans = max(ls)
count = ls.count(f_ans)

if f_ans <= 0:
    print(0, 1)
else:
    print(f_ans, count)
