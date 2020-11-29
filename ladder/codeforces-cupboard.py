n = int(input())
l = []
r = []
for i in range(n):
    a,b = input().split()
    l.append(a)
    r.append(b)
ans1 = 0
ans2 = 0
if l.count('1')>=l.count('0'):
    ans1 = l.count('0')
else:
    ans1 = l.count('1')
if r.count('1')>=r.count('0'):
    ans2 = r.count('0')
else:
    ans2 = r.count('1')
print(ans1+ans2)
