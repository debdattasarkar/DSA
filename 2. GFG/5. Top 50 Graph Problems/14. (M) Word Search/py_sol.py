class Solution:
	def isWordExist(self, mat, word):
		"""
        Backtracking DFS: try to match the word starting at every cell.
        When visiting a cell, mark it (e.g., '#') to avoid reuse, then restore.

        Let n,m be grid dims, k=len(word).
        Time  : O(n*m*3^k) average; worst-case O(n*m*4^k)
        Space : O(k) recursion (no extra visited matrix if we mark in-place)
        """
        if not mat or not mat[0] or not word:
            return False

        n, m = len(mat), len(mat[0])
        W = len(word)

        # Small pre-pruning: if grid doesn't even contain enough occurrences
        # of any char in 'word', it's impossible.
        from collections import Counter
        need = Counter(word)
        have = Counter(ch for row in mat for ch in row)
        for ch, cnt in need.items():
            if have[ch] < cnt:
                return False

        # Directions: 4-adjacent
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, k):
            """Return True if we can match word[k:] starting from mat[r][c]."""
            if mat[r][c] != word[k]:
                return False
            if k == W - 1:           # matched the last char
                return True

            # mark visited
            tmp = mat[r][c]
            mat[r][c] = '#'          # any sentinel not in 'A'..'Z'/'a'..'z'

            # try neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] != '#':
                    if mat[nr][nc] == word[k + 1] and dfs(nr, nc, k + 1):
                        mat[r][c] = tmp
                        return True

            # backtrack
            mat[r][c] = tmp
            return False

        # Try only cells matching first letter for fewer starts
        first = word[0]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == first and dfs(i, j, 0):
                    return True
        return False