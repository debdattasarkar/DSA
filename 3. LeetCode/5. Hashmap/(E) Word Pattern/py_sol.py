class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split string into words
        words = s.split()

        # Pattern and words must be the same length
        if len(pattern) != len(words):
            return False

        # Create bijection maps
        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # If pattern char is already mapped, check consistency
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            # If word is already mapped to another char
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c

        return True