class Solution:
    def getLongestPrefix(self, s):
        # code here
        n = len(s)
        if n <= 1:
            return -1
        
        # --- Build prefix-function (pi) in O(n) ---
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        
        # Walk down the border chain to find the smallest positive border
        b = pi[-1]
        if b == 0:
            return -1  # no positive border -> no period
        while pi[b - 1] > 0:
            b = pi[b - 1]
        
        # largest period = n - (smallest positive border)
        return n - b
