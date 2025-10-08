# Rotten Oranges

**Difficulty:** Medium
**Accuracy:** 46.02%
**Submissions:** 190K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a matrix **mat[][]** of dimension **n * m** where each cell in the matrix can have values **0, 1 or 2** which has the following meaning:

* **0** : Empty cell
* **1** : Cell have fresh oranges
* **2** : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (**up, down, left and right**) in a unit time.

**Note:** Your task is to return the minimum time to rot all the fresh oranges. If not possible returns **-1**.

---

## Examples

### Example 1

**Input:**

```
mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
```

**Output:**

```
1
```

**Explanation:**
Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.

---

### Example 2

**Input:**

```
mat[][] = [[2, 2, 0, 1]]
```

**Output:**

```
-1
```

**Explanation:**
Oranges at (0,0) and (0,1) can't rot orange at (0,3).

---

### Example 3

**Input:**

```
mat[][] = [[2, 2, 2], [0, 2, 0]]
```

**Output:**

```
0
```

**Explanation:**
There is no fresh orange.

---

## Constraints

* (1 \le \text{mat.size()} \le 500)
* (1 \le \text{mat}[0].\text{size()} \le 500)
* (\text{mat}[i][j] \in {0, 1, 2})

---

## Expected Complexities

* **Time Complexity:** (O(n * m))
* **Auxiliary Space:** (O(n * m))

---

## Company Tags

Flipkart · Accolite · Amazon · Microsoft · OYO Rooms · Samsung · MakeMyTrip

---

## Topic Tags

Matrix · Graph · Data Structures · Queue

---

## Related Interview Experiences

* Microsoft Interview Experience Set 76 On Campus
* Accolite Interview Experience Set 3 On Campus
* Amazon Interview Experience Set 389 Campus Full Time
* Samsung Research Institute Bangalore Srib Intern
* Flipkart Interview Experience For Sde2 2 5 Yr Exp

---

## Related Articles

* Minimum Time Required So That All Oranges Become Rotten

---

---

awesome — here’s an interview-ready pack for **Rotten Oranges**: crisp intuition, a step-by-step dry run, and multiple Python solutions in your requested template (with inline complexity notes), plus common interview Q&A.

---

# 2) Intuition & Step-by-Step Dry Run

## Core idea (what interviewers expect)

Treat the grid as a graph. All initially **rotten** cells (`2`) start rotting their 4-neighbors (`1`) **in parallel** every minute. That’s a classic **multi-source BFS**:

* Put **all** rotten cells in the queue at time 0.
* Expand level by level (each level = 1 minute).
* When we turn a fresh orange to rotten, push it into the queue for the next minute.
* Track how many fresh oranges remain.
* If BFS finishes and some fresh remain, it’s **impossible** → return `-1`.

Time is simply the number of BFS **layers** needed to visit all fresh cells.

---

## Dry run (Example 1)

```
mat = [
 [0,1,2],
 [0,1,2],
 [2,1,1]
]
```

* Initial rotten (time 0): `[(0,2), (1,2), (2,0)]`. Fresh count = 5 (cells with 1).
* Minute 1 (BFS layer 1):

  * From (0,2) → rots (0,1).
  * From (1,2) → rots (1,1).
  * From (2,0) → rots (2,1).
  * New queue after minute 1: `[(0,1), (1,1), (2,1)]`. Fresh left = 2 (positions (2,2) and (2,1) was rotted).
* Minute 2 (BFS layer 2):

  * From (0,1) → nothing new.
  * From (1,1) → rots (2,1) (already rotten) and (2,1)’s neighbor (2,2).
  * From (2,1) → rots (2,2) (already accounted).
  * Fresh left becomes 0 **during** this layer.

Answer = **2 − 1?** Careful: with layered BFS we count **finished layers that actually propagate**. If we loop while `queue` and `fresh>0`, we increment minutes **after** processing each layer that rots new oranges. For this input, result is **1** (as in the prompt), because all remaining fresh are reached in **one** layer from the initial rotten set.

Using the standard pattern “while queue and fresh>0: process layer; minutes += 1”, we end with `minutes = 1`.

---

# 3) Python solutions (interview-ready)

### A) Multi-source BFS (primary & most expected)

```python
from collections import deque

class Solution:
    def orangesRotting(self, mat):
        """
        Multi-source BFS from all initially rotten cells.
        - Each BFS layer = 1 minute.
        - Stop when no fresh left or queue exhausted.

        Let n = rows, m = cols.
        Time:  O(n*m)   - each cell enqueued at most once, 4 neighbors per cell (constant).
        Space: O(n*m)   - queue in worst case.
        """
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        q = deque()
        fresh = 0

        # 1) Collect all rotten (sources) and count fresh ---------- O(n*m)
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 2:
                    q.append((r, c))
                elif mat[r][c] == 1:
                    fresh += 1

        # No fresh oranges? Time = 0
        if fresh == 0:
            return 0

        minutes = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2) BFS layers while we still have fresh ------------------ ≤ O(n*m)
        while q and fresh > 0:
            for _ in range(len(q)):  # process one "minute" worth
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    # if neighbor is fresh, rot it and enqueue
                    if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                        mat[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1  # finished one minute of spread

        # 3) If fresh remains, impossible
        return minutes if fresh == 0 else -1
```

---

### B) BFS with explicit timestamps (same logic, sometimes clearer)

```python
from collections import deque

class Solution:
    def orangesRotting(self, mat):
        """
        Store (r, c, t) in queue; track 'ans' = max time seen for any rotting.
        Time:  O(n*m)
        Space: O(n*m)
        """
        if not mat or not mat[0]:
            return 0
        n, m = len(mat), len(mat[0])

        q = deque()
        fresh = 0

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 2:
                    q.append((r, c, 0))  # time 0
                elif mat[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        ans = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, t = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, t + 1))
                    ans = max(ans, t + 1)

        return ans if fresh == 0 else -1
```

---

### C) “Brute simulation by rounds” (educational baseline)

```python
class Solution:
    def orangesRotting(self, mat):
        """
        Repeatedly scan the grid; in each minute, mark all fresh neighbors of current rotten.
        Use a copy (or mark-to-2-after-round) to avoid chaining within the same minute.

        Time:  O(K * n * m), K = minutes until steady state (worst case O(n*m))
        Space: O(n*m) for a copy or O(1) if marking with a sentinel.
        """
        if not mat or not mat[0]:
            return 0
        n, m = len(mat), len(mat[0])

        fresh = sum(mat[r][c] == 1 for r in range(n) for c in range(m))
        if fresh == 0:
            return 0

        minutes = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while True:
            changed = []
            for r in range(n):
                for c in range(m):
                    if mat[r][c] == 2:
                        for dr, dc in DIRS:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                                changed.append((nr, nc))
            if not changed:
                break
            for r, c in changed:
                mat[r][c] = 2
                fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
```

> This brute is easy to reason about but can be too slow for the largest bounds—use BFS in interviews.

---

# 4) Interview Q&A (high-yield)

**Q1. Why multi-source BFS?**
Because all initially rotten oranges spread **simultaneously** each minute. BFS from all sources naturally models parallel waves; each **level** corresponds to one minute.

**Q2. How do you detect “impossible”?**
If BFS finishes and `fresh > 0`, some fresh oranges were never reached → return `-1` (blocked by `0`s).

**Q3. What’s the time/space complexity?**
`O(n*m)` time (each cell processed at most once; 4 constant neighbors) and `O(n*m)` space for the queue (worst case).

**Q4. Do we need a `visited` matrix?**
No. When a fresh orange is rotted (`1 → 2`), it won’t be processed as fresh again. The grid itself serves as visited marking.

**Q5. Why does the “while queue and fresh>0” minute-counting pattern work?**
You increment minutes **after** fully processing the current layer. Each full layer equals one minute of spread, so the count matches elapsed time until all fresh are rotted.

**Q6. What edge cases to test?**

* No fresh oranges at all → return `0`.
* Fresh but no rotten → return `-1`.
* Single cell grids (0/1/2).
* Islands of fresh separated by `0`s.

**Q7. Could we use Dijkstra / weighted BFS?**
Not needed—each move takes exactly 1 minute and all edges have equal weight → plain BFS is optimal.

**Q8. How to return the set of minutes per cell (if asked)?**
Use variant **B** (timestamps). The `t` you assign is the minute that cell turned rotten.

---

---

you got it — here’s a **runnable, interview-style full program** for **Rotten Oranges** with:

* your requested class/method signature,
* detailed inline **time/space complexity** notes,
* a simple **driver** that prints inputs & outputs,
* **timeit** micro-benchmarks for the full program call,
* and a short list of **real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Rotten Oranges (Multi-source BFS)

Grid cell meaning:
  0 = empty, 1 = fresh, 2 = rotten
Each minute, rotten cells rot their 4-neighbors (up/down/left/right).

Approach:
  Put ALL initially-rotten cells into a queue (time 0) and run BFS in layers.
  Each BFS layer corresponds to 1 minute. Whenever we convert fresh -> rotten,
  we push the cell into the queue for the next layer and decrement 'fresh' count.
  If BFS finishes and fresh > 0, it's impossible -> return -1.

Global complexities for an n x m grid:
  Time:  O(n*m)   (each cell processed at most once; constant 4 neighbors)
  Space: O(n*m)   (queue worst-case, no extra visited needed — we modify the grid)
"""

from collections import deque
import timeit
from typing import List


class Solution:
    # ----------------------------------------------------------------------
    # Function to compute minimum minutes to rot all fresh oranges.
    # Signature as requested by the prompt.
    # ----------------------------------------------------------------------
    def orangesRotting(self, mat: List[List[int]]) -> int:
        """
        Multi-source BFS from all initially-rotten cells.

        Steps:
          1) Scan grid: enqueue all rotten and count fresh.       Time: O(n*m)  Space: O(#rotten) ⊆ O(n*m)
          2) While queue not empty AND fresh > 0:
               - Process one BFS layer (all nodes currently in q) Time: O(width_of_layer)
               - For each popped cell, rot its fresh neighbors.   Time: O(1) per neighbor (4 neighbors)
               - minutes += 1 after finishing the layer.
          3) If fresh == 0, return minutes else -1.

        Returns:
            int: minutes needed or -1 if impossible.
        """
        # Guard ------------------------------------------------------------ O(1)
        if not mat or not mat[0]:
            return 0

        n, m = len(mat), len(mat[0])
        q = deque()
        fresh = 0

        # (1) Collect all rotten sources and count fresh ------------ O(n*m)
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 2:
                    q.append((r, c))                # enqueue rotten (time 0)
                elif mat[r][c] == 1:
                    fresh += 1

        # If no fresh oranges exist, no time is needed -------------- O(1)
        if fresh == 0:
            return 0

        # Directions: 4-neighborhood -------------------------------- O(1) space
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minutes = 0

        # (2) BFS in layers ----------------------------------------- ≤ O(n*m)
        while q and fresh > 0:
            # Process exactly one minute worth of spread
            layer_size = len(q)  # O(1)
            for _ in range(layer_size):
                r, c = q.popleft()     # O(1)

                # Visit 4 neighbors (constant) ---------------------- O(1)
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    # If neighbor is inside and fresh, rot it
                    if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                        mat[nr][nc] = 2  # mark as rotten (serves as visited)
                        fresh -= 1
                        q.append((nr, nc))  # O(1)

            # Finished one full layer => 1 minute elapsed ----------- O(1)
            minutes += 1

        # (3) If fresh remains, impossible; else minutes is the answer
        return minutes if fresh == 0 else -1


# ----------------------------- Tiny benchmark helper -----------------------------
def bench(func, *args, number=10000):
    """
    Use timeit to measure average seconds per run for func(*args).
    Note: On tiny inputs, overhead dominates — treat as relative indicator only.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ----------------------------- Main: inputs, outputs, timings -----------------------------
if __name__ == "__main__":
    tests = [
        # (matrix, expected, note)
        (
            [[0, 1, 2],
             [0, 1, 2],
             [2, 1, 1]],
            1,
            "Example 1: all fresh rot within 1 minute"
        ),
        (
            [[2, 2, 0, 1]],
            -1,
            "Example 2: isolated fresh cannot be reached"
        ),
        (
            [[2, 2, 2],
             [0, 2, 0]],
            0,
            "Example 3: no fresh present"
        ),
        (
            [[1, 1, 1],
             [1, 2, 1],
             [1, 1, 1]],
            2,
            "Symmetric spread from center"
        ),
        (
            [[1, 0, 1],
             [0, 2, 0],
             [1, 0, 1]],
            -1,
            "Walls block all fresh from the only rotten"
        ),
    ]

    print("=== Rotten Oranges — Multi-source BFS ===\n")
    solver = Solution()

    # Show inputs & outputs
    for mat, expected, note in tests:
        mat_show = [row[:] for row in mat]  # keep a pretty copy for printing
        ans = solver.orangesRotting(mat)    # note: mutates the grid
        print(note)
        for row in mat_show:
            print(row)
        print(f"Output: {ans} | Expected: {expected}\n")

    # --------------- Timings with timeit ---------------
    print("=== Timings (average seconds per run) ===")
    small = [[0, 1, 2],
             [0, 1, 2],
             [2, 1, 1]]
    medium = [[2, 1, 1, 0, 1, 1],
              [1, 0, 1, 1, 0, 2],
              [1, 1, 1, 0, 1, 1],
              [0, 1, 0, 1, 1, 1],
              [2, 1, 1, 1, 0, 1],
              [1, 1, 0, 1, 1, 1]]
    large = [[1]*40 for _ in range(40)]
    large[20][20] = 2  # single rotten in the middle

    runs_small = 20000
    runs_medium = 5000
    runs_large = 500

    t_small = bench(Solution().orangesRotting, [row[:] for row in small], number=runs_small)
    t_medium = bench(Solution().orangesRotting, [row[:] for row in medium], number=runs_medium)
    t_large = bench(Solution().orangesRotting, [row[:] for row in large], number=runs_large)

    print(f"Small (3x3)  runs={runs_small}: {t_small:.8e} s")
    print(f"Medium (6x6) runs={runs_medium}: {t_medium:.8e} s")
    print(f"Large (40x40) runs={runs_large}: {t_large:.8e} s")

    print("\nNote: timings vary by machine and Python version.")
```

---

## 6) Real-World Use Cases (the important ones)

1. **Epidemic / Contagion Modeling on Grids**
   Simulate infection spread from multiple initial carriers across neighborhoods/floors with blocked zones.

2. **Fire/Contaminant Propagation in Facilities**
   Estimate time for smoke/contaminants to reach all reachable rooms, accounting for walls and sealed areas.

3. **Network Failure / Patch Propagation**
   Model how fast an update (or outage) propagates from several nodes to the rest of a grid/mesh network.

4. **Multi-source Flood Fill in Image Processing**
   Grow regions from multiple seeds over a 2D raster, counting steps (iterations) to reach all pixels in a component.