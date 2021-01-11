import time


# time = O(2**n) space = O(n)
def slow_fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


# time = O(n) space = O(n)
def fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if n < 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    n = int(input("Enter Number: "))
    a = time.time()
    print(slow_fib(n))
    print(time.time()-a)
    print(fib(n))
    print(time.time()-a)
