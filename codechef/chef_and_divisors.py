l=100
fac = [0]*l
ls = [0]*l
for i in range(1, l):
    for j in range(i, l, i):
        fac[j] += 1
        ls[j] += 1

for i in range(1, l):
    for j in range(i, l, i):
        if fac[j//i] == 4:
            ls[j] = min(ls[j], ls[i])

print(fac, ls, sep="\n\n")
for _ in range(int(input())):
    n = int(input())
    print(ls[n])
    