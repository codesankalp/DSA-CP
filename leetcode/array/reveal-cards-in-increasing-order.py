from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        n = len(deck)
        ans = [0]*n
        index = deque([i for i in range(n)])
        
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ans

ls = list(map(int, input().split()))
a = Solution()
ans = a.deckRevealedIncreasing(ls)
print(ans)
