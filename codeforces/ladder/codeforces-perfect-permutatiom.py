def printPermutation(n): 
      
    # If n is odd 
    if (n % 2 != 0): 
        print(-1); 
  
    # Otherwise 
    else: 
        for i in range(1, (n // 2) + 1): 
            print((2 * i), (2 * i - 1), end = " ");
  
# Driver code 
n = int(input())
printPermutation(n)
