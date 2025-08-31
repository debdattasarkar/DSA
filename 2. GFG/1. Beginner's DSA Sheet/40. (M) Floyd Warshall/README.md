# Floyd Warshall

**Difficulty:** Medium
**Accuracy:** 32.89%
**Submissions:** 222K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

You are given a weighted **directed** graph, represented by an adjacency matrix, `dist[][]` of size `n x n`, where `dist[i][j]` represents the weight of the edge from **node `i` to node `j`**. If there is no direct edge, `dist[i][j]` is set to a large value (i.e., **`10^8`**) to represent infinity.

The graph **may contain negative edge weights**, but it **does not contain any negative weight cycles**.

Your task is to find the **shortest distance between every pair of nodes `i` and `j`** in the graph.

**Note:** Modify the distances for every pair **in place**.

---

## Examples

### Example 1

**Input:**
`dist[][] = [[0, 4, 10^8, 5, 10^8], [10^8, 0, 1, 10^8, 6], [2, 10^8, 0, 3, 10^8], [10^8, 10^8, 1, 0, 2], [1, 10^8, 10^8, 4, 0]]`

**Output:**
`[[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]`

**Explanation:**
Each cell `dist[i][j]` in the output shows the shortest distance from node `i` to node `j`, computed by considering all possible intermediate nodes.

---

### Example 2

**Input:**
`dist[][] = [[0, -1, 2], [1, 0, 10^8], [3, 1, 0]]`

**Output:**
`[[0, -1, 2], [1, 0, 3], [2, 1, 0]]`

**Explanation:**
Each cell `dist[i][j]` in the output shows the shortest distance from node `i` to node `j`, computed by considering all possible intermediate nodes.

* From `2` to `0` shortest distance should be `2` by following path `2 -> 1 -> 0`.
* From `1` to `2` shortest distance should be `3` by following path `1 -> 0 -> 2`.

---

## Expected Complexities

* **Time Complexity:** `O(n^3)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Samsung

---

## Topic Tags

* Dynamic Programming
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* [Floyd Warshall Algorithm Dp 16](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)

---

---

Here’s an interview-ready breakdown for **Floyd–Warshall** (all-pairs shortest paths).

---

## 2) Intuition + step-by-step dry run

We’re given an `n × n` matrix `dist`, where `dist[i][j]` is the edge weight from `i` to `j` (or `10^8` meaning “no edge”).
The graph may have **negative edges** but **no negative cycles**.
Goal: overwrite `dist[i][j]` with the **shortest distance** from `i` to `j`.

### Key idea (DP over intermediates)

For each node `k` (as a potential **intermediate**), try to improve every pair `(i, j)` by going **through `k`**:

```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

Do this for `k = 0..n-1`. After finishing with all `k`, `dist[i][j]` equals the shortest path cost.

* **Time:** `O(n^3)` (three nested loops)
* **Aux space:** `O(1)` (in-place), not counting the input matrix
* **Note:** Always skip additions involving `INF` (here `10^8`) to avoid bogus sums.

### Dry run (Example 2 from the prompt)

Input:

```
dist = [
  [0,  -1,   2],
  [1,   0, 1e8],
  [3,   1,   0]
]
INF = 1e8
```

We iterate `k = 0, 1, 2`.

**k = 0** (allow node 0 as intermediate):

* Check pairs `(i, j)`:

  * (1,2): `dist[1][0]+dist[0][2] = 1 + 2 = 3 < INF` ⇒ update `dist[1][2] = 3`
  * (2,1): `dist[2][0]+dist[0][1] = 3 + (-1) = 2 < 1`? No.
  * Others either don’t improve or involve INF.
    Matrix now:

```
[ [0, -1, 2],
  [1,  0, 3],
  [3,  1, 0] ]
```

**k = 1** (allow node 1 as intermediate):

* (2,0): `dist[2][1]+dist[1][0] = 1 + 1 = 2 < 3` ⇒ `dist[2][0] = 2`
* (0,2): `dist[0][1]+dist[1][2] = -1 + 3 = 2 < 2`? equal → keep 2
  Matrix:

```
[ [0, -1, 2],
  [1,  0, 3],
  [2,  1, 0] ]
```

**k = 2** (allow node 2 as intermediate):

* (1,0): `dist[1][2]+dist[2][0] = 3 + 2 = 5 < 1`? No.
  No further changes.

**Final output**

```
[ [0, -1, 2],
  [1,  0, 3],
  [2,  1, 0] ]
```

which matches the expected result.

---

## 3) Python solutions (expected in interviews)

### A) Standard Floyd–Warshall (in-place, with `INF = 10**8`)

```python
# User function template for Python

class Solution:
    def floydWarshall(self, dist):
        """
        In-place APSP with intermediate node DP.
        Time:  O(n^3)
        Space: O(1) extra (besides the dist matrix we modify)
        """
        n = len(dist)
        INF = 10**8  # sentinel for "no path"

        # k = intermediate node we are allowed to use
        for k in range(n):                                # O(n)
            dk = dist[k]                                  # local ref (micro-optimization)
            for i in range(n):                            # O(n)
                # If i->k is INF, no path via k for this i
                dik = dist[i][k]
                if dik == INF:
                    continue
                row_i = dist[i]
                for j in range(n):                        # O(n)
                    # Skip if k->j is INF
                    dj = dk[j]
                    if dj == INF:
                        continue
                    # Try to improve i->j via k
                    new_cost = dik + dj
                    if new_cost < row_i[j]:
                        row_i[j] = new_cost
        # dist mutated in place
        return dist
```

### B) With path reconstruction (returns `next` matrix for rebuilding a path)

```python
class SolutionWithPath:
    def floydWarshall(self, dist):
        """
        Returns (dist, nxt) where nxt[i][j] is the next vertex after i on
        a shortest path to j (or -1 if j unreachable from i).
        Time:  O(n^3)
        Space: O(n^2) for 'nxt' (needed to reconstruct paths)
        """
        n = len(dist)
        INF = 10**8
        nxt = [[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] != INF:
                    nxt[i][j] = j

        for k in range(n):
            for i in range(n):
                if dist[i][k] == INF:
                    continue
                for j in range(n):
                    if dist[k][j] == INF:
                        continue
                    new_cost = dist[i][k] + dist[k][j]
                    if new_cost < dist[i][j]:
                        dist[i][j] = new_cost
                        nxt[i][j] = nxt[i][k]  # step towards k

        return dist, nxt

    def build_path(self, i, j, nxt):
        """Reconstruct one shortest path i -> j as a list of vertices, or [] if none."""
        if i == j:
            return [i]
        if nxt[i][j] == -1:
            return []
        path = [i]
        while i != j:
            i = nxt[i][j]
            path.append(i)
        return path
```

### C) Baseline alternative (for completeness): run single-source shortest paths for all sources

* If edges are **non-negative**, you could run **Dijkstra `n` times** (`O(n * (E log V))`), which beats `O(n^3)` on sparse graphs.
* With **negative edges** (but no negative cycles), you could run **Bellman–Ford `n` times** (`O(n * V * E)`), which is usually slower than Floyd–Warshall for dense graphs and small `n`.

> In most interviews for this problem, **Solution A** is what they expect.

---

## 4) Likely interviewer Q\&A

**Q1. Why does the triple-loop order use `k` outside?**
Because it’s DP by **allowed intermediates**. After finishing iteration `k`, all paths whose intermediate vertices are from the set `{0..k}` are optimal. By the time `k = n-1`, all nodes are allowed, so distances are final.

**Q2. How do you handle “infinity” safely?**
Use a large sentinel (here `10^8`). Never add with `INF`; check `dist[i][k] != INF` and `dist[k][j] != INF` before doing `dist[i][k] + dist[k][j]`.

**Q3. Can the algorithm detect negative cycles?**
Yes—after running, if any `dist[i][i] < 0`, there’s a negative cycle reachable from `i`. (This problem states there are none, but it’s a common extension.)

**Q4. When is Floyd–Warshall preferable to Dijkstra-from-every-node?**

* When the graph is **dense** and `n` is modest (e.g., `n ≤ 400–600`).
* When there are **negative edges** (no negative cycles).
* When you need **all-pairs** results and possibly **path reconstruction** with a simple implementation.

**Q5. Space complexity?**

* In-place distances only: **`O(1)` extra** beyond the `n×n` matrix you were given.
* With path reconstruction (`nxt`): **`O(n^2)`**.

**Q6. Common pitfalls?**

* Forgetting to skip additions involving `INF`.
* Mutating the matrix but also reading stale values: it’s fine because at step `k` you’re allowed to use `k` as an intermediate; updates within the same `k` are intended.
* Confusing Floyd–Warshall (subsequence of intermediates) with repeated Dijkstra/Bellman–Ford (sources).

---

---

Done! I executed a **full inline Python program** that:

* Implements **Floyd–Warshall** in-place with careful `INF` handling.
* Prints **inputs and outputs** for the two sample matrices.
* Uses `timeit.default_timer()` to print the **TOTAL MAIN RUNTIME**.

```python

# Execute again to show outputs
from typing import List
import timeit

class Solution:
    def floydWarshall(self, dist: List[List[int]]) -> List[List[int]]:
        n = len(dist)
        INF = 10**8
        for k in range(n):
            dist_k = dist[k]
            for i in range(n):
                dik = dist[i][k]
                if dik == INF:
                    continue
                row_i = dist[i]
                for j in range(n):
                    dkj = dist_k[j]
                    if dkj == INF:
                        continue
                    new_cost = dik + dkj
                    if new_cost < row_i[j]:
                        row_i[j] = new_cost
        return dist

def print_matrix(M: List[List[int]]):
    print("[")
    for row in M:
        print(" ", row)
    print("]")

def main():
    sol = Solution()
    print("=== Floyd–Warshall — Demo ===")
    INF = 10**8
    dist1 = [
        [0,   4,  INF, 5,   INF],
        [INF, 0,  1,   INF, 6],
        [2,   INF,0,   3,   INF],
        [INF, INF,1,   0,   2],
        [1,   INF,INF, 4,   0],
    ]
    print("\nInput 1:")
    print_matrix(dist1)
    out1 = sol.floydWarshall(dist1)
    print("Output 1:")
    print_matrix(out1)

    dist2 = [
        [0,  -1, 2],
        [1,   0, INF],
        [3,   1, 0],
    ]
    print("\nInput 2:")
    print_matrix(dist2)
    out2 = sol.floydWarshall(dist2)
    print("Output 2:")
    print_matrix(out2)

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **All-pairs routing tables:** Precompute shortest travel times/latencies between every city/server pair (e.g., logistics networks, data-center fabrics).
* **Game AI pathfinding on small maps:** Instant lookups of path costs between any two nodes after one `O(n^3)` precomputation.
* **Social-network closeness / graph analytics:** Compute pairwise distances (e.g., closeness centrality) on modest-sized graphs.
* **Timetable planning with transfers:** Find best multi-leg connections (allowing negative edges for credits/penalties but no negative cycles).
