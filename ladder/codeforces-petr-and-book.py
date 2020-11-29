n = int(input())
ls = list(map(int, input().split()))
i = 0
s = 0
while i<=len(ls):
    if i == len(ls):
        i=0
    s += ls[i]
    if s>= n:
        print(i+1)
        break
    i += 1
