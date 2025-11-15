class Solution:
    def LCIS(self, a, b):
        """
        dp[j] = length of LCIS that ends exactly at b[j].
        For each a[i], sweep b left->right keeping best_len_of_smaller.
        Time:  O(n*m)
        Space: O(m)
        """
        m = len(b)
        dp = [0] * m

        for x in a:                      # O(n)
            best_len_of_smaller = 0
            for j in range(m):           # O(m)
                if b[j] < x:
                    # any LCIS ending at b[j] can be extended by x later
                    if dp[j] > best_len_of_smaller:
                        best_len_of_smaller = dp[j]
                elif b[j] == x:
                    # we can end the LCIS at b[j] using x now
                    if best_len_of_smaller + 1 > dp[j]:
                        dp[j] = best_len_of_smaller + 1
        return max(dp, default=0)