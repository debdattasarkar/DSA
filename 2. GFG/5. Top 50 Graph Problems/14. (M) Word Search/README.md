
---

# Word Search

**Difficulty:** Medium
**Accuracy:** 32.69%
**Submissions:** 81K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

You are given a matrix `mat[][]` of size `n*m` containing English alphabets and a string `word`.
Check if the word exists on the `mat[][]` or not.

The word can be constructed by using letters from **adjacent cells**, either horizontally or vertically.
The same cell **cannot** be used more than once.

---

## Examples

### Example 1:

**Input:**

```
mat[][] = [['T', 'E', 'E'], 
           ['S', 'G', 'K'], 
           ['T', 'E', 'L']]
word = "GEEK"
```

**Output:**

```
true
```

**Explanation:**
Word **"GEEK"** can be found in the given grid as follows:

```
T E E
S G K
T E L
```

---

### Example 2:

**Input:**

```
mat[][] = [['T', 'E', 'U'], 
           ['S', 'G', 'K'], 
           ['T', 'E', 'L']]
word = "GEEK"
```

**Output:**

```
false
```

**Explanation:**
Word **"GEEK"** cannot be found in the given grid.

```
T E U
S G K
T E L
```

---

### Example 3:

**Input:**

```
mat[][] = [['A', 'B', 'A'], 
           ['B', 'A', 'B']]
word = "AB"
```

**Output:**

```
true
```

**Explanation:**
There are multiple ways to construct the word **"AB"**.

```
A B A
B A B
```

---

## Constraints:

* `1 ≤ n, m ≤ 6`
* `1 ≤ word.size() ≤ 15`
* `mat` and `word` consist of only **lowercase and uppercase English letters**.

---

## Expected Complexities:

* **Time Complexity:** `O(n * m * 3^k)`

  * where `k` = length of the word
* **Auxiliary Space:** `O(k)`

---

## Company Tags:

* Amazon
* Microsoft
* Intuit
* Apple

---

## Topic Tags:

* Recursion
* DFS
* Graph
* Backtracking
* Data Structures
* Algorithms

---

## Related Articles:

* [Check If A Word Exists In A Grid Or Not](#)

---

---

awesome — here’s an interview-ready pack for **Word Search**: crisp intuition + a concrete dry run, then multiple Python solutions in your requested signature (clean backtracking and a slightly optimized variant), all with inline comments you can say out loud. I’ll end with high-yield interviewer Q&A.

---

## 2) Intuition & step-by-step dry run

### Problem recap

* Grid `mat` of size `n × m` with letters.
* A word exists if we can trace it by moving **up/down/left/right** (no diagonals), using a cell **at most once** in the same path.
* Return `True/False` (or `1/0` depending on judge).

### Core idea (what interviewers expect)

Use **DFS + backtracking**:

* For every cell whose letter matches `word[0]`, start a DFS.
* At each step `(r,c,k)` we need `mat[r][c] == word[k]`.
* Temporarily **mark the cell as visited** (e.g., change it to `'#'`) to avoid reuse, recurse to its 4 neighbors to match `word[k+1]`, then **restore** the letter (backtrack).

**Why complexity is ~ `O(n*m*3^k)`?**
We try each start (`n*m`), and for each subsequent character we branch to at most **3** new neighbors on average (4 minus the one we came from). Worst-case upper bound is `O(n*m*4^k)`, but the standard bound quoted for this problem is `O(n*m*3^k)`.

---

### Dry run (Example 1)

```
mat =
T E E
S G K
T E L
word = "GEEK"
```

1. Scan for starting ‘G’: found at (1,1).
2. DFS((1,1), k=0): matches 'G'. Mark (1,1) visited.
3. Need 'E' at k=1: neighbors of (1,1) are (0,1)=E, (2,1)=E, (1,0)=S, (1,2)=K.

   * Try (0,1)=E → k=2, need 'E' again:
     neighbors of (0,1) with (1,1) blocked are (0,0)=T, (0,2)=E, (1,1)=#, (-1,1)=out.
     pick (0,2)=E → k=3, need 'K':
     neighbors of (0,2): (1,2)=K → success for full word.
     So the function returns **True**.

---

## 3) Python solutions (interview-ready)

Both solutions obey your signature `isWordExist(self, mat, word)` and return `True/False`.

### A) Clean backtracking (most expected)

```python
class Solution:
    def isWordExist(self, mat, word):
        """
        Backtracking DFS: try to match the word starting at every cell.
        When visiting a cell, mark it (e.g., '#') to avoid reuse, then restore.

        Let n,m be grid dims, k=len(word).
        Time  : O(n*m*3^k) average; worst-case O(n*m*4^k)
        Space : O(k) recursion (no extra visited matrix if we mark in-place)
        """
        if not mat or not mat[0] or not word:
            return False

        n, m = len(mat), len(mat[0])
        W = len(word)

        # Small pre-pruning: if grid doesn't even contain enough occurrences
        # of any char in 'word', it's impossible.
        from collections import Counter
        need = Counter(word)
        have = Counter(ch for row in mat for ch in row)
        for ch, cnt in need.items():
            if have[ch] < cnt:
                return False

        # Directions: 4-adjacent
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, k):
            """Return True if we can match word[k:] starting from mat[r][c]."""
            if mat[r][c] != word[k]:
                return False
            if k == W - 1:           # matched the last char
                return True

            # mark visited
            tmp = mat[r][c]
            mat[r][c] = '#'          # any sentinel not in 'A'..'Z'/'a'..'z'

            # try neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] != '#':
                    if mat[nr][nc] == word[k + 1] and dfs(nr, nc, k + 1):
                        mat[r][c] = tmp
                        return True

            # backtrack
            mat[r][c] = tmp
            return False

        # Try only cells matching first letter for fewer starts
        first = word[0]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == first and dfs(i, j, 0):
                    return True
        return False
```

### B) Slightly optimized backtracking (ordering + two-way scan)

Two practical tweaks:

1. **Heuristic ordering:** If possible, search the word **forwards or backwards** based on the rarer end letter (searching for the rarer char first cuts starts).
2. **In-place marking** (already used), with an early **neighbor pre-check** to skip useless recursive calls.

```python
class Solution:
    def isWordExist(self, mat, word):
        """
        Optimized backtracking:
          - Choose to search 'word' or 'word[::-1]' so that we start on the rarer boundary char.
          - Pre-check neighbor match before recursing.
        Same asymptotics, but faster in practice.
        """
        if not mat or not mat[0] or not word:
            return False

        n, m = len(mat), len(mat[0])
        from collections import Counter
        grid_cnt = Counter(ch for row in mat for ch in row)

        # Pick direction that starts with the rarer end char
        w = word
        if grid_cnt[word[0]] > grid_cnt[word[-1]]:
            w = word[::-1]

        # Char availability prune
        need = Counter(w)
        for ch, cnt in need.items():
            if grid_cnt[ch] < cnt:
                return False

        W = len(w)
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, k):
            if mat[r][c] != w[k]:
                return False
            if k == W - 1:
                return True

            tmp = mat[r][c]
            mat[r][c] = '#'

            next_ch = w[k + 1]
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # quick neighbor check to reduce function calls
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == next_ch:
                    if dfs(nr, nc, k + 1):
                        mat[r][c] = tmp
                        return True

            mat[r][c] = tmp
            return False

        start_char = w[0]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == start_char and dfs(i, j, 0):
                    return True
        return False
```

> In practice, variant **B** noticeably reduces starts and calls when one boundary letter is rare.

---

## 4) Interview Q&A (high-yield)

**Q1. Why DFS/backtracking? Why not BFS?**
We’re matching a **specific order of characters** along a path with **no revisits**. DFS naturally explores sequences and lets us **backtrack** (unmark) as we unwind. BFS could work but adds overhead and isn’t as clean for string matching.

**Q2. Where does the `O(n*m*3^k)` come from?**
We try each start cell (`n*m`). At each next character, we branch to at most ~3 new neighbors on average (4 minus where we came from). Worst-case is `O(n*m*4^k)`, but the quoted bound is `O(n*m*3^k)`.

**Q3. How do you avoid revisiting a cell on the same path?**
Temporarily **mark** the cell (e.g., swap with `'#'`) before recursing, then **restore** it after (backtrack). This avoids a separate `visited` matrix and keeps space `O(k)`.

**Q4. Any quick prunings?**

* **Letter frequency check**: if the grid has fewer of some required char than the word needs, return `False` immediately.
* **Start filtering**: only start DFS at cells with the first (or chosen) letter.
* **Neighbor pre-check**: compare `next_ch` before recursing to cut calls.

**Q5. Are diagonals allowed?**
Not in this problem statement: only **horizontal/vertical** moves.

**Q6. Case sensitivity?**
Yes. The grid and word can be uppercase or lowercase. Compare characters **as given** (don’t lowercase unless the judge says so).

**Q7. Could we memoize `(r,c,k)`?**
Not safely with revisits across different path histories, because feasibility depends on which cells are currently visited. A full mask memo is exponential; in practice, **pruning + in-place marking** is the accepted solution.

**Q8. Edge cases?**

* `len(word)==1`: just check if that letter exists in the grid.
* Very repetitive grids (e.g., all ‘A’s): worst-case branching; prunings help.
* Single row/column grids: still works since moves are orthogonal.

---

---

you got it — here’s a **runnable, interview-style full program** for **Word Search** with:

* your requested signature `class Solution.isWordExist(self, mat, word)`,
* rich **inline time/space complexity** notes,
* a tiny **driver** that prints **inputs & outputs**,
* and **timeit** micro-benchmarks comparing two variants:

  * **Clean Backtracking** (canonical)
  * **Optimized Backtracking** (rarer-end heuristic + neighbor pre-check)

I finish with a few **high-value real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Word Search (Leet/GFG style)
----------------------------
Given grid mat[n][m] of letters and a word, return True if the word can be traced
by moving 4-directionally (up/down/left/right) without reusing a cell.

Two approaches:
 A) Solution: Clean backtracking (canonical).
 B) SolutionOpt: Practical optimizations (rarer-end heuristic, neighbor pre-check).

Complexities (n x m grid, word length k):
 - Time  : ~ O(n*m*3^k) average (worst O(n*m*4^k))
 - Space : O(k) recursion depth, constant extra if using in-place marking.

The driver prints example inputs & outputs and benchmarks both approaches using timeit.
"""

from typing import List
import timeit
from collections import Counter


# ----------------------------- Approach A: Clean Backtracking ----------------------------- #
class Solution:
    def isWordExist(self, mat: List[List[str]], word: str) -> bool:
        """
        DFS + backtracking with in-place visited marking.

        Steps per call:
          1) If current cell char != word[k] -> fail.                      O(1)
          2) If k == len(word)-1 -> success.                               O(1)
          3) Mark current cell as visited (e.g., '#'), explore 4 neighbors O(1) + 4 * T(k+1)
             whose letter matches next char, then restore (backtrack).
        Global:
          - Try every grid cell that matches word[0] as a start: O(n*m)
          - Branching factor ~3 (we don't go back to where we came from on average).
        Time  : O(n*m*3^k) typical; worst O(n*m*4^k)
        Space : O(k) recursion; no extra visited matrix needed.
        """
        if not mat or not mat[0] or not word:
            return False

        n, m = len(mat), len(mat[0])
        k = len(word)

        # Quick frequency pruning: if grid lacks enough of any needed char -> impossible.
        need = Counter(word)                                 # O(k)
        have = Counter(ch for row in mat for ch in row)      # O(n*m)
        for ch, cnt in need.items():                         # O(k)
            if have[ch] < cnt:
                return False

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int, idx: int) -> bool:
            # base checks
            if mat[r][c] != word[idx]:                       # O(1)
                return False
            if idx == k - 1:                                 # matched entire word
                return True

            # mark visited in-place (constant space)
            tmp = mat[r][c]
            mat[r][c] = '#'

            nxt = word[idx + 1]                              # next char to match
            # 4-way explore
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # bounds + not visited + next char pre-check to prune calls
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == nxt:
                    if dfs(nr, nc, idx + 1):
                        mat[r][c] = tmp                      # restore before returning
                        return True

            mat[r][c] = tmp                                  # restore on backtrack
            return False

        # Only start from cells that match the first letter
        first = word[0]
        for i in range(n):                                   # O(n*m) starts (filtered)
            for j in range(m):
                if mat[i][j] == first and dfs(i, j, 0):
                    return True
        return False


# ----------------------------- Approach B: Optimized Backtracking ----------------------------- #
class SolutionOpt:
    def isWordExist(self, mat: List[List[str]], word: str) -> bool:
        """
        Same DFS, two practical optimizations:
          - Choose to search 'word' or 'word[::-1]' based on which end char is rarer
            in the grid -> fewer starting points on average.
          - Neighbor pre-check (already done) to reduce recursion calls.
        Time  : same asymptotics; faster constant factors in practice.
        Space : O(k)
        """
        if not mat or not mat[0] or not word:
            return False

        n, m = len(mat), len(mat[0])
        grid_cnt = Counter(ch for row in mat for ch in row)  # O(n*m)

        # If end char is rarer than start char, search reversed word to reduce starts.
        w = word if grid_cnt[word[0]] <= grid_cnt[word[-1]] else word[::-1]

        # Frequency pruning
        need = Counter(w)
        for ch, cnt in need.items():
            if grid_cnt[ch] < cnt:
                return False

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        L = len(w)

        def dfs(r: int, c: int, idx: int) -> bool:
            if mat[r][c] != w[idx]:
                return False
            if idx == L - 1:
                return True

            tmp = mat[r][c]
            mat[r][c] = '#'

            nxt = w[idx + 1]
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == nxt:
                    if dfs(nr, nc, idx + 1):
                        mat[r][c] = tmp
                        return True

            mat[r][c] = tmp
            return False

        start_char = w[0]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == start_char and dfs(i, j, 0):
                    return True
        return False


# ------------------------------------ timing helper ------------------------------------ #
def bench(func, *args, number=5000):
    """
    Return average seconds/run using timeit.
    Use as a *relative* metric (Python function-call overhead dominates tiny cases).
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------------ demo ------------------------------------------ #
if __name__ == "__main__":
    print("=== Word Search — Backtracking variants ===\n")

    # Example 1 (from prompt)
    mat1 = [['T', 'E', 'E'],
            ['S', 'G', 'K'],
            ['T', 'E', 'L']]
    word1 = "GEEK"

    # Example 2 (no match)
    mat2 = [['T', 'E', 'U'],
            ['S', 'G', 'K'],
            ['T', 'E', 'L']]
    word2 = "GEEK"

    # Example 3 (multiple ways)
    mat3 = [['A', 'B', 'A'],
            ['B', 'A', 'B']]
    word3 = "AB"

    A = Solution()
    B = SolutionOpt()

    # Run examples (note: each call mutates its grid in-place for visited marking,
    # so pass a deep copy if you reuse the same grid multiple times)
    import copy
    print(">>> Example 1")
    print("Grid:", mat1, "Word:", word1)
    outA1 = A.isWordExist(copy.deepcopy(mat1), word1)
    outB1 = B.isWordExist(copy.deepcopy(mat1), word1)
    print("Clean Backtracking  :", outA1)
    print("Optimized Backtrack :", outB1, "\n")

    print(">>> Example 2")
    print("Grid:", mat2, "Word:", word2)
    outA2 = A.isWordExist(copy.deepcopy(mat2), word2)
    outB2 = B.isWordExist(copy.deepcopy(mat2), word2)
    print("Clean Backtracking  :", outA2)
    print("Optimized Backtrack :", outB2, "\n")

    print(">>> Example 3")
    print("Grid:", mat3, "Word:", word3)
    outA3 = A.isWordExist(copy.deepcopy(mat3), word3)
    outB3 = B.isWordExist(copy.deepcopy(mat3), word3)
    print("Clean Backtracking  :", outA3)
    print("Optimized Backtrack :", outB3, "\n")

    # ------------------------------- Micro-benchmarks ------------------------------- #
    print("=== Timings (average seconds per run) ===")
    board_small = [['A', 'B', 'C', 'E'],
                   ['S', 'F', 'C', 'S'],
                   ['A', 'D', 'E', 'E']]
    word_small_hit = "ABCCED"     # typical Leet example -> True
    word_small_miss = "ABCB"      # -> False

    runs = 10000
    t1 = bench(Solution().isWordExist, copy.deepcopy(board_small), word_small_hit, number=runs)
    t2 = bench(SolutionOpt().isWordExist, copy.deepcopy(board_small), word_small_hit, number=runs)
    print(f"Hit  ({word_small_hit})  runs={runs}:  Clean {t1:.8e}s  |  Opt {t2:.8e}s")

    t1m = bench(Solution().isWordExist, copy.deepcopy(board_small), word_small_miss, number=runs)
    t2m = bench(SolutionOpt().isWordExist, copy.deepcopy(board_small), word_small_miss, number=runs)
    print(f"Miss ({word_small_miss}) runs={runs}:  Clean {t1m:.8e}s |  Opt {t2m:.8e}s")

    print("\nNote: timings vary by machine & Python version. Both are O(n*m*3^k) in theory.")
```

**What the program prints**

* For the three examples, you’ll see `True/False` for both variants (they should agree).
* Then a small **timeit** section showing average seconds/run for a hit and a miss on a small board.

---

## 6) Real-World Use Cases (the important ones)

1. **Crossword / Word-puzzle solvers**
   Validate whether a given word can be formed in a puzzle grid with movement rules and no-reuse constraints.

2. **Pathfinding with labels**
   Planning problems where you must traverse cells in a **specific label order** without revisiting (e.g., workflow stations, UI tours, or training simulators).

3. **OCR Post-processing on Grids**
   After optical character recognition on a scanned puzzle (Boggle, word-search sheets), verify candidate words by **adjacent-path validation** to reject spurious text.

4. **Security Keypads / Gesture Unlock**
   Validate if a gesture (sequence) can be traced on a keypad/grid under adjacency and non-reuse constraints.
