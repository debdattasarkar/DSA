class Solution:
	def distinctSubsequences(self, s):
		MOD = 1_000_000_007
        n = len(s)

        # dp[i] = # of distinct subsequences of s[:i], including ""
        # Time to fill: O(n); Space: O(n)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base: empty string has one subsequence ""

        # last[pos] holds last 1-based index where char occurred; 0 means unseen.
        # For lowercase English letters, we can store in an array of size 26.
        last = [0] * 26

        for i in range(1, n + 1):
            c_idx = ord(s[i - 1]) - ord('a')
            # Double the count: include-or-exclude current char
            dp[i] = (2 * dp[i - 1]) % MOD

            # If we've seen this character before, subtract duplicates created earlier
            if last[c_idx] != 0:
                dp[i] = (dp[i] - dp[last[c_idx] - 1] + MOD) % MOD  # +MOD to avoid negative mod

            # Update last occurrence to current position (1-based)
            last[c_idx] = i

        # dp[n] is the number of distinct subsequences of s
        return dp[n]