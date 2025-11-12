class Solution:
    def wildCard(self, txt, pat):
        """
        dp(i, j) => does pat[i:] match txt[j:] ?
        Time:  O(n*m) states, O(1) per state
        Space: O(n*m) memo + recursion
        """
        from functools import lru_cache
        n, m = len(txt), len(pat)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return j == n
            if j == n:
                # pattern remainder must be only '*' to match empty
                return all(ch == '*' for ch in pat[i:])

            p = pat[i]
            if p == '*':
                # '*' is empty OR consumes one text char
                return dp(i + 1, j) or dp(i, j + 1)
            if p == '?' or p == txt[j]:
                return dp(i + 1, j + 1)
            return False

        return dp(0, 0)