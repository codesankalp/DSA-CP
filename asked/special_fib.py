def fib(a, b, n, memo={}):
    if n in memo.keys():
        return memo[n]
    if n == 0:
        return a
    if n == 1:
        return b
    memo[n] = fib(a, b, n-1, memo) ^ fib(a, b, n-2, memo)
    print(memo, sep="\n")
    print()
    return memo[n]


for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    ls = [a, b, a ^ b]
    print(ls[n % 3])
