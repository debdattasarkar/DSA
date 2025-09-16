#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        """
        Count surplus letters in s1 relative to s2.
        Time : O(n)   (one pass to count, one pass to compare 26 letters)
        Space: O(1)   (26-int array for lowercase)
        """
        if len(s1) != len(s2):
            return False  # must be same length

        # Frequency arrays for 'a'..'z'
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        base = ord('a')

        for ch in s1:           # O(n)
            cnt1[ord(ch) - base] += 1
        for ch in s2:           # O(n)
            cnt2[ord(ch) - base] += 1

        # Surplus in s1 only
        changes = 0
        for c in range(26):     # O(26) == O(1)
            if cnt1[c] > cnt2[c]:
                changes += cnt1[c] - cnt2[c]

        return changes <= k