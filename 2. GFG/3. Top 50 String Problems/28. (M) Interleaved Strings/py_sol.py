class Solution:
    def isInterleave(self, s1, s2, s3):
        # Quick length check: O(1)
        if len(s1) + len(s2) != len(s3):
            return False

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, j):
            k = i + j
            if k == len(s3):                      # reached end
                return i == len(s1) and j == len(s2)

            # Option 1: take next from s1 if it matches s3[k]
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1, j):
                return True

            # Option 2: take next from s2 if it matches s3[k]
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j+1):
                return True

            return False

        return dfs(0, 0)