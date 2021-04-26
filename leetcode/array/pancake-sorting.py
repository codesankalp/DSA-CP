class Solution:
    def pancakeSort(self, arr):
        n = len(arr)
        sort_arr = [i for i in range(1,n+1)]
        ans = []
        while (arr!=sort_arr):
            i = arr.index(n)
            arr=arr[:i+1][::-1] + arr[i+1:]
            arr=arr[:n][::-1] + arr[n:]
            ans.append(i+1)
            ans.append(n)
            n-=1
        return ans

arr = list(map(int, input().split()))
ans = Solution().pancakeSort(arr)
print(ans)
