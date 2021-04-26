class Solution():
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = sum(arr)/3
        n = len(arr)
        temp, s_i, s_j = 0, 0, 0
        for i in range(n):
            temp += arr[i]
            if temp == s:
                s_i = i
                break
        else:
            return False
        temp = 0
        for j in range(n-1, s_i, -1):
            temp += arr[j]
            if temp == s:
                s_j = j
                break
        else:
            return False
        temp = 0
        for k in range(s_i+1, s_j):
            temp += arr[k]
            if temp == s:
                return True
        return False

a = Solution()
arr = list(map(int, input().split()))
ans = a.canThreePartsEqualSum(arr)
print(ans)