# Possible Paths Between 2 Vertices

**Difficulty:** Medium
**Accuracy:** 56.57%
**Submissions:** 32K+
**Points:** 4

---

## Problem Statement

Given a **Directed Graph** having `V` nodes numbered from `0` to `V-1`, and `E` directed edges.
Given two nodes, **source** and **destination**, count the number of **distinct paths** between these two vertices in the directed graph.

> These paths should **not contain any cycle**.

**Note:**

* The graph doesn’t contain multiple edges, self-loops, or cycles.

---

## Examples

### Example 1

**Input:**

```
V = 5, E = 7  
Adj = [[1, 2, 4], [3, 4], [4], [2], []]  
source = 0  
destination = 4
```

**Output:**

```
4
```

**Explanation:**
There are **4 paths** from node `0` to node `4`:

```
0 → 4
0 → 1 → 4
0 → 2 → 4
0 → 1 → 3 → 2 → 4
```

---

### Example 2

**Input:**

```
V = 4, E = 5  
Adj = [[1, 3], [2, 3], [3], []]  
source = 0  
destination = 3
```

**Output:**

```
3
```

**Explanation:**
There are **3 paths** from node `0` to node `3`:

```
0 → 3
0 → 1 → 3
0 → 1 → 2 → 3
```

---

## Your Task

You do **not** need to read, input, or print anything.
Your task is to complete the function:

```python
def countPaths(V, adj, source, destination):
    # returns the number of paths from source to destination
```

which takes:

* Integer `V` denoting the number of vertices,
* Adjacency list `adj`,
* Integers `source` and `destination` as input parameters,
  and returns the **number of paths** from `source` vertex to `destination` vertex.

---

## Expected Complexities

* **Expected Time Complexity:** `O(V!)`
  (In the worst case, we explore every possible permutation of vertices)
* **Expected Auxiliary Space:** `O(V)`
  (Due to recursion stack and visited array)

---

## Constraints

* `1 ≤ V, E ≤ 100`
* `1 ≤ source, destination ≤ V`

---

## Topic Tags

* DFS
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* [Count Possible Paths Between Two Vertices](https://www.geeksforgeeks.org/count-possible-paths-two-vertices/)

---

---

Here’s a crisp, interview-ready package for **“Count the number of paths between two vertices in a directed graph (DAG)”**.

---

## 2) Explanation + Step-by-Step Dry Run

**Core idea**

* A path count from a node `u` to `destination` equals the **sum of path counts** from all its neighbors to `destination`.
* Because the graph is a DAG (no cycles), this recurrence is well defined and we can:

  * (A) do a **DFS backtracking** (brute; explores all paths),
  * (B) add **memoization** to cache sub-results (optimal),
  * (C) or do a **topological DP** (iterative, also optimal).

All return the same answer; (B) and (C) run in **O(V+E)**.

### Dry run (memoized DFS) on Example 1

```
V = 5
Adj = [
  [1,2,4],  # 0
  [3,4],    # 1
  [4],      # 2
  [2],      # 3
  []        # 4
]
source = 0, destination = 4
```

Let `ways(u)` be paths from `u` to `4`. Base: `ways(4)=1`.

1. Start at `0`: `ways(0) = ways(1) + ways(2) + ways(4)`
2. Compute `ways(1) = ways(3) + ways(4)`

   * `ways(3) = ways(2)`

     * `ways(2) = ways(4) = 1` → memoize `ways(2)=1`
   * So `ways(3)=1`
   * `ways(4)=1`
   * Hence `ways(1)=1+1=2` (memoize)
3. We already have `ways(2)=1` (from above)
4. `ways(4)=1` (base)
5. Therefore `ways(0)=2+1+1=4` ✅

---

## 3) Optimized Python Codes (with interview-friendly comments)

### A) Brute Force DFS Backtracking (explores all paths)

```python
# User function Template for python3
class Solution:
    # Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # Brute-force DFS over all paths.
        # Time: O(#paths) worst-case can be O(V!) in dense DAGs
        # Space: O(V) recursion stack + pathVisited
        
        pathVisited = [False] * V  # guards against cycles / revisits in current path

        def dfs(u):
            # Reached destination => exactly one path
            if u == destination:
                return 1
            pathVisited[u] = True
            total = 0
            for v in adj[u]:
                # avoid revisiting the same node in current path (safe even if input is a DAG)
                if not pathVisited[v]:
                    total += dfs(v)
            pathVisited[u] = False  # backtrack
            return total

        return dfs(source)
```

### B) Memoized DFS (Top choice in interviews)

```python
class Solution:
    # Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # DAG + memoization (DP on DAG)
        # Time: O(V + E) since each node/edge processed once; memo prunes repeats
        # Space: O(V) for memo + recursion stack
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def ways(u):
            if u == destination:
                return 1
            total = 0
            for v in adj[u]:
                total += ways(v)
            return total
        
        return ways(source)
```

> Why no `visited` here? The premise is **DAG**. If you still want to be robust, add a `state` array to detect unexpected cycles and return 0 when a back-edge is seen.

### C) Iterative Topological DP (Kahn’s algorithm)

```python
class Solution:
    # Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # Topo order + forward DP
        # Time: O(V + E), Space: O(V)
        
        from collections import deque
        
        # 1) Kahn's topo sort
        indeg = [0]*V
        for u in range(V):
            for v in adj[u]:
                indeg[v] += 1
        
        q = deque([u for u in range(V) if indeg[u] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        # 2) DP over topo: number of ways to reach each node from source
        dp = [0]*V
        dp[source] = 1
        for u in topo:
            # If there are dp[u] ways to reach u, push them to all its neighbors
            for v in adj[u]:
                dp[v] += dp[u]
        
        return dp[destination]
```

**Which one to present?**

* If the interviewer emphasizes “DAG”, pick **(B) Memoized DFS** or **(C) Topological DP**.
* If they want to see raw recursion/backtracking, show **(A)** and then optimize to **(B)**.

---

## 4) Common Interview Q&A

**Q1. Why is memoization correct here?**
**A.** In a DAG, the number of paths from `u` to `dest` only depends on its outgoing neighbors (no cycles). Once computed, the result for `u` never changes, so caching (`memo[u]`) is safe and removes repeated subproblems.

**Q2. What’s the time complexity of each approach?**
**A.**

* Brute DFS: proportional to the **number of paths**, worst-case `O(V!)`.
* Memoized DFS / Topo DP: **O(V + E)**.

**Q3. Do we need a `visited` array?**
**A.** For a guaranteed DAG, not for memo/topo methods. In a defensive brute DFS, a `pathVisited` (on the current recursion path) prevents cycles if the input were malformed.

**Q4. How would you handle huge path counts (overflow)?**
**A.** Use `mod` arithmetic (e.g., 1e9+7) if the problem requires; Python ints can grow arbitrarily, but performance or output constraints may mandate a modulus.

**Q5. Can we count paths between **all** pairs efficiently?**
**A.** Yes, using DP in topological order with different sources, or compute the **transitive path counts** via DP on DAG / matrix exponentiation (less practical for large V), depending on constraints.

**Q6. What if the graph contains cycles?**
**A.** The recurrence breaks (infinite paths possible). You must first detect cycles (e.g., with DFS color states or Kahn’s algorithm). If cycles exist on any path from source to destination, define behavior: either report infinite or block paths that revisit nodes (simple‐path counting is #P-complete).

---

### Edge cases to call out in interviews

* `source == destination` → at least one path (the empty path), so return `1`.
* `source` has **no outgoing edges** and `source != destination` → `0`.
* **Disconnected** graph segments.
* **Large V, sparse E** → O(V+E) solution shines.

---

---

Below is a **complete, runnable Python program** that:

* Implements an **O(V+E)** solution (memoized DFS on a DAG).
* Builds the graph, runs the algorithm, prints the result.
* Measures wall-clock runtime with `time.perf_counter()`.
* Includes tight, inline comments explaining **time & space** at each step.

You can paste this into a single file and run it.

```python
# Count paths between two vertices in a directed acyclic graph (DAG)
# ---------------------------------------------------------------
# Approach used in main(): Memoized-DFS (DP on DAG)
#   Time:   O(V + E)  — each node/edge contributes once due to memoization
#   Space:  O(V)      — recursion depth (<= V) + memo table of size V
#
# Notes:
#  - We assume the input is a DAG (as per problem statement). If you aren't sure,
#    you can detect cycles first, or use a topological DP variant (also O(V+E)).

from collections import defaultdict
from functools import lru_cache
from time import perf_counter


class Solution:
    # Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        """
        Parameters
        ----------
        V : int
            Number of vertices (0..V-1)
        adj : List[List[int]]
            Adjacency list of a directed acyclic graph (DAG)
        source : int
            Start vertex
        destination : int
            End vertex

        Returns
        -------
        int : number of distinct directed paths from source to destination
        """

        # --- DP on DAG with memoization ---
        # Time: O(V + E) because each node's ways(u) is computed once and
        #       each outgoing edge (u->v) is traversed once within that call.
        # Space: O(V) for memo + O(V) recursion stack in the worst case (a long chain).
        @lru_cache(maxsize=None)
        def ways(u):
            # Base case: one path that is "already at destination"
            if u == destination:
                return 1
            total = 0
            # Sum of ways over all children
            for v in adj[u]:
                total += ways(v)
            return total

        return ways(source)


# ---------- Optional: a second implementation (iterative Topological DP) ----------
def count_paths_topo(V, adj, source, destination):
    """
    Kahn's algorithm to compute a topological order,
    then forward DP across the topo list.
    Time:  O(V + E), Space: O(V)
    """
    from collections import deque

    indeg = [0] * V
    for u in range(V):
        for v in adj[u]:
            indeg[v] += 1

    q = deque([u for u in range(V) if indeg[u] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    dp = [0] * V
    dp[source] = 1
    for u in topo:
        for v in adj[u]:
            dp[v] += dp[u]
    return dp[destination]


# ------------------------------ Driver / Demo ------------------------------
def build_adj(V, edges):
    """
    Build adjacency list from (u, v) edge list.
    Time:  O(V + E) (initialization and appending edges)
    Space: O(V + E) for the adjacency structure
    """
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj


def demo_one(V, edges, source, destination, use="memo"):
    """
    Run a single demo with timing and print input + output.
    """
    print("\n--- Demo -------------------------------------")
    print(f"V={V}, edges={edges}, source={source}, destination={destination}")
    adj = build_adj(V, edges)

    t0 = perf_counter()
    if use == "memo":
        ans = Solution().countPaths(V, adj, source, destination)
    else:
        ans = count_paths_topo(V, adj, source, destination)
    t1 = perf_counter()

    print(f"Paths: {ans}")
    print(f"Elapsed: {(t1 - t0)*1e6:.1f} µs  ({t1 - t0:.6f} s)")
    print("----------------------------------------------")


if __name__ == "__main__":
    # Example 1 (from prompt-like example)
    # Graph (DAG):
    # 0 -> 1,2,4
    # 1 -> 3,4
    # 2 -> 4
    # 3 -> 2
    # 4 -> (none)
    V1 = 5
    edges1 = [(0, 1), (0, 2), (0, 4),
              (1, 3), (1, 4),
              (2, 4),
              (3, 2)]
    source1, dest1 = 0, 4
    # Expected: 4 (0->4, 0->1->4, 0->2->4, 0->1->3->2->4)
    demo_one(V1, edges1, source1, dest1, use="memo")   # memoized DFS
    demo_one(V1, edges1, source1, dest1, use="topo")   # topological DP

    # Example 2
    # V=4, edges: 0->1, 1->3, 0->2, 2->3
    # Paths 0->3: {0->1->3, 0->2->3} => 2
    V2 = 4
    edges2 = [(0, 1), (1, 3), (0, 2), (2, 3)]
    source2, dest2 = 0, 3
    demo_one(V2, edges2, source2, dest2, use="memo")
```

### Sample Output (will vary slightly in timings)

```
--- Demo -------------------------------------
V=5, edges=[(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 4), (3, 2)], source=0, destination=4
Paths: 4
Elapsed: 150.3 µs  (0.000150 s)
----------------------------------------------
--- Demo -------------------------------------
V=5, edges=[(0, 1), (0, 2), (0, 4), (1, 3), (1, 4), (2, 4), (3, 2)], source=0, destination=4
Paths: 4
Elapsed: 120.2 µs  (0.000120 s)
----------------------------------------------
--- Demo -------------------------------------
V=4, edges=[(0, 1), (1, 3), (0, 2), (2, 3)], source=0, destination=3
Paths: 2
Elapsed: 72.1 µs  (0.000072 s)
----------------------------------------------
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Workflow/Build pipelines (DAGs):**
   Count the number of valid execution paths from a “start” task to a “release” task to estimate variability or test coverage.

2. **Network routing in acyclic overlays:**
   In content distribution networks or DAG-based overlays, compute how many distinct acyclic routes exist from a source to a sink for redundancy analysis.

3. **Version control DAGs (e.g., Git):**
   Counting distinct ancestry paths between commits or tags to understand merge options (when constrained to acyclic segments).

4. **Course/Prerequisite planning:**
   Given a DAG of prerequisites, count distinct completion routes from an entry course to a capstone to estimate curriculum flexibility.

These scenarios rely on DAG structure and benefit from the **O(V+E)** dynamic programming approach you implemented above.