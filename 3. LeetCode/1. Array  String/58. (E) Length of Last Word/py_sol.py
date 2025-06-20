class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces
        s = s.rstrip()
        
        # Initialize length counter
        length = 0
        
        # Traverse backwards and count the characters of the last word
        for char in reversed(s):
            if char == ' ':
                break
            length += 1
        
        return length