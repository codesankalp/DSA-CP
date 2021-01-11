days = 120
for _ in range(int(input())):
    n = int(input())
    b = input()
    p = ((days-b.count('0'))/days)*100
    if p >= 75:
        print("YES")
    else:
        print("NO")
