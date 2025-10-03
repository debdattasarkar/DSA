Got it ✅
Here’s the **README conversion** of the problem statement you uploaded, with **all details preserved** and formatted cleanly in Markdown:

---

# Circle of Strings

**Difficulty:** Hard
**Accuracy:** 15.56%
**Submissions:** 93K+
**Points:** 8
**Average Time:** 28m

---

## Problem Statement

Given an array `arr` of lowercase strings, determine if the strings can be chained together to form a circle.

A string `X` can be chained together with another string `Y` if the **last character of `X` is the same as the first character of `Y`**.

If every string of the array can be chained with exactly two strings of the array (one with the first character and the second with the last character of the string), it will form a circle.

---

## Example

For example, for the array `arr[] = ["for", "geek", "rig", "kaf"]` the answer will be **Yes** as the given strings can be chained as:

```
"for" → "rig" → "geek" → "kaf" → "for"
```

---

## Examples

### Example 1

**Input:**

```
arr[] = ["abc", "bcd", "cdf"]
```

**Output:**

```
0
```

**Explanation:**
These strings can’t form a circle because no string has `'d'` at the starting index.

---

### Example 2

**Input:**

```
arr[] = ["ab", "bc", "cd", "da"]
```

**Output:**

```
1
```

**Explanation:**
These strings can form a circle of strings:

```
"ab" → "bc" → "cd" → "da" → "ab"
```

---

## Expected Complexity

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Constraints

* `1 ≤ length of strings ≤ 20`

---

## Company Tags

* Flipkart
* Accolite
* Microsoft
* FactSet

---

## Topic Tags

* Strings
* Graph
* Data Structures

---

## Related Interview Experiences

* Accolite Interview Experience Set 4 On Campus
* Flipkart Internship Interview On Campus

---

## Related Articles

* [Find Array Strings Can Chained Form Circle Set 2]
* [Given Array Strings Find Strings Can Chained Form Circle]

---

---

awesome — let’s make this interview-ready: clean intuition + a concrete dry run, then multiple Python solutions (optimal graph check, DSU+degree variant, and a brute-force backtracking), all in your requested signature. I’ll wrap with high-yield interviewer Q&A.

---

# 2) Intuition & Step-by-Step Dry Run

## Problem recap

You’re given strings over lowercase letters. You can chain `X → Y` iff `last(X) == first(Y)`.
We must decide if **all** strings can be arranged into a **single circle** (each string used exactly once, head-to-tail, last connects back to the first).

## Key idea (what interviewers expect)

Model this as a **directed multigraph** on the 26 letters:

* Each string `s` adds a **directed edge** from `u = first(s)` to `v = last(s)`.
* Using every string **exactly once** in a circle is exactly an **Eulerian cycle** in this directed graph (a cycle that uses **every edge once**).

For a directed graph to have an Eulerian cycle:

1. **Balanced degrees:** for every vertex, `in_degree[v] == out_degree[v]`.
2. **Strong connectivity on the active subgraph:** if you start from any vertex that has at least one edge, you can reach all other active vertices **and** they can reach back (i.e., the directed graph restricted to vertices with nonzero degree is **strongly connected**).

> We can check strong connectivity by doing one DFS/BFS on the original graph and one on the **reversed graph** (Kosaraju idea), both starting from any vertex with nonzero outdegree.

If both conditions hold → return `1` (Yes), else `0`.

---

## Dry run

`arr = ["ab", "bc", "cd", "da"]`

Build graph (letters as nodes):

* "ab": a → b
* "bc": b → c
* "cd": c → d
* "da": d → a

Degree check:

* a: out=1 (ab), in=1 (da)
* b: out=1, in=1
* c: out=1, in=1
* d: out=1, in=1

All balanced ✅

Connectivity:

* From `a`, follow edges: `a→b→c→d→a` visits all active vertices ✅
* Reverse edges form `a←b←c←d←a`; from `a` you can reach all again ✅

Hence Eulerian cycle exists ⇒ **answer = 1**.

Counterexample: `["abc","bcd","cdf"]`

* edges: a→c, b→d, c→f
* degrees not balanced (e.g., a: out=1,in=0; f: out=0,in=1) ⇒ **0**.

---

# 3) Python solutions (interview-ready)

Return `1` for “Yes” and `0` for “No”.

### A) Optimal: Eulerian cycle via indegree==outdegree + strong connectivity (Kosaraju-style)

```python
# User function Template for python3

class Solution:
    def isCircle(self, arr):
        """
        Graph view:
          - Vertices: 26 letters [0..25] for 'a'..'z'
          - Each string s adds a directed edge u->v where u=s[0], v=s[-1]
        Condition for circle of ALL strings = Eulerian cycle over all edges:
          1) In-degree[v] == Out-degree[v] for all vertices
          2) All vertices with nonzero degree lie in one strongly-connected component
             (on the directed graph)

        Time  : O(V + E) = O(26 + n) ~ O(n)
        Space : O(V + E) = O(26 + n) ~ O(n)
        """
        if not arr:
            return 0

        V = 26
        adj = [[] for _ in range(V)]
        rev = [[] for _ in range(V)]
        indeg = [0] * V
        outdeg = [0] * V
        active = [False] * V   # vertex appears in any edge

        def idx(ch): return ord(ch) - 97  # 'a' -> 0

        # Build graph ------------------------------------------------ O(n)
        for s in arr:
            u = idx(s[0])
            v = idx(s[-1])
            adj[u].append(v)
            rev[v].append(u)
            outdeg[u] += 1
            indeg[v] += 1
            active[u] = active[v] = True

        # 1) Balanced degrees ---------------------------------------- O(V)
        for v in range(V):
            if indeg[v] != outdeg[v]:
                return 0

        # Find a start vertex that has edges
        start = -1
        for v in range(V):
            if outdeg[v] > 0:
                start = v
                break
        if start == -1:
            # No edges at all (all strings length>=1 per constraints, but just in case)
            return 0

        # 2) Strong connectivity: DFS on adj and on rev --------------- O(V+E)
        def dfs(graph, s, seen):
            stack = [s]
            seen[s] = True
            while stack:
                u = stack.pop()
                for w in graph[u]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)

        seen1 = [False] * V
        dfs(adj, start, seen1)
        for v in range(V):
            if active[v] and not seen1[v]:
                return 0

        seen2 = [False] * V
        dfs(rev, start, seen2)
        for v in range(V):
            if active[v] and not seen2[v]:
                return 0

        return 1
```

---

### B) DSU (Union-Find) + degree balancing (popular alternative)

This relies on the theorem that for a directed Eulerian **cycle**, it suffices to have:

* `in==out` for every active vertex, and
* all active vertices lie in a **single connected component of the underlying undirected graph** (i.e., if you ignore directions).

```python
class Solution:
    def isCircle(self, arr):
        """
        Union-Find on the *undirected* version to ensure all active letters connect,
        plus in-degree == out-degree everywhere.

        Time  : O(n * α(26)) ~ O(n)
        Space : O(26)
        """
        if not arr:
            return 0

        V = 26
        parent = list(range(V))
        rank = [0] * V
        indeg = [0] * V
        outdeg = [0] * V
        active = [False] * V

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        def idx(c): return ord(c) - 97

        # Build degrees & undirected connectivity --------------------- O(n)
        for s in arr:
            u, v = idx(s[0]), idx(s[-1])
            outdeg[u] += 1
            indeg[v] += 1
            active[u] = active[v] = True
            union(u, v)  # undirected link

        # Degree balance check ---------------------------------------- O(V)
        for v in range(V):
            if indeg[v] != outdeg[v]:
                return 0

        # Single connected component among active nodes --------------- O(V)
        root = -1
        for v in range(V):
            if active[v]:
                if root == -1:
                    root = find(v)
                elif find(v) != root:
                    return 0

        return 1
```

> Many platforms accept the DSU + balance approach; it’s simple and fast.

---

### C) Brute force (backtracking permutations) — educational only

Try to arrange all strings into a Hamiltonian **cycle** (match `last(i) == first(i+1)` and last to first).
This is **O(n! · n)** — only for tiny `n` (or to prove correctness).

```python
class Solution:
    def isCircle(self, arr):
        """
        Brute backtracking: try to order all strings into a cycle.
        Time : O(n! * n) worst case  (impractical for big n)
        Space: O(n) recursion + O(n) used flags
        """
        n = len(arr)
        if n == 0:
            return 0

        first = arr[0][0]

        used = [False] * n
        used[0] = True
        path = [0]  # store indices

        def backtrack(last_char):
            if len(path) == n:
                # close the cycle
                return arr[path[-1]][-1] == first
            for i in range(1, n):  # we fixed index 0 to break symmetry
                if not used[i] and arr[i][0] == last_char:
                    used[i] = True
                    path.append(i)
                    if backtrack(arr[i][-1]):
                        return True
                    path.pop()
                    used[i] = False
            return False

        ok = backtrack(arr[0][-1])
        return 1 if ok else 0
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why is this an Eulerian cycle problem and not Hamiltonian?**
We must use **each string exactly once**; modeling each string as an **edge** (first→last) means we need a cycle that uses **all edges once** ⇒ **Eulerian** cycle. Hamiltonian would require visiting each **vertex** exactly once, which is different and generally NP-hard.

**Q2. What exact conditions guarantee an Eulerian cycle in a directed graph?**
(i) `in_degree[v] == out_degree[v]` for every vertex, and
(ii) all vertices with nonzero degree belong to **one strongly connected component** (in directed sense).
(Practical check: DFS/BFS on graph and on its reverse starting from any active vertex.)

**Q3. Why can we check connectivity on the undirected version (DSU approach)?**
For Eulerian cycles, with balanced degrees, strong connectivity of the directed graph reduces to connectivity of the **underlying undirected** graph among active vertices. This is a classic characterization and yields a simpler check.

**Q4. Time/space complexity of your optimal solution?**
`O(n + 26)` time (build graph + 2 DFS runs), `O(n + 26)` space. With constants, it’s effectively `O(n)`.

**Q5. Edge cases?**

* Single string `"aa"` → yes (a→a).
* Multiple edges between same pair (e.g., `"ab","ab","ba","ba"`) → still fine.
* A letter appears but only as start or only as end → degree mismatch ⇒ no.
* Empty array → no (per typical problem expectations).

**Q6. Why do you start DFS from a node with nonzero outdegree?**
We only care about vertices participating in the edge set (active); starting at an isolated vertex would incorrectly fail connectivity.

**Q7. Can we do it without building reverse adjacency?**
You need the reverse graph (or Kosaraju/Tarjan SCC) to ensure **strong connectivity** in directed sense. DSU shortcut avoids it by using undirected connectivity with degree balance.

**Q8. How would you return the actual circle order?**
Run **Hierholzer’s algorithm** to construct an **Eulerian circuit** in `O(E)` after the two conditions pass.

---

---

awesome — here’s a **runnable, interview-style full program** for **Circle of Strings** with:

* your required signature `class Solution.isCircle(self, arr)`,
* detailed inline **time/space complexity** notes at each step,
* a small **driver** that prints **inputs & outputs**,
* and **timeit** micro-benchmarks comparing two linear-time solutions:

  * **Graph (Eulerian cycle + strong connectivity)**
  * **DSU (undirected connectivity + degree balance)**

I’ve also added a few crisp **real-world use cases** at the end.

---

## 5) Full Python Program (with inline complexity comments + timings)

```python
"""
Circle of Strings
-----------------
Given an array of lowercase strings, determine if all strings can be arranged to form
one cycle such that last char of s[i] == first char of s[i+1] and last connects to first.

Core modeling:
- Build a directed multigraph on 26 letters a..z
- Each string s contributes a directed edge u->v where u=s[0], v=s[-1]
- Using each string exactly once in a single circle == an Eulerian cycle over all edges.

Eulerian cycle conditions (directed):
  1) in_degree[v] == out_degree[v] for all v
  2) all vertices with nonzero degree belong to one strongly connected component
     (i.e., strongly connected in the directed sense)

We implement:
  A) Graph approach: degree balance + strong connectivity via DFS on graph and on reverse
     Time  : O(V + E) ~ O(n) because V=26, E=len(arr)
     Space : O(V + E) ~ O(n)
  B) DSU approach: degree balance + connected in the underlying UNdirected graph
     (valid characterization for Eulerian cycle)
     Time  : O(n * α(26)) ~ O(n)  |  Space: O(26)

We also include a tiny benchmark using timeit to compare both.

NOTE: We return 1 for "Yes" and 0 for "No", per the common judge format.
"""

import timeit
from typing import List


# --------------------------- Approach A: Graph (Eulerian cycle check) --------------------------- #
class Solution:
    def isCircle(self, arr: List[str]) -> int:
        """
        Time  : O(V + E) ~ O(n)
        Space : O(V + E) ~ O(n)
        where V=26 (letters), E=len(arr)
        """
        if not arr:
            return 0

        V = 26
        adj = [[] for _ in range(V)]     # directed adjacency
        rev = [[] for _ in range(V)]     # reverse directed adjacency
        indeg = [0] * V
        outdeg = [0] * V
        active = [False] * V             # vertex participates in any edge

        def idx(ch: str) -> int:
            return ord(ch) - 97  # 'a' -> 0

        # Build graph: O(E)
        for s in arr:
            u = idx(s[0])
            v = idx(s[-1])
            adj[u].append(v)
            rev[v].append(u)
            outdeg[u] += 1
            indeg[v] += 1
            active[u] = active[v] = True

        # 1) Degree balance: O(V)
        for v in range(V):
            if indeg[v] != outdeg[v]:
                return 0

        # Find a start vertex that has edges: O(V)
        start = -1
        for v in range(V):
            if outdeg[v] > 0:
                start = v
                break
        if start == -1:
            # no edges (shouldn't happen with non-empty arr of non-empty strings)
            return 0

        # 2) Strong connectivity check using DFS on graph and reverse: O(V+E)
        def dfs(graph, s, seen):
            stack = [s]
            seen[s] = True
            while stack:
                u = stack.pop()
                for w in graph[u]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)

        seen = [False] * V
        dfs(adj, start, seen)
        for v in range(V):
            if active[v] and not seen[v]:
                return 0

        seen_rev = [False] * V
        dfs(rev, start, seen_rev)
        for v in range(V):
            if active[v] and not seen_rev[v]:
                return 0

        return 1


# --------------------------- Approach B: DSU + degree balance (undirected) --------------------------- #
class SolutionDSU:
    def isCircle(self, arr: List[str]) -> int:
        """
        Time  : O(n * α(26)) ~ O(n)
        Space : O(26)
        """
        if not arr:
            return 0

        V = 26
        parent = list(range(V))
        rank = [0] * V
        indeg = [0] * V
        outdeg = [0] * V
        active = [False] * V

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        def idx(c: str) -> int:
            return ord(c) - 97

        # Build degree counts + undirected connectivity: O(n)
        for s in arr:
            u, v = idx(s[0]), idx(s[-1])
            outdeg[u] += 1
            indeg[v] += 1
            active[u] = active[v] = True
            union(u, v)  # undirected join

        # Degree balance: O(V)
        for v in range(V):
            if indeg[v] != outdeg[v]:
                return 0

        # Single connected component among active vertices: O(V)
        root = -1
        for v in range(V):
            if active[v]:
                r = find(v)
                if root == -1:
                    root = r
                elif r != root:
                    return 0

        return 1


# -------------------------------------- Tiny benchmark helper -------------------------------------- #
def bench(func, *args, number=30000):
    """
    Average seconds/run using timeit.
    For tiny inputs, Python overhead dominates; treat results as relative.
    """
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


# ---------------------------------------------- Demo ---------------------------------------------- #
if __name__ == "__main__":
    print("=== Circle of Strings — Eulerian Cycle Check ===\n")

    tests = [
        (["abc", "bcd", "cdf"], 0, "No circle — degree mismatch"),
        (["ab", "bc", "cd", "da"], 1, "Yes — a→b→c→d→a"),
        (["aa"], 1, "Single loop on 'a'"),
        (["ab","ba","ab","ba"], 1, "Multiple parallel edges still fine"),
        (["ab","bc","ca","ad"], 0, "Disconnected / degree issue"),
        (["for", "geek", "rig", "kaf"], 1, "Example in prompt"),
    ]

    A = Solution()
    B = SolutionDSU()

    for arr, expected, note in tests:
        outA = A.isCircle(arr)
        outB = B.isCircle(arr)
        print(f"Input: {arr}\nNote: {note}")
        print(f"Graph  approach: {outA}")
        print(f"DSU    approach: {outB}")
        print(f"Expected (if provided): {expected}")
        print(f"Both agree? {outA == outB}\n{'-'*60}\n")

    # ------------------------------ Timings ------------------------------ #
    print("=== Timings (average seconds per run) ===")
    small = ["ab","bc","cd","da"]
    medium = ["ab","bc","cd","de","ef","fg","gh","ha"] * 3  # 24 edges
    large = ["ab","bc","ca","ad","de","ea","af","fg","ga","ah","hi","ia"] * 5  # 60 edges

    runs_small = 80000
    runs_medium = 20000
    runs_large = 8000

    tA_s = bench(Solution().isCircle, small, number=runs_small)
    tB_s = bench(SolutionDSU().isCircle, small, number=runs_small)
    print(f"Small   ({len(small)} strings)  runs={runs_small}: Graph {tA_s:.8e}s | DSU {tB_s:.8e}s")

    tA_m = bench(Solution().isCircle, medium, number=runs_medium)
    tB_m = bench(SolutionDSU().isCircle, medium, number=runs_medium)
    print(f"Medium  ({len(medium)} strings) runs={runs_medium}: Graph {tA_m:.8e}s | DSU {tB_m:.8e}s")

    tA_l = bench(Solution().isCircle, large, number=runs_large)
    tB_l = bench(SolutionDSU().isCircle, large, number=runs_large)
    print(f"Large   ({len(large)} strings)  runs={runs_large}: Graph {tA_l:.8e}s | DSU {tB_l:.8e}s")

    print("\nNote: timings vary by machine and Python version.")
```

---

## 6) Real-World Use Cases (the important ones)

1. **Task/Workflow chaining by input/output “types”**
   Each step produces an artifact type (last char) and requires an input type (first char). An Eulerian cycle ensures a closed loop that uses **every step exactly once**.

2. **DNA fragment assembly toy model**
   Model fragments by their start/end nucleotides (or k-mers). A circular genome formation corresponds to an Eulerian cycle over fragment edges.

3. **Pipeline scheduling / data integration**
   When jobs are described by (source_system → target_system), a full cycle using every job once is equivalent to an Eulerian tour feasibility check.

4. **Word games / puzzles**
   “Make a circle of words by last→first letter” is exactly this problem; checking feasibility is instant via the graph criteria.
