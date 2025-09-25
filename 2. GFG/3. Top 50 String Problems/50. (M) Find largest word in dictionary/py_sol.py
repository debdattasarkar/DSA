#User function Template for python3
class Solution:
    def findLongestWord (ob, S, d):
        """
        Check each dictionary word with a two-pointer subsequence test.
        Time:  O(|S| * |d|) worst-case (each word scans S once)
        Space: O(1)
        """
        def is_subseq(word: str, s: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            # walk s; advance j when we match word[j]
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m

        best = ""
        for w in d:
            if is_subseq(w, S):
                # choose longer; on tie choose lexicographically smaller
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best