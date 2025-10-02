# Replace O's with X's

**Difficulty:** Medium
**Accuracy:** 34.0%
**Submissions:** 124K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a matrix **mat** where every element is either `'O'` or `'X'`. Replace all `'O'` or a group of `'O'` with `'X'` that are surrounded by `'X'`.

A `'O'` (or a set of `'O'`) is considered to be surrounded by `'X'` if there are `'X'` at locations just below, just above, just left and just right of it.

---

## Examples

### Example 1

**Input:**

```
mat =
[['X', 'X', 'X', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'O', 'O', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'X', 'O', 'O']]
```

**Output:**

```
[['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'O', 'O']]
```

**Explanation:**
We only changed those `'O'` that are surrounded by `'X'`.

---

### Example 2

**Input:**

```
mat =
[['X', 'O', 'X', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'O', 'O', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'X', 'O', 'O']]
```

**Output:**

```
[['X', 'O', 'X', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'O', 'O', 'X'],
 ['X', 'O', 'X', 'X'],
 ['X', 'X', 'O', 'O']]
```

**Explanation:**
There's no `'O'` that's surrounded by `'X'`.

---

### Example 3

**Input:**

```
mat =
[['X', 'X', 'X'],
 ['X', 'O', 'X'],
 ['X', 'X', 'X']]
```

**Output:**

```
[['X', 'X', 'X'],
 ['X', 'X', 'X'],
 ['X', 'X', 'X']]
```

**Explanation:**
There's only one `'O'` that's surrounded by `'X'`.

---

## Constraints

* (1 \leq \text{mat.size()} \leq 100)
* (1 \leq \text{mat}[0].\text{size()} \leq 100)

---

## Expected Complexities

* **Time Complexity:** (O(n \times m))
* **Auxiliary Space:** (O(1))

---

## Company Tags

* Google

---

## Topic Tags

* Recursion
* Matrix
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* Given Matrix O X Replace O X Surrounded X

---

---

awesome — let’s make this interview-ready: clean intuition, a quick dry run, and multiple Python solutions in your requested template (with inline comments and complexities), plus the typical Q&A.

---

# 2) Intuition & Approach

You only replace those `'O'` cells that are **fully surrounded** by `'X'` in the four directions (up, down, left, right). Any `'O'` that is on the **border** or **connected to the border** through other `'O'` cells must **not** be flipped.

So the trick is to find **border-connected O-regions** (call them **safe**), mark them, then flip the rest.

### Standard plan (most expected in interviews)

1. For every `'O'` on the **border**, run a flood fill (DFS/BFS) and mark all reachable `'O'` as **safe** (e.g., temporarily mark as `'#'`).
2. After marking, traverse the grid again:

   * any `'O'` you see is **truly surrounded** → flip to `'X'`;
   * any `'#'` you see is **safe** → restore to `'O'`.

**Why it works:** any `'O'` that can reach the border via 4-connected `'O'`s cannot be surrounded on all four sides by `'X'`.

**Complexity:** Each cell is visited at most a constant number of times → **O(n·m)** time. Extra space depends on the flood fill: **O(n·m)** worst-case for BFS queue or DFS recursion stack; the **in-place marker** itself is **O(1)**.

---

## Step-by-step Dry Run (Example 1)

```
mat =
X X X X
X O X X
X O O X
X O X X
X X O O
```

**Border O’s:** positions `(4,2)` and `(4,3)` (0-indexed).
Start flood fill from each border `'O'`:

* From `(4,2)` mark `'#'` (safe). Its 4-neighbors are all `X` or out of bounds.
* From `(4,3)` mark `'#'`. Its neighbors are `O` at `(3,3)`? No (it's `X`). Others are out or `X`. So only the last two stay `'#'`.

Now the grid (with marks):

```
X X X X
X O X X
X O O X
X O X X
X X # #
```

Second pass:

* Any remaining `'O'` **not** marked is surrounded → flip to `'X'`.
* Any `'#'` restore to `'O'`.

Result:

```
X X X X
X X X X
X X X X
X X X X
X X O O
```

Exactly as in the example: only the truly surrounded region in the middle was flipped.

---

# 3) Python solutions (multiple ways, interview-ready)

## A) BFS from borders (primary; iterative, stack-safe)

```python
# User function Template for python3

from collections import deque

class Solution:
    def fill(self, mat):
        """
        Mark border-connected 'O' as safe via multi-source BFS, then flip others.
        
        Let n = rows, m = cols.
        Time:  O(n*m)    # each cell enqueued/visited at most once
        Space: O(n*m)    # worst-case queue; in-place marker uses O(1) extra
        """
        if not mat or not mat[0]:
            return mat
        
        n, m = len(mat), len(mat[0])
        q = deque()
        
        # 1) Push all border 'O' cells into the queue (multi-source BFS).
        # Top & bottom rows
        for c in range(m):
            if mat[0][c] == 'O':
                q.append((0, c))
                mat[0][c] = '#'           # mark safe in-place (O(1) space)
            if mat[n-1][c] == 'O':
                q.append((n-1, c))
                mat[n-1][c] = '#'
        # Left & right columns
        for r in range(n):
            if mat[r][0] == 'O':
                q.append((r, 0))
                mat[r][0] = '#'
            if mat[r][m-1] == 'O':
                q.append((r, m-1))
                mat[r][m-1] = '#'
        
        # 2) BFS: mark every 'O' reachable from border as '#'
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:                            # each cell visited at most once -> total O(n*m)
            r, c = q.popleft()
            for dr, dc in DIRS:             # constant 4 neighbors
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 'O':
                    mat[nr][nc] = '#'
                    q.append((nr, nc))
        
        # 3) Final pass: flip unmarked 'O' to 'X', restore '#' to 'O'
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O':        # not safe -> surrounded -> flip
                    mat[r][c] = 'X'
                elif mat[r][c] == '#':      # safe -> restore
                    mat[r][c] = 'O'
        
        return mat
```

---

## B) DFS from borders (recursive; concise, but watch stack depth)

```python
# User function Template for python3

class Solution:
    def fill(self, mat):
        """
        DFS variant: same logic, marking border-connected 'O' as '#'.
        
        Time:  O(n*m)
        Space: O(n*m) recursion stack worst-case
        """
        if not mat or not mat[0]:
            return mat
        
        n, m = len(mat), len(mat[0])
        
        def dfs(r, c):
            # Guard and do-nothing checks: O(1)
            if r < 0 or r >= n or c < 0 or c >= m or mat[r][c] != 'O':
                return
            mat[r][c] = '#'               # mark safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Call DFS from all border 'O's
        for c in range(m):
            if mat[0][c] == 'O': dfs(0, c)
            if mat[n-1][c] == 'O': dfs(n-1, c)
        for r in range(n):
            if mat[r][0] == 'O': dfs(r, 0)
            if mat[r][m-1] == 'O': dfs(r, m-1)
        
        # Flip / restore pass
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O':
                    mat[r][c] = 'X'
                elif mat[r][c] == '#':
                    mat[r][c] = 'O'
        
        return mat
```

---

## C) DSU / Union–Find with a dummy border node (nice to mention)

```python
# User function Template for python3

class Solution:
    def fill(self, mat):
        """
        Union-Find:
          - Create a dummy node representing "border".
          - Union every border 'O' with dummy.
          - Union 4-connected adjacent 'O'-'O' pairs.
          - Finally, any 'O' not connected to dummy is surrounded -> flip.

        Time:  O(n*m * α(n*m)) ~ O(n*m)   (α is inverse Ackermann, ~constant)
        Space: O(n*m)
        """
        if not mat or not mat[0]:
            return mat
        
        n, m = len(mat), len(mat[0])
        N = n * m
        dummy = N  # border component
        
        parent = list(range(N + 1))
        size = [1] * (N + 1)
        
        def idx(r, c): return r * m + c
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        
        # Union border 'O' to dummy; union adjacent 'O's
        for r in range(n):
            for c in range(m):
                if mat[r][c] != 'O':
                    continue
                idrc = idx(r, c)
                if r in (0, n-1) or c in (0, m-1):
                    union(idrc, dummy)  # border O
                # union with up/left only to avoid duplicates
                if r > 0 and mat[r-1][c] == 'O':
                    union(idrc, idx(r-1, c))
                if c > 0 and mat[r][c-1] == 'O':
                    union(idrc, idx(r, c-1))
        
        # Flip surrounded O's (not connected to dummy)
        root_dummy = find(dummy)
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O' and find(idx(r, c)) != root_dummy:
                    mat[r][c] = 'X'
        return mat
```

---

## D) (Educational) Brute region-by-region check (not recommended)

For each unvisited `'O'`, run a DFS to see if its region touches the border. If it **doesn’t**, flip the whole region. If it **does**, leave it. This re-traverses regions and can degrade to **O((n·m)²)**, so it’s mainly useful as a learning baseline—interviews expect A or B.

---

# 4) Interview Q&A (high-yield)

**Q1. Why start from the border?**
Any `'O'` that is on the border—or connected to the border through other `'O'`s—cannot be fully surrounded on all four sides. Marking these as “safe” and flipping the rest is both correct and efficient.

**Q2. Why does the two-pass mark-and-flip run in O(n·m)?**
Each cell is visited at most a constant number of times: once when marked (if reachable from border), and once during the final sweep.

**Q3. What counts as “surrounded”?**
Only **4-directional** adjacency matters (up/down/left/right). Diagonals do **not** connect regions.

**Q4. Space complexity?**
Using in-place marker `'#'` is **O(1)** **extra storage**, but BFS/DFS may need **O(n·m)** queue/stack in the worst case. Some judges report “Aux space O(1)” when they ignore the recursion/queue since we don’t allocate per-cell arrays.

**Q5. What are the corner cases?**

* All `'O'` → nothing flips if any `'O'` is on border; only the internal moat (if any) flips.
* No `'O'` → unchanged.
* Single row/column → all `'O'` are border-connected; nothing flips.
* Islands entirely inside → flip all of them.

**Q6. Why not check each `'O'`’s 4 neighbors directly?**
Local checks don’t determine global connectivity. An `'O'` might have an `'O'` neighbor that eventually reaches the border; we need connectivity (flood fill / union-find).

**Q7. How to avoid recursion depth issues in Python?**
Prefer **BFS** (queue) or an explicit stack. Recursion may hit the recursion limit on 100×100 worst-case grids.

**Q8. Can we do it without modifying the grid?**
Yes—keep a separate `visited` matrix for safe cells and then flip `O` cells not in `visited`. This uses **O(n·m)** extra memory.

---

---

awesome — here’s a **runnable, interview-style full program** for **Replace O’s with X’s** with:

* your requested class/method signature,
* detailed inline **time/space complexity** notes,
* a small **driver** that prints **inputs & outputs**,
* and **timeit** micro-benchmarks for the full call.

I’ve also included a short list of **real-world use cases** at the end.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Replace O's with X's (a.k.a. Surrounded Regions — 4-directional)

Goal:
  Flip every 'O' that is NOT connected to the border (through other 'O's)
  to 'X'. Leave border-connected 'O' regions unchanged.

Key idea (most expected in interviews):
  1) Multi-source flood fill (BFS) from all border 'O's; mark them as SAFE
     using a temporary marker (e.g., '#').
  2) Final sweep: flip all remaining 'O' -> 'X'; restore '#' -> 'O'.

Global complexities for an n x m matrix:
  Time:  O(n*m)   -- every cell visited a constant number of times
  Space: O(n*m)   -- BFS queue worst case; in-place marking uses O(1) extra
"""

from collections import deque
import timeit
from typing import List


# ------------------------------- User Function ------------------------------- #
class Solution:
    def fill(self, mat: List[List[str]]) -> List[List[str]]:
        """
        Border BFS + mark & flip.

        Steps:
          1) Push every border 'O' into queue and mark as '#' (SAFE).   Time: O(n*m)
          2) BFS: for each popped cell, mark 4-neighbor 'O' as '#'.     Time: O(n*m)
          3) Final sweep:
             - remaining 'O' -> surrounded -> flip to 'X'
             - '#' -> restore to 'O'                                     Time: O(n*m)

        Total:
          Time:  O(n*m)
          Space: O(n*m)  (queue worst case); in-place marker = O(1) extra
        """
        # Guard: empty matrix --------------------------------------------- O(1)
        if not mat or not mat[0]:
            return mat

        n, m = len(mat), len(mat[0])
        q = deque()

        # (1) Collect all border 'O' cells as BFS sources ----------------- O(n + m) ⊆ O(n*m)
        # Top and bottom rows
        for c in range(m):
            if mat[0][c] == 'O':
                mat[0][c] = '#'   # mark SAFE in-place (O(1) space)
                q.append((0, c))
            if mat[n - 1][c] == 'O':
                mat[n - 1][c] = '#'
                q.append((n - 1, c))

        # Left and right columns
        for r in range(n):
            if mat[r][0] == 'O':
                mat[r][0] = '#'
                q.append((r, 0))
            if mat[r][m - 1] == 'O':
                mat[r][m - 1] = '#'
                q.append((r, m - 1))

        # (2) Multi-source BFS to mark all border-connected 'O' as '#' ---- O(n*m)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()  # O(1)
            for dr, dc in DIRS:  # constant 4 neighbors
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 'O':
                    mat[nr][nc] = '#'
                    q.append((nr, nc))

        # (3) Final sweep: flip surrounded 'O', restore SAFE '#' ----------- O(n*m)
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O':     # surrounded region
                    mat[r][c] = 'X'
                elif mat[r][c] == '#':   # SAFE border-connected
                    mat[r][c] = 'O'

        return mat


# ------------------------------- Bench Helper ------------------------------- #
def bench(func, *args, number=10000):
    """
    Measure average seconds per run using timeit.
    Note: Tiny inputs are dominated by Python overhead; treat as relative only.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------- Main / Demo -------------------------------- #
if __name__ == "__main__":
    tests = [
        # (matrix, note/expectation)
        (
            [['X','X','X','X'],
             ['X','O','X','X'],
             ['X','O','O','X'],
             ['X','O','X','X'],
             ['X','X','O','O']],
            "Example 1: inner region flips; border-connected remain"
        ),
        (
            [['X','O','X','X'],
             ['X','O','X','X'],
             ['X','O','O','X'],
             ['X','O','X','X'],
             ['X','X','O','O']],
            "Example 2: no surrounded region; unchanged"
        ),
        (
            [['X','X','X'],
             ['X','O','X'],
             ['X','X','X']],
            "Example 3: single surrounded 'O' flips"
        ),
        (
            [['O','O','O'],
             ['O','O','O'],
             ['O','O','O']],
            "All O's on border → nothing flips"
        ),
    ]

    print("=== Replace O's with X's — Border BFS ===\n")
    solver = Solution()

    # Show inputs & outputs
    for mat, note in tests:
        print(note)
        print("Input:")
        for row in mat: print(row)
        out = solver.fill([row[:] for row in mat])  # work on a copy
        print("Output:")
        for row in out: print(row)
        print()

    # ---------------- Timings ----------------
    print("=== Timings (average seconds per run) ===")
    small = [['X','X','X','X'],
             ['X','O','X','X'],
             ['X','O','O','X'],
             ['X','O','X','X'],
             ['X','X','O','O']]

    # a medium-ish grid with a big interior
    medium = [['X']*30 for _ in range(30)]
    for r in range(1,29):
        for c in range(1,29):
            medium[r][c] = 'O'
    # make a tiny border leak so a large region stays 'O'
    medium[15][0] = 'O'

    runs_small = 20000
    runs_medium = 2000

    t_small = bench(Solution().fill, [row[:] for row in small], number=runs_small)
    t_medium = bench(Solution().fill, [row[:] for row in medium], number=runs_medium)

    print(f"Small (5x4/5x5)  runs={runs_small}: {t_small:.8e} s")
    print(f"Medium (30x30)   runs={runs_medium}: {t_medium:.8e} s")
    print("\nNote: values vary by machine and Python version.")
```

---

## 6) Real-World Use Cases (the important ones)

1. **Image Segmentation / Flood Fill with Holes**
   Identify and fill “holes” fully enclosed by a boundary color while keeping boundary-connected regions intact (e.g., removing interior artifacts).

2. **Map/Regions Processing**
   Mark lakes fully surrounded by land while preserving water connected to the outer ocean (classic “enclosed water” detection).

3. **Game Board Mechanics**
   Go/Baduk or territory-capture games: determine stones/regions fully surrounded by the opponent and flip/capture them.

4. **CAD / Graphics**
   Fill enclosed areas in vector/raster drawings while leaving open (border-connected) shapes unchanged.