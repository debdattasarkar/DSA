class Solution:
    def numberOfWays(self, n):
        """
        Memoized recursion (DFS + cache).
        Time:  O(n)     (each state computed once)
        Space: O(n)     (memo + recursion stack)
        """
        from functools import lru_cache

        @lru_cache(None)
        def ways(k):
            if k == 0 or k == 1:
                return 1
            return ways(k - 1) + ways(k - 2)

        return ways(n)