# Level of Nodes

**Difficulty:** Medium
**Accuracy:** 50.95%
**Submissions:** 62K+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

Given an integer `x` and an **undirected acyclic graph** with `v` nodes (labeled from `0` to `v-1`) and `e` edges, return the **level** of the node labeled as `x`.

The **Level** of a node is the **minimum number of edges** you must travel from the node `0` to reach the target node.

If there doesn’t exist such a node labeled as `x`, return **-1**.

---

## Examples

### Example 1

**Input:**
`x = 4`

Graph visualization:

```
       0
      / \
     1   2
    / \   \
   3   4   5
```

**Output:**
`2`

**Explanation:**

```
Level 0 → [0]
Level 1 → [1, 2]
Level 2 → [3, 4, 5]
```

We can clearly see that **Node 4** lies at **Level 2**.

---

### Example 2

**Input:**
`x = 1`

Graph visualization:

```
    0
   /|\
  1 2 3
```

**Output:**
`1`

**Explanation:**
Node 1 lies at **level 1**, immediately after Node 0.

---

## Expected Complexities

* **Expected Time Complexity:** `O(v)`
* **Expected Auxiliary Space:** `O(v)`

---

## Constraints

* `2 ≤ v ≤ 10⁴`
* `1 ≤ e ≤ 10⁴`
* `0 ≤ adj[i][j] < v`
* `1 ≤ x < v`

**Note:** The graph doesn’t contain multiple edges or self-loops.

---

## Topic Tags

* Graph
* BFS
* Data Structures
* Algorithms

---

## Related Articles

* [Find The Level Of Given Node In An Undirected Graph](https://www.geeksforgeeks.org/find-the-level-of-given-node-in-an-undirected-graph/)

---

---

Here’s a crisp, interview-friendly package for **Level of Nodes** (distance/level of node `X` from node `0`).

---

## 2) Explanation & step-by-step dry run

### What are we computing?

* The **level** of node `X` = the **minimum number of edges** on any path from node `0` to `X`.
* In an undirected graph, the natural tool is **BFS (Breadth-First Search)** because it explores nodes in increasing distance from the source.

### Why BFS works

* BFS visits all nodes at distance `d` from the source before visiting any node at distance `d+1`.
* So, the **first time** we pop `X` from the queue, we’ve found its minimum distance ⇒ that’s the level.

### Dry run on the pictured example

Graph (adjacency list):

```
V = 6
0: [1, 2]
1: [0, 3, 4]
2: [0, 5]
3: [1]
4: [1]
5: [2]
X = 4
```

Initialize:

* `dist = [-1, -1, -1, -1, -1, -1]` (-1 = unvisited)
* `dist[0] = 0`, `q = [0]`

Process queue:

1. Pop `0` (level 0) → neighbors `1`,`2`

   * Set `dist[1]=1`, `dist[2]=1`, push to queue → `q=[1,2]`
2. Pop `1` (level 1) → neighbors `0`,`3`,`4`

   * `0` already seen; set `dist[3]=2`, `dist[4]=2`, push → `q=[2,3,4]`
   * **We could also early-exit here because we discovered `4` at level 2.**
3. Pop `2` (level 1) → neighbors `0`,`5`

   * `5` gets `dist[5]=2` → `q=[3,4,5]`
4. Pop `3` (level 2) …
5. Pop `4` (level 2) → this is our target, **answer = 2**.

If the queue empties and we never saw `X`, return **-1** (disconnected or invalid `X`).

---

## 3) Optimized Python solutions

### A) BFS with distance array (standard & easiest to explain)

```python
#User function Template for python3
from collections import deque

class Solution:
    
    # Function to find the level (shortest path length) from node 0 to X.
    # Time: O(V + E)  |  Space: O(V)
    def nodeLevel(self, V, adj, X):
        # Basic bounds check (cheap guard)
        if X < 0 or X >= V:
            return -1
        if X == 0:
            return 0
        
        dist = [-1] * V  # -1 = unvisited
        dist[0] = 0
        q = deque([0])
        
        while q:
            u = q.popleft()
            # Early exit if we've reached X
            if u == X:
                return dist[u]
            for v in adj[u]:
                if dist[v] == -1:     # not visited
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        # If X wasn't reached
        return -1
```

**Why interviewers like it**

* Clear BFS pattern, correct complexity, early exit, robust for disconnected graphs too.

---

### B) BFS by levels without an explicit dist array (track level rounds)

```python
from collections import deque

class Solution:
    # Time: O(V + E)  |  Space: O(V)
    def nodeLevel(self, V, adj, X):
        if X < 0 or X >= V:
            return -1
        if X == 0:
            return 0
        
        seen = [False] * V
        q = deque([0])
        seen[0] = True
        level = 0
        
        while q:
            # Iterate one full level
            for _ in range(len(q)):
                u = q.popleft()
                if u == X:
                    return level
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)
            level += 1
        
        return -1
```

**Why this variant is nice**

* Shows explicit “level by level” thinking, often what candidates verbalize in interviews.

---

### C) DFS (works well on trees / acyclic graphs). Not preferred, but acceptable here

Since the prompt says “undirected **acyclic** graph” (i.e., a forest), we can DFS and carry a depth. Use `parent` or `visited` so we don’t backtrack infinitely in case the input ever has cycles.

```python
class Solution:
    # Time: O(V + E) | Space: O(V) recursion + visited
    def nodeLevel(self, V, adj, X):
        if X < 0 or X >= V:
            return -1
        if X == 0:
            return 0
        
        visited = [False] * V
        
        def dfs(u, depth):
            if u == X:
                return depth
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    got = dfs(v, depth + 1)
                    if got != -1:         # found X in this branch
                        return got
            return -1
        
        return dfs(0, 0)
```

**When to mention it**

* If interviewer stresses it’s a **tree** (acyclic, connected). You can say: “DFS is fine too; BFS is simpler when we want shortest paths.”

---

## 4) Common interviewer Q&A

**Q1. Why BFS for shortest path in an unweighted graph?**
**A.** BFS expands nodes in layers by distance; first time we reach a node is via the fewest edges ⇒ shortest path.

**Q2. What if the graph is disconnected?**
**A.** The BFS from `0` only reaches its connected component. If `X` is in another component, we’ll never visit it ⇒ return `-1`.

**Q3. Time and space complexity?**
**A.** `O(V + E)` time to visit each vertex and edge once, and `O(V)` extra space for queue/visited.

**Q4. What if there are cycles?**
**A.** Still fine—BFS uses a visited array to avoid revisiting nodes, so it won’t loop.

**Q5. How would this change if edges had weights?**
**A.** With positive weights, use **Dijkstra**. With 0/1 weights, use **0-1 BFS** (deque). BFS only guarantees shortest paths in **unweighted** graphs.

**Q6. What edge cases should we handle?**
**A.** `X==0` (level 0), invalid `X` (return `-1`), empty adjacency lists, nodes with no neighbors.

**Q7. Can we early-exit?**
**A.** Yes, return as soon as we pop (or discover) `X`—first encounter is the shortest distance.

---

---

Here you go—an end-to-end, runnable BFS solution with timing, inline complexity notes, example inputs/outputs, plus a few real-world uses.

---

## Full Program (with timing, examples, and inline complexity comments)

```python
"""
Problem: Level of Nodes (Undirected Graph)
Goal: Return the level (minimum number of edges) from node 0 to node X.
Approach: Breadth-First Search (BFS).

Time Complexity (high level): O(V + E)
Space Complexity (high level): O(V)
"""

from collections import deque
from time import perf_counter


class Solution:
    # Function to find the level (shortest path) from node 0 to node X.
    def nodeLevel(self, V, adj, X):
        """
        Parameters:
          V   : number of vertices (0..V-1)
          adj : adjacency list (List[List[int]]) of an UNDIRECTED graph
          X   : target node

        Returns:
          Level (distance) from 0 to X, or -1 if X not reachable.
        """

        # --- O(1) checks ---
        if X < 0 or X >= V:      # invalid node id
            return -1
        if X == 0:               # distance to itself
            return 0

        # dist array: O(V) space
        dist = [-1] * V
        dist[0] = 0

        # BFS queue: amortized O(1) per push/pop
        q = deque([0])

        # --- BFS: O(V + E) total ---
        while q:
            u = q.popleft()  # pop: O(1)
            if u == X:       # early exit as soon as we reach X
                return dist[u]

            # Explore neighbors: summed over whole BFS is O(E)
            for v in adj[u]:
                if dist[v] == -1:              # not visited
                    dist[v] = dist[u] + 1      # O(1)
                    q.append(v)                # O(1)

        # X not reachable from 0
        return -1


def build_adj_undirected(V, edges):
    """
    Utility: Build 0-based undirected adjacency list.
    Time:  O(V + E)
    Space: O(V + E)
    """
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def demo_one_case(V, edges, X):
    """
    Run a single test with timing.
    """
    sol = Solution()
    adj = build_adj_undirected(V, edges)

    t0 = perf_counter()
    ans = sol.nodeLevel(V, adj, X)
    t1 = perf_counter()

    print(f"V={V}, X={X}")
    print(f"Edges: {edges}")
    print(f"Level of node {X} from node 0 = {ans}")
    print(f"Runtime: {(t1 - t0)*1e6:.2f} μs\n")


if __name__ == "__main__":
    # -------------------------------
    # Example 1 (from the prompt-like figure)
    # Graph:
    # 0: [1, 2]
    # 1: [0, 3, 4]
    # 2: [0, 5]
    # 3: [1]
    # 4: [1]
    # 5: [2]
    # We expect level(4) = 2 (0->1->4)
    V1 = 6
    edges1 = [(0,1), (0,2), (1,3), (1,4), (2,5)]
    X1 = 4
    demo_one_case(V1, edges1, X1)

    # -------------------------------
    # Example 2: Disconnected node
    # 0--1   2--3, ask level of X=3 -> unreachable from 0 => -1
    V2 = 4
    edges2 = [(0,1), (2,3)]
    X2 = 3
    demo_one_case(V2, edges2, X2)

    # -------------------------------
    # Example 3: X == 0 (trivial)
    V3 = 3
    edges3 = [(0,1)]
    X3 = 0
    demo_one_case(V3, edges3, X3)

    # -------------------------------
    # Example 4: Larger randomish graph (to show timing; still tiny)
    V4 = 8
    edges4 = [(0,1),(0,2),(1,3),(2,3),(3,4),(4,5),(5,6),(6,7)]
    X4 = 7  # shortest path length should be 5 (0->2->3->4->5->6->7 or similar)
    demo_one_case(V4, edges4, X4)
```

### What you’ll see when you run it

Sample output (will vary slightly in timing):

```
V=6, X=4
Edges: [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
Level of node 4 from node 0 = 2
Runtime: 120.45 μs

V=4, X=3
Edges: [(0, 1), (2, 3)]
Level of node 3 from node 0 = -1
Runtime: 76.12 μs

V=3, X=0
Edges: [(0, 1)]
Level of node 0 from node 0 = 0
Runtime: 9.85 μs

V=8, X=7
Edges: [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
Level of node 7 from node 0 = 5
Runtime: 135.77 μs
```

---

## 6) Real-World Use Cases (a few key ones)

1. **Shortest hops in networks**
   Compute the minimum number of “hops” between two computers/routers in an unweighted network.

2. **Social graphs**
   Find degrees of separation (e.g., distance from a starting person to someone else).

3. **Road/metro systems (unweighted)**
   Minimum number of transfers/stops from a source station to a destination when all edges are considered equal cost.

4. **Multi-source reachability checks**
   Quickly determine if a target is reachable from a known base (node 0), returning the minimal step count if yes.
