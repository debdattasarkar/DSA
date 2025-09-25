class Solution:
    def rabinKarp(self, text, pattern):
        n, m = len(text), len(pattern)
        if m == 0 or m > n:
            return []

        # Rolling-hash parameters
        B = 256          # base (covers lowercase ASCII)
        M = 10**9 + 7    # large prime modulus

        # Precompute B^(m-1) % M to remove the leftmost char in O(1)
        power = pow(B, m - 1, M)

        # Initial hashes for pattern and first window in text
        ph = 0  # pattern hash
        th = 0  # text window hash
        for i in range(m):
            ph = (ph * B + ord(pattern[i])) % M
            th = (th * B + ord(text[i])) % M

        res = []

        # Slide over all windows
        for i in range(n - m + 1):
            # On hash match, verify to avoid false positives
            if ph == th and text[i:i + m] == pattern:
                res.append(i)  # return 0-based index

            # Roll the hash: remove left char, add right char
            if i < n - m:
                left = (ord(text[i]) * power) % M
                th = (th - left) % M
                th = (th * B + ord(text[i + m])) % M

        return res