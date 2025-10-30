
---

# 🧩 Replace O's with X's

**Difficulty:** Medium
**Accuracy:** 34.0%
**Submissions:** 129K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

You are given a **grid[][]** of size **n × m**, where every element is either `'O'` or `'X'`.
You have to **replace all 'O' (or groups of 'O') with 'X'** that are **completely surrounded by 'X'** on all sides.

A `'O'` (or a set of `'O'`) is considered to be **surrounded by 'X'** if there are `'X'` cells just **below**, **above**, **left**, and **right** of it (no connection to border).

---

## 🧠 Concept

* Think of all `'O'` cells that are **connected to the border** — they **cannot** be replaced (since they are not surrounded by `'X'` on all sides).
* Any other `'O'` (not connected to border `'O'`) is **truly surrounded** → replace it with `'X'`.

---

## 🧩 Examples

### Example 1

**Input:**

```python
grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]
```

**Output:**

```python
[
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]
```

**Explanation:**
We only changed those `'O'` that were **completely surrounded by `'X'`**.
The `'O'`s on the bottom border remain unchanged.

---

### Example 2

**Input:**

```python
grid = [
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]
```

**Output:**

```python
[
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]
```

**Explanation:**
No `'O'` is fully surrounded by `'X'`.
All `'O'`s are connected to the border (directly or indirectly), so none are changed.

---

### Example 3

**Input:**

```python
grid = [
    ['X', 'X', 'X'],
    ['X', 'O', 'X'],
    ['X', 'X', 'X']
]
```

**Output:**

```python
[
    ['X', 'X', 'X'],
    ['X', 'X', 'X'],
    ['X', 'X', 'X']
]
```

**Explanation:**
There’s only one `'O'` in the middle, completely surrounded by `'X'` → it gets replaced.

---

## ⚙️ Constraints

```
1 ≤ grid.size() ≤ 100
1 ≤ grid[0].size() ≤ 100
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n * m)   |
| **Auxiliary Space** | O(n * m)   |

---

## 🏢 Company Tags

`Google`

---

## 🧵 Topic Tags

`Recursion` • `Matrix` • `Graph` • `Data Structures` • `Algorithms` • `BFS`

---

## 🔗 Related Articles

* [Given Matrix O X Replace O X Surrounded X](https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/)

---

---

Awesome—this is the classic **“Surrounded Regions”** pattern. I’ll give you:

1. a clear explanation with a tiny step-by-step dry run,
2. interview-ready Python in your exact signature: **DFS** (most common), **BFS** alternative, plus a **simple brute** to illustrate why we don’t use it,
3. a 60-second recall mnemonic + high-yield Q&A.

---

## 2) Text explanation + dry run

### Problem in one line

Replace every `'O'` that is **not connected to the border** (via up/down/left/right) with `'X'`.

### Key idea (optimal, expected in interviews)

* Any `'O'` touching the **border** (directly or through a chain of `'O'`s) is **safe** and must **stay `'O'`**.
* All other `'O'`s are **trapped** (surrounded) and must be turned to `'X'`.

So we:

1. **Mark all border-connected 'O's** (via DFS/BFS) as **SAFE** (e.g., temporarily mark `'S'`).
2. **Flip remaining 'O' → 'X'** (they’re surrounded).
3. **Restore 'S' → 'O'** (keep safe zones).

This touches each cell **O(n·m)** once.

### Tiny dry run

Input:

```
X X X X
X O O X
X X O X
X O X X
```

Rows=4, Cols=4.

1. Start from borders and flood-fill (4-neighbors) only on `'O'`:

   * Border O at (3,1) → mark as `S`. Its up neighbor (2,1) is `X` so stop.
   * No other border O.

After marking SAFE:

```
X X X X
X O O X
X X O X
X S X X
```

2. Flip remaining unmarked `'O'` → `'X'`:

```
X X X X
X X X X
X X X X
X S X X
```

3. Restore `'S'` → `'O'`:

```
X X X X
X X X X
X X X X
X O X X
```

Only the region touching the border remained `'O'`. Others got surrounded and flipped.

---

## 3) Python solutions (brute → optimal), with inline comments

Signature you asked for:

```python
class Solution:
    def fill(self, grid):
        # Code here
```

### A) DFS (border-marking), **expected** solution — O(n·m) time, O(n·m) space (recursion/stack)

```python
class Solution:
    def fill(self, grid):
        """
        Mark border-connected 'O' as SAFE via DFS, flip the rest.
        Time  : O(n*m)  -- each cell visited at most once
        Space : O(n*m)  -- recursion stack worst-case + grid in-place
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])

        # 4-directional moves
        DIRS = ((1,0), (-1,0), (0,1), (0,-1))

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            # Mark this 'O' as SAFE ('S') to avoid flipping later
            grid[r][c] = 'S'
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == 'O':
                    dfs(nr, nc)

        # 1) Seed DFS from all border 'O's
        for r in range(rows):
            if grid[r][0] == 'O': dfs(r, 0)
            if grid[r][cols-1] == 'O': dfs(r, cols-1)
        for c in range(cols):
            if grid[0][c] == 'O': dfs(0, c)
            if grid[rows-1][c] == 'O': dfs(rows-1, c)

        # 2) Flip interior 'O' -> 'X'
        # 3) Restore SAFE 'S' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'   # surrounded
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O'   # safe

        return grid
```

### B) BFS (queue) variant — same complexity, iterative (useful if recursion depth is a concern)

```python
from collections import deque

class SolutionBFS:
    def fill(self, grid):
        """
        Iterative BFS from border 'O's to mark SAFE cells.
        Time  : O(n*m)
        Space : O(n*m) for the queue in worst-case
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])
        q = deque()

        def push_if_border_O(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 'O':
                grid[r][c] = 'S'     # mark as SAFE upon enqueue (avoid repeats)
                q.append((r, c))

        # 1) Enqueue all border 'O's and mark as SAFE
        for r in range(rows):
            push_if_border_O(r, 0)
            push_if_border_O(r, cols - 1)
        for c in range(cols):
            push_if_border_O(0, c)
            push_if_border_O(rows - 1, c)

        # 2) BFS flood to mark all connected 'O's as SAFE
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                push_if_border_O(nr, nc)

        # 3) Flip interior 'O' -> 'X', restore 'S' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O': grid[r][c] = 'X'
                elif grid[r][c] == 'S': grid[r][c] = 'O'

        return grid
```

### C) Brute (educational): flood every `'O'` and check if region touches border — O(n·m) but slower constants

```python
from collections import deque

class SolutionBrute:
    def fill(self, grid):
        """
        For each unvisited 'O', BFS its region; if region touches border, keep it,
        else flip whole region to 'X'.
        Time  : O(n*m) overall (each cell enters exactly one region BFS)
        Space : O(n*m) for visited/queue
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        def on_border(r, c):
            return r == 0 or r == rows-1 or c == 0 or c == cols-1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O' and not visited[r][c]:
                    q = deque([(r, c)])
                    visited[r][c] = True
                    region = [(r, c)]
                    touches_border = on_border(r, c)

                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 'O':
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                region.append((nx, ny))
                                if on_border(nx, ny):
                                    touches_border = True

                    # Flip region only if it does NOT touch border
                    if not touches_border:
                        for x, y in region:
                            grid[x][y] = 'X'

        return grid
```

> In interviews, prefer **DFS or BFS border-marking** (A or B). The brute is fine as a warmup explanation.

---

## 4) 60-second recall + interviewer Q&A

### Mnemonic (say it once before coding)

**“Border → Mark Safe → Flip Others → Restore.”**
Or shorter: **“B–M–F–R.”**

* **Border:** start from every border `'O'`.
* **Mark Safe:** flood-fill to mark border-connected region (use `'S'`).
* **Flip Others:** any remaining `'O'` is surrounded → flip to `'X'`.
* **Restore:** `'S'` → `'O'`.

### Likely Q&A

**Q1. Why start from borders?**
Surrounded regions are exactly those **not** connected to the border. Border flood-fill labels all “escape to border” areas as safe.

**Q2. Time/space complexity?**
Each cell is processed a constant number of times → **O(n·m)** time.
Extra memory for recursion/queue/visited → **O(n·m)** worst-case.

**Q3. DFS vs BFS?**
Either works. DFS is concise; BFS avoids deep recursion (stack overflow) on very large grids.

**Q4. Why mark as `'S'` and not a boolean visited only?**
You can use either. Using `'S'` lets us **avoid another array** and makes the final restore step straightforward.

**Q5. Diagonals allowed?**
No—only 4-direction connectivity (up/down/left/right) counts, per problem statement.

**Q6. Can we do it truly in-place?**
Yes—by marking with `'S'` (or a sentinel) and restoring later; no separate visited array is required (DFS version).

---

---

Great—wrapping this up with (5) crisp real-world uses and (6) a **complete, runnable program** (DFS + BFS), with clear inline complexity notes and timings.

---

## 5) Real-World Use Cases (interview-friendly)

1. **Capture regions in image segmentation**
   Pixels = grid cells. “Foreground” (`'O'`) touching the border is background leak; only fully enclosed blobs should be filled—exactly this problem.

2. **Maze/room sealing in games**
   Flood from outer boundary to mark rooms reachable from outside; any `'O'` not touched is a sealed chamber → fill with walls.

3. **Map water fill (lakes vs ocean)**
   On an elevation grid reduced to `'O'` water and `'X'` land: border-connected water is **ocean**; enclosed `'O'` pools are **lakes** → convert to land.

4. **UI/Canvas paint-bucket with boundaries**
   When user “fills” with a color, don’t cross the global frame edges: mark outside-connectivity; fill only bounded areas.

5. **Security zoning**
   Floor plan cells: mark zones accessible from exits (borders). Enclosed accessible `'O'` regions with no border path are restricted and can be “sealed”.

---

## 6) Full Program (DFS + BFS, outputs + timings)

```python
#!/usr/bin/env python3
"""
Replace O's with X's (Surrounded Regions)
-----------------------------------------
Approaches:
  A) DFS border-marking (class Solution)        -> O(n*m) time, O(n*m) space (recursion)
  B) BFS border-marking (class SolutionBFS)     -> O(n*m) time, O(n*m) space (queue)

The algorithmic pattern:
  1) From ALL border 'O's, flood-fill and mark SAFE cells as 'S'.
  2) Flip remaining 'O' -> 'X' (trapped).
  3) Restore 'S' -> 'O' (keep safe).

We include:
  - Pretty printing of grids
  - Example inputs from the prompt
  - perf_counter + timeit timings
"""

from collections import deque
from time import perf_counter
import timeit
from copy import deepcopy
from typing import List


# ======================================================================
# A) DFS (most common in interviews)
# ======================================================================
class Solution:
    def fill(self, grid: List[List[str]]) -> List[List[str]]:
        """
        DFS from border 'O's to mark SAFE region ('S'), then flip & restore.

        Complexity by step:
          - Build constants/dir helpers: O(1)
          - Step 1 (seed + DFS flood): visits each cell at most once -> O(n*m)
            * Space: recursion stack worst-case O(n*m)
          - Step 2/3 (final sweep to flip/restore): O(n*m)
          => Overall: Time O(n*m), Aux Space O(n*m)
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            grid[r][c] = 'S'  # mark as SAFE immediately (O(1))
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == 'O':
                    dfs(nr, nc)  # recurse; stack depth bounded by region size

        # Step 1: run DFS from *all* border 'O's (O(perimeter) calls; total work O(n*m))
        for r in range(rows):
            if grid[r][0] == 'O': dfs(r, 0)
            if grid[r][cols - 1] == 'O': dfs(r, cols - 1)
        for c in range(cols):
            if grid[0][c] == 'O': dfs(0, c)
            if grid[rows - 1][c] == 'O': dfs(rows - 1, c)

        # Step 2 + 3: single sweep to flip surrounded and restore safe (O(n*m))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'  # surrounded region
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O'  # restore border-connected

        return grid


# ======================================================================
# B) BFS (iterative; avoid recursion limits)
# ======================================================================
class SolutionBFS:
    def fill(self, grid: List[List[str]]) -> List[List[str]]:
        """
        BFS from border 'O's, marking as 'S' upon enqueue to avoid revisits.

        Complexity:
          - Enqueue borders: O(n+m)
          - BFS processes each cell at most once: O(n*m) time, O(n*m) space (queue)
          - Final sweep flip/restore: O(n*m)
          => Overall: Time O(n*m), Aux Space O(n*m)
        """
        if not grid or not grid[0]:
            return grid

        rows, cols = len(grid), len(grid[0])
        q = deque()

        def push_if_O(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 'O':
                grid[r][c] = 'S'  # mark SAFE as soon as we see it
                q.append((r, c))

        # Seed all border 'O's (O(n+m))
        for r in range(rows):
            push_if_O(r, 0)
            push_if_O(r, cols - 1)
        for c in range(cols):
            push_if_O(0, c)
            push_if_O(rows - 1, c)

        # BFS flood (O(n*m))
        while q:
            r, c = q.popleft()
            push_if_O(r + 1, c)
            push_if_O(r - 1, c)
            push_if_O(r, c + 1)
            push_if_O(r, c - 1)

        # Final sweep (O(n*m))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O'
        return grid


# ======================================================================
# Utilities
# ======================================================================
def print_grid(g: List[List[str]]) -> None:
    for row in g:
        print(" ".join(row))


def run_case(name: str, grid: List[List[str]]):
    print(f"\n-- {name} --")
    print("Input:")
    print_grid(grid)

    # Make independent copies
    grid_dfs = deepcopy(grid)
    grid_bfs = deepcopy(grid)

    # Single-run timings (perf_counter)
    t0 = perf_counter()
    out_dfs = Solution().fill(grid_dfs)
    t1 = perf_counter()

    t2 = perf_counter()
    out_bfs = SolutionBFS().fill(grid_bfs)
    t3 = perf_counter()

    print("\nOutput (DFS):")
    print_grid(out_dfs)
    print("Output (BFS):")
    print_grid(out_bfs)
    print(f"\nSingle-run time: DFS { (t1 - t0)*1e6:.2f} µs | BFS { (t3 - t2)*1e6:.2f} µs")

    # Average timings with timeit (more stable)
    def call_dfs():
        Solution().fill(deepcopy(grid))

    def call_bfs():
        SolutionBFS().fill(deepcopy(grid))

    reps = 200
    avg_dfs = timeit.timeit(call_dfs, number=reps) / reps
    avg_bfs = timeit.timeit(call_bfs, number=reps) / reps
    print(f"Average over {reps} runs: DFS {avg_dfs*1e6:.2f} µs/run | BFS {avg_bfs*1e6:.2f} µs/run")


# ======================================================================
# Main: sample inputs from the prompt
# ======================================================================
def main():
    ex1 = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O']
    ]
    ex2 = [
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O']
    ]
    ex3 = [
        ['X', 'X', 'X'],
        ['X', 'O', 'X'],
        ['X', 'X', 'X']
    ]

    run_case("Example 1", ex1)
    run_case("Example 2", ex2)
    run_case("Example 3", ex3)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==== TOTAL PROGRAM RUNTIME: {(end - start):.6f} s ====")
```

**What you’ll see when you run it**

* For each example: input grid, DFS output, BFS output (they match).
* **Single-run** microsecond timings and **average** timings via `timeit`.
* Inline comments clearly state the time/space complexity at each step—great for interviews.

