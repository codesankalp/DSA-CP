class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        n, ans = len(arr), 0
        for i in range(n):
            for j in range(i+1,n):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1, n):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            ans+=1
        return ans

arr = list(map(int, input('array: ').split()))
a, b, c = list(map(int, input('a, b, c: ').split()))
d = Solution()
ans = d.countGoodTriplets(arr, a, b, c)
print(ans)
