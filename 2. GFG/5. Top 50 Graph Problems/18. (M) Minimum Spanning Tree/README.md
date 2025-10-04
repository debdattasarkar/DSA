
---

# 🧩 Minimum Spanning Tree

**Difficulty:** Medium
**Accuracy:** 47.82%
**Submissions:** 183K+
**Points:** 4
**Average Time:** 25m

---

## Problem Statement

Given a weighted, undirected, and connected graph with **V** vertices and **E** edges, your task is to find the **sum of the weights of the edges** in the **Minimum Spanning Tree (MST)** of the graph. The graph is provided as a list of edges, where each edge is represented as **[u, v, w]**, indicating an edge between vertex **u** and vertex **v** with edge weight **w**.

---

## Examples

### Example 1

**Input:**
V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]

**Output:**
4

**Explanation:**
The Spanning Tree resulting in a weight of **4** is shown above.

### Example 2

**Input:**
V = 2, E = 1, Edges = [[0, 1, 5]]

**Output:**
5

**Explanation:**
Only one Spanning Tree is possible which has a weight of **5**.

---

## Constraints

* 2 ≤ V ≤ 1000
* V − 1 ≤ E ≤ (V * (V − 1)) / 2
* 1 ≤ w ≤ 1000
* The graph is connected and doesn’t contain self-loops & multiple edges.

---

## Expected Complexities

* **Time Complexity:** O((V + E) log V)
* **Auxiliary Space:** O(V + E)

---

## Company Tags

Flipkart, Amazon, Microsoft, Samsung, Cisco

---

## Topic Tags

Greedy, Graph, Data Structures, Algorithms

---

## Related Interview Experiences

* Samsung Interview Experience Through CoCubes 2019
* Samsung Bangalore SRI B Interview Experience

---

## 📚 Related Articles

* [Prim’s Minimum Spanning Tree (MST) – Greedy Algorithm 5](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)

---

## 💡 Summary

A **Minimum Spanning Tree (MST)** connects all vertices of a connected, undirected, weighted graph with the **minimum possible total edge weight**, such that no cycles are formed.

There are two famous greedy algorithms to find MST:

* **Kruskal’s Algorithm:** Sorts all edges and picks the smallest edges that don’t form a cycle (using DSU).
* **Prim’s Algorithm:** Expands a tree from an arbitrary vertex by always choosing the smallest edge leading out.

Both algorithms yield the same total weight for MST but may differ in the actual set of edges chosen.

---

---

awesome — here’s an interview-ready package for **Minimum Spanning Tree**:

* clean intuition & a **step-by-step dry run** on the sample,
* two Python solutions in the exact signature you asked for:

  * **Kruskal (DSU)** → most common in interviews
  * **Prim** (both **heap O((V+E)logV)** and **easy O(V²)** variant)
* and a compact **interviewer Q&A** section.

---

## 2) Intuition & step-by-step dry run

**Goal.** In a connected, undirected, weighted graph find the sum of edge weights of any **Minimum Spanning Tree (MST)** (a spanning, acyclic set of exactly `V−1` edges with minimum total weight).

**Two classic greedy ways**

1. **Kruskal:** Sort edges by weight, keep taking the cheapest edge that **doesn’t create a cycle** (use **Disjoint Set Union / Union-Find**).

   * Time: `O(E log E)` (sorting) + near-linear DSU.
2. **Prim:** Grow a tree from any start vertex; always add the **cheapest edge leaving the tree** (use **min-heap** or a simple array).

   * Heap version: `O((V+E) log V)`
   * Array version (easy): `O(V² + E)`

### Dry run (Kruskal) on Example 1

```
V=3, E=3
edges = [ [0,1,5], [1,2,3], [0,2,1] ]
```

1. Sort by weight ⇒ `[(0,2,1), (1,2,3), (0,1,5)]`
2. DSU sets: `{0},{1},{2}`

   * Take (0,2,1): different sets → union → total = 1
   * Take (1,2,3): 1 and 2 are different (2 is with 0) → union → total = 1+3 = 4
   * We already have `V−1 = 2` edges. **Stop.**
     **Answer = 4.**

---

## 3) Python — optimized codes (interview-style)

### A) Kruskal (DSU) — **recommended**

```python
# Python Format
class Solution:
    def spanningTree(self, V, edges):
        """
        Kruskal's Algorithm with Disjoint Set Union (Union-Find).

        Input:
          V     : number of vertices (0..V-1)
          edges : list of [u, v, w] for undirected graph

        Returns:
          Sum of weights of the MST.

        Complexity:
          - Sort edges: O(E log E)
          - DSU ops:   near O(E α(V)) ~ O(E)
          - Total:     O(E log E)
          - Space:     O(V) for DSU
        """

        # --- Disjoint Set Union (Union-Find) with path compression + union by size ---
        parent = list(range(V))
        size   = [1] * V

        def find(x):
            # Amortized ~O(1) with path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            # Union by size; returns True if merged (i.e., they were in different sets)
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra]  += size[rb]
            return True

        # Sort all edges by weight  -> O(E log E)
        edges.sort(key=lambda e: e[2])

        mst_wt = 0
        picked = 0

        # Greedily pick smallest non-cycle edges
        for u, v, w in edges:
            if union(u, v):             # if this does not create a cycle
                mst_wt += w
                picked += 1
                if picked == V - 1:     # MST complete
                    break

        return mst_wt
```

---

### B) Prim’s algorithm — **heap (optimal)**

```python
import heapq

class Solution:
    def spanningTree(self, V, edges):
        """
        Prim's Algorithm with a min-heap.

        Build adjacency list, start from node 0, repeatedly take the minimum
        edge going out of the growing tree.

        Complexity:
          - Building adj: O(E)
          - Heap ops:     O((V+E) log V)
          - Space:        O(V+E)
        """
        # Build adjacency list for undirected graph
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = [False] * V
        mst_wt = 0
        taken  = 0

        # (weight, node). Start with node 0 at cost 0
        heap = [(0, 0)]
        while heap and taken < V:
            w, u = heapq.heappop(heap)      # O(log V)
            if visited[u]:
                continue
            visited[u] = True
            mst_wt += w                      # add this edge's weight (0 for the start)
            taken  += 1

            # Push neighbors that leave the tree
            for v, w2 in adj[u]:
                if not visited[v]:
                    heapq.heappush(heap, (w2, v))

        return mst_wt
```

---

### (Optional) Prim’s algorithm — **easy O(V²)** (no heap, very teachable)

```python
class Solution:
    def spanningTree(self, V, edges):
        """
        Prim's Algorithm with O(V^2) selection (no heap).
        Good to explain in interviews; plenty fast for V <= 1000.

        Complexity:
          - Build adj: O(E)
          - For V iterations, pick min key in O(V) and relax neighbors: O(V^2 + E)
          - Space: O(V + E)
        """
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = 10**18
        in_mst = [False] * V
        key    = [INF] * V       # min edge weight to connect this node to MST
        key[0] = 0

        mst_wt = 0
        for _ in range(V):
            # Pick the not-yet-in-MST vertex with minimum key  -> O(V)
            u = -1
            best = INF
            for i in range(V):
                if not in_mst[i] and key[i] < best:
                    best, u = key[i], i

            in_mst[u] = True
            mst_wt += best

            # Relax neighbors
            for v, w in adj[u]:
                if not in_mst[v] and w < key[v]:
                    key[v] = w

        return mst_wt
```

> All three return **the sum of weights** of an MST. The first two match the expected time complexities in the problem statement.

---

## 4) Interview-style Q&A

**Q1. Kruskal vs Prim — when to prefer which?**

* **Kruskal**: simple on **edge list** input; great if the graph is **sparse** and sorting edges is straightforward; DSU implementation is a common interview topic.
* **Prim**: convenient when you already have/need an **adjacency structure**; the **heap version** gives `O((V+E)logV)`; the **O(V²)** version is easy to code and fine for `V ≤ 1000`.

**Q2. Why do these greedy algorithms work?**
They both rely on the **cut property**: The lightest edge crossing any cut of the graph is safe to include in **some** MST. Kruskal repeatedly picks global lightest safe edges; Prim repeatedly picks the lightest edge leaving the growing tree.

**Q3. Does MST remain unique?**
Not necessarily. If **all edge weights are distinct**, the MST is **unique**. Otherwise different valid MSTs may exist (but their **total weight** is the same minimum).

**Q4. Can MST have negative weights?**
Yes. Both algorithms still work; sorting (Kruskal) and min-edge selection (Prim) naturally handle negatives.

**Q5. What if the graph is disconnected?**
An MST doesn’t exist; each connected component has its own **Minimum Spanning Forest**. This problem statement guarantees **connected**, so we don’t need special handling.

**Q6. Why does Kruskal need DSU?**
To detect cycles efficiently as we add edges. DSU supports `find/union` in **amortized near O(1)**, keeping Kruskal `O(E log E)` overall.

**Q7. Can we produce the actual set of edges, not just the sum?**
Yes: in Kruskal, store each accepted edge; in Prim, store the parent for each vertex when you relax it. Not needed here, but easy to add.

**Q8. Complexity recap?**

* **Kruskal:** `O(E log E)` time, `O(V)` space (DSU).
* **Prim (heap):** `O((V+E) log V)` time, `O(V+E)` space.
* **Prim (array):** `O(V² + E)` time, `O(V+E)` space.

---

---

here you go — a **runnable, interview-style full program** for **Minimum Spanning Tree** that:

* implements **Kruskal (DSU)** and **Prim (min-heap)**,
* prints results for the given samples,
* and uses **timeit** to report the **average runtime per call** for both methods.

I’ve added **inline comments** at each step clarifying **time/space** costs.

---

## 5) Full Python Program (with inline complexity notes + timings)

```python
"""
Minimum Spanning Tree (MST) — Full Demo with Timing
---------------------------------------------------
Two classic greedy algorithms that both return the MST total weight:

A) Kruskal (with Disjoint Set Union / Union-Find)
   - Sort edges by weight, take lightest non-cycling edge.
   - Time  : O(E log E)   [sorting dominates; DSU is near O(1) amortized]
   - Space : O(V)         [DSU parent/size arrays]

B) Prim (with min-heap / priority queue)
   - Grow a tree from an arbitrary start vertex; always take minimum outgoing edge.
   - Time  : O((V + E) log V) [heap pushes/pops]
   - Space : O(V + E)         [adjacency + heap + visited]

Driver:
  * Runs two examples from the prompt.
  * Benchmarks both solutions using timeit (average seconds/run).
"""

from typing import List
import heapq
import timeit


# ------------------------------- A) Kruskal (DSU) ------------------------------- #
class SolutionKruskal:
    def spanningTree(self, V: int, edges: List[List[int]]) -> int:
        """
        Parameters
        ----------
        V      : number of vertices (0..V-1)
        edges  : list of edges [u, v, w] (undirected)

        Returns
        -------
        int : sum of weights in any MST

        Complexity annotations (by section)
        -----------------------------------
        - Build DSU arrays: O(V) space/time
        - Sort edges by weight: O(E log E) time
        - Loop edges with DSU unions: ~O(E α(V)) ≈ O(E) time, O(1) extra space per op
        """
        # --- Disjoint Set Union (Union-Find) with path compression + union by size --- #
        parent = list(range(V))   # O(V) space
        size   = [1] * V          # O(V) space

        def find(x: int) -> int:
            # Path compression → amortized ~O(1)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            # Union by size; returns True if merged
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra]  += size[rb]
            return True

        # Sort edges by weight — O(E log E)
        edges_sorted = sorted(edges, key=lambda e: e[2])

        mst_weight = 0
        chosen = 0
        # Greedily add edges that don't form a cycle
        for u, v, w in edges_sorted:    # O(E)
            if union(u, v):             # near O(1)
                mst_weight += w
                chosen += 1
                if chosen == V - 1:     # stop early when MST is complete
                    break

        return mst_weight


# ------------------------------- B) Prim (min-heap) ------------------------------- #
class SolutionPrim:
    def spanningTree(self, V: int, edges: List[List[int]]) -> int:
        """
        Prim's Algorithm using a min-heap priority queue.

        Build adjacency (O(E) time/space), then push candidate edges from the tree
        and pop the cheapest until all V vertices are added.

        Time  : O((V + E) log V)
        Space : O(V + E)
        """
        # Build adjacency list — O(E) time/space
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visited = [False] * V    # O(V) space
        heap = [(0, 0)]          # (weight, vertex); start at vertex 0 with cost 0
        mst_weight = 0
        picked = 0

        # Extract-min loop — each vertex is inserted to MST exactly once
        while heap and picked < V:
            w, u = heapq.heappop(heap)      # O(log V)
            if visited[u]:
                continue
            visited[u] = True
            mst_weight += w
            picked += 1

            # Push all outgoing edges to unvisited neighbors — O(deg(u) log V)
            for v, w2 in adj[u]:
                if not visited[v]:
                    heapq.heappush(heap, (w2, v))  # O(log V)

        return mst_weight


# ------------------------------- Timing helper ------------------------------- #
def bench(func, *args, number=3000) -> float:
    """
    Measure average seconds/run using timeit.
    For tiny inputs, Python overhead dominates; use for *relative* comparison.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------ Demo ------------------------------------ #
if __name__ == "__main__":
    print("=== Minimum Spanning Tree — Kruskal vs Prim (min-heap) ===\n")

    # Example 1 from prompt
    V1 = 3
    edges1 = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
    print(">>> Example 1")
    print("V =", V1, "Edges =", edges1)
    kr = SolutionKruskal().spanningTree(V1, edges1)
    pr = SolutionPrim().spanningTree(V1, edges1)
    print("Kruskal MST weight :", kr)   # expected 4
    print("Prim    MST weight :", pr, "\n")

    # Example 2 from prompt
    V2 = 2
    edges2 = [[0, 1, 5]]
    print(">>> Example 2")
    print("V =", V2, "Edges =", edges2)
    kr2 = SolutionKruskal().spanningTree(V2, edges2)
    pr2 = SolutionPrim().spanningTree(V2, edges2)
    print("Kruskal MST weight :", kr2)  # expected 5
    print("Prim    MST weight :", pr2, "\n")

    # A slightly larger dense-ish graph to show timings
    V3 = 8
    edges3 = [
        [0,1,4],[0,2,3],[1,2,1],[1,3,2],[2,3,4],[3,4,2],[4,5,6],
        [2,5,5],[1,5,3],[5,6,2],[6,7,1],[4,7,7],[3,6,3]
    ]

    print("=== Timings (average seconds per run) ===")
    runs_small = 20000
    tK_small = bench(SolutionKruskal().spanningTree, V1, edges1, number=runs_small)
    tP_small = bench(SolutionPrim().spanningTree,    V1, edges1, number=runs_small)
    print(f"Small (V={V1}) runs={runs_small:5d}:  Kruskal {tK_small:.8e}s | Prim {tP_small:.8e}s")

    runs_med = 8000
    tK_med = bench(SolutionKruskal().spanningTree, V3, edges3, number=runs_med)
    tP_med = bench(SolutionPrim().spanningTree,    V3, edges3, number=runs_med)
    print(f"Medium(V={V3}) runs={runs_med:5d}:  Kruskal {tK_med:.8e}s | Prim {tP_med:.8e}s")

    print("\nNote: runtimes vary by machine/Python version. Both algorithms are optimal Big-O for MST.\n")
```

### What the program prints

* For **Example 1**: both algorithms output **4**.
* For **Example 2**: both output **5**.
* Then you’ll see **average seconds/run** for Kruskal and Prim on small and medium graphs.

---

## 6) Real-World Use Cases (the important ones)

1. **Network Design / Cost-Optimal Connectivity**
   Building least-cost networks (fiber, power grid, water pipelines) where you must connect all sites with minimum overall cabling/pipe cost.

2. **Clustering (Single-Linkage via MST)**
   Use MST to build a dendrogram; cutting the largest `k−1` edges yields `k` clusters — common in unsupervised learning.

3. **Approximate TSP (Christofides, etc.)**
   MST is a building block for approximation algorithms for Traveling Salesman in metric spaces.

4. **Image Processing / Segmentation**
   Graph-based segmentation often uses MST (e.g., Felzenszwalb-Huttenlocher) to group pixels while minimizing inter-cluster edge weights.

5. **Circuit/PCB Layout & VLSI**
   Wire routing / Steiner tree heuristics start with MST to minimize interconnect length before refinement.