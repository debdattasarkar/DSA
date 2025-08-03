# Word Boggle Solver

## 🧩 Introduction

The **Word Boggle** problem involves searching for valid dictionary words in a grid of characters. Words must be formed using adjacent cells (8 directions allowed), and no cell can be used more than once per word.

This solution uses **Trie** and **DFS** to efficiently find all such words on the board.

---

## 🚀 Problem Statement

Given:

* A dictionary of `N` distinct words.
* A board with `R` rows and `C` columns filled with characters.

Return:

* All possible words from the dictionary that can be formed using adjacent characters on the board.
* Output the result in **lexicographical order**.

---

## 📌 Examples

### Example 1

```
Input:
N = 1
dictionary = {"CAT"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}

Output:
CAT

Explanation:
Words we got is denoted using same color on the board:
C A P
A N D
T I E
```

### Example 2

```
Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3
board = {{G,I,Z},{U,E,K},{Q,S,E}}

Output:
GEEKS QUIZ

Explanation:
G I Z
U E K
Q S E
Words found: GEEKS, QUIZ
```

---

## 📐 Constraints

* 1 ≤ N ≤ 15
* 1 ≤ R, C ≤ 50
* 1 ≤ word length ≤ 60
* Each word consists of uppercase and lowercase letters

---

## 💡 Expected Time and Space Complexity

* **Time Complexity**: O(N × W + R × C²)
* **Auxiliary Space**: O(N × W + R × C)

Where:

* `N` = number of dictionary words
* `W` = average word length
* `R`, `C` = dimensions of the board

---

## 🧠 Techniques Used

* Trie (Prefix Tree)
* Depth-First Search (DFS)
* Backtracking
* Graph traversal

---

## 🏢 Company Tags

* Amazon
* Microsoft
* MakeMyTrip
* Directi
* Google
* Facebook
* Yahoo
* Nvidia

---

## 🧪 Related Interview Experiences

* Directi Interview Experience Set 14 On Campus
* Makemytrip Interview Experience Set 7 On Campus

---

## 📚 Related Articles

* [Boggle Find Possible Words Board Characters](#)
* [Boggle Using Trie](#)

---

Here is a detailed explanation and dry run for the **Word Boggle** problem along with Python, C++, and JavaScript implementations using **Trie and DFS**:

---

## ✅ Problem Summary

Given:

* A dictionary of `N` words.
* A 2D board of characters.

Goal:

* Return all dictionary words that can be constructed from characters of the board using adjacent (8-directional) cells. Each cell can be used only once per word.

---

## 🧠 Step-by-Step Explanation

1. **Insert dictionary words into a Trie** for quick prefix lookup.
2. **Traverse each cell** of the board.
3. From each cell, **perform DFS**:

   * Check if the current character matches a prefix in the Trie.
   * Recurse into neighboring cells.
   * Mark cells as visited during traversal and backtrack appropriately.
4. If a word is formed and found in the Trie as a complete word, add it to the result.
5. **Use a set** to avoid duplicates.

---

## 🔁 Dry Run (Example 2)

### Inputs:

```plaintext
dictionary = {"GEEKS","FOR","QUIZ","GO"}
board = [
  ['G','I','Z'],
  ['U','E','K'],
  ['Q','S','E']
]
```

### Step-by-step:

* Start DFS from every cell.
* From (0,0) = 'G':

  * Check 'G', found in Trie.
  * Explore 'E' -> 'E' -> 'K' -> 'S' forms "GEEKS".
  * Add to result.
* From (0,2) = 'Z':

  * Check 'Z', no path in Trie.
* From (2,0) = 'Q':

  * Check 'Q' -> 'U' -> 'I' -> 'Z' forms "QUIZ".

Result: `["GEEKS", "QUIZ"]`

---

## 🐍 Python Code

```python
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
    def wordBoggle(self, board, dictionary):
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
```

---

## 💻 C++ Code

```cpp
class TrieNode {
public:
    TrieNode* children[26];
    bool isEnd;
    TrieNode() {
        isEnd = false;
        fill(begin(children), end(children), nullptr);
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() { root = new TrieNode(); }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'A';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }
};

class Solution {
    int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, string& path, set<string>& result, vector<vector<bool>>& visited) {
        if (node->isEnd) result.insert(path);

        visited[i][j] = true;
        for (int d = 0; d < 8; ++d) {
            int ni = i + dx[d], nj = j + dy[d];
            if (ni >= 0 && nj >= 0 && ni < board.size() && nj < board[0].size() && !visited[ni][nj]) {
                char ch = board[ni][nj];
                if (node->children[ch - 'A']) {
                    path.push_back(ch);
                    dfs(board, ni, nj, node->children[ch - 'A'], path, result, visited);
                    path.pop_back();
                }
            }
        }
        visited[i][j] = false;
    }

public:
    vector<string> wordBoggle(vector<vector<char>>& board, vector<string>& dictionary) {
        Trie trie;
        for (auto& word : dictionary) trie.insert(word);

        int R = board.size(), C = board[0].size();
        set<string> result;
        vector<vector<bool>> visited(R, vector<bool>(C, false));

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                char ch = board[i][j];
                if (trie.root->children[ch - 'A']) {
                    string path = "";
                    path += ch;
                    dfs(board, i, j, trie.root->children[ch - 'A'], path, result, visited);
                }
            }
        }

        return vector<string>(result.begin(), result.end());
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class TrieNode {
    constructor() {
        this.children = {};
        this.end = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (let ch of word) {
            if (!node.children[ch]) node.children[ch] = new TrieNode();
            node = node.children[ch];
        }
        node.end = true;
    }
}

class Solution {
    wordBoggle(board, dictionary) {
        const trie = new Trie();
        for (let word of dictionary) trie.insert(word);

        const R = board.length, C = board[0].length;
        const found = new Set();
        const directions = [-1, 0, 1];

        function dfs(i, j, node, path) {
            if (node.end) found.add(path);

            const temp = board[i][j];
            board[i][j] = '#';

            for (let dx of directions) {
                for (let dy of directions) {
                    const ni = i + dx, nj = j + dy;
                    if ((dx || dy) && ni >= 0 && nj >= 0 && ni < R && nj < C) {
                        const ch = board[ni][nj];
                        if (ch !== '#' && node.children[ch]) {
                            dfs(ni, nj, node.children[ch], path + ch);
                        }
                    }
                }
            }
            board[i][j] = temp;
        }

        for (let i = 0; i < R; i++) {
            for (let j = 0; j < C; j++) {
                const ch = board[i][j];
                if (trie.root.children[ch]) {
                    dfs(i, j, trie.root.children[ch], ch);
                }
            }
        }

        return Array.from(found).sort();
    }
}
```

---



