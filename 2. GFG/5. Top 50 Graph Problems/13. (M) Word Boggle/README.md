# Word Boggle

**Difficulty:** Medium
**Accuracy:** 15.85%
**Submissions:** 89K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a dictionary of distinct **words** and an **M x N board** where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board.

We can move to any of the **8 adjacent characters**.

### Note:

* While forming a word we can move to any of the 8 adjacent cells.
* A cell can be used only once in one word.

---

## Example 1

**Input:**

```
N = 1  
dictionary = {"CAT"}  
R = 3, C = 3  
board = {{C, A, P},  
         {A, N, D},  
         {T, I, E}}
```

**Output:**

```
CAT
```

**Explanation:**

```
C A P
A N D
T I E
```

Words we got is denoted using same color.

---

## Example 2

**Input:**

```
N = 4  
dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}  
R = 3, C = 3  
board = {{G, I, Z},  
         {U, E, K},  
         {Q, S, E}}
```

**Output:**

```
GEEKS QUIZ
```

**Explanation:**

```
G I Z
U E K
Q S E
```

Words we got is denoted using same color.

---

## Your Task

You don’t need to read input or print anything.
Your task is to complete the function **wordBoggle()** which takes the dictionary containing **N space-separated strings** and the **R x C board** as input parameters and returns a list of words that exist on the board in **lexicographical order**.

---

## Expected Time Complexity

* **O(N * W + R * C * A²)**

  * where N = number of words
  * W = average word length
  * A = branching factor (up to 8)

## Expected Auxiliary Space

* **O(N * W + R * C)**

---

## Constraints

* ( 1 \leq N \leq 15 )
* ( 1 \leq R, C \leq 50 )
* ( 1 \leq \text{length of Word} \leq 60 )
* Each word can consist of both lowercase and uppercase letters.

---

## Company Tags

* Amazon
* Microsoft
* MakeMyTrip
* Directi
* Google
* Facebook
* Yahoo
* Nvidia

---

## Topic Tags

* Recursion
* DFS
* Graph
* Backtracking
* Trie
* Data Structures
* Algorithms
* Advanced Data Structure

---

## Related Interview Experiences

* Directi Interview Experience Set 14 On Campus
* Makemytrip Interview Experience Set 7 On Campus

---

## Related Articles

* [Boggle Find Possible Words Board Characters]
* [Boggle Using Trie]

---

---

awesome — let’s make this interview-ready: clear intuition + a concrete dry run, then multiple Python solutions in your requested signature (Trie+DFS and a simpler brute DFS), with interview-style inline comments. I’ll wrap with high-yield Q&A.

---

## 2) Intuition & step-by-step dry run

### Problem recap

* Grid `board` of size `R x C`, each cell is a letter.
* Dictionary is a set/list of distinct words.
* A word exists if you can trace it by moving to **any of the 8 neighbors** (N, NE, E, SE, S, SW, W, NW).
* You **cannot reuse a cell within the same word**.
* Return all dictionary words that exist, **sorted lexicographically**.

### Most expected approach (Trie + DFS)

* Build a **Trie** of all words (optionally with `is_end` flag).
* From each cell, do a DFS that follows only children that match current character.
* Prune early if the path is not a prefix in the Trie — this avoids exploring 8-way branches that can’t form any word.
* Mark cells as visited during the current DFS path to prevent reuse.
* When you reach a node with `is_end=True`, add the accumulated word to the result.

**Why Trie?**
For big boards and many words, prefix-pruning eliminates the vast majority of paths early, giving near optimal performance in practice.

---

### Dry run (Example 2 from prompt)

```
dictionary = {"GEEKS","FOR","QUIZ","GO"}
board =
G I Z
U E K
Q S E
```

1. Build Trie for the 4 words; notable prefixes: G, GE, GEE, GEEK…, GO; Q, QU, QUI, QUIZ; F…
2. Start DFS at `(0,0)='G'`. Matches Trie child ‘G’ → continue with 8 neighbors.
3. From `(0,0)`, one path visits `(1,1)='E'` (prefix “GE”), then `(2,2)='E'` (“GEE”), then `(1,2)='K'` (“GEEK”), then `(0,2)='Z'` (“GEEKZ” – not a word) backtracks, try `(2,1)='S'` → “GEEKS” is an end → **add "GEEKS"**.
4. Start at `(0,2)='Z'`… matches ‘Z’? no; pruned.
5. Start at `(2,0)='Q'` → follow Q→U→I→Z across neighbors (e.g., `(2,0)->(1,1)->(0,2)->(1,2)` etc.) to form **"QUIZ"** → add.
6. Other starts either don’t match prefixes or hit visited-cell constraints.

Result (lexicographic): `["GEEKS","QUIZ"]`.

---

## 3) Python solutions (interview-ready)

### A) Optimized: **Trie + board DFS (8 directions)** — preferred in interviews

```python
# User function Template for python3

class Solution:
    def wordBoggle(self, board, dictionary):
        """
        Build a trie for all dictionary words, then DFS from each cell following
        only valid trie prefixes. Add a word when we hit a trie node with is_end=True.

        Let R,C = board dims, D = number of words, L = avg word length.
        Time  : O(R*C * 8^L_pruned) in practice; upper bound O(R*C*8^L) but
                trie prefix-pruning makes it fast.
                Trie build is O(sum |w|) = O(D*L).
        Space : O(D*L) for trie + O(L) recursion + O(R*C) for visited flags.
        """
        if not board or not board[0] or not dictionary:
            return []

        R, C = len(board), len(board[0])

        # --- Build trie ---
        # Each node: {"children": {ch:node}, "end": False}
        def new_node():
            return {"ch": {}, "end": False}
        root = new_node()

        for w in dictionary:
            node = root
            for ch in w:
                if ch not in node["ch"]:
                    node["ch"][ch] = new_node()
                node = node["ch"][ch]
            node["end"] = True

        res = set()  # set to avoid duplicates if multiple paths form same word
        visited = [[False]*C for _ in range(R)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 neighbors

        def dfs(r, c, node, path):
            ch = board[r][c]
            if ch not in node["ch"]:         # prefix pruning
                return
            nxt = node["ch"][ch]
            path.append(ch)
            visited[r][c] = True
            if nxt["end"]:
                res.add("".join(path))       # whole word found

            # explore neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    # only proceed if neighbor char is a child in trie (fast check)
                    if board[nr][nc] in nxt["ch"]:
                        dfs(nr, nc, nxt, path)

            visited[r][c] = False
            path.pop()

        # Start DFS from each cell if it is a possible prefix
        # micro-optimization: pre-check char existence at root
        root_children = root["ch"]
        for i in range(R):
            for j in range(C):
                if board[i][j] in root_children:
                    dfs(i, j, root, [])

        return sorted(res)  # lexicographical order as required
```

---

### B) Simpler (brute-ish): **Check each word with DFS** (no Trie)

Good to mention in interviews; easy to code but slower on large inputs.

```python
class Solution:
    def wordBoggle(self, board, dictionary):
        """
        For each word, try to find it in the board by DFS from matching starts.
        Time  : O( sum_w R*C * 8^|w| ) worst-case
        Space : O(|w|) recursion + O(R*C) visited
        """
        if not board or not board[0] or not dictionary:
            return []

        R, C = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def exists(word):
            visited = [[False]*C for _ in range(R)]

            def dfs(r, c, k):
                # k is index in word (board[r][c] already matched)
                if k == len(word) - 1:
                    return True
                visited[r][c] = True
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == word[k+1]:
                        if dfs(nr, nc, k+1):
                            visited[r][c] = False
                            return True
                visited[r][c] = False
                return False

            # try all starting positions that match word[0]
            ch0 = word[0]
            for i in range(R):
                for j in range(C):
                    if board[i][j] == ch0 and dfs(i, j, 0):
                        return True
            return False

        found = [w for w in dictionary if exists(w)]
        return sorted(set(found))
```

---

## 4) Interview Q&A (high-yield)

**Q1. Why is a Trie helpful here?**
It enables **prefix pruning**: from a board cell, you only continue along paths that match some dictionary prefix. This collapses the search space dramatically compared to naively exploring all 8-way paths.

**Q2. What’s the time complexity?**

* Building the trie is `O(Σ|w|)`.
* DFS explores each path only as long as it matches a trie prefix. Worst-case bounds are large (`O(R*C*8^L)`), but with pruning it is fast in practice, often near `O(R*C + Σ|w|)` on typical inputs.

**Q3. Why use a `set` for results?**
Different paths may form the **same** word (especially if letters repeat). The spec wants distinct words in lexicographic order.

**Q4. How do you avoid revisiting cells?**
Maintain a `visited` matrix; mark a cell before exploring deeper and unmark on backtrack.

**Q5. Why 8 directions?**
The problem explicitly allows moving to **any adjacent cell**, including diagonals, so we list all 8 deltas.

**Q6. Can we stop early once all words are found?**
If you also track how many words are in the dictionary and how many you’ve found, yes — you can early-exit the outer loops to save time.

**Q7. Memory considerations?**
Trie has at most `Σ|w|` nodes; recursion depth is at most the longest word length (≤ 60), well within limits.

**Q8. What about case-sensitivity?**
The statement says words can be lower or upper case; treat characters as-is (no forced lowercase). Ensure your trie uses the exact characters from `board`/`dictionary`.

---

---

here you go — a **runnable, interview-style full program** for **Word Boggle** with:

* the exact method signature you asked for,
* detailed inline **time/space complexity** notes,
* a small **driver** that prints inputs & outputs,
* and a **timeit** harness to compare **Trie+DFS (optimized)** vs **per-word DFS (baseline)**.

I’ve kept sample inputs identical to the prompt so you can sanity-check quickly.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Word Boggle (8-directional adjacency, no cell reuse per word)

Two implementations:
  A) Trie + DFS (preferred): Build a Trie of dictionary words; DFS from each cell,
     following only trie prefixes (aggressively prunes search).
     Time  : O(sum|w|) to build trie + search that is heavily pruned in practice.
             Worst-case theoretical upper bound is O(R*C*8^L), L=max word length,
             but real runtime is usually near-linear in board size + total dictionary length.
     Space : O(sum|w|) for trie + O(R*C) for visited + O(L) recursion depth.

  B) Per-word DFS (baseline): For each word, try to find it by DFS from every cell.
     Time  : O( sum_w (R*C*8^|w|) ) worst-case, can be slow for large dictionaries.
     Space : O(R*C) visited + O(|w|) recursion.

Driver:
  - Runs two example tests (from the prompt), prints found words (lexicographic).
  - Benchmarks both approaches with timeit on small/medium boards.
"""

from typing import List
import timeit


# ------------------------------ Approach A: Trie + DFS ------------------------------ #
class Solution:
    def wordBoggle(self, board: List[List[str]], dictionary: List[str]) -> List[str]:
        """
        Build a trie from dictionary; DFS from each board cell while matching prefixes.
        Return unique words in lexicographical order.

        Time & Space details inline below.
        """
        if not board or not board[0] or not dictionary:
            return []

        R, C = len(board), len(board[0])

        # ---- Build Trie ----
        # Node: {"ch": {char: child_node}, "end": False}
        # Build cost: O(total_len) where total_len = sum(len(w) for w in dictionary)
        def new_node():
            return {"ch": {}, "end": False}
        root = new_node()
        for w in dictionary:                   # O(total_len)
            node = root
            for ch in w:
                if ch not in node["ch"]:
                    node["ch"][ch] = new_node()
                node = node["ch"][ch]
            node["end"] = True

        res = set()                             # avoid duplicates
        visited = [[False] * C for _ in range(R)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 neighbors

        # ---- DFS with prefix pruning ----
        # Recursion depth <= L (max word length) -> O(L) stack
        def dfs(r: int, c: int, node, path: List[str]):
            ch = board[r][c]
            nxt = node["ch"].get(ch)
            if nxt is None:                     # prefix fail -> prune
                return
            path.append(ch)
            visited[r][c] = True

            if nxt["end"]:
                res.add("".join(path))         # O(L) to build (amortized small)

            # explore neighbors only when their letter is a child in trie
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    if board[nr][nc] in nxt["ch"]:  # constant-time child check
                        dfs(nr, nc, nxt, path)

            visited[r][c] = False
            path.pop()

        # Kick off DFS from cells whose char is a root child
        root_children = root["ch"]
        for i in range(R):                      # O(R*C) starts (light early check)
            for j in range(C):
                if board[i][j] in root_children:
                    dfs(i, j, root, [])

        return sorted(res)                      # O(k log k) for k results


# ------------------------------ Approach B: Per-word DFS ------------------------------ #
class SolutionBrute:
    def wordBoggle(self, board: List[List[str]], dictionary: List[str]) -> List[str]:
        """
        Check each word independently via DFS.
        Simpler code; slower for large inputs.
        """
        if not board or not board[0] or not dictionary:
            return []

        R, C = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def exists(word: str) -> bool:
            visited = [[False] * C for _ in range(R)]

            def dfs(r: int, c: int, k: int) -> bool:
                # Board[r][c] matches word[k] already
                if k == len(word) - 1:
                    return True
                visited[r][c] = True
                nk = k + 1
                need = word[nk]
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == need:
                        if dfs(nr, nc, nk):
                            visited[r][c] = False
                            return True
                visited[r][c] = False
                return False

            ch0 = word[0]
            for i in range(R):
                for j in range(C):
                    if board[i][j] == ch0 and dfs(i, j, 0):
                        return True
            return False

        found = [w for w in dictionary if exists(w)]
        return sorted(set(found))


# ---------------------------------------- timing helper ---------------------------------------- #
def bench(func, *args, number=100):
    """
    Average seconds per run using timeit.
    For tiny inputs, Python overhead dominates; treat as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# --------------------------------------------- Demo --------------------------------------------- #
if __name__ == "__main__":
    print("=== Word Boggle — Trie vs Per-word DFS ===\n")

    # Example 1
    dict1 = ["CAT"]
    board1 = [
        ["C", "A", "P"],
        ["A", "N", "D"],
        ["T", "I", "E"],
    ]

    # Example 2
    dict2 = ["GEEKS", "FOR", "QUIZ", "GO"]
    board2 = [
        ["G", "I", "Z"],
        ["U", "E", "K"],
        ["Q", "S", "E"],
    ]

    A = Solution()
    B = SolutionBrute()

    # Run examples
    print(">>> Example 1")
    outA1 = A.wordBoggle(board1, dict1)
    outB1 = B.wordBoggle(board1, dict1)
    print("Optimized (Trie):", outA1)
    print("Brute (Per-word):", outB1)
    print()

    print(">>> Example 2")
    outA2 = A.wordBoggle(board2, dict2)
    outB2 = B.wordBoggle(board2, dict2)
    print("Optimized (Trie):", outA2)
    print("Brute (Per-word):", outB2)
    print()

    # ----------------------------- Micro-benchmarks ----------------------------- #
    print("=== Timings (average seconds per run) ===")
    # A slightly larger random-ish board with repeated letters to highlight pruning
    board_med = [
        list("GEEKS"),
        list("FORQE"),
        list("QUIZG"),
        list("GEEKS"),
    ]  # 4x5
    dict_med = ["GEEKS", "GEEK", "QUIZ", "GO", "SEEK", "FROG", "SEE", "SO", "ROSE", "GIG"]

    runs = 1000  # adjust as you like
    tA = bench(Solution().wordBoggle, board_med, dict_med, number=runs)
    tB = bench(SolutionBrute().wordBoggle, board_med, dict_med, number=runs)
    print(f"Trie + DFS     runs={runs}: {tA:.8e} s/run")
    print(f"Per-word DFS   runs={runs}: {tB:.8e} s/run")
    print("\nNote: exact numbers vary by machine/Python version.")
```

### What you’ll see

* For Example 1, both methods return `["CAT"]`.
* For Example 2, both methods return `["GEEKS", "QUIZ"]`.
* The timing section typically shows the **Trie+DFS** method is consistently faster (often by a large margin), especially as the dictionary grows.

---

## 6) Real-World Use Cases (the important ones)

1. **Word search engines / puzzle generators**
   Boggle/Scrabble-like games, crossword assistants — quickly enumerate dictionary words that can be formed on a letter grid with adjacency rules.

2. **Pattern pathfinding in grids**
   Detecting specific symbol paths in 2D arrays (e.g., on-chip routing layouts, printed circuit boards, or maze-like blueprints) where *adjacent* relationships matter.

3. **OCR post-processing on grids**
   After recognizing characters on a grid (e.g., scanned puzzle pages), validate & extract valid dictionary words via adjacency — helps **denoise** or **rank** OCR hypotheses.

4. **Bioinformatics (toy analog)**
   Searching paths of symbols (amino acids/nucleotides) on a lattice under adjacency constraints — useful in teaching or preliminary exploration of motif discovery.