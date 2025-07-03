class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Early return if lengths mismatch
        if len(s) != len(t):
            return False

        # Step 2: Count characters in both strings
        s_count = Counter(s)  # O(n)
        t_count = Counter(t)  # O(n)

        # Step 3: Compare both dictionaries
        return s_count == t_count