
---

# **Path With Minimum Effort**

**Difficulty:** Medium
**Accuracy:** 53.13%
**Submissions:** 54K+
**Points:** 4
**Average Time:** 25m

You are given a 2D array `mat[][]` of size `n * m`. Your task is to find the **minimum possible path cost** from the top-left cell `(0, 0)` to the bottom-right cell `(n-1, m-1)` by moving **up, down, left, or right** between adjacent cells.

> **Note:**
> The cost of a path is defined as the **maximum absolute difference** between the values of any two consecutive cells along that path.

---

## **Examples**

### **Example 1**

**Input:**
`mat[][] = [[7, 2, 6, 5],`
`             [3, 1, 10, 8]]`

**Output:**
`4`

**Explanation:**
The route of:
`7 → 3 → 1 → 2 → 6 → 5 → 8`
has a minimum value of maximum absolute difference between any two consecutive cells in the path, i.e., **4**.

Illustration:

```
7  →  2  →  6  →  5
↓                 ↑
3  →  1 → 10 →  8
```

---

### **Example 2**

**Input:**
`mat[][] = [[2, 2, 2, 1],`
`             [8, 1, 2, 7],`
`             [2, 2, 2, 8],`
`             [2, 1, 4, 7],`
`             [2, 2, 2, 2]]`

**Output:**
`0`

**Explanation:**
The route
`2 → 2 → 2 → 2 → 2 → 2 → 2 → 2 → 2 → 2`
has a minimum value of maximum absolute difference between any two consecutive cells along the route, i.e., **0**.

Illustration:

```
2 → 2 → 2 → 2 → 1
↓               ↓
8 → 1 → 2 → 7
↓               ↓
2 → 2 → 2 → 8
↓               ↓
2 → 1 → 4 → 7
↓               ↓
2 → 2 → 2 → 2
```

---

## **Constraints**

* `1 ≤ n, m ≤ 100`
* `0 ≤ mat[i][j] ≤ 10⁶`

---

## **Expected Complexities**

* **Time Complexity:**
  `O(n * m * log(n * m))`
* **Auxiliary Space:**
  `O(n * m)`

---

## **Company Tags**

* Bloomberg
* Amazon
* Microsoft
* Google

---

## **Topic Tags**

* Graph
* DFS
* BFS

---

## **Related Articles**

* [**Path With Smallest Difference Between Consecutive Cells Path With Minimum Effort**](https://www.geeksforgeeks.org/path-with-smallest-difference-between-consecutive-cells-path-with-minimum-effort/)

---

---

I’ll go in this order:

1. Intuition + explanation of the problem
2. Step-by-step dry run (with Dijkstra / min-heap idea)
3. Python codes

   * Brute-force DFS (for understanding)
   * Optimized Dijkstra (in the requested `class Solution`)
   * Alternate optimized: Binary search + BFS
4. Interview “cheat sheet”: how to recall + likely Q&A

---

## 1. Problem explanation (in your own words)

We have an `n x m` grid `mat` with non-negative integers.
We start at the **top-left** cell `(0,0)` and want to reach the **bottom-right** cell `(n-1,m-1)`.

We can move **up, down, left, right** to adjacent cells.

For any *single path*:

* Look at all consecutive cell pairs on this path.
* For each pair, compute `abs(value1 - value2)`.
* Take the **maximum** of these values.
  This is the **cost of that path**.

Our goal: among all possible paths, choose one whose **path cost** (maximum edge difference along it) is **minimum possible**.

This is a **minimax path** problem:

* Each move (edge) has a “effort” = `abs(a - b)`.
* For each path, take `max(edge efforts)` on that path.
* We want the path minimizing this maximum.

---

## 2. Step-by-step dry run (Dijkstra / min-heap idea)

We’ll use the example:

```text
mat = [
    [7, 2, 6, 5],
    [3, 1,10, 8]
]
```

Grid indices:

* `(0,0)=7, (0,1)=2, (0,2)=6, (0,3)=5`
* `(1,0)=3, (1,1)=1, (1,2)=10,(1,3)=8`

### Idea of the algorithm (Dijkstra variant)

Think of each cell as a **node** in a graph.
Edges connect to up/down/left/right neighbors with weight:

```python
weight = abs(mat[current] - mat[neighbor])
```

We don’t want to minimize the **sum** of weights.
We want to minimize the **maximum weight along the path**.

So in Dijkstra, instead of:

```text
new_cost = current_cost + edge_weight
```

we use:

```text
new_cost = max(current_cost, edge_weight)
```

The priority queue (min-heap) always expands the cell with the **current smallest “max difference so far”**.

Let `cost[r][c]` = minimum possible path cost to reach `(r,c)` found so far.

---

### Initialization

* `cost` grid = infinity everywhere
* `cost[0][0] = 0` (no move, so max difference so far = 0)

Min-heap holds `(cost, r, c)`:

* Start with heap = `[(0, 0, 0)]`

---

### Step 1: Pop `(0, 0, 0)`  (cell value 7)

Neighbors of `(0,0)`:

1. Down `(1,0)` value 3

   * Edge diff = `abs(7 - 3) = 4`
   * new_cost = `max(0, 4) = 4`
   * `cost[1][0]` was `inf`, now becomes `4`
   * Push `(4, 1, 0)` to heap

2. Right `(0,1)` value 2

   * Edge diff = `abs(7 - 2) = 5`
   * new_cost = `max(0, 5) = 5`
   * `cost[0][1]` = `5`
   * Push `(5, 0, 1)` to heap

Heap now: `[(4, 1, 0), (5, 0, 1)]`

---

### Step 2: Pop smallest cost from heap → `(4, 1, 0)` (value 3)

Neighbors of `(1,0)`:

1. Up `(0,0)` already best cost 0 – going back is useless.

2. Right `(1,1)` value 1

   * Edge diff = `abs(3 - 1) = 2`
   * new_cost = `max(4, 2) = 4`
     (max along path 7→3→1 is still 4 because 7→3 was 4)
   * `cost[1][1]` was `inf`, update to `4`
   * Push `(4, 1, 1)` to heap

3. Down: out of grid.

Heap now: `[(4, 1, 1), (5, 0, 1)]`

---

### Step 3: Pop smallest → `(4, 1, 1)` (value 1)

Neighbors of `(1,1)`:

1. Left `(1,0)` (already cost 4, going back won’t improve).

2. Up `(0,1)` value 2

   * Edge diff = `abs(1 - 2) = 1`
   * new_cost = `max(4, 1) = 4`
   * `cost[0][1]` currently 5 → **better path found** with cost 4
   * Update `cost[0][1] = 4` and push `(4, 0, 1)`

3. Right `(1,2)` value 10

   * Edge diff = `abs(1 - 10) = 9`
   * new_cost = `max(4, 9) = 9`
   * `cost[1][2] = 9`
   * Push `(9, 1, 2)`

Heap now: `[(4, 0, 1), (5, 0, 1), (9, 1, 2)]`
(Note: there are two entries for `(0,1)`; only the smallest matters.)

---

### Step 4: Pop smallest → `(4, 0, 1)` (value 2)

Check neighbors:

1. Left `(0,0)` – no improvement

2. Right `(0,2)` value 6

   * Edge diff = `abs(2 - 6) = 4`
   * new_cost = `max(4,4) = 4`
   * `cost[0][2]` was `inf` → becomes `4`
   * Push `(4, 0, 2)`

3. Down `(1,1)` already cost 4, same

Heap: `[(4, 0, 2), (5, 0, 1), (9, 1, 2)]`

---

### Step 5: Pop smallest → `(4, 0, 2)` (value 6)

Neighbors:

1. Left `(0,1)` (cost 4 already)

2. Right `(0,3)` value 5

   * Edge diff = `abs(6 - 5) = 1`
   * new_cost = `max(4,1) = 4`
   * `cost[0][3]` becomes 4
   * Push `(4, 0, 3)`

3. Down `(1,2)` value 10

   * Edge diff = `abs(6 - 10) = 4`
   * new_cost = `max(4,4)=4`
   * `cost[1][2]` currently 9 → update to 4
   * Push `(4, 1, 2)`

Heap: `[(4, 0, 3), (4, 1, 2), (9, 1, 2), (5, 0, 1)]`

---

### Step 6: Pop smallest → `(4, 0, 3)` (value 5)

Neighbors:

1. Left `(0,2)` (cost 4)
2. Down `(1,3)` value 8

   * Edge diff = `abs(5 - 8) = 3`
   * new_cost = `max(4,3) = 4`
   * `cost[1][3]` becomes 4
   * Push `(4, 1, 3)`

Heap: `[(4, 1, 2), (4, 1, 3), (9, 1, 2), (5, 0, 1)]`

---

### Step 7: Pop smallest → `(4, 1, 2)` or `(4, 1, 3)` (both cost 4)

Eventually we pop `(4, 1, 3)` which is the **bottom-right cell**.

Because the heap always pops the **smallest cost** first, the first time we pop `(n-1,m-1)` its cost is already the **minimum possible path cost**.

So the answer is **4**, which exactly matches the example.

---

## 3. Python Codes

### 3.1 Brute-force DFS (for understanding, NOT for large constraints)

* Explore all possible paths using DFS.
* Track `current_max_diff` along the path.
* At the end cell, update global `best_answer`.
* Optionally prune paths whose `current_max_diff` is already ≥ `best_answer`.

Time complexity is exponential → **TLE** for big `n, m`; but it helps conceptually.

```python
class SolutionBrute:
    def minCostPath(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Global best answer (minimized maximum difference)
        self.best_cost = float('inf')
        
        # Visited set to avoid cycles
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, current_max_diff):
            # If we already have a better answer, prune this path
            if current_max_diff >= self.best_cost:
                return
            
            if r == rows - 1 and c == cols - 1:
                # Reached destination – update best_cost
                self.best_cost = min(self.best_cost, current_max_diff)
                return
            
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    # Edge effort between current and neighbor
                    edge_diff = abs(mat[r][c] - mat[nr][nc])
                    # Max diff so far on this path if we go to neighbor
                    new_max_diff = max(current_max_diff, edge_diff)
                    dfs(nr, nc, new_max_diff)
            
            visited[r][c] = False  # backtrack
        
        dfs(0, 0, 0)
        return self.best_cost
```

> Again: this is *not* suitable for production interview constraints, but good to understand the minimax nature of the problem.

---

### 3.2 Optimized – Dijkstra with modified cost (recommended interview solution)

This is the one you should give in most interviews.

```python
import heapq

class Solution:
    def minCostPath(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # cost[r][c] := minimum possible path cost (minimized maximum diff)
        # to reach cell (r, c) from (0, 0)
        cost = [[float('inf')] * cols for _ in range(rows)]
        cost[0][0] = 0
        
        # Min-heap of (current_cost, row, col)
        min_heap = [(0, 0, 0)]
        
        # 4-directional movement
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while min_heap:
            current_cost, r, c = heapq.heappop(min_heap)
            
            # If this entry is outdated (we already found a better cost), skip it
            if current_cost > cost[r][c]:
                continue
            
            # If we reached the destination, current_cost is the answer
            if r == rows - 1 and c == cols - 1:
                return current_cost
            
            # Relax all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Edge effort between current cell and neighbor
                    edge_diff = abs(mat[r][c] - mat[nr][nc])
                    
                    # If we go to neighbor through this path, the maximum difference
                    # on that path becomes max(current path cost, this edge's diff)
                    new_cost = max(current_cost, edge_diff)
                    
                    # Standard Dijkstra relaxation with our modified cost definition
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        heapq.heappush(min_heap, (new_cost, nr, nc))
        
        # For safety, though we should have returned earlier
        return cost[rows - 1][cols - 1]
```

**Time complexity**

* Each cell is pushed at most a few times into a heap of size `O(n*m)`.
* Complexity ~ `O((n*m) * log(n*m))`
  which matches the expected time complexity.

**Space complexity**

* `cost` array + heap = `O(n*m)`.

---

### 3.3 Alternate Optimized – Binary Search on Answer + BFS

Observation:

* Let `X` be a candidate maximum allowed difference.
* Ask: *“Is there some path from start to end such that every step has difference ≤ X?”*
* If answer is **Yes** for some `X`, then it’s also Yes for any `Y > X`.
  (Because allowing larger differences can only make it easier.)
* So the predicate “reachable with max diff ≤ X” is **monotonic**.
  That’s perfect for **binary search**.

Algorithm:

1. Binary search on `X` in range `[0, max_possible_diff]`.
   We can use `0` to `max_val - min_val` in the matrix.
2. For a fixed `X`, run BFS/DFS on the grid, but only traverse edges
   where `abs(diff) ≤ X`.
3. If we can reach the bottom-right, then `X` is feasible → move left (try smaller).
   Otherwise, move right (increase `X`).

Code:

```python
from collections import deque

class SolutionBinarySearch:
    def minCostPath(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # Precompute global minimum and maximum values in the matrix
        min_val = float('inf')
        max_val = float('-inf')
        for r in range(rows):
            for c in range(cols):
                val = mat[r][c]
                min_val = min(min_val, val)
                max_val = max(max_val, val)
        
        # Allowed max difference lies between 0 and max_val - min_val
        low = 0
        high = max_val - min_val
        answer = high
        
        # Directions for BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def can_reach_with_max_diff(limit):
            """Return True if we can reach (rows-1, cols-1) from (0,0)
            such that every step's abs difference <= limit."""
            visited = [[False] * cols for _ in range(rows)]
            queue = deque()
            queue.append((0, 0))
            visited[0][0] = True
            
            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if abs(mat[r][c] - mat[nr][nc]) <= limit:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            return False
        
        # Standard binary search on the minimal feasible limit
        while low <= high:
            mid = (low + high) // 2
            if can_reach_with_max_diff(mid):
                answer = mid           # mid is feasible
                high = mid - 1         # try smaller value
            else:
                low = mid + 1          # need larger difference
        
        return answer
```

Complexity:

* BFS/DFS each run: `O(n*m)`
* Binary search iterations: `O(log(MaxValueDiff))`
  (MaxValueDiff ≤ 1e6, so ~20 iterations)
* Overall: `O((n*m) * log(MaxValueDiff))`, comparable to Dijkstra.

---

## 4. Interview Cheat Sheet — How to remember & what they may ask

### 4.1 How to recall quickly in an interview

**Mental steps:**

1. **Rephrase the problem**:
   “Grid, can move in 4 directions, each step cost is absolute difference, path cost is max difference along path. Need to minimize that max.”

2. **Recognize pattern**:

   > “Minimize the maximum edge weight along a path” = **minimax path**.

3. **Link to known techniques**:

   * Minimax path →

     * Dijkstra variant (cost = max along the path), or
     * Binary search on answer + BFS, or
     * MST (Kruskal) alternative (not required, but nice fact).

4. **Choose the easiest to implement under pressure**:

   * Dijkstra with `new_cost = max(current_cost, edge_weight)`
     is usually the **cleanest** and very acceptable in interviews.

5. **Outline before coding** (say it aloud):

   * “I’ll model each cell as a node, edges to its neighbors.”
   * “I’ll run Dijkstra, but path cost is maximum edge instead of sum.”
   * “Complexity: O(n*m log(n*m)).”

Once you say this confidently, the interviewer usually nods and lets you code.

---

### 4.2 Common questions & good answers

---

**Q1. Why does Dijkstra work here? It usually minimizes sum of weights, not max.**

**A:**
Dijkstra works as long as:

1. Edge weights are **non-negative** (here, absolute differences).
2. The “cost” function is **monotonic along a path**: when we extend a path, its cost does not decrease.

Here, when we extend a path, the path cost is:

```text
new_cost = max(old_cost, edge_weight)
```

This is **monotonic non-decreasing**.
So once we pop a node with the smallest cost from the min-heap, we know we have already found the **minimal possible** cost for that node. Therefore the standard Dijkstra reasoning applies.

---

**Q2. What is the time and space complexity of your solution?**

**A:**
Let `V = n * m` be number of cells, and `E ≈ 4 * V` edges (each cell has up to 4 neighbors).

* Time: `O(E log V)` = `O(n * m * log(n * m))` using a binary heap.
* Space: `O(V)` for distance array + heap.

---

**Q3. Can you do it without Dijkstra?**

**A:**
Yes, two main alternatives:

1. **Binary search on the answer + BFS/DFS**:

   * For a fixed max difference `X`, check via BFS whether we can reach the end using only edges with `diff ≤ X`.
   * The predicate “reachable with max difference ≤ X” is monotonic; so we can binary search over `X`.

2. **Minimum Spanning Tree (MST) idea**:

   * Build edges between adjacent cells with weight `diff`.
   * Sort edges and build MST using Kruskal.
   * The unique path in the MST between start and end minimizes the maximum edge weight.
   * The answer is then the largest edge weight on that path.
     (Though implementation is a bit more involved because you must detect when start and end become connected.)

---

**Q4. Why is this problem tagged with BFS/DFS as well?**

**A:**
Because in the **binary search approach**, for each trial maximum `X` we do a **BFS/DFS exploration** of the grid restricted to edges with `diff ≤ X`. So BFS/DFS is still a core component of one optimal solution.

---

**Q5. Are there any edge cases you considered?**

**A:**

* **Single cell** `n = m = 1`: there is no move; cost = 0 (our initialization handles that).
* Grids with very large values (up to 1e6) → using `abs()` fits easily within Python’s `int`.
* Multiple paths with same cost → we only need the minimal cost, not the path itself.
* Non-square grids (e.g., `1 x m` or `n x 1`) → Dijkstra/BFS logic is identical.

---

**Q6. How would you modify your code to also return the actual path, not just the cost?**

**A:**
Keep a **`parent`** pointer for each cell:

* When we relax neighbor `(nr, nc)` from `(r, c)`, we set `parent[nr][nc] = (r, c)` if `new_cost < cost[nr][nc]`.
* After the algorithm finishes, we backtrack from `(n-1,m-1)` to `(0,0)` using `parent` to reconstruct the path.

---

---

Alright, let’s wrap this up nicely.

---

## 5. Real-World Use Cases (easy to talk about in an interview)

You can mention **2–3** of these, and link them to the “minimize the maximum step/effort” idea.

### a) Hiking / Terrain Navigation (elevation changes)

* Grid cells = points on a map, value = elevation.
* Moving between cells has “effort” = elevation difference.
* A hiker with knee problems doesn’t care about total climb as much as **the steepest step**.
* We want a path where the **steepest segment is as gentle as possible** → exactly minimizing the **maximum** elevation difference.

### b) Robotics on Uneven Floors or Stairs

* A wheeled robot has a **max safe bump/step height** it can handle.
* Grid cells = floor patches, value = floor height.
* Moving between adjacent cells has height difference; we want a path where robot’s largest bump is minimized so it **never hits an unsafe bump**.

### c) Network Routing with Worst-Case Latency

* Nodes = servers/routers; edges have latency.
* Some applications care about **worst hop latency** along a route (e.g., jitter-sensitive streaming).
* Instead of minimizing total latency, we minimize the **largest single hop latency** in the route → same minimax path pattern.

### d) Temperature / Stress Limits in a Manufacturing Line

* Grid = stages or positions on a line; value = temperature or stress level.
* Moving product between stages with big jumps in temperature/stress is risky.
* We want a path of operations where the **largest jump** between consecutive stages is minimized.

These are easy to explain and map directly to the problem’s definition.

---

## 6. Full Python Program (with time measurement & complexity comments)

This is a **complete file** you can show in an interview or run locally.

Key points:

* Uses **Dijkstra-style minimax path** (the optimized solution we discussed).
* Uses `timeit.default_timer()` to measure total run time.
* Includes inline comments with **time/space complexity** notes.

```python
"""
Path With Minimum Effort (Minimax Path in a Grid)

We are given a 2D matrix 'mat' of size n x m.
We start at (0, 0) and want to reach (n-1, m-1).
We can move up, down, left, or right.

Cost of a path = maximum absolute difference between values of any
two consecutive cells along that path.

Goal: Minimize this path cost.

Optimized solution:
    - Dijkstra's algorithm variant
    - Instead of summing edge weights, we keep the maximum edge on the path so far.

Time Complexity:  O((n * m) * log(n * m))
Space Complexity: O(n * m)
"""

import heapq             # for priority queue (min-heap)
from timeit import default_timer as timer  # for timing the full run


class Solution:
    def minCostPath(self, mat):
        """
        Return the minimum possible path cost from top-left to bottom-right.

        :param mat: List[List[int]] - 2D grid of non-negative integers
        :return: int - minimum possible path cost

        Overall:
        --------
        Time Complexity:  O((n * m) * log(n * m))
            - Each cell can enter the heap multiple times, but effectively
              we process at most O(n*m) * log(n*m) heap operations.
        Space Complexity: O(n * m)
            - cost matrix + heap storage in worst case
        """
        rows = len(mat)
        cols = len(mat[0])

        # cost[r][c] will store the minimum achievable "max edge diff"
        # along any path from (0,0) to (r,c) found so far.
        #
        # Time:  O(n * m) to initialize
        # Space: O(n * m) for the cost matrix
        cost = [[float('inf')] * cols for _ in range(rows)]
        cost[0][0] = 0  # starting cell has cost 0 (no step taken yet)

        # Min-heap storing tuples of (current_cost, row, col).
        # At each step, we pop the cell with the smallest "max diff so far".
        #
        # Heap operations:
        #   - push/pop: O(log(n * m)) per operation
        #   - up to O(n * m) pushes in practice
        min_heap = [(0, 0, 0)]

        # Possible moves: down, up, right, left (4-directional)
        # Time per expansion: O(1), constant number of neighbors
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            # Pop the cell with smallest known path cost so far
            current_cost, r, c = heapq.heappop(min_heap)  # O(log(n * m))

            # If this heap entry is outdated (we found a better path later), skip it.
            # Time: O(1). This check avoids unnecessary neighbor relaxations.
            if current_cost > cost[r][c]:
                continue

            # If we reached bottom-right, by Dijkstra's property,
            # current_cost is the minimum possible path cost.
            if r == rows - 1 and c == cols - 1:
                return current_cost

            # Relax all 4 valid neighbors.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Bound check: O(1)
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Edge effort between current cell and neighbor cell.
                    # Time: O(1)
                    edge_diff = abs(mat[r][c] - mat[nr][nc])

                    # New path cost to neighbor = max of
                    # current path cost and this edge's diff.
                    # This is the key "minimax" twist.
                    new_cost = max(current_cost, edge_diff)  # O(1)

                    # Relaxation step (like Dijkstra):
                    # If going through (r,c) gives a smaller max-diff to (nr,nc), update it.
                    #
                    # Time: O(1) for comparison and assignment,
                    #       plus O(log(n*m)) for pushing into heap.
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        heapq.heappush(min_heap, (new_cost, nr, nc))  # O(log(n * m))

        # In theory, we should have returned from inside the loop.
        # But as a safe fallback, return the stored cost at destination.
        return cost[rows - 1][cols - 1]


if __name__ == "__main__":
    # Example input grid (from the problem statement)
    example_mat = [
        [7, 2, 6, 5],
        [3, 1, 10, 8]
    ]

    # Print input for clarity
    print("Input matrix:")
    for row in example_mat:
        print(row)

    # Measure total run time of the algorithm for this input.
    start_time = timer()
    solution = Solution()
    result = solution.minCostPath(example_mat)
    end_time = timer()

    # Output result
    print("\nMinimum possible path cost:", result)

    # Output elapsed time in seconds (this will be very small for such a tiny input)
    elapsed = end_time - start_time
    print("Elapsed time (seconds):", elapsed)
```

### What this prints (example)

If you run the program above, you’ll see something like:

```text
Input matrix:
[7, 2, 6, 5]
[3, 1, 10, 8]

Minimum possible path cost: 4
Elapsed time (seconds): 3.2e-05
```

(Your actual elapsed time will vary, but it will be tiny for such a small grid.)
