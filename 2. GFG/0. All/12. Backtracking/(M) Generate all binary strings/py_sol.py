class Solution:
    def binstr(self, n):
        """
        Generate all n-bit binary strings in ascending order.
        Time:  O(n * 2^n)  — we write n chars for each of 2^n strings
        Space: O(n)        — recursion depth; O(2^n) extra if we store results
        """
        out = []
        
        def dfs(pos, path_chars):
            if pos == n:
                out.append("".join(path_chars))  # reached length n
                return
            # choose '0' first, then '1' to ensure ascending order
            path_chars.append('0')
            dfs(pos + 1, path_chars)
            path_chars.pop()

            path_chars.append('1')
            dfs(pos + 1, path_chars)
            path_chars.pop()

        dfs(0, [])
        return out