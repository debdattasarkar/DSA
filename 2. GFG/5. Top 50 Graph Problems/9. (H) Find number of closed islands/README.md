# Find number of closed islands

**Difficulty:** Hard
**Accuracy:** 61.43%
**Submissions:** 28K+
**Points:** 8
**Average Time:** 30m

---

## Problem Statement

Given a **binary matrix** `mat[][]` of dimensions **N × M** such that `1` denotes **land** and `0` denotes **water**. Find the **number of closed islands** in the given matrix.

An island is a **4-directional** (up, right, down, left) connected part of `1`s.

**Note:**
A **closed island** is a group of `1`s **surrounded by only `0`s on all the boundaries (except diagonals)**. In simple words, a closed island is an island whose **none of the `1`s lie on the edges** of the matrix.

---

## Example 1

**Input:**

```
N = 5, M = 8
mat[][] = {
 {0, 0, 0, 0, 0, 0, 0, 1},
 {0, 1, 1, 1, 1, 0, 0, 1},
 {0, 1, 0, 1, 0, 0, 0, 1},
 {0, 1, 1, 1, 0, 1, 0, 1},
 {1, 0, 0, 0, 0, 1, 0, 1}
}
```

**Output:**

```
2
```

**Explanation:**

```
mat[][] = {
 {0, 0, 0, 0, 0, 0, 0, 1},
 {0, 1, 1, 1, 1, 0, 0, 1},
 {0, 1, 0, 1, 0, 0, 0, 1},
 {0, 1, 1, 1, 0, 1, 0, 1},
 {1, 0, 0, 0, 0, 1, 0, 1}
}
```

There are **2 closed islands**. The islands in dark are closed because they are completely surrounded by `0`s (water). There are two more islands in the last column of the matrix, but they are **not completely surrounded by `0`s**. Hence they are **not** closed islands.

---

## Example 2

**Input:**

```
N = 3, M = 3
mat[][] = {
 {1, 0, 0},
 {0, 1, 0},
 {0, 0, 1}
}
```

**Output:**

```
1
```

**Explanation:**

```
mat[][] = {
 {1, 0, 0},
 {0, 1, 0},
 {0, 0, 1}
}
```

There is just **one** closed island.

---

## Your Task

You don’t need to read input or print anything. Your task is to complete the function **`closedIslands()`** which takes two integers `N` and `M`, and a 2D binary matrix `mat` as input parameters and **returns the number of closed islands**.

---

## Expected Complexities

* **Time Complexity:** `O(N * M)`
* **Auxiliary Space:** `O(N * M)`

---

## Constraints

* `1 ≤ N, M ≤ 500`

---

## Company Tags

Google

---

## Topic Tags

DFS · Matrix · Graph · BFS · Union-Find · Data Structures · Algorithms

---

## Related Articles

* Find Number Of Closed Islands In Given Matrix

---

---

awesome — here’s an interview-ready pack for **Find number of closed islands**: a clear intuition + dry run, multiple Python solutions in your requested template (with inline complexity notes), and high-yield interview Q&A.

---

## 2) Intuition & Step-by-Step Dry Run

**Definitions**

* Grid has `1 = land`, `0 = water`.
* 4-directional adjacency (up, down, left, right).
* A **closed island** is a connected component of `1`s with **no cell on the border** (hence completely surrounded by `0`s).

### Core idea (what interviewers expect)

There are two equally good O(N·M) strategies:

1. **Border flood-fill of land**
   Any island touching the border **cannot** be closed. Flood-fill all `1`s reachable from the border and mark them as **open**. Then count the remaining unmarked `1` components — those are **closed**.

2. **Component DFS/BFS with a flag**
   For each unvisited `1`, traverse its component. If any cell of this component lies on the border, mark **not closed**; otherwise count it.

Both run in **O(N·M)** time and **O(N·M)** space (visited/queue/stack).

---

### Dry run (Example 1)

```
N=5, M=8
mat =
0 0 0 0 0 0 0 1
0 1 1 1 1 0 0 1
0 1 0 1 0 0 0 1
0 1 1 1 0 1 0 1
1 0 0 0 0 1 0 1
```

**Border flood-fill approach:**

1. Push all **border cells** that are `1` into a queue:

   * Row 0: (0,7) is `1`
   * Row 4: (4,0) is `1`, (4,5) is `1`, (4,7) is `1`
   * Col 0 and Col 7 already covered above (duplicates okay if guarded by visited)
2. BFS from these, mark visited as **open** (or visited). You’ll end up marking the rightmost column islands (those touching col 7) and the land at (4,0)/(4,5) and anything connected to them.
3. Now scan interior. The big diamond-like island in the middle **does not touch border** — it remains unvisited → **closed**.
4. There are **2** such closed components → answer **2**.

---

## 3) Python solutions (interview-ready, multiple ways)

Return just the **count**.

### A) BFS from border 1’s, then count remaining land components (primary)

```python
# User function Template for python3

from collections import deque

class Solution:
    def closedIslands(self, matrix, N, M):
        """
        Approach: Flood-fill all land that touches the border; then count the
        remaining land components (those are closed).

        Let n=N, m=M.
        Time : O(n*m)  - each cell visited at most once across all BFS runs
        Space: O(n*m)  - visited + queue worst case
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        visited = [[False] * m for _ in range(n)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        # 1) Remove/open all border-connected land ------------------ O(n*m)
        # Top & bottom rows
        for c in range(m):
            if matrix[0][c] == 1 and not visited[0][c]:
                bfs(0, c)
            if matrix[n-1][c] == 1 and not visited[n-1][c]:
                bfs(n-1, c)
        # Left & right columns
        for r in range(n):
            if matrix[r][0] == 1 and not visited[r][0]:
                bfs(r, 0)
            if matrix[r][m-1] == 1 and not visited[r][m-1]:
                bfs(r, m-1)

        # 2) Count closed islands among the remaining land ---------- O(n*m)
        count = 0
        for r in range(1, n-1):          # interior only is enough, but whole scan is fine
            for c in range(1, m-1):
                if matrix[r][c] == 1 and not visited[r][c]:
                    bfs(r, c)            # mark this closed component
                    count += 1

        return count
```

---

### B) Single-pass BFS per component with a “touches border” flag (also O(N·M))

```python
from collections import deque

class Solution:
    def closedIslands(self, matrix, N, M):
        """
        For each unvisited land cell, BFS its component.
        If any cell in the component lies on the border, it's NOT closed.
        Otherwise, increase count.
        
        Time : O(n*m)
        Space: O(n*m)
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        visited = [[False] * m for _ in range(n)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            touches_border = (sr == 0 or sc == 0 or sr == n-1 or sc == m-1)
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        if nr == 0 or nc == 0 or nr == n-1 or nc == m-1:
                            touches_border = True
                        q.append((nr, nc))
            return 0 if touches_border else 1

        count = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 1 and not visited[r][c]:
                    count += bfs(r, c)
        return count
```

> This version never does an initial border pass; it decides closed/open per component in a single BFS/DFS. Same complexity.

---

### C) Union-Find (DSU) with a dummy border node (nice to mention)

```python
class Solution:
    def closedIslands(self, matrix, N, M):
        """
        DSU approach:
          - Make a DSU over all cells + one dummy node for the border.
          - Union adjacent land cells (4-dir).
          - Union any border-land cell with the dummy.
          - Count distinct roots of land components that are NOT connected to dummy.

        Time : O(n*m * α(n*m)) ~ O(n*m)
        Space: O(n*m)
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        size = n * m
        dummy = size  # border land root
        parent = list(range(size + 1))
        rank = [0] * (size + 1)

        def idx(r, c): return r * m + c

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        # Union neighboring land and link border-land to dummy ----- O(n*m)
        for r in range(n):
            for c in range(m):
                if matrix[r][c] != 1:
                    continue
                idrc = idx(r, c)
                if r == 0 or c == 0 or r == n-1 or c == m-1:
                    union(idrc, dummy)
                if r+1 < n and matrix[r+1][c] == 1:
                    union(idrc, idx(r+1, c))
                if c+1 < m and matrix[r][c+1] == 1:
                    union(idrc, idx(r, c+1))

        # Count unique roots among interior land not connected to dummy
        root_dummy = find(dummy)
        seen = set()
        for r in range(1, n-1):
            for c in range(1, m-1):
                if matrix[r][c] == 1:
                    rt = find(idx(r, c))
                    if rt != root_dummy:
                        seen.add(rt)
        return len(seen)
```

---

## 4) Interview Q&A (high-yield)

**Q1. What exactly makes an island “closed”?**
A connected component of `1`s is closed if **none** of its cells lie on the **outer border** of the grid (0th/last row/column). With 4-directional connectivity only.

**Q2. Why does “border flood-fill” solve it?**
Any land touching the border cannot be surrounded by `0`s on all sides. If we remove/mark all border-reachable land first, the remaining `1` components are necessarily enclosed → closed.

**Q3. Complexity of your solutions?**
All three are **O(N·M)** time.
Space: **O(N·M)** for visited/queue/stack (BFS/DFS) or DSU arrays.

**Q4. DFS vs BFS vs DSU — which to present?**
Lead with **BFS/DFS** (simplest, linear). Mention **DSU** to show breadth; useful when you already maintain DSU for other operations or incremental updates.

**Q5. Do diagonals matter?**
No — only up/down/left/right. If diagonals were allowed, the definition of “closed” changes and the connectivity set grows by 4.

**Q6. Edge cases to test?**

* All water → `0`.
* All land → `0` (touches border).
* Single cell islands inside a moat of water → count them.
* Narrow grids (1 row/1 col): any land is border → `0`.

**Q7. Can we do it in place without extra visited?**
Yes — you can temporarily write a marker value (e.g., `2`) during flood-fill and then optionally restore. Many platforms allow mutation.

**Q8. Why not check each island’s “surrounded by zeros” directly?**
That reduces to “does it touch border?” when adjacency is 4-dir. So tracking a **touches_border** flag during traversal is sufficient and linear.

---

---

you got it — here’s a **runnable, interview-style full program** for **Find number of closed islands** with:

* your requested signature `class Solution.closedIslands(self, matrix, N, M)`,
* detailed **inline time/space complexity** notes,
* a tiny **driver** that prints **inputs & outputs**,
* and **timeit** micro-benchmarks comparing two linear-time approaches (**Border Flood-Fill** vs **Per-Component BFS with a touches-border flag**).

I’ve also added a short list of **high-value real-world use cases** at the end.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Find number of closed islands (4-directional)

Definitions:
- matrix[r][c] = 1 -> land, 0 -> water
- A closed island is a connected component of 1's such that *none* of its cells
  are on the border (0th or last row/column).

Approach A (primary): Border Flood-Fill
  1) Flood-fill (BFS) all land that is reachable from any border cell -> mark visited.
  2) Scan interior; every remaining unvisited land component is a closed island.

Approach B (alternative): Per-Component BFS With Flag
  For each unvisited land cell, BFS the component and track if *any* cell touches
  the border. If yes -> not closed; else -> closed.

Global complexities (N x M grid):
  Time : O(N*M)       # each cell enqueued/visited at most once
  Space: O(N*M)       # visited matrix + queue worst case
"""

from collections import deque
import timeit
from typing import List


# ------------------------ Approach A: Border Flood-Fill (primary) ------------------------ #
class Solution:
    def closedIslands(self, matrix: List[List[int]], N: int, M: int) -> int:
        """
        Flood-fill all border-connected land, then count remaining land components.

        Steps:
          1) visited[n][m] = False, multi-source BFS from *all* border land cells
             to mark them as non-closed (open).                         Time: O(N*M), Space: O(N*M)
          2) Scan the grid; for every unvisited land cell, BFS to mark its component
             and increment count (these are closed).                     Time: O(N*M)

        Returns:
          int: number of closed islands.
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        visited = [[False] * m for _ in range(n)]     # O(N*M) space
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> None:
            """Mark the whole land component starting at (sr,sc).  O(size_of_component)"""
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        # 1) Remove all border-connected land (cannot be closed) ----- O(N*M)
        # Top & bottom rows
        for c in range(m):
            if matrix[0][c] == 1 and not visited[0][c]:
                bfs(0, c)
            if matrix[n - 1][c] == 1 and not visited[n - 1][c]:
                bfs(n - 1, c)
        # Left & right columns
        for r in range(n):
            if matrix[r][0] == 1 and not visited[r][0]:
                bfs(r, 0)
            if matrix[r][m - 1] == 1 and not visited[r][m - 1]:
                bfs(r, m - 1)

        # 2) Count remaining (closed) components --------------------- O(N*M)
        count = 0
        for r in range(1, n - 1):
            for c in range(1, m - 1):
                if matrix[r][c] == 1 and not visited[r][c]:
                    bfs(r, c)        # mark this entire closed component
                    count += 1
        return count


# ---------------- Approach B: Per-Component BFS with "touches border" flag --------------- #
class SolutionFlag:
    def closedIslands(self, matrix: List[List[int]], N: int, M: int) -> int:
        """
        BFS each unvisited land component once; if it touches border -> not closed.
        Time:  O(N*M)   Space: O(N*M)
        """
        n, m = N, M
        if n == 0 or m == 0:
            return 0

        visited = [[False] * m for _ in range(n)]
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr: int, sc: int) -> int:
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            touches_border = (sr == 0 or sc == 0 or sr == n - 1 or sc == m - 1)
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        if nr == 0 or nc == 0 or nr == n - 1 or nc == m - 1:
                            touches_border = True
                        q.append((nr, nc))
            return 0 if touches_border else 1

        closed = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 1 and not visited[r][c]:
                    closed += bfs(r, c)
        return closed


# ------------------------------ Benchmark helper (timeit) ------------------------------- #
def bench(func, *args, number=3000):
    """
    Measure average seconds per run using timeit.
    On tiny inputs, Python overhead dominates; treat results as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------ Pretty printing ------------------------------------ #
def print_grid(g: List[List[int]]):
    for row in g:
        print(row)


# -------------------------------------------- Demo -------------------------------------------- #
if __name__ == "__main__":
    print("=== Closed Islands — Border Flood-Fill vs Component-Flag BFS ===\n")

    tests = [
        (
            # Example 1 from prompt
            [
                [0,0,0,0,0,0,0,1],
                [0,1,1,1,1,0,0,1],
                [0,1,0,1,0,0,0,1],
                [0,1,1,1,0,1,0,1],
                [1,0,0,0,0,1,0,1],
            ],
            "Example 1 (answer = 2)"
        ),
        (
            # Example 2 from prompt
            [
                [1,0,0],
                [0,1,0],
                [0,0,1],
            ],
            "Example 2 (answer = 1)"
        ),
        (
            # No closed islands (land touches border)
            [
                [1,1,1,1],
                [1,0,0,1],
                [1,0,0,1],
                [1,1,1,1],
            ],
            "Land ring touches border → 0"
        ),
        (
            # Two small closed islands inside
            [
                [0,0,0,0,0],
                [0,1,0,1,0],
                [0,0,0,0,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
            ],
            "Two closed islands → 2"
        ),
    ]

    A = Solution()
    B = SolutionFlag()

    for mat, note in tests:
        n, m = len(mat), len(mat[0])
        print(f">>> {note}")
        print("Input:")
        print_grid(mat)
        outA = A.closedIslands([row[:] for row in mat], n, m)
        outB = B.closedIslands([row[:] for row in mat], n, m)
        print(f"Output (Approach A): {outA}")
        print(f"Output (Approach B): {outB}")
        print(f"Both agree? {outA == outB}\n{'-'*60}\n")

    # ---------------------------- Timings (average seconds/run) ---------------------------- #
    print("=== Timings (average seconds per run) ===")
    small = [
        [0,0,0],
        [0,1,0],
        [0,0,0],
    ]  # 1 closed island in the center
    nS, mS = len(small), len(small[0])

    # Medium random-ish grid: a few inner islands
    medium = [[0]*40 for _ in range(40)]
    for r in range(5, 35, 6):
        for c in range(6, 34, 7):
            medium[r][c] = 1
            medium[r+1][c] = 1
            medium[r][c+1] = 1
            medium[r+1][c+1] = 1  # tiny 2x2 patches, most closed
    nM, mM = len(medium), len(medium[0])

    runs_small = 30000
    runs_medium = 4000

    tA_s = bench(Solution().closedIslands, [row[:] for row in small], nS, mS, number=runs_small)
    tB_s = bench(SolutionFlag().closedIslands, [row[:] for row in small], nS, mS, number=runs_small)
    print(f"Small  (3x3)   runs={runs_small}:  A {tA_s:.8e}s  |  B {tB_s:.8e}s")

    tA_m = bench(Solution().closedIslands, [row[:] for row in medium], nM, mM, number=runs_medium)
    tB_m = bench(SolutionFlag().closedIslands, [row[:] for row in medium], nM, mM, number=runs_medium)
    print(f"Medium (40x40) runs={runs_medium}:  A {tA_m:.8e}s  |  B {tB_m:.8e}s")

    print("\nNote: timings depend on machine and Python version.")
```

**What the program prints**

* For each test, it shows the **input grid**, the **outputs** from both approaches, and whether they **agree**.
* Then it prints **timeit** averages for small/medium grids.

---

## 6) Real-World Use Cases (the important ones)

1. **Geospatial analysis (lakes completely inland)**
   Count land regions fully surrounded by water (or vice versa) on rasterized maps.

2. **Image processing / segmentation**
   Detect **holes** (enclosed blobs) in binary masks; e.g., quality checks in printed circuit boards, medical imaging cavities.

3. **Game maps / maze regions**
   Identify safe rooms or enclosed areas (not connected to the boundary) for gameplay logic, spawn zones, or AI planning.

4. **Urban planning / enclosure detection**
   Find blocks or parcels fully enclosed by roads/canals to analyze accessibility or isolation.
