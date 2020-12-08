d1, v1, d2, v2, p = list(map(int, input().split()))
min_day = min(d1, d2)
count = 0
curr_day = min_day
while count < p:

    if curr_day >= d1:
        count += v1
    if curr_day >= d2:
        count += v2
    curr_day += 1
    # print(curr_day, count, d1, d2)

print(curr_day-1)
