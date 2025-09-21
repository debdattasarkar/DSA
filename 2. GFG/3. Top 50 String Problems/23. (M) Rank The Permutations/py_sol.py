#User function Template for python3

class Solution:
	def findRank(self, S):
		n = len(S)
        if n == 0:
            return 0  # or 1 depending on convention; here n>=1 per constraints
        
        # 1) Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i  # Python bigints handle up to 18! easily
        
        # 2) Frequency of available characters (use ASCII range 256 to be general)
        ALPH = 256
        freq = [0] * ALPH
        for ch in S:
            freq[ord(ch)] += 1
        
        # Given: all characters are distinct; but if not, we could early return 0 / handle duplicates.
        
        # 3) Build cumulative counts helper for quick "how many smaller exist?"
        # Instead of recomputing prefix sums each time (O(ALPH) per step),
        # we’ll maintain raw freq and compute the prefix count on the fly,
        # which still keeps us in O(n * ALPH) as expected.
        
        rank = 1  # ranks are 1-based
        for i, ch in enumerate(S):
            code = ord(ch)
            
            # Count how many available characters are strictly smaller than current
            smaller = 0
            for c in range(code):  # O(ALPH) loop; with 26/256 it is fine
                smaller += freq[c]
            
            # Add permutations contributed by choosing each smaller char here
            rank += smaller * fact[n - i - 1]
            
            # Consume current char
            freq[code] -= 1
        
        return rank