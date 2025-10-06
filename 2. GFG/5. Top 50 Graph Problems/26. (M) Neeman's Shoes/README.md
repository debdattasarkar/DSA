# Neeman’s Shoes

**Difficulty:** Medium
**Accuracy:** 32.16%
**Submissions:** 41K+
**Points:** 4
**Average Time:** 25m

---

Due to the second wave of Corona virus, Geekland imposed another lockdown and Geek has gained some weight. Now Geek has decided to exercise.

There are **N** intersections in the city numbered from **0 to N-1** and **M** bidirectional roads each road connecting two intersections. All the intersections are connected to each-other through some set of roads, the **iᵗʰ** road connects intersections **A[i][0]** and **A[i][1]** and is of length **A[i][2]**.

Every morning Geek will start at intersection **src** and will run/walk up to intersection **dest**. Geek only has one hour in the morning so he will choose to cover the **shortest path** from **src** to **dest**.

After planning his exercising schedule, Geek wants to buy the perfect shoes to walk/run in the morning. He goes to Neeman’s Shoe factory which is the National Shoe factory of Geekland.

Geek sees that there are two types of shoes **"Neeman's Wool Joggers"** and **"Neeman's Cotton Classics"**,
"Neeman's Wool Joggers" are good for **running** and "Neeman's Cotton Classics" are good for **walking**.

Geek is confused which shoes to buy, so he comes up with a strategy. If the distance he has to cover in the morning is **less than or equal to X**, then he will walk the distance, therefore he will buy **"Neeman's Cotton Classics"**. If the distance is **greater than X**, he will buy **"Neeman's Wool Joggers"**. Geek is too lazy to calculate the shortest distance between two intersections **src** and **dest**. Help him decide which shoes to buy.

---

## Examples

### Example 1

**Input:**

```
N = 3, M = 2, src = 0, dest = 2, X = 5
A[][] = { {0, 1, 3},
          {1, 2, 3} }
```

**Output:**

```
Neeman's Wool Joggers
```

**Explanation:**
Shortest path from **src** to **dest** is **6** which is greater than **X**, hence Geek will buy **"Neeman's Wool Joggers"**.

---

### Example 2

**Input:**

```
N = 3, M = 2, src = 0, dest = 2, X = 6
A[][] = { {0, 1, 3},
          {1, 2, 3} }
```

**Output:**

```
Neeman's Cotton Classics
```

**Explanation:**
Shortest path from **src** to **dest** is **6** which is **not greater than X**, hence Geek will buy **"Neeman's Cotton Classics"**.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`exercise()`** which takes **N, M, A[][], src, dest and X** as input parameters and returns a string representing the shoes he selects. Either **"Neeman's Wool Joggers"** or **"Neeman's Cotton Classics"**.

---

## Expected Complexities

* **Time Complexity:** `O((N + M) * log(M))`
* **Auxiliary Space:** `O(N + M)`

---

## Constraints

```
2 ≤ N ≤ 10^4
1 ≤ M ≤ min((N*(N-1))/2, 2*10^5)
0 ≤ A[i][0], A[i][1] < N
0 ≤ src, dest < N
1 ≤ A[i][2], X ≤ 10^9
```

---

## Topic Tags

* Graph
* Data Structures

---

---

Great problem! You’re asked to decide which shoes to buy by comparing **the shortest distance from `src` to `dest`** against `X`. This is a classic **single-source shortest path** on a **weighted, undirected** graph with **non-negative** weights → **Dijkstra** is the right tool.

---

## 2) Intuition + step-by-step dry run

### Idea

1. Build an adjacency list from `A` (each edge `[u, v, w]` is bidirectional).
2. Run **Dijkstra** from `src` using a min-heap (priority queue) to get the shortest distance to `dest`.
3. Compare `dist[dest]` with `X`:

   * `dist <= X` → `"Neeman's Cotton Classics"` (walk)
   * `dist >  X` → `"Neeman's Wool Joggers"` (run)
   * If `dest` unreachable (dist stays `inf`) → distance is effectively ∞ (> X) → `"Neeman's Wool Joggers"`

### Dry run (Example 1)

```
N=3, M=2, src=0, dest=2, X=5
Edges: (0-1,3), (1-2,3)
Adj:
0: (1,3)
1: (0,3), (2,3)
2: (1,3)

Dijkstra:
dist = [0, inf, inf]
heap = [(0,0)]

pop (0,0):
  relax 0->1 (3): dist[1]=3, push(3,1)

pop (3,1):
  relax 1->0 (3): new 6 ≥ dist[0]=0 -> ignore
  relax 1->2 (3): dist[2]=6, push(6,2)

pop (6,2): reached dest; we can early-exit with dist=6

Compare: 6 > X(5) -> "Neeman's Wool Joggers"
```

Example 2 is the same path length (6) and with `X=6` → `6 ≤ 6` → `"Neeman's Cotton Classics"`.

---

## 3) Optimized Python solutions (interview-ready)

Both keep your required signature:

```python
#User function Template for python3

class Solution:
    def exercise(self, N, M, A, src, dest, X):
        # code here
```

### A) Dijkstra with adjacency list + min-heap (recommended)

```python
import heapq

#User function Template for python3

class Solution:
    def exercise(self, N, M, A, src, dest, X):
        """
        Return which shoes Geek buys based on the shortest path distance
        between src and dest compared to X.

        Graph: undirected, non-negative weights -> Dijkstra
        Time  : O((N + M) log N) using adjacency list + min-heap
        Space : O(N + M) for adjacency + O(N) for dist/heap
        """
        # 1) Build adjacency list: O(N + M)
        adj = [[] for _ in range(N)]
        for u, v, w in A:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # 2) Dijkstra from src: O((N + M) log N)
        INF = 10**20
        dist = [INF] * N
        dist[src] = 0
        # heap entries: (distance_so_far, node)
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                # stale entry; skip (heap optimization)
                continue
            if u == dest:
                # early exit: shortest distance to dest is finalized
                break
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # 3) Decide based on distance
        dmin = dist[dest]
        # If unreachable, dmin stays INF -> definitely > X -> Joggers
        if dmin <= X:
            return "Neeman's Cotton Classics"
        else:
            return "Neeman's Wool Joggers"
```

#### Notes interviewers like

* **Early exit** when `u == dest`: once popped from the heap, its distance is final (Dijkstra invariant).
* **Skip stale heap entries** by checking `d != dist[u]` (classic optimization).
* `O((N+M)logN)` fits constraints up to `N=1e4, M=2e5`.

---

### B) Dijkstra (memory-lean tweak) — store only distances; no parents

Same complexity; shows you can keep it minimal and robust. (Already done above; included to emphasize lean design.) If asked, mention alternatives:

* **0-1 BFS** when edge weights are 0/1 (not our case).
* **Bellman-Ford** if negative edges existed (they don’t here).
* **A*** if you had coordinates and a consistent heuristic (not available here).

---

## 4) Interview Q & A (high-yield)

**Q1. Why Dijkstra and not BFS?**
BFS is only correct for **unweighted** (or uniformly weighted) graphs. We have **general non-negative weights**, so **Dijkstra** is the right choice.

**Q2. What if there were negative weights?**
Dijkstra fails with negative edges. You’d use **Bellman-Ford** (O(N·M)) or **SPFA** (heuristic) — but constraints here would be tight. Fortunately, weights are ≥ 1.

**Q3. Why is “early exit on dest” correct in Dijkstra?**
Once a node is popped from the min-heap, its shortest distance is **final**. If it’s `dest`, no shorter path will appear later.

**Q4. Complexity and memory?**

* **Time:** `O((N+M) log N)` using adjacency list & min-heap (each edge relaxed at most once with a heap push; each node popped at most once effectively).
* **Space:** `O(N+M)` adjacency + `O(N)` distance and heap overhead.

**Q5. How to handle “unreachable dest”?**
Distance remains `INF`. Treat as **> X** → return **"Neeman's Wool Joggers"**.

**Q6. Why not Floyd–Warshall?**
`O(N^3)` is infeasible for `N ≤ 10^4`. Single-pair shortest path with Dijkstra is optimal here.

**Q7. Any practical optimizations?**

* Early exit on `dest`.
* Skip stale entries (`d != dist[u]`).
* Use adjacency lists (not matrices).
* If the graph is very sparse and degrees vary wildly, a **bidirectional Dijkstra** can sometimes help, but standard Dijkstra already meets constraints.

---

---

awesome — here’s a **runnable, interview-style full program** that:

* implements the exact signature `class Solution: def exercise(self, N, M, A, src, dest, X)`
* prints **inputs & outputs** for a few cases (including the two from the prompt)
* uses **`timeit`** to report **average runtime** of the algorithm
* includes **inline comments** calling out **time & space complexity** where it matters

---

## 5) Full Python program (with inline complexity notes + timing)

```python
"""
Neeman's Shoes — Shortest Path vs Threshold
-------------------------------------------
We must choose shoes based on the shortest distance from `src` to `dest`
in a weighted, undirected graph with non-negative weights.

Correct tool: Dijkstra with a min-heap.

Let:
  N = number of intersections (vertices)
  M = number of roads (edges)
  A = list of edges [u, v, w] (bidirectional, weight w >= 1)

Complexities (using adjacency list + binary heap):
  • Build adjacency: Time  O(N + M), Space O(N + M)
  • Dijkstra:        Time  O((N + M) log N)   [each edge relax → heap push; each pop log N]
                     Space O(N) for dist + heap (amortized)
Overall: O((N + M) log N) time, O(N + M) space.
"""

from typing import List, Tuple
import heapq
import timeit


class Solution:
    def exercise(self, N: int, M: int, A: List[List[int]], src: int, dest: int, X: int) -> str:
        """
        Decide shoe type based on shortest distance:
          - If shortest distance <= X  → "Neeman's Cotton Classics"
          - Else                       → "Neeman's Wool Joggers"

        Time  : O((N + M) log N)
        Space : O(N + M)
        """
        # ---- 1) Build adjacency list (undirected) ----
        # Space: O(N + M)
        adj: List[List[Tuple[int, int]]] = [[] for _ in range(N)]
        for u, v, w in A:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # ---- 2) Dijkstra from src ----
        # dist[i] = shortest known distance from src to i
        # Space: O(N)
        INF = 10**20
        dist = [INF] * N
        dist[src] = 0

        # Min-heap of (distance_so_far, node)
        # Space: up to O(N) effective, O(M) pushes through the run
        heap: List[Tuple[int, int]] = [(0, src)]

        # Time: O((N + M) log N) due to heap operations
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                # stale heap entry (we already found a better dist)
                continue
            if u == dest:
                # Early exit is safe in Dijkstra:
                # once popped, d == dist[u] is FINAL shortest distance to u
                break
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        # ---- 3) Decision based on distance ----
        dmin = dist[dest]
        # If unreachable, dmin remains INF → definitely > X → Joggers
        return "Neeman's Cotton Classics" if dmin <= X else "Neeman's Wool Joggers"


# --------------------------- Demo & Benchmark --------------------------- #
def run_demo():
    sol = Solution()

    print("=== Demo Cases ===")

    # Example 1
    N, M, src, dest, X = 3, 2, 0, 2, 5
    A = [[0, 1, 3], [1, 2, 3]]
    print(f"Input: N={N}, M={M}, src={src}, dest={dest}, X={X}, A={A}")
    print("Output:", sol.exercise(N, M, A, src, dest, X))
    print("Explanation: path length 6 > 5 → Joggers\n")

    # Example 2
    N, M, src, dest, X = 3, 2, 0, 2, 6
    A = [[0, 1, 3], [1, 2, 3]]
    print(f"Input: N={N}, M={M}, src={src}, dest={dest}, X={X}, A={A}")
    print("Output:", sol.exercise(N, M, A, src, dest, X))
    print("Explanation: path length 6 ≤ 6 → Cotton Classics\n")

    # An extra: unreachable dest (disconnected graph)
    N, M, src, dest, X = 4, 1, 0, 3, 10
    A = [[0, 1, 5]]  # node 3 is disconnected
    print(f"Input: N={N}, M={M}, src={src}, dest={dest}, X={X}, A={A}")
    print("Output:", sol.exercise(N, M, A, src, dest, X))
    print("Explanation: dest unreachable (∞) > X → Joggers\n")


def benchmark():
    """
    Lightweight timing with timeit.
    Creates a mid-sized sparse graph and measures average seconds/run.
    """
    sol = Solution()

    # Build a reproducible sparse graph: a line + some chords
    N = 10_000
    edges = []
    # Chain edges (N-1)
    for i in range(N - 1):
        edges.append([i, i + 1, 1])
    # Add extra jumps every 250 nodes to create shortcuts
    for i in range(0, N - 50, 250):
        edges.append([i, i + 50, 3])
    M = len(edges)

    src, dest, X = 0, N - 1, 12_000  # long threshold

    # Wrap the call for timeit
    def task():
        return sol.exercise(N, M, edges, src, dest, X)

    runs = 5
    avg = timeit.timeit(task, number=runs) / runs
    print("=== Benchmark ===")
    print(f"Graph: N={N}, M={M}, runs={runs}")
    print(f"Average time: {avg:.4f} s/run")
    print("(Asymptotically O((N+M) log N); this build is sparse and Dijkstra is efficient.)\n")


if __name__ == "__main__":
    run_demo()
    benchmark()
```

### What you’ll see when you run it

* The two sample cases print:

  * **Neeman’s Wool Joggers** for `X=5`
  * **Neeman’s Cotton Classics** for `X=6`
* An extra “unreachable” case prints **Joggers** (∞ > X).
* A timing section shows average seconds/run for a 10k-node sparse graph.

---

## 6) Real-World Use Cases (most important ones)

1. **Navigation / Maps**
   Choose travel mode (walk vs run/drive) based on the **shortest path distance** between two points in a road network with varying edge weights (time, distance, congestion).

2. **Fitness Planning**
   Route planning apps decide **workout type** (walk vs run) or suggest shoe types based on the **length of the planned route** (thresholds like 5km, 10km).

3. **Logistics & Warehousing**
   In a weighted aisle graph (travel times), decide between **manual walking** or **using a cart/robot** if the **shortest path** to the next pick is above a certain threshold.

4. **Campus / Facility Management**
   For maintenance crews, determine whether to **walk** or **use a vehicle** depending on the shortest route length between buildings along allowed paths.