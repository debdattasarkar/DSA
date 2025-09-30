#User function Template for python3

class Solution:
    def palPartition(self, s):
        """
        Build isPal[i][j] in O(n^2), then compute cuts[i] (min cuts for s[:i+1]).
        Time:  O(n^2)
        Space: O(n^2) for isPal, O(n) for cuts
        """
        n = len(s)
        if n <= 1:
            return 0

        # ---- Palindrome DP table: isPal[i][j] ----
        isPal = [[False] * n for _ in range(n)]  # O(n^2) space
        for i in range(n):
            isPal[i][i] = True  # single char

        # length >= 2
        for length in range(2, n + 1):                  # O(n)
            for i in range(0, n - length + 1):          # O(n)
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i + 1][j - 1]

        # ---- cuts[i] = min cuts for s[:i+1] ----
        cuts = [0] * n                                  # O(n) space
        for i in range(n):                              # O(n)
            if isPal[0][i]:
                cuts[i] = 0
            else:
                best = i  # worst case: cut before each char
                for j in range(i):                      # O(n) total per i
                    if isPal[j + 1][i]:
                        best = min(best, cuts[j] + 1)
                cuts[i] = best

        return cuts[-1]