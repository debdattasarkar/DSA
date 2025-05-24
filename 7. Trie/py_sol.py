#User function Template for python3

class Solution:
    def wordBreak(self, A, B):
        # Complete this function
        word_set = set(B)
        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                # If A[j:i] is a word and dp[j] is True, then dp[i] is True
                if dp[j] and A[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further

        return 1 if dp[n] else 0