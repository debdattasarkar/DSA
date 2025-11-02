
---

# 🔺 Max DAG Edges

**Difficulty:** Medium
**Accuracy:** 75.07%
**Submissions:** 6K+
**Points:** 4

---

## 📘 Problem Statement

Given a **directed acyclic graph (DAG)** with `V` vertices numbered from `0` to `V-1` and `E` edges, represented as a 2D array `edges[][]`,
where each entry `edges[i] = [u, v]` denotes a **directed edge** from vertex `u` to vertex `v`,
find the **maximum number of additional edges** that can be added to the graph **without forming any cycles**.

---

### 🧩 Note

The resulting graph must **remain a DAG**, meaning that adding any further edge would **create a cycle**.

---

## 🧠 Examples

### Example 1

**Input:**

```
V = 3, E = 2
edges[][] = [[0, 1], [1, 2]]
```

**Output:**

```
1
```

**Explanation:**
The given DAG allows one more edge `0 -> 2`, which keeps the structure acyclic.
Adding anything else would create a cycle.

---

### Example 2

**Input:**

```
V = 4, E = 4
edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
```

**Output:**

```
2
```

**Explanation:**
Two additional edges (`0 -> 3`, `1 -> 3`) can be added without forming cycles.

---

## ⚙️ Constraints

```
1 ≤ V ≤ 10³
0 ≤ E ≤ (V * (V - 1)) / 2
0 ≤ edges[i][0], edges[i][1] < V
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(1)       |
| **Auxiliary Space** | O(1)       |

---

## 🧵 Topic Tags

`Graph` • `topological-sort` • `Mathematical`

---

## 🔗 Related Articles

* [Maximum Edges That Can Be Added to a DAG Without Creating a Cycle](https://www.geeksforgeeks.org/maximum-edges-can-added-dag-remains-dag/)

---

---

Awesome — this one is sneaky-easy once you see the trick. Here’s everything you asked for.

---

## 2) Intuition + step-by-step dry run

### Core fact (burn this in 🔥)

In a DAG you can **topologically order** the vertices.
If you **add an edge only from an earlier index to a later index** in that order, you **can’t** create a cycle.

* For a fixed linear (topo) order of `V` nodes, the **maximum** number of edges that still keeps it acyclic is the number of ordered pairs `(i, j)` with `i < j`, i.e.
  **`V * (V - 1) / 2`**.
* If the current graph already has `E` edges, the **max additional** edges you can add is simply:
  **`V*(V-1)/2 - E`**.

No need to check reachability or compute the actual order — that count is independent of which valid topological order you pick.

### Why this is safe

* Any **backward** edge (later → earlier) breaks the order and **creates a cycle**.
* Any **forward** edge (earlier → later) keeps acyclicity, **even if a path already exists** (it’s just a shortcut).

### Dry run

**Example 1**
`V = 3, edges = [[0,1],[1,2]]` ⇒ `E = 2`
Max possible in any DAG on 3 nodes = `3*2/2 = 3`
Additional = `3 – 2 = 1` → (the missing forward pair is `0→2`). ✅

**Example 2**
`V = 4, edges = [[0,1],[0,2],[1,2],[2,3]]` ⇒ `E = 4`
Max possible = `4*3/2 = 6`
Additional = `6 – 4 = 2` → (e.g., `0→3` and `1→3`). ✅

---

## 3) Python solutions (tiny O(1) + a “topo-count” variant)

Signature you asked for:

```python
class Solution:
    def maxEdgesToAdd(self, V, edges):
        # code here
```

### A) Mathematical O(1) solution (most expected in interviews)

```python
class Solution:
    def maxEdgesToAdd(self, V, edges):
        """
        Max edges in any DAG on V nodes (for some topological order) = V*(V-1)/2.
        Current edges = E = len(edges).
        Answer = V*(V-1)/2 - E.

        Time  : O(1)
        Space : O(1)
        """
        E = len(edges)
        max_possible = V * (V - 1) // 2
        return max_possible - E
```

### B) Topological-order counting (educational, O(V²))

Counts the number of **missing forward pairs** in a specific topological order; matches A’s answer.

```python
from collections import defaultdict, deque

class SolutionTopoCount:
    def maxEdgesToAdd(self, V, edges):
        """
        1) Compute a topological order (Kahn).
        2) Build a set of existing edges.
        3) For all i<j in topo order, if edge (topo[i] -> topo[j]) absent, count it.
        Time  : O(V^2 + V + E)  (V^2 dominates)
        Space : O(V + E)
        """
        # Build graph and indegrees
        g = defaultdict(list)
        indeg = [0] * V
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1

        # Kahn's algorithm to get one topological order
        q = deque([i for i in range(V) if indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for w in g[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)

        # Graph is guaranteed DAG; but if not, return 0 (no definition).
        if len(topo) != V:
            return 0

        # For quick "edge exists?" checks
        has = set((u, v) for u, v in edges)

        # Count missing forward edges in this topo order
        pos = {node: i for i, node in enumerate(topo)}  # not strictly needed
        addable = 0
        for i in range(V):
            u = topo[i]
            for j in range(i+1, V):
                v = topo[j]
                if (u, v) not in has:
                    addable += 1
        return addable
```

> In interviews, give **A)** first. If they want a proof-y or constructive angle, mention **B)** to show you can compute it explicitly by a topo order and count missing forward pairs.

---

## 4) Interview quick recall + Q&A

### 5-line pseudo you can write from memory

```
E = number of edges
max_possible = V*(V-1)/2
return max_possible - E
```

(okay that’s 3 lines… it’s really that simple 😄)

### Mnemonic

**“DAG = Order → Only Forward → Count all pairs → Subtract current.”**
(“Order, Forward, Pairs, Minus E”)

### High-yield Q&A

**Q1. Why is `V*(V-1)/2` the cap?**
Pick any topological order; you can add an edge for **every** pair `(i, j)` with `i<j` (forward). That’s exactly `V choose 2` pairs.

**Q2. Don’t we need to avoid adding an edge where a path already exists?**
No. Adding a **forward** edge in a DAG **never** creates a cycle, even if a path exists (it becomes a shortcut). Only **backward** edges risk cycles.

**Q3. Do we need the actual topological order?**
No, because the **maximum** over all DAGs on `V` nodes is always `V*(V-1)/2`, and your current `E` edges are already acyclic. So **max additional = that cap – E**.

**Q4. What if the input had multi-edges?**
Typically edges are unique. If duplicates existed (rare/invalid for this problem), deduplicate `E` before applying the formula.

**Q5. What about a disconnected DAG?**
Still fine. A topological order exists globally; forward edges across different components are also safe. The formula remains valid.

**Q6. Complexity?**
O(1) time/space for the formula; the educational topo-count is O(V²).

---

---

Great—wrapping up **Max DAG Edges** with (5) crisp real-world uses and a **complete runnable Python program** (both O(1) math solution and a constructive topo-count check), including timings.

---

## 5) Real-World Use Cases (interview-friendly)

1. **Project planning / CI pipelines:**
   Convert a partially ordered set of tasks (DAG). The max extra dependencies you can safely add (without introducing circular blockers) equals `V*(V-1)/2 - E`.

2. **Data/ML DAG orchestrators (Airflow, Dagster):**
   Compute the headroom of dependency constraints you can add across stages without breaking acyclicity.

3. **Package managers / microservices rollout:**
   Ensure additional “depends-on” relations won’t create circular install or deployment requirements.

4. **Curriculum design (courses/prereqs):**
   Given current prerequisite graph, the formula tells how many more prerequisite relations could be added before cycles are inevitable.

5. **Knowledge graphs with causal edges:**
   Estimate the budget of extra causal links you can add while preserving a DAG (no causal loops).

---

## 6) Full Program (O(1) math + constructive topo count) with timings

```python
#!/usr/bin/env python3
"""
Max DAG Edges
-------------
Given a DAG with V nodes and E edges, find the maximum number of additional edges
that can be added while keeping it acyclic.

Key fact:
- For any topological order of V nodes, the maximum number of edges that keeps it a DAG
  is the number of forward pairs: V*(V-1)/2.
  Therefore:
      answer = V*(V-1)//2 - E

We implement:
  1) O(1) mathematical solution (expected in interviews)
  2) Constructive check: compute one topological order and count missing forward edges
     (O(V^2), educational sanity check)

We also:
  * Run sample inputs from the prompt
  * Print outputs
  * Time both approaches (perf_counter + timeit)
"""

from collections import defaultdict, deque
from time import perf_counter
import timeit
from typing import List, Tuple


# ---------------------------------------------------------
# 1) Expected: O(1) mathematical solution
# ---------------------------------------------------------
class Solution:
    def maxEdgesToAdd(self, V: int, edges: List[List[int]]) -> int:
        """
        Max edges in any DAG with V nodes = V*(V-1)/2 (all forward pairs in some topo order).
        Current E = len(edges). Additional edges = cap - E.

        Time  : O(1)
        Space : O(1)
        """
        E = len(edges)
        cap = V * (V - 1) // 2
        return cap - E


# ---------------------------------------------------------
# 2) Constructive: topo order + count missing forward pairs
# ---------------------------------------------------------
class SolutionTopoCount:
    def maxEdgesToAdd(self, V: int, edges: List[List[int]]) -> int:
        """
        Steps:
          1) Build graph and indegrees (O(V + E))
          2) Kahn's algorithm to get one topological order (O(V + E))
          3) Count missing forward edges across that order (O(V^2))
        Total time: O(V^2 + V + E)  -> O(V^2)
        Space     : O(V + E)
        """
        g = defaultdict(list)
        indeg = [0] * V
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1

        # Kahn's algorithm: O(V + E)
        q = deque([i for i in range(V) if indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for w in g[u]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)

        # If not a DAG, the problem statement wouldn’t apply; return 0 safely.
        if len(topo) != V:
            return 0

        existing = set(map(tuple, edges))  # O(E) space
        addable = 0

        # Count all forward pairs missing as edges: O(V^2)
        for i in range(V):
            u = topo[i]
            for j in range(i + 1, V):
                v = topo[j]
                if (u, v) not in existing:
                    addable += 1
        return addable


# ---------------------------------------------------------
# Utilities to run and time cases
# ---------------------------------------------------------
def run_case(title: str, V: int, edges: List[Tuple[int, int]]):
    print(f"\n-- {title} --")
    print("V =", V)
    print("edges =", edges)

    # Single-run timings (micro-benchmark)
    t0 = perf_counter()
    ans_math = Solution().maxEdgesToAdd(V, edges)
    t1 = perf_counter()

    t2 = perf_counter()
    ans_topo = SolutionTopoCount().maxEdgesToAdd(V, edges)
    t3 = perf_counter()

    print(f"O(1) math      : {ans_math}   [single-run {(t1 - t0)*1e6:.2f} µs]")
    print(f"Topo-count     : {ans_topo}   [single-run {(t3 - t2)*1e6:.2f} µs]")
    print("Match?         :", ans_math == ans_topo)

    # Averaged timings (exclude print cost)
    def call_math():
        Solution().maxEdgesToAdd(V, edges)

    def call_topo():
        SolutionTopoCount().maxEdgesToAdd(V, edges)

    reps = 1000
    avg_math = timeit.timeit(call_math, number=reps) / reps
    avg_topo = timeit.timeit(call_topo, number=reps) / reps
    print(f"Avg over {reps} runs: math {avg_math*1e6:.2f} µs/run | topo {avg_topo*1e6:.2f} µs/run")


# ---------------------------------------------------------
# Demo / Main
# ---------------------------------------------------------
def main():
    # Example 1 (from prompt): V=3, E=2 -> cap=3 -> add=1
    V1 = 3
    edges1 = [(0, 1), (1, 2)]
    run_case("Example 1", V1, edges1)

    # Example 2 (from prompt): V=4, E=4 -> cap=6 -> add=2
    V2 = 4
    edges2 = [(0, 1), (0, 2), (1, 2), (2, 3)]
    run_case("Example 2", V2, edges2)

    # Extra: disconnected DAG
    V3 = 5
    edges3 = [(0, 2), (1, 3)]  # two small chains; cap=10, E=2 -> add=8
    run_case("Disconnected DAG", V3, edges3)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==== TOTAL PROGRAM RUNTIME: {(end - start):.6f} s ====")
```

**What you’ll see when you run it**

* For each sample: the **O(1) math** result, the **constructive topo** result, and a **match** check.
* **Single-run** microsecond timings and **averaged** timings via `timeit`.
* Inline comments explain **time/space complexity** right where they matter—interview friendly.

