class Solution:
    def uniquePerms(self, arr):
        # code here 
        """
        Backtracking over value counts.
        - Sort keys; always iterate keys in sorted order -> output is lexicographically sorted.
        Time:   O(K * n) where K = #distinct permutations (<= n!), each append is O(n).
        Space:  O(n) recursion/path + O(u) for freq map, where u = #unique values.
        """
        from collections import Counter

        n = len(arr)
        freq = Counter(arr)
        keys = sorted(freq)        # fixed order ensures lexicographic generation
        path, out = [], []

        def dfs():
            if len(path) == n:     # built one permutation
                out.append(path.copy())
                return
            for x in keys:
                if freq[x] == 0:
                    continue
                freq[x] -= 1
                path.append(x)
                dfs()
                path.pop()
                freq[x] += 1

        dfs()
        return out