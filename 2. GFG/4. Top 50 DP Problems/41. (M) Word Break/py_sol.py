class Solution:
    def wordBreak(self, s, dictionary):
        """
        Bottom-up DP over prefix length.
        Time:  O(n * Lmax)  (Lmax = longest word length, <= 100 by constraints)
        Space: O(n)
        """
        n = len(s)
        if not dictionary:
            return False
        words = set(dictionary)
        Lmax = max((len(w) for w in words), default=0)

        dp = [False] * (n + 1)
        dp[0] = True  # empty prefix

        for i in range(1, n + 1):
            # Only need to check last Lmax characters
            start = max(0, i - Lmax)
            for j in range(start, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]