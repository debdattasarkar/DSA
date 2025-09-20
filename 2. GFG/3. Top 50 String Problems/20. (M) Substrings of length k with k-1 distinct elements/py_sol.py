class Solution:
    def substrCount(self, s, k):
        """
        Count substrings of length k that have exactly k-1 distinct characters.
        Sliding window of fixed size k, maintain distinct count in O(1).

        Time : O(n)
        Space: O(1) for 26 lowercase letters
        """
        n = len(s)
        if k > n:
            return 0

        freq = [0] * 26
        def idx(c): return ord(c) - 97  # 'a'..'z'

        distinct = 0
        ans = 0

        # build first window
        for i in range(k):
            j = idx(s[i])
            if freq[j] == 0:
                distinct += 1
            freq[j] += 1
        if distinct == k - 1:
            ans += 1

        # slide
        for i in range(k, n):
            # add right char
            r = idx(s[i])
            if freq[r] == 0:
                distinct += 1
            freq[r] += 1

            # remove left char
            l = idx(s[i - k])
            freq[l] -= 1
            if freq[l] == 0:
                distinct -= 1

            if distinct == k - 1:
                ans += 1

        return ans