from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input example
        # s = "anagram", t = "nagaram"
        
        # Step 1: If strings are of different lengths, they can't be anagrams.
        # Time Complexity: O(1), Space: O(1)
        if len(s) != len(t):
            return False

        # Step 2: Count character frequencies in both strings
        # Time Complexity: O(n), where n is the length of the strings
        # Space Complexity: O(1) (bounded to 26 lowercase letters)
        s_count = Counter(s)  # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        t_count = Counter(t)  # {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

        # Step 3: Compare the two frequency dictionaries
        # Time Complexity: O(1), since max 26 keys (lowercase)
        return s_count == t_count

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))  # Output: True