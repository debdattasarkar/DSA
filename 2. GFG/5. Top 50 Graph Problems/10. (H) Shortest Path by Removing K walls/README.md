# Shortest Path by Removing K walls

**Difficulty:** Hard
**Accuracy:** 50.4%
**Submissions:** 22K+
**Points:** 8
**Average Time:** 40m

---

## Problem Statement

Given a 2-D binary **matrix** of size **n * m**, where `0` represents an empty space while `1` represents a wall you cannot walk through. You are also given an integer **k**.

You can walk up, down, left, or right. **Given that you can remove up to k walls, return the minimum number of steps** to walk from the top-left corner `(0, 0)` to the bottom-right corner `(n-1, m-1)`.

**Note:** If there is no way to walk from the top-left corner to the bottom-right corner, return **-1**.

---

## Examples

### Example 1

**Input:**

```
n = 3, m = 3, k = 1
mat = {{0, 0, 0},
       {0, 0, 1},
       {0, 1, 0}}
```

**Output:**

```
4
```

**Explanation:**
We can remove any one of the walls and reach the bottom in 4 moves.

---

### Example 2

**Input:**

```
n = 2, m = 2, k = 0
mat = {{0, 1},
       {1, 0}}
```

**Output:**

```
-1
```

**Explanation:**
There's no way of reaching the bottom corner **without** removing any walls.

---

## Your Task

The task is to complete the function **`shotestPath()`** which takes three integers `n`, `m`, and `k` and also a matrix of size `n*m` as input and **returns the minimum number of steps** to walk from the top-left corner to the bottom-right corner.

---

## Constraints

* (1 \le n, m \le 50)
* (0 \le k \le n * m)
* Top-left and bottom-right corners **don't** have `1`

---

## Expected Complexities

* **Time Complexity:** (O(n * m * k))
* **Auxiliary Space:** (O(n * m * k))

---

## Company Tags

Google

---

## Topic Tags

Matrix · BFS · Data Structures · Algorithms

---

## Related Articles

* Shortest Path By Removing K Walls

---

---

awesome — here’s an interview-ready bundle for **Shortest Path by Removing K Walls**: crisp intuition, a concrete dry run, and multiple Python solutions (optimal BFS, a memory-lean variant, and a brute-force for learning), all in your requested signature. I’ll finish with high-yield interviewer Q&A.

---

# 2) Intuition & step-by-step dry run

## Problem recap

* Grid `mat` (0 = free, 1 = wall), moves in 4 dirs.
* You may delete up to `k` walls *on the way*.
* Return **minimum steps** from `(0,0)` → `(n-1,m-1)`, else `-1`.

## Core idea (what interviewers expect)

Treat each state as **(row, col, remaining_walls)**.
Use **BFS** because all edges cost 1. BFS explores by layers ⇒ the first time we pop a goal state is the **shortest steps**.

### Key pruning

You can revisit the same cell with **more** remaining walls and still be better:
Keep a `seen[r][c]` recording the **maximum** `remaining_walls` we have seen at `(r,c)`.
If we arrive at `(r,c)` with `rem ≤ seen[r][c]`, it’s a **worse or equal** state → **skip**.

This turns the usual 3D `visited[r][c][rem]` into a **2D pruning** and is very common in interviews.

---

## Dry run (Example 1)

```
n=m=3, k=1
mat =
0 0 0
0 0 1
0 1 0
target = (2,2)
```

Start: `(0,0,1)`, steps = 0, seen[0][0] = 1.

Layer 1 (steps=1): neighbors of (0,0)

* (1,0,1) [free], (0,1,1) [free]

Layer 2 (steps=2):

* From (1,0,1) → (2,0,1) [free], (1,1,1) [free]
* From (0,1,1) → (0,2,1) [free], (1,1,1) again (pruned by seen)

Layer 3 (steps=3):

* (2,0,1) → (2,1,**wall**) ⇒ consume 1 → (2,1,0)
* (1,1,1) → (1,2,**wall**) ⇒ consume 1 → (1,2,0), (2,1,**wall**) again but worse (rem 0 ≤ seen 0) ties allowed, pruned later
* (0,2,1) → (1,2,**wall**) ⇒ (1,2,0) (duplicate, pruned)

Layer 4 (steps=4):

* From (2,1,0) → (2,2,0) [free] → **goal** reached in **4**.

Answer = **4**.

---

# 3) Python solutions (interview-ready)

## A) Optimal BFS with **2D “best remaining k” pruning** (most expected)

```python
# User function Template for python3
from collections import deque

class Solution:
    def shotestPath(self, mat, n, m, k):
        """
        BFS over state = (r, c, rem_k) with pruning by best remaining k per cell.

        Let N=n, M=m.
        Time  : O(N*M*K)    (each (r,c) can be improved up to K times)
        Space : O(N*M) for 'seen' + O(N*M) for queue in worst case
        """
        # Quick target check
        if n == 0 or m == 0:
            return -1
        if (n - 1, m - 1) == (0, 0):
            return 0  # already there

        # seen[r][c] = max remaining k we've ever had upon reaching (r,c)
        seen = [[-1] * m for _ in range(n)]
        q = deque()
        q.append((0, 0, k))
        seen[0][0] = k

        steps = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            # process one BFS layer => one step
            for _ in range(len(q)):
                r, c, rem = q.popleft()

                if (r, c) == (n - 1, m - 1):
                    return steps

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        nrem = rem
                        if mat[nr][nc] == 1:
                            if rem == 0:      # can't remove more
                                continue
                            nrem = rem - 1    # consume a wall

                        # prune if we have seen this cell with >= remaining walls
                        if nrem <= seen[nr][nc]:
                            continue
                        seen[nr][nc] = nrem
                        q.append((nr, nc, nrem))
            steps += 1

        return -1
```

---

## B) Same BFS but with **3D visited** (straightforward, easy to explain)

```python
from collections import deque

class Solution:
    def shotestPath(self, mat, n, m, k):
        """
        3D visited[r][c][rem] to avoid revisiting same state.
        Time  : O(N*M*K)
        Space : O(N*M*K)
        """
        visited = [[[False]*(k+1) for _ in range(m)] for __ in range(n)]
        q = deque()
        q.append((0, 0, k, 0))  # (r, c, rem, steps)
        visited[0][0][k] = True
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, rem, steps = q.popleft()
            if (r, c) == (n - 1, m - 1):
                return steps
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    nrem = rem - mat[nr][nc]  # consume 1 if wall, else 0
                    if nrem < 0:
                        continue
                    if not visited[nr][nc][nrem]:
                        visited[nr][nc][nrem] = True
                        q.append((nr, nc, nrem, steps + 1))
        return -1
```

---

## C) (Educational) Brute DFS with memo (still exponential without good pruning)

```python
class Solution:
    def shotestPath(self, mat, n, m, k):
        """
        Exponential DFS exploring paths; memoize best remaining k at (r,c,steps).
        Still can blow up on worst cases; included for learning contrast.
        """
        best = {}  # (r,c,rem) -> smallest steps seen
        ans = [float('inf')]
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, rem, steps):
            if steps >= ans[0]:                # pruning by current best
                return
            if (r, c) == (n-1, m-1):
                ans[0] = min(ans[0], steps)
                return
            key = (r, c, rem)
            if key in best and best[key] <= steps:
                return
            best[key] = steps

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if mat[nr][nc] == 1:
                        if rem > 0:
                            dfs(nr, nc, rem - 1, steps + 1)
                    else:
                        dfs(nr, nc, rem, steps + 1)

        dfs(0, 0, k, 0)
        return -1 if ans[0] == float('inf') else ans[0]
```

> In interviews, lead with **A** (or **B**). Mention why DFS is a bad fit here (shortest path in an unweighted graph → BFS).

---

# 4) Interview Q&A (high-yield)

**Q1. Why BFS instead of Dijkstra?**
All moves cost 1, so BFS already guarantees shortest path. Dijkstra would be overkill.

**Q2. Why 2D `seen[r][c] = bestRemainingK` works?**
If you’ve reached `(r,c)` with `rem_x` removals left, later reaching `(r,c)` with `rem_y ≤ rem_x` can never produce a **better** future path (having fewer bombs is never better). So we only keep visits that *improve* remaining `k`.

**Q3. Complexity?**
Each cell can be improved at most `k+1` times (from `k` down to `0`) → **O(n·m·k)** states. Each state processes 4 neighbors: **O(n·m·k)** time, **O(n·m)** (version A) or **O(n·m·k)** (version B) space.

**Q4. What if `k` is huge (≥ number of walls)?**
If `k` ≥ number of walls along an optimal Manhattan route, answer is at least the plain Manhattan distance `|n-1|+|m-1|` (if within bounds). You can early-check an upper bound, but BFS is still fine for constraints.

**Q5. Edge cases?**

* `n=m=1` → already at goal → `0`.
* Start/goal guaranteed not to be walls (per constraints).
* `k=0` reduces to classic shortest path in a binary maze (walls forbidden).
* Grid full of 0 → Manhattan distance.

**Q6. Could we use A*?**
Yes; an **admissible heuristic** is `h = manhattan((r,c),(n-1,m-1))`. It never overestimates even with removals. It often explores fewer states but adds code complexity; BFS passes within constraints.

**Q7. Why not mark 2D visited without tracking `k`?**
Because reaching the same cell with more remaining `k` can lead to a better path later. You must keep the **resource dimension**.

---

---

here you go — a **runnable, interview-style full program** for **Shortest Path by Removing K Walls** with:

* your requested signature,
* detailed inline **time/space complexity** notes,
* a small **driver** that prints inputs & outputs,
* and **timeit** micro-benchmarks (comparing the two common BFS variants).

I’ve wrapped **Approach A (2D best-k pruning)** as primary and **Approach B (3D visited)** for comparison.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Shortest Path by Removing K Walls (4-directional grid)

We must find the minimum steps from (0,0) to (n-1,m-1) in a 0/1 grid,
where '1' is a wall that can be removed at most k times along the path.

Primary approach (SolutionA.shotestPath):
  - State = (r, c, rem_k). Use BFS (unweighted edges).
  - Prune with a 2D table 'seen[r][c]' that stores the maximum remaining k
    we've ever had upon reaching (r,c). If we reach (r,c) with <= seen[r][c],
    we skip — having fewer removals left can never be better.
  - This reduces memory from O(n*m*k) to O(n*m) while keeping complexity O(n*m*k).

Alternate approach (SolutionB.shotestPath):
  - 3D visited[r][c][rem] to avoid revisits of exact states. Simpler to explain.

Global complexities for an n x m grid and budget k:
  Time : O(n*m*k)   # each cell can be improved up to k+1 times; constant 4 neighbors
  Space: 
     - Approach A: O(n*m) for 'seen' + O(n*m) queue worst-case
     - Approach B: O(n*m*k) for visited + O(n*m) queue
"""

from collections import deque
import timeit
from typing import List, Tuple


# -------------------------- Approach A: BFS + 2D best-k pruning (primary) -------------------------- #
class Solution:
    def shotestPath(self, mat: List[List[int]], n: int, m: int, k: int) -> int:
        """
        BFS over (r,c,rem) with pruning by best remaining 'k' seen at (r,c).

        Steps:
          1) Initialize 'seen' with -1 (unvisited). Push (0,0,k).               Time: O(1), Space: O(n*m)
          2) Standard BFS by layers (each layer = 1 step).                      Time: O(n*m*k)
             - For neighbor:
                 * If it's a wall and rem==0 -> skip, else nrem=rem-1
                 * If nrem <= seen[nr][nc] -> skip (not an improvement)
                 * Else record seen[nr][nc]=nrem and enqueue (nr,nc,nrem)
          3) First time we pop goal -> steps is the shortest.                   Time: O(n*m*k)

        Returns:
            Minimum steps or -1 if no path.

        Time  : O(n*m*k)
        Space : O(n*m) for 'seen' + O(n*m) queue worst-case
        """
        if n == 0 or m == 0:
            return -1
        if (n - 1, m - 1) == (0, 0):
            return 0

        seen = [[-1] * m for _ in range(n)]   # seen[r][c] = max remaining k observed at (r,c)
        q = deque([(0, 0, k)])
        seen[0][0] = k

        steps = 0
        DIRS: Tuple[Tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            layer_size = len(q)
            # Process one BFS layer => accounts for exactly 'steps' moves so far
            for _ in range(layer_size):
                r, c, rem = q.popleft()

                # If we reached target, current 'steps' is the shortest.
                if r == n - 1 and c == m - 1:
                    return steps

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:
                        nrem = rem
                        if mat[nr][nc] == 1:
                            if rem == 0:
                                continue  # cannot pass wall
                            nrem = rem - 1

                        # Prune: only accept if we improved remaining budget at this cell
                        if nrem <= seen[nr][nc]:
                            continue
                        seen[nr][nc] = nrem
                        q.append((nr, nc, nrem))
            steps += 1

        return -1


# ------------------------------ Approach B: BFS + 3D visited (reference) ------------------------------ #
class Solution3D:
    def shotestPath(self, mat: List[List[int]], n: int, m: int, k: int) -> int:
        """
        BFS over exact states with 3D visited[r][c][rem].

        Time  : O(n*m*k)
        Space : O(n*m*k)
        """
        visited = [[[False] * (k + 1) for _ in range(m)] for __ in range(n)]
        q = deque([(0, 0, k, 0)])  # (r, c, rem, steps)
        visited[0][0][k] = True

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, rem, steps = q.popleft()
            if r == n - 1 and c == m - 1:
                return steps
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    nrem = rem - mat[nr][nc]  # consume 1 if wall, else 0
                    if nrem < 0:
                        continue
                    if not visited[nr][nc][nrem]:
                        visited[nr][nc][nrem] = True
                        q.append((nr, nc, nrem, steps + 1))
        return -1


# -------------------------------------- timeit helper -------------------------------------- #
def bench(func, *args, number=5000):
    """
    Return average seconds per run using timeit.
    For tiny inputs, Python overhead dominates. Use as relative indicator only.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------------- demo ------------------------------------------- #
if __name__ == "__main__":
    print("=== Shortest Path by Removing K Walls — BFS with resource dimension ===\n")

    tests = [
        # (mat, n, m, k, note, expected)
        (
            [[0, 0, 0],
             [0, 0, 1],
             [0, 1, 0]],
            3, 3, 1, "Example 1", 4
        ),
        (
            [[0, 1],
             [1, 0]],
            2, 2, 0, "Example 2", -1
        ),
        (
            [[0, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 1, 1, 1],
             [0, 0, 0, 0]],
            5, 4, 2, "Corridor with two breakable walls", 7  # one plausible answer
        ),
        (
            [[0]],
            1, 1, 0, "Single cell already at goal", 0
        ),
    ]

    A = Solution()
    B = Solution3D()

    for mat, n, m, k, note, expected in tests:
        print(f">>> {note}")
        print("Grid:")
        for row in mat:
            print(row)
        outA = A.shotestPath([row[:] for row in mat], n, m, k)
        outB = B.shotestPath([row[:] for row in mat], n, m, k)
        print(f"Output (Approach A): {outA}")
        print(f"Output (Approach B): {outB}")
        if expected is not None:
            print(f"Expected (if provided): {expected}")
        print(f"Both approaches agree? {outA == outB}\n{'-'*60}\n")

    # ---------------------------- timings (average seconds per run) ---------------------------- #
    print("=== Timings (average seconds per run) ===")
    small = (
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]],
        3, 3, 1
    )
    medium = (
        [[0 if (r + c) % 3 else 1 for c in range(20)] for r in range(20)],
        20, 20, 4
    )
    large = (
        [[0 if (r * c) % 5 else 1 for c in range(35)] for r in range(35)],
        35, 35, 6
    )

    runs_small = 20000
    runs_medium = 3000
    runs_large = 800

    tA_s = bench(Solution().shotestPath, *small, number=runs_small)
    tB_s = bench(Solution3D().shotestPath, *small, number=runs_small)
    print(f"Small  (3x3, k=1)  runs={runs_small}:  A {tA_s:.8e}s  |  B {tB_s:.8e}s")

    tA_m = bench(Solution().shotestPath, *medium, number=runs_medium)
    tB_m = bench(Solution3D().shotestPath, *medium, number=runs_medium)
    print(f"Medium (20x20,k=4) runs={runs_medium}:  A {tA_m:.8e}s  |  B {tB_m:.8e}s")

    tA_l = bench(Solution().shotestPath, *large, number=runs_large)
    tB_l = bench(Solution3D().shotestPath, *large, number=runs_large)
    print(f"Large  (35x35,k=6) runs={runs_large}:  A {tA_l:.8e}s  |  B {tB_l:.8e}s")

    print("\nNote: exact times vary by machine and Python version.")
```

**What this prints**

* For each test: the **grid**, outputs from **Approach A** and **Approach B**, and whether they **agree**.
* Then it prints **timeit** averages for small/medium/large instances so you can compare memory-light vs 3D-visited BFS.

---

## 6) Real-World Use Cases (the important ones)

1. **Robotics navigation with limited obstacle clearing**
   A robot can push aside or cut a limited number of light obstacles; compute the quickest route under that budget.

2. **Routing with quotas**
   Network packets or vehicles that may traverse a limited number of toll/blocked edges — find the fastest path with a quota of “expensive” crossings.

3. **Game pathfinding with consumables**
   Player can break a limited number of walls/doors; AI needs shortest path considering remaining bombs/keys.

4. **Disaster response planning**
   First responders can breach a limited number of barriers (locked doors/debris) — plan the quickest access path under a breach quota.
