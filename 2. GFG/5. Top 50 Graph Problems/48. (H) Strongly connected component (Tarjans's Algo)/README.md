# Strongly Connected Components (Tarjan's Algorithm)

**Difficulty:** Hard
**Accuracy:** 36.78%
**Submissions:** 31K+
**Points:** 8
**Average Time:** 30m

---

## 🧩 Problem Description

Given a **Directed Graph** having `V` vertices and `E` edges,
Find the members of **Strongly Connected Components (SCCs)** in the graph.

> **Note:** Sort both the **individual components** and the **array of components**.

---

## 🧠 Example 1

### **Input:**

```
V = 5
Edges:
0 -> 1
1 -> 2
2 -> 0
0 -> 3
3 -> 4
```

### **Output:**

```
0 1 2 3 4
```

### **Explanation:**

The graph can be visualized as:

```
  0 → 1
  ↑   ↓
  2 ←─┘
   ↓
   3 → 4
```

We can clearly see that there are **3 Strongly Connected Components** in the graph:

1. `{0, 1, 2}`
2. `{3}`
3. `{4}`

When combined in lexicographical order:

```
0 1 2 3 4
```

---

## 🧠 Example 2

### **Input:**

```
V = 3
Edges:
0 -> 1
1 -> 2
2 -> 0
```

### **Output:**

```
0 1 2
```

### **Explanation:**

All of the nodes are reachable from each other (mutual connectivity).
So there is **only one Strongly Connected Component (SCC)** in the graph.

---

## 🧩 Your Task

You don’t need to read or print anything.
Your task is to complete the function:

```python
def tarjans(self, V, adj):
    # code here
```

which takes:

* the number of vertices `V`, and
* adjacency list of the graph `adj`
  as input parameters and returns a **list of lists** of integers denoting the members of all SCCs in the graph.

---

### 🔎 Important Notes

* Each individual **Strongly Connected Component (SCC)** must be represented as a **list of integers sorted in ascending order**.
* The resulting **list of SCCs** must be sorted such that the **lexicographically smaller list appears first**.

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V)

---

## 🔒 Constraints

```
1 ≤ V ≤ 10⁵
1 ≤ E ≤ 10⁵
0 ≤ u, v < N
```

---

## 🏢 Company Tags

* Amazon

---

## 🧩 Topic Tags

* Graph
* Data Structures

---

## 📚 Related Articles

* [Tarjan Algorithm to Find Strongly Connected Components](https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/)

---

---

Here’s a compact interview-ready cheat-sheet for **Strongly Connected Components (SCCs)** with a clear dry-run and two Python solutions (Tarjan’s one-pass and Kosaraju’s two-pass).

---

# 2) Concept + Step-by-Step Dry Run

## Problem recap

Given a directed graph `adj` of `V` vertices (`0..V-1`), return **all SCCs** (each SCC sorted ascending), and the list of SCCs sorted **lexicographically**.

### What is an SCC?

A maximal set of vertices where every vertex is reachable from every other vertex in the set.

---

## Tarjan’s algorithm (intuition)

We perform a single DFS and maintain:

* `disc[u]`: discovery time of `u` (first DFS time we see it).
* `low[u]`: the **lowest discovery time** reachable from `u` via **any** path that uses 0+ tree edges and **at most one** back edge.
* `in_stack[u]`: is `u` currently in the active recursion stack?
* A stack `st` of active nodes.

When we finish exploring `u`, if `low[u] == disc[u]`, then `u` is the **root** of an SCC. We pop nodes from the stack until we pop `u` → that set is one SCC.

**Why it works:**
`low[u]` captures if we can reach an **earlier** ancestor (back edge). If we cannot (i.e., `low[u] == disc[u]`), the subgraph rooted at `u` cannot reach higher ancestors; hence it closes an SCC.

---

## Dry run on the classic example

Graph:

```
0 -> 1, 0 -> 3
1 -> 2
2 -> 0
3 -> 4
4 -> (none)
```

Adj list (0..4):

```
0: [1,3]
1: [2]
2: [0]
3: [4]
4: []
```

Start Tarjan from 0:

1. Visit 0:
   `disc[0]=0, low[0]=0`, push `0` (in stack)

   * Go 0→1
     Visit 1: `disc[1]=1, low[1]=1`, push `1`

     * Go 1→2
       Visit 2: `disc[2]=2, low[2]=2`, push `2`

       * Go 2→0 (0 is **in stack**) → **back edge**
         `low[2] = min(low[2], disc[0]) = min(2,0) = 0`
         Return to 1: `low[1] = min(low[1], low[2]) = min(1,0)=0`
         Return to 0: `low[0] = min(low[0], low[1]) = min(0,0)=0`

   * Go 0→3
     Visit 3: `disc[3]=3, low[3]=3`, push `3`

     * Go 3→4
       Visit 4: `disc[4]=4, low[4]=4`, push `4`
       4 has no edges → `low[4]==disc[4]` ⇒ pop SCC `{4}`
       Back to 3: `low[3] = min(3, low[4]=4) = 3`
       `low[3]==disc[3]` ⇒ pop SCC `{3}`

Finish 0: Check `low[0]==disc[0]` ⇒ yes (0 is root).
Pop until 0: pop `2,1,0` → SCC `{0,1,2}`

SCCs found: `{4}`, `{3}`, `{0,1,2}`
Sort each SCC: `[ [4], [3], [0,1,2] ]`
Lexicographically sort list of SCCs: `[[0,1,2], [3], [4]]`

---

# 3) Optimized Codes (Tarjan + Kosaraju)

## A) Optimized one-pass Tarjan (typical interview favorite)

```python
# User function Template for python3
class Solution:
    # Return a list of lists of integers denoting SCC members.
    # Each SCC sorted; list of SCCs sorted lexicographically.
    def tarjans(self, V, adj):
        disc = [-1] * V         # discovery times
        low  = [0]  * V         # low-link values
        in_stack = [False] * V  # membership in current stack
        st = []                 # active nodes stack
        time = 0
        sccs = []

        def dfs(u):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            st.append(u); in_stack[u] = True

            for v in adj[u]:
                if disc[v] == -1:
                    # Tree edge
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    # Back edge to an ancestor in the stack
                    low[u] = min(low[u], disc[v])

            # If u is the root of an SCC
            if low[u] == disc[u]:
                comp = []
                while True:
                    w = st.pop()
                    in_stack[w] = False
                    comp.append(w)
                    if w == u:
                        break
                comp.sort()     # sort the individual SCC
                sccs.append(comp)

        for u in range(V):
            if disc[u] == -1:
                dfs(u)

        # Sort the list of SCCs lexicographically
        sccs.sort()
        return sccs
```

**Complexity:**

* Time: **O(V + E)** (each edge and vertex processed O(1) amortized).
* Space: **O(V)** for recursion, arrays, stack.

**Why this is “optimized”:** One DFS traversal, no reverse graph or second pass.

---

## B) “Brute / Easy to reason” alternative: Kosaraju’s 2-pass (also O(V+E))

Idea:

1. DFS to compute **finishing order** (push nodes on a stack when exiting).
2. Reverse all edges.
3. Pop nodes from stack; for each unvisited node, DFS on **reversed** graph → one SCC.

```python
class SolutionKosaraju:
    def tarjans(self, V, adj):
        # Implementing Kosaraju to match the required signature
        # (name kept as tarjans for the judge harness)
        g = adj
        order = []
        vis = [False] * V

        def dfs1(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs1(v)
            order.append(u)  # finish time stack

        for u in range(V):
            if not vis[u]:
                dfs1(u)

        # Build reverse graph
        rg = [[] for _ in range(V)]
        for u in range(V):
            for v in g[u]:
                rg[v].append(u)

        # Second pass on reversed graph
        vis = [False] * V
        sccs = []

        def dfs2(u, comp):
            vis[u] = True
            comp.append(u)
            for v in rg[u]:
                if not vis[v]:
                    dfs2(v, comp)

        # Process in reverse finishing order
        for u in reversed(order):
            if not vis[u]:
                comp = []
                dfs2(u, comp)
                comp.sort()
                sccs.append(comp)

        sccs.sort()
        return sccs
```

**Complexity:**

* Time: **O(V + E)** (two DFS passes + reverse edges).
* Space: **O(V + E)** (extra reverse graph).

**When interviewers like this:** It’s conceptually simple and shows comfort with graph transformations and DFS order.

---

# 4) Common Interview Q&A

**Q1. What’s the difference between Tarjan’s and Kosaraju’s?**

* **Tarjan:** Single DFS pass using `disc/low`, a stack, detects SCC roots when `low[u]==disc[u]`.
* **Kosaraju:** Two DFS passes and a reversed graph.
  Both are **O(V+E)**; Tarjan is often slightly more memory-friendly and elegant in one pass.

**Q2. What does `low[u]` mean exactly?**
Minimum discovery time reachable from `u` using any number of tree edges and **at most one back edge** (to a node currently on stack in Tarjan).

**Q3. Why do we need the stack in Tarjan?**
To maintain the **current DFS component**. If we find a root (`low[u]==disc[u]`), we pop the stack to form that SCC.

**Q4. How do you ensure the required output order?**

* Sort each SCC’s node list after extraction.
* Sort the list of SCC lists lexicographically at the end.

**Q5. Edge cases to consider?**

* Disconnected graphs (run DFS from every unvisited node).
* Single node with/without self loop (self loop → SCC of size 1 anyway).
* Acyclic graph (every node is an SCC of size 1).

**Q6. Recursion limits?**
In Python, deep graphs can cause recursion depth issues; either raise the recursion limit or convert to iterative DFS (allowed if interviewer asks).

**Q7. Can this be done iteratively?**
Yes, Tarjan can be implemented iteratively with an explicit stack and states, though code becomes more verbose. For interviews, recursive is fine.

---

### Quick sanity check with the dry-run graph

Input:

```
V = 5
adj = [[1,3],[2],[0],[4],[]]
```

Tarjan returns:

```
[[0,1,2],[3],[4]]
```

…which matches the expected lexicographic order.

---

---

Here’s a **ready-to-run program** that:

* implements **Tarjan’s one-pass SCC** (default) and a **Kosaraju two-pass** variant,
* documents **time & space complexity** right beside each step,
* runs a couple of **sample inputs** and prints the **outputs**, and
* measures total runtime using `timeit.default_timer()` (high-res clock).

---

```python
"""
Strongly Connected Components — Tarjan (one pass) + Kosaraju (two pass)
----------------------------------------------------------------------
This script exposes:
  - class Solution: tarjan-based SCC extraction (O(V+E) time, O(V) space)
  - class SolutionKosaraju: two-pass SCC extraction (O(V+E) time, O(V+E) space)

It also includes a simple main that:
  1) builds sample directed graphs
  2) runs both implementations
  3) prints SCCs (each sorted, list of SCCs lexicographically sorted)
  4) reports runtime with timeit.default_timer()

Notes on output format (as most judges require):
  - Each SCC (list of ints) is sorted ascending
  - The list of SCCs is sorted lexicographically
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    """
    Tarjan's algorithm (single DFS pass).
    Time Complexity:  O(V + E)
      - Each vertex discovered once; each edge processed at most twice
    Space Complexity: O(V)
      - Arrays disc, low, in_stack, stack, recursion stack
    """

    def tarjans(self, V: int, adj: List[List[int]]) -> List[List[int]]:
        # disc[u] = discovery time of u; -1 => unvisited               # O(V) space
        disc = [-1] * V
        # low[u] = lowest discovery time reachable from u              # O(V) space
        low = [0] * V
        # in_stack[u] = True if u currently in active recursion stack  # O(V) space
        in_stack = [False] * V
        st: List[int] = []  # the active stack                         # O(V) space
        time = 0            # DFS timestamp counter                     # O(1)
        sccs: List[List[int]] = []                                      # O(V) lists total across all SCCs

        def dfs(u: int) -> None:                                        # recursion depth ≤ V
            nonlocal time
            disc[u] = low[u] = time                                     # O(1)
            time += 1
            st.append(u)                                                # O(1) amortized
            in_stack[u] = True

            # Explore all outgoing edges (u -> v)                       # Sum over all dfs: O(E)
            for v in adj[u]:
                if disc[v] == -1:                                       # Tree edge
                    dfs(v)                                              # Recurse
                    low[u] = min(low[u], low[v])                        # O(1)
                elif in_stack[v]:                                       # Back edge to stack member
                    low[u] = min(low[u], disc[v])                       # O(1)

            # If u is root of SCC                                       # O(1)
            if low[u] == disc[u]:
                comp: List[int] = []
                while True:                                             # Each vertex pushed/popped once → O(1) amortized
                    w = st.pop()
                    in_stack[w] = False
                    comp.append(w)
                    if w == u:
                        break
                comp.sort()                                             # Sum of sizes across SCCs = V → O(V log V) worst-case
                sccs.append(comp)

        # Run DFS from every unvisited node (disconnected digraph OK)   # O(V + E)
        for u in range(V):
            if disc[u] == -1:
                dfs(u)

        sccs.sort()                                                      # At most V SCCs → O(V log V)
        return sccs


class SolutionKosaraju:
    """
    Kosaraju (two passes + reverse graph).
    Time Complexity:  O(V + E)
    Space Complexity: O(V + E) (stores reversed graph)
    """

    def tarjans(self, V: int, adj: List[List[int]]) -> List[List[int]]:
        g = adj
        visited = [False] * V                                          # O(V)
        order: List[int] = []

        def dfs1(u: int) -> None:                                      # pass 1: finishing times
            visited[u] = True
            for v in g[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)                                            # O(1)

        for u in range(V):                                             # O(V + E)
            if not visited[u]:
                dfs1(u)

        # Build reverse graph                                           # O(V + E)
        rg: List[List[int]] = [[] for _ in range(V)]                   # O(V + E) space
        for u in range(V):
            for v in g[u]:
                rg[v].append(u)

        # pass 2: traverse reversed graph in reverse finishing order
        visited = [False] * V
        sccs: List[List[int]] = []

        def dfs2(u: int, comp: List[int]) -> None:
            visited[u] = True
            comp.append(u)
            for v in rg[u]:
                if not visited[v]:
                    dfs2(v, comp)

        for u in reversed(order):                                      # O(V + E)
            if not visited[u]:
                comp: List[int] = []
                dfs2(u, comp)
                comp.sort()                                            # O(sz log sz)
                sccs.append(comp)

        sccs.sort()                                                    # O(#SCC log #SCC)
        return sccs


# -------------------------------
# Demonstration / simple test bed
# -------------------------------
def run_and_time(title: str, func, *args):
    t0 = timer()
    out = func(*args)
    t1 = timer()
    print(f"\n[{title}]")
    print("SCCs:", out)
    print(f"Elapsed: {(t1 - t0) * 1e6:.1f} µs")
    return out


if __name__ == "__main__":
    # -------- Sample 1 (from the dry run) --------
    V1 = 5
    adj1 = [
        [1, 3],  # 0 -> 1,3
        [2],     # 1 -> 2
        [0],     # 2 -> 0
        [4],     # 3 -> 4
        []       # 4
    ]
    # Expected SCCs (sorted each, then lexicographically): [[0,1,2], [3], [4]]

    # -------- Sample 2 (single SCC) --------
    V2 = 3
    adj2 = [
        [1],   # 0 -> 1
        [2],   # 1 -> 2
        [0]    # 2 -> 0
    ]
    # Expected: [[0,1,2]]

    sol_tarjan = Solution()
    sol_kos = SolutionKosaraju()

    print("=== Tarjan's one-pass ===")
    run_and_time("Sample 1", sol_tarjan.tarjans, V1, adj1)
    run_and_time("Sample 2", sol_tarjan.tarjans, V2, adj2)

    print("\n=== Kosaraju two-pass ===")
    run_and_time("Sample 1", sol_kos.tarjans, V1, adj1)
    run_and_time("Sample 2", sol_kos.tarjans, V2, adj2)
```

### Example output (will vary slightly depending on machine)

```
=== Tarjan's one-pass ===

[Sample 1]
SCCs: [[0, 1, 2], [3], [4]]
Elapsed: 340.7 µs

[Sample 2]
SCCs: [[0, 1, 2]]
Elapsed: 86.4 µs

=== Kosaraju two-pass ===

[Sample 1]
SCCs: [[0, 1, 2], [3], [4]]
Elapsed: 422.3 µs

[Sample 2]
SCCs: [[0, 1, 2]]
Elapsed: 98.1 µs
```

---

## 6) Real-World Use Cases (a few high-impact ones)

1. **Microservice dependency analysis**
   Detect mutually dependent microservices (SCCs). Refactor or isolate cycles to improve deployability and fault isolation.

2. **Package/module managers**
   Identify cyclical dependencies between libraries or modules for safe build ordering and version conflict resolution.

3. **Program analysis & compilers**
   SCCs in call graphs / control-flow graphs enable optimizations like common subexpression elimination, inlining within strongly connected regions, or partial evaluation.

4. **Social/communication networks**
   Find tightly knit communities where every member can reach every other (e.g., mutual follow/DM reachability).

5. **Deadlock detection**
   In resource-allocation graphs, SCCs containing cycles can reveal potential or actual deadlocks.
