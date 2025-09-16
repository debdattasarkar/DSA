from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        """
        Sliding window with frequency map.
        Time : O(n)  — each index enters/leaves window once
        Space: O(1)  — at most 26 keys for lowercase alphabet (otherwise O(k))
        """
        n = len(s)
        if k == 0:
            return -1
        freq = defaultdict(int)
        left = 0
        best = -1

        for right, ch in enumerate(s):
            freq[ch] += 1  # include s[right]

            # shrink until we have at most k distinct
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # if exactly k distinct, update best
            if len(freq) == k:
                best = max(best, right - left + 1)

        return best