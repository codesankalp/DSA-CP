for _ in range(int(input())):
    s = (input())
    z = s.count('0')
    o = s.count('1')
    if len(s) % 2 == 0 and not (z == len(s) or o == len(s)):
        print(len(s)//2-min(z, o))
    else:
        print(-1)
