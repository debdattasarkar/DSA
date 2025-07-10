import time
from collections import defaultdict, deque

# -----------------------------------
# Trie Node definition
# -----------------------------------
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False       # Marks the end of a valid word
        self.word = ""         # Store word at terminal node for easy retrieval

class Solution():
    def longestString(self, words):
        # code here
        """
        Build Trie from given words, then perform BFS from root.
        Only continue BFS if all prefixes of a word are valid (end=True).

        Time Complexity:
            - Trie Construction: O(n * L), n = no. of words, L = max word length
            - BFS Traversal: O(n * 26), bounded by total number of Trie edges

        Space Complexity:
            - Trie Storage: O(n * L)
            - BFS Queue: O(n)
        """

        root = TrieNode()

        # -------------------------------
        # Step 1: Insert all words into the Trie
        # -------------------------------
        for word in words:
            node = root
            for ch in word:
                node = node.children[ch]
            node.end = True
            node.word = word

        # -------------------------------
        # Step 2: BFS to find the longest valid word
        # -------------------------------
        queue = deque([root])
        longest = ""

        while queue:
            node = queue.popleft()

            # Traverse children in reverse lexicographical order
            # So that in case of tie, lexicographically smaller word is picked
            for ch in sorted(node.children.keys(), reverse=True):
                child = node.children[ch]

                if child.end:  # Only valid prefix chains can continue
                    queue.append(child)

                    # Update longest if:
                    # - Current word is longer
                    # - Or equal in length but lex smaller
                    if len(child.word) > len(longest) or (
                        len(child.word) == len(longest) and child.word < longest
                    ):
                        longest = child.word

        return longest
        