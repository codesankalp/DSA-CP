n = int(input())
x = 0
for i in range(n):
    op = input().split('X')
    if op[0] == '++' or op[1] == '++':
        x+=1
    elif op[0] == '--' or op[1] == '--':
        x-=1
print(x)
