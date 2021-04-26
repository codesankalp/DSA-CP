from math import ceil

class Solution:
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        n =len(s)
        a = 0
        while a<n:
            if s[a] in vowels:
                if s[n-1] in vowels:
                    s[a], s[n-1] = s[n-1], s[a]
                    a += 1
                    n -= 1
                else:
                    n-=1
            else:
                a+=1

        return ''.join(s)

a = Solution()
s = input()
ans = a.reverseVowels(s)
print(ans)
