from collections import Counter
class Solution:
	def topKFreq(self, arr, k):
		"""
        1) Count frequencies
        2) Sort unique values by (-freq, -value) to honor:
           - higher frequency first
           - on ties, larger value first
        Time  : O(n log m) where m = #distinct (≤ n)
        Space : O(m)
        """
        freq = Counter(arr)                                # O(n)
        ranked = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))  # O(m log m)
        return [val for val, _ in ranked[:k]]