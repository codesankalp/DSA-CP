from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


for _ in range(int(input())):
    n = int(input())
    factor = factors(n)
    factor.remove(1)
    print(min(factor))