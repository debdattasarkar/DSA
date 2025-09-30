#User function Template for python3

class Solution:
	def solveWordWrap(self, arr, k):
		"""
        Bottom-up DP:
          dp[i] = minimum cost to wrap words starting at i (0-based)
        Transitions consider putting words i..j on the next line if feasible.

        Time:  O(n^2)    — for each i we may try all j >= i until width exceeds k
        Space: O(n)      — dp + prefix sums
        """
        n = len(arr)
        # Edge case: no words
        if n == 0:
            return 0

        # Prefix sum of word lengths to get sum(arr[i..j]) in O(1)
        pref = [0] * (n + 1)      # O(n) space
        for i in range(n):        # O(n) time
            pref[i + 1] = pref[i] + arr[i]

        def words_sum(i, j):      # O(1)
            return pref[j + 1] - pref[i]

        # dp[n] = 0 (no words left)
        dp = [0] * (n + 1)        # O(n) space
        dp[n] = 0

        # Fill dp from right to left — O(n^2)
        for i in range(n - 1, -1, -1):
            best = float('inf')
            # Try all feasible j starting at i
            j = i
            while j < n:
                # len on line i..j includes single spaces between words
                length = words_sum(i, j) + (j - i)  # (j-i) spaces
                if length > k:
                    break  # further j will only get longer
                # Last line cost is 0 else square of extras
                if j == n - 1:
                    cost = 0
                else:
                    extras = k - length
                    cost = extras * extras
                # Candidate
                best = min(best, cost + dp[j + 1])
                j += 1
            dp[i] = best

        return dp[0]