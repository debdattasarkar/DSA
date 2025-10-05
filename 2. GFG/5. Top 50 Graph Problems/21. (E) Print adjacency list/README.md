

---

# 🧭 Print Adjacency List

### Difficulty:

**Easy**

### Accuracy:

**43.42%**

### Submissions:

**172K+**

### Points:

**2**

---

### 🧩 Problem Description

Given an **undirected graph** with **V nodes** and **E edges**, create and return an **adjacency list** of the graph.
**0-based indexing** is followed everywhere.

---

### 🧠 Example 1:

#### Input:

```
V = 5, E = 7  
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
```

#### Output:

```
[[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
```

#### Explanation:

* Node 0 is connected to 1 and 4.
* Node 1 is connected to 0, 2, 3, and 4.
* Node 2 is connected to 1 and 3.
* Node 3 is connected to 1, 2, and 4.
* Node 4 is connected to 0, 1, and 3.

---

### 🧠 Example 2:

#### Input:

```
V = 4, E = 3  
edges = [[0,3], [0,2], [2,1]]
```

#### Output:

```
[[2,3], [2], [0,1], [0]]
```

#### Explanation:

* Node 0 is connected to 2 and 3.
* Node 1 is only connected to 2.
* Node 2 is connected to 0 and 1.
* Node 3 is only connected to 0.

---

### ⚙️ Constraints:

```
1 ≤ V, E ≤ 10⁵
```

---

### 🧮 Expected Complexities:

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V + E)

---

### 🧰 Topic Tags:

* Graph
* Data Structures

---

---

awesome — let’s make this crisp for interviews: quick intuition + a dry run, then two Python solutions in your requested signature (clean & optimal; plus a deliberately “brute/naïve” version to contrast), followed by tight interviewer Q&A.

---

## 2) Intuition & Dry Run

### Goal

You’re given an undirected graph with `V` vertices (0…V-1) and a list of `edges` where each edge is `[u, v]`.
Return the **adjacency list**: for every vertex `i`, a list of all vertices directly connected to `i`.

### Why it’s simple

* For an **undirected** edge `[u, v]`, add `v` to `u`’s list **and** `u` to `v`’s list.
* Many platforms expect each neighbor list **sorted** ascending to have a deterministic output.

### Dry run (Example 1)

```
V = 5
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
Init adj = [[], [], [], [], []]

Process edges:
[0,1] -> adj[0]=[1], adj[1]=[0]
[0,4] -> adj[0]=[1,4], adj[4]=[0]
[4,1] -> adj[4]=[0,1], adj[1]=[0,4]
[4,3] -> adj[4]=[0,1,3], adj[3]=[4]
[1,3] -> adj[1]=[0,4,3], adj[3]=[4,1]
[1,2] -> adj[1]=[0,4,3,2], adj[2]=[1]
[3,2] -> adj[3]=[4,1,2], adj[2]=[1,3]

Sort each list:
adj[0] -> [1,4]
adj[1] -> [0,2,3,4]
adj[2] -> [1,3]
adj[3] -> [1,2,4]
adj[4] -> [0,1,3]

Result:
[[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
```

---

## 3) Optimized codes (expected in interviews)

Both are already linear in input size; the only extra cost can be optional sorting of neighbors.

### A) Clean & optimal (list-of-lists + final per-row sort) — recommended

```python
from typing import List

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Build adjacency list for an undirected graph.
        - Initialize V empty lists: O(V)
        - For each edge (u,v), append both ways: O(E)
        - Sort every neighbor list for deterministic output: sum O(deg(i) log deg(i))
          which overall is O(E log(max_deg)) in worst case.
        
        Time   : O(V + E + sum log(deg(i)))  ~ O(V + E log E) worst-case dense sort
        Space  : O(V + E) for adjacency storage
        """
        adj = [[] for _ in range(V)]          # O(V)

        for u, v in edges:                    # O(E)
            adj[u].append(v)
            adj[v].append(u)

        for i in range(V):                    # total O(E log deg(i)) over all i
            adj[i].sort()

        return adj
```

### B) “Brute/naïve” variant (with duplicate checks & no sort) — to contrast

This version shows what **not** to do in production: it linearly checks for duplicates on every insert (unnecessary unless the input could contain parallel edges and you were required to deduplicate), and it **doesn’t** sort (so output order depends on input order).

```python
from typing import List

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Naïve/demonstrative variant:
        - Checks membership before appending (O(deg) per insertion) => slower.
        - Doesn't sort neighbor lists -> order depends on edges input order.
        
        Time   : O(V + sum over edges of (deg(u) + deg(v)))  -> can degrade to O(V + E^2)
        Space  : O(V + E)
        """
        adj = [[] for _ in range(V)]  # O(V)

        for u, v in edges:            # potentially much slower than linear
            if v not in adj[u]:
                adj[u].append(v)
            if u not in adj[v]:
                adj[v].append(u)

        # no sorting — may fail platforms expecting sorted adjacency lists
        return adj
```

> In interviews, write **A**. If asked about deterministic output or matching samples, mention **sorting neighbors**.

---

## 4) Interviewer Q&A (high-yield)

**Q1. What’s the complexity to build the adjacency list?**

* Initializing: **O(V)**
* Adding edges: **O(E)**
* Optional sorting neighbors: sum over all vertices of **O(deg(i) log deg(i))**, which is ≤ **O(E log E)** worst-case.
* **Space:** **O(V + E)**

**Q2. Why do we sort each neighbor list?**
To produce a **deterministic** adjacency list that matches the sample (and many judges). It’s not required algorithmically.

**Q3. How would you handle parallel edges or self-loops?**

* If duplicates must be removed, use a **set** per vertex while building, then convert to list and sort (space ↑).
* If self-loops are allowed and should appear, add `u` into `adj[u]` once per loop.

**Q4. What changes for a **directed** graph?**
Only add `v` to `adj[u]` (do **not** add the reverse).

**Q5. What if V is large (up to 1e5) and E is large (up to 1e5)?**
The list-of-lists approach remains **memory-efficient** and **linear-time** (plus sorting if needed). Avoid per-edge membership checks (`in` on list) which can make it quadratic.

**Q6. How to store weights if edges are weighted?**
Store pairs/tuples `(neighbor, weight)` instead of just neighbor IDs. Sorting would use the `neighbor` key as needed.

---

---

here’s a **runnable, interview-style full program** for **Print Adjacency List** that:

* implements the exact signature you asked for,
* prints results for the two examples,
* and uses **timeit** to report an average runtime per call.

I’ve added **inline comments** that explain **time & space complexity** at each step.

---

## 5) Full Python program (with inline complexity notes + timings)

```python
"""
Print Adjacency List — Full Demo with Timing
--------------------------------------------
Given V (0..V-1) and undirected edges, return an adjacency list.

We implement:
  Solution.printGraph(V, edges) -> List[List[int]]

Complexities:
  - Build:  O(V + E) time, O(V + E) space
  - Sort:   sum_i O(deg(i) log deg(i))  (≤ O(E log E) worst case dense)
"""

from typing import List
import timeit


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Build adjacency list for an undirected graph.

        Steps & Costs:
        1) Allocate V empty lists: O(V) time/space
        2) For each edge (u, v): append both directions -> O(E) overall
        3) Sort each list for deterministic output:
           total cost = sum over vertices of O(deg(i) log deg(i))
           worst-case ≤ O(E log E)

        Overall:
          Time  : O(V + E + sum log deg)  (often written O(V + E) if you
                  don't require sorting)
          Space : O(V + E)
        """
        # 1) init adjacency lists — O(V)
        adj = [[] for _ in range(V)]

        # 2) add edges both ways — O(E)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 3) sort neighbor lists — Σ O(deg(i) log deg(i))
        for i in range(V):
            adj[i].sort()

        return adj


# ------------------------------ helper: pretty print ------------------------------ #
def show_adj(adj: List[List[int]]) -> None:
    print("[")
    for row in adj:
        print(" ", row)
    print("]")


# ------------------------------------- timing ------------------------------------- #
def bench(func, *args, number=5000) -> float:
    """
    Return avg seconds/run via timeit.
    Note: for tiny inputs, Python overhead dominates; treat as relative signal.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ------------------------------------- driver ------------------------------------- #
if __name__ == "__main__":
    print("=== Print Adjacency List — demo & timings ===\n")

    S = Solution()

    # Example 1 (from prompt)
    V1 = 5
    edges1 = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
    print(">>> Example 1")
    print("V =", V1, "edges =", edges1)
    adj1 = S.printGraph(V1, edges1)
    print("Output adjacency list:")
    show_adj(adj1)
    # Expected: [[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
    print()

    # Example 2 (from prompt)
    V2 = 4
    edges2 = [[0,3], [0,2], [2,1]]
    print(">>> Example 2")
    print("V =", V2, "edges =", edges2)
    adj2 = S.printGraph(V2, edges2)
    print("Output adjacency list:")
    show_adj(adj2)
    # Expected: [[2,3], [2], [0,1], [0]]
    print()

    # --------------- micro-benchmark on moderate size graph ----------------
    print("=== Timings (average seconds per call) ===")
    # Build a moderate random-like graph deterministically
    V3 = 10_000
    edges3 = []
    # Create a line (V3-1 edges)
    for i in range(V3 - 1):
        edges3.append([i, i + 1])
    # Add a few extra connections (sparse)
    step = 97
    j = 0
    for _ in range(20_000):  # total edges ≈ 30k
        u = j % V3
        v = (j + step) % V3
        edges3.append([u, v])
        j += 137

    runs_small = 100
    avg = bench(Solution().printGraph, V3, edges3, number=runs_small)
    print(f"V={V3}, E≈{len(edges3)}  runs={runs_small}:  {avg:.6f} s/call")

    print("\nNotes:")
    print(" • Build phase is linear in V+E; sorting neighbors adds Σ O(deg log deg).")
    print(" • Space usage is O(V+E) for adjacency storage.")
```

### What you’ll see

* Example 1 prints the adjacency list:

  ```
  [
   [1, 4]
   [0, 2, 3, 4]
   [1, 3]
   [1, 2, 4]
   [0, 1, 3]
  ]
  ```
* Example 2 prints:

  ```
  [
   [2, 3]
   [2]
   [0, 1]
   [0]
  ]
  ```
* A timing line like:

  ```
  V=10000, E≈30000  runs=100:  0.00xyz s/call
  ```

  (Numbers vary by machine/Python version.)

---

## 6) Real-World Use Cases (the important ones)

1. **Graph algorithms pre-processing**
   Most algorithms (BFS/DFS, Dijkstra, Kruskal/Prim on adjacency, connected components) require the graph in **adjacency list** form for linear-time iteration over neighbors.

2. **Sparse network modeling**
   Social networks, road maps, routing tables, dependency graphs are typically **sparse**; adjacency lists minimize memory (`O(V+E)`) and optimize neighbor traversal.

3. **Input normalization & reproducibility**
   Many systems read edges as pairs and then **normalize** into sorted adjacency lists to ensure **deterministic outputs** (important for testing, caching, and diffing results).