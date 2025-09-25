class Solution:
    def search(self, pat, txt):
        # code here
        n, m = len(txt), len(pat)
        if m > n:
            return []

        base = 256  # ASCII
        mod = 10**9 + 7

        # Compute hash of pattern and first window
        pat_hash = 0
        txt_hash = 0
        h = 1  # base^(m-1)

        for i in range(m - 1):
            h = (h * base) % mod

        for i in range(m):
            pat_hash = (pat_hash * base + ord(pat[i])) % mod
            txt_hash = (txt_hash * base + ord(txt[i])) % mod

        res = []
        for i in range(n - m + 1):
            if pat_hash == txt_hash:
                if txt[i:i + m] == pat:
                    res.append(i + 1)  # 1-based indexing

            if i < n - m:
                txt_hash = (txt_hash - ord(txt[i]) * h) % mod
                txt_hash = (txt_hash * base + ord(txt[i + m])) % mod
                txt_hash = (txt_hash + mod) % mod  # avoid negative

        return res