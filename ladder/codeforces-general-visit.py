n = int(input())
h_lst = list(map(int, input().split()))
h_max = max(h_lst)
pos_max = h_lst.index(h_max)
# print(h_max,pos_max)
h_rev = h_lst[::-1]
h_min  = min(h_rev)
pos_min = h_rev.index(h_min)
# print(h_min,pos_min)
ans = pos_max+pos_min
if len(h_lst)-1-pos_min < pos_max:
    print(ans-1)
else:
    print(ans)
