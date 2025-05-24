#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, A, B):
        # Complete this function
        root = TrieNode()

        # Insert words into the Trie
        for word in B:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        n = len(A)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string can be segmented

        for i in range(n):
            if dp[i]:
                node = root
                for j in range(i, n):
                    ch = A[j]
                    if ch not in node.children:
                        break
                    node = node.children[ch]
                    if node.is_end:
                        dp[j + 1] = True

        return 1 if dp[n] else 0