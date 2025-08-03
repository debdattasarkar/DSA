class Solution:
    def cuts(self, s):
        # code here
        n = len(s)

        # Precompute powers of 5 in binary
        powers = set()
        val = 1
        while val <= int('1' * n, 2):
            powers.add(bin(val)[2:])
            val *= 5

        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No cuts for empty string

        for i in range(n):
            if s[i] == '0':
                continue  # Skip leading zero
            for j in range(i + 1, n + 1):
                if s[i:j] in powers:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1