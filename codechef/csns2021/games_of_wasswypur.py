
for _ in range(int(input())):
    n = int(input())
    s = input()
    start = s[0]
    count = 1
    for i in range(n):
        if start != s[i]:
            start = s[i]
            count += 1
        # print(count, start)

    block_sum = 1
    for i in range(1, n):
        if s[i-1] != s[i]:
            block_sum += 1
    l = block_sum
    # print(count, l, count == l)
    if l == 1:
        print("SAHID")
    elif l == 2:
        print("RAMADHIR")
    else:
        if l % 3 == 0:
            print("SAHID")
        elif l % 3 == 1:
            print("SAHID")
        else:
            print("RAMADHIR")

# SAHID
# SAHID
# SAHID
# SAHID
# RAMADHIR
# RAMADHIR

# SAHID
# RAMADHIR
# SAHID
# RAMADHIR
# SAHID
# SAHID
