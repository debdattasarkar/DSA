
---

# 🌀 Undirected Graph Cycle

**Difficulty:** Medium
**Accuracy:** 30.13%
**Submissions:** 648K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

Given an **undirected graph** with **V vertices** and **E edges**, represented as a 2D vector `edges[][]`, where each entry `edges[i] = [u, v]` denotes an edge between vertices **u** and **v**, determine whether the graph contains a **cycle** or not.
The graph can have **multiple components**.

---

## 🧩 Examples

### **Example 1:**

**Input:**

```
V = 4, E = 4
edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
```

**Output:**

```
true
```

**Explanation:**
1 -> 2 -> 0 -> 1 is a cycle.

---

### **Example 2:**

**Input:**

```
V = 4, E = 3
edges[][] = [[0, 1], [1, 2], [2, 3]]
```

**Output:**

```
false
```

**Explanation:**
No cycle in the graph.

---

## ⚙️ Constraints

```
1 ≤ V ≤ 10^5
1 ≤ E = edges.size() ≤ 10^5
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V)

---

## 🏢 Company Tags

* Flipkart
* Amazon
* Microsoft
* Samsung
* MakeMyTrip
* Oracle
* Adobe

---

## 🧠 Topic Tags

* DFS
* Graph
* Union-Find
* Data Structures
* Algorithms

---

## 💼 Related Interview Experiences

* Makemytrip Interview Experience Set 13 On Campus For Full Time

---

## 📚 Related Articles

* Detect Cycle In An Undirected Graph Using BFS
* Detect Cycle Undirected Graph

---

---

awesome — let’s crack **Undirected Graph Cycle Detection** the interview way.

---

## 2) Intuition + step-by-step dry run

### Problem

You’re given `V` vertices (`0 … V-1`) and an **edge list** `edges = [[u,v], ...]` for an **undirected** graph.
Return `True` if **any cycle** exists, else `False`.

### Two standard approaches

1. **DSU / Union-Find (most expected)**

   * Initially, every node is its own parent.
   * For each undirected edge `(u, v)`:

     * If `find(u) == find(v)`, then `u` and `v` are already connected → adding `(u,v)` forms a **cycle** → return `True`.
     * Otherwise, **union** their sets and continue.
   * If all edges processed and no conflict → `False`.

2. **Graph traversal (BFS/DFS) with parent tracking**

   * Convert to adjacency list.
   * For each unvisited node, run BFS/DFS:

     * On visiting `u → v`, if `v` is visited and `v != parent[u]`, you found a **back edge** → cycle.
   * If no such back edge appears → acyclic.

Both are **O(V+E)** time. DSU is very clean on edge lists; DFS/BFS is great if adjacency is already built.

---

### Dry run (Example 1)

```
V = 4
edges = [[0,1], [0,2], [1,2], [2,3]]

Process with DSU:
parents initially: [0,1,2,3]

Edge (0,1): find(0)=0, find(1)=1 -> different -> union -> parent[1]=0 (or by rank)
Edge (0,2): find(0)=0, find(2)=2 -> different -> union -> parent[2]=0
Edge (1,2): find(1)->0, find(2)->0 -> SAME -> cycle => return True
```

Matches the visual cycle `1-2-0-1`.

---

## 3) Python implementations (interview-ready)

All methods match your signature:

```python
class Solution:
    def isCycle(self, V, edges):
        # code here
```

### A) DSU / Union-Find (path compression + rank) — **recommended**

```python
class Solution:
    def isCycle(self, V, edges):
        """
        Detect cycle in an undirected graph using DSU (Union-Find).
        If an edge connects two vertices already in the same set, a cycle exists.

        Time  : O((V + E) * α(V)) ~ O(V + E)   [α is inverse Ackermann]
        Space : O(V)
        """
        # parent and rank arrays
        parent = list(range(V))  # O(V)
        rank   = [0] * V         # O(V)

        def find(x):
            # Path compression: amortized ~O(1)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            # Union by rank: amortized ~O(1)
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # already in same set -> using this edge forms a cycle
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        for u, v in edges:         # O(E)
            if not union(u, v):    # found cycle
                return True
        return False                # no cycle
```

### B) DFS (parent tracking) — also common

```python
from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        """
        Detect cycle in an undirected graph using DFS and parent tracking.
        If we see a visited neighbor that is NOT the parent -> cycle.

        Time  : O(V + E)
        Space : O(V + E) for adjacency + O(V) recursion/visited
        """
        # Build adjacency list   O(V + E)
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        def dfs(u, parent):
            visited[u] = True
            for w in adj[u]:
                if not visited[w]:
                    if dfs(w, u):
                        return True
                elif w != parent:
                    # back edge in undirected graph -> cycle
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
        return False
```

### C) BFS (parent tracking) — equivalent to DFS flavor

```python
from collections import deque

class Solution:
    def isCycle(self, V, edges):
        """
        BFS with parent tracking for undirected graphs.

        Time  : O(V + E)
        Space : O(V + E)
        """
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V
        for s in range(V):
            if visited[s]: 
                continue
            q = deque([(s, -1)])
            visited[s] = True
            while q:
                u, p = q.popleft()
                for w in adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        q.append((w, u))
                    elif w != p:
                        return True
        return False
```

> Which to pick?
> **DSU** is the shortest and cleanest when edges are already a list.
> **DFS/BFS** are great if you already have / need adjacency.

---

## 4) Interview Q&A (high-yield)

**Q1. Why does Union-Find detect cycles in undirected graphs?**
If an edge `(u, v)` connects two vertices already in the **same connected component** (`find(u) == find(v)`), adding it would create an additional path between them → **cycle**.

**Q2. What optimizations do you use in DSU and why?**

* **Path compression** in `find` and **union by rank/size** keep the trees shallow, giving almost O(1) time per operation (formally `O(α(V))`).

**Q3. Complexity of DSU approach?**
**Time:** `O((V+E) * α(V)) ≈ O(V+E)`; **Space:** `O(V)`.

**Q4. How does DFS/BFS detect cycles in undirected graphs?**
During traversal, if you see an edge to a **visited neighbor** that is **not the parent**, it’s a **back edge** → cycle.

**Q5. What about multiple components?**
Start DFS/BFS (or DSU initialization) for **each unvisited node**; DSU implicitly handles components.

**Q6. Will self-loops or parallel edges matter?**

* A **self-loop** `(u,u)` is an immediate cycle.
* **Parallel edges** `(u,v)` twice: the second edge will report a cycle in DSU or appear as a non-parent visited neighbor in DFS/BFS.

**Q7. When would you prefer DFS/BFS over DSU?**
If you **already have adjacency** or need to do **other graph work** (like counting components) in one pass, DFS/BFS may be more natural.

---

---

you got it — here’s a **runnable, interview-style full program** for **Cycle Detection in an Undirected Graph** that:

* implements **both** approaches with your required signature `isCycle(self, V, edges)`:

  * **DSU (Union-Find with path compression + rank)** — primary, very common in interviews
  * **DFS (parent tracking)** — equally standard
* shows **inputs & outputs** for sample graphs (cyclic & acyclic),
* and **benchmarks** both with `timeit` on a larger random graph.

I’ve sprinkled **inline comments** stating **time / space** where they matter.

---

## 5) Full Python program (with inline complexity notes + timing)

```python
"""
Undirected Graph Cycle Detection
--------------------------------
We provide two solutions with the *exact* required signature:

  1) DSU / Union-Find (optimized: path compression + union-by-rank)
  2) DFS with parent tracking

Complexities:
  • DSU    : Time O((V+E) * α(V)) ≈ O(V+E), Space O(V)
  • DFS    : Time O(V+E), Space O(V+E) adjacency + O(V) recursion/visited

The script also:
  • Runs two small examples (one cyclic, one acyclic) and prints outputs
  • Benchmarks both approaches with timeit on a larger random graph
"""

from collections import deque
from typing import List, Tuple
import random
import timeit


# =============================== DSU / Union-Find =============================== #
class SolutionDSU:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        """
        Detect a cycle in an undirected graph using DSU.

        Idea: For each edge (u, v), if find(u) == find(v) -> they are already
              in the same component; adding edge closes a loop -> cycle.

        Time  : O((V+E) * α(V)) amortized, ~ O(V+E)
        Space : O(V) for parent & rank
        """
        parent = list(range(V))  # O(V) space
        rank   = [0] * V         # O(V) space

        def find(x: int) -> int:
            # Path compression => amortized near O(1)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            # Union by rank => amortized near O(1)
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # cycle would form
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        # Process each edge exactly once  -> O(E) finds/unions
        for u, v in edges:
            if not union(u, v):   # already same set => cycle
                return True
        return False


# ===================================== DFS ===================================== #
class SolutionDFS:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        """
        Detect a cycle using DFS with parent tracking.

        Build adjacency, then for each unvisited node run DFS:
          If you find an edge to an already-visited neighbor that is NOT
          the parent, it's a back-edge -> cycle.

        Time  : O(V + E)
        Space : O(V + E) adjacency + O(V) visited/recursion
        """
        # Build undirected adjacency list  -> O(V+E) time/space
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        def dfs(u: int, parent: int) -> bool:
            visited[u] = True
            for w in adj[u]:
                if not visited[w]:
                    if dfs(w, u):
                        return True
                elif w != parent:
                    # already visited and not parent -> back-edge
                    return True
            return False

        for s in range(V):
            if not visited[s]:
                if dfs(s, -1):
                    return True
        return False


# ============================= Helper / Benchmarking ============================= #
def make_random_undirected_graph(V: int, E: int) -> List[List[int]]:
    """
    Produce a random simple undirected graph with V nodes and ~E edges.
    (No self-loops, no duplicate edges.)
    Average case generation time O(E). Space O(V+E).
    """
    rng = random.Random(42)
    edges = set()
    while len(edges) < E:
        u = rng.randrange(V)
        v = rng.randrange(V)
        if u == v:
            continue
        a, b = (u, v) if u < v else (v, u)
        if (a, b) not in edges:
            edges.add((a, b))
    return [[u, v] for (u, v) in edges]


def bench(func, *args, number=30) -> float:
    """
    Return average seconds per call using timeit.
    For small inputs, Python overhead dominates; use for *relative* comparison.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ========================================= Demo ========================================= #
if __name__ == "__main__":
    print("=== Undirected Graph Cycle — DSU vs DFS ===\n")

    # ---------- Example 1: cyclic ----------
    V1 = 4
    edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]  # 0-1-2-0 forms a cycle
    print(">>> Example 1 (cyclic)")
    print("V =", V1, "Edges =", edges1)
    print("DSU ->", SolutionDSU().isCycle(V1, edges1), " (expected: True)")
    print("DFS ->", SolutionDFS().isCycle(V1, edges1), " (expected: True)\n")

    # ---------- Example 2: acyclic ----------
    V2 = 4
    edges2 = [[0, 1], [1, 2], [2, 3]]  # chain, no cycle
    print(">>> Example 2 (acyclic)")
    print("V =", V2, "Edges =", edges2)
    print("DSU ->", SolutionDSU().isCycle(V2, edges2), " (expected: False)")
    print("DFS ->", SolutionDFS().isCycle(V2, edges2), " (expected: False)\n")

    # ---------- Timing on a larger random graph ----------
    print("=== Timings (average seconds per run) ===")
    V3 = 50_000
    E3 = 120_000  # sparse graph
    edges3 = make_random_undirected_graph(V3, E3)

    runs = 5
    t_dsu = bench(SolutionDSU().isCycle, V3, edges3, number=runs)
    t_dfs = bench(SolutionDFS().isCycle, V3, edges3, number=runs)

    print(f"Random graph: V={V3}, E≈{E3}  runs={runs}")
    print(f"DSU : {t_dsu:.6f} s/run")
    print(f"DFS : {t_dfs:.6f} s/run")

    print("\nNotes:")
    print(" • DSU is very compact on edge lists and near O(1) per union/find (amortized).")
    print(" • DFS requires building adjacency but is likewise O(V+E).")
    print(" • Both handle multiple components naturally.")
```

### What you’ll see when you run it

* Example 1 → `True` for both DSU & DFS (cycle present)
* Example 2 → `False` for both (no cycle)
* Two timing lines comparing DSU vs DFS on a large random graph (numbers vary by machine)

---

## 6) Real-World Use Cases (the few that matter)

1. **Network & Topology validation**
   Prevent loops in physical/virtual network topologies (e.g., L2 loop detection before enabling links).

2. **File-sync & replication graphs**
   Ensure replication relationships (peer-to-peer mirroring) don’t accidentally introduce circular synchronization paths.

3. **Dependency graphs for resources**
   Validate that “locks” or resource dependencies in systems / scripts don’t form cycles that could deadlock.

4. **Road / utility planning**
   Quickly test whether adding a proposed undirected link creates unwanted cycles (e.g., during tree-like infrastructure design).