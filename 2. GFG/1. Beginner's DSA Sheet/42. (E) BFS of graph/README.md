# BFS of graph

**Difficulty:** Easy
**Accuracy:** 44.09%
**Submissions:** 516K+
**Points:** 2
**Average Time:** 10m

---

## Problem Statement

Given a **connected undirected graph** containing `V` vertices, represented by a 2-D adjacency list `adj[][]`, where each `adj[i]` represents the list of vertices connected to vertex `i`. Perform a **Breadth First Search (BFS)** traversal starting from vertex `0`, visiting vertices from **left to right according to the given adjacency list**, and return a list containing the BFS traversal of the graph.

**Note:** Do traverse in the **same order** as they are in the given **adjacency list**.

---

## Examples

### Example 1

**Input:** `adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]`

**Output:** `[0, 2, 3, 1, 4]`

**Explanation:**
Starting from `0`, the BFS traversal will follow these steps:
Visit `0` → Output: `0`
Visit `2` (first neighbor of `0`) → Output: `0, 2`
Visit `3` (next neighbor of `0`) → Output: `0, 2, 3`
Visit `1` (next neighbor of `0`) → Output: `0, 2, 3, 1`
Visit `4` (neighbor of `2`) → Final Output: `0, 2, 3, 1, 4`.

---

### Example 2

**Input:** `adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]`

**Output:** `[0, 1, 2, 3, 4]`

**Explanation:**
Starting from `0`, the BFS traversal proceeds as follows:
Visit `0` → Output: `0`
Visit `1` (the first neighbor of `0`) → Output: `0, 1`
Visit `2` (the next neighbor of `0`) → Output: `0, 1, 2`
Visit `3` (the first neighbor of `2` that hasn't been visited yet) → Output: `0, 1, 2, 3`
Visit `4` (the next neighbor of `2`) → Final Output: `0, 1, 2, 3, 4`.

---

## Constraints

* `1 ≤ V = adj.size() ≤ 10^4`
* `1 ≤ adj[i][j] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(V + E)`
* **Auxiliary Space:** `O(V + E)`

---

## Company Tags

* Flipkart
* Amazon
* Microsoft
* Samsung
* Ola Cabs
* Adobe
* SAP Labs

---

## Topic Tags

* Graph
* BFS
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Adobe Interview Experience Set 48 Campus

---

## Related Articles

* [Breadth First Search Or Bfs For A Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

---

---

Here’s a tight, interview-ready guide for **BFS traversal from node 0** on a connected, undirected graph.

---

## 2) Explanation + step-by-step dry run

**Goal:** Return the BFS order starting at vertex `0`, visiting neighbors **in the same order as given** in each `adj[i]`.

**Core idea (Breadth-First Search):**

* Use a **queue** to explore vertices in layers: distance 0 (start), then all distance 1, then distance 2, etc.
* Maintain a **visited** array so each vertex is enqueued once.

**Why it works:**
BFS always removes the earliest-seen vertex from the queue; therefore all vertices at distance `d` are processed before any at distance `d+1`. With “mark visited when enqueuing”, each vertex appears at most once in the queue → `O(V+E)`.

### Dry run on Example 1

`adj = [[2,3,1], [0], [0,4], [0], [2]]` (neighbors already ordered)

Start at `0`

* `visited = [T, F, F, F, F]`, `queue = [0]`, `order = []`

1. pop `0` → `order = [0]`
   neighbors: `2, 3, 1`
   enqueue `2,3,1` (mark visited)
   `visited = [T, T, T, T, F]`, `queue = [2, 3, 1]`

2. pop `2` → `order = [0, 2]`
   neighbors: `0, 4` → `0` seen; enqueue `4`
   `visited = [T, T, T, T, T]`, `queue = [3, 1, 4]`

3. pop `3` → `order = [0, 2, 3]`
   neighbors: `0` (seen) → nothing added
   `queue = [1, 4]`

4. pop `1` → `order = [0, 2, 3, 1]`
   neighbors: `0` (seen)
   `queue = [4]`

5. pop `4` → `order = [0, 2, 3, 1, 4]`
   neighbors: `2` (seen)
   `queue = []` → done ✅

---

## 3) Python solutions (brute → clean/optimized)

### A) Canonical BFS with `deque` (recommended)

```python
from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        """
        Start at node 0, traverse neighbors in the given adjacency order.
        Time:  O(V + E)  -- each node/edge processed a constant number of times
        Space: O(V)      -- visited + queue
        """
        V = len(adj)
        order = []
        if V == 0:
            return order

        visited = [False] * V
        q = deque()

        # BFS root is fixed at 0 per problem statement
        visited[0] = True
        q.append(0)

        while q:
            u = q.popleft()          # O(1)
            order.append(u)
            for v in adj[u]:         # iterate in given order
                if not visited[v]:
                    visited[v] = True
                    q.append(v)      # enqueue once per vertex

        return order
```

### B) “Brute-ish” queue using a Python list (still O(V+E) with head index)

> Using `pop(0)` would be **O(n²)** total; we avoid that by keeping a head index.

```python
class Solution:
    def bfs(self, adj):
        V = len(adj)
        order = []
        if V == 0: return order

        visited = [False] * V
        q = [0]               # list as queue
        visited[0] = True
        head = 0              # index of current front

        while head < len(q):  # amortized O(1) per pop via head++
            u = q[head]; head += 1
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)      # append is amortized O(1)
        return order
```

### C) Extension: BFS for **disconnected** graphs (if the judge ever changes the spec)

```python
from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)
        order, visited = [], [False] * V
        for s in range(V):
            if visited[s]: continue
            visited[s] = True
            q = deque([s])
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
        return order
```

*Still `O(V+E)`, just ensures we cover all components in order `0..V-1`.*

---

## 4) Likely interviewer Q\&A

**Q1. What’s the time and space complexity?**
**A.** `O(V+E)` time (each vertex/edge processed at most once), `O(V)` space for `visited` and queue.

**Q2. Why mark visited when enqueuing (not when dequeuing)?**
**A.** To guarantee each vertex is enqueued **at most once**; otherwise you may enqueue duplicates and blow up the queue.

**Q3. Does BFS find shortest paths?**
**A.** Yes, in **unweighted** graphs (or unit weights), BFS finds shortest path lengths by edge count (layer by layer).

**Q4. Why does adjacency order matter here?**
**A.** The problem asks to traverse neighbors **in the order provided**. BFS order can vary unless this is enforced.

**Q5. How to handle a disconnected graph?**
**A.** Loop over all vertices; start a new BFS from every unvisited vertex (see solution C). This preserves `O(V+E)`.

**Q6. Differences from DFS?**
**A.** BFS uses a **queue** (level order), DFS uses a **stack/recursion** (depth-first). BFS gives shortest paths in unweighted graphs; DFS doesn’t guarantee that.

**Q7. Any pitfalls?**
**A.** Using `list.pop(0)` (quadratic), forgetting to mark visited on enqueue, or not respecting given neighbor order.

---

---

All set! I ran a **complete inline Python program** that:

* Implements BFS starting at 0 with two variants (deque and list-queue),
* Prints inputs and outputs for both example graphs,
* Benchmarks on a 10,000-node line graph,
* And prints the **TOTAL MAIN RUNTIME** using `timeit.default_timer()`.

```python

# Re-run to display outputs
from collections import deque
import timeit
from typing import List

class Solution:
    def bfs(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)
        order: List[int] = []
        if V == 0:
            return order
        visited = [False] * V
        q = deque()
        visited[0] = True
        q.append(0)
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

    def bfs_list_queue(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)
        order: List[int] = []
        if V == 0:
            return order
        visited = [False] * V
        q = [0]
        visited[0] = True
        head = 0
        while head < len(q):
            u = q[head]; head += 1
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

def main():
    sol = Solution()
    print("=== BFS of Graph — Demo & Timing ===\n")
    adj1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print("Input 1 adj:", adj1)
    out1 = sol.bfs(adj1)
    print("Output 1 (deque BFS):", out1)
    out1b = sol.bfs_list_queue(adj1)
    print("Output 1 (list-queue):", out1b)
    print()
    adj2 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    print("Input 2 adj:", adj2)
    out2 = sol.bfs(adj2)
    print("Output 2 (deque BFS):", out2)
    out2b = sol.bfs_list_queue(adj2)
    print("Output 2 (list-queue):", out2b)
    print()
    V = 10000
    adj_line = [[] for _ in range(V)]
    for i in range(V-1):
        adj_line[i].append(i+1)
        adj_line[i+1].append(i)
    t0 = timeit.default_timer()
    res = sol.bfs(adj_line)
    t1 = timeit.default_timer()
    print(f"Timing on line graph with V={V}: BFS length={len(res)}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (the essentials)

* **Shortest paths in unweighted networks:** Find minimum hops between devices/users/servers; BFS gives true shortest paths by edge count.
* **Level-by-level processing:** Topological layers in organization structures, distance-k neighborhood queries, friend recommendations at distance 1–2.
* **Web crawlers / reachability:** Systematically explore pages/sites/components while preventing revisits with a visited set.
* **Broadcast/flood simulations:** Model propagation (rumors, packets, viruses) stepwise across a network.
* **AI/game grids:** Multi-source BFS for zone control, flood fill, or minimal moves in unweighted grids/mazes.

If you want, I can add a version that also returns **parent arrays** to reconstruct the shortest path tree, or a **multi-source** BFS template.
