class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Loop through the haystack with a sliding window of length equal to needle
        for i in range(len(haystack) - len(needle) + 1):
            # If the substring from i to i+len(needle) matches, return the index
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1  # If no match is found