class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        c = 0
        S = list(S)
        n = len(S)
        while (i<n):
            if c == 0 and i!=0:
                S[i] = ''
                S[i-1] = ''
                i+=1
                c+=1
                continue
            if S[i] == '(':
                c+=1
            elif S[i]==')':
                c-=1
            i+=1
        S[0] = ''
        S[n-1] = ''
        return ''.join(S)

