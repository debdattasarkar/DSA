#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end_of_word = True
        
class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        def dfs(i, j, node, path):
            if node.end_of_word:
                found.add(path)
                # Continue to avoid duplicates, not return

            temp = board[i][j]
            board[i][j] = '#'
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni, nj = i + dx, j + dy
                    if (dx != 0 or dy != 0) and 0 <= ni < rows and 0 <= nj < cols:
                        char = board[ni][nj]
                        if char in node.children:
                            dfs(ni, nj, node.children[char], path + char)
            board[i][j] = temp

        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        found = set()

        for i in range(rows):
            for j in range(cols):
                char = board[i][j]
                if char in trie.root.children:
                    dfs(i, j, trie.root.children[char], char)

        return sorted(list(found))