class Solution:
	def editDistance(self, s1, s2):
		from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            # edits to convert s1[i:] -> s2[j:]
            if i == len(s1):  # only inserts left
                return len(s2) - j
            if j == len(s2):  # only deletes left
                return len(s1) - i

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)  # no cost

            ins  = 1 + dfs(i, j + 1)     # insert s2[j]
            dele = 1 + dfs(i + 1, j)     # delete s1[i]
            repl = 1 + dfs(i + 1, j + 1) # replace s1[i]→s2[j]
            return min(ins, dele, repl)

        return dfs(0, 0)