# 🧠 Articulation Point - II

**Difficulty:** Hard
**Accuracy:** 55.15%
**Submissions:** 32K+
**Points:** 8
**Average Time:** 30m

---

## 🧩 Problem Statement

You are given an **undirected graph** with `V` vertices and `E` edges.
The graph is represented as a 2D array `edges[][]`, where each element `edges[i] = [u, v]` indicates an **undirected edge** between vertices `u` and `v`.

Your task is to **return all the articulation points** (or **cut vertices**) in the graph.

> An **articulation point** is a vertex whose **removal**, along with all its **connected edges**, increases the number of **connected components** in the graph.

---

### 🧾 Note:

* The graph **may be disconnected**, i.e., it may consist of more than one connected component.
* If no such point exists, return **`[-1]`**.

---

## 🧮 Examples

### **Example 1**

#### Input:

```
V = 5
edges = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
```

#### Output:

```
[1, 4]
```

#### Explanation:

Removing vertex **1** or **4** will disconnect the graph as follows:

* Removing vertex `1` disconnects vertex `0` from the rest of the graph.
* Removing vertex `4` disconnects vertices `2` and `3` from the rest.

So, `[1, 4]` are articulation points.

**Visual Representation:**

```
    0
    |
    1
     \
      4
     / \
    2 - 3
```

Removing **1** or **4** increases the number of disconnected components.

---

### **Example 2**

#### Input:

```
V = 4
edges = [[0, 1], [0, 2]]
```

#### Output:

```
[0]
```

#### Explanation:

Removing vertex `0` will increase the number of disconnected components to **3**, since both `1` and `2` become isolated.

---

## ⚙️ Constraints

```
1 ≤ V, E ≤ 10^4
```

---

## 🧮 Expected Complexities

| Metric              | Complexity |
| :------------------ | :--------- |
| **Time Complexity** | O(V + E)   |
| **Auxiliary Space** | O(V)       |

---

## 🏷️ Topic Tags

* **Graph**
* **Data Structures**

---

## 📚 Related Articles

* [Articulation Points or Cut Vertices in a Graph (GeeksforGeeks)](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/)

---

---

Here’s a crisp, interview-style walkthrough + code you can drop in and run.

---

# 2) Explanation + step-by-step dry run

### What’s an articulation point?

In an **undirected** graph, a vertex `u` is an **articulation point (cut vertex)** if removing `u` (and its incident edges) **increases the number of connected components**.

### Core idea (Tarjan’s DFS):

Do a single DFS and compute for each node:

* `disc[u]`: time when `u` is first discovered.
* `low[u]`: the smallest discovery time reachable from `u` by taking **zero or more tree edges followed by at most one back edge**.

Rules to mark `u` as articulation point:

1. **Root rule**: if `u` is a DFS root and has **≥ 2** DFS children → `u` is an articulation point.
2. **Bridge-like rule**: for any **non-root** `u`, if there exists a child `v` with `low[v] >= disc[u]` → no back edge from `v`’s subtree reaches an ancestor of `u`; cutting `u` separates `v`’s subtree → `u` is an articulation point.

We must run DFS from **every unvisited node** (graph can be disconnected).

---

### Dry run on the sample

```
V = 5
edges = [[0,1], [1,4], [4,3], [4,2], [2,3]]
Adj:
0: 1
1: 0,4
2: 4,3
3: 4,2
4: 1,3,2
```

One possible DFS (start at 0):

* Visit 0: `disc[0]=0`, `low[0]=0`

  * Go to 1: `disc[1]=1`, `low[1]=1`

    * Go to 4: `disc[4]=2`, `low[4]=2`

      * Go to 3: `disc[3]=3`, `low[3]=3`

        * 3 → 4 is parent; 3 → 2 is unvisited

          * Go to 2: `disc[2]=4`, `low[2]=4`

            * 2 → 4 is parent; 2 → 3 is **back edge** to an already discovered ancestor (3)

              * update `low[2] = min(4, disc[3]=3) = 3`
          * return to 3: update `low[3] = min(3, low[2]=3) = 3`
      * return to 4: update `low[4] = min(2, low[3]=3) = 2`
      * 4 → 2 is visited; consider back edge `disc[2]=4` (> disc[4]), `low[4]` stays 2
    * return to 1: update `low[1] = min(1, low[4]=2) = 1`
    * Check AP condition for **non-root** `u=1` with child `v=4`:

      * `low[4] (2) >= disc[1] (1)` → **true**, so **1 is an articulation point**
  * return to 0: update `low[0] = min(0, low[1]=1) = 0`
* Root 0 has only **one** DFS child (node 1) → root rule **not** triggered.

Now, check node 4 while unwinding:

* For parent `1`, child `3` under `4` had `low[3]=3` and `disc[4]=2` → `low[3] (3) >= disc[4] (2)` → **4 is also an articulation point**.

**Result:** `{1, 4}` — removing either splits the graph.

---

# 3) Optimized code (Tarjan, O(V+E)) + Brute force (O(V·(V+E)))

Both follow the requested Python format and accept an **edge list**.
(We ignore self-loops and collapse duplicate edges when building the adjacency list.)

## A) Optimized Tarjan DFS (what interviewers expect)

```python
class Solution:
    def articulationPoints(self, V, edges):
        """
        Tarjan's DFS to find articulation points in an undirected (possibly disconnected) graph.
        Time:  O(V + E)
        Space: O(V + E)
        """

        # Build adjacency list (undirected). Ignore self-loops.
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:  # self loop doesn't affect articulation logic
                continue
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * V             # discovery times
        low = [0] * V               # low-link values
        is_ap = [False] * V         # articulation point flags
        time = 0                    # global DFS timestamp

        def dfs(u: int, parent: int) -> None:
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            child_count = 0  # number of DFS tree children (for root rule)

            for w in adj[u]:
                if w == parent:
                    continue
                if disc[w] == -1:
                    child_count += 1
                    dfs(w, u)

                    # On return, propagate low-link value up
                    low[u] = min(low[u], low[w])

                    # Non-root articulation condition:
                    # If the earliest reachable time from w's subtree is
                    # not earlier than u's discovery, cutting u disconnects that subtree.
                    if parent != -1 and low[w] >= disc[u]:
                        is_ap[u] = True
                else:
                    # Back edge to an ancestor (or already visited neighbor): update low[u]
                    low[u] = min(low[u], disc[w])

            # Root articulation condition:
            if parent == -1 and child_count >= 2:
                is_ap[u] = True

        # Graph can be disconnected: run DFS from every unvisited node.
        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        ans = [i for i, flag in enumerate(is_ap) if flag]
        return ans if ans else [-1]
```

### Why it works (intuition bullets you can say in an interview)

* `disc[u]` timestamps the entry of `u` into DFS.
* `low[u]` asks: “what is the earliest discovery time reachable from `u` if I may take as many tree edges as I want and **one** back edge?”
* If a child `v` of `u` can’t reach an ancestor of `u` (`low[v] >= disc[u]`), then `u` is the “only bridge upward” for that subtree — removing `u` disconnects it.

---

## B) Simple Brute Force (check components after removing each vertex)

```python
class Solution:
    def articulationPoints(self, V, edges):
        """
        Brute-force: remove each vertex u and compare component count before/after.
        Time:  O(V * (V + E))  -- too slow for the largest constraints, but great as a correctness baseline
        Space: O(V + E)
        """
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:
                continue
            adj[u].append(v)
            adj[v].append(u)

        # Helper: count connected components, optionally skipping `banned` vertex
        def count_components(banned: int | None) -> int:
            seen = [False] * V
            comps = 0

            def dfs(s: int):
                stack = [s]
                seen[s] = True
                while stack:
                    x = stack.pop()
                    for y in adj[x]:
                        if y == banned or seen[y]:
                            continue
                        seen[y] = True
                        stack.append(y)

            for i in range(V):
                if i == banned or seen[i]:
                    continue
                comps += 1
                dfs(i)
            return comps

        original = count_components(banned=None)
        ap = []
        for u in range(V):
            after = count_components(banned=u)
            if after > original:
                ap.append(u)

        return ap if ap else [-1]
```

---

# 4) Interview Q&A (the ones you’re likely to be asked)

**Q1. What’s the difference between an articulation point and a bridge?**

* A **bridge** is an edge whose removal increases #components.
* An **articulation point** is a **vertex** whose removal increases #components.
* Both can be found with the same DFS infrastructure (`disc/low`), with different conditions (`low[v] > disc[u]` for a bridge; `low[v] >= disc[u]` for AP, plus the root rule).

**Q2. Why is the root a special case?**

* The root has no parent, so the “`low[child] >= disc[root]`” test alone is not sufficient.
* A root is an articulation point **iff** it has **≥ 2** DFS children — that means it’s a junction for at least two disjoint DFS subtrees.

**Q3. What does `low[u]` represent intuitively?**

* The **earliest discovery time** reachable from `u` by going down the DFS tree edges and using **at most one back edge**.

**Q4. Why do we check `low[v] >= disc[u]` for non-root `u`?**

* If `low[v] < disc[u]`, the subtree of `v` can reach an ancestor of `u` via some back edge, so removing `u` won’t separate `v`’s subtree.
* If `low[v] >= disc[u]`, there is **no** such back edge — `u` is the only gateway upwards for that subtree.

**Q5. Do we need to sort the answer?**

* If the problem statement requires sorted order, return `sorted(indices)`.
* Many online judges accept natural DFS order; when in doubt, **sort**.

**Q6. How do you handle disconnected graphs?**

* Run DFS from every unvisited node. Articulation points can appear in any component.

**Q7. Can multiple edges or self-loops affect the algorithm?**

* **Self-loops** do not create articulation points; they can be ignored.
* **Parallel edges** don’t break correctness but can create redundant back-edges; filtering duplicates is optional.

**Q8. Complexity of Tarjan’s algorithm?**

* **Time:** `O(V + E)`
* **Space:** `O(V + E)` for recursion + adjacency.

**Q9. What about recursion depth?**

* Worst case depth is `O(V)`. In Python for very deep graphs you may need to raise recursion limit or write an iterative DFS.

**Q10. How would you test corner cases?**

* Single node / single edge.
* A tree (every non-leaf except root w/1 child is AP? In a tree, **any node with degree ≥ 2** can be AP depending on position; run the algo to be safe).
* Fully connected clique (no APs).
* Disconnected graph.

---

## Tiny sanity check you can run mentally

* **Chain** `0-1-2-3`: APs are `{1,2}`.
* **Triangle** `0-1-2-0`: no APs → `[-1]`.

---

---

Here’s a complete, runnable Python program for **Articulation Point – II (edge-list input, undirected graph)** with:

* Clear inline comments (including **time & space complexity** notes right where they matter)
* A tiny **driver** that feeds example inputs and prints outputs
* A quick **runtime measurement** using `timeit.default_timer` (lightweight and precise)

---

## Full Program (drop-in)

```python
# ------------------------------------------------------------
# Articulation Point – II
# Find all articulation points (cut vertices) in an undirected
# graph given as an edge list. If none exist, return [-1].
#
# Core method: Tarjan's DFS with discovery/low-link times.
# ------------------------------------------------------------

from timeit import default_timer as timer
from typing import List


class Solution:
    def articulationPoints(self, V: int, edges: List[List[int]]) -> List[int]:
        """
        Tarjan's algorithm for articulation points on an undirected graph.

        Build adjacency: O(V + E) time, O(V + E) space
        DFS traversal:   O(V + E) time, O(V) recursion stack + arrays

        Total (asymptotic):
          - Time   : O(V + E)
          - Space  : O(V + E)
        """

        # ---- Build adjacency list (ignore self loops) ----
        # Time: O(E), Space: O(V + E)
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:        # Self-loop has no effect on AP logic
                continue
            adj[u].append(v)
            adj[v].append(u)

        # ---- Arrays for DFS bookkeeping ----
        # disc[u] = discovery time of u; -1 => unvisited
        # low[u]  = earliest discovery time reachable from u by:
        #           tree edges + at most one back edge
        # Space for all arrays: O(V)
        disc = [-1] * V
        low = [0] * V
        is_ap = [False] * V

        # Monotonic DFS timestamp
        time = 0

        def dfs(u: int, parent: int) -> None:
            """
            Standard Tarjan DFS:
              - Set disc[u] = low[u] = time
              - Recurse to neighbors
              - On return, update low[u] via low[child]
              - Apply articulation rules
            Time (across whole run): O(V + E)
            Space: O(V) recursion depth worst-case
            """
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            child_count = 0  # number of DFS tree children (for root rule)

            for w in adj[u]:
                if w == parent:
                    continue
                if disc[w] == -1:
                    child_count += 1
                    dfs(w, u)

                    # Propagate low-link from child back to u
                    low[u] = min(low[u], low[w])

                    # Non-root articulation condition:
                    # If child's subtree can't reach an ancestor of u,
                    # cutting u separates that subtree.
                    if parent != -1 and low[w] >= disc[u]:
                        is_ap[u] = True
                else:
                    # Back edge -> update low[u] by neighbor's discovery time
                    low[u] = min(low[u], disc[w])

            # Root articulation condition:
            if parent == -1 and child_count >= 2:
                is_ap[u] = True

        # ---- Run DFS on every component (graph may be disconnected) ----
        # Time: O(V + E)
        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        # ---- Collect result ----
        # Time: O(V), Space: O(k) for k articulation points
        res = [i for i, flag in enumerate(is_ap) if flag]
        return res if res else [-1]


# ------------------------------------------------------------
# Example usage + simple timing
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # -----------------------
    # Test Case 1 (from prompt-like example)
    # Graph:
    # V = 5
    # edges = [[0,1], [1,4], [4,3], [4,2], [2,3]]
    # Expected APs: [1, 4]
    # -----------------------
    V1 = 5
    edges1 = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
    start = timer()
    ans1 = sol.articulationPoints(V1, edges1)
    end = timer()
    print("Input 1:")
    print("V =", V1, ", edges =", edges1)
    print("Articulation Points:", ans1)
    print(f"Time taken (s): {end - start:.6f}\n")

    # -----------------------
    # Test Case 2
    # Single biconnected component (triangle): no articulation points
    # Expected: [-1]
    # -----------------------
    V2 = 3
    edges2 = [[0, 1], [1, 2], [2, 0]]
    start = timer()
    ans2 = sol.articulationPoints(V2, edges2)
    end = timer()
    print("Input 2:")
    print("V =", V2, ", edges =", edges2)
    print("Articulation Points:", ans2)
    print(f"Time taken (s): {end - start:.6f}\n")

    # -----------------------
    # Test Case 3
    # Chain 0-1-2-3 => APs are [1, 2]
    # -----------------------
    V3 = 4
    edges3 = [[0, 1], [1, 2], [2, 3]]
    start = timer()
    ans3 = sol.articulationPoints(V3, edges3)
    end = timer()
    print("Input 3:")
    print("V =", V3, ", edges =", edges3)
    print("Articulation Points:", ans3)
    print(f"Time taken (s): {end - start:.6f}\n")

    # -----------------------
    # Optional quick micro-benchmark:
    # Run the first case multiple times to see “program run time”
    # (Loops mostly amplify the articulationPoints call time.)
    # -----------------------
    loops = 1000
    start = timer()
    for _ in range(loops):
        sol.articulationPoints(V1, edges1)
    end = timer()
    print(f"Repeated {loops} runs on Test Case 1 -> total time (s): {end - start:.6f}")
```

### Sample Output (what you’ll see)

```
Input 1:
V = 5 , edges = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
Articulation Points: [1, 4]
Time taken (s): 0.0000xx

Input 2:
V = 3 , edges = [[0, 1], [1, 2], [2, 0]]
Articulation Points: [-1]
Time taken (s): 0.0000xx

Input 3:
V = 4 , edges = [[0, 1], [1, 2], [2, 3]]
Articulation Points: [1, 2]
Time taken (s): 0.0000xx

Repeated 1000 runs on Test Case 1 -> total time (s): 0.0xx
```

> Exact timings will vary by machine, but the algorithm is **linear** in `V + E`, so even fairly large sparse graphs run fast.

---

## 6) Real-World Use Cases (high-impact)

1. **Network reliability / router maintenance**
   In a computer network, articulation points correspond to **single points of failure**: removing such a router will disconnect subnets. Network teams use this to prioritize redundancy and hardware upgrades.

2. **Urban transport planning**
   In road/rail graphs, articulation stations/junctions identify critical hubs whose closure (construction, accident) would split the network, helping planners design **detours** and **redundant links**.

3. **Social & financial networks**
   In influence or transaction graphs, articulation nodes indicate **brokers or gatekeepers**. Their removal fragments communities/flows; this matters for **risk containment** and **fraud isolation**.

4. **Power grids & utilities**
   Articulation substations/pipes reveal **critical infrastructure** whose failure isolates consumers — vital for **resilience audits** and **emergency preparedness**.