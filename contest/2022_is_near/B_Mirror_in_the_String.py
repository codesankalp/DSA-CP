for _ in range(int(input())):
    n = int(input())
    s = input()
    prev_min = s[0] + s[0]
    for i in range(1, n):
        sub_str = s[: i + 1]
        rev_str = sub_str[::-1]
        if prev_min < sub_str + rev_str:
            break
        else:
            prev_min = sub_str + rev_str
    print(prev_min)
