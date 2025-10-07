# Find the number of islands

**Difficulty:** Medium
**Accuracy:** 42.12%
**Submissions:** 253K+
**Points:** 4
**Average Time:** 20m

---

Given a grid of size **n × m** (n is the number of rows and m is the number of columns in the grid) consisting of **'W'**s (Water) and **'L'**s (Land). **Find the number of islands.**

**Note:** An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands **horizontally or vertically or diagonally** i.e., in **all 8 directions**.

---

## Examples

### Example 1

**Input:**

```
grid[][] = [
  ['L', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'L'],
  ['W', 'W', 'W', 'L', 'L'],
  ['W', 'W', 'W', 'W', 'W'],
  ['L', 'W', 'L', 'L', 'W']
]
```

**Output:**

```
4
```

**Explanation:**
The image below shows all the 4 islands in the grid.

```
L L L W W W
W L W W W L
W W W L L L
W W W W W W
L W L L W W
```

---

### Example 2

**Input:**

```
grid[][] = [
  ['W', 'L', 'L', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'W', 'L', 'W']
]
```

**Output:**

```
2
```

**Explanation:**
The image below shows 2 islands in the grid.

```
W L L L L W W W
W W L L L W L W
```

---

## Constraints

```
1 ≤ n, m ≤ 500
grid[i][j] ∈ {'L', 'W'}
```

---

## Expected Complexities

* **Time Complexity:** O(n * m)
* **Auxiliary Space:** O(n * m)

---

## Company Tags

Paytm, Flipkart, Amazon, Microsoft, OYO Rooms, Samsung, Snapdeal, Citrix, D-E-Shaw, MakeMyTrip, Ola Cabs, Visa, Intuit, Google, Linkedin, Opera, One97, Streamoid Technologies, Informatica, Walmart

---

## Topic Tags

DFS, Graph, Data Structures, Algorithms

---

## Related Interview Experiences

* Paytm Interview Experience Set 14 For Senior Android Developer
* Intuit Interview Set 8 On Campus
* Paytm Interview Experience Set 6 Recruitment Drive
* Paytm Interview Experience Set 7 Written Test Hyderabad
* Samsung RD Bangalore Freshers Full Timeinternship
* Amazon Interview Experience For Software Developer Intern
* Makemytrip Interview Experience Senior Software Engineer Android 3 Years Experienced

---

## Related Articles

* [Find The Number Of Islands Using DFS](https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/)

---

---

here’s a crisp, interview-ready walkthrough + multiple Python solutions for **Number of Islands (8-directional)**.

---

## 2) Intuition + step-by-step dry run

### Problem recap

* Grid of size `n × m` with cells `'L'` (land) and `'W'` (water).
* An island = maximal set of `'L'` cells connected in **8 directions**
  (N, NE, E, SE, S, SW, W, NW).
* Return the **count of islands**.

### Core idea

Scan every cell.
When you find an **unvisited** land cell, you’ve found a **new island** → run a flood-fill (DFS/BFS) to mark **all** connected land cells as visited so they aren’t counted again.

Time is linear in the grid size because each cell is visited at most once.

### Dry run (Example 1)

```
grid
[
 ['L','L','W','W','W'],
 ['W','L','W','W','L'],
 ['W','W','W','L','L'],
 ['W','W','W','W','W'],
 ['L','W','L','L','W']
]
```

We also keep a `visited` matrix (all False initially).

1. i=0,j=0 = 'L' and not visited → island += 1 (now 1).
   DFS/BFS from (0,0) marks its 8-directionally connected land:

   * (0,0) connects to (0,1) and (1,1) diagonally; mark all three.
     End of flood-fill #1.

2. Continue scanning… next unseen `'L'` at (1,4) → island += 1 (now 2).
   Flood-fill from (1,4) spreads to (2,3), (2,4) (8-dir). Mark them.
   End flood-fill #2.

3. Next unseen `'L'` at (4,0) → island += 1 (now 3).
   No neighbors (water around). End flood-fill #3.

4. Next unseen `'L'` at (4,2) → island += 1 (now 4).
   Connected to (4,3). Mark both. End flood-fill #4.

Finish scan → **4 islands**.

---

## 3) Python solutions (expected in interviews)

All solutions keep your signature:

```python
class Solution:
    def numIslands(self, grid):
        # code here
```

### A) Recursive DFS (clean & fastest to write)

```python
from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        Flood-fill with DFS in 8 directions.
        Time  : O(n*m)  — each cell visited at most once
        Space : O(n*m)  — recursion stack in worst case + visited/marking
        """
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])

        # normalize to characters; if input is 0/1 you can tweak the check below
        def is_land(i, j):
            return grid[i][j] == 'L' or grid[i][j] == 1

        # 8 directions (dr, dc)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        visited = [[False]*m for _ in range(n)]

        def dfs(r, c):
            # mark this cell O(1)
            visited[r][c] = True
            # explore 8 neighbors O(1) per neighbor
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and is_land(nr, nc):
                    dfs(nr, nc)

        islands = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and is_land(i, j):
                    islands += 1
                    dfs(i, j)      # flood-fill this island
        return islands
```

### B) Iterative BFS (no recursion limit worries)

```python
from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        Flood-fill with BFS in 8 directions (iterative).
        Time  : O(n*m)
        Space : O(n*m) — queue + visited
        """
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])

        def is_land(i, j):
            return grid[i][j] == 'L' or grid[i][j] == 1

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        visited = [[False]*m for _ in range(n)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and is_land(nr, nc):
                        visited[nr][nc] = True
                        q.append((nr, nc))

        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and is_land(i, j):
                    count += 1
                    bfs(i, j)
        return count
```

### C) Union-Find / DSU (good to mention; handy for many queries)

```python
class Solution:
    def numIslands(self, grid):
        """
        DSU: union all adjacent lands (8-dir), count distinct roots.
        Time  : O(n*m * α(n*m)) ~ O(n*m)
        Space : O(n*m)
        """
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])

        def is_land(i, j):
            return grid[i][j] == 'L' or grid[i][j] == 1

        # Map (r,c) -> id
        def id_of(r, c): return r*m + c

        parent = [i for i in range(n*m)]
        rank = [0]*(n*m)

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

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Union all adjacent lands
        for r in range(n):
            for c in range(m):
                if not is_land(r, c): 
                    continue
                a = id_of(r, c)
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and is_land(nr, nc):
                        union(a, id_of(nr, nc))

        # Count distinct roots among land cells
        roots = set()
        for r in range(n):
            for c in range(m):
                if is_land(r, c):
                    roots.add(find(id_of(r, c)))
        return len(roots)
```

> In most interviews, **DFS/BFS** is the expected approach.
> Mentioning **DSU** earns bonus points, especially if there are many “flip cell” or “add land” updates in follow-ups.

---

## 4) Common interview Q & A

**Q1. Why is the time complexity O(n·m)?**
Every cell is **visited at most once** (marked visited) and each edge (neighbor check) is considered a constant number of times (8 directions). Hence linear in the number of cells.

**Q2. What changes if connectivity is only 4-directional?**
Just use directions: `[(−1,0),(1,0),(0,−1),(0,1)]`. Everything else is identical.

**Q3. DFS vs BFS — which should I use?**
Both are fine.

* **DFS** is super quick to write.
* **BFS** avoids recursion depth issues in very large grids (Python recursion limit).

**Q4. How to handle inputs with `0/1` instead of `'W'/'L'`?**
Normalize the land check, e.g., `grid[i][j] == 1` (used in the helper `is_land` above).

**Q5. What if the grid is huge and there are many queries (e.g., toggling cells)?**
Consider **Disjoint Set Union (Union-Find)** to maintain connected components incrementally. For pure one-shot counting, DFS/BFS is simpler and fast.

**Q6. Any pitfalls?**

* Don’t forget **8 directions** here.
* Mark as visited **when enqueueing/recursing**, not after popping/returning, to avoid multiple enqueues.
* Always bounds-check neighbors.

---

---

awesome — here’s a complete, runnable script for **Number of Islands (8-directional)** with:

* clean DFS solution (primary) + optional BFS function for reference
* inline **time & space complexity** notes right where they matter
* demo runs on the two examples from the prompt + one custom case
* a small **timeit** benchmark that reports average seconds/run

---

## 5) Full program (with inline complexity + inputs/outputs + timing)

```python
"""
Number of Islands (8-directional)
---------------------------------
We count connected components of 'L' cells where connectivity is in 8 directions
(N, NE, E, SE, S, SW, W, NW). A simple flood-fill (DFS/BFS) does the job.

Notation:
  n = rows, m = cols

Complexities (DFS/BFS one-shot):
  • Scan + flood-fills:
        Time  : O(n * m)   (each cell visited at most once)
        Space : O(n * m)   (visited array + worst-case recursion stack or queue)
"""

from collections import deque
import timeit
from typing import List, Union


# ---------------------------- Core Solution ---------------------------- #
class Solution:
    def numIslands(self, grid: List[List[Union[str, int]]]) -> int:
        """
        DFS flood-fill in 8 directions.
        Time  : O(n*m)  — visit each cell at most once
        Space : O(n*m)  — visited + worst-case recursion stack
        """
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])

        # Helper to treat both 'L'/'W' and 1/0 inputs as valid.
        def is_land(i: int, j: int) -> bool:
            # O(1)
            return grid[i][j] == 'L' or grid[i][j] == 1

        # 8 directions — constant size set, O(1) per step
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # visited matrix — O(n*m) space
        visited = [[False] * m for _ in range(n)]

        def dfs(r: int, c: int) -> None:
            """
            Depth-first flood-fill.
            Each cell gets marked once → O(1) per cell over the whole run.
            """
            visited[r][c] = True
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and is_land(nr, nc):
                    dfs(nr, nc)

        islands = 0
        # Full grid scan → O(n*m)
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and is_land(i, j):
                    islands += 1
                    dfs(i, j)   # flood-fill this new island
        return islands


# ---------------------------- Optional BFS ----------------------------- #
def num_islands_bfs(grid: List[List[Union[str, int]]]) -> int:
    """
    Iterative BFS variant (avoids recursion limits).
    Time  : O(n*m)
    Space : O(n*m)
    """
    if not grid or not grid[0]:
        return 0
    n, m = len(grid), len(grid[0])

    def is_land(i, j):
        return grid[i][j] == 'L' or grid[i][j] == 1

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    visited = [[False] * m for _ in range(n)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and is_land(nr, nc):
                    visited[nr][nc] = True
                    q.append((nr, nc))

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and is_land(i, j):
                count += 1
                bfs(i, j)
    return count


# ---------------------------- Demo & Timing ---------------------------- #
def run_demo():
    sol = Solution()

    # Example 1 from the prompt
    grid1 = [
        ['L','L','W','W','W'],
        ['W','L','W','W','L'],
        ['W','W','W','L','L'],
        ['W','W','W','W','W'],
        ['L','W','L','L','W'],
    ]
    print("Example 1:")
    print("Grid:")
    for row in grid1: print(" ", row)
    print("Islands (DFS):", sol.numIslands(grid1))  # Expected: 4
    print()

    # Example 2 from the prompt
    grid2 = [
        ['W','L','L','L','W','W','W'],
        ['W','W','L','L','W','L','W'],
    ]
    print("Example 2:")
    print("Grid:")
    for row in grid2: print(" ", row)
    print("Islands (DFS):", sol.numIslands(grid2))  # Expected: 2
    print()

    # Custom quick case
    grid3 = [
        ['L','W','L'],
        ['W','L','W'],
        ['L','W','L'],
    ]
    print("Custom:")
    for row in grid3: print(" ", row)
    print("Islands (DFS):", sol.numIslands(grid3))  # Diagonals connect: should be 1 (all touch diagonally)
    print()

    # --------- Timing (timeit) ----------
    def task():
        # Medium random-like dense pattern
        g = [
            ['L' if (i*j + i + j) % 3 == 0 else 'W' for j in range(60)]
            for i in range(60)
        ]
        sol.numIslands(g)

    runs = 10
    avg = timeit.timeit(task, number=runs) / runs
    print(f"Average runtime over {runs} runs: {avg:.6f} seconds/run")
    print("(Asymptotically O(n*m); this measures the whole flood-fill end to end.)")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* Printed grids for the two given examples and a custom case.
* The island counts (4, 2, and 1 for the custom diagonal-heavy grid).
* A small average runtime report from `timeit`.

---

## 6) Real-World Use Cases (high-impact)

1. **Satellite imagery & GIS**
   Counting contiguous regions like **forests, lakes, urban blocks** where adjacency may be defined in 8 directions due to diagonal pixel contact.

2. **Medical imaging**
   Identifying connected components (e.g., lesions, tissues) in raster images; 8-connectivity is standard in many segmentation tasks.

3. **Computer vision / OCR**
   Counting and labeling **blobs** in binary images (characters, objects). 8-connectivity avoids missing diagonally-touching parts.

4. **Game maps & simulations**
   Determining number of **territories/biomes** or flood-fill based reachability in tile-based games.

5. **Network/Cluster analysis on grids**
   Modeling percolation or connectivity in **sensor grids** and **cellular automata**—8-neighborhood often better captures “adjacency” in square lattices.