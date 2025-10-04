
---

# 🏇 Steps by Knight

**Difficulty:** Medium
**Accuracy:** 37.32%
**Submissions:** 128K+
**Points:** 4
**Average Time:** 20m

---

## 🧩 Problem Statement

Given a square **chessboard** of size ( n \times n ), the **initial position** and **target position** of a Knight are given.
Your task is to **find out the minimum steps** a Knight will take to reach the target position.

> 📝 **Note:**
> The initial and target position coordinates of the Knight are given according to **1-based indexing**.

---

## 🧠 Examples

### Example 1

**Input:**

```
n = 3
knightPos[] = [3, 3]
targetPos[] = [1, 2]
```

**Output:**

```
1
```

**Explanation:**
Knight takes **1 step** to reach from (3, 3) to (1, 2).

---

### Example 2

**Input:**

```
n = 6
knightPos[] = [4, 5]
targetPos[] = [1, 1]
```

**Output:**

```
3
```

**Explanation:**
Knight takes **3 steps** to reach from (4, 5) to (1, 1):
Path →

```
(4, 5) → (5, 3) → (3, 2) → (1, 1)
```

![Knight Path Example](Steps-by-Knight.png)

---

## ⚙️ Constraints

```
1 ≤ n ≤ 1000
1 ≤ knightPos[x, y], targetPos[x, y] ≤ n
```

---

## ⏱️ Expected Complexities

| Complexity Type     | Value |
| ------------------- | ----- |
| **Time Complexity** | O(n²) |
| **Auxiliary Space** | O(n²) |

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* OYO Rooms
* MakeMyTrip
* Goldman Sachs
* Intuit
* LinkedIn

---

## 🧮 Topic Tags

* Graph
* BFS
* Data Structures
* Algorithms
* Queue

---

## 💬 Related Interview Experiences

* [Amazon Interview Experience Set 414 (SDE-1)](https://www.geeksforgeeks.org/amazon-interview-experience-set-414-sde-1/)
* [Intuit Interview Experience Set 13 (Campus)](https://www.geeksforgeeks.org/intuit-interview-experience-set-13-campus/)

---

## 📚 Related Articles

* [Minimum Steps to Reach Target by a Knight](https://www.geeksforgeeks.org/minimum-steps-to-reach-target-by-a-knight/)

---

---

awesome — let’s make this one airtight for interviews: a crisp intuition + dry run, then two Python solutions in your requested signature (classic BFS and a faster **bidirectional BFS**), with the exact inline comments interviewers like. I’ll wrap with common Q&A.

---

## 2) Intuition & Step-by-Step Dry Run

### Problem recap

* Chessboard is `n × n` (1-indexed in the prompt).
* Knight moves in **8 L-shaped** ways: `(±1, ±2)` and `(±2, ±1)`.
* Find the **minimum** moves to go from `knightPos` to `targetPos`.

### Why BFS?

Each move has the **same cost** (1). On an unweighted graph (cells are nodes; edges are knight moves), **BFS** from the source returns the **shortest path length** in layers.

### Dry run (Example 2)

```
n = 6
knightPos = [4, 5]
targetPos = [1, 1]
```

* Start at `(4,5)`; distance = 0.
* All 8 knight moves that stay inside the board are enqueued at distance 1. Two useful neighbors: `(5,3)`, `(2,4)`, etc.
* From `(5,3)` (dist 1), we expand: one child is `(3,2)` (dist 2).
* From `(3,2)` (dist 2), we expand: one child is `(1,1)` (dist 3) → reached target.
  So answer = **3**. One shortest path:
  `(4,5) → (5,3) → (3,2) → (1,1)`.

---

## 3) Optimized Codes (two ways)

### A) Standard BFS (what interviewers expect)

```python
from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        """
        Classic BFS on an unweighted grid graph.
        - State: (r, c)
        - Start: knightPos
        - Goal:  targetPos
        - Edges: 8 knight moves inside [1..n] × [1..n]
        
        Time  : O(n^2) in worst case (every cell visited once)
        Space : O(n^2) for visited + queue
        """
        sr, sc = knightPos
        tr, tc = targetPos
        
        # Trivial case
        if (sr, sc) == (tr, tc):
            return 0
        
        # 8 knight moves
        moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                 (+2, +1), (+2, -1), (-2, +1), (-2, -1)]
        
        # visited as a boolean grid (1-based indexing convenient here)
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        q = deque()
        q.append((sr, sc, 0))      # (row, col, steps)
        visited[sr][sc] = True
        
        while q:
            r, c, d = q.popleft()
            # expand neighbors
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= n and 1 <= nc <= n and not visited[nr][nc]:
                    if (nr, nc) == (tr, tc):
                        return d + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))
        
        # For completeness; a knight on a finite board always reaches any square.
        return -1
```

### B) Bidirectional BFS (reduces search dramatically when n is large)

```python
from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        """
        Bidirectional BFS from both start and target simultaneously.
        Expected to be faster in practice (search depth roughly halves).
        
        Time  : O(n^2) worst-case, but ~O(b^(d/2)) nodes visited vs O(b^d) for normal BFS
                (b ~ 6 on average for knight moves inside board, d = shortest distance)
        Space : O(n^2) for visited/frontiers
        """
        sr, sc = knightPos
        tr, tc = targetPos
        if (sr, sc) == (tr, tc):
            return 0
        
        moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                 (+2, +1), (+2, -1), (-2, +1), (-2, -1)]
        
        # visited maps store distance from their respective sides
        vis_s = [[-1] * (n + 1) for _ in range(n + 1)]
        vis_t = [[-1] * (n + 1) for _ in range(n + 1)]
        
        qs = deque([(sr, sc)])
        qt = deque([(tr, tc)])
        vis_s[sr][sc] = 0
        vis_t[tr][tc] = 0
        
        def expand(q, vis_self, vis_other):
            """Expand one level from one side; return total distance if frontiers meet."""
            for _ in range(len(q)):
                r, c = q.popleft()
                d = vis_self[r][c]
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= n and 1 <= nc <= n and vis_self[nr][nc] == -1:
                        vis_self[nr][nc] = d + 1
                        # If the other side has already visited this cell, we met!
                        if vis_other[nr][nc] != -1:
                            return vis_self[nr][nc] + vis_other[nr][nc]
                        q.append((nr, nc))
            return None
        
        while qs and qt:
            # Expand the smaller frontier first (heuristic)
            if len(qs) <= len(qt):
                meet = expand(qs, vis_s, vis_t)
            else:
                meet = expand(qt, vis_t, vis_s)
            if meet is not None:
                return meet
        
        return -1  # should not happen on a valid board
```

> Both versions accept 1-based coordinates as in the prompt. If you prefer 0-based, just shift by −1 and adjust bounds.

---

## 4) Interview Q&A (high-yield)

**Q1. Why is BFS optimal here?**
Edges all have equal weight (1 move). In unweighted graphs, BFS discovers vertices in **increasing distance layers**, guaranteeing the first time you see the target is the shortest path.

**Q2. Time and space complexity?**

* BFS: visits each cell at most once → **O(n²)** time and space.
* Bidirectional BFS: same big-O worst case, but typically explores about ( b^{d/2} ) states from each side instead of ( b^d ) (where ( b ) is branching, ( d ) is distance) — often much faster.

**Q3. Are there unreachable cases?**
On an empty ( n \times n ) board, a knight can reach any square from any other square for ( n \ge 2 ). (For ( n=1 ), only one cell, trivial.) The `-1` return is defensive.

**Q4. Do we need Dijkstra/A*?**
No. All moves cost 1, so BFS suffices. A* needs a consistent heuristic; there’s no simple admissible heuristic that substantially outperforms BFS here.

**Q5. Why 1-based indexing in code?**
The prompt uses 1-based `(row, col)`. Keeping 1-based avoids off-by-one errors. Converting to 0-based is also fine.

**Q6. Any micro-optimizations?**

* Expand the **smaller frontier first** in bidirectional BFS.
* Precompute valid moves or use a local tuple list (as shown) to avoid reallocations.

**Q7. Path reconstruction?**
Not required here (only minimum steps). If asked, store parents (`parent[r][c]`) and backtrack after reaching the target.

---

---

here’s a **runnable, interview-style full program** for **Steps by Knight** with:

* two implementations: **BFS** (canonical) and **Bidirectional BFS** (faster in practice),
* dense inline **time/space complexity** notes where they matter,
* a tiny **driver** that prints inputs & outputs,
* and **timeit** micro-benchmarks comparing both variants.

I finish with a handful of **important real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Steps by Knight (minimum knight moves on an n x n chessboard)

We implement:
  A) BFS (canonical shortest path in unweighted graphs)
     - Time  : O(n^2) in the worst case (each cell visited once)
     - Space : O(n^2) for visited + queue

  B) Bidirectional BFS (search from start and target simultaneously)
     - Same worst-case O(n^2) space/time, but typically ~O(b^(d/2)) nodes
       from each side instead of O(b^d) for standard BFS (b≈6 average branching,
       d = shortest distance), hence much faster in practice on large boards.

Driver:
  - Runs the two examples from the prompt and a couple of extra tests.
  - Benchmarks both approaches with timeit.
"""

from collections import deque
import timeit
from typing import List, Tuple


# ------------------------------- Approach A: BFS -------------------------------- #
class SolutionBFS:
    def minStepToReachTarget(self, knightPos: List[int], targetPos: List[int], n: int) -> int:
        """
        Classic BFS over board cells.
        Each cell is a node; edges are knight moves (cost=1).
        BFS explores layers by distance, so first time we see target is optimal.

        Time  : O(n^2) — each cell enqueued/visited at most once
        Space : O(n^2) — visited matrix + queue in the worst case
        """
        sr, sc = knightPos
        tr, tc = targetPos

        # Trivial case — same cell.
        if (sr, sc) == (tr, tc):
            return 0

        # 8 knight moves (Δrow, Δcol)
        moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                 (+2, +1), (+2, -1), (-2, +1), (-2, -1)]

        # visited matrix; we keep 1-based indexing to match prompt
        visited = [[False] * (n + 1) for _ in range(n + 1)]

        # Standard BFS queue: (row, col, dist)
        q = deque()
        q.append((sr, sc, 0))
        visited[sr][sc] = True

        while q:
            r, c, d = q.popleft()  # O(1)

            # Expand neighbors — up to 8, constant factor
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                # Keep inside board and not seen before: O(1)
                if 1 <= nr <= n and 1 <= nc <= n and not visited[nr][nc]:
                    if (nr, nc) == (tr, tc):
                        return d + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

        # Should not happen for n>=2 on an empty board, but keep for completeness
        return -1


# --------------------------- Approach B: Bidirectional BFS --------------------------- #
class SolutionBiBFS:
    def minStepToReachTarget(self, knightPos: List[int], targetPos: List[int], n: int) -> int:
        """
        Bidirectional BFS: grow two frontiers (from source & target) and stop when they meet.
        Heuristically halves the depth explored.

        Time  : O(n^2) worst-case, but in practice ~O(b^(d/2)) nodes per side.
        Space : O(n^2) for visited distance maps + queues.
        """
        sr, sc = knightPos
        tr, tc = targetPos
        if (sr, sc) == (tr, tc):
            return 0

        moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                 (+2, +1), (+2, -1), (-2, +1), (-2, -1)]

        # Distance-from-source / -from-target; -1 means unvisited
        vis_s = [[-1] * (n + 1) for _ in range(n + 1)]
        vis_t = [[-1] * (n + 1) for _ in range(n + 1)]
        qs = deque([(sr, sc)])
        qt = deque([(tr, tc)])
        vis_s[sr][sc] = 0
        vis_t[tr][tc] = 0

        def expand(q: deque, vis_self, vis_other):
            """
            Expand one breadth layer from one frontier.
            If we hit a cell already touched by the other frontier, return total distance.
            Otherwise return None.
            """
            # Expand a whole layer for well-formed bi-BFS
            for _ in range(len(q)):
                r, c = q.popleft()
                d = vis_self[r][c]
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= n and 1 <= nc <= n and vis_self[nr][nc] == -1:
                        vis_self[nr][nc] = d + 1
                        if vis_other[nr][nc] != -1:
                            # Frontiers met → shortest path found
                            return vis_self[nr][nc] + vis_other[nr][nc]
                        q.append((nr, nc))
            return None

        # Alternate expanding the smaller frontier for efficiency
        while qs and qt:
            if len(qs) <= len(qt):
                meet = expand(qs, vis_s, vis_t)
            else:
                meet = expand(qt, vis_t, vis_s)
            if meet is not None:
                return meet

        return -1


# ---------------------------------- timing harness ---------------------------------- #
def bench(func, *args, number=3000) -> float:
    """
    Average seconds/run using timeit.
    For tiny inputs Python overhead dominates; treat results as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# --------------------------------------- demo --------------------------------------- #
if __name__ == "__main__":
    print("=== Steps by Knight — BFS vs Bidirectional BFS ===\n")

    # Example 1 (prompt)
    n1 = 3
    knight1 = [3, 3]
    target1 = [1, 2]

    # Example 2 (prompt)
    n2 = 6
    knight2 = [4, 5]
    target2 = [1, 1]

    # A larger example for timing
    n3 = 1000
    knight3 = [1, 1]
    target3 = [987, 543]

    A = SolutionBFS()
    B = SolutionBiBFS()

    # --- Run examples and print outputs ---
    print(">>> Example 1")
    print(f"n={n1}, knight={knight1}, target={target1}")
    ansA1 = A.minStepToReachTarget(knight1, target1, n1)
    ansB1 = B.minStepToReachTarget(knight1, target1, n1)
    print("BFS            :", ansA1)
    print("Bidirectional  :", ansB1, "\n")

    print(">>> Example 2")
    print(f"n={n2}, knight={knight2}, target={target2}")
    ansA2 = A.minStepToReachTarget(knight2, target2, n2)
    ansB2 = B.minStepToReachTarget(knight2, target2, n2)
    print("BFS            :", ansA2)
    print("Bidirectional  :", ansB2, "\n")

    # --- Micro-benchmarks ---
    print("=== Timings (average seconds per run) ===")
    runs_small = 20000
    tA_s = bench(SolutionBFS().minStepToReachTarget, knight1, target1, n1, number=runs_small)
    tB_s = bench(SolutionBiBFS().minStepToReachTarget, knight1, target1, n1, number=runs_small)
    print(f"Small  (n={n1}) runs={runs_small:5d}:  BFS {tA_s:.8e}s | BiBFS {tB_s:.8e}s")

    runs_med = 5000
    tA_m = bench(SolutionBFS().minStepToReachTarget, knight2, target2, n2, number=runs_med)
    tB_m = bench(SolutionBiBFS().minStepToReachTarget, knight2, target2, n2, number=runs_med)
    print(f"Medium (n={n2}) runs={runs_med:5d}:  BFS {tA_m:.8e}s | BiBFS {tB_m:.8e}s")

    # A single-run style benchmark for a larger board to show practical difference
    runs_big = 20
    tA_b = bench(SolutionBFS().minStepToReachTarget, knight3, target3, n3, number=runs_big)
    tB_b = bench(SolutionBiBFS().minStepToReachTarget, knight3, target3, n3, number=runs_big)
    print(f"Large  (n={n3}) runs={runs_big:5d}:  BFS {tA_b:.8e}s | BiBFS {tB_b:.8e}s")

    print("\nNote: exact timing depends on machine and Python version. "
          "Bidirectional BFS typically shines as the board and distance grow.")
```

### What you’ll see

* Example 1 prints `1`; Example 2 prints `3`.
* Timings show both variants are fast on small boards; **Bidirectional BFS** gains on larger boards or distant targets.

---

## 6) Real-World Use Cases (the important ones)

1. **Robot motion on grid with discrete moves**
   When a robot/tool has movement constraints akin to “knight-like” jumps, shortest-move planning uses **BFS** in an unweighted move graph.

2. **Game AI pathfinding (unweighted state graphs)**
   Many board games (knight tours, puzzles) map to unweighted graphs where **BFS gives optimal move counts**; **bi-BFS** reduces turnaround in real-time AI.

3. **Network/graph reachability with uniform costs**
   When every transition has equal cost (e.g., hop count), minimal-hop routing or state-space exploration uses **BFS**; bi-BFS accelerates queries.

4. **Interactive puzzle solvers & tutoring tools**
   Teaching shortest-path concepts with knight moves is common; these implementations are the **canonical references**.