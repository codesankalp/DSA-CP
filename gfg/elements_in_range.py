class Solution:
    def check_elements(self, arr, n, A, B):
        while(A<=B):
            for i in arr:
                if i==A:
                    break
            else:
                return False
            A+=1
        return True

# Input: N = 7, A = 2, B = 6
# arr[] = {1, 4, 5, 2, 7, 8, 3}
# Output: No
# Explanation: Array does not contain 6.
