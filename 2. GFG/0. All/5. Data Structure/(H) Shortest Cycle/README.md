
---

# 🔁 Shortest Cycle

**Difficulty:** Hard
**Accuracy:** 83.33%
**Submissions:** 6+
**Points:** 8

---

## 📘 Problem Statement

You are given an **undirected connected graph** with `V` vertices numbered from `0` to `V-1` and `E` edges, represented as a 2D array `edges[][]`, where each element `edges[i] = [u, v]` represents an **undirected edge** between vertex `u` and vertex `v`.

Your task is to **find the length of the shortest cycle** in the graph.

If the graph does **not contain any cycle**, return `-1`.

---

### 📍 Definition

* A **cycle** is a path that **starts and ends at the same vertex** without repeating any edge or vertex (except for the start and end vertex).
* The **shortest cycle** is the one with the **minimum number of edges**.

---

## 🧩 Examples

### Example 1

**Input:**

```
V = 7, E = 8
edges[][] = [
  [0, 5], [0, 6], [5, 1], [6, 1],
  [6, 2], [2, 3], [3, 4], [1, 4]
]
```

**Output:**

```
4
```

**Explanation:**
Possible cycles are:

```
0 → 5 → 1 → 6 → 0   (length = 4)
1 → 4 → 3 → 2 → 6 → 1   (length = 5)
```

The smallest one is `0 → 5 → 1 → 6 → 0`,
with **length = 4**.

---

### Example 2

**Input:**

```
V = 7, E = 9
edges[][] = [
  [0, 5], [0, 6], [1, 2], [1, 4], [1, 5],
  [1, 6], [2, 6], [2, 3], [3, 4]
]
```

**Output:**

```
3
```

**Explanation:**
Possible cycles include:

```
1 → 2 → 6 → 1   (length = 3)
1 → 2 → 3 → 4 → 1   (length = 4)
0 → 5 → 1 → 6 → 0   (length = 4)
```

The smallest is `1 → 2 → 6 → 1`,
with **length = 3**.

---

## ⚙️ Constraints

```
1 ≤ V ≤ 10³
0 ≤ E ≤ 10³
0 ≤ edges[i][0], edges[i][1] < V
```

---

## ⏱️ Expected Complexities

| Type                | Complexity     |
| ------------------- | -------------- |
| **Time Complexity** | O(V * (V + E)) |
| **Auxiliary Space** | O(V)           |

---

## 🧵 Topic Tags

`Graph` • `DFS` • `BFS`

---

## 🔗 Related Articles

* [Shortest Cycle in an Undirected Unweighted Graph](https://www.geeksforgeeks.org/shortest-cycle-in-an-undirected-unweighted-graph/)

---

---

Awesome—this is a classic graph pattern. I’ll give you:

1. a clean explanation with a tiny dry run,
2. interview-ready Python in your exact signature (two ways: BFS-per-source and Edge-removal brute),
3. a 60-second recall + high-yield Q&A.

---

## 2) Explanation + step-by-step dry run

### Goal

In an **undirected, unweighted** graph, return the **length (edges)** of the **shortest cycle**. If no cycle exists, return `-1`.

### Key idea (most expected)

Use **BFS from each vertex**. During BFS from a source `s`, if you explore edge `(u, v)` and `v` is already **visited** but **v ≠ parent[u]** (i.e., not the tree edge back), you just found a cycle.
The length of that cycle is:

```
dist[u] + dist[v] + 1
```

because:

* distance from `s` to `u` is `dist[u]`,
* to `v` is `dist[v]`,
* plus the extra edge `(u, v)` to close the loop.

Take the **minimum** over all BFS runs.

Why BFS? In unweighted graphs, BFS layers give **shortest paths** from `s`, so the first time you touch a back/side edge you get the **shortest** cycle involving that frontier.

> Complexity: doing a fresh BFS from every vertex gives **O(V·(V+E))**, which matches the given expected time for constraints up to 1e3.

---

### Tiny dry run (from Example 2)

```
V=7
edges = [[0,5],[0,6],[1,2],[1,4],[1,5],[1,6],[2,6],[2,3],[3,4]]
Shortest cycle is 1–2–6–1 (length 3).
```

* Start BFS at `s=1`:

  * dist[1]=0; queue: [1]
  * Pop 1 → neighbors {2,4,5,6} → set dist=1, parent=1; queue: [2,4,5,6]
  * Pop 2 → neighbors {1,6,3}

    * 1 is parent → ignore
    * 6 is **visited and not parent** → cycle length = dist[2] (1) + dist[6] (1) + 1 = **3** → update answer = 3 (can’t get smaller than 3 in simple graphs).
      Stop early if you want since 3 is minimal possible for simple cycles.

---

## 3) Python solutions (brute → optimal), your requested signature

```python
from collections import deque, defaultdict
from typing import List

class Solution:
    def shortCycle(self, V: int, edges: List[List[int]]) -> int:
        """
        BFS-from-each-vertex (most expected).
        Time  : O(V * (V + E))   -- fresh BFS per source
        Space : O(V + E)         -- adjacency + BFS arrays
        """
        # Build adjacency list: O(V + E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        INF = 10**9
        best = INF

        # BFS from every node as source
        for s in range(V):
            # Fresh structures per BFS to avoid cross-contamination
            dist   = [-1] * V
            parent = [-1] * V
            q = deque([s])
            dist[s] = 0

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        # Tree edge
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:
                        # Found a non-parent visited neighbor -> cycle
                        # Length = dist[u] + dist[v] + 1
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < best:
                            best = cycle_len
                # Optional micro-optimization: early stop if best==3
                # if best == 3: return 3

        return -1 if best == INF else best
```

### Why this is preferred in interviews

* Uses only BFS + parent tracking—simple and robust.
* Matches expected complexity from the problem statement.
* Easy to reason about and prove correctness.

---

### Alternative “brute” (edge-removal idea)

For each **edge (u, v)**:

* Temporarily **remove** edge `(u, v)`.
* Compute **shortest distance** `d(u, v)` with BFS.
* If reachable, potential cycle length = `d(u, v) + 1` (re-adding the removed edge closes that cycle).
* Restore the edge; take the global minimum.

This is straightforward but usually **slower** in practice (still `O(E·(V+E))`).

```python
from collections import deque, defaultdict
from typing import List

class SolutionEdgeRemove:
    def shortCycle(self, V: int, edges: List[List[int]]) -> int:
        """
        Brute-ish: For each edge (u,v), remove it, BFS distance(u,v), then +1.
        Time  : O(E * (V + E))
        Space : O(V + E)
        """
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        INF = 10**9
        best = INF

        def bfs_dist(a: int, b: int) -> int:
            dist = [-1] * V
            q = deque([a])
            dist[a] = 0
            while q:
                x = q.popleft()
                if x == b:
                    return dist[x]
                for y in graph[x]:
                    if dist[y] == -1:
                        dist[y] = dist[x] + 1
                        q.append(y)
            return INF

        for u, v in edges:
            # Temporarily remove edge u<->v
            graph[u].remove(v)
            graph[v].remove(u)

            d = bfs_dist(u, v)
            if d != INF:
                best = min(best, d + 1)

            # Restore
            graph[u].add(v)
            graph[v].add(u)

        return -1 if best == INF else best
```

---

## 4) Interview quick-recall + Q&A

### 10-second mnemonic

**“BFS + parent check → dist[u] + dist[v] + 1”**

* BFS from each node
* If you see an already-visited neighbor that **isn’t your parent**, you closed a cycle
* Cycle length = distances to `u` and `v` plus the closing edge

### 60-second recall routine

1. **Build adjacency** `O(V+E)`.
2. **Loop sources s=0..V-1**:

   * fresh `dist`, `parent`, `queue`
   * BFS:

     * Tree edge: set `dist[v]=dist[u]+1`, `parent[v]=u`
     * Back/side edge: `if parent[u] != v`: `ans=min(ans, dist[u]+dist[v]+1)`
3. Return `ans` or `-1`.

### High-yield Q&A

**Q1. Why does BFS give shortest cycle?**
Because in unweighted graphs BFS explores in increasing distance layers. For any cycle through `s`, the first cross-edge between two visited nodes yields the **minimum possible sum of depths** → shortest cycle length.

**Q2. Why check `parent[u] != v`?**
To avoid counting the **tree edge** you just came from; we only want **non-tree** edges that close a loop.

**Q3. Complexity?**
Each BFS is `O(V+E)`. Running it from all vertices → `O(V·(V+E))`. Aux space `O(V)` per BFS.

**Q4. Can we stop early?**
Yes—if you ever find a **triangle (3)**, that’s the minimum possible simple cycle; you can return 3 immediately.

**Q5. Works for directed graphs?**
Not directly. For directed graphs, shortest directed cycle needs different handling (e.g., BFS per node on directed edges or Johnson’s algorithm variants).

**Q6. Can DFS do it?**
You can detect cycles with DFS, but extracting the **shortest** cycle is trickier; BFS is the standard approach for shortest cycles in unweighted graphs.

---

---

Great—here are (5) crisp, interview-friendly use cases and a complete, runnable Python script that solves **Shortest Cycle in an undirected, unweighted graph** with timings.

---

## 5) Real-World Use Cases (easy to relate)

1. **Network health (routing loops)**
   Detect the *smallest* loop of routers/switches to locate misconfigurations or fast-reroute rings.

2. **Social graph analysis**
   Shortest cycle ≈ smallest “closed friend group” (triangles/4-cycles) for community detection and transitivity studies.

3. **Fraud/risk in transaction graphs**
   Minimal money-flow loop can indicate wash-trading or circular transfers.

4. **Road/utility grids**
   Smallest loop helps in planning inspections or redundancy circuits with minimal edges.

5. **Knowledge graphs**
   Find small contradictory loops (A→B→C→A) pointing to data inconsistencies.

---

## 6) Full Program (BFS-per-source + optional edge-removal, with timings)

```python
#!/usr/bin/env python3
"""
Shortest Cycle in an Undirected, Unweighted Graph
-------------------------------------------------
Two implementations:
  1) BFS-from-each-vertex (most expected): O(V * (V + E)) time, O(V + E) space
  2) Edge-removal (educational):           O(E * (V + E)) time, O(V + E) space

The script:
  * Builds adjacency
  * Runs both algorithms on sample inputs
  * Prints outputs
  * Measures single-run and averaged runtimes (perf_counter + timeit)
"""

from collections import deque, defaultdict
from time import perf_counter
import timeit
from typing import List, Tuple


# -----------------------------------------------
# 1) Interview-expected solution: BFS per source
# -----------------------------------------------
class Solution:
    def shortCycle(self, V: int, edges: List[List[int]]) -> int:
        """
        For each source 's', run BFS. When exploring edge (u, v):
          - If 'v' is unvisited -> tree edge: set dist[v], parent[v], enqueue
          - Else if parent[u] != v -> found a cross/back edge that closes a cycle
                cycle_len = dist[u] + dist[v] + 1
                minimize answer

        Complexity per BFS: O(V + E), repeated V times -> O(V * (V + E))
        Space: O(V + E) adjacency + O(V) per BFS arrays
        """
        # Build adjacency list: O(V + E)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        INF = 10**9
        best = INF

        for s in range(V):
            # Fresh arrays per source; O(V)
            dist   = [-1] * V
            parent = [-1] * V
            q = deque([s])
            dist[s] = 0

            # BFS from source s; total edges processed O(V + E)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        # Tree edge: visit v
                        dist[v] = dist[u] + 1       # O(1)
                        parent[v] = u               # O(1)
                        q.append(v)
                    elif parent[u] != v:
                        # Non-parent visited neighbor -> cycle
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < best:
                            best = cycle_len
                            # Early exit possible: 3 is minimal simple cycle
                            # if best == 3: return 3

        return -1 if best == INF else best


# -----------------------------------------------------
# 2) Educational alternative: edge removal + BFS
# -----------------------------------------------------
class SolutionEdgeRemove:
    def shortCycle(self, V: int, edges: List[List[int]]) -> int:
        """
        For each edge (u, v):
          - Remove it
          - BFS shortest distance d(u, v)
          - If reachable, cycle = d + 1 (restore the removed edge)
        Time  : O(E * (V + E))
        Space : O(V + E)
        """
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        INF = 10**9
        best = INF

        def bfs_dist(a: int, b: int) -> int:
            dist = [-1] * V
            q = deque([a])
            dist[a] = 0
            while q:
                x = q.popleft()
                if x == b:
                    return dist[x]
                for y in graph[x]:
                    if dist[y] == -1:
                        dist[y] = dist[x] + 1
                        q.append(y)
            return INF

        for u, v in edges:
            # Remove edge (u, v) temporarily; O(1) average
            graph[u].remove(v)
            graph[v].remove(u)

            d = bfs_dist(u, v)  # O(V + E)
            if d != INF:
                best = min(best, d + 1)

            # Restore edge
            graph[u].add(v)
            graph[v].add(u)

        return -1 if best == INF else best


# -------------------------
# Utilities for pretty I/O
# -------------------------
def run_case(name: str, V: int, edges: List[Tuple[int, int]], expected: int):
    print(f"\n-- {name} --")
    print(f"V = {V}")
    print("edges =", edges)

    sol = Solution()
    t0 = perf_counter()
    ans = sol.shortCycle(V, edges)
    t1 = perf_counter()

    print(f"Shortest cycle (BFS-per-source): {ans}   [single-run {(t1 - t0)*1e6:.2f} µs]")
    print(f"Expected                         : {expected}")

    # Edge-removal (for comparison; optional)
    sol2 = SolutionEdgeRemove()
    t2 = perf_counter()
    ans2 = sol2.shortCycle(V, edges)
    t3 = perf_counter()
    print(f"Edge-removal result             : {ans2}   [single-run {(t3 - t2)*1e6:.2f} µs]")

    # Averaged timings (more stable)
    def call_bfs():
        sol.shortCycle(V, edges)

    avg_bfs = timeit.timeit(call_bfs, number=200) / 200
    print(f"Avg over 200 runs (BFS-per-source): {avg_bfs*1e6:.2f} µs/run")


# -----------
# Demo / Main
# -----------
def main():
    # Example 1 from prompt (answer = 4)
    V1 = 7
    edges1 = [(0,5),(0,6),(5,1),(6,1),(6,2),(2,3),(3,4),(1,4)]
    run_case("Example 1", V1, edges1, expected=4)

    # Example 2 from prompt (answer = 3)
    V2 = 7
    edges2 = [(0,5),(0,6),(1,2),(1,4),(1,5),(1,6),(2,6),(2,3),(3,4)]
    run_case("Example 2", V2, edges2, expected=3)

    # Another tiny case: no cycle
    V3 = 4
    edges3 = [(0,1),(1,2),(2,3)]
    run_case("No Cycle (path graph)", V3, edges3, expected=-1)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==== TOTAL PROGRAM RUNTIME: {(end - start):.6f} s ====")
```

### What you’ll see when you run it

* For each sample: the **shortest cycle length**, the **expected** value, and **timings** (single run + average).
* Clear, inline comments indicating **time/space complexity** for each piece of logic—perfect for interviews.
