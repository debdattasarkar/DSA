# Distance of nearest cell having 1

**Difficulty:** Medium
**Accuracy:** 47.7%
**Submissions:** 106K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a binary grid of **n * m**. Find the distance of the nearest **1** in the grid for each cell.

The distance is calculated as **|i₁ − i₂| + |j₁ − j₂|**, where `i₁, j₁` are the row and column of the current cell, and `i₂, j₂` are the row and column of the nearest cell having value **1**.
There should be **at least one 1** in the grid.

---

## Examples

### Example 1

**Input:**

```
grid = [[0,1,1,0],
        [1,1,0,0],
        [0,0,1,1]]
```

**Output:**

```
[[1,0,0,1],
 [0,0,1,1],
 [1,1,0,0]]
```

**Explanation:**
The grid is:

```
0 1 1 0
1 1 0 0
0 0 1 1
```

0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1 from 1's at (0,1), (0,2), (0,2), (2,3), (1,0) and (1,1) respectively.

---

### Example 2

**Input:**

```
grid = [[1,0,1],
        [1,1,0],
        [1,0,0]]
```

**Output:**

```
[[0,1,0],
 [0,0,1],
 [0,1,2]]
```

**Explanation:**
The grid is:

```
1 0 1
1 1 0
1 0 0
```

0's at (0,1), (1,2), (2,1) and (2,2) are at distances of 1, 1, 1 and 2 from 1's at (0,0), (0,2), (2,0) and (1,1) respectively.

---

## Your Task

You don't need to read or print anything. Your task is to complete the function **`nearest()`** which takes the grid as an input parameter and **returns a matrix of the same dimensions** where the value at index `(i, j)` in the resultant matrix signifies the **minimum distance** to a cell with value **1** in the original `grid[i][j]`.

---

## Constraints

* (1 \le n, m \le 500)

---

## Expected Complexities

* **Time Complexity:** (O(n \times m))
* **Auxiliary Space:** (O(n \times m))

---

## Topic Tags

Matrix · Graph · **BFS** · Data Structures · Algorithms

---

## Related Articles

* Distance Nearest Cell 1 Binary Matrix

---

---

awesome — here’s a tight, interview-ready walkthrough + multiple Python solutions (with inline comments) for **Distance of nearest cell having 1**.

---

# 2) Intuition & step-by-step dry run

## Problem recap

For every cell in a binary grid, return the **Manhattan distance** to the nearest cell whose value is `1`.
Manhattan distance = `|r1-r2| + |c1-c2|`. Movement is 4-directional.

### Key idea (most expected)

Treat all `1` cells as **sources** and run a **multi-source BFS**.
Because edges are unweighted (each move costs 1), BFS from all sources simultaneously yields the **shortest distance** to the nearest `1` for every cell.

### Why it works

BFS explores by layers: distance 0 (all 1s), then distance 1 neighbors, then distance 2, … The first time we reach a cell is its minimum distance to any `1`.

---

## Dry run (on Example 2)

```
grid =
1 0 1
1 1 0
1 0 0
```

**Init**
Queue with all 1’s at distance 0:
`q = [(0,0),(0,2),(1,0),(1,1),(2,0)]`, dist of these = 0. All others = -1 (unvisited).

**BFS layer by layer**

* Pop (0,0) → push its 0-neighbors with dist 1: (0,1) ← 1
* Pop (0,2) → push (1,2) ← 1
* Pop (1,0) → (2,0) already 0; (2,0) is source; others seen
* Pop (1,1) → (2,1) ← 1
* Pop (2,0) → (2,1) already 1

Next layer:

* Pop (0,1) dist=1 → neighbors updated if -1 (none)
* Pop (1,2) dist=1 → (2,2) ← 2
* Pop (2,1) dist=1 → (2,2) already 2

Done. Final `dist`:

```
0 1 0
0 0 1
0 1 2
```

Matches the sample.

---

# 3) Python solutions (what interviewers expect)

### A) Multi-source BFS (primary / optimal)

```python
from collections import deque

class Solution:

    # Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        """
        Multi-source BFS seeded with all '1' cells.
        Let n = rows, m = cols.

        Time : O(n*m)    each cell enqueued/dequeued at most once
        Space: O(n*m)    for the queue + distance matrix
        """
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(n)]       # -1 means unvisited
        q = deque()

        # Seed BFS with all 1-cells at distance 0  ---------------- O(n*m)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        # 4-directional moves
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS ------------------------------------------------------ O(n*m)
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # If not visited, set dist and enqueue
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist
```

---

### B) Two-pass DP relaxation (also O(n·m), no queue)

Idea: initialize `dist = 0` for 1’s, `INF` for 0’s.
Two sweeps relax distances using neighbors already processed:

* Pass 1 (top-left → bottom-right): use **up / left** neighbors
* Pass 2 (bottom-right → top-left): use **down / right** neighbors

```python
class Solution:

    def nearest(self, grid):
        """
        Two-pass DP (Manhattan distance relaxation).
        Time : O(n*m)
        Space: O(1) extra (besides the dist matrix)
        """
        n, m = len(grid), len(grid[0])
        INF = 10**9

        # Init: 0 for ones, INF for zeros ------------------------- O(n*m)
        dist = [[0 if grid[r][c] == 1 else INF for c in range(m)] for r in range(n)]

        # Pass 1: top-left to bottom-right ------------------------- O(n*m)
        for r in range(n):
            for c in range(m):
                if dist[r][c] == 0:  # already 1
                    continue
                if r > 0:
                    dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                if c > 0:
                    dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)

        # Pass 2: bottom-right to top-left ------------------------- O(n*m)
        for r in range(n-1, -1, -1):
            for c in range(m-1, -1, -1):
                if r+1 < n:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c+1 < m:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)

        return dist
```

> This DP works because Manhattan distance decomposes across axes, and each pass propagates the best known distances from already-processed neighbors.

---

### C) Brute force (educational baseline, not for production)

For each cell, run a BFS until you hit a `1`. Worst case **O((n·m)²)**.

```python
from collections import deque

class Solution:

    def nearest(self, grid):
        """
        For each cell, run a BFS to nearest '1'.
        Time : O((n*m)^2) worst-case
        Space: O(n*m) for BFS queue + visited
        """
        n, m = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = [[0]*m for _ in range(n)]

        def bfs(sr, sc):
            if grid[sr][sc] == 1:
                return 0
            vis = [[False]*m for _ in range(n)]
            q = deque([(sr, sc, 0)])
            vis[sr][sc] = True
            while q:
                r, c, d = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]:
                        if grid[nr][nc] == 1:
                            return d+1
                        vis[nr][nc] = True
                        q.append((nr, nc, d+1))
            return 0  # should not happen (at least one 1 exists)

        for i in range(n):
            for j in range(m):
                ans[i][j] = bfs(i, j)

        return ans
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why multi-source BFS?**
Because we want the minimum distance to **any** `1`. Seeding BFS with **all** 1’s (distance 0) ensures each cell’s first visit is its shortest distance in an unweighted 4-connected grid.

**Q2. Time/space complexity of BFS solution?**
`O(n·m)` time (each cell visited once) and `O(n·m)` space for the queue and distance matrix.

**Q3. How does the two-pass DP work?**
Initialize `0` at 1’s and `INF` at 0’s. Two linear passes propagate distances from already-computed neighbors (up/left then down/right). Manhattan distance is additive over steps, so local relaxations converge to the true minimum.

**Q4. Which approach should I present first?**
Multi-source BFS. It’s idiomatic and maps directly to “shortest distance to sources” in an unweighted graph.

**Q5. Edge cases?**

* All ones → all zeros in result.
* Exactly one `1` → distances equal Manhattan distance to that point.
* At least one `1` is guaranteed, so no cell remains `INF`.

**Q6. Diagonal moves allowed?**
No, only 4-directional. If diagonals were allowed, you’d add 4 more directions to BFS; DP variant would need a different relaxation (Chebyshev distance).

**Q7. Can we do it in place?**
You can reuse an output matrix only; avoid overwriting the original grid values needed for seeding. DP computes into `dist` without extra structures.

**Q8. Why not Dijkstra?**
All edges have weight 1; BFS (or the DP) is enough and faster/simpler.

---

---

awesome — here’s a **runnable, interview-style full program** for **Distance of nearest cell having 1** with:

* your requested class/method signature,
* detailed inline **time/space complexity** notes,
* a tiny **driver** that prints inputs & outputs,
* and **timeit** micro-benchmarks comparing **Multi-source BFS** (primary) vs **Two-pass DP**.

I’ve also added a short list of **real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Distance of nearest cell having 1 (Manhattan distance, 4-neighbors)

Primary approach (Solution.nearest):
  - Multi-source BFS seeded with all cells that contain 1 (distance 0).
  - Explore in layers; first visit to each cell gives its shortest distance.

Alternate approach (SolutionDP.nearest):
  - Two-pass DP relaxation:
      dist = 0 for cells with 1, INF for cells with 0
      pass1 TL->BR: relax from up/left
      pass2 BR->TL: relax from down/right

Global complexities (n x m grid):
  - Multi-source BFS:
      Time:  O(n*m)   (each cell enqueued/dequeued at most once; 4 neighbors constant)
      Space: O(n*m)   (queue + distance matrix)
  - Two-pass DP:
      Time:  O(n*m)   (two linear sweeps)
      Space: O(n*m)   (dist matrix; no extra big structures)
"""

from collections import deque
import timeit
from typing import List


# ------------------------------ Primary: Multi-source BFS ------------------------------ #
class Solution:
    # Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Multi-source BFS from all '1' cells.

        Steps:
          1) Initialize dist with -1 (unvisited).                   Time: O(n*m), Space: O(n*m)
             Push all (r,c) with grid[r][c]==1 into queue; dist=0.
          2) BFS: pop cell, try its 4 neighbors;                     Time: O(n*m)
             if neighbor unvisited, set dist=dist[cur]+1 and enqueue.
          3) Return dist matrix.

        Returns:
            dist[r][c] = min Manhattan distance from (r,c) to any '1'.
        """
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(n)]         # O(n*m) space
        q = deque()                                  # O(n*m) worst-case

        # (1) Seed queue with all 1-cells at distance 0 -------------- O(n*m)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        # 4-directional neighbors (constant)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # (2) BFS traversal ------------------------------------------- O(n*m)
        while q:
            r, c = q.popleft()  # O(1)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # push if inside grid and unvisited
                if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))  # O(1)

        return dist


# ------------------------------ Alternative: Two-pass DP ------------------------------ #
class SolutionDP:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Two-pass DP relaxation using Manhattan metric.

        Steps:
          1) dist = 0 where grid==1 else INF.                        Time: O(n*m)
          2) Pass 1 (top-left -> bottom-right): relax up/left.       Time: O(n*m)
          3) Pass 2 (bottom-right -> top-left): relax down/right.    Time: O(n*m)

        Returns:
            dist matrix with minimum distances.
        """
        n, m = len(grid), len(grid[0])
        INF = 10**9

        # (1) Init --------------------------------------------------- O(n*m)
        dist = [[0 if grid[r][c] == 1 else INF for c in range(m)] for r in range(n)]

        # (2) Pass 1: TL -> BR -------------------------------------- O(n*m)
        for r in range(n):
            for c in range(m):
                if dist[r][c] == 0:
                    continue
                if r > 0:
                    dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                if c > 0:
                    dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)

        # (3) Pass 2: BR -> TL -------------------------------------- O(n*m)
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if r + 1 < n:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c + 1 < m:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)

        return dist


# ------------------------------ Benchmark helper (timeit) ------------------------------ #
def bench(func, *args, number=2000):
    """
    Measure average seconds per run using timeit.
    On tiny inputs, Python call overhead dominates — treat numbers as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------ Pretty-print helper ------------------------------ #
def print_matrix(mat: List[List[int]]):
    for row in mat:
        print(row)


# ------------------------------------------ Demo ------------------------------------------ #
if __name__ == "__main__":
    print("=== Distance of Nearest 1 — Multi-source BFS (primary) vs Two-pass DP ===\n")

    tests = [
        # (grid, note)
        (
            [[0,1,1,0],
             [1,1,0,0],
             [0,0,1,1]],
            "Sample 1"
        ),
        (
            [[1,0,1],
             [1,1,0],
             [1,0,0]],
            "Sample 2"
        ),
        (
            [[0,0,0,0],
             [0,0,1,0],
             [0,0,0,0]],
            "Single 1 in the middle"
        ),
        (
            [[1,1,1],
             [1,1,1]],
            "All ones"
        ),
    ]

    bfs_solver = Solution()
    dp_solver = SolutionDP()

    for grid, note in tests:
        print(f">>> {note}")
        print("Input grid:")
        print_matrix(grid)

        out_bfs = bfs_solver.nearest([row[:] for row in grid])
        out_dp  = dp_solver.nearest([row[:] for row in grid])

        print("\nBFS output:")
        print_matrix(out_bfs)
        print("\nDP  output:")
        print_matrix(out_dp)

        print(f"\nResults identical? {out_bfs == out_dp}\n{'-'*60}\n")

    # ------------------------------ Timings ------------------------------ #
    print("=== Timings (average seconds per run) ===")
    small = [[1,0,1],[1,1,0],[1,0,0]]
    medium = [[0]*30 for _ in range(30)]
    medium[10][10] = 1
    medium[20][25] = 1
    large = [[0]*60 for _ in range(60)]
    for r in range(0, 60, 7):
        for c in range(0, 60, 11):
            large[r][c] = 1

    runs_small = 20000
    runs_medium = 2000
    runs_large = 500

    tb_s = bench(Solution().nearest, [row[:] for row in small], number=runs_small)
    td_s = bench(SolutionDP().nearest, [row[:] for row in small], number=runs_small)
    print(f"Small  (3x3)  runs={runs_small}:  BFS {tb_s:.8e}s  |  DP {td_s:.8e}s")

    tb_m = bench(Solution().nearest, [row[:] for row in medium], number=runs_medium)
    td_m = bench(SolutionDP().nearest, [row[:] for row in medium], number=runs_medium)
    print(f"Medium (30x30) runs={runs_medium}:  BFS {tb_m:.8e}s  |  DP {td_m:.8e}s")

    tb_l = bench(Solution().nearest, [row[:] for row in large], number=runs_large)
    td_l = bench(SolutionDP().nearest, [row[:] for row in large], number=runs_large)
    print(f"Large  (60x60) runs={runs_large}:  BFS {tb_l:.8e}s  |  DP {td_l:.8e}s")

    print("\nNote: timings vary by machine and Python version.")
```

### What this prints

* For each test: the **input grid**, **BFS output**, **DP output**, and whether they **match**.
* Then **timeit** averages for small/medium/large grids, comparing BFS and DP.

---

## 6) Real-World Use Cases (the important ones)

1. **Nearest Facility / Service Distance (city grid)**
   Compute distance from every block to the nearest **hospital/fire station** modeled as cells with `1`.

2. **Image Processing / Binary Masks**
   Distance to the nearest foreground pixel (approx. a simpler form of **distance transform**) for features like stroke expansion or thinning.

3. **Routing Heuristics / Initialization**
   Precompute lower-bound distances to targets to guide A* or to seed region growing in grid maps.

4. **Sensor Coverage & Placement**
   Evaluate coverage gaps: distance from each location to the nearest installed **sensor/AP/beacon**.
