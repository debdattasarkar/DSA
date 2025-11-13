class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        Memoized recursion on indices (i,j): we've formed s3[:i+j].
        Time:  O(n1*n2)
        Space: O(n1*n2) memo + O(n1+n2) stack
        """
        from functools import lru_cache
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        @lru_cache(None)
        def can(i, j):  # i used from s1, j used from s2
            k = i + j
            if k == n3:
                return i == n1 and j == n2
            take1 = i < n1 and s1[i] == s3[k] and can(i + 1, j)
            if take1:
                return True
            take2 = j < n2 and s2[j] == s3[k] and can(i, j + 1)
            return take2

        return can(0, 0)