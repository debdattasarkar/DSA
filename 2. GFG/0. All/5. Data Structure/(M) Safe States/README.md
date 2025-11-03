
---

# 🧩 Safe States

### Difficulty: Medium

**Accuracy:** 55.52%
**Submissions:** 73K+
**Points:** 4
**Average Time:** 20m

---

## 🧠 Problem Statement

Given a directed graph with **V** vertices numbered from **0 to V-1** and **E** directed edges, represented as a 2D array **edges[][]**, where each element **edges[i] = [u, v]** represents a directed edge from vertex **u** to vertex **v**.
Return **all Safe Nodes** of the graph.

A vertex with **no outgoing edges** is called a **terminal node**.
A vertex is considered **safe** if **every path starting from it eventually reaches a terminal node**.

---

## 🧩 Examples

### Example 1

**Input:**

```
V = 5, E = 6  
edges[][] = [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
```

**Output:**

```
[0, 1, 2, 3, 4]
```

**Explanation:**
4 and 0 are terminal nodes, and all paths from 1, 2, 3 lead to terminal node 4.

---

### Example 2

**Input:**

```
V = 4, E = 3  
edges[][] = [[1, 2], [2, 3], [3, 2]]
```

**Output:**

```
[0]
```

**Explanation:**
0 is the terminal node, and no other node than 0 leads to 0.

---

## ⚙️ Constraints

* ( 1 \leq V \leq 10^5 )
* ( 0 \leq E \leq 10^5 )
* ( 0 \leq edges[i][0], edges[i][1] < V )

---

## ⏱️ Expected Time & Space Complexity

* **Time Complexity:** ( O(V + E) )
* **Auxiliary Space:** ( O(V) )

---

## 🏢 Company Tags

* **Bloomberg**

---

## 🧩 Topic Tags

* DFS
* Graph
* BFS
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [**Eventual Safe States**](https://www.geeksforgeeks.org/eventual-safe-states/)

---

---

Alright — let’s nail this like an interview.

# 2) Text explanation + step-by-step dry run

## Problem in one line

Return all vertices from which **every** path eventually reaches a **terminal node** (a node with no outgoing edges). These are called **eventually safe nodes**. Any node that can reach a cycle is **unsafe**.

## Two standard ways (both O(V+E))

1. **Reverse graph + Kahn’s BFS** (topological on reverse):

   * Reverse all edges.
   * Start with all **terminal nodes** (outdegree 0 in original graph). In the **reversed graph** these have indegree 0.
   * Repeatedly remove such nodes; when a node is removed, reduce the outdegree of its predecessors (in original graph).
   * Nodes that get reduced to outdegree 0 become safe too.
   * All removed nodes are safe. The rest are part of or can reach a cycle.

2. **DFS 3-color / state marking**:

   * `0 = unvisited`, `1 = visiting (in stack)`, `2 = safe (done)`.
   * DFS from each node.
   * If you ever revisit a `visiting` node → found a cycle → current path is unsafe.
   * If all neighbors are safe, mark current node `2` (safe).
   * Memoization makes each node processed once.

Both return the sorted list of safe nodes.

---

## Dry run (Reverse graph + Kahn) on Example 1

**Input**
V = 5, E = 6
edges = [
[1,0], [1,2], [1,3], [1,4], [2,3], [3,4]
]

**Build original outdegree**
outdeg[0]=0, outdeg[1]=4, outdeg[2]=1, outdeg[3]=1, outdeg[4]=0

**Build reversed graph** (v -> u for each u->v):
0: [1]
2: [1]
3: [1,2]
4: [1,3]
1: []

**Queue init**: all original outdeg==0 → `q = [0,4]`, safe = {0,4}.

Process:

1. pop 0 → predecessors in reversed: [1]

   * decrement outdeg[1] from 4→3
2. pop 4 → predecessors: [1,3]

   * outdeg[1]: 3→2
   * outdeg[3]: 1→0 → push 3; safe add 3
3. pop 3 → predecessors: [1,2]

   * outdeg[1]: 2→1
   * outdeg[2]: 1→0 → push 2; safe add 2
4. pop 2 → predecessors: [1]

   * outdeg[1]: 1→0 → push 1; safe add 1
5. pop 1 → predecessors: [] (done)

Safe nodes collected (sorted): `[0,1,2,3,4]`.

---

## Dry run (DFS 3-color) on Example 2

**Input**
V = 4, edges = [
[1,2], [2,3], [3,2]
]

Adj:
0: []
1: [2]
2: [3]
3: [2]

States initially all 0.

* Node 0: no neighbors → mark `2` (safe).
* Node 1: visit → to 2 → to 3 → to 2 (but 2 is **visiting=1**) → cycle → 3 unsafe, 2 unsafe, 1 unsafe.
  Result: only node `0` is safe → `[0]`.

---

# 3) Python solutions (brute/easy + two optimized ways)

All versions match your expected signature:

```python
class Solution:
    def safeNodes(self, V, edges):
        # Code here
```

### A) Brute/easy (interview warm-up): DFS from each node without memoization

* For each node, do a DFS with a fresh `path_visiting` set.
* If any path returns to the path set → unsafe.
* This is simple but **O(V * (V+E))** in worst case.

```python
class Solution:
    def safeNodes(self, V, edges):
        # Build adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        def reaches_cycle(start):
            # Fresh sets per start (no memo), brute but easy to follow
            visiting = set()
            visited = set()

            def dfs(u):
                if u in visiting:
                    return True  # found a back-edge => cycle
                if u in visited:
                    return False  # already proven acyclic for this start

                visiting.add(u)
                for nbr in graph[u]:
                    if dfs(nbr):
                        return True
                visiting.remove(u)
                visited.add(u)
                return False

            return dfs(start)

        safe = []
        for node in range(V):
            if not reaches_cycle(node):
                safe.append(node)
        return safe
```

> Use this only as a conceptual stepping stone; next two are optimal.

---

### B) Optimized #1 — **Reverse graph + Kahn’s BFS** (often the cleanest to code)

**Why it’s great:** linear time, simple queue logic, and directly matches the “every path ends at terminal” idea by peeling off dead ends.

```python
from collections import deque

class Solution:
    def safeNodes(self, V, edges):
        # Build graph and reverse graph; also track outdegree in original graph
        graph = [[] for _ in range(V)]
        reverse_graph = [[] for _ in range(V)]
        outdeg = [0] * V

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)   # reversed edge
            outdeg[u] += 1

        # Start with all terminal nodes (outdegree 0)
        queue = deque([u for u in range(V) if outdeg[u] == 0])
        is_safe = [False] * V

        while queue:
            node = queue.popleft()
            is_safe[node] = True  # if we can peel it, it's safe
            # In reversed graph, go to predecessors in original graph
            for pred in reverse_graph[node]:
                outdeg[pred] -= 1              # remove edge pred->node
                if outdeg[pred] == 0:          # pred became terminal
                    queue.append(pred)

        # Safe nodes are those we peeled off (sorted because nodes are 0..V-1)
        return [i for i, safe in enumerate(is_safe) if safe]
```

**Complexity:** `O(V + E)` time, `O(V + E)` space.

---

### C) Optimized #2 — **DFS 3-color (cycle detection + memo)**

**Why it’s great:** standard interview trick for cycle detection in directed graphs; elegant recursion with states.

```python
import sys
sys.setrecursionlimit(1 << 25)

class Solution:
    def safeNodes(self, V, edges):
        # Build adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        # 0 = unvisited, 1 = visiting, 2 = safe (done and not leading to cycle)
        state = [0] * V

        def dfs(u):
            if state[u] != 0:
                # state 1 => cycle on path; state 2 => already safe
                return state[u] == 2

            state[u] = 1  # mark as visiting
            for nbr in graph[u]:
                # If neighbor is unsafe or leads to cycle, current is unsafe
                if not dfs(nbr):
                    return False
            state[u] = 2  # all neighbors safe => this node is safe
            return True

        safe_nodes = []
        for node in range(V):
            if dfs(node):
                safe_nodes.append(node)
        return safe_nodes
```

**Complexity:** `O(V + E)` time (each node processed once), `O(V)` recursion stack in worst case.

---

# 4) Interview quick-recall + expected Q&A

## Mental model (10-second recall)

* **Safe = cannot reach a cycle.**
* Two recipes:

  1. **Reverse + Kahn**: Start from terminal nodes (outdeg=0), peel backwards; peeled = safe.
  2. **DFS 3-color**: If you re-enter a `visiting` node → cycle; nodes whose neighbors are all safe → safe.

## Checklist before you code

1. Decide representation → adjacency list.
2. If **Kahn**: compute `outdeg[]`, build `reverse_graph`, init queue with outdeg 0.
3. If **DFS**: define `state[]` (0/1/2) and recursive function returning “is safe”.
4. Return indices with `safe=True`, already sorted.

## Common pitfalls

* Forgetting to **reverse edges** for Kahn, or mistakenly using indegrees of original graph.
* Not marking node as **visiting (1)** before exploring neighbors in DFS → misses cycle detection.
* Multiple components and isolated nodes (0 outdegree) → they are **safe**.
* Large graphs → ensure **O(V+E)** and avoid per-node fresh DFS (unless asked to discuss brute force).

## Expected questions & crisp answers

**Q1. What does “eventually safe” mean?**
**A.** From that node, **every** path ends at a terminal node; equivalently, the node **cannot reach a cycle**.

**Q2. Why does the reverse-graph Kahn approach work?**
**A.** Removing terminal nodes and edges can only make more nodes terminal; any node that can be peeled off this way **cannot** reach a cycle. Nodes left unpeeled must lie **on** or **reach** a cycle.

**Q3. Complexity of both optimal methods?**
**A.** Time `O(V+E)`, Space `O(V+E)`.

**Q4. How do you detect cycles with DFS?**
**A.** Use 3-coloring: mark node `visiting` on entry, `safe` on exit; encountering a `visiting` node during DFS implies a **back edge → cycle**.

**Q5. Which approach would you choose and why?**
**A.** Either is fine; I default to **reverse + Kahn** for iterative clarity and no recursion-depth issues. If recursion is allowed, **3-color DFS** is equally standard.

**Q6. Edge cases?**
**A.**

* All nodes terminal → all safe.
* Single big cycle → none safe.
* Disconnected components → handle each naturally.
* Very deep chains → prefer Kahn if recursion depth is a concern.

**Q7. Can we do it without building the reverse graph?**
**A.** Yes, with **DFS 3-color**. For Kahn specifically, reverse simplifies “peeling predecessors”; without it you’d need to scan edges to find predecessors (costly).

**Q8. How to prove correctness briefly?**
**A.**

* **Soundness:** Kahn removes only nodes whose every path leads to already removed nodes → by induction they end at terminals.
* **Completeness:** A node that can reach a cycle never becomes outdeg 0; hence never removed.
* DFS proof mirrors cycle detection: a node is safe iff all neighbors are safe and no cycle reachable.

---

---

awesome—wrapping this up with crisp, interview-friendly extras.

# 5) Real-world use cases (short & relatable)

* **Build/Deployment pipelines (DAG checks):** Stages that *can’t* reach a cyclic dependency are **eventually safe**—they’ll always finish. Cyclic stages are unsafe because some path loops forever.
* **Microservice call graphs:** A service is **safe** if any call chain starting from it always terminates (no circular call chains). Helps detect potential outage amplifiers.
* **Task/workflow engines (Airflow-like):** Tasks whose downstream graph can’t reach a cycle are **safe**—they’ll always complete if started.
* **Package dependency graphs:** A package is **safe** to install if its dependency chain never cycles. Anything that can reach a cycle risks non-termination during resolution.

These map 1:1 to “safe nodes = nodes that cannot reach a cycle.”

---

# 6) Full Python program (with inline complexity notes + timing)

* Includes BOTH optimal methods:

  * Reverse Graph + Kahn’s BFS (default in `safeNodes`)
  * DFS 3-color (`safeNodesDFS`)
* Shows sample inputs and outputs.
* Uses `timeit` to time each full run.

```python
"""
Safe States — Full Program (Python)

Contains:
1) Solution.safeNodes(V, edges): Reverse-graph + Kahn’s BFS  (O(V+E))
2) Solution.safeNodesDFS(V, edges): DFS 3-color + memo       (O(V+E))

Includes a main section with:
- Two sample inputs (from the prompt)
- Pretty printing of outputs
- timeit-based runtimes for each method

Notes on complexity:
- Building adjacency / reverse adjacency: O(V + E) time, O(V + E) space
- Kahn processing (queue pops + edge relaxations): O(V + E) time
- DFS processing: each node/edge visited at most once => O(V + E) time
"""

from collections import deque
import timeit
import sys
sys.setrecursionlimit(1 << 25)


class Solution:
    def safeNodes(self, V, edges):
        """
        Reverse-graph + Kahn’s BFS (Topological peeling)
        ------------------------------------------------
        Idea:
            - Nodes with outdegree 0 (terminal) are safe by definition.
            - In reverse graph, we pull predecessors; when a predecessor’s outdegree
              drops to 0, it becomes safe too.
            - Nodes we can peel this way are precisely the nodes that cannot reach cycles.

        Steps & Complexity:
            1) Build adjacency lists and reverse graph: O(V + E) time, O(V + E) space
            2) Initialize queue with outdegree==0 nodes: O(V) time, O(V) space
            3) BFS: pop each node once and relax each edge once: O(V + E) time
            4) Collect safe nodes: O(V) time

        Returns:
            Sorted list of safe nodes.
        """
        # ----- Step 1: Build graph structures -----
        graph = [[] for _ in range(V)]          # original adjacency; space O(V + E)
        reverse_graph = [[] for _ in range(V)]  # reversed adjacency; space O(V + E)
        outdegree = [0] * V                     # outdegree per node; space O(V)

        for u, v in edges:                      # loop E times; time O(E)
            graph[u].append(v)
            reverse_graph[v].append(u)
            outdegree[u] += 1

        # ----- Step 2: Initialize queue with terminals (outdegree == 0) -----
        queue = deque([i for i in range(V) if outdegree[i] == 0])  # time O(V), space O(V)
        is_safe = [False] * V  # mark peeled nodes; space O(V)

        # ----- Step 3: Kahn BFS on reversed graph -----
        while queue:                             # each node enters once => O(V)
            node = queue.popleft()
            is_safe[node] = True
            # For every predecessor in original graph, remove edge pred->node
            for pred in reverse_graph[node]:     # each reversed edge visited once => O(E)
                outdegree[pred] -= 1
                if outdegree[pred] == 0:
                    queue.append(pred)

        # ----- Step 4: Collect safe nodes (already sorted since nodes are 0..V-1) -----
        safe_nodes = [i for i, ok in enumerate(is_safe) if ok]     # time O(V)
        return safe_nodes

    def safeNodesDFS(self, V, edges):
        """
        DFS 3-color with memoization
        ----------------------------
        States:
            0 = unvisited
            1 = visiting (in recursion stack)
            2 = safe (visited & proved not to reach a cycle)

        Logic:
            - If during DFS we hit a node in state 1 => cycle found => unsafe path.
            - A node becomes safe if *all* neighbors are safe.

        Complexity:
            - Build adjacency: O(V + E) time, O(V + E) space
            - DFS visits each node/edge once: O(V + E) time
            - Stack depth up to O(V) in worst case
        """
        # Build adjacency list: time O(V + E), space O(V + E)
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        state = [0] * V  # 0=unvisited, 1=visiting, 2=safe; space O(V)

        def dfs(u):
            # If already decided
            if state[u] == 2:       # already safe
                return True
            if state[u] == 1:       # back-edge => cycle
                return False

            state[u] = 1            # mark as visiting
            for nbr in graph[u]:    # explore all outgoing edges; aggregate safety
                if not dfs(nbr):
                    return False    # any neighbor unsafe => current unsafe
            state[u] = 2            # all neighbors safe => this node safe
            return True

        # Run DFS from every node (each node processed once overall)
        safe_nodes = []
        for node in range(V):
            if dfs(node):
                safe_nodes.append(node)
        return safe_nodes


# -------------- Demo / Timing --------------
def run_once_with_kahn(V, edges):
    sol = Solution()
    return sol.safeNodes(V, edges)

def run_once_with_dfs(V, edges):
    sol = Solution()
    return sol.safeNodesDFS(V, edges)


if __name__ == "__main__":
    # Example 1
    V1 = 5
    E1 = 6
    edges1 = [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

    # Example 2
    V2 = 4
    E2 = 3
    edges2 = [[1, 2], [2, 3], [3, 2]]

    # Print outputs
    print("Example 1 input:")
    print("V =", V1, "E =", E1, "edges =", edges1)
    print("Kahn safe nodes   :", run_once_with_kahn(V1, edges1))
    print("DFS  safe nodes   :", run_once_with_dfs(V1, edges1))
    print()

    print("Example 2 input:")
    print("V =", V2, "E =", E2, "edges =", edges2)
    print("Kahn safe nodes   :", run_once_with_kahn(V2, edges2))
    print("DFS  safe nodes   :", run_once_with_dfs(V2, edges2))
    print()

    # Timing with timeit (execute each method once per dataset)
    # We capture closures to satisfy timeit without global lookups.
    t_kahn_1 = timeit.timeit(lambda: run_once_with_kahn(V1, edges1), number=1)
    t_dfs_1  = timeit.timeit(lambda: run_once_with_dfs(V1, edges1),  number=1)
    t_kahn_2 = timeit.timeit(lambda: run_once_with_kahn(V2, edges2), number=1)
    t_dfs_2  = timeit.timeit(lambda: run_once_with_dfs(V2, edges2),  number=1)

    print(f"Timing (seconds) — Example 1: Kahn={t_kahn_1:.6f}, DFS={t_dfs_1:.6f}")
    print(f"Timing (seconds) — Example 2: Kahn={t_kahn_2:.6f}, DFS={t_dfs_2:.6f}")
```

**How to read the comments quickly in an interview:**

* Each block states its **time/space** so you can narrate confidently.
* The main shows **inputs/outputs** and uses `timeit`’s `number=1` to time each full program run per example.
