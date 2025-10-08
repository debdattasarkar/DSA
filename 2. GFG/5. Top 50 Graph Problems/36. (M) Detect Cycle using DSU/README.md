
---

# 🧩 Detect Cycle using DSU

### Difficulty: Medium

**Accuracy:** 48.37%
**Submissions:** 66K+
**Points:** 4
**Average Time:** 15 minutes

---

## 🧠 Problem Statement

Given an **undirected graph** with **no self loops** with `V` (from 0 to V-1) nodes and `E` edges, the task is to check if there is **any cycle** in the undirected graph.

> **Note:** Solve the problem using **Disjoint Set Union (DSU)**.

---

## 🧾 Examples

### Example 1:

#### Input:

```
V = 5, E = 5
Edges = [
    [0, 1],
    [1, 3],
    [3, 2],
    [2, 4],
    [4, 0]
]
```

#### Output:

```
1
```

#### Explanation:

There is a cycle between `0 -> 2 -> 4 -> 0`.

---

### Example 2:

#### Input:

```
V = 5, E = 4
Edges = [
    [0, 3],
    [3, 1],
    [0, 2],
    [2, 4]
]
```

#### Output:

```
0
```

#### Explanation:

The graph doesn't contain any cycle.

---

## 🎯 Your Task

You don't need to read input or print anything.
Your task is to complete the function **`detectCycle()`** which takes:

* Number of vertices in the graph, denoting as **`V`**
* **Adjacency list** `adj`

and returns:

* `1` if graph contains **any cycle**
* `0` otherwise.

---

## ⏱ Expected Time and Space Complexity

| Complexity Type     | Complexity |
| ------------------- | ---------- |
| **Time**            | O(V + E)   |
| **Auxiliary Space** | O(V)       |

---

## ⚙️ Constraints

```
2 ≤ V ≤ 10^4
1 ≤ E ≤ 10^4
```

---

## 🏷 Topic Tags

* Graph
* Disjoint Set
* Data Structures

---

## 🔗 Related Articles

* [Detect Cycle in Graph Using DSU](https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-disjoint-set/)

---

## 🧩 Intuition

The **Disjoint Set Union (DSU)** or **Union-Find** algorithm is perfect for detecting cycles in undirected graphs.

* We treat each vertex as part of a **set**.
* Initially, each vertex is its **own parent** (disjoint).
* For each edge (u, v):

  * If `find(u)` and `find(v)` are the same → they belong to the same set → **cycle found**.
  * Otherwise, we **union(u, v)** (merge their sets).

---

### 🔍 How DSU Detects Cycle

* DSU maintains **parent[]** and **rank[]** (for optimization).
* The key functions:

  1. **find(x):** Finds the representative parent of x with path compression.
  2. **union(x, y):** Merges two sets if they are disjoint.
* While adding edges:

  * If both vertices already belong to the same parent → a cycle exists.

---

## 🧮 Example Dry Run

Let’s dry-run **Example 1** step-by-step:

```
V = 5, E = 5
Edges = [[0,1], [1,3], [3,2], [2,4], [4,0]]
```

Initially:

```
Parent = [0,1,2,3,4]
Rank   = [0,0,0,0,0]
```

### Process each edge:

1️⃣ Edge [0, 1]

* find(0) = 0, find(1) = 1 → different sets
  → union(0, 1)
  ✅ No cycle yet.

Parent = [0,0,2,3,4]

---

2️⃣ Edge [1, 3]

* find(1) → find(0) → 0
* find(3) = 3
  → union(0, 3)
  ✅ Still no cycle.

Parent = [0,0,2,0,4]

---

3️⃣ Edge [3, 2]

* find(3) → 0
* find(2) = 2
  → union(0, 2)
  ✅ Still no cycle.

Parent = [0,0,0,0,4]

---

4️⃣ Edge [2, 4]

* find(2) → 0
* find(4) = 4
  → union(0, 4)
  ✅ Still no cycle.

Parent = [0,0,0,0,0]

---

5️⃣ Edge [4, 0]

* find(4) = 0, find(0) = 0 → SAME parent
  🚨 **Cycle detected!**

Hence output = `1`.

---

## ✅ Interview-Expected Optimized Solution (Python)

```python
# User function Template for python3

class Solution:
    def find(self, parent, i):
        # Path compression optimization
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        # Union by rank optimization
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def detectCycle(self, V, adj):
        parent = [i for i in range(V)]
        rank = [0] * V
        
        # To avoid double edges, store unique ones
        seen = set()
        
        for u in range(V):
            for v in adj[u]:
                if (v, u) in seen:
                    continue
                seen.add((u, v))
                
                x = self.find(parent, u)
                y = self.find(parent, v)
                
                if x == y:
                    return 1  # Cycle found
                self.union(parent, rank, x, y)
        return 0
```

---

## 🧩 Time and Space Complexity Analysis

| Step              | Operation                       | Time           | Space |
| ----------------- | ------------------------------- | -------------- | ----- |
| Initialization    | Creating parent[] and rank[]    | O(V)           | O(V)  |
| Find              | Amortized with path compression | O(α(V)) ≈ O(1) | -     |
| Union             | With rank optimization          | O(α(V)) ≈ O(1) | -     |
| Process all edges | Iterate all adjacency pairs     | O(V + E)       | O(V)  |

> ✅ **Overall:**
> Time Complexity → **O(V + E)**
> Space Complexity → **O(V)**

---

## 💡 Real-World Use Cases

1. **Network Connectivity Checks**
   Used to detect **loops** in computer networks (e.g., LAN topologies, routers).

2. **Cycle Detection in Electrical Circuits**
   Ensures that the design of circuit graphs does not form feedback loops.

3. **Kruskal’s Minimum Spanning Tree (MST)**
   DSU cycle detection is a critical part of Kruskal’s algorithm for MST construction.

4. **Cluster Merging in Data Mining**
   Used to efficiently track merges of clusters without redundant overlaps.

---

---

awesome — here’s the interview-ready pack for **Detect Cycle in an Undirected Graph using DSU**:

* quick intuition + **step-by-step dry run**
* two Python solutions in your required signature:

  1. **Optimized DSU** (path compression + union by rank) — what interviewers expect
  2. **Brute DSU** (no compression/rank) — to contrast why optimizations matter
     *(bonus: a concise DFS approach included after DSU, in case they ask for a non-DSU method)*
* tight **interviewer Q&A**

---

## 2) Intuition & step-by-step dry run

### Idea (why DSU works)

Treat each vertex as belonging to a **set**. For every undirected edge `(u, v)`:

* If `find(u) == find(v)`, `u` and `v` are already in the **same set** → adding this edge would **close a cycle** → **cycle exists**.
* Otherwise `union(u, v)` (merge the two components) and continue.

To keep operations near O(1), use:

* **Path compression** in `find` (flatten trees on the fly),
* **Union by rank/size** (attach smaller tree under larger).

**Important:** In an adjacency list of an undirected graph, each edge appears **twice** (u→v and v→u). We must only process each **unique** edge once. An easy way is to only process when `u < v`, or keep a `seen` set of undirected pairs.

---

### Dry run on Example 1

```
V = 5
Edges (undirected): (0,1), (1,3), (3,2), (2,4), (4,0)

Initially:
parent = [0,1,2,3,4]          # each is its own parent
rank   = [1,1,1,1,1]
```

Process unique edges in order:

1. (0,1): find(0)=0, find(1)=1 → different → union(0,1)
   parent: 1 under 0 (rank[0] becomes 2)

2. (1,3): find(1)→root 0, find(3)=3 → different → union(0,3)
   parent[3] = 0

3. (3,2): find(3)→0, find(2)=2 → different → union(0,2)
   parent[2] = 0

4. (2,4): find(2)→0, find(4)=4 → different → union(0,4)
   parent[4] = 0

5. (4,0): find(4)→0, find(0)=0 → **same root** → **cycle detected** → return `1`.

---

## 3) Python — optimized & brute DSU (plus DFS bonus)

All versions use your required signature:

```python
class Solution:

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        # code here
```

### A) Optimized DSU (path compression + union by rank) — **recommended**

```python
class Solution:

    # --- find with path compression (amortized ~ O(1)) ---
    def _find(self, x, parent):
        if parent[x] != x:
            parent[x] = self._find(parent[x], parent)  # compress path
        return parent[x]

    # --- union by rank (attach smaller rank under larger) ---
    def _union(self, a, b, parent, rank):
        ra, rb = self._find(a, parent), self._find(b, parent)
        if ra == rb:
            return False  # already in same set -> would form a cycle if used
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[rb] < rank[ra]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        """
        V : number of vertices (0..V-1)
        adj : adjacency list (undirected), i.e., for each edge (u,v), v in adj[u] and u in adj[v]

        Algorithm:
          - Initialize DSU.
          - For each unique edge (u,v) with u < v:
              * If find(u) == find(v) -> cycle -> return 1
              * Else union(u,v)
          - No cycle encountered -> return 0

        Complexity:
          Time  : O(V + E * α(V))  ~ O(V + E)
          Space : O(V)
        """
        parent = [i for i in range(V)]   # O(V)
        rank   = [1] * V                 # O(V)

        # Process each undirected edge exactly once to avoid duplicates.
        for u in range(V):
            for v in adj[u]:
                if u < v:  # ensures (u,v) handled once
                    ru, rv = self._find(u, parent), self._find(v, parent)
                    if ru == rv:
                        return 1        # cycle found
                    # merge components
                    self._union(ru, rv, parent, rank)

        return 0  # no cycle
```

### B) Brute DSU (no compression, no rank) — **for contrast**

```python
class Solution:

    def _find(self, x, parent):
        # climb without compression -> worst-case O(V)
        while parent[x] != x:
            x = parent[x]
        return x

    def _union(self, a, b, parent):
        ra, rb = self._find(a, parent), self._find(b, parent)
        if ra == rb:
            return False
        parent[rb] = ra  # arbitrary root choice -> can create tall trees
        return True

    def detectCycle(self, V, adj):
        """
        Simpler but slower DSU.
        Time  : up to O(V + E*V) in worst cases (degenerate chains)
        Space : O(V)
        """
        parent = [i for i in range(V)]
        for u in range(V):
            for v in adj[u]:
                if u < v:
                    if self._find(u, parent) == self._find(v, parent):
                        return 1
                    self._union(u, v, parent)
        return 0
```

### (Bonus) DFS approach (not DSU, but often asked as an alternative)

```python
class Solution:

    def detectCycle(self, V, adj):
        """
        DFS on undirected graph: if we visit a neighbor that is visited and
        not the parent, we've found a cycle.
        Time  : O(V + E)
        Space : O(V) recursion/visited
        """
        visited = [False] * V

        def dfs(u, parent):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v, u):
                        return True
                elif v != parent:
                    return True  # back-edge to an already visited vertex (not parent)
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return 1
        return 0
```

---

## 4) Interview Q&A (high-yield)

**Q1. Why does DSU detect cycles in undirected graphs?**
Because if an edge `(u,v)` connects two vertices already in the **same connected component** (`find(u) == find(v)`), then adding it necessarily creates a **cycle**.

**Q2. What are the DSU optimizations and why use them?**

* **Path compression** makes every `find` flatten paths → future finds are faster.
* **Union by rank/size** keeps the tree shallow while unioning.
  Together they give **amortized near O(1)** per op (formally `O(α(V))`).

**Q3. How do you avoid double-counting edges with an adjacency list?**
Process only when `u < v` (or store a `seen` set of `(min(u,v), max(u,v))`). Each undirected edge is then handled once.

**Q4. Time/Space complexity of your optimized DSU solution?**

* **Time:** `O(V + E * α(V))` ≈ `O(V + E)`
* **Space:** `O(V)` for `parent` and `rank`.

**Q5. How would you modify for a **directed** graph?**
DSU is not directly suitable for cycle detection in directed graphs. Use **DFS with colors** (white/gray/black) or **Kahn’s algorithm** (topological sort) instead.

**Q6. Can the graph have self-loops or multi-edges?**

* The prompt says **no self loops**. If they existed, `(u,u)` is an immediate cycle.
* **Multi-edges** between the same `(u,v)` pair cause a cycle if both ends are already in the same set by the time the second edge is processed.

**Q7. Real-world contexts?**

* **Network topology** loop detection,
* **Kruskal’s MST** (skip edge if endpoints in same set),
* Dynamic **connectivity queries**.

---

---

here’s a **runnable, interview-style full program** for **Detect Cycle in an Undirected Graph using DSU** that:

* implements the exact signature you asked for,
* shows outputs for two sample graphs (cycle / no cycle),
* and uses **timeit** to report average runtime per call (also compares against a naïve DSU to highlight the optimization win).

I’ve added **inline comments** that state **time & space** costs right where they apply.

---

## 5) Full Python program (with inline complexity notes + timings)

```python
"""
Detect Cycle in an Undirected Graph using DSU (Union-Find)
----------------------------------------------------------

Core idea:
  • For each *unique* undirected edge (u, v):
      - If find(u) == find(v)  -> cycle exists.
      - Else union(u, v).

Optimizations:
  • Path Compression in find()
  • Union by Rank in union()

Complexities (with both optimizations):
  • Time per op (amortized): O(α(V))  [inverse Ackermann; < 5 for all practical sizes]
  • Overall time            : O(V + E * α(V))  ≈ O(V + E)
  • Extra space             : O(V) for parent[] and rank[].
"""

from typing import List
import timeit


# ============================ Optimized DSU Solution ============================ #
class Solution:
    # ----- find with path compression: amortized ~O(1) -----
    def _find(self, x: int, parent: List[int]) -> int:
        # Path compression flattens the tree. Future finds become faster.
        # Time (amortized): O(α(V)), Space: O(1) extra.
        if parent[x] != x:
            parent[x] = self._find(parent[x], parent)
        return parent[x]

    # ----- union by rank: attach lower-rank root under higher-rank root -----
    def _union(self, a: int, b: int, parent: List[int], rank: List[int]) -> bool:
        # Returns True if merged; False if already same set (which would indicate a cycle
        # when used while adding edges).
        # Time (amortized): O(α(V)), Space: O(1) extra.
        ra, rb = self._find(a, parent), self._find(b, parent)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[rb] < rank[ra]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V: int, adj: List[List[int]]) -> int:
        """
        Parameters:
          V   : number of vertices (0..V-1)
          adj : undirected adjacency list; for each edge u-v, v in adj[u] and u in adj[v]

        Algorithm:
          - Initialize DSU arrays parent[] and rank[]  -> O(V) time/space.
          - For each vertex u:
              For each neighbor v in adj[u]:
                Process each undirected edge once by enforcing u < v.
                If find(u) == find(v), cycle -> return 1.
                Else union(u, v).
          - If no cycle found, return 0.

        Complexity:
          Time  : O(V + E * α(V)) ≈ O(V + E)
          Space : O(V)
        """
        parent = [i for i in range(V)]  # O(V) space, O(V) time to init
        rank   = [1] * V                # O(V) space

        # Iterate over each unique edge once (use u < v to avoid double processing)
        for u in range(V):              # sum of degrees over all u is 2E
            for v in adj[u]:
                if u < v:               # ensures each undirected edge handled once
                    ru, rv = self._find(u, parent), self._find(v, parent)  # ~O(1) amortized
                    if ru == rv:
                        return 1        # cycle detected
                    self._union(ru, rv, parent, rank)                      # ~O(1) amortized
        return 0                        # no cycle found


# ============================= Naïve DSU (for timing contrast) ============================= #
class NaiveDSU:
    def _find(self, x: int, parent: List[int]) -> int:
        # No path compression -> can be O(V) in worst case
        while parent[x] != x:
            x = parent[x]
        return x

    def _union(self, a: int, b: int, parent: List[int]) -> bool:
        ra, rb = self._find(a, parent), self._find(b, parent)
        if ra == rb:
            return False
        parent[rb] = ra  # arbitrary root choice -> trees can get tall
        return True

    def detectCycle(self, V: int, adj: List[List[int]]) -> int:
        parent = [i for i in range(V)]
        for u in range(V):
            for v in adj[u]:
                if u < v:
                    if self._find(u, parent) == self._find(v, parent):
                        return 1
                    self._union(u, v, parent)
        return 0


# ============================== Helpers: graph construction & timing ============================== #
def make_adj(V: int, edges: List[List[int]]) -> List[List[int]]:
    """Utility to convert edge list to undirected adjacency list. O(V+E) time/space."""
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def bench(func, *args, number=200) -> float:
    """Return avg seconds/run via timeit. For small inputs, Python overhead dominates."""
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ============================================ Demo ============================================ #
if __name__ == "__main__":
    print("=== Detect Cycle in Undirected Graph using DSU — Demo & Timings ===\n")

    # ----- Example 1 (has cycle) -----
    V1 = 5
    edges1 = [[0, 1], [1, 3], [3, 2], [2, 4], [4, 0]]  # 0-2-4-0 makes a cycle
    adj1 = make_adj(V1, edges1)

    sol = Solution()
    ans1 = sol.detectCycle(V1, adj1)
    print(">>> Example 1")
    print("V =", V1, "Edges =", edges1)
    print("Cycle?", ans1, "(1 means cycle present; expected: 1)\n")

    # ----- Example 2 (no cycle) -----
    V2 = 5
    edges2 = [[0, 3], [3, 1], [0, 2], [2, 4]]  # forms a tree (no cycle)
    adj2 = make_adj(V2, edges2)

    ans2 = sol.detectCycle(V2, adj2)
    print(">>> Example 2")
    print("V =", V2, "Edges =", edges2)
    print("Cycle?", ans2, "(expected: 0)\n")

    # ----- Micro-benchmarks: optimized vs naive on a larger sparse graph -----
    print("=== Timings (average seconds per run) ===")
    # Build a 50k-vertex sparse graph: a long chain + a few extra chords + one back-edge
    V3 = 50_000
    chain_edges = [[i, i + 1] for i in range(V3 - 1)]  # tree, no cycle
    chord_edges = [[i, (i + 1000) % V3] for i in range(0, V3, 5000)]  # sparse extra edges
    cycle_edge = [[V3 - 1, 0]]  # add one extra edge to create a single cycle
    edges3 = chain_edges + chord_edges + cycle_edge
    adj3 = make_adj(V3, edges3)

    # Optimized DSU timing
    runs = 10
    t_opt = bench(Solution().detectCycle, V3, adj3, number=runs)
    print(f"Optimized DSU  : V={V3}, E≈{len(edges3)}  runs={runs:3d}  -> {t_opt:.6f} s/run")

    # Naive DSU timing (smaller runs to keep it reasonable)
    runs_naive = 3
    t_naive = bench(NaiveDSU().detectCycle, V3, adj3, number=runs_naive)
    print(f"Naive DSU      : V={V3}, E≈{len(edges3)}  runs={runs_naive:3d} -> {t_naive:.6f} s/run")

    print("\nNotes:")
    print(" • Optimized DSU uses path compression + union-by-rank -> near O(1) per op.")
    print(" • Naive DSU can degrade badly on tall trees -> much slower.")
    print(" • Space used by DSU is O(V).")
```

### What you’ll see when you run it

* Example 1 → `Cycle? 1`
* Example 2 → `Cycle? 0`
* Then two timing lines comparing **optimized DSU** vs **naïve DSU** (exact numbers vary by machine).

---

## 6) Real-World Use Cases (the important ones)

1. **Kruskal’s Minimum Spanning Tree (MST)**
   While scanning edges in increasing weight, use DSU to **skip** edges whose endpoints are already connected (i.e., adding them would form a **cycle**).

2. **Network / Topology Loop Detection**
   Detect accidental loops in **LANs**, **overlay networks**, or **peer-to-peer overlays** as links are added, in near real time.

3. **Dynamic Connectivity Queries**
   Maintain components as edges arrive (e.g., **friend groups**, **cluster merging**, **percolation simulations**) and detect whether a new relation introduces a loop.