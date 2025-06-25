class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move on in s if match found
            j += 1      # always move in t
        return i == len(s)  # if i reached end, s is subsequence