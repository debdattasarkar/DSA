
class Solution:
    def findCatalan(self, n):
        """
        DP recurrence:
          C[0] = 1
          C[k] = sum_{i=0..k-1} C[i] * C[k-1-i]   for k >= 1

        Time:  O(n^2)   (double loop)
        Space: O(n)     (array of C[0..n])
        """
        if n <= 1:
            return 1

        C = [0] * (n + 1)
        C[0] = 1
        C[1] = 1

        for k in range(2, n + 1):            # O(n)
            s = 0
            for i in range(k):               # sum k terms -> O(k)
                s += C[i] * C[k - 1 - i]
            C[k] = s
        return C[n]