#User function Template for python3

class Solution:
	def shortestDistance(self, s, word1, word2):
		"""
        Single scan with last-seen indices.
        Time : O(n)  |  Space : O(1)
        Judge convention: if word1 == word2, answer is 0.
        """
        if word1 == word2:
            return 0  # <- required by this judge

        last1 = last2 = -1
        ans = float('inf')

        for i, w in enumerate(s):
            if w == word1:
                last1 = i
                if last2 != -1:
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d
            elif w == word2:
                last2 = i
                if last1 != -1:
                    d = abs(last1 - last2)
                    if d < ans:
                        ans = d

        return -1 if ans == float('inf') else ans