
---

# 🧩 Hamiltonian Path

**Difficulty:** Medium
**Accuracy:** 40.8%
**Submissions:** 45K+
**Points:** 4

---

### 🧠 Problem Statement

Given an **undirected graph** with `n` vertices and `m` edges, your task is to determine if a **Hamiltonian Path** exists in the graph.

A **Hamiltonian path** is a path in an undirected graph that visits **each vertex exactly once**.

---

### 📘 Input Format

You are provided with the following:

* `n`: The number of vertices in the graph.
* `m`: The number of edges in the graph.
* `edges[][]`: A 2D list where each element `edges[i]` represents an edge between two vertices `edges[i][0]` and `edges[i][1]`.

---

### 🧾 Examples

#### **Example 1**

**Input:**

```
n = 4, m = 4  
edges[][] = { {1, 2}, {2, 3}, {3, 4}, {2, 4} }
```

**Output:**

```
1
```

**Explanation:**
There is a Hamiltonian path:

```
1 -> 2 -> 3 -> 4
```

---

#### **Example 2**

**Input:**

```
n = 4, m = 3  
edges[][] = { {1, 2}, {2, 3}, {2, 4} }
```

**Output:**

```
0
```

**Explanation:**
It can be proved that there is **no Hamiltonian path** in the given graph.

---

### ⚙️ Constraints

```
1 ≤ n ≤ 10  
1 ≤ m ≤ 15  
Size of edges[i] = 2  
1 ≤ edges[i][0], edges[i][1] ≤ n
```

---

### 🧮 Expected Complexities

* **Time Complexity:** O(n!)
* **Auxiliary Space:** O(n + m)

---

### 🏢 Company Tags

* **Amazon**

---

### 🧩 Topic Tags

* DFS
* Graph
* Backtracking
* Data Structures
* Algorithms

---

### 🔗 Related Articles

* [Hamiltonian Cycle](https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/)

---

### 🧭 Summary

This problem focuses on identifying whether a Hamiltonian Path exists in an undirected graph — a path that visits **every vertex exactly once** without repetition. It uses **Depth First Search (DFS)** and **Backtracking** to explore all possible paths, marking visited nodes and backtracking when dead ends are encountered.

The brute force approach explores all possible vertex permutations (O(n!)), which is acceptable given the small constraint (`n ≤ 10`).

---

---

awesome — let’s make this interview-ready: clear intuition + a tiny dry run, then two Python solutions in your requested signature:

1. Backtracking/DFS (what interviewers expect first)
2. Bitmask DP over subsets (clean, optimal for n≤20; here n≤10 so it flies)

I’ll wrap with high-yield Q&A.

---

## 2) Intuition & Step-by-Step Dry Run

### Problem recap

We’re given an **undirected** graph (`n` vertices labeled 1..n). A **Hamiltonian path** visits **every vertex exactly once**. We only need to tell if **there exists** such a path (return `1`) or not (`0`).

### Key approaches

* **Backtracking (DFS over permutations with pruning):**
  Try each vertex as a start; extend the path by walking to an unvisited neighbor; backtrack when stuck. With `n ≤ 10`, this is fine.
* **Bitmask DP (subset DP):**
  `dp[mask][v] = True` if there is a path that visits exactly the set `mask` and **ends** at `v`.
  Transition: `dp[mask | (1<<v)][v] |= dp[mask][u]` when there’s an edge `u—v`.
  If any `dp[(1<<n)-1][v]` is True → Hamiltonian path exists.

### Dry run (Example 1)

```
n=4, edges: (1-2),(2-3),(3-4),(2-4)
Adj:
1: [2]
2: [1,3,4]
3: [2,4]
4: [2,3]
```

Backtracking from `1`:

* path = [1], visit neighbor 2
* path = [1,2], try neighbor 3
* path = [1,2,3], try neighbor 4 → success (length=4).
  Hence answer `1`.

On DP:

* Initialize `dp[1<<i][i]=True` for all i.
* Grow masks; ultimately `dp[1111][v]` becomes True (e.g., end at 4), so answer `1`.

---

## 3) Python — Optimized Codes (brute/backtracking + DP)

Return `1` if a Hamiltonian path exists, else `0`.

### A) Backtracking (DFS) — interview staple

```python
# User function Template for python3
class Solution:
    def check(self, n, m, edges):
        """
        Backtracking over path endpoints.
        Build adjacency list. For each start node, DFS picking unvisited neighbors.
        
        Time  : O(n! ) worst-case, but n ≤ 10 so it's fine; heavy pruning from adjacency.
        Space : O(n + m) for graph + O(n) recursion stack + O(n) visited.
        """
        # Build 0-based adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1; v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # Quick pruning: if any isolated vertex and n>1 -> impossible
        if n > 1 and any(len(adj[i]) == 0 for i in range(n)):
            return 0

        visited = [False] * n

        def dfs(u, depth):
            """Return True if we can build a path of length 'depth' ending at u."""
            if depth == n:                      # visited all vertices exactly once
                return True
            # Try unvisited neighbors
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, depth + 1):
                        return True
                    visited[v] = False
            return False

        # Try each vertex as a starting point
        for s in range(n):
            visited[s] = True
            if dfs(s, 1):
                return 1
            visited[s] = False
        return 0
```

#### Why this works (what to say)

* We enumerate simple paths by DFS while enforcing “visit once” with `visited`.
* We stop as soon as path length reaches `n`.
* Complexity is exponential in worst case, but `n ≤ 10` → fast.

---

### B) Bitmask DP over subsets — neat, scalable to ~20 nodes

```python
# User function Template for python3
class Solution:
    def check(self, n, m, edges):
        """
        Subset DP: dp[mask][v] == 1 if there's a path visiting exactly 'mask' and ending at vertex v.
        Transition: from any u in mask with edge u-v, set dp[mask|1<<v][v] |= dp[mask][u].

        Time  : O(n * 2^n + m * 2^n)   (here n ≤ 10 → ~10k states * small factor)
        Space : O(n * 2^n)
        """
        # Build adjacency bitmasks for quicker transitions
        adj = [0] * n
        for u, v in edges:
            u -= 1; v -= 1
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

        ALL = (1 << n) - 1
        # dp[mask][v] as booleans; use list of ints for speed
        dp = [ [0]*n for _ in range(1 << n) ]

        # Initialize: single-vertex paths
        for v in range(n):
            dp[1 << v][v] = 1

        # Iterate over masks, grow by one vertex each step
        for mask in range(1 << n):
            # speed: skip masks with no bits (but 0 not used anyway)
            for v in range(n):
                if dp[mask][v] == 0:
                    continue
                # we are at 'v' having visited 'mask'; try to add a neighbor 'w'
                # candidate neighbors are those adjacent to v and not yet in mask
                nxt = adj[v] & ~mask
                w = nxt
                while w:
                    lsb = w & -w
                    w_idx = (lsb.bit_length() - 1)
                    dp[mask | (1 << w_idx)][w_idx] = 1
                    w -= lsb

        # If any full-mask state exists, we have a Hamiltonian path
        for v in range(n):
            if dp[ALL][v]:
                return 1
        return 0
```

#### Notes you can say

* `dp[mask][v]` compactly encodes all partial endpoints; we don’t store order, only reachability.
* Space/time are `Θ(n·2^n)` which is perfect here.

---

## 4) Interview Q&A (high-yield)

**Q1. Difference between Hamiltonian path and Eulerian path?**

* **Hamiltonian**: visits **each vertex** exactly once (NP-complete in general).
* **Eulerian**: uses **each edge** exactly once (linear-time characterizations via degree/connectivity).

**Q2. Why is backtracking acceptable here?**
Constraints are tiny (`n ≤ 10`). Worst case `O(n!)` is still manageable, and adjacency pruning helps a lot.

**Q3. How does the `*bitmask DP*` work?**
We store whether any path visits a set of vertices `mask` and **ends at** vertex `v`. We extend by one neighbor at a time. If any state reaches `mask = (1<<n)-1`, a Hamiltonian path exists.

**Q4. Can we reconstruct the path with DP?**
Yes — store a `parent[mask][v] = u` when you set `dp[mask][v] = True`. Backtrack from any `dp[ALL][v]`.

**Q5. Common pruning ideas for the backtracking?**

* Early return if a vertex has degree `0` (and `n>1`).
* Order next neighbors by smaller degree first (heuristic).
* Start from vertices with extreme degree (sometimes prunes faster).

**Q6. Why 0-based vs 1-based nodes in code?**
Input labels are 1..n; internally we convert to 0..n-1 for array indexing.

**Q7. Could we use BFS/DFS to detect Hamiltonicity directly?**
No; plain DFS/BFS only tests reachability, not the “exactly once” constraint. You need backtracking or subset DP.

**Q8. Complexity of bitmask DP here?**
`O(n·2^n + m·2^n)` time, `O(n·2^n)` space. With `n=10`, that’s at most ~10,240 states * small factor → fast.

---

---

awesome — here’s a **runnable, interview-style full program** for **Hamiltonian Path** with:

* two implementations (Backtracking DFS and Bitmask DP),
* rich **inline time/space complexity** notes right where they matter,
* a tiny **driver** that prints **inputs & outputs**, and
* **timeit** micro-benchmarks comparing both approaches on small graphs.

I finish with a few crisp **real-world use cases**.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Hamiltonian Path — full demo
----------------------------
Given an undirected graph (n <= 10 here), return 1 if there exists a Hamiltonian path,
else 0.

We include two approaches:

A) Backtracking DFS (interview staple)
   - Try every vertex as a start; recursively visit an unvisited neighbor and backtrack.
   - Time  : O(n!) worst-case (n <= 10 is fine), but heavily pruned by degrees.
   - Space : O(n + m) for graph + O(n) recursion + O(n) visited.

B) Bitmask DP over subsets (optimal for n up to ~20)
   - dp[mask][v] = 1 if there exists a path that visits exactly vertices in 'mask'
     and ends at vertex v.
   - Transition: for any u in mask with edge u-v, dp[mask | 1<<v][v] |= dp[mask][u]
   - Time  : Θ(n * 2^n + m * 2^n)
   - Space : Θ(n * 2^n)

The driver prints example outputs and runs timeit micro-benchmarks.
"""

from typing import List
import timeit


# --------------------------- Approach A: Backtracking / DFS --------------------------- #
class SolutionBacktrack:
    def check(self, n: int, m: int, edges: List[List[int]]) -> int:
        """
        Build adjacency and run DFS from each node.

        Complexity commentary (at the point of use below):
          - Building adjacency: O(n + m)
          - For each start vertex: DFS explores permutations of neighbors with pruning.
            Worst-case O(n!), typical much smaller for sparse graphs / small n.
          - Space: visited[] O(n), recursion depth O(n)
        """
        # Build 0-based adjacency list  — O(n + m)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1; v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # Quick pruning: if a vertex is isolated and n > 1 → impossible.
        if n > 1 and any(len(adj[i]) == 0 for i in range(n)):
            return 0

        visited = [False] * n

        def dfs(u: int, depth: int) -> bool:
            """Return True if path of length 'depth' ending at u can be extended to n."""
            if depth == n:                      # O(1): all vertices visited exactly once
                return True
            # Try unvisited neighbors — branching = deg(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True           # O(1)
                    if dfs(v, depth + 1):       # depth grows to at most n → O(n) stack
                        return True
                    visited[v] = False          # backtrack O(1)
            return False

        # Try each vertex as starting point — O(n) starts
        for s in range(n):
            visited[s] = True
            if dfs(s, 1):
                return 1
            visited[s] = False
        return 0


# --------------------------- Approach B: Bitmask DP over subsets --------------------------- #
class SolutionDP:
    def check(self, n: int, m: int, edges: List[List[int]]) -> int:
        """
        dp[mask][v] == 1 if there exists a path visiting exactly 'mask' and ending at v.

        Complexity at use:
          - Build adjacency as bitmasks: O(n + m)
          - States: (2^n) * n  (here n <= 10 → at most 1024 * 10)
          - For each dp[mask][v]=1, we iterate neighbors not in mask (bit tricks) — O(deg(v))
          - Time  : Θ(n*2^n + m*2^n)
          - Space : Θ(n*2^n)
        """
        # Build bitmask adjacency  — O(n + m)
        adj_mask = [0] * n
        for u, v in edges:
            u -= 1; v -= 1
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)

        ALL = (1 << n) - 1
        # dp[mask][v] as ints (0/1) — O(n * 2^n) memory
        dp = [[0] * n for _ in range(1 << n)]

        # Initialize single-vertex paths — O(n)
        for v in range(n):
            dp[1 << v][v] = 1

        # Iterate masks in increasing order — O(n * 2^n)
        for mask in range(1 << n):
            for v in range(n):
                if dp[mask][v] == 0:
                    continue
                # neighbors not yet visited: adj_mask[v] & ~mask
                rem = adj_mask[v] & ~mask
                while rem:
                    lsb = rem & -rem                 # O(1) isolate lowest set bit
                    u = (lsb.bit_length() - 1)       # index of that bit
                    dp[mask | (1 << u)][u] = 1       # transition — O(1)
                    rem -= lsb

        # If any full-mask state exists, a Hamiltonian path exists — O(n)
        for v in range(n):
            if dp[ALL][v]:
                return 1
        return 0


# ------------------------------------ timeit helpers ------------------------------------ #
def bench(func, *args, number=2000):
    """
    Simple micro-benchmark wrapper.
    Returns average seconds/run using timeit. For tiny graphs, treat as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------------ demo ------------------------------------------ #
if __name__ == "__main__":
    print("=== Hamiltonian Path — Backtracking vs Bitmask DP ===\n")

    # Example 1 (from prompt): Hamiltonian path exists
    n1, m1 = 4, 4
    edges1 = [[1, 2], [2, 3], [3, 4], [2, 4]]

    # Example 2 (from prompt): No Hamiltonian path
    n2, m2 = 4, 3
    edges2 = [[1, 2], [2, 3], [2, 4]]

    A = SolutionBacktrack()
    B = SolutionDP()

    print(">>> Example 1")
    print("n, m:", n1, m1, "edges:", edges1)
    outA1 = A.check(n1, m1, edges1)
    outB1 = B.check(n1, m1, edges1)
    print("Backtracking :", outA1)
    print("Bitmask DP   :", outB1, "\n")

    print(">>> Example 2")
    print("n, m:", n2, m2, "edges:", edges2)
    outA2 = A.check(n2, m2, edges2)
    outB2 = B.check(n2, m2, edges2)
    print("Backtracking :", outA2)
    print("Bitmask DP   :", outB2, "\n")

    # ------------------------------ Micro-benchmarks ------------------------------ #
    print("=== Timings (average seconds per run) ===")
    # A denser random-like small graph (n=9) for timing; still deterministic here
    n3 = 9
    edges3 = [
        [1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9], # path backbone
        [1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],       # chords to increase branching
        [1,5],[2,6],[3,7],[4,8],[5,9]
    ]
    m3 = len(edges3)

    runs_small = 4000
    t_back = bench(SolutionBacktrack().check, n1, m1, edges1, number=runs_small)
    t_dp   = bench(SolutionDP().check,         n1, m1, edges1, number=runs_small)
    print(f"Small (n={n1})  runs={runs_small}: Backtracking {t_back:.8e}s | DP {t_dp:.8e}s")

    runs_med = 800
    t_back2 = bench(SolutionBacktrack().check, n3, m3, edges3, number=runs_med)
    t_dp2   = bench(SolutionDP().check,         n3, m3, edges3, number=runs_med)
    print(f"Medium(n={n3})  runs={runs_med:4d}: Backtracking {t_back2:.8e}s | DP {t_dp2:.8e}s")

    print("\nNote: numbers vary by machine. DP is Θ(n·2^n) and often wins for n≥9;")
    print("      Backtracking can be faster on very sparse graphs due to strong pruning.")
```

### What you’ll see

* For Example 1: both methods print `1`.
* For Example 2: both print `0`.
* Timing section: you’ll see average seconds/run for a small and a medium-sized instance; typically DP is more consistent as `n` grows.

---

## 6) Real-World Use Cases (the important ones)

1. **Scheduling/Sequencing with Visit-Exactly-Once Constraints**
   Visiting each workstation/room/inspection point exactly once — e.g., manufacturing or facility audits — when order feasibility matters more than distance optimality.

2. **Puzzle/Path Games & Tour Problems**
   Checking if a given graph puzzle allows a single sweep visiting each node exactly once (variations of “find a path touching every tile once”).

3. **Compiler/Register Allocation Heuristics (toy models)**
   Some heuristics explore permutations of items with pairwise constraints; Hamiltonian feasibility shows whether a full traversal order exists.

4. **Bioinformatics (toy graph models)**
   Validating whether a path exists that visits each unique feature/node exactly once in simplified assembly/annotation graphs.