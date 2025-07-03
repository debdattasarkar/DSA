class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings are isomorphic.
        A character in string s must map uniquely to a character in t and vice versa.

        Time Complexity: O(n)
        Space Complexity: O(1)  (since mappings are limited to 256 ASCII characters)
        """

        # Dictionary to store mapping from characters in s to characters in t
        map_s_t = {}  # e.g., {'a': 'x'}
        # Dictionary to store reverse mapping from t to s
        map_t_s = {}  # e.g., {'x': 'a'}

        # Iterate over both strings in parallel
        for cs, ct in zip(s, t):  # O(n) where n = len(s)

            # If cs is already mapped, ensure it maps to ct
            if cs in map_s_t:
                if map_s_t[cs] != ct:
                    return False  # Mismatch in mapping

            # If not already mapped, add mapping cs → ct
            else:
                map_s_t[cs] = ct

            # Similarly, check reverse mapping for ct → cs
            if ct in map_t_s:
                if map_t_s[ct] != cs:
                    return False  # Mismatch in reverse mapping
            else:
                map_t_s[ct] = cs

        return True  # All mappings are consistent
    
s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))  # Output: True