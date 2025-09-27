# Minimum Cost Path

**Difficulty:** Hard
**Accuracy:** 26.99%
**Submissions:** 125K+
**Points:** 8

---

Given a square **grid** of size **N**, each cell of which contains an integer **cost** that represents a cost to traverse through that cell, we need to find a **path** from the **top left** cell to the **bottom right** cell by which the total cost incurred is **minimum**.

From the cell (i, j) we can go **(i, j-1), (i, j+1), (i-1, j), (i+1, j)**.

---

## Examples

### Example 1

**Input:**
`grid = [[9,4,9,9],`
`         [6,7,6,4],`
`         [8,3,3,7],`
`         [7,4,9,10]]`

**Output:** `43`
**Explanation:** The minimum cost is —
`9 + 4 + 7 + 3 + 3 + 7 + 10 = 43`.

---

### Example 2

**Input:**
`grid = [[4,4],`
`         [3,7]]`

**Output:** `14`
**Explanation:** The minimum cost is — `4 + 4 + 3 + 7 = 14`.

---

## Constraints

* `1 ≤ n ≤ 500`
* `1 ≤ cost of cells ≤ 500`

---

## Expected Complexities

* **Time Complexity:** `O(n^2 * log(n))`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

Amazon • Microsoft • Samsung • MakeMyTrip • Goldman Sachs

---

## Topic Tags

Graph • Data Structures • Algorithms • Dynamic Programming • Heap

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 2 Campus
* Samsung Interview Experience Through Co Cubes 2019

---

## Related Articles

* Minimum Cost Path Left Right Bottom Moves Allowed

---

---

# Minimum Cost Path — Explanation + Dry Run + Python Solutions

## 2) Intuition

Treat the grid as a **weighted graph** with `N*N` nodes (each cell is a node).
From `(i, j)` you may move to the 4 neighbors: `(i±1, j)` and `(i, j±1)` (if in bounds).
The **cost of a path** is the **sum of the costs of all visited cells**; you **pay** the cost of the **start cell** too.

All edge weights are **non-negative**, so the right model is **Dijkstra’s shortest path** from `(0, 0)` to `(N-1, N-1)`.

* `dist[r][c]` = minimum cost found so far to reach `(r, c)`
* Initialize `dist[0][0] = grid[0][0]`, push it in a min-heap.
* Repeatedly pop the cell with the smallest cost; relax its 4 neighbors.
* As soon as you pop `(N-1, N-1)`, that cost is optimal → return it.

Why not simple DP? DP with only right/down moves works, but here **4 directions** allow cycles; DP without a fixed order can revisit cells. Dijkstra handles cycles with a visited set / monotone distances.

---

## Step-by-step Dry Run (sample 1)

Grid:

```
9  4  9  9
6  7  6  4
8  3  3  7
7  4  9 10
```

Start `dist(0,0)=9`. Min-heap keeps pairs `(cost, r, c)`.

1. Pop `(9,0,0)`
   Push neighbors:
   `(0,1): 9+4=13`, `(1,0): 9+6=15`.

2. Pop `(13,0,1)`
   Update: `(0,2): 13+9=22`, `(1,1): 13+7=20` (ignore `(0,0)`).

3. Pop `(15,1,0)`
   Update: `(2,0): 15+8=23`, `(1,1): 15+7=22` (worse than 20, ignore).

4. Pop `(20,1,1)`
   Update: `(1,2): 20+6=26`, `(2,1): 20+3=23`.

5. Pop `(22,0,2)`
   Update: `(0,3): 22+9=31`, `(1,2): min(26, 22+6=28)=26`.

6. Pop `(23,2,0)` and `(23,2,1)` (tie; order doesn’t matter)
   From `(2,1)=23` → `(2,2): 23+3=26`, `(3,1): 23+4=27`.

7. Pop `(26,1,2)` and `(26,2,2)`
   From `(2,2)=26` → `(2,3): 26+7=33`, `(3,2): 26+9=35`.

8. Pop `(27,3,1)`
   Update `(3,2): min(35, 27+9=36)=35`, `(2,1)` ignored.

9. Pop `(31,0,3)` → `(1,3): 31+4=35)`.

10. Pop `(33,2,3)` → `(3,3): 33+10=43)`.

11. Next pop is `(35,1,3)` or `(35,3,2)` etc., but once `(3,3)` is popped (cost **43**), it’s optimal.
    **Answer = 43** (path e.g., `9 → 4 → 7 → 3 → 3 → 7 → 10`).

---

## 3) Python solutions (with interview-style inline comments)

### ✅ Recommended: Dijkstra with a Min-Heap — `O(n^2 log n)` time, `O(n^2)` space

```python
import heapq
from math import inf

class Solution:
    
    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    def minimumCostPath(self, grid):
        n = len(grid)                           # O(1)
        # dist[r][c] = best known cost to reach (r, c)
        dist = [[inf] * n for _ in range(n)]    # O(n^2) space & init time
        dist[0][0] = grid[0][0]                 # cost includes start cell
        
        # Min-heap of (current_cost, r, c)
        pq = [(grid[0][0], 0, 0)]               # O(1) push
        # 4-direction moves
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Dijkstra: each cell can be popped at most once with its final cost
        # Time: each push/pop is O(log (n^2)) = O(log n). Total O(n^2 log n).
        while pq:
            cost, r, c = heapq.heappop(pq)      # O(log n)
            # If we popped a stale pair (greater than best), skip in O(1)
            if cost != dist[r][c]:
                continue
            # Early exit: first time we pop target -> optimal
            if r == n - 1 and c == n - 1:
                return cost                      # O(1)
            # Relax 4 neighbors
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n: # O(1)
                    ncost = cost + grid[nr][nc] # pay neighbor cell cost
                    if ncost < dist[nr][nc]:    # strict improvement
                        dist[nr][nc] = ncost
                        heapq.heappush(pq, (ncost, nr, nc))  # O(log n)

        # Should never get here since grid is connected via 4-dir moves
        return dist[n-1][n-1]
```

**Why it’s optimal:** all weights are non-negative; Dijkstra guarantees that when a node is popped from the PQ, its distance is finalized.

---

### Simpler but slower: Array-based Dijkstra (no heap) — `O(n^4)` time, `O(n^2)` space

Good as a “brute but easy” baseline.

```python
from math import inf

class SolutionArrayDijkstra:
    def minimumCostPath(self, grid):
        n = len(grid)
        dist = [[inf]*n for _ in range(n)]        # O(n^2)
        seen = [[False]*n for _ in range(n)]      # O(n^2)
        dist[0][0] = grid[0][0]
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # Repeat V times (V = n^2): each time pick unseen node with smallest dist
        for _ in range(n*n):                      # O(n^2) outer
            # Find the unseen node with minimum distance — O(n^2)
            rmin = cmin = -1
            best = inf
            for r in range(n):
                for c in range(n):
                    if not seen[r][c] and dist[r][c] < best:
                        best = dist[r][c]
                        rmin, cmin = r, c
            if rmin == -1: break
            if rmin == n-1 and cmin == n-1:
                return dist[rmin][cmin]
            seen[rmin][cmin] = True
            # Relax neighbors — O(1) each
            for dr,dc in DIRS:
                nr, nc = rmin+dr, cmin+dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    cand = dist[rmin][cmin] + grid[nr][nc]
                    if cand < dist[nr][nc]:
                        dist[nr][nc] = cand
        
        return dist[n-1][n-1]
```

---

### Heuristic speed-up: **A*** (admissible heuristic) — usually faster, worst-case like Dijkstra

Use `h = (|dr| + |dc|) * min_cell_cost` (Manhattan distance × best possible per step). This never overestimates → still finds the optimal cost.

```python
import heapq
from math import inf

class SolutionAStar:
    def minimumCostPath(self, grid):
        n = len(grid)
        min_cell = min(min(row) for row in grid)   # O(n^2)
        def h(r, c):                               # admissible heuristic
            return (abs(n-1 - r) + abs(n-1 - c)) * min_cell

        g = [[inf]*n for _ in range(n)]            # actual cost so far
        g[0][0] = grid[0][0]
        # PQ holds (f = g + h, g, r, c)
        pq = [(grid[0][0] + h(0,0), grid[0][0], 0, 0)]
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while pq:
            f, cost, r, c = heapq.heappop(pq)
            if cost != g[r][c]:
                continue
            if r == n-1 and c == n-1:
                return cost
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n:
                    cand = cost + grid[nr][nc]
                    if cand < g[nr][nc]:
                        g[nr][nc] = cand
                        heapq.heappush(pq, (cand + h(nr,nc), cand, nr, nc))
        return g[n-1][n-1]
```

---

## Complexity Summary

* **Dijkstra + heap (recommended):**

  * Time: `O((N^2) log (N^2)) = O(N^2 log N)`
  * Space: `O(N^2)` (distance table + heap)
* **Array-based Dijkstra (brute-ish):**

  * Time: `O((N^2)^2) = O(N^4)`
  * Space: `O(N^2)`
* **A*:**

  * Worst-case time like Dijkstra; often explores fewer nodes.
  * Space: `O(N^2)`.

---

## 4) Interview Q&A

**Q1. Why not simple DP like `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`?**
**A.** That DP assumes only right & down moves; with 4-direction moves, there are cycles and no natural topological order. Dijkstra is needed to handle revisits safely.

**Q2. Do we count the cost of the start cell?**
**A.** Yes; initialize `dist[0][0] = grid[0][0]`. Each move adds the cost of the **destination** cell.

**Q3. Can there be negative costs?**
**A.** The constraints state costs are positive (≥1). If negatives existed, Dijkstra is invalid; we’d need Bellman–Ford or detect negative cycles. With all positive weights, Dijkstra is correct and fast.

**Q4. When can we stop the algorithm early?**
**A.** In Dijkstra, the first time you **pop** `(n-1,n-1)` from the min-heap, its cost is optimal—return immediately.

**Q5. What’s the node/edge count?**
**A.** Nodes `V = N^2`. Edges `E ≈ 4N^2` (each cell has ≤4 neighbors). Hence `O(E log V) = O(N^2 log N)`.

**Q6. How do you reconstruct the path itself?**
**A.** Keep a `parent[r][c]` pointer when you relax a neighbor (set parent of neighbor to current cell). After finishing, backtrack from `(n-1,n-1)` to `(0,0)` and reverse.

**Q7. How would you reduce constant factors?**
**A.** Use **A*** with an admissible heuristic (e.g., Manhattan × min cell cost) to focus the search; also break early on target pop, and avoid pushing stale states by checking `if cost != dist[r][c]: continue`.

**Q8. Space optimizations?**
**A.** `dist` must remember the best cost for every cell: `O(N^2)` is tight. You can reuse a single heap and avoid a separate visited matrix by the “stale pop” check.

**Q9. If moves were only right/down, what would you do?**
**A.** A simple DP in `O(N^2)` time and `O(1)` or `O(N)` space with rolling rows.

**Q10. What about very large grids (e.g., N=2000)?**
**A.** `N=500` here is fine. For larger, use A* with a strong heuristic, or multi-source techniques if applicable; ensure you use a fast `heapq` and avoid Python overhead where possible (e.g., prebinding, using arrays).

---

---

Done! You’ve got a **full runnable program** (above) that:

* Implements three versions: **Dijkstra (heap)**, **A***, and **array-based Dijkstra**.
* Prints **inputs, outputs, expected results**, and **best run-times** via `timeit`.
* Includes **inline comments** marking **time & space complexity** at every major step.

If you only want one interview-ready class, stick with the `Solution` (heap-based Dijkstra). It matches the exact requested signature:

```python
class Solution:
    
    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    def minimumCostPath(self, grid):
        # Dijkstra with a min-heap; Time: O(n^2 log n), Space: O(n^2)
        import heapq
        from math import inf

        n = len(grid)
        dist = [[inf]*n for _ in range(n)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        DIRS = ((1,0), (-1,0), (0,1), (0,-1))

        while pq:
            cost, r, c = heapq.heappop(pq)
            if cost != dist[r][c]:
                continue
            if r == n-1 and c == n-1:
                return cost
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    ncost = cost + grid[nr][nc]
                    if ncost < dist[nr][nc]:
                        dist[nr][nc] = ncost
                        heapq.heappush(pq, (ncost, nr, nc))
```

---

## Real-World Use Cases (the big ones)

* **Robot path planning / warehouse routing:** choose the least-cost route on a grid with terrain/traffic costs (non-negative weights), moving in 4 directions.
* **Maps & navigation on raster cost layers:** optimal traversal over cost rasters (e.g., slope/landcover/friction costs in GIS).
* **Network routing / packet costs:** grid or mesh-like networks where link traversal costs are non-negative; Dijkstra or A* directly apply.
* **Game AI pathfinding:** shortest path with tile costs (movement penalties); A* with Manhattan heuristic is the go-to.
