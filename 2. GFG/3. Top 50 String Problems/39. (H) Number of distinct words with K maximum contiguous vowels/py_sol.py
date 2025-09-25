# User function Template for python3
MOD = 1_000_000_007

class Solution:
    def kvowelwords(self, N,K):
		# Rolling DP over "j = number of trailing vowels"
        # prev[j] = count of length i-1 strings ending with j consecutive vowels
        prev = [0] * (K + 1)
        prev[0] = 1  # empty string
        
        for _ in range(1, N + 1):
            total_prev = sum(prev) % MOD
            curr = [0] * (K + 1)
            
            # Append a consonant -> resets trailing vowel run to 0
            curr[0] = (21 * total_prev) % MOD
            
            # Append a vowel -> j from 1..K
            for j in range(1, K + 1):
                curr[j] = (5 * prev[j - 1]) % MOD
            
            prev = curr
        
        return sum(prev) % MOD