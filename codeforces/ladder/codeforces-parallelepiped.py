a1, a2, a3 = list(map(int, input().split()))
b = ((a1*a2)/a3)**0.5
l = (a3/a2)*b
h = a2/b
print(4*int(l+b+h))
