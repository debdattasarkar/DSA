# Unit Area of Largest Region of 1's

**Difficulty:** Medium
**Accuracy:** 50.83%
**Submissions:** 73K+
**Points:** 4
**Average Time:** 20m

---

You are given a grid of dimension **n × m** containing `0`s and `1`s. Find the **unit area of the largest region of 1s**.
A *region of 1s* is a group of `1`s connected **8-directionally** (horizontally, vertically, and diagonally).

---

## Examples

### Example 1

**Input:**
`grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}`

**Output:**
`5`

**Explanation:**
The grid is:

```
1 1 1 0
0 0 1 0
0 0 0 1
```

The largest region of `1`s (highlighted in orange in the problem image) has an area of **5**.

---

### Example 2

**Input:**
`grid = {{0,1}}`

**Output:**
`1`

**Explanation:**
The grid is:

```
0 1
```

The largest region of `1`s (highlighted in orange in the problem image) has an area of **1**.

---

## Your Task

You don’t need to read input or print anything. Complete the function **`findMaxArea()`** which takes the grid as input and **returns the area of the largest region of 1’s**.

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## Constraints

* `1 ≤ n, m ≤ 500`

---

## Company Tags

Flipkart, Amazon, Microsoft, Samsung, Ola Cabs, Google, Salesforce

---

## Topic Tags

DFS, Graph, BFS, Data Structures, Algorithms

---

## Related Interview Experiences

* Microsoft Interview Experience Set 159 Campus

---

## Related Articles

* [Find Length Largest Region Boolean Matrix](https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/)

---

---

Here’s a compact, interview-ready pack for **Unit Area of Largest Region of 1s (8-directional)**.

---

## 2) Explanation + Step-by-Step Dry Run

### Problem in one line

Given an `n × m` grid of 0/1, find the **largest connected component** of 1s when connectivity is **8-directional** (N, NE, E, SE, S, SW, W, NW). Return its **area (number of cells)**.

### Core idea

Do a **single pass flood-fill** (DFS or BFS).
Maintain a `visited` matrix to avoid recounting cells.
For each unvisited `1`, expand to all 8 neighbors, compute the component’s area, and keep the maximum.

### Dry run (Example 1)

```
grid =
1 1 1 0
0 0 1 0
0 0 0 1
```

* `vis` all False initially.
* (0,0)=1 & unvisited → start flood-fill:

  * Visit (0,0): area=1; its 8-neighbors include (0,1),(1,1),(1,0),(-1,*),…
    Only valid 1s: (0,1). Push/visit.
  * Visit (0,1): area=2; valid 1 neighbors: (0,2), (1,2), (−,− filtered).
  * Visit (0,2): area=3; valid 1 neighbors: (1,3 out), (1,2=1), (−,− filtered).
  * Visit (1,2): area=4; valid 1 neighbors: (0,2 visited), (0,3=0), (2,3=1), (2,1=0), …
  * Visit (2,3): area=5; neighbors are all 0/out/visited.
  * Region ended → max_area = max(0, 5) = **5**.
* Remaining 1s are already visited; answer **5**.

---

## 3) Optimized Codes for Python

### A) Iterative DFS (stack) — preferred in Python to avoid recursion limits

```python
class Solution:

    # Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        # 8 directions: N, NE, E, SE, S, SW, W, NW
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]

        def inside(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs_area(sr, sc):
            """Flood-fill from (sr, sc) using a stack.
            Time per component: O(size_of_component)
            Space: O(size_of_component) for stack + visited (global O(n*m)).
            """
            stack = [(sr, sc)]
            visited[sr][sc] = True
            area = 0
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
            return area

        max_area = 0
        # Overall Time: O(n*m) (each cell visited at most once)
        # Overall Space: O(n*m) for visited; stack worst-case O(n*m).
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs_area(i, j))
        return max_area
```

### B) BFS (queue) — equally acceptable

```python
from collections import deque

class SolutionBFS:
    def findMaxArea(self, grid):
        n, m = len(grid), len(grid[0])
        vis = [[False]*m for _ in range(n)]
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]

        def inside(r, c): return 0 <= r < n and 0 <= c < m

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            vis[sr][sc] = True
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc) and not vis[nr][nc] and grid[nr][nc] == 1:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return area

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    ans = max(ans, bfs(i, j))
        return ans
```

### (What is the “brute force”?)

A true brute force would, for **every** cell `1`, run a fresh flood-fill **without** a global `visited` (or by copying it each time). That can be **Θ((n·m)²)** in the worst case and is not practical. The optimized versions above do **one** pass with a global `visited` → **O(n·m)**.

**Complexities (both A & B):**

* **Time:** `O(n * m)` — each cell enqueued/stacked at most once.
* **Space:** `O(n * m)` — `visited` plus the worst-case frontier.

---

## 4) Interview Q&A

**Q1. What’s the difference between this and the classic “number of islands”?**
**A.** Here we return the **largest area**; also connectivity is **8-directional**, while “number of islands” is often **4-directional**. Adjust the `dirs` accordingly.

**Q2. Why do we need a `visited` matrix?**
**A.** To avoid revisiting cells and recounting components. Without it, you can loop forever or inflate counts.

**Q3. DFS or BFS — which to choose?**
**A.** Both work with the same asymptotics. In Python, **iterative DFS or BFS** avoids recursion limit issues for large components.

**Q4. Can Union-Find solve it?**
**A.** Yes. Union all adjacent 1s (8 directions) and track component sizes in parent roots. It’s also `~O(n*m α(n*m))` but with more code; DFS/BFS is simpler.

**Q5. Edge cases to consider?**

* All zeros → answer `0`.
* Single cell `1` → answer `1`.
* Non-rectangular considerations (not here — grid is rectangular).
* Large contiguous blob (stress queue/stack size).

**Q6. How would you switch between 4- and 8-directional connectivity?**
**A.** Change the `dirs` array to either 4 directions `[(1,0),(-1,0),(0,1),(0,-1)]` or the 8 used above.

---

---

Below is a **complete, runnable Python program** for “Unit Area of Largest Region of 1’s” with rich inline comments explaining **time and space** at each step, plus a tiny harness that uses `timeit` to measure the run time on sample inputs.

---

### Full Program (with timing + examples)

```python
from collections import deque
import timeit

class Solution:
    """
    We solve with a single pass flood-fill (BFS).
    Global complexity over the whole grid:
      - Time:  O(n * m)  — each cell is visited at most once
      - Space: O(n * m)  — visited matrix + BFS queue worst-case
    """

    # Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        n, m = len(grid), len(grid[0])

        # visited[r][c] marks whether cell (r,c) has been enqueued/dequeued.
        # Space: O(n*m)
        visited = [[False] * m for _ in range(n)]

        # 8-directional movement (N, NE, E, SE, S, SW, W, NW)
        # Constant size: O(1)
        DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]

        def inside(r, c):
            # O(1) boundary check
            return 0 <= r < n and 0 <= c < m

        def bfs_area(sr, sc):
            """
            Flood-fills the component that contains (sr, sc) using BFS.
            Per component cost is proportional to its size:
              - Time:  O(size_of_component)
              - Space: O(size_of_component) for queue
            """
            q = deque([(sr, sc)])
            visited[sr][sc] = True  # O(1)
            area = 0                # O(1)

            while q:                # Each cell enters/leaves once → across whole grid O(n*m)
                r, c = q.popleft()
                area += 1
                # Iterate 8 neighbors: constant work per cell: O(1) * 8
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            return area

        max_area = 0  # O(1)

        # Scan entire grid once: O(n*m)
        for i in range(n):
            for j in range(m):
                # O(1) checks; each cell’s BFS triggered at most once
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, bfs_area(i, j))

        return max_area


# -----------------------------
# Demo + time measurement
# -----------------------------
def run_demo():
    sol = Solution()

    # Example 1 (from prompt)
    grid1 = [
        [1, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    # Expected largest region area = 5
    ans1 = sol.findMaxArea(grid1)
    print("Grid 1:")
    for row in grid1:
        print(row)
    print("Largest 1-region area:", ans1)   # -> 5
    print()

    # Example 2 (from prompt)
    grid2 = [[0, 1]]  # Expected = 1
    ans2 = sol.findMaxArea(grid2)
    print("Grid 2:")
    for row in grid2:
        print(row)
    print("Largest 1-region area:", ans2)   # -> 1
    print()

    # Another custom example
    grid3 = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
    ]
    # Two big blobs; left blob area should be 6 (8-directional), right top-lone is 1, bottom-right is 1
    ans3 = sol.findMaxArea(grid3)
    print("Grid 3:")
    for row in grid3:
        print(row)
    print("Largest 1-region area:", ans3)   # -> 6
    print()


def timed_run():
    # Wrap demo in a function for timeit
    run_demo()

if __name__ == "__main__":
    # Print outputs once
    timed_run()

    # Measure time for a single repeated run of the demo
    repeats = 5
    total_time = timeit.timeit("timed_run()", setup="from __main__ import timed_run", number=repeats)
    print(f"\nTime for {repeats} run(s): {total_time:.6f} seconds")
    print(f"Average per run: {total_time/repeats:.6f} seconds")
```

**What the program prints (example):**

```
Grid 1:
[1, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Largest 1-region area: 5

Grid 2:
[0, 1]
Largest 1-region area: 1

Grid 3:
[1, 0, 0, 1]
[1, 1, 0, 0]
[0, 1, 1, 0]
[0, 0, 0, 1]
Largest 1-region area: 6

Time for 5 run(s): 0.00xxxx seconds
Average per run: 0.00xxxx seconds
```

(Your timing numbers will vary by machine.)

---

## 6) Real-World Use Cases (a few high-impact ones)

1. **Image Processing / Computer Vision**
   Detect the largest connected bright blob (e.g., tumor regions in scans, largest object in binary segmentation masks) where diagonal adjacency often matters.

2. **Geospatial / Satellite Analytics**
   Measure the largest contiguous land, forest burn scar, or flood extent in raster tiles—8-connectivity better mirrors real-world contiguity.

3. **Network Failure Analysis**
   In a binary matrix representing operational nodes, find the largest functioning cluster to assess service availability regions.

4. **Game/Map Regions**
   Identify the largest contiguous territory or resource patch on a tile-based map, considering diagonal adjacency for movement rules.
