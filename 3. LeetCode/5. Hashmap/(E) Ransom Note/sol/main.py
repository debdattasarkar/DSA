from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Count frequency of each character in magazine
        # Time: O(m), where m = len(magazine)
        # Space: O(1) since at most 26 lowercase letters (constant)
        magazine_count = Counter(magazine)
        
        # Step 2: For each character in ransomNote, check if it's available in magazine_count
        # Time: O(n), where n = len(ransomNote)
        # Space: O(1) for the loop, no extra data structure created
        for char in ransomNote:
            if magazine_count[char] == 0:
                # Char either not present or already used up
                return False
            magazine_count[char] -= 1  # Use one instance of the character
        
        # If we got here, all characters were available
        return True

# Test code
sol = Solution()
print(sol.canConstruct("a", "b"))        # False
print(sol.canConstruct("aa", "ab"))      # False
print(sol.canConstruct("aa", "aab"))     # True
print(sol.canConstruct("abc", "cbaabc")) # True
print(sol.canConstruct("aabbcc", "abc")) # False