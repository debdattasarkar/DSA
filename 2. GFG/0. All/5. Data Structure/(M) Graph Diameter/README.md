
---

# 📏 Graph Diameter

**Difficulty:** Medium
**Accuracy:** 100.0%
**Submissions:** 2+
**Points:** 4

---

## 🧠 Problem Statement

You are given an **undirected graph** with `V` vertices numbered from `0` to `V-1` and `E` edges, represented as a 2D array `edges[][]`, where each element `edges[i] = [u, v]` represents an undirected edge between vertex `u` and vertex `v`.

Your task is to **find the diameter of the graph**.

---

### 🧩 What is the Diameter of a Graph?

The **diameter** of a graph (sometimes called the **width**) is the **number of edges on the longest path** between any two vertices in the graph.

---

## 🧮 Examples

### Example 1

**Input:**

```
V = 6, E = 5
edges[][] = [[0, 1], [0, 4], [1, 3], [1, 2], [2, 5]]
```

**Output:**

```
4
```

**Explanation:**
The longest path in the graph is from vertex **4** to vertex **5**:

```
4 → 0 → 1 → 2 → 5
```

The number of edges on this path is **4**.

---

### Example 2

**Input:**

```
V = 7, E = 6
edges[][] = [[0, 2], [0, 4], [0, 3], [3, 1], [3, 5], [1, 6]]
```

**Output:**

```
4
```

**Explanation:**
The longest path in the graph is from vertex **2** to vertex **6**:

```
2 → 0 → 3 → 1 → 6
```

The number of edges on this path is **4**.

---

## ⚙️ Constraints

```
2 ≤ V ≤ 10^5
1 ≤ E ≤ V - 1
0 ≤ edges[i][0], edges[i][1] < V
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n)       |
| **Auxiliary Space** | O(n)       |

---

## 🏷️ Topic Tags

`Graph` • `DFS` • `Data Structures`

---

## 🔗 Related Articles

* [Diameter Tree Using DFS](https://www.geeksforgeeks.org/diameter-of-a-tree-using-dfs/)

---

---

Awesome choice—this is a classic. Below is everything you asked for: clear intuition + dry run, then interview-ready Python (brute, 2-BFS/DFS, and 1-DFS), and a fast recall kit with common Q&A.

---

# 2) Explanation + step-by-step dry run

## What “diameter” means here

Diameter = the **number of edges** on the **longest simple path** between any two vertices.

> With the given constraints (E ≤ V − 1), the input is effectively a **tree or a forest**.
> For a connected tree, there’s a one-line recipe: **two BFS/DFS**.

## Key idea (most expected)

**Two BFS/DFS trick**:

1. Start from an arbitrary node `s`. Run BFS/DFS to find the **farthest node A** from `s`.
2. Run BFS/DFS again, now starting from **A**, to find the farthest node **B** and its distance `dist(A,B)`.
   That distance is the **diameter (in edges)**.

Why it works: in a tree, **one end of any longest path** is always a farthest node from an arbitrary start. The second traversal reaches the other end.

### Dry run (Example 1)

```
V = 6
edges = [[0,1],[0,4],[1,3],[1,2],[2,5]]
Adj:
0: 1,4
1: 0,3,2
2: 1,5
3: 1
4: 0
5: 2
```

1. BFS from `s=0`

* Distances: 0→0, 1→1, 4→1, 3→2, 2→2, 5→3
* Farthest node = **5** (distance 3). Call this **A=5**.

2. BFS from `A=5`

* Distances: 5→0, 2→1, 1→2, 0→3, 3→3, 4→4
* Farthest distance = **4** (node 4). So diameter = **4** (path 4–0–1–2–5).

---

# 3) Python solutions (brute → optimal)

Use the requested signature:

```python
class Solution:
    def diameter(self, V, edges):
        # Code here
```

### A) Brute force (for teaching; O(V*(V+E)))

Run BFS from **every** vertex; take the largest distance seen.

* Time: `O(V * (V+E))` (for a tree, `O(V^2)`)
* Space: `O(V)`

```python
from collections import deque, defaultdict

class Solution:
    def diameter(self, V, edges):
        """
        Brute-force: BFS from every node and take the maximum distance seen.
        Time  : O(V * (V + E))  ~ O(V^2) for trees
        Space : O(V) for BFS structures
        """
        if V == 0:
            return 0

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(src):
            """Single BFS returning (farthest_node, farthest_dist) from src."""
            dist = [-1] * V
            q = deque([src])
            dist[src] = 0
            far_node, far_dist = src, 0
            while q:
                x = q.popleft()
                for nbr in graph[x]:
                    if dist[nbr] == -1:
                        dist[nbr] = dist[x] + 1
                        q.append(nbr)
                        if dist[nbr] > far_dist:
                            far_dist = dist[nbr]
                            far_node = nbr
            return far_node, far_dist

        # If the graph might be disconnected (forest), take max over components
        seen = [False] * V
        best = 0
        for s in range(V):
            if seen[s]:
                continue
            # Mark this component
            comp_nodes = []
            q = deque([s])
            seen[s] = True
            while q:
                x = q.popleft()
                comp_nodes.append(x)
                for y in graph[x]:
                    if not seen[y]:
                        seen[y] = True
                        q.append(y)

            # BFS from any node in this component, say comp_nodes[0]
            a, _ = bfs(comp_nodes[0])
            # BFS from 'a' to get the component diameter
            _, d = bfs(a)
            best = max(best, d)

        return best
```

---

### B) Optimal & “most expected”: **Two BFS/DFS** — `O(V+E)`, `O(V)`

```python
from collections import deque, defaultdict

class Solution:
    def diameter(self, V, edges):
        """
        Two-BFS/DFS trick (handles forest by taking max per component).
        Time  : O(V + E)     -- each edge visited O(1) per BFS
        Space : O(V)         -- adjacency + queues/visited
        """
        if V == 0:
            return 0

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(src):
            """Return (farthest_node, farthest_dist) from src."""
            dist = [-1] * V
            q = deque([src])
            dist[src] = 0
            far_node, far_dist = src, 0
            while q:
                x = q.popleft()
                for nbr in graph[x]:
                    if dist[nbr] == -1:
                        dist[nbr] = dist[x] + 1
                        q.append(nbr)
                        if dist[nbr] > far_dist:
                            far_dist = dist[nbr]
                            far_node = nbr
            return far_node, far_dist

        visited = [False] * V
        answer = 0

        # In case the graph is a forest, compute diameter per component
        for s in range(V):
            if visited[s]:
                continue
            # 1) Discover this component (O(size_of_component))
            comp = []
            q = deque([s])
            visited[s] = True
            while q:
                x = q.popleft()
                comp.append(x)
                for y in graph[x]:
                    if not visited[y]:
                        visited[y] = True
                        q.append(y)

            # 2) Two BFS within this component
            a, _ = bfs(comp[0])   # farthest from an arbitrary node
            _, d = bfs(a)         # farthest from 'a' → component diameter
            answer = max(answer, d)

        return answer
```

> Swap BFS with DFS if the interviewer asks for recursion. Complexity stays `O(V+E)`.

---

### C) Single DFS (post-order) computing heights — `O(V+E)`, `O(V)`

For a **tree**, you can compute in a single DFS:
`height(u) = 1 + max(height(children))`.
Track the largest two child heights at each node to update a global `diameter`.

```python
from collections import defaultdict
import sys
sys.setrecursionlimit(1_000_000)

class Solution:
    def diameter(self, V, edges):
        """
        One-DFS (tree only):
          - Track top two child heights at each node.
          - Update global diameter = max(diameter, h1 + h2).
        Time  : O(V + E)
        Space : O(V) recursion + adjacency
        """
        if V == 0:
            return 0

        # Build adjacency list
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * V
        best = 0

        def dfs(u) -> int:
            """
            Returns the height (max depth in edges) of subtree rooted at u.
            Also updates 'best' using the top two child heights.
            """
            nonlocal best
            visited[u] = True
            top1 = top2 = -1  # top two child heights (in edges)
            for v in g[u]:
                if not visited[v]:
                    h = dfs(v)
                    if h > top1:
                        top2 = top1
                        top1 = h
                    elif h > top2:
                        top2 = h
            # If u has no children, height is 0
            node_height = 0 if top1 == -1 else top1 + 1
            # Path through u combines top1 and top2 (+2 edges if both exist)
            path_through_u = 0
            if top1 != -1:
                path_through_u = top1 + 1
            if top2 != -1:
                path_through_u += top2 + 1
            best = max(best, path_through_u)
            return node_height

        # Handle forest: run DFS per component
        for s in range(V):
            if not visited[s]:
                dfs(s)

        return best
```

---

# 4) Interview quick-recall + Q&A

## 10-second recall

> **“Pick any → farthest A → farthest from A = diameter.”**
> (That’s the **2-BFS trick**. Works for any unweighted connected component.)

Or mnemonic: **“Any → A → B → dist(A,B)”**.

## Common Q&A (high yield)

**Q1. Why does 2-BFS work?**
In a tree, choose an arbitrary node `s`. One endpoint of a longest path is a farthest node from `s`. Starting there reaches the other endpoint; the distance is the diameter. (Classic property of trees / unique simple path between nodes.)

**Q2. What if the graph is disconnected?**
Compute the diameter **per component** (2-BFS in each) and take the **maximum**. Code above handles that.

**Q3. Are we counting edges or nodes?**
This problem’s diameter is **#edges**. If you need **#nodes**, add `+1`.

**Q4. What about **weighted** graphs?**
Replace BFS with **Dijkstra** twice (or once from an arbitrary node to get A, then again from A). For a tree with positive weights, **two Dijkstras** gives the weighted diameter.

**Q5. Stack vs queue?**
Either: BFS with a queue or DFS (recursive or iterative). Complexity is the same, `O(V+E)`.

**Q6. Space/time?**
`O(V+E)` time; `O(V)` aux space.

**Q7. Single-pass alternative?**
Yes—**one DFS** tracking the top two child heights at each node and updating a global best (shown above). Works directly on trees.

---

---

## 5) Real-World Use Cases (easy to relate)

1. **Worst-case message hops in a tree network**
   In a tree-topology LAN (or a spanning tree built over a mesh), the diameter equals the **maximum hop count** a packet may travel—useful for latency/TTL bounds.

2. **Propagation delay in org charts / hierarchies**
   Org chart ≈ tree. Diameter gives the **longest escalation/communication chain** end-to-end.

3. **Deepest folder chain in a filesystem**
   Directory tree diameter = longest path between any two folders—useful to locate **extreme path lengths** that may hit OS path limits.

4. **Road networks with no cycles (rural feeders, pipelines)**
   For acyclic infrastructures, diameter ≈ **longest physical route**; helps sizing maintenance windows or cache placement.

5. **Phylogenetic / taxonomy trees**
   Diameter indicates the **maximum evolutionary distance** (in edges) between two species/clades in the simplified unweighted tree.

---

## 6) Full Program (with inline complexity notes + timings)

```python
#!/usr/bin/env python3
"""
Graph Diameter — Two-BFS/DFS and One-DFS implementations
--------------------------------------------------------

What this script does:
  * Builds an undirected graph from edge list
  * Computes diameter per connected component and returns the maximum
  * Shows both methods:
      - two_bfs_diameter()  -> O(V+E), most expected in interviews
      - one_dfs_diameter()  -> O(V+E), single DFS using top-two heights (tree)
  * Runs example inputs and prints outputs
  * Times each method using perf_counter and timeit

Conventions:
  - Diameter here = number of EDGES on the longest simple path.
"""

from collections import deque, defaultdict
from time import perf_counter
import timeit
from typing import List, Tuple
import sys

sys.setrecursionlimit(1_000_000)


# ----------------------------- Utilities -----------------------------
def build_graph(V: int, edges: List[Tuple[int, int]]):
    """
    Build adjacency list.
    Time:  O(V + E)
    Space: O(V + E)
    """
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


def bfs_farthest(V: int, g, src: int) -> Tuple[int, int]:
    """
    Single BFS from src — returns (farthest_node, distance).
    Time:  O(size_of_component)
    Space: O(V) for dist/queue
    """
    dist = [-1] * V
    q = deque([src])
    dist[src] = 0
    far_node, far_dist = src, 0

    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > far_dist:
                    far_dist, far_node = dist[v], v
    return far_node, far_dist


# ----------------------- Two-BFS/DFS (expected) ----------------------
def two_bfs_diameter(V: int, edges: List[Tuple[int, int]]) -> int:
    """
    Diameter across possibly multiple components (forest):
      For each component:
        1) BFS from any node -> farthest A
        2) BFS from A -> distance to farthest B = component diameter
    Return max over components.

    Time:  O(V + E) total (each node/edge touched O(1) amortized)
    Space: O(V) for visited arrays and BFS queues
    """
    if V == 0:
        return 0
    g = build_graph(V, edges)

    visited = [False] * V
    best = 0

    for s in range(V):
        if visited[s]:
            continue

        # Discover this component (BFS). Time: O(size_of_component)
        comp_nodes = []
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            comp_nodes.append(u)
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

        # Two BFS within this component. Time: O(size_of_component)
        A, _ = bfs_farthest(V, g, comp_nodes[0])
        _, comp_diam = bfs_farthest(V, g, A)
        best = max(best, comp_diam)

    return best


# ------------------------- One-DFS (tree only) -----------------------
def one_dfs_diameter(V: int, edges: List[Tuple[int, int]]) -> int:
    """
    Single DFS that computes heights and updates diameter:
      - Height(u) = max child height + 1
      - Track the top two child heights to update a global best = h1 + h2

    Works correctly for trees; for a forest, we run it per component.
    Time:  O(V + E)
    Space: O(V) recursion + adjacency
    """
    g = build_graph(V, edges)
    visited = [False] * V
    best = 0

    def dfs(u: int) -> int:
        nonlocal best
        visited[u] = True

        # Top two child heights (in edges); start with -1 meaning "none"
        h1 = h2 = -1
        for v in g[u]:
            if not visited[v]:
                h = dfs(v)
                if h > h1:
                    h2, h1 = h1, h
                elif h > h2:
                    h2 = h

        # Node height: 0 if leaf, else h1 + 1
        node_height = 0 if h1 == -1 else h1 + 1

        # Path through u (if two children exist): (h1+1) + (h2+1) = h1 + h2 + 2
        path_through_u = 0
        if h1 != -1:
            path_through_u = h1 + 1
        if h2 != -1:
            path_through_u += h2 + 1
        best = max(best, path_through_u)
        return node_height

    for s in range(V):
        if not visited[s]:
            dfs(s)
    return best


# ------------------------------- Demo --------------------------------
def main():
    print("=== Graph Diameter — Demo & Timing ===\n")

    # Examples from the prompt
    examples = [
        # (V, edges, expected_diameter)
        (6, [(0, 1), (0, 4), (1, 3), (1, 2), (2, 5)], 4),  # 4-0-1-2-5
        (7, [(0, 2), (0, 4), (0, 3), (3, 1), (3, 5), (1, 6)], 4),  # 2-0-3-1-6
        # A forest (two separate chains): diameters 3 and 2 -> overall 3
        (8, [(0,1),(1,2),(2,3), (5,6),(6,7)], 3),
    ]

    for (V, edges, exp) in examples:
        print(f"V={V}, edges={edges}")
        # Single-run timings (perf_counter)
        t0 = perf_counter()
        out_two_bfs = two_bfs_diameter(V, edges)
        t1 = perf_counter()

        t2 = perf_counter()
        out_one_dfs = one_dfs_diameter(V, edges)
        t3 = perf_counter()

        print(f"Two-BFS Diameter : {out_two_bfs}  (time {(t1-t0)*1e6:.2f} µs)")
        print(f"One-DFS Diameter : {out_one_dfs}  (time {(t3-t2)*1e6:.2f} µs)")
        print(f"Expected         : {exp}")
        print(f"OK? {out_two_bfs == exp and out_one_dfs == exp}\n")

    # Average timing with timeit (short reps; graph sizes are small here)
    V, edges, _ = examples[0]
    reps = 200

    def run_two_bfs():
        two_bfs_diameter(V, edges)

    def run_one_dfs():
        one_dfs_diameter(V, edges)

    avg_two_bfs = timeit.timeit(run_two_bfs, number=reps) / reps
    avg_one_dfs = timeit.timeit(run_one_dfs, number=reps) / reps
    print("--- Average time over", reps, "runs (timeit) ---")
    print(f"Two-BFS avg : {avg_two_bfs*1e6:.2f} µs/run")
    print(f"One-DFS avg : {avg_one_dfs*1e6:.2f} µs/run")


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print("\n==== TOTAL PROGRAM RUNTIME ====")
    print(f"{(end - start):.6f} seconds")
```

**How to use in interviews (talk track while you code):**

* “We’re unweighted; longest path in a tree/forest → **two BFS** per component.”
* “Build adjacency `O(V+E)`, BFS to get farthest `A`, BFS from `A` to get diameter—repeat for each component, keep max.”
* “Overall **O(V+E) time, O(V) space**.”
