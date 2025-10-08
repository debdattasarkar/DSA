# Bridge Edge in a Graph

**Difficulty:** Medium
**Accuracy:** 34.61%
**Submissions:** 78K+
**Points:** 4

---

### Problem Statement

Given an undirected graph with **V** vertices numbered from **0 to V-1** and **E** edges, represented by a 2D array `edges[][]`, where `edges[i] = [u, v]` represents the edge between the vertices **u** and **v**.
Determine whether a specific edge between two vertices **(c, d)** is a **bridge**.

---

### Note

* An edge is called a **bridge** if **removing it increases the number of connected components** of the graph.
* If there’s only one path between **c** and **d** (which is the edge itself), then that edge is a **bridge**.

---

### Examples

#### Example 1:

**Input:**

```
V = 4  
edges = [[0, 1], [1, 2], [2, 3]]  
c = 1, d = 2
```

**Output:**

```
true
```

**Explanation:**
From the graph, we can clearly see that removing the edge **1–2** will disconnect the graph.
Hence, it is a **bridge**.

Graph Visualization:

```
0
|
1
|
2
|
3
```

If edge (1–2) is removed, the graph breaks into two components.

---

#### Example 2:

**Input:**

```
V = 5  
edges = [[0, 1], [0, 3], [1, 2], [2, 0], [3, 4]]  
c = 0, d = 2
```

**Output:**

```
false
```

**Explanation:**
Removing the edge between nodes **0** and **2** won’t affect the graph’s connectivity.

So, it’s **not a Bridge Edge**.

All bridge edges in this graph are shown as green lines in the below conceptual diagram.

```
    1
   / \
  2 - 0 - 3 - 4
```

Removing (0–2) does not disconnect the graph because 0 ↔ 2 are still connected via 1.

---

### Constraints

```
1 ≤ V, E ≤ 10^5  
0 ≤ c, d ≤ V - 1
```

---

### Expected Complexities

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V + E)

---

### Company Tags

Amazon, Microsoft, OYO Rooms

---

### Topic Tags

Graph, Data Structures

---

### Related Articles

* [Bridge in a Graph](https://www.geeksforgeeks.org/bridge-in-a-graph/)
* [Check if removing an edge disconnects the graph](https://www.geeksforgeeks.org/check-removing-given-edge-disconnects-given-graph/)

---

---

Here’s an interview-ready guide to **Bridge Edge in an Undirected Graph** with a clear intuition, step-by-step dry run, and two Python solutions (efficient Tarjan + simple “remove & test” brute force).

---

## 2) Intuition + step-by-step dry run

### What is a bridge?

An edge **(u, v)** is a **bridge** if removing it **increases the number of connected components**.
Equivalently in DFS terms: edge **(u → v)** (where `u` is the DFS parent of `v`) is a bridge iff

```
low[v] > tin[u]
```

where:

* `tin[x]` = time when node `x` was first discovered (DFS discovery/entry time).
* `low[x]` = the earliest discovery time reachable from `x` by taking **zero or more tree edges** followed by **at most one back edge** (i.e., the minimum `tin` over x’s subtree and its back edges).

If there are **multiple parallel edges** between `c` and `d`, then (c,d) is **not** a bridge (removing one leaves another path).

### Dry run 1 (Example 1)

```
V = 4
edges: 0–1, 1–2, 2–3       (a line)
query: c=1, d=2
```

Run DFS starting at 0 (times increase each discover):

* Discover 0: `tin[0]=0, low[0]=0`

  * Go to 1: `tin[1]=1, low[1]=1`

    * Go to 2: `tin[2]=2, low[2]=2`

      * Go to 3: `tin[3]=3, low[3]=3`

        * No unvisited neighbors; backtrack: low[2] = min(low[2], low[3]) = 2
      * Check edge (2,3): `low[3](=3) > tin[2](=2)` → **(2,3) is a bridge**
    * Backtrack 2→1: low[1] = min(1, low[2]=2) = 1

      * Check (1,2): `low[2](=2) > tin[1](=1)` → **(1,2) is a bridge** ✅ (our query)
  * Backtrack 1→0: low[0] = min(0, low[1]=1) = 0

    * Check (0,1): `low[1](=1) > tin[0](=0)` → **(0,1) is a bridge**
      Conclusion: (1,2) is a bridge → `true`.

### Dry run 2 (Example 2)

```
V = 5
edges: 0–1, 0–3, 1–2, 2–0, 3–4
query: c=0, d=2
```

There’s a cycle 0–1–2–0. DFS (one possible order):

* 0 discovered (`tin[0]=0, low[0]=0`), go to 1 (`tin[1]=1, low[1]=1`), go to 2 (`tin[2]=2, low[2]=2`).
* From 2 we see back edge to 0 ⇒ low[2] = min(2, tin[0]=0) = 0.
* Back to 1: low[1] = min(1, low[2]=0) = 0.
* Back to 0: low[0] = min(0, low[1]=0) = 0.
* Check (0,2) via parent chain: `low[2]=0 > tin[0]=0`? **No** → NOT a bridge.
  Even if we look at the explicit edge (0,2), the presence of the cycle keeps 0 and 2 connected after removing it. → `false`.

---

## 3) Python solutions (both styles)

All codes follow the requested format:

```python
class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
```

### A) Efficient (Tarjan’s bridge algorithm) — **O(V+E)**

```python
# Tarjan's bridge detection (DFS). Handles big graphs in O(V+E).

class Solution:
    def isBridge(self, V, edges, c, d):
        """
        Returns 1 if edge (c,d) is a bridge else 0.

        Core idea: Run a single DFS computing tin[u] (discovery time)
        and low[u] (lowest reachable discovery time). For tree edge (u->v),
        it's a bridge iff low[v] > tin[u].

        Time  : O(V + E)
        Space : O(V + E) for adjacency + O(V) for DFS stacks/arrays
        """
        # Normalize query edge as an unordered pair
        x, y = (c, d) if c <= d else (d, c)

        # Build adjacency + count parallel edges
        adj = [[] for _ in range(V)]
        multiplicity = {}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            a, b = (u, v) if u <= v else (v, u)
            multiplicity[(a, b)] = multiplicity.get((a, b), 0) + 1

        # If there are multiple edges between (c,d), removing one won't disconnect -> not a bridge
        if multiplicity.get((x, y), 0) > 1:
            return 0

        # Tarjan arrays
        tin  = [-1] * V   # discovery time
        low  = [-1] * V   # lowest discovery reachable
        timer = [0]
        seen_bridge = [False]  # flag to early stop when we find (c,d)

        import sys
        sys.setrecursionlimit(1_000_000)

        def dfs(u: int, parent: int):
            if seen_bridge[0]:
                return
            tin[u] = low[u] = timer[0]
            timer[0] += 1

            for v in adj[u]:
                if v == parent:
                    continue
                if tin[v] != -1:
                    # back edge
                    low[u] = min(low[u], tin[v])
                else:
                    # tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Check bridge condition for tree edge (u, v)
                    if low[v] > tin[u]:
                        # Is THIS the queried edge?
                        a, b = (u, v) if u <= v else (v, u)
                        if (a, b) == (x, y):
                            seen_bridge[0] = True
                            return

        # Graph may be disconnected; run DFS from every unvisited node
        for i in range(V):
            if tin[i] == -1:
                dfs(i, -1)
                if seen_bridge[0]:
                    break

        return 1 if seen_bridge[0] else 0
```

**Why this works**
If the only way from `v` back to `u` or above is through the parent edge `(u,v)`, then the earliest reachable discovery from `v`’s subtree remains **after** `tin[u]`, hence `low[v] > tin[u]` → removing `(u,v)` disconnects those subtrees.

---

### B) Simple “remove & test connectivity” (Brute-ish, easy to reason about)

```python
# Remove the edge (once), then DFS/BFS from c and see if d is still reachable.

from collections import deque

class Solution:
    def isBridge(self, V, edges, c, d):
        """
        Steps:
        1) If there are parallel edges between (c,d), it's NOT a bridge.
        2) Build adjacency sets.
        3) Remove a single (c,d) edge.
        4) BFS/DFS from c; if d is unreachable -> it's a bridge.

        Time  : O(V + E) for one BFS/DFS (building/removing are linear overall)
        Space : O(V + E)
        """
        a, b = (c, d) if c <= d else (d, c)

        # Count multiplicities to handle parallel edges
        mult = {}
        for u, v in edges:
            x, y = (u, v) if u <= v else (v, u)
            mult[(x, y)] = mult.get((x, y), 0) + 1
        if mult.get((a, b), 0) > 1:
            return 0  # removing just one still leaves another path via parallel edge

        # Build adjacency as sets (safe now since multiplicity==1 for (c,d))
        adj = [set() for _ in range(V)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        # Remove edge (c,d) once
        if d in adj[c]:
            adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)

        # BFS from c; if we can't reach d, it's a bridge
        vis = [False] * V
        q = deque([c])
        vis[c] = True
        while q:
            u = q.popleft()
            for w in adj[u]:
                if not vis[w]:
                    vis[w] = True
                    q.append(w)

        return 1 if not vis[d] else 0
```

> Although this is also **O(V+E)** for one query, it’s considered the **brute/easy** way because it literally tests connectivity after removal and does not compute all bridges in one pass as Tarjan does.

---

## 4) Interview Q & A

**Q1. Why is the Tarjan condition `low[v] > tin[u]` the test for a bridge?**
Because `low[v]` tracks the **earliest discoverable ancestor** reachable from `v`’s subtree. If it’s **strictly greater** than `tin[u]`, then the subtree under `v` cannot reach `u` or any ancestor of `u` via a back edge—so removing `(u,v)` disconnects the graph there.

**Q2. What about parallel (multi) edges or self loops?**

* **Parallel edges** between `c` and `d` mean removing one still leaves another direct path; hence it’s **not a bridge**. We check multiplicities.
* **Self loops** never affect connectivity between distinct vertices, so they aren’t bridges.

**Q3. Do we need to run DFS from every node?**
If the graph can be disconnected, yes—start DFS in every unvisited component to ensure you evaluate all tree edges. Early-exit when you’ve already confirmed the queried edge is a bridge.

**Q4. Recursion limits in Python?**
For `V` up to `1e5`, recursion depth can exceed defaults. Either increase recursion limit (`sys.setrecursionlimit`) or write an **iterative** DFS.

**Q5. Complexity?**

* **Tarjan:** `O(V+E)` time, `O(V+E)` space.
* **Remove & test:** building adjacency + one BFS/DFS is also `O(V+E)`; still fine per single query but doesn’t scale to “many edge queries” as efficiently as computing all bridges once.

**Q6. How to return all bridges?**
Collect every tree edge `(u,v)` satisfying `low[v] > tin[u]` while running Tarjan and return the list.

**Q7. Can we do this with DSU?**
Not efficiently for bridges in static graphs. DSU is great for connectivity but does not directly tell you if a **specific** edge is a bridge. Dynamic bridge-finding uses more advanced structures (e.g., Link-Cut Trees).

---

---

awesome — here’s a complete, runnable script for **“Bridge edge in a graph”** that includes:

* the optimal **Tarjan (DFS low-link)** solution in the required `Solution.isBridge` method
* an optional **brute “remove & test connectivity”** helper for reference
* **inline time/space-complexity** notes where they matter
* demo runs on the two examples from the prompt + one custom case
* a small **timeit** benchmark that reports average seconds/run

---

## 5) Full program (with inline complexity + inputs/outputs + timing)

```python
"""
Bridge edge in an undirected graph
----------------------------------
Given V vertices (0..V-1) and E edges, determine whether a specific edge (c, d)
is a BRIDGE (i.e., removing it increases the number of connected components).

Primary algorithm: Tarjan's bridge-finding via DFS (tin/low)
  Bridge condition for tree edge (u->v): low[v] > tin[u]

Asymptotics:
  Let V = number of vertices, E = number of edges.
  Time  : O(V + E)   — single DFS over the graph
  Space : O(V + E)   — adjacency + recursion/arrays
"""

from collections import deque
import sys
import timeit
from typing import List, Tuple


# ------------------------------ Core Solution ------------------------------ #
class Solution:
    def isBridge(self, V: int, edges: List[Tuple[int, int]], c: int, d: int) -> int:
        """
        Return 1 if the edge (c, d) is a bridge, else 0.

        Steps:
        1) Build adjacency list and count multiplicities for (min(c,d), max(c,d)).
           If multiple parallel edges exist between c and d -> NOT a bridge.
           - Build: O(V + E) time, O(V + E) space
        2) Run Tarjan DFS (tin/low). For each tree edge (u->v),
           if low[v] > tin[u], it's a bridge.
           - DFS: O(V + E) time, O(V) aux arrays + recursion
        3) Early stop once we find the queried edge to be a bridge.
        """
        # Normalize the queried edge as an unordered pair (a <= b)
        a, b = (c, d) if c <= d else (d, c)

        # Build adjacency & multiplicity map
        adj = [[] for _ in range(V)]
        multiplicity = {}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            x, y = (u, v) if u <= v else (v, u)
            multiplicity[(x, y)] = multiplicity.get((x, y), 0) + 1

        # If parallel edges exist between c and d, removing one doesn't disconnect
        if multiplicity.get((a, b), 0) > 1:
            return 0

        tin  = [-1] * V     # discovery time of each node (O(V) space)
        low  = [-1] * V     # earliest discovery reachable from node (O(V) space)
        timer = [0]         # list to allow closure write (O(1) space)
        found = [False]     # early-stop flag (O(1) space)

        sys.setrecursionlimit(1_000_000)

        def dfs(u: int, parent: int) -> None:
            """
            DFS to compute tin[u] and low[u].
            Each vertex/edge is processed once: O(V + E) time total.
            """
            if found[0]:  # early stop if already answered
                return
            tin[u] = low[u] = timer[0]
            timer[0] += 1

            for v in adj[u]:
                if v == parent:
                    continue
                if tin[v] != -1:
                    # Back edge: update low[u] with tin[v]
                    low[u] = min(low[u], tin[v])
                else:
                    # Tree edge
                    dfs(v, u)
                    # After returning from v, propagate low[]
                    low[u] = min(low[u], low[v])

                    # Check bridge condition for tree edge (u, v)
                    if low[v] > tin[u]:
                        x, y = (u, v) if u <= v else (v, u)
                        if (x, y) == (a, b):
                            found[0] = True
                            return

        # Graph may be disconnected → run DFS from all components
        for i in range(V):
            if tin[i] == -1:
                dfs(i, -1)
                if found[0]:
                    break

        return 1 if found[0] else 0


# ------------------------- Optional Brute (for reference) ------------------------- #
def is_bridge_bruteforce(V: int, edges: List[Tuple[int, int]], c: int, d: int) -> int:
    """
    Remove & test connectivity once.

    1) If parallel edges exist between (c,d) -> return 0 (not a bridge).
    2) Remove exactly one (c,d) from adjacency.
    3) BFS/DFS from c; if d is unreachable -> bridge.

    Time  : O(V + E)
    Space : O(V + E)
    """
    a, b = (c, d) if c <= d else (d, c)
    mult = {}
    for u, v in edges:
        x, y = (u, v) if u <= v else (v, u)
        mult[(x, y)] = mult.get((x, y), 0) + 1
    if mult.get((a, b), 0) > 1:
        return 0

    # Build adjacency sets
    adj = [set() for _ in range(V)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # Remove one instance of (c, d)
    if d in adj[c]:
        adj[c].remove(d)
    if c in adj[d]:
        adj[d].remove(c)

    # BFS from c to see if we can still reach d
    vis = [False] * V
    q = deque([c])
    vis[c] = True
    while q:
        u = q.popleft()
        for w in adj[u]:
            if not vis[w]:
                vis[w] = True
                q.append(w)
    return 1 if not vis[d] else 0


# ------------------------------ Demo & Timing ------------------------------ #
def print_case(V, edges, c, d, label):
    print(f"{label}:")
    print("  V =", V)
    print("  edges =", edges)
    print(f"  query edge = ({c}, {d})")
    sol = Solution()
    ans = sol.isBridge(V, edges, c, d)
    print("  isBridge (Tarjan)  ->", bool(ans))
    brute = is_bridge_bruteforce(V, edges, c, d)
    print("  isBridge (Brute)   ->", bool(brute))
    print()


def run_demo_and_benchmark():
    # Example 1
    V1 = 4
    E1 = [(0, 1), (1, 2), (2, 3)]
    c1, d1 = 1, 2
    print_case(V1, E1, c1, d1, "Example 1 (should be True)")

    # Example 2
    V2 = 5
    E2 = [(0, 1), (0, 3), (1, 2), (2, 0), (3, 4)]
    c2, d2 = 0, 2
    print_case(V2, E2, c2, d2, "Example 2 (should be False)")

    # Custom: parallel edges (c,d) appears twice -> NOT a bridge
    V3 = 3
    E3 = [(0, 1), (1, 2), (1, 2)]
    c3, d3 = 1, 2
    print_case(V3, E3, c3, d3, "Custom (parallel edges → False)")

    # ------------------------------ Timing ------------------------------ #
    # Build a larger random-ish chain with extra chords to simulate bigger inputs.
    V = 50
    edges = []
    for i in range(V - 1):
        edges.append((i, i + 1))            # chain edges are bridges
    # add some chords to reduce number of actual bridges
    for i in range(0, V - 2, 5):
        edges.append((i, i + 2))
    c, d = 20, 21  # one of the chain edges (likely still a bridge in this graph)

    sol = Solution()

    def task_tarjan():
        sol.isBridge(V, edges, c, d)

    runs = 20
    avg = timeit.timeit(task_tarjan, number=runs) / runs
    print(f"Timing (Tarjan): V={V}, E={len(edges)}, average over {runs} runs -> {avg:.6f} s/run")
    print("Asymptotic time: O(V + E).")


if __name__ == "__main__":
    run_demo_and_benchmark()
```

### What you’ll see when you run it

* For **Example 1** (line graph), `(1,2)` prints `True`.
* For **Example 2** (contains cycle 0–1–2–0), `(0,2)` prints `False`.
* For a **parallel edge** case, it prints `False`.
* A small timing line like:

  ```
  Timing (Tarjan): V=50, E=..., average over 20 runs -> 0.000xx s/run
  ```

---

## 6) Real-World Use Cases (high-impact)

1. **Network reliability / single points of failure**
   In computer networks, power grids, or road networks, a bridge edge is a **critical link**—its failure disconnects the system. Identifying bridges helps add redundancy.

2. **Software dependency graphs**
   In build systems or microservice architectures, a bridge dependency indicates a **critical integration** whose removal isolates components—useful for risk analysis and refactoring.

3. **Social & collaboration graphs**
   Bridge relationships can signal **brokers** or **gatekeepers** connecting communities. Removing such ties fragments the graph—important in influence or information flow studies.

4. **Infrastructure planning**
   For transportation and logistics, bridges (in graph sense) pinpoint roads/routes where extra capacity or backup routes are strategically valuable.