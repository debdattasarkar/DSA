class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       # Early exit if lengths differ
        if len(s1) != len(s2):
            return False

        # Time: O(n), Space: O(1) since fixed size 26
        freq = [0] * 26  # For 'a' to 'z'

        for c1, c2 in zip(s1, s2):
            freq[ord(c1) - ord('a')] += 1
            freq[ord(c2) - ord('a')] -= 1

        return all(f == 0 for f in freq)