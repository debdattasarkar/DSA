
---

# **Detect Cycle in a Directed Graph 🚀**

**Difficulty:** Medium
**Accuracy:** 27.88%
**Submissions:** 532K+
**Points:** 4

---

## 🧩 **Problem Statement**

Given a **Directed Graph** with **V** vertices (Numbered from **0 to V-1**) and **E** edges, check whether it contains **any cycle or not**.
The graph is represented as a 2D vector `edges[][]`, where each entry `edges[i] = [u, v]` denotes an edge **from vertex `u` to vertex `v`**.

---

## 🧠 **Examples**

### **Example 1**

**Input:**
`V = 4, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 3]]`

**Output:**
`true`

**Explanation:**
There is a cycle between `3 -> 3`.

---

### **Example 2**

**Input:**
`V = 3, edges[][] = [[0, 1], [1, 2]]`

**Output:**
`false`

**Explanation:**
There is **no cycle** in the graph.

---

## ⚙️ **Constraints**

```
1 ≤ V, E ≤ 10⁵
```

---

## ⏱ **Expected Complexities**

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V + E)

---

## 🏢 **Company Tags**

`Flipkart`
`Amazon`
`Microsoft`
`Samsung`
`MakeMyTrip`
`Oracle`
`Goldman Sachs`
`Adobe`
`BankBazaar`
`Rockstand`

---

## 📚 **Topic Tags**

* Graph
* Data Structures

---

## 🧾 **Related Interview Experiences**

* Makemytrip Interview Experience Set 13 On Campus For Full Time
* Samsung R&D Noida Interview Experience On Campus
* Samsung Interview Experience On Campus For Software Engineer September 2018

---

## 📘 **Related Articles**

* [Detect Cycle In A Graph](https://www.geeksforgeeks.org/detect-cycle-in-a-graph/)

---

---

awesome — let’s lock down “**Detect Cycle in a Directed Graph**” the interview way: clear intuition, a quick dry run, then two standard solutions in your requested signature (DFS recursion-stack and Kahn’s topological sort). I’ll end with tight interviewer Q&A.

---

## 2) Intuition + Step-by-step dry run

### Problem

Given `V` (0…V-1) and directed edges, return `True` if **any directed cycle** exists, else `False`.

### Two classic ways

1. **DFS + recursion stack (or 3-coloring)**

   * While DFS’ing, nodes currently on the recursion stack are “GRAY/visiting.”
   * If you ever go to a GRAY node → **back edge** → **cycle**.
2. **Kahn’s algorithm (BFS/topological sort)**

   * Compute in-degrees; repeatedly pop nodes of in-degree 0.
   * If you can’t process all `V` nodes (i.e., some nodes always have positive in-degree), the remainder forms a **cycle**.

Both are **O(V+E)** time, **O(V+E)** space.

### Dry run (Example 1)

```
V = 4
edges = [[0,1], [1,2], [2,3], [3,3]]  # self-loop at 3
Adj:
0: [1]
1: [2]
2: [3]
3: [3]
```

#### DFS recursion-stack view

* Start 0 → mark 0 visiting → go 1 → visiting → go 2 → visiting → go 3 → visiting
* From 3, edge to **3** again; 3 is **visiting** → back edge → **cycle** ⇒ return True.

#### Kahn’s view

* indeg: 0→0, 1→1, 2→1, 3→2 (edges 2→3, 3→3)
* Queue starts with [0]. Process 0 → indeg[1]=0 → enqueue 1.
* Process 1 → indeg[2]=0 → enqueue 2.
* Process 2 → indeg[3]=1 (still >0).
* Queue empties with only 3 nodes processed (< V) → **cycle**.

---

## 3) Python solutions (interview-ready)

Both use your exact signature:

```python
class Solution:
    def isCycle(self, V, edges):
        # code here
```

### A) DFS + recursion stack (most common in interviews)

```python
class Solution:
    def isCycle(self, V, edges):
        """
        Detect a cycle in a directed graph using DFS + recursion stack.
        Steps:
          1) Build adjacency list: O(V+E)
          2) DFS each unvisited node keeping a recursion-stack flag.
             If we reach a node that is on the current recursion stack,
             we found a back edge -> cycle.
        Time  : O(V + E)
        Space : O(V + E) for graph + O(V) recursion/visited
        """
        # 1) Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V     # permanently finished nodes
        in_stack = [False] * V    # nodes on current DFS path

        def dfs(u: int) -> bool:
            visited[u] = True
            in_stack[u] = True
            for w in adj[u]:
                if not visited[w]:
                    if dfs(w):               # cycle detected below
                        return True
                elif in_stack[w]:
                    # Back edge to a node currently in recursion stack -> cycle
                    return True
            in_stack[u] = False              # backtrack
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
```

### B) Kahn’s Algorithm (BFS Topological Sort)

```python
from collections import deque

class Solution:
    def isCycle(self, V, edges):
        """
        Detect a cycle using Kahn’s algorithm (topological sort).
        If we cannot process all V nodes (i.e., processed < V), a cycle exists.
        Time  : O(V + E)
        Space : O(V + E)
        """
        # 1) Build adjacency + indegree
        adj = [[] for _ in range(V)]
        indeg = [0] * V
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        # 2) Push all 0-indegree nodes
        q = deque(i for i in range(V) if indeg[i] == 0)

        processed = 0
        while q:
            u = q.popleft()
            processed += 1
            for w in adj[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)

        # If any node couldn't be processed, graph has a cycle
        return processed != V
```

> Which to pick?
> Use **DFS recursion-stack** if you want a simple, memory-light answer; use **Kahn** when you also need a topological order (or to detect cycles in bulk).

---

## 4) Interviewer Q&A (high-yield)

**Q1. Why does DFS recursion-stack detect cycles?**
A directed **back edge** is exactly an edge to a node **currently on the DFS call stack** (i.e., still “visiting”). That’s the definition of a directed cycle in DFS tree terminology.

**Q2. What’s the complexity?**
Both methods are **O(V + E)** time and **O(V + E)** space (graph) plus **O(V)** auxiliary (visited/stack or indegree/queue).

**Q3. Difference between recursion-stack vs 3-coloring?**
They’re equivalent. 3-coloring uses states: `0=WHITE`(unvisited), `1=GRAY`(visiting), `2=BLACK`(done). Detect `GRAY→GRAY` edges.

**Q4. Can DSU detect cycles in directed graphs?**
Not reliably. DSU works neatly for **undirected** cycles. For directed cycles, prefer **DFS with colors** or **Kahn’s**.

**Q5. How to return the actual cycle?**
In DFS, maintain a parent map; when you find a back edge to a GRAY node, walk parents to reconstruct the cycle.

**Q6. What about self-loops and parallel edges?**

* A self-loop `(u,u)` is an immediate cycle. Both solutions catch it.
* Parallel edges don’t matter unless one closes a cycle; algorithms handle them naturally.

**Q7. When might Kahn’s be preferable?**
When you also need a **topological order** (DAG only) or want an **iterative** solution that avoids recursion depth issues.

---

---

Here’s a **runnable, interview-style full program** for **Detecting a Cycle in a Directed Graph** that:

* implements your required signature `class Solution: def isCycle(self, V, edges): ...` twice:

  * **DFS + recursion stack** (classic)
  * **Kahn’s algorithm** (BFS / topo sort)
* prints outputs for a couple of inputs,
* and benchmarks both approaches with **timeit** (avg seconds/run).

I’ve added **inline comments** that spell out **time & space complexity** exactly where they apply.

---

## 5) Full Python program (with inline complexity notes + timings)

```python
"""
Detect Cycle in a Directed Graph
--------------------------------
We provide two standard solutions that fit the required signature:

  1) DFS + recursion stack (a.k.a. GRAY/visiting detection)
  2) Kahn's algorithm (BFS topological sort)

Both have:
  Time  : O(V + E)
  Space : O(V + E) for adjacency + O(V) auxiliary structures

This script:
  * Runs two small examples (one cyclic, one acyclic).
  * Benchmarks both approaches with timeit on a moderate graph.
"""

from collections import deque
import timeit
from typing import List


# =============================== DFS + recursion stack =============================== #
class SolutionDFS:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        """
        Detect a cycle using DFS with a recursion stack.
        Steps:
          1) Build adjacency list: O(V + E) time/space
          2) DFS each unvisited node:
             - visited[u]     -> node was fully processed (BLACK)
             - in_stack[u]    -> node is on current DFS path (GRAY)
             If we encounter an edge to a node in the current recursion stack,
             we found a back edge -> cycle.

        Overall complexity:
          Time  : O(V + E)
          Space : O(V + E) for adjacency, + O(V) for visited/in_stack, + O(V) recursion
        """
        # 1) adjacency list (directed)
        adj = [[] for _ in range(V)]  # O(V) space
        for u, v in edges:            # O(E) time
            adj[u].append(v)

        visited = [False] * V   # O(V)
        in_stack = [False] * V  # O(V)

        def dfs(u: int) -> bool:
            visited[u] = True
            in_stack[u] = True
            # Explore all outgoing edges of u: total across graph = O(E)
            for w in adj[u]:
                if not visited[w]:
                    if dfs(w):          # recursion: O(V) depth worst-case
                        return True
                elif in_stack[w]:
                    # Back edge to a node on current path -> cycle
                    return True
            in_stack[u] = False         # backtrack
            return False

        for i in range(V):              # O(V)
            if not visited[i]:
                if dfs(i):
                    return True
        return False


# ================================== Kahn’s algorithm ================================== #
class SolutionKahn:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        """
        Detect a cycle using Kahn's topological sort.
        Steps:
          1) Build adjacency list & indegree array: O(V + E)
          2) Push all indegree-0 nodes into a queue.
          3) Pop nodes, reduce neighbors' indegree, push new zeros.
          4) If processed count < V, nodes remain in a cycle -> cycle exists.

        Overall complexity:
          Time  : O(V + E)
          Space : O(V + E) for adjacency + O(V) for indegree + O(V) for queue
        """
        adj = [[] for _ in range(V)]  # O(V) space
        indeg = [0] * V               # O(V) space
        for u, v in edges:            # O(E)
            adj[u].append(v)
            indeg[v] += 1

        q = deque(i for i in range(V) if indeg[i] == 0)  # O(V)
        processed = 0
        while q:                                         # O(V + E)
            u = q.popleft()
            processed += 1
            for w in adj[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)

        # If we couldn't process all nodes, some are part of a cycle
        return processed != V


# =============================== Timing helper (timeit) =============================== #
def bench(func, *args, number=50) -> float:
    """
    Return average seconds per run using timeit.
    For small graphs, Python overhead dominates; treat results as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ========================================= Demo ========================================= #
if __name__ == "__main__":
    print("=== Detect Cycle in a Directed Graph — DFS vs Kahn ===\n")

    # ---- Example 1 (cyclic) ----
    V1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 3]]  # self-loop at 3
    print(">>> Example 1 (cyclic)")
    print("V =", V1, "Edges =", edges1)
    print("DFS  ->", SolutionDFS().isCycle(V1, edges1), " (expected: True)")
    print("Kahn ->", SolutionKahn().isCycle(V1, edges1), " (expected: True)")
    print()

    # ---- Example 2 (acyclic) ----
    V2 = 3
    edges2 = [[0, 1], [1, 2]]  # DAG
    print(">>> Example 2 (acyclic)")
    print("V =", V2, "Edges =", edges2)
    print("DFS  ->", SolutionDFS().isCycle(V2, edges2), " (expected: False)")
    print("Kahn ->", SolutionKahn().isCycle(V2, edges2), " (expected: False)")
    print()

    # ---- Moderate benchmark: layered DAG + one back edge to make a cycle ----
    print("=== Timings (average seconds per call) ===")
    # Build a layered graph of ~20k nodes and ~100k edges
    LAYERS = 200
    WIDTH  = 100
    V3 = LAYERS * WIDTH
    edges3 = []
    # forward edges layer->layer+1 (DAG)
    for layer in range(LAYERS - 1):
        base = layer * WIDTH
        nxt  = (layer + 1) * WIDTH
        for i in range(WIDTH):
            u = base + i
            # connect to two neighbors in next layer (bounded degree)
            edges3.append([u, nxt + i])               # straight
            if i + 1 < WIDTH:
                edges3.append([u, nxt + i + 1])       # diagonal
    # create one back edge to form a cycle
    edges3.append([WIDTH, 0])  # from layer 1 to layer 0

    runs = 10
    t_dfs  = bench(SolutionDFS().isCycle,  V3, edges3, number=runs)
    t_kahn = bench(SolutionKahn().isCycle, V3, edges3, number=runs)
    print(f"DFS   : V={V3}, E≈{len(edges3)} runs={runs:3d} -> {t_dfs:.6f} s/run")
    print(f"Kahn  : V={V3}, E≈{len(edges3)} runs={runs:3d} -> {t_kahn:.6f} s/run")

    print("\nNotes:")
    print(" • Both methods are O(V+E). Kahn avoids recursion and gives topo order for DAGs.")
    print(" • DFS recursion-stack is compact & idiomatic; beware recursion depth on very deep graphs.")
    print(" • Space is O(V+E) for adjacency; extra O(V) for visited/stack or indegree/queue.")
```

### What you’ll see

* Example 1: `True` (cycle present) for both methods.
* Example 2: `False` for both methods.
* Timing lines comparing DFS vs Kahn on a moderate graph (exact numbers vary by machine).

---

## 6) Real-World Use Cases (the important ones)

1. **Build/Deployment Pipelines & Package Managers (topological order)**

   * Ensure task/package dependencies form a **DAG**. If a cycle exists (A depends on B which depends on A), builds/installs must fail.

2. **Scheduling with Prerequisites (courses, jobs)**

   * Courses with prerequisites or jobs with dependencies require **cycle-free** graphs; otherwise no valid schedule exists.

3. **Makefile / CI pipelines**

   * Detect circular dependencies between targets/stages, preventing infinite rebuild loops.

4. **Static Analysis of Code (module/import graphs)**

   * Identify unwanted cycles in module imports (like Python packages) which can cause runtime initialization issues.