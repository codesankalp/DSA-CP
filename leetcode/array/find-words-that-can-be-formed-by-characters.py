class Solution:
    def countCharacters(self, words, chars: str) -> int:
        ans = 0
        for word in words:
            for char in word:
                if word.count(char)> chars.count(char):
                    break
            else:
                ans += len(word)
        return ans

words = list(input().split())
chars = input()
ans = Solution().countCharacters(words, chars)
print(ans)

