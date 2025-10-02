# Find whether path exist

**Difficulty:** Medium
**Accuracy:** 45.09%
**Submissions:** 94K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a grid of size **n * n** filled with **0, 1, 2, 3**. Check whether there is a path possible from the **source** to **destination**. You can traverse **up, down, right and left**.

The description of cells is as follows:

* A value of cell **1** means **Source**.
* A value of cell **2** means **Destination**.
* A value of cell **3** means **Blank cell**.
* A value of cell **0** means **Wall** (blocked cell which we cannot traverse).

**Note:** There are only a single source and a single destination.

---

## Examples

### Example 1

**Input:**

```
grid = {{3,0,3,0,0},{3,0,0,0,3},{3,3,3,3,3},{0,2,3,0,0},{3,0,0,1,3}}
```

**Output:**

```
0
```

**Explanation:**
The grid is-

```
3 0 3 0 0
3 0 0 0 3
3 3 3 3 3
0 2 3 0 0
3 0 0 1 3
```

There is no path to reach at **(3,1)** i.e., at destination from **(4,3)** i.e., source.

---

### Example 2

**Input:**

```
grid = {{1,3},{3,2}}
```

**Output:**

```
1
```

**Explanation:**
The grid is-

```
1 3
3 2
```

There is a path from **(0,0)** i.e., source to **(1,1)** i.e., destination.

---

## Expected Complexities

* **Expected Time Complexity:** ( O(n^2) )
* **Expected Auxiliary Space:** ( O(n^2) )

---

## Constraints

* ( 1 \le n \le 500 )

---

## Company Tags

* Morgan Stanley
* Amazon
* Microsoft
* Samsung
* Adobe

---

## Topic Tags

* DFS
* Matrix
* Graph
* BFS
* Data Structures
* Algorithms

---

## Related Articles

* Find Whether Path Two Cells Matrix

---

---

awesome — here’s an interview-ready pack: clear intuition, step-by-step dry run, and multiple Python solutions in your requested template.

---

# 2) Intuition & Approach

We have an `n x n` grid with:

* `1` = **source** (exactly one),
* `2` = **destination** (exactly one),
* `3` = **blank/passable**,
* `0` = **wall** (blocked).

You can move **up / down / left / right**.
This is a classic **reachability** problem on a grid → treat each passable cell (1/2/3) as a node, add edges to its 4-neighbors (if inside bounds and not a wall). Then check if `source` can reach `destination`.

**Natural solutions:**

* **BFS (most expected):** level-order from source until we see destination.
* **DFS (recursive or stack):** depth-first search from source; stop when we hit destination.
* **Union-Find (DSU):** union all adjacent passable cells; finally check if `src` and `dst` are in the same set. (Good to mention in interviews; BFS/DFS is simpler.)

**Why O(n²)?**
We’ll visit each cell at most once and look at up to 4 neighbors → **O(n²)** time and **O(n²)** space for `visited` (and queue/stack).

---

## Step-by-step Dry Run

### Example 2 (has a path)

```
grid =
1 3
3 2
```

Coordinates: `(0,0)=1` (source), `(1,1)=2` (destination). All `3` are passable.

**BFS:**

1. Enqueue source `(0,0)`. Mark visited.
2. Pop `(0,0)`. Its passable neighbors: `(1,0)` and `(0,1)` → enqueue both.
3. Pop `(1,0)` → neighbors: `(1,1)` is destination → **found** → return `1`.

**DFS** would also reach `(1,1)` via either `(0,0)→(1,0)→(1,1)` or `(0,0)→(0,1)→(1,1)`.

### Example 1 (no path)

```
3 0 3 0 0
3 0 0 0 3
3 3 3 3 3
0 2 3 0 0
3 0 0 1 3
source = (4,3), destination = (3,1)
```

Start BFS at `(4,3)`. From there, the only passable neighbor is `(4,4)` (since `(4,2)` is `0`, `(3,3)` is `0`, `(5,3)` is out).
From `(4,4)` there are no further passable new cells (blocked or out-of-bounds). Queue empties without ever reaching `(3,1)` → **no path** → return `0`.

---

# 3) Python solutions (interview-ready, inline comments)

### A) BFS (Kahn-style level traversal) — **primary/most expected**

```python
from collections import deque

class Solution:
    
    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        """
        BFS from the unique source over passable cells (1/2/3) looking for destination (2).

        Time:  O(n^2)   - each cell enqueued/dequeued at most once, 4 neighbors checked per cell.
        Space: O(n^2)   - 'visited' + queue in worst case.
        """
        n = len(grid)
        if n == 0:
            return 0  # no grid
        
        # 1) Locate source (and optionally destination) ------------------ O(n^2)
        src = None
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    src = (r, c)
                    break
            if src:
                break
        
        if not src:
            return 0  # no source found (shouldn't happen per constraints)
        
        # 2) Standard BFS setup ------------------------------------------ O(1)
        q = deque([src])
        visited = [[False] * n for _ in range(n)]
        visited[src[0]][src[1]] = True
        
        # 4-directional movement
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # 3) BFS loop ----------------------------------------------------- O(n^2)
        while q:
            r, c = q.popleft()  # Dequeue in O(1)
            
            # If we reached destination, return 1 in O(1)
            if grid[r][c] == 2:
                return 1
            
            # Explore 4 neighbors (bounded constant factor)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # Boundary + wall + visited checks in O(1)
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        # Queue exhausted without hitting destination
        return 0
```

---

### B) Recursive DFS (clean & concise)

```python
class Solution:
    
    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        """
        DFS with visited marking.

        Time:  O(n^2)   - each cell visited once at most.
        Space: O(n^2)   - recursion stack in worst case + visited.
        """
        n = len(grid)
        if n == 0:
            return 0
        
        # Find source ----------------------------------------------------- O(n^2)
        src = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    src = (i, j)
                    break
            if src:
                break
        if not src:
            return 0
        
        visited = [[False]*n for _ in range(n)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # DFS returns True if destination found
        def dfs(r, c):
            # Out of bounds or wall or already visited -------------------- O(1)
            if r < 0 or r >= n or c < 0 or c >= n or visited[r][c] or grid[r][c] == 0:
                return False
            if grid[r][c] == 2:
                return True
            visited[r][c] = True
            # Explore neighbors ------------------------------------------- O(1) * 4
            for dr, dc in DIRS:
                if dfs(r+dr, c+dc):
                    return True
            return False
        
        return 1 if dfs(src[0], src[1]) else 0
```

---

### C) Union-Find (DSU) — **good to mention**

```python
class Solution:
    
    # Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        """
        DSU: union all adjacent passable cells; check if src and dst share the same root.

        Time:  O(n^2 * α(n^2)) ~ O(n^2)  (α is inverse Ackermann, ~constant)
        Space: O(n^2)
        """
        n = len(grid)
        if n == 0:
            return 0
        
        # Helper to map (r,c) -> 1D id
        def id_of(r, c): return r*n + c
        
        # DSU with path compression + union by size ---------------------- O(1) amortized per op
        parent = list(range(n*n))
        size = [1]*(n*n)
        
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
        
        src_id = dst_id = None
        DIRS = [(1,0), (0,1)]  # only need to check right & down to avoid duplicate unions
        
        # Pass 1: identify src/dst and union adjacent passable cells ----- O(n^2)
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if val != 0:  # passable
                    if val == 1: src_id = id_of(r, c)
                    if val == 2: dst_id = id_of(r, c)
                    # union with right and down neighbors if passable
                    for dr, dc in DIRS:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 0:
                            union(id_of(r, c), id_of(nr, nc))
        
        if src_id is None or dst_id is None:
            return 0
        
        # Pass 2: connectivity check ------------------------------------- O(α(n^2))
        return 1 if find(src_id) == find(dst_id) else 0
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why BFS/DFS is O(n²) here?**
Because there are `n²` cells and each cell is processed at most once; each processing checks a constant number (4) of neighbors.

**Q2. What’s the difference between BFS and DFS in this problem?**
Both detect reachability with the same complexity. BFS is often preferred for shortest-path in unweighted grids; here we only need existence, so either works.

**Q3. What edge cases do you handle?**

* No source or destination (defensive: return 0).
* Source equals destination (if a cell with value `1` is also `2`—won’t happen by spec, but conceptually it’s immediate success).
* Grids with size 1, fully blocked borders, or isolated open areas.

**Q4. Why keep a `visited` array?**
To prevent revisiting and infinite loops; guarantees each cell is processed once.

**Q5. Could we do it in-place without extra `visited`?**
Yes—temporarily mark visited passable cells (e.g., change `3` to `-1`) during traversal, then optionally restore. But many platforms disallow mutation; a boolean `visited` is safer.

**Q6. Why even mention DSU?**
It shows breadth: you can solve reachability by **connectivity**. DSU unions adjacent passable cells and answers in almost-linear time. It’s elegant when many connectivity queries are asked on the same static grid.

**Q7. If diagonal moves were allowed?**
Add 4 more directions to the neighbor list. Complexity remains **O(n²)**.

**Q8. How to return the actual path, not just existence?**
Store parent pointers (`parent[(r,c)] = (pr,pc)`) during BFS. When destination is reached, reconstruct the path by backtracking parents.

---

---

awesome — here’s a **runnable, interview-style full program** for *Find whether path exist* with:

* Primary BFS solution in your exact template,
* Inline **time/space complexity** notes at each step,
* A small **driver** that prints inputs & outputs,
* **timeit** benchmarks for the full run,
* Plus a short list of high-value **real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Find whether a path exists in an n x n grid with cells:
  1 = Source, 2 = Destination, 3 = Blank/Passable, 0 = Wall/Blocked.
We can move in 4 directions (up, down, left, right). Return 1 if a path exists, else 0.

Primary approach: BFS from the unique source.

Global complexities (for an n x n grid):
  - Time:  O(n^2)   # each cell processed at most once; each has up to 4 neighbors (constant)
  - Space: O(n^2)   # visited matrix + queue in the worst case
"""

from collections import deque
import timeit
from typing import List


class Solution:
    # ------------------------------------------------------------------------------
    # Function to find whether a path exists from the source to destination.
    # ------------------------------------------------------------------------------
    def is_Possible(self, grid: List[List[int]]) -> int:
        """
        BFS over passable cells (1/2/3) looking for destination (2).

        Steps:
          1) Find the source cell '1' ---------------------------------- Time: O(n^2), Space: O(1)
          2) Initialize queue and visited matrix ----------------------- Time: O(1),   Space: O(n^2)
          3) Standard BFS (pop, check, push neighbors) ---------------- Time: O(n^2), Space: O(n^2)
          4) If destination found -> return 1; else 0.

        Returns:
            1 if path exists, otherwise 0.
        """
        n = len(grid)
        if n == 0:
            return 0  # defensive

        # (1) Locate the source cell ------------------------------------ O(n^2)
        src = None
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    src = (r, c)
                    break
            if src:
                break

        if not src:
            # Per problem there is exactly one source, but keep it safe
            return 0

        # (2) Setup BFS queue and visited matrix ------------------------ O(1) + O(n^2) space
        q = deque([src])                           # queue for BFS (Space up to O(n^2))
        visited = [[False] * n for _ in range(n)]  # visited marks (Space O(n^2))
        visited[src[0]][src[1]] = True

        # Direction vectors: 4-neighborhood ----------------------------- O(1)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # (3) BFS traversal ---------------------------------------------- O(n^2)
        while q:
            r, c = q.popleft()                    # Dequeue: O(1)

            # Destination check: O(1)
            if grid[r][c] == 2:
                return 1

            # Visit all 4 neighbors: constant work per cell (4 checks)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # Boundary check + not visited + not a wall: O(1)
                if (
                    0 <= nr < n and 0 <= nc < n and
                    not visited[nr][nc] and
                    grid[nr][nc] != 0     # passable if 1/2/3
                ):
                    visited[nr][nc] = True
                    q.append((nr, nc))    # Enqueue: O(1)

        # (4) Queue exhausted; destination not reached ------------------- O(1)
        return 0


# ----------------------------- Optional parity solution (DFS) -----------------------------
class SolutionDFS:
    def is_Possible(self, grid: List[List[int]]) -> int:
        """
        Recursive DFS variant — same asymptotics.
        Time:  O(n^2)
        Space: O(n^2) (visited + recursion depth in worst case)
        """
        n = len(grid)
        if n == 0:
            return 0

        src = None
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    src = (r, c)
                    break
            if src:
                break
        if not src:
            return 0

        visited = [[False] * n for _ in range(n)]
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # O(1) guards
            if r < 0 or r >= n or c < 0 or c >= n:
                return False
            if visited[r][c] or grid[r][c] == 0:
                return False
            if grid[r][c] == 2:
                return True
            visited[r][c] = True
            # Explore 4 neighbors: constant factor
            for dr, dc in DIRS:
                if dfs(r + dr, c + dc):
                    return True
            return False

        return 1 if dfs(src[0], src[1]) else 0


# ----------------------------- Benchmark helper using timeit -----------------------------
def bench(func, *args, number=10000):
    """
    Measure average seconds per run for func(*args) over 'number' iterations.
    Note: micro-benchmarks are dominated by Python overhead for tiny inputs.
    """
    t = timeit.timeit(lambda: func(*args), number=number)
    return t / number


# ----------------------------- Main Program: inputs, outputs, timings -----------------------------
if __name__ == "__main__":
    # Test cases from the problem + a couple extras
    tests = [
        (
            [
                [3, 0, 3, 0, 0],
                [3, 0, 0, 0, 3],
                [3, 3, 3, 3, 3],
                [0, 2, 3, 0, 0],
                [3, 0, 0, 1, 3],
            ],
            0,  # expected
            "Example 1: No path"
        ),
        (
            [
                [1, 3],
                [3, 2],
            ],
            1,  # expected
            "Example 2: Path exists"
        ),
        (
            [
                [1, 0, 3],
                [3, 0, 3],
                [3, 3, 2],
            ],
            1,
            "Zig-zag around walls"
        ),
        (
            [
                [1, 0],
                [0, 2],
            ],
            0,
            "Blocked destination"
        ),
    ]

    print("=== Find whether path exist (BFS primary) ===\n")
    bfs_solver = Solution()
    dfs_solver = SolutionDFS()  # for parity checks

    for grid, expected, note in tests:
        out_bfs = bfs_solver.is_Possible([row[:] for row in grid])  # keep grid intact for parity
        out_dfs = dfs_solver.is_Possible([row[:] for row in grid])

        print(f"{note}")
        for row in grid:
            print(row)
        print(f"BFS output: {out_bfs} | DFS output: {out_dfs} | Expected: {expected}")
        print(f"Both methods agree? {out_bfs == out_dfs}\n")

    # ---------------- Timings with timeit (average seconds per run) ----------------
    print("=== Timings (average seconds per run) ===")
    small_grid = [
        [1, 3],
        [3, 2],
    ]
    medium_grid = [
        [3, 3, 3, 0, 3, 3, 3],
        [0, 0, 3, 0, 3, 0, 3],
        [3, 3, 3, 3, 3, 0, 3],
        [3, 0, 0, 0, 3, 0, 3],
        [3, 3, 3, 3, 3, 0, 3],
        [0, 0, 0, 0, 3, 0, 3],
        [1, 3, 3, 3, 3, 3, 2],
    ]

    runs_small = 20000
    runs_medium = 5000

    t_bfs_small = bench(bfs_solver.is_Possible, [row[:] for row in small_grid], number=runs_small)
    t_dfs_small = bench(dfs_solver.is_Possible, [row[:] for row in small_grid], number=runs_small)
    print(f"Small grid runs={runs_small}: BFS {t_bfs_small:.8e}s | DFS {t_dfs_small:.8e}s")

    t_bfs_med = bench(bfs_solver.is_Possible, [row[:] for row in medium_grid], number=runs_medium)
    t_dfs_med = bench(dfs_solver.is_Possible, [row[:] for row in medium_grid], number=runs_medium)
    print(f"Medium grid runs={runs_medium}: BFS {t_bfs_med:.8e}s | DFS {t_dfs_med:.8e}s")

    print("\nNote: timings depend on machine and Python version.")
```

---

## 6) Real-World Use Cases (the important ones)

1. **Robot/Drone Navigation in a Warehouse/Factory**
   Check if a path exists from a robot’s current cell to a destination while avoiding blocked cells/racks.

2. **Network/Infrastructure Reachability**
   Model nodes as grid points and walls as outages/firewalls; determine if service can still reach a target endpoint.

3. **Maze/Security & Evacuation Planning**
   Simulate whether there’s a viable route from a room (source) to an exit (destination) with certain doors blocked.

4. **Game AI / Path Existence Checks**
   In tile-based games, quickly check if a unit can reach a goal before computing expensive shortest paths.
