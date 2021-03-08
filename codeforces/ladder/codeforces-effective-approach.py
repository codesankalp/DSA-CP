arr = [0]*100001
vasya = 0
petya = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n+1):
    arr[a[i-1]] = i
m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    vasya += arr[b[i]]
    petya += (n+1-arr[b[i]])
print(int(vasya), int(petya))
