# Bipartite Graph 🟢🔵

**Difficulty:** Medium
**Accuracy:** 31.25%
**Submissions:** 205K+
**Points:** 4
**Average Time:** 15m

---

Given a graph with **V** vertices (numbered from **0 to V-1**) and **E** edges, check whether the graph is **bipartite** or not.

A **bipartite graph** can be colored with two colors such that **no two adjacent vertices share the same color**. This means we can divide the graph’s vertices into two distinct sets where:

* All edges connect vertices from one set to vertices in the other set.
* No edges exist between vertices within the same set.

---

## Examples

### Example 1

**Input:** `V = 3`, `edges[][] = [[0, 1], [1,2]]`
**Output:** `true`
**Explanation:** The given graph can be colored in two colors, so it is a bipartite graph.

### Example 2

**Input:** `V = 4`, `edges[][] = [[0, 3], [1, 2], [3, 2], [0, 2]]`
**Output:** `false`
**Explanation:** The given graph **cannot** be colored in two colors such that the color of adjacent vertices differs. Hence, it is **not** bipartite.

---

## Constraints

* `1 ≤ V ≤ 2 * 10^5`
* `1 ≤ edges.size() ≤ 10^5`
* `1 ≤ edges[i][j] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(V + E)`
* **Auxiliary Space:** `O(V)`

---

## Company Tags

`Flipkart` `Microsoft` `Samsung`

---

## Topic Tags

`DFS` `Graph` `BFS` `Data Structures` `Algorithms`

---

## Related Interview Experiences

* Samsung SRIB Interview Experience 2018
* Samsung R&D Bangalore Interview (1 Year Experienced)
* Samsung Research Institute Bangalore – Research Engineer
* Flipkart Interview Experience for SDE 1 On Campus 2019 (Set 2)

---

## Related Articles

* [**Bipartite Graph**](https://www.geeksforgeeks.org/bipartite-graph/)


---

---

Here’s a compact, interview-ready package for **checking if an undirected graph is bipartite**.

---

## 2) Explanation + step-by-step dry run

**Idea:**
A graph is bipartite if you can 2-color its vertices so that no edge has the same color on both ends.
We can try to color each connected component using **BFS or DFS**:

* Uncolored start node → color `0`.
* Every neighbor must get `1 - color[u]`.
* If we ever see an edge `(u,v)` with `color[u] == color[v]`, the graph is **not** bipartite.

We must also handle **disconnected graphs**: run BFS/DFS from every uncolored node.

### Dry run 1 (bipartite)

`V=3, edges=[[0,1],[1,2]]`

1. Build adjacency: `0:[1], 1:[0,2], 2:[1]`.
2. Start at `0`: color[0]=0.
   Neigh 1 → color[1]=1.
   From 1: neigh 0 already 0 (OK), neigh 2 → color[2]=0.
3. From 2: neigh 1 already 1 (OK).
   No conflicts → **bipartite** (True).

### Dry run 2 (not bipartite)

`V=4, edges=[[0,3],[1,2],[3,2],[0,2]]` (triangle 0–3–2–0)

1. Adj: `0:[3,2], 1:[2], 2:[1,3,0], 3:[0,2]`.
2. Start at `0`: color[0]=0.
   Visit 3 → color[3]=1. Visit 2 → color[2]=1.
3. Process 3: neigh 2 has color 1 (same as 3) → **conflict** → **not** bipartite (False).

**Edge cases:**

* **Self loop** `(u,u)` ⇒ immediately not bipartite.
* **Multiple edges** are fine (just recheck same constraint).
* **Isolated vertices** are fine (each is a trivial component).

---

## 3) Optimized Python solutions (with interview-style inline comments)

### A) BFS 2-coloring (iterative, stack-safe) — recommended

```python
from collections import deque

class Solution:
    def isBipartite(self, V, edges):
        # Build adjacency list; O(V + E)
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:               # self-loop => cannot be bipartite
                return False
            adj[u].append(v)
            adj[v].append(u)
        
        color = [-1] * V             # -1 = uncolored; 0/1 are the two colors
        
        for s in range(V):           # cover disconnected graphs
            if color[s] != -1:
                continue
            # BFS from s
            color[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == -1:
                        color[w] = color[u] ^ 1  # opposite color
                        q.append(w)
                    elif color[w] == color[u]:
                        return False             # conflict
        return True                               # all components colored without conflicts
```

**Time:** `O(V + E)`
**Space:** `O(V)` (colors + queue)

---

### B) DFS 2-coloring (recursive, concise)

```python
class Solution:
    def isBipartite(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            if u == v:
                return False
            adj[u].append(v); adj[v].append(u)
        
        color = [-1] * V
        
        def dfs(u, c):
            color[u] = c
            for w in adj[u]:
                if color[w] == -1:
                    if not dfs(w, c ^ 1):   # color neighbor opposite
                        return False
                elif color[w] == c:
                    return False            # conflict
            return True
        
        for s in range(V):
            if color[s] == -1:
                if not dfs(s, 0):
                    return False
        return True
```

**Time:** `O(V + E)`
**Space:** `O(V)` (color + recursion stack; beware deep recursion on big graphs)

---

### C) Union-Find with “opposite set” trick (no graph traversal)

Use 2N nodes: for each vertex `u`, track `u` and `u+V` meaning “opposite set of u”.
For edge `(u,v)`: enforce `u` with `v+V` and `v` with `u+V`. If `find(u) == find(u+V)` for any `u`, not bipartite.

```python
class Solution:
    def isBipartite(self, V, edges):
        # parent/rank over 2*V nodes
        parent = list(range(2 * V))
        rank = [0] * (2 * V)
        
        def find(x):
            # path-compressed find
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        
        for u, v in edges:
            if u == v:                 # self-loop => not bipartite
                return False
            # u with opposite of v, v with opposite of u
            union(u, v + V)
            union(v, u + V)
            # immediate contradiction check is optional; final check covers it
            if find(u) == find(u + V) or find(v) == find(v + V):
                return False
        
        # Final consistency check
        for u in range(V):
            if find(u) == find(u + V):
                return False
        return True
```

**Time:** ~`O((V + E) α(2V))` (α = inverse Ackermann, practically constant)
**Space:** `O(V)`.

> Interview tip: BFS/DFS is the most expected. DSU solution is a nice alternative when asked to “avoid recursion/queues” or when constraints push for a union-find approach.

---

## 4) Likely Interview Q&A

**Q1. Why does 2-coloring detect bipartiteness?**
A1. A graph is bipartite iff it has **no odd cycle**. BFS/DFS alternates colors layer by layer; an odd cycle forces a same-color edge, which we detect as a conflict.

**Q2. How do you handle disconnected graphs?**
A2. Loop through all vertices; if a vertex is uncolored, start a BFS/DFS from it.

**Q3. What about self loops or multiple edges?**
A3. A self loop `(u,u)` instantly violates bipartiteness. Multiple edges don’t change the result (they just recheck the same constraint).

**Q4. Space/time complexity?**
A4. Both BFS and DFS are `O(V+E)` time and `O(V)` space. DSU is ~`O((V+E) α(V))` time, `O(V)` space.

**Q5. When would you prefer DSU?**
A5. When you want an iterative approach without graph traversal stacks/queues, or you’re already using DSU for other constraints so it integrates naturally.

**Q6. Does this work for directed graphs?**
A6. No—bipartiteness is defined for undirected graphs. For directed graphs you might be checking for 2-colorability of the underlying undirected version or solving a different property.

**Q7. What if recursion depth is a concern?**
A7. Use the **BFS** version to avoid recursion, or implement iterative DFS.

**Q8. Can you return the two sets as well?**
A8. Yes. After successful coloring, vertices with color `0` form set A, and color `1` form set B.


---

---

Below is a **complete, runnable Python program** that:

* Implements the **BFS 2-coloring** solution (most expected in interviews).
* Includes **inline comments** that note the **time & space complexity** of each relevant step.
* Shows **sample inputs** (both bipartite and non-bipartite), **prints outputs**, and uses `time.perf_counter()` to measure elapsed time for the full run.

---

```python
"""
Bipartite Graph Check — Full Program (BFS 2-coloring)

Approach:
- Build adjacency list O(V + E) time, O(V + E) space (dominated by edges storage).
- For each uncolored node, run BFS and color neighbors with opposite color.
- If we ever find an edge whose endpoints have the same color -> not bipartite.

Why BFS? Iterative (stack-safe), clean, and O(V+E) — exactly what interviewers expect.
"""

from collections import deque
from time import perf_counter


class Solution:
    def isBipartite(self, V, edges):
        """
        Parameters:
            V     : int            -> number of vertices labeled [0..V-1]
            edges : List[List[int]] -> undirected edges [[u,v], ...]

        Returns:
            bool: True if the graph is bipartite, else False
        """

        # ----- Build adjacency list -----
        # Time:  O(V + E)
        # Space: O(V + E) for the adjacency list itself
        adj = [[] for _ in range(V)]
        for u, v in edges:
            # Self-loop check (O(1)): immediate failure if present
            # Time: O(1) per edge
            # Space: O(1)
            if u == v:
                return False
            adj[u].append(v)
            adj[v].append(u)

        # color[v] = -1 means uncolored; 0 and 1 are the two colors
        # Space: O(V)
        color = [-1] * V

        # ----- Process all connected components -----
        # Outer loop visits each vertex at most once as a BFS source
        # Combined Time for all BFS traversals: O(V + E)
        for src in range(V):
            if color[src] != -1:
                continue

            # Initialize BFS for this component
            # Space (worst-case queue): O(V) in total over the whole run
            q = deque()
            color[src] = 0  # assign first color
            q.append(src)

            # ----- BFS -----
            # Each vertex and edge is processed at most once across the whole program
            # Time: O(V + E)
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == -1:
                        # Assign opposite color (O(1))
                        color[w] = color[u] ^ 1
                        q.append(w)
                    elif color[w] == color[u]:
                        # Found an edge with same-colored endpoints => not bipartite
                        return False

        # If we colored everything without conflicts, it's bipartite
        return True


# -------------------------
# Demo / Driver
# -------------------------
if __name__ == "__main__":
    start = perf_counter()

    sol = Solution()

    # ----------- Test Case 1: Bipartite -----------
    V1 = 3
    edges1 = [[0, 1], [1, 2]]  # 0—1—2 is a path => bipartite
    res1 = sol.isBipartite(V1, edges1)
    print("Test Case 1 (Expected: True)  ->", res1)

    # ----------- Test Case 2: Not Bipartite -----------
    # Triangle 0—3—2—0 causes odd cycle
    V2 = 4
    edges2 = [[0, 3], [1, 2], [3, 2], [0, 2]]
    res2 = sol.isBipartite(V2, edges2)
    print("Test Case 2 (Expected: False) ->", res2)

    # ----------- Test Case 3: Disconnected graph -----------
    # Component A: 0—1 (OK), Component B: 2—3—4 (path, also OK)
    V3 = 5
    edges3 = [[0, 1], [2, 3], [3, 4]]
    res3 = sol.isBipartite(V3, edges3)
    print("Test Case 3 (Expected: True)  ->", res3)

    # ----------- Test Case 4: Self-loop (immediate False) -----------
    V4 = 2
    edges4 = [[0, 0]]
    res4 = sol.isBipartite(V4, edges4)
    print("Test Case 4 (Expected: False) ->", res4)

    end = perf_counter()
    print(f"\nTotal program time: {end - start:.6f} seconds")
```

### Sample Output (will be very close to this)

```
Test Case 1 (Expected: True)  -> True
Test Case 2 (Expected: False) -> False
Test Case 3 (Expected: True)  -> True
Test Case 4 (Expected: False) -> False

Total program time: 0.000xxx seconds
```

---

## Complexity Summary (BFS approach)

* **Building adjacency list:** `O(V + E)` time, `O(V + E)` space
* **BFS over all components:** `O(V + E)` time, `O(V)` extra space for colors + queue
* **Overall:** `O(V + E)` time, `O(V + E)` space (dominated by adjacency list)

---

## 6) Real-World Use Cases (a few critical ones)

1. **Scheduling with two alternating slots/teams**
   Assign tasks/people to one of two groups where conflicts (edges) mean “can’t share the same slot/team.”

2. **Two-coloring social graphs**
   Separate users into two communities when edges denote rivalry/incompatibility; bipartiteness ensures no intra-group conflicts.

3. **Bipartite validation before matching**
   Many algorithms (e.g., maximum bipartite matching / assignment) require the graph to be bipartite. This check guards correctness early.

4. **Circuit design & netlist partitioning**
   Validate whether a set of components/wires can be partitioned into two layers without crossing constraints (approximate modeling).
