
---

# 🧮 Distance of Nearest Cell Having 1

**Difficulty:** Medium
**Accuracy:** 47.7%
**Submissions:** 114K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

Given a binary matrix `grid[][]`, where each cell contains either `0` or `1`, find the distance of the nearest `1` for every cell in the grid.

The distance between two cells `(i1, j1)` and `(i2, j2)` is calculated as:
[
|i1 - i2| + |j1 - j2|
]

You need to return a matrix of the same size, where each cell `(i, j)` contains the **minimum distance** from `grid[i][j]` to the nearest cell having value `1`.

> **Note:** It is guaranteed that there is at least one cell with value `1` in the grid.

---

## 🧩 Examples

### Example 1

**Input:**

```
grid[][] = [
  [0, 1, 1, 0],
  [1, 1, 0, 0],
  [0, 0, 1, 1]
]
```

**Output:**

```
[
  [1, 0, 0, 1],
  [0, 0, 1, 1],
  [1, 1, 0, 0]
]
```

**Explanation:**
The grid is -

|       | 0 | 1 | 2 | 3 |
| ----- | - | - | - | - |
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 0 | 0 |
| **2** | 0 | 0 | 1 | 1 |

`0`s at `(0,0)`, `(0,3)`, `(1,2)`, `(1,3)`, `(2,0)` and `(2,1)` are at a distance of 1 from `1`s at `(0,1)`, `(0,2)`, `(0,2)`, `(2,3)`, `(2,3)`, `(1,0)`, and `(1,1)` respectively.

Output matrix:

|       | 0 | 1 | 2 | 3 |
| ----- | - | - | - | - |
| **0** | 1 | 0 | 0 | 1 |
| **1** | 0 | 0 | 1 | 1 |
| **2** | 1 | 1 | 0 | 0 |

---

### Example 2

**Input:**

```
grid[][] = [
  [1, 0, 1],
  [1, 1, 0],
  [1, 0, 0]
]
```

**Output:**

```
[
  [0, 1, 0],
  [0, 0, 1],
  [0, 1, 2]
]
```

**Explanation:**
The grid is -

|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 1 | 0 | 1 |
| **1** | 1 | 1 | 0 |
| **2** | 1 | 0 | 0 |

`0`s at `(0,1)`, `(1,2)`, `(2,1)`, and `(2,2)` are at a distance of `1`, `1`, `1`, and `2` from `1`s at `(0,0)`, `(0,2)`, `(2,0)`, and `(1,1)` respectively.

Output matrix:

|       | 0 | 1 | 2 |
| ----- | - | - | - |
| **0** | 0 | 1 | 0 |
| **1** | 0 | 0 | 1 |
| **2** | 0 | 1 | 2 |

---

## ⚙️ Constraints

```
1 ≤ grid.size() ≤ 200
1 ≤ grid[0].size() ≤ 200
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## 🏷️ Company Tags

`Bloomberg`, `Amazon`, `Microsoft`, `Accenture`, `Google`, `Flipkart`, `Uber`

---

## 🧠 Topic Tags

* Matrix
* Graph
* BFS
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Distance Nearest Cell 1 Binary Matrix](https://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/)

---

---

Awesome—this is a classic “nearest 1 in a binary matrix” problem. I’ll give you:

1. a crisp explanation + step-by-step dry run,
2. interview-ready Python solutions in your requested class/signature (Brute → Optimal BFS → DP 2-pass),
3. quick memory aids and common interviewer Q&A.

---

# 2) Text explanation + dry run

## What we want

For every cell `(r, c)`, fill the answer with the **Manhattan distance** to the **nearest cell that contains 1** (distance = `|r-r1| + |c-c1|`). There is at least one `1` somewhere.

## Key idea (optimal)

Treat all cells that already have `1` as **sources** with distance `0`.
Then perform a **multi-source BFS** outward (4 directions). The first time we reach a cell, that’s its **minimum** distance (BFS explores in rings of increasing distance).

Why BFS? Because all edges have equal cost (1 step up/down/left/right), so the shortest distance is found as soon as a node is dequeued for the first time.

### Dry run (tiny)

```
grid =
1 0 0
0 0 1
0 0 0
```

* Init queue with all 1s: positions `(0,0)` and `(1,2)` with distance 0.
* dist matrix starts as:

```
0  INF  INF
INF INF  0
INF INF INF
```

BFS rings:

* Pop (0,0), push its neighbors with dist=1: (1,0), (0,1)
* Pop (1,2), push its neighbors with dist=1: (0,2), (1,1), (2,2)

Now dist:

```
0  1  1
1  1  0
INF INF 1
```

Next ring (distance 2):

* Visit (2,0) from (1,0); (2,1) from (2,2) or (1,1); (1,2) is already 0, etc.

Final dist:

```
0 1 1
1 1 0
2 2 1
```

Every cell holds the minimum #steps to the nearest 1.

---

# 3) Python solutions (brute → optimal)

All solutions follow your requested format:

```python
class Solution:
    def nearest(self, grid):
        # code here
```

### A) Brute force (simple but slow) — O((n*m) * (n*m))

For each cell, scan all cells with value 1 and keep the minimum Manhattan distance. Easy to explain, too slow for large matrices.

```python
class Solution:
    def nearest(self, grid):
        """
        Brute-force:
          For each cell, compute min |r-r1|+|c-c1| over all 1-cells.
        Time  : O((n*m)*(n*m))  -> too slow for n,m up to 200 but illustrative
        Space : O(1) besides the output
        """
        n, m = len(grid), len(grid[0])
        ones = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]

        ans = [[0]*m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans[r][c] = 0
                else:
                    best = float('inf')
                    for (i, j) in ones:                      # check every 1
                        d = abs(r - i) + abs(c - j)
                        if d < best:
                            best = d
                    ans[r][c] = best
        return ans
```

---

### B) Optimal (multi-source BFS) — **O(n*m)** time, **O(n*m)** space

This is the most expected interview solution.

```python
from collections import deque

class Solution:
    def nearest(self, grid):
        """
        Multi-source BFS from all ones.
        Steps:
          1) Enqueue every cell with value 1 with distance 0.
          2) BFS to fill neighbors' distance if not set yet.
        Time  : O(n*m)  -- each cell enters queue at most once
        Space : O(n*m)  -- for dist/queue
        """
        n, m = len(grid), len(grid[0])

        # Initialize distances with +inf; set 0 where grid==1 and enqueue those cells
        dist = [[float('inf')] * m for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))   # multi-source seed

        # 4-connected directions
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        # Standard BFS
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # in-bounds and can we relax to a shorter distance?
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist
```

---

### C) DP 2-pass (also O(n*m), elegant alternative)

We can compute distances via two dynamic programming sweeps using the fact that Manhattan distance with 4-neighbors can be built from neighbors:

* First pass: top-left → bottom-right (use top and left)
* Second pass: bottom-right → top-left (use bottom and right)
* Cells with `1` start at distance `0`. Others start at `INF`.

```python
class Solution:
    def nearest(self, grid):
        """
        DP two-pass (no explicit queue).
        Pass1: top-left to bottom-right  -> uses up and left neighbors
        Pass2: bottom-right to top-left  -> uses down and right neighbors
        Time  : O(n*m)
        Space : O(n*m) for the dist matrix
        """
        n, m = len(grid), len(grid[0])
        INF = 10**9

        dist = [[0 if grid[r][c] == 1 else INF for c in range(m)] for r in range(n)]

        # Pass 1: TL -> BR
        for r in range(n):
            for c in range(m):
                if dist[r][c] == 0:        # already a 1
                    continue
                if r > 0:
                    dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                if c > 0:
                    dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)

        # Pass 2: BR -> TL
        for r in reversed(range(n)):
            for c in reversed(range(m)):
                if r + 1 < n:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c + 1 < m:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)

        return dist
```

**Which one to present?**

* If the interviewer says “graph/BFS,” show **BFS**.
* If they say “no queue / DP approach?” show the **2-pass DP**.
  Both are O(n·m); BFS is usually the primary expectation.

---

# 4) Interview quick-recall + Q&A

## 10-second mnemonic

> **“Seed all 1s → BFS in waves → first visit = shortest distance.”**

Or even shorter: **“All-ones as sources; wave-BFS.”**

## Likely Q&A

**Q1. Why multi-source BFS?**
Because all moves have equal cost (1). BFS explores cells in increasing distance; the first time we pop a cell is the shortest path length from *any* source. Seeding all `1`s at distance 0 gives the nearest 1 to each cell.

**Q2. Complexity?**
Each cell is enqueued/dequeued at most once; each edge (up to 4 per cell) is checked a constant number of times → **O(n·m)** time, **O(n·m)** space.

**Q3. Can you do it without a queue?**
Yes, the **2-pass DP** uses the recurrence from neighbors and also runs in **O(n·m)**.

**Q4. What if diagonals were allowed?**
Then the distance metric changes. With 8-neighbors and unit weights, BFS still works; for true Chebyshev distance you’d adapt transitions accordingly.

**Q5. Any pitfalls?**

* Forgetting to initialize all `1`s with distance 0 (multi-source).
* Re-visiting cells and accidentally overwriting shorter distances if you don’t check `>` before relaxing.
* Using DFS (doesn’t guarantee shortest in unweighted grids).

**Q6. How do you prove minimality?**
BFS processes by **layers** (`0, 1, 2, ...`). If a cell were assigned a distance larger than its true minimum, there would be a BFS layer containing it earlier—contradiction.

**Q7. Which version uses less auxiliary memory?**
Both keep an `n×m` matrix. BFS additionally holds a queue (≤ n·m), but the asymptotic space is still **O(n·m)**.

---

---

Here you go—short, interview-ready extras plus a complete runnable script.

---

## 5) Real-World Use Cases (easy to relate)

* **Routing to nearest facility:** In a city grid, each `1` is a hospital/charging station; every block wants the walking distance to the nearest one.
* **Image processing (binary masks):** Distance‐to‐foreground map—pixels (`0`) store distance to the nearest feature pixel (`1`) for effects like dilation/edge emphasis.
* **Network placement / Wi-Fi planning:** Floors as grids; compute how far any spot is from the nearest access point to check coverage holes.
* **Fire/contagion simulation (time to reach):** With synchronous spread per step, the “time” each cell gets affected equals BFS distance from initially affected cells.

These map perfectly to the **multi-source BFS** logic.

---

## 6) Full Program (with inline complexity notes + timings)

```python
#!/usr/bin/env python3
"""
Distance of Nearest Cell Having 1
---------------------------------
Implementations:
  - Brute force        : O((n*m)^2) time, O(1) extra
  - Multi-source BFS   : O(n*m)     time, O(n*m) extra
  - DP Two-Pass        : O(n*m)     time, O(n*m) extra

The 'Solution' class uses the *BFS* version (most expected in interviews).
We also provide SolutionBrute and SolutionDP for comparison and validation.

This script:
  * Runs sample inputs
  * Prints outputs
  * Times each method using perf_counter and timeit
"""

from collections import deque
from time import perf_counter
import timeit
from typing import List


# -------------------------- Brute Force --------------------------
class SolutionBrute:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        """
        For each cell, scan all 1-cells and keep the minimal Manhattan distance.
        Time  : O((n*m) * (n*m))  -- worst-case quadratic in number of cells
        Space : O(1) extra besides the output matrix
        """
        n, m = len(grid), len(grid[0])
        ones = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]

        ans = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans[r][c] = 0
                else:
                    best = float('inf')
                    # O(#ones) check for this single cell
                    for (i, j) in ones:
                        d = abs(r - i) + abs(c - j)
                        if d < best:
                            best = d
                    ans[r][c] = best
        return ans


# -------------------------- Multi-Source BFS (Optimal) --------------------------
class Solution:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Multi-source BFS from all ones.
        Rationale: All edges have unit cost; BFS layers expand in increasing distance.
        Steps:
          1) Enqueue every '1' cell with distance 0.          -> O(n*m)
          2) Pop & relax 4-neighbors if we find a shorter dist -> Each cell enters queue at most once
        Time  : O(n*m)
        Space : O(n*m) for dist + queue
        """
        n, m = len(grid), len(grid[0])

        # Initialize distances: 0 for ones, +inf for zeros  -> O(n*m)
        dist = [[float('inf')] * m for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))  # seed all sources at once

        # 4-connected moves
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # BFS  -> Total pushes/pops <= n*m
        while q:
            r, c = q.popleft()
            base = dist[r][c]
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] > base + 1:
                    dist[nr][nc] = base + 1
                    q.append((nr, nc))

        return dist


# -------------------------- DP Two-Pass (Alternative Optimal) --------------------------
class SolutionDP:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        """
        DP via two directional sweeps.
        Pass 1 (TL->BR): use top/left neighbors
        Pass 2 (BR->TL): use bottom/right neighbors
        Time  : O(n*m)
        Space : O(n*m)
        """
        n, m = len(grid), len(grid[0])
        INF = 10**9

        # O(n*m) init
        dist = [[0 if grid[r][c] == 1 else INF for c in range(m)] for r in range(n)]

        # Pass 1: top-left -> bottom-right
        for r in range(n):
            for c in range(m):
                if dist[r][c] == 0:
                    continue
                if r > 0:
                    # look up
                    cand = dist[r - 1][c] + 1
                    if cand < dist[r][c]:
                        dist[r][c] = cand
                if c > 0:
                    # look left
                    cand = dist[r][c - 1] + 1
                    if cand < dist[r][c]:
                        dist[r][c] = cand

        # Pass 2: bottom-right -> top-left
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if r + 1 < n:
                    cand = dist[r + 1][c] + 1
                    if cand < dist[r][c]:
                        dist[r][c] = cand
                if c + 1 < m:
                    cand = dist[r][c + 1] + 1
                    if cand < dist[r][c]:
                        dist[r][c] = cand

        return dist


# -------------------------- Utility printing --------------------------
def print_matrix(mat: List[List[int]]):
    for row in mat:
        print(" ".join(map(str, row)))


# -------------------------- Demo & Timing --------------------------
def main():
    print("=== Distance of Nearest Cell Having 1 ===\n")

    # Sample inputs from the prompt and a custom case
    grids = [
        (
            [[0, 1, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 1, 1]],
            "Example 1"
        ),
        (
            [[1, 0, 1],
             [1, 1, 0],
             [1, 0, 0]],
            "Example 2"
        ),
        (
            [[1, 0, 0],
             [0, 0, 1],
             [0, 0, 0]],
            "Custom"
        ),
    ]

    sol_bfs = Solution()
    sol_dp = SolutionDP()
    sol_brute = SolutionBrute()

    for grid, name in grids:
        print(f"-- {name} --")
        print("Input:")
        print_matrix(grid)

        # ---------- Single-run timings using perf_counter ----------
        t0 = perf_counter()
        out_bfs = sol_bfs.nearest([row[:] for row in grid])   # copy for fairness
        t1 = perf_counter()

        t2 = perf_counter()
        out_dp = sol_dp.nearest([row[:] for row in grid])
        t3 = perf_counter()

        # Brute only for small grids (safe here)
        t4 = perf_counter()
        out_brute = sol_brute.nearest([row[:] for row in grid])
        t5 = perf_counter()

        print("\nOutput (BFS):")
        print_matrix(out_bfs)
        print("Output (DP two-pass):")
        print_matrix(out_dp)
        print("Output (Brute):")
        print_matrix(out_brute)

        # Check correctness equality
        ok = (out_bfs == out_dp == out_brute)
        print("\nEqual across methods? ->", ok)

        print(f"\nTiming (single run):")
        print(f"  BFS       : {(t1 - t0)*1e6:9.2f} µs")
        print(f"  DP two-pass: {(t3 - t2)*1e6:9.2f} µs")
        print(f"  Brute     : {(t5 - t4)*1e6:9.2f} µs")

        # ---------- Average timing using timeit over a few runs ----------
        # Create bound callables to avoid re-constructing inside timeit
        def _run_bfs():
            sol_bfs.nearest([row[:] for row in grid])

        def _run_dp():
            sol_dp.nearest([row[:] for row in grid])

        reps = 50
        avg_bfs = timeit.timeit(_run_bfs, number=reps) / reps
        avg_dp = timeit.timeit(_run_dp, number=reps) / reps

        print(f"\nAverage over {reps} runs (timeit):")
        print(f"  BFS       : {avg_bfs*1e6:9.2f} µs/run")
        print(f"  DP two-pass: {avg_dp*1e6:9.2f} µs/run")

        print("\n" + "-"*60 + "\n")


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print("==== TOTAL PROGRAM RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

**What this script gives you**

* Clear outputs for BFS, DP two-pass, and Brute (they should match).
* Single-run microsecond timings and averaged timings via `timeit`.
* Inline comments noting the **time/space** at each step—great to cite during interviews.
