class Solution:
    def search(self, txt, pat):
        # Edge cases
        if not pat or len(pat) > len(txt):
            return []
        
        # Separator not in lowercase 'a'-'z' (safe per constraints)
        sep = '{'
        S = pat + sep + txt
        
        # ---- Z-array computation: O(|S|)
        n = len(S)
        Z = [0] * n
        L = R = 0  # current Z-box [L, R]
        
        for i in range(1, n):
            if i <= R:
                # Use previously computed values when inside Z-box
                Z[i] = min(R - i + 1, Z[i - L])
            # Extend by direct comparisons
            while i + Z[i] < n and S[Z[i]] == S[i + Z[i]]:
                Z[i] += 1
            # Update Z-box if we extended past R
            if i + Z[i] - 1 > R:
                L, R = i, i + Z[i] - 1
        
        # ---- Collect matches
        m = len(pat)
        ans = []
        for i in range(m + 1, n):  # positions inside txt region
            if Z[i] == m:
                ans.append(i - (m + 1))  # convert to index in txt
        return ans