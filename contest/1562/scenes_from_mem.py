from itertools import combinations

def isPrime(num):
    if num <= 1:
        return False

    for x in range(2, num):
        # if number is divisble by x, return False
        if not num % x:
            return False
    return True

for _ in range(int(input())):
    k = int(input())
    x = input()
    n=1
    found = False
    while(n<=k):
        ls = [''.join(l) for l in list(combinations(x,n))]
        # print(ls)
        for i in ls:
            if isPrime(int(i)):
                continue
            else:
                print(len(i))
                print(i)
                n=k+1
                break
        n+=1
    if (n==k+1):
        print(1)
        print(1)
