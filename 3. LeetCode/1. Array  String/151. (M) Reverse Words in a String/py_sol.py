class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace, automatically removes extra spaces
        words = s.strip().split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join them with a single space
        return " ".join(words)