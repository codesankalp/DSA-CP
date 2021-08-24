# def check_for_sorting(arr, n):
#     for i in range(1, n-1):
#         if (arr[i] > arr[i+1]):
#             if (arr[i-1]+arr[i+1])>arr[i]:
#                 arr[i-1], arr[i+1] = arr[i+1], arr[i-1]
#             else:
#                 return False
#     return True



# for _ in range(int(input())):
#     n = int(input())
#     ls = (list(map(int, input().split())))
#     if len(ls)==1:
#         print("YES")
#     elif len(ls)==2:
#         if ls[0]>ls[1]:
#             print("NO")
#         else:
#             print("YES")
#     else:
#         if check_for_sorting(ls, n):
#             print("YES")
#         else:
#             print("NO")
        

# def seq(s):
#     s = "".join(set(s))
#     alls=[]
#     k=[]
#     for i in range(len(s)):
#         k = [i for i in s]
#         alls.append("".join(k))
#     print(alls)
#     return alls

# from itertools import combinations

# def seq(s):
#     out = set()
#     for r in range(1, len(s) + 1):
#         for c in combinations(s, r):
#             out.add(''.join(c))
#     out = filter(lambda x: len(x)==len(set(s)),list(out))
#     return sorted(out)


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if (sorted(arr)==arr):
        print("YES")
        return
    else:
        b = sorted(arr)
        i=0
        while (i<n):
            if (arr[i]==arr[i+1]):
                if(b[i]%2==b[i+1]%2):
                    print("NO")
                    return
                else:
                    print("YES")
                    return
            elif (b[i]%2!=0 and i%2!=0):
                continue
            elif (b[i]%2==0 and i%2==0):
                continue
            else:
                print("NO")
                return
                

for _ in range(int(input())):
    solve()
        