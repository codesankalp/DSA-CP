class Solution:
    def sortArrayByParity(self, A:list) -> list:
        odds = []
        evens = []
        for num in A:
            if num%2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        evens.extend(odds)
        return evens


ls = list(map(int, input().split()))
a = Solution()
ans = a.sortArrayByParity(ls)
print(ans)
