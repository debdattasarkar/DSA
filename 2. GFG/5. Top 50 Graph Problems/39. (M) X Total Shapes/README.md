
---

# 🧩 X Total Shapes

**Difficulty:** Medium
**Accuracy:** 65.94%
**Submissions:** 48K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

Given a grid of size **n × m** consisting of **'O'**s and **'X'**s, the task is to find the number of **'X' total shapes**.

> **Note:**
> An **'X' shape** consists of one or more adjacent 'X's connected either **vertically** or **horizontally** (but not diagonally).

---

## 🧠 Examples

### Example 1:

```
Input:
grid = {{X, O, X},
        {O, X, O},
        {X, X, X}}

Output:
3
```

**Explanation:**
The grid is:

```
X O X
O X O
X X X
```

* The 'X's with the same colour are adjacent either vertically or horizontally (diagonals not included).
* Hence, there are **3 distinct X groups** in the grid.

---

### Example 2:

```
Input:
grid = {{X, X},
        {X, X}}

Output:
1
```

**Explanation:**
The grid is:

```
X X
X X
```

* Here, all 'X's are connected either vertically or horizontally.
* Therefore, there is **only 1 group** of 'X' shapes.

---

## 🧑‍💻 Your Task

You don’t need to read input or print anything.
Your task is to complete the function:

```python
def xShape(self, grid):
    # code here
```

which takes the **grid** as input and returns the **count of total 'X' shapes**.

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n × m)
* **Space Complexity:** O(n × m)

---

## ⚙️ Constraints

```
1 ≤ n, m ≤ 100
```

---

## 🏷️ Company Tags

* Amazon
* Google

---

## 💡 Topic Tags

* DFS
* Graph
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Find The Number Of X Total Shapes](https://www.geeksforgeeks.org/find-the-number-of-x-total-shapes/)

---

---

Here’s everything you need to crush **X Total Shapes** in an interview.

---

## 2) Idea + step-by-step dry run

### Problem in one line

Count how many **4-connected** (up/down/left/right) groups of `'X'` exist in an `n × m` grid of `'X'` and `'O'`. Diagonals do **not** connect.

### Core insight

It’s exactly the number of **connected components** of cells labeled `'X'` when connectivity is 4-directional.
Scan the grid; whenever you see an unvisited `'X'`, that starts a **new shape**. Do a flood-fill (DFS/BFS) to mark the whole component as visited so you don’t count it again.

### Dry run (Example-1)

Grid:

```
X O X
O X O
X X X
```

Index with (r,c) from (0,0).

* Start (0,0) = 'X' & unvisited → shape **#1**.
  Flood-fill reaches only (0,0). (Neighbors: (1,0)='O', (0,1)='O')
* (0,1)='O' → skip.
* (0,2)='X' & unvisited → shape **#2**.
  Flood-fill reaches only (0,2). (Neighbors: (1,2)='O', (0,1)='O')
* Next row:
  (1,0)='O' skip, (1,1)='X' & unvisited → shape **#3**.
  Flood-fill from (1,1) reaches: (1,1) → (2,1) → (2,0) → (2,2).
  (Check their neighbors too, they’re either already visited or 'O'.)
* Remaining cells are visited or 'O'.

Total shapes = **3** ✅

Complexities:

* Time `O(n*m)`: each cell is visited at most once.
* Extra space: `O(n*m)` for `visited` (or `O(1)` if you mutate the grid).

---

## 3) Python solutions (interview-ready)

### A) Standard DFS (recursive) — clean & expected

```python
class Solution:
    
    # Function to find the number of 'X' total shapes.
    # Time:  O(n*m)
    # Space: O(n*m) worst-case due to recursion stack + visited
    def xShape(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        
        # 4-directional moves (no diagonals)
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            # Mark (r,c) as visited and expand to 4-neighbors that are 'X'
            visited[r][c] = True
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == 'X' and not visited[nr][nc]:
                        dfs(nr, nc)
        
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'X' and not visited[r][c]:
                    count += 1        # new component found
                    dfs(r, c)         # flood-fill the entire shape
        return count
```

**Why this is great for interviews:** minimal code, clear logic, matches the standard “count islands” pattern (with 4-dir).

---

### B) BFS (iterative, avoids recursion depth)

```python
from collections import deque

class SolutionBFS:
    # Time:  O(n*m)
    # Space: O(n*m)
    def xShape(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 'X' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
        
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'X' and not visited[r][c]:
                    count += 1
                    bfs(r, c)
        return count
```

**When to use:** If interviewer brings up recursion limits / stack safety, switch to BFS.

---

### C) Union–Find / DSU (alternative) — good for DSU discussions

```python
class SolutionDSU:
    # Time:  O(n*m * α(n*m)) ~ O(n*m)
    # Space: O(n*m)
    def xShape(self, grid):
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        
        # Map (r,c) -> id in [0..n*m-1]
        def idx(r, c): return r*m + c
        
        parent = list(range(n*m))
        rank   = [0]*(n*m)
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        
        # Union adjacent 'X' cells (4-directional)
        for r in range(n):
            for c in range(m):
                if grid[r][c] != 'X': 
                    continue
                id1 = idx(r, c)
                if r+1 < n and grid[r+1][c] == 'X':
                    union(id1, idx(r+1, c))
                if c+1 < m and grid[r][c+1] == 'X':
                    union(id1, idx(r, c+1))
        
        # Count distinct roots among 'X' cells
        roots = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'X':
                    roots.add(find(idx(r, c)))
        return len(roots)
```

**When to use:** If interviewer asks for a DSU approach or when you expect many union/find queries.

---

## 4) Interview Q&A (most asked)

**Q1. Why not count diagonal neighbors?**
The problem explicitly defines shape connectivity as **vertical and horizontal only**. Including diagonals would change the answer.

**Q2. Time and space complexity?**
Both DFS and BFS visit each cell at most once → **Time `O(n*m)`**, **Space `O(n*m)`** (visited + recursion/BFS queue). DSU is effectively `O(n*m)` too.

**Q3. Can we do it in `O(1)` extra space?**
Yes, if mutation is allowed: mark visited `'X'` cells as `'O'` during flood-fill (in-place). That reduces auxiliary space to `O(1)` (barring recursion stack).

**Q4. What if recursion depth is a concern?**
Use the **BFS** version (or iterative DFS with a Python list as a stack).

**Q5. How to generalize to 8-direction connectivity?**
Change the neighbor set to include diagonal deltas:
`[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]`.

**Q6. What edge cases should we test?**

* All `'O'` → result `0`.
* Single `'X'` → result `1`.
* One long snake of `'X'` → result `1`.
* Checkerboard of `'X'`/`'O'` → many single-cell shapes.

**Q7. Why does scanning + flood-fill work?**
Because each unvisited `'X'` cell starts a **new connected component**; the flood-fill marks the entire component visited so we count it exactly once.

---

---

Below is a **complete, runnable program** that solves **X Total Shapes** using an in-place DFS flood-fill (space-efficient) and measures execution time inline. I’ve added **clear, line-by-line complexity comments** and shown sample **inputs & outputs**.

---

## Full program (with timing & inline complexity notes)

```python
from timeit import default_timer as timer
from collections import deque
from typing import List


class Solution:
    """
    Count the number of 4-connected components of 'X' in a grid.

    Overall complexity (this implementation):
      - Time:  O(n*m)  — every cell is visited at most once by flood-fill.
      - Space: O(1) extra (we mutate the grid to mark visited), ignoring recursion stack.
               If recursion depth is a concern, use the BFS variant below (O(n*m) aux in the worst case for the queue).
    """

    # ------- DFS (in-place) -------
    def xShape(self, grid: List[List[str]]) -> int:
        # Guard — O(1)
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])  # O(1)

        # 4-directional neighbors — O(1)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS flood fill — marks visited 'X' cells by flipping to 'O'
        # Each cell is flipped once => total work across all calls is O(n*m)
        def dfs(r: int, c: int) -> None:
            # Boundary + value check — O(1)
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != 'X':
                return
            grid[r][c] = 'O'  # mark visited — O(1)
            # Expand to 4 neighbors — each neighbor checked once overall — amortized O(1) per cell
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)

        count = 0  # O(1)
        # Scan all cells — O(n*m)
        for r in range(n):
            for c in range(m):
                # If an unvisited 'X' is found, that's a new component — O(1)
                if grid[r][c] == 'X':
                    count += 1
                    dfs(r, c)  # Flood-fill its entire component — amortized O(1) per cell over whole grid
        return count

    # ------- Optional: BFS (iterative) variant (stack-safe) -------
    def xShape_bfs(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> None:
            q = deque([(sr, sc)])     # push starting cell — O(1)
            grid[sr][sc] = 'O'        # mark visited — O(1)
            # BFS loop — each cell enqueued/dequeued at most once across grid => O(n*m) total
            while q:
                r, c = q.popleft()    # O(1)
                for dr, dc in DIRS:   # 4 neighbors constant — O(1)
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'X':
                        grid[nr][nc] = 'O'  # mark visited — O(1)
                        q.append((nr, nc))  # O(1)

        count = 0
        # Scan grid — O(n*m)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'X':
                    count += 1
                    bfs(r, c)
        return count


# -------------------------
# Demo + timing
# -------------------------
if __name__ == "__main__":
    # Helper to pretty print a grid
    def show_grid(g):
        return "\n".join(" ".join(row) for row in g)

    # Example 1 (from prompt)
    grid1 = [
        list("XOX"),
        list("OXO"),
        list("XXX"),
    ]
    # Example 2 (from prompt)
    grid2 = [
        list("XX"),
        list("XX"),
    ]
    # More edge tests
    grid3 = [list("OOOO")]                     # 0 shapes
    grid4 = [list("X")]                        # 1 shape
    grid5 = [list("XOXOX"), list("OXOXO")]     # 5 shapes (checker-ish horizontally)

    sol = Solution()

    # Prepare duplicates because our implementation mutates the grid in place.
    tests = [
        ("Example-1", [row[:] for row in grid1], 3),
        ("Example-2", [row[:] for row in grid2], 1),
        ("All-O",     [row[:] for row in grid3], 0),
        ("Single-X",  [row[:] for row in grid4], 1),
        ("ZigZag",    [row[:] for row in grid5], 5),
    ]

    for name, g, expected in tests:
        g_copy_for_print = [row[:] for row in g]
        print(f"\n{name} — Input grid:\n{show_grid(g_copy_for_print)}")
        start = timer()                   # start timing — O(1)
        ans = sol.xShape(g)               # run solution — O(n*m)
        end = timer()                     # end timing — O(1)
        print(f"Output: {ans}   |   Expected: {expected}")
        print(f"Elapsed: {(end - start) * 1e6:.2f} μs")

    # Also demo BFS variant on Example-1
    print("\nBFS Variant Demo on Example-1")
    g_bfs = [row[:] for row in grid1]
    start = timer()
    ans_bfs = sol.xShape_bfs(g_bfs)
    end = timer()
    print(f"Output: {ans_bfs}   |   Expected: 3")
    print(f"Elapsed (BFS): {(end - start) * 1e6:.2f} μs")
```

### Sample Output (illustrative)

```
Example-1 — Input grid:
X O X
O X O
X X X
Output: 3   |   Expected: 3
Elapsed: 180.50 μs

Example-2 — Input grid:
X X
X X
Output: 1   |   Expected: 1
Elapsed: 25.10 μs

All-O — Input grid:
O O O O
Output: 0   |   Expected: 0
Elapsed: 7.30 μs

Single-X — Input grid:
X
Output: 1   |   Expected: 1
Elapsed: 3.90 μs

ZigZag — Input grid:
X O X O X
O X O X O
Output: 5   |   Expected: 5
Elapsed: 20.40 μs

BFS Variant Demo on Example-1
Output: 3   |   Expected: 3
Elapsed (BFS): 210.70 μs
```

> Note: Timings vary by machine and environment; they’re only to give you a sense of the performance.

---

## 6) Real-World Use Cases (why this matters)

1. **Image segmentation (binary masks):**
   Counting connected components of foreground pixels (e.g., lesions, objects) when connectivity is 4-neighborhood.

2. **Map/terrain analysis:**
   Detecting contiguous land patches in a binary water/land raster (diagonals often excluded for conservative adjacency).

3. **Document processing / OCR:**
   Identifying connected blobs of ink (characters or components) in binarized images using 4-connectivity.

4. **Game mechanics on grids:**
   Regions capture, flood-fill tools, and puzzle detection (e.g., “paint bucket” or “island” puzzles).