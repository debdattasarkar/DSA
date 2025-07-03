from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each letter in magazine
        magazine_count = Counter(magazine)
        
        # Check if each character in ransomNote can be satisfied by magazine
        for char in ransomNote:
            if magazine_count[char] == 0:
                return False  # Not enough of 'char' in magazine
            magazine_count[char] -= 1
        
        return True