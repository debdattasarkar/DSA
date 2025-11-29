class TrieNode:
    def __init__(self):
        # Each node holds outgoing edges for characters
        self.children = {}  # dict: char -> TrieNode

class Solution:
    def countSubs(self, s):
        """
        Optimized O(n^2) solution using a Trie (prefix tree) of all substrings.

        Logic:
        - Insert every suffix s[i:] into a Trie.
        - While inserting from position i, we walk characters s[i], s[i+1], ...
        - Whenever we need to create a NEW child node, that path corresponds
          to a NEW distinct substring. So we increment the count.
        - Existing nodes mean the substring was already seen before starting
          from some earlier position.

        Time complexity:
            - There are O(n^2) characters across all substrings.
            - For each character we perform O(1) dict operations.
            => O(n^2) time.

        Space complexity:
            - Each distinct substring adds exactly one node.
            - Maximum distinct substrings is O(n^2).
            => O(n^2) space.
        """
        root = TrieNode()
        unique_substring_count = 0
        n = len(s)

        # For every starting index of substring
        for start in range(n):
            current_node = root

            # Extend substring one character at a time
            for end in range(start, n):
                current_char = s[end]

                # If this character edge doesn't exist from current node,
                # it means this substring (s[start:end+1]) is seen for the first time.
                if current_char not in current_node.children:
                    current_node.children[current_char] = TrieNode()
                    unique_substring_count += 1  # new distinct substring

                # Move deeper into the trie
                current_node = current_node.children[current_char]

        return unique_substring_count