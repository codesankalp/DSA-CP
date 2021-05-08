from itertools import combinations


def replace(s):
    ans = ''
    for j, k in enumerate(s):
        if k == '?':
            if j-1 != -1:
                if s[j-1] == '?':
                    if ans[-1] == '0':
                        ans += '1'
                    else:
                        ans += '0'
                elif s[j-1] == '0':
                    ans += '1'
                else:
                    ans += '0'
            else:
                if j+1 >= len(s):
                    ans += '0'
                else:
                    if s[j+1] == '?':
                        ans += '1'
                    elif s[j+1] == '0':
                        ans += '1'
                    else:
                        ans += '0'
        else:
            ans += k
    return ans


for _ in range(int(input())):
    s = input()
    s1 = s.replace('?', '0')
    s2 = s.replace('?', '1')
    res = [s[x:y] for x, y in combinations(
        range(len(s) + 1), r=2)]
    ans = 0
    for i in res:
        s1 = replace(i)
        if s1 == '0' or s1 == '1':
            ans += 1
        elif '00' in s1 or '11' in s1:
            continue
        else:
            ans += 1
    print(ans)
