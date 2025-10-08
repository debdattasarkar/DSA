# Flood Fill Algorithm

**Difficulty:** Medium
**Accuracy:** 41.11%
**Submissions:** 150K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

You are given a 2D grid **image[][]** of size **n * m**, where each **image[i][j]** represents the color of a pixel in the image.
Also provided a coordinate **(sr, sc)** representing the **starting pixel** (row and column) and a **newColor** value.

Your task is to perform a **flood fill** starting from the pixel **(sr, sc)**, changing its color to **newColor** and the color of all the connected pixels that have the same **original color**.

Two pixels are considered connected if they are adjacent **horizontally or vertically** (not diagonally) and have the same original color.

---

## Examples

### Example 1

**Input:**

```
image[][] = [[1, 1, 1, 0], 
             [0, 1, 1, 1], 
             [1, 0, 1, 1]], 
sr = 1, sc = 2, newColor = 2
```

**Output:**

```
[[2, 2, 2, 0], 
 [0, 2, 2, 2], 
 [1, 0, 2, 2]]
```

**Explanation:**
Starting from pixel (1, 2) with value 1, flood fill updates all connected pixels (up, down, left, right) with value 1 to 2, resulting in `[[2, 2, 2, 0], [0, 2, 2, 2], [1, 0, 2, 2]]`.

---

### Example 2

**Input:**

```
image[][] = [[1, 1, 1], 
             [1, 1, 0], 
             [1, 0, 1]], 
sr = 1, sc = 1, newColor = 2
```

**Output:**

```
[[2, 2, 2], 
 [2, 2, 0], 
 [2, 0, 1]]
```

**Explanation:**
From the center of the image (position (sr, sc) = (1, 1)), all pixels connected by a path of the same color as the starting pixel are colored with the new color. Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

---

### Example 3

**Input:**

```
image[][] = [[0, 1, 0], 
             [0, 1, 0]], 
sr = 0, sc = 1, newColor = 0
```

**Output:**

```
[[0, 0, 0], 
 [0, 0, 0]]
```

**Explanation:**
Starting from pixel (0, 1) with value 1, flood fill changes all 4-directionally connected pixels with value 1 to 0, resulting in `[[0, 0, 0], [0, 0, 0]]`.

---

## Constraints

* (1 \leq n \leq 500)
* (1 \leq m \leq 500)
* (0 \leq image[i][j] \leq 10)
* (0 \leq newColor \leq 10)
* (0 \leq sr \leq (n-1))
* (0 \leq sc \leq (m-1))

---

## Expected Complexities

* **Time Complexity:** (O(n * m))
* **Auxiliary Space:** (O(n * m))

---

## Company Tags

* Microsoft
* Google

---

## Topic Tags

* Recursion
* DFS
* Matrix
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* Flood Fill Algorithm Implement Fill Paint
* Flood Fill Algorithm

---

---

awesome — here’s an interview-ready pack for **Flood Fill**: clear intuition, a step-by-step dry run, and multiple Python solutions in your requested template (with inline complexity notes), plus common interview Q&A.

---

# 2) Intuition & Approach

We must recolor the **connected component** (4-directional) that contains the starting pixel `(sr, sc)`, but **only** those pixels whose color equals the **starting color**. This is a classic flood-fill:

* Let `old = image[sr][sc]`.
* If `old == newColor`, nothing to do (avoid infinite loops).
* Do **DFS/BFS** from `(sr, sc)` visiting only pixels with color `old`; recolor them to `newColor`.

Because each pixel is enqueued/visited at most once and we only check 4 neighbors, the runtime is **O(n·m)** and space is **O(n·m)** (recursion stack / queue / visited at worst).

---

## Step-by-Step Dry Run (Example 1)

```
image =
[ [1, 1, 1, 0],
  [0, 1, 1, 1],
  [1, 0, 1, 1] ]
sr = 1, sc = 2, newColor = 2
old = image[1][2] = 1
```

Start at `(1,2)`:

1. Visit `(1,2)` (color 1 == old) → set to 2.
   Neighbors with color 1: `(0,2)`, `(1,1)`, `(1,3)`, `(2,2)` → push.

2. Pop `(0,2)` → set to 2. Neighbors with color 1: `(0,1)` → push.

3. Pop `(1,1)` → set to 2. Neighbors with color 1: `(0,1)` (already in queue), `(1,0)` is 0 (skip), `(1,2)` now 2, `(2,1)` is 0.

4. Pop `(1,3)` → set to 2. Neighbor with color 1: `(0,3)` is 0; `(1,2)` is 2; `(2,3)` is 1 → push.

5. Pop `(2,2)` → set to 2. Neighbor with color 1: `(2,3)` (already queued).

6. Pop `(0,1)` → set to 2. Neighbor with color 1: `(0,0)` → push.

7. Pop `(2,3)` → set to 2.

8. Pop `(0,0)` → set to 2.

Finished: all 1’s connected to `(1,2)` become 2; others unchanged.

---

# 3) Python solutions (multiple ways, interview-ready)

## A) DFS (recursive) — most common/concise

```python
# User function Template for python3

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        DFS over the 4-connected component starting at (sr, sc).
        Time:  O(n * m)   -- each pixel visited at most once
        Space: O(n * m)   -- recursion stack in worst case (snakelike region)
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:               # Important guard to avoid infinite recursion
            return image

        def dfs(r, c):
            # boundary and color check: O(1)
            if r < 0 or r >= n or c < 0 or c >= m or image[r][c] != old:
                return
            image[r][c] = newColor        # paint
            # explore 4 neighbors: O(1) each
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
```

---

## B) BFS (queue) — robust to deep recursion

```python
from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        BFS (iterative) to avoid recursion depth issues.
        Time:  O(n * m)
        Space: O(n * m)   -- queue in worst case
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:
            return image

        q = deque([(sr, sc)])
        image[sr][sc] = newColor
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # visit only pixels with original color old
                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == old:
                    image[nr][nc] = newColor
                    q.append((nr, nc))

        return image
```

---

## C) Iterative DFS (explicit stack) — same complexity, no recursion

```python
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        Iterative DFS using a stack.
        Time:  O(n * m)
        Space: O(n * m)
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:
            return image

        stack = [(sr, sc)]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        while stack:
            r, c = stack.pop()
            if 0 <= r < n and 0 <= c < m and image[r][c] == old:
                image[r][c] = newColor
                # push neighbors with old color
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))
        return image
```

---

## D) (Educational) “Brute” with visited set (avoids recoloring checks)

```python
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        DFS with a visited set (educational; same asymptotics, tiny overhead).
        Time:  O(n * m)  | Space: O(n * m)
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:
            return image

        visited = set()
        def dfs(r, c):
            if (r, c) in visited: return
            if r < 0 or r >= n or c < 0 or c >= m: return
            if image[r][c] != old: return
            visited.add((r, c))
            image[r][c] = newColor
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)

        dfs(sr, sc)
        return image
```

> For interviews, **A or B** is typically expected; mention the guard `if old == newColor: return image` explicitly.

---

# 4) Interview Q&A (high-yield)

**Q1. Why check `old == newColor` first?**
If we recolor pixels from `old` to the **same** color, the “unvisited→visit if color==old” condition is always true and we’d loop forever. Early return avoids that.

**Q2. Time & space complexity?**
Each pixel is pushed/visited at most once; 4 constant-degree neighbors checked → **O(n·m)** time. Space is **O(n·m)** for recursion stack / queue / stack in worst case.

**Q3. DFS vs BFS — which to pick?**
Both are fine. DFS is concise; BFS avoids recursion depth issues (Python recursion limit) and is often preferred for robustness.

**Q4. Do diagonals count?**
No; only **4-directional** connectivity (up, down, left, right). If diagonals were included, just extend the neighbor list.

**Q5. How would you extend this to multiple starting seeds?**
Initialize the queue/stack with **all seeds** (multi-source BFS/DFS) and the same `old` color per seed, or handle per-seed colors if they differ.

**Q6. How to restrict fill to a boundary color?**
Classic “paint bucket with boundary”: change the eligibility test from `image[r][c] == old` to `image[r][c] != boundary_color` while still avoiding revisits.

**Q7. How to return the filled area size too?**
Maintain a counter; increment each time you recolor a pixel.

**Q8. What edge cases do you test?**

* Minimal grids (1×1), already newColor, entire image same color, starting on a unique color island, serpentine paths to stress recursion depth.

---

---

you got it — here’s a **runnable, interview-style full program** for **Flood Fill** with:

* your requested class/method signature,
* detailed inline **time/space complexity** notes at each step,
* a small **driver** that prints **inputs & outputs**,
* and **timeit** micro-benchmarks for the full call.

I’ve also added a short list of **real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Flood Fill (4-directional)

Task:
  Recolor the connected component (up, down, left, right) that contains (sr, sc)
  from its original color to newColor.

Key points:
  - Let old = image[sr][sc]. If old == newColor => nothing to do (avoid infinite loops).
  - Use DFS or BFS to visit only pixels with color == old, recolor to newColor.

Global complexities for an n x m image:
  Time:  O(n*m)   -- each pixel visited at most once; 4 neighbors per pixel (constant)
  Space: O(n*m)   -- recursion stack or queue in the worst case; no extra grids needed
"""

from collections import deque
import timeit
from typing import List


# --------------------------- User Function (primary: BFS) --------------------------- #
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Multi-Source? No, single source (sr, sc). We do a normal BFS from (sr, sc).

        Steps:
          1) Read old = image[sr][sc]; if old == newColor, return image.
             - Time: O(1), Space: O(1)
          2) Initialize queue with (sr, sc); recolor it to newColor.
             - Time: O(1), Space: O(1) extra (queue holds coordinates)
          3) Standard BFS:
             - Pop cell; for each of 4 neighbors, if inside bounds and color==old,
               recolor and push into queue.
             - Each cell processed once: overall Time O(n*m), Space O(n*m) worst case.

        Returns:
          The image after flood fill.
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:  # Guard to avoid infinite processing
            return image

        q = deque([(sr, sc)])       # queue can grow to O(n*m) in worst case
        image[sr][sc] = newColor    # in-place recolor; serves as visited mark
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]  # constant neighbors

        while q:  # Each node enqueued/dequeued once -> total O(n*m)
            r, c = q.popleft()  # O(1)
            # Explore neighbors (constant 4 checks) -> O(1) per cell
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                # Boundary+color checks are O(1)
                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == old:
                    image[nr][nc] = newColor   # recolor/mark visited
                    q.append((nr, nc))         # O(1)
        return image


# --------------------------- Optional Parity (recursive DFS) --------------------------- #
class SolutionDFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Recursive DFS variant; same asymptotics.
        Time:  O(n*m)
        Space: O(n*m) recursion depth in worst case (snake-like region)
        """
        n, m = len(image), len(image[0])
        old = image[sr][sc]
        if old == newColor:
            return image

        def dfs(r: int, c: int):
            if r < 0 or r >= n or c < 0 or c >= m:  # O(1)
                return
            if image[r][c] != old:  # O(1)
                return
            image[r][c] = newColor  # recolor
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)

        dfs(sr, sc)
        return image


# --------------------------- Tiny benchmark helper (timeit) --------------------------- #
def bench(func, *args, number=10000):
    """
    Measure average seconds per run for func(*args) over 'number' iterations.
    For tiny inputs, Python overhead dominates; use for relative comparisons only.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# --------------------------- Main: inputs, outputs, timings --------------------------- #
if __name__ == "__main__":
    tests = [
        # (image, sr, sc, newColor, note)
        (
            [[1, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 0, 1, 1]],
            1, 2, 2,
            "Example 1: recolor connected 1's from (1,2) to 2"
        ),
        (
            [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]],
            1, 1, 2,
            "Example 2: center region to 2; bottom-right remains 1 (not 4-connected)"
        ),
        (
            [[0, 1, 0],
             [0, 1, 0]],
            0, 1, 0,
            "Example 3: recolor 1's to 0 from (0,1)"
        ),
        (
            [[3, 3, 3, 3],
             [3, 2, 2, 3],
             [3, 2, 2, 3],
             [3, 3, 3, 3]],
            1, 1, 5,
            "Square block of 2's becomes 5's"
        ),
    ]

    print("=== Flood Fill — BFS primary, DFS parity ===\n")
    bfs_solver = Solution()
    dfs_solver = SolutionDFS()

    for img, sr, sc, color, note in tests:
        img_bfs_in = [row[:] for row in img]  # copies to keep prints clean
        img_dfs_in = [row[:] for row in img]
        out_bfs = bfs_solver.floodFill(img_bfs_in, sr, sc, color)
        out_dfs = dfs_solver.floodFill(img_dfs_in, sr, sc, color)

        print(note)
        print("Input image:")
        for row in img: print(row)
        print(f"Start=({sr},{sc}), newColor={color}")
        print("BFS output:")
        for row in out_bfs: print(row)
        print("DFS output:")
        for row in out_dfs: print(row)
        print(f"Both methods agree? {out_bfs == out_dfs}\n")

    # ---------------- Timings (average seconds per run) ----------------
    print("=== Timings (average seconds per run) ===")
    small_img = [[1,1,1,0],[0,1,1,1],[1,0,1,1]]
    medium_img = [[1]*40 for _ in range(40)]  # big connected component
    runs_small = 20000
    runs_medium = 1000

    t_bfs_small = bench(Solution().floodFill, [row[:] for row in small_img], 1, 2, 2, number=runs_small)
    t_dfs_small = bench(SolutionDFS().floodFill, [row[:] for row in small_img], 1, 2, 2, number=runs_small)
    print(f"Small (3x4/3x4)  runs={runs_small}: BFS {t_bfs_small:.8e}s | DFS {t_dfs_small:.8e}s")

    t_bfs_med = bench(Solution().floodFill, [row[:] for row in medium_img], 20, 20, 9, number=runs_medium)
    t_dfs_med = bench(SolutionDFS().floodFill, [row[:] for row in medium_img], 20, 20, 9, number=runs_medium)
    print(f"Medium (40x40)   runs={runs_medium}: BFS {t_bfs_med:.8e}s | DFS {t_dfs_med:.8e}s")

    print("\nNote: timings vary by machine and Python version.")
```

---

## 6) Real-World Use Cases (the important ones)

1. **Paint Bucket Tool (Image Editing)**
   Filling a contiguous region of the same color with a new paint color (exactly this algorithm).

2. **Segmentation & Mask Propagation**
   Growing a region from a seed in medical or satellite imagery where connectivity is 4- or 8-directional.

3. **Game Mechanics / Path Regions**
   Detecting and transforming connected tiles/regions (e.g., “spread” effects, territory marking, connected gem clusters).

4. **Topology/CAD Clean-up**
   Expanding selections across contiguous faces/pixels to apply a material or property consistently.