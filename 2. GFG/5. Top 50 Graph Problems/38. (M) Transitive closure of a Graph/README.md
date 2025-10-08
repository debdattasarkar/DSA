# Transitive closure of a Graph

**Difficulty:** Medium
**Accuracy:** 29.1%
**Submissions:** 52K+
**Points:** 4
**Average Time:** 20m

---

Given a **directed graph**, determine whether a vertex **j** is reachable from another vertex **i** for **all** vertex pairs **(i, j)** in the given **graph**.
Here, vertex **j** is reachable from vertex **i** means that **there is a path from i to j**.
The **reachability matrix** is called the **transitive closure of a graph**.

The directed graph is represented by an **adjacency matrix** where there are **N** vertices.

---

## Example 1

**Input:**

```
N = 4
graph = {
  {1, 1, 0, 1},
  {0, 1, 1, 0},
  {0, 0, 1, 1},
  {0, 0, 0, 1}
}
```

**Output:**

```
{
  {1, 1, 1, 1},
  {0, 1, 1, 1},
  {0, 0, 1, 1},
  {0, 0, 0, 1}
}
```

**Explanation:**
The output list shows the **reachable** indexes (the transitive closure).

---

## Example 2

**Input:**

```
N = 3
graph = {
  {1, 0, 0},
  {0, 1, 0},
  {0, 0, 1}
}
```

**Output:**

```
{
  {1, 0, 0},
  {0, 1, 0},
  {0, 0, 1}
}
```

**Explanation:**
The output list shows the reachable indexes.

---

## Your Task

You do not need to read input or print anything. Your task is to complete the function **`transitiveClosure()`** which takes an integer **N** and a 2D array **`graph`** (adjacency matrix of the graph) as **input parameters** and **returns the transitive closure** of the graph in the form of a **2D array**.

---

## Expected Complexities

* **Time Complexity:** `O(N^3)`
* **Auxiliary Space:** `O(N^2)`

---

## Constraints

```
1 ≤ N ≤ 100
```

---

## Topic Tags

Graph, Data Structures

---

## Related Articles

* [Transitive Closure Of A Graph](https://www.geeksforgeeks.org/transitive-closure-of-a-graph/)

---

---

here’s a crisp, interview-oriented guide for **Transitive Closure of a Directed Graph**.

---

## 2) Intuition + step-by-step dry run

### Goal

Given an **adjacency matrix** `graph` (0/1), build an `N×N` matrix `reach` where
`reach[i][j] == 1` iff there exists **a path** (length ≥ 0) from `i` to `j`.

* A vertex is always reachable from itself through a path of length 0 ⇒ set diagonal to 1.

### Classic approach — Warshall’s algorithm (the boolean version of Floyd–Warshall)

For every **intermediate** vertex `k`, allow paths that go *through* `k`:

```
reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
```

Order of loops (k outermost) guarantees we only use intermediates from `{0..k}` when updating.

* **Time:** O(N³)
* **Space:** O(N²)

### Dry run (Example 1)

Input:

```
N = 4
graph =
1 1 0 1
0 1 1 0
0 0 1 1
0 0 0 1
```

Initialize `reach = graph` and ensure `reach[i][i] = 1` (already true here).

Process `k = 0`:

* For `(i,j)`, if `reach[i][0] and reach[0][j]` then set `reach[i][j]=1`.
* Row 0 already has [1 1 0 1].
* Row 1 has `reach[1][0]=0` → nothing via 0.
* Rows 2,3 also have `reach[*][0]=0` → nothing via 0.

Process `k = 1`:

* Now `reach[*][1]` may open new paths.
* Row 0: `reach[0][1]=1`; combine row 0 with row 1: row 1 is [0 1 1 0], so row 0 gains reach to node 2 → row 0 becomes [1 1 1 1].
* Others unchanged yet.

Process `k = 2`:

* Row 1: `reach[1][2]=1`; row 2 is [0 0 1 1]; row 1 gains reach to 3 → row 1 becomes [0 1 1 1].
* Row 0 already reaches everyone.

Process `k = 3`:

* Row 2: `reach[2][3]=1`; row 3 is [0 0 0 1]; nothing new (3 has no outgoing except itself).
  Final:

```
1 1 1 1
0 1 1 1
0 0 1 1
0 0 0 1
```

Matches the expected closure.

---

## 3) Python solutions (interview-ready)

All solutions match the requested signature:

```python
#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
```

### A) Warshall’s Algorithm (boolean Floyd–Warshall) — **Recommended**

```python
class Solution:
    def transitiveClosure(self, N, graph):
        """
        Warshall's algorithm (boolean Floyd–Warshall).
        reach[i][j] |= reach[i][k] & reach[k][j] for all i,j, for k=0..N-1

        Time  : O(N^3)
        Space : O(N^2) (we store/return the closure)
        """
        # Copy to avoid mutating the caller's matrix (if needed)
        reach = [row[:] for row in graph]

        # Ensure self reachability (path of length 0)
        for i in range(N):
            reach[i][i] = 1

        # k must be the OUTERMOST loop
        for k in range(N):
            for i in range(N):
                if reach[i][k]:                # small prune (common trick)
                    rik = 1
                    row_k = reach[k]
                    row_i = reach[i]
                    for j in range(N):
                        # bottom line: reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
                        if row_k[j]:
                            row_i[j] = 1
        return reach
```

**Notes for interviews**

* Mention the diagonal initialization.
* The `if reach[i][k]` prune avoids `N` multiplications when no path `i→k` exists.
* You can write it in pure boolean math (`|=` & `&`) but the integer `0/1` logic is fine.

---

### B) BFS/DFS from each source — also common

* For each node `s`, do a BFS/DFS and mark all reachable `v`.
* **Time:** O(N·(N+E)). With an adjacency **matrix**, `E` can be O(N²) ⇒ still **O(N³)** worst-case.
* **Space:** O(N²) for the result + O(N) for visited.

```python
from collections import deque

class Solution:
    def transitiveClosure(self, N, graph):
        """
        Run BFS from each source s using the adjacency matrix.
        Time  : O(N^3) in worst case with dense adjacency matrix
        Space : O(N^2)
        """
        reach = [[0]*N for _ in range(N)]
        for s in range(N):
            # self reachable
            reach[s][s] = 1
            # BFS
            q = deque([s])
            visited = [0]*N
            visited[s] = 1
            while q:
                u = q.popleft()
                # Scan neighbors via matrix row u
                row = graph[u]
                for v in range(N):
                    if row[v] and not visited[v]:
                        visited[v] = 1
                        reach[s][v] = 1
                        q.append(v)
        return reach
```

> If input were an adjacency **list**, this becomes O(N·(N+E)) which is often better than N³ for sparse graphs.

---

### C) Bitset-accelerated Warshall (nice optimization to mention)

Represent each row as a **Python int** bitset; then
`row_i |= (reach[i][k] ? row_k : 0)` in O(N / word_size) per update in practice:

```python
class Solution:
    def transitiveClosure(self, N, graph):
        """
        Bitset version (uses Python big ints).
        Often considerably faster in practice for N≤100 (constraints here).
        Time  : O(N^3 / word_size) in spirit (bitwise ops), but still O(N^3) asymptotically.
        Space : O(N^2) (we return a matrix)
        """
        # Build bitset rows
        rows = []
        for i in range(N):
            bits = 0
            for j in range(N):
                if graph[i][j]:
                    bits |= (1 << j)
            bits |= (1 << i)  # self reachability
            rows.append(bits)

        for k in range(N):
            mask_k = rows[k]
            bit_k = (1 << k)
            for i in range(N):
                if rows[i] & bit_k:       # if i can reach k
                    rows[i] |= mask_k     # then i can reach everything k reaches

        # Convert bitsets back to 0/1 matrix
        ans = [[0]*N for _ in range(N)]
        for i in range(N):
            row = rows[i]
            for j in range(N):
                ans[i][j] = 1 if (row >> j) & 1 else 0
        return ans
```

---

## 4) Interview Q&A (what you’ll likely be asked)

**Q1. Why set the diagonal to 1?**
Because transitive closure includes paths of length **0**; every vertex reaches itself.

**Q2. Difference between Floyd–Warshall and Warshall?**

* **Floyd–Warshall** solves **all-pairs shortest paths** on weighted graphs.
* **Warshall** is the **boolean** specialization for **reachability** (unweighted, just existence).

**Q3. Why must `k` be the outermost loop in Warshall?**
We only allow paths whose intermediates come from the set `{0..k}`. Placing `k` outermost preserves this invariant and yields correctness.

**Q4. Complexity trade-offs vs BFS/DFS from each node?**

* Matrix input + dense graph: both are **O(N³)**.
* If you had an adjacency list and a **sparse** graph, `N` BFS/DFS runs (`O(N·(N+E))`) can be faster.

**Q5. Do self-loops or multiple edges matter?**
No—closure depends only on **existence** of paths. Self-loops are okay (diagonal is set anyway).

**Q6. Can we compute closure on a DAG more efficiently?**
Yes—processing nodes in **topological order** and propagating reachability can be faster than cubic in practice, though coding complexity rises.

**Q7. How to modify for undirected graphs?**
The same approaches work; the input matrix would be symmetric. Closure becomes the connected-component relation (all nodes in the same component mutually reachable).

**Q8. Memory concerns?**
For `N ≤ 100` (as in constraints), `O(N²)` memory is tiny. For larger `N`, prefer bitset compression (like method C) to speed and shrink footprint.

---

---

awesome — here’s a complete, runnable script for **Transitive Closure of a Directed Graph** with:

* the canonical **Warshall** algorithm (boolean Floyd–Warshall) inside the requested `Solution.transitiveClosure`
* tight, line-level comments about **time & space**
* **I/O demo** using the two examples from the prompt + one custom case
* a small **timeit** benchmark that reports average seconds/run

---

## 5) Full program (with inline complexity + inputs/outputs + timing)

```python
"""
Transitive Closure of a Graph (Adjacency Matrix)
------------------------------------------------
We compute reachability for every pair (i, j): reach[i][j] == 1 if a path exists from i to j.

Chosen approach:
  Warshall's algorithm (boolean Floyd–Warshall)
    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j]) for k = 0..N-1

Asymptotics (N = number of vertices):
  Time  : O(N^3)  — triple nested loops over k, i, j
  Space : O(N^2)  — we store and return an N×N reachability matrix
"""

from typing import List
import timeit


# ----------------------------- Core Solution ----------------------------- #
class Solution:
    def transitiveClosure(self, N: int, graph: List[List[int]]) -> List[List[int]]:
        """
        Warshall's algorithm for reachability.

        Parameters
        ----------
        N     : int            number of vertices (0..N-1)
        graph : List[List[int]] adjacency matrix (0/1), graph[i][j] == 1 iff edge i->j exists

        Returns
        -------
        List[List[int]] : N×N reachability matrix (0/1)

        Complexity
        ----------
        Time  : O(N^3) — three nested loops over k, i, j
        Space : O(N^2) — output matrix
        """
        # Copy input (O(N^2) time & space) so we don't mutate caller data
        reach = [row[:] for row in graph]

        # Every node reaches itself by a path of length 0  → diagonal = 1  (O(N))
        for i in range(N):
            reach[i][i] = 1

        # Warshall — k MUST be outermost.
        # For each intermediate k, try to improve reach[i][j] through k.
        # Total updates: N * N * N → O(N^3)
        for k in range(N):
            row_k = reach[k]         # Alias to avoid repeated indexing (micro-optimization)
            for i in range(N):
                if reach[i][k]:      # Small prune: only if i can already reach k (constant check)
                    row_i = reach[i]
                    # If row_k[j] is 1, then i can reach j via k → set row_i[j] = 1
                    for j in range(N):
                        if row_k[j]:
                            row_i[j] = 1
        return reach


# ----------------------------- Demo & Timing ----------------------------- #
def print_matrix(M: List[List[int]]):
    for r in M:
        print(" ", r)


def run_demo_and_benchmark():
    sol = Solution()

    # Example 1 (from prompt)
    N1 = 4
    G1 = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
    ]
    print("Example 1:")
    print("Input adjacency matrix:")
    print_matrix(G1)
    ans1 = sol.transitiveClosure(N1, G1)
    print("\nTransitive closure:")
    print_matrix(ans1)
    print()

    # Example 2 (from prompt)
    N2 = 3
    G2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    print("Example 2:")
    print("Input adjacency matrix:")
    print_matrix(G2)
    ans2 = sol.transitiveClosure(N2, G2)
    print("\nTransitive closure:")
    print_matrix(ans2)
    print()

    # Custom example (adds more reachability)
    N3 = 5
    G3 = [
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
    ]
    print("Custom Example:")
    print("Input adjacency matrix:")
    print_matrix(G3)
    ans3 = sol.transitiveClosure(N3, G3)
    print("\nTransitive closure:")
    print_matrix(ans3)
    print()

    # ---------------------------- Timing ---------------------------- #
    # We benchmark on a moderately dense N=100 graph (worst-case-ish).
    N = 100
    # Build a graph with edges i->i and i->(i+1)%N and i->(i+2)%N to ensure some density.
    base_graph = [[0]*N for _ in range(N)]
    for i in range(N):
        base_graph[i][i] = 1
        base_graph[i][(i + 1) % N] = 1
        base_graph[i][(i + 2) % N] = 1

    def task():
        sol.transitiveClosure(N, base_graph)

    runs = 5
    avg = timeit.timeit(task, number=runs) / runs
    print(f"Benchmark on N={N} (avg over {runs} runs): {avg:.4f} seconds/run")
    print("Asymptotic time is O(N^3); this measures end-to-end cost on a dense-ish graph.")


if __name__ == "__main__":
    run_demo_and_benchmark()
```

### Sample output you’ll see (abridged)

```
Example 1:
Input adjacency matrix:
  [1, 1, 0, 1]
  [0, 1, 1, 0]
  [0, 0, 1, 1]
  [0, 0, 0, 1]

Transitive closure:
  [1, 1, 1, 1]
  [0, 1, 1, 1]
  [0, 0, 1, 1]
  [0, 0, 0, 1]

Example 2:
Input adjacency matrix:
  [1, 0, 0]
  [0, 1, 0]
  [0, 0, 1]

Transitive closure:
  [1, 0, 0]
  [0, 1, 0]
  [0, 0, 1]

Custom Example:
...
Benchmark on N=100 (avg over 5 runs): 0.xxxx seconds/run
Asymptotic time is O(N^3); this measures end-to-end cost on a dense-ish graph.
```

---

## 6) Real-World Use Cases (high-impact)

1. **Database query planning / reachability**
   In dependency graphs (views, stored procedures, ETL DAGs), transitive closure answers “What objects are (indirectly) affected if I change X?”

2. **Package/module dependency analysis**
   Given a directed dependency graph, closure tells you **all transitive dependencies** (what must be installed/loaded) or **reverse dependencies** (what breaks if module X changes).

3. **Access control & trust chains**
   In authorization systems, roles/permissions often form directed graphs. The closure yields **all effective permissions** reachable from a role/user.

4. **Web & social graphs**
   For curated subgraphs (bounded N), closure allows “can A reach B?” queries offline, enabling fast on-device or server-side checks for features like **navigation shortcuts** or **influence propagation**.

5. **Compiler toolchains**
   Build systems and compilers compute transitive includes/imports for **incremental builds** and **dead code elimination**.
