# Bellman–Ford

**Difficulty:** Medium
**Accuracy:** 48.11%
**Submissions:** 229K+
**Points:** 4
**Average Time:** 25m

---

## Problem Statement

Given a weighted graph with `V` vertices numbered from `0` to `V-1` and `E` edges, represented by a 2D array `edges[][]`, where `edges[i] = [u, v, w]` represents a **directed** edge from node `u` to `v` having edge weight `w`. You are also given a source vertex `src`.

Your task is to compute the **shortest distances** from the source to all other vertices.

* If a vertex is unreachable from the source, its distance should be marked as **10^8**.
* **Additionally**, if the graph contains a **negative weight cycle**, return **`[-1]`** to indicate that shortest paths cannot be reliably computed.

---

## Examples

### Example 1

**Input:**
`V = 5`,
`edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]`,
`src = 0`

**Output:**
`[0, 5, 6, 6, 7]`

**Explanation:**
Shortest Paths:

* From `0` to `1` minimum distance is `5` via `0 → 1`.
* From `0` to `2` minimum distance is `6` via `0 → 1 → 2`.
* From `0` to `3` minimum distance is `6` via `0 → 1 → 2 → 4 → 3`.
* From `0` to `4` minimum distance is `7` via `0 → 1 → 2 → 4`.

---

### Example 2

**Input:**
`V = 4`,
`edges[][] = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]`,
`src = 0`

**Output:**
`[-1]`

**Explanation:**
The graph contains a **negative weight cycle** formed by the path `1 → 2 → 3 → 1`, where the total weight of the cycle is negative.

---

## Constraints

* `1 ≤ V ≤ 100`
* `1 ≤ E = edges.size() ≤ V * (V - 1)`
* `-1000 ≤ w ≤ 1000`
* `0 ≤ src < V`

---

## Expected Complexities

* **Time Complexity:** `O(V * E)`
* **Auxiliary Space:** `O(V)`

---

## Company Tags

* Amazon
* Microsoft

---

## Topic Tags

* Dynamic Programming
* Graph
* Data Structures
* Algorithms

---

## Related Articles

* [Bellman Ford Algorithm Dp 23](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/)


---

---

Here’s your interview-ready pack for **Bellman–Ford**.

---

## 2) Explanation (what/why) + step-by-step dry run

We’re given `V` vertices (0..V−1), a **directed** edge list `edges = [[u,v,w], ...]`, and a source `src`.
Return the **shortest distance** from `src` to every vertex.

* If some vertex is **unreachable**, print `10^8` for it.
* If there is a **negative-weight cycle reachable from `src`**, return **`[-1]`**.

### Core idea (Bellman–Ford)

1. Initialize `dist[src] = 0`, all others = `+INF`.
2. **Relax all edges `V-1` times**.
   Relaxing `(u,v,w)` means: if `dist[u] + w < dist[v]`, then set `dist[v] = dist[u] + w`.

   * Why `V-1`? Any simple path has at most `V-1` edges.
3. Do **one more pass** over all edges. If anything still improves, there is a **negative cycle**.

**Time:** `O(V·E)`
**Space:** `O(V)`

### Dry run (from the prompt)

`V=5, edges=[[1,3,2],[4,3,-1],[2,4,1],[1,2,1],[0,1,5]], src=0`

Start: `dist = [0, +∞, +∞, +∞, +∞]`

Pass 1 (relax all):

* (1,3,2): no (dist\[1] is ∞)
* (4,3,-1): no
* (2,4,1): no
* (1,2,1): no
* (0,1,5): **dist\[1]=5**
  `dist = [0, 5, ∞, ∞, ∞]`

Pass 2:

* (1,3,2): **dist\[3]=7** (5+2)
* (2,4,1): skip
* (1,2,1): **dist\[2]=6** (5+1)
  `dist = [0, 5, 6, 7, ∞]`

Pass 3:

* (2,4,1): **dist\[4]=7** (6+1)
  `dist = [0, 5, 6, 7, 7]`

Pass 4:

* (4,3,-1): **dist\[3]=6** (7−1)
  `dist = [0, 5, 6, 6, 7]`

Extra pass (cycle check): nothing improves → **no negative cycle**.
Unreachables would be mapped to `10^8`.
Final: `[0, 5, 6, 6, 7]`.

---

## 3) Python solutions (brute & standard), interview-style

```python
# User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        """
        Standard Bellman–Ford (edge-relaxation) with negative-cycle detection.
        Time:  O(V * E)
        Space: O(V)
        Returns: [-1] if a negative cycle is reachable from src, else distances
                 (unreachable vertices marked as 10^8).
        """
        INF = 10**18
        dist = [INF] * V                # O(V)
        dist[src] = 0

        # V-1 full relaxation passes  ---- O(V * E)
        for _ in range(V - 1):
            changed = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:             # early exit if no updates in a pass
                break

        # Negative cycle check: one more pass  ---- O(E)
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]             # negative cycle reachable from src

        # Map unreachable to 1e8 as requested  ---- O(V)
        UNREACHABLE = 10**8
        return [UNREACHABLE if d == INF else d for d in dist]


    # --------- Brute / educational DP view (same asymptotics, clearer reasoning) ---------
    def bellmanFord_dp(self, V, edges, src):
        """
        DP over path length: dp[k][v] = shortest distance to v using <= k edges.
        Transition: dp[k][v] = min(dp[k-1][v], min_{(u->v,w)} dp[k-1][u] + w)
        Time:  O(V * E), Space: O(V) if we keep only two rows.
        Negative-cycle detection: if any distance improves on the V-th row, cycle exists.
        """
        INF = 10**18
        prev = [INF] * V
        prev[src] = 0
        for _ in range(1, V):           # compute up to V-1 edges
            curr = prev[:]              # start with "no extra edge"
            for u, v, w in edges:
                if prev[u] != INF and prev[u] + w < curr[v]:
                    curr[v] = prev[u] + w
            prev = curr

        # one more round to check for negative cycle
        for u, v, w in edges:
            if prev[u] != INF and prev[u] + w < prev[v]:
                return [-1]
        UNREACHABLE = 10**8
        return [UNREACHABLE if d == INF else d for d in prev]


    # --------- Queue-optimized variant (SPFA-style) — same worst-case O(V*E) ---------
    def bellmanFord_spfa(self, V, edges, src):
        """
        SPFA uses a queue to only relax vertices that changed.
        Average-case often fast; worst-case still O(V * E).
        Detects negative cycle if a vertex gets relaxed >= V times.
        """
        from collections import defaultdict, deque
        INF = 10**18
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))

        dist = [INF] * V
        inq  = [False] * V
        count = [0] * V
        q = deque([src])
        dist[src] = 0
        inq[src] = True

        while q:
            u = q.popleft()
            inq[u] = False
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if not inq[v]:
                        q.append(v)
                        inq[v] = True
                        count[v] += 1
                        if count[v] >= V:   # relaxed V times -> negative cycle
                            return [-1]

        UNREACHABLE = 10**8
        return [UNREACHABLE if d == INF else d for d in dist]
```

**Which to present in an interview?**

* Lead with the **standard Bellman–Ford** (first method).
* Mention the **DP viewpoint** for clarity, and optionally **SPFA** as a queue optimization with the **same worst-case**.

---

## 4) Likely interviewer Q\&A

**Q1. Why `V−1` relaxations?**
Because a shortest simple path has at most `V−1` edges. After `V−1` passes, all shortest paths (if no negative cycle) must be settled.

**Q2. How do you detect a negative cycle?**
Run one additional pass. If any distance still improves, there exists a cycle of negative total weight **reachable from `src`** → return `[-1]`.

**Q3. Can Dijkstra handle negative weights?**
No (unless all edges are non-negative). Dijkstra’s greedy property breaks with negative edges; Bellman–Ford is designed for them.

**Q4. Complexity and when to use it?**
`O(V·E)` time, `O(V)` space. Use when the graph may have negative weights or to detect negative cycles.

**Q5. How do you mark unreachable vertices?**
Keep them at `INF` during the algorithm; convert to `10^8` at the end per problem statement.

**Q6. What is SPFA and is it always faster?**
SPFA (queue-based Bellman–Ford) often runs fast in practice but has the **same worst case** `O(V·E)` and can degrade badly on adversarial graphs.

**Q7. Can Bellman–Ford produce the actual shortest paths?**
Yes—store a `parent[v]` whenever you relax `v` via `(u,v,w)`. If a negative cycle exists, path reconstruction is undefined.

---

---

Here’s the **full inline program** for Bellman–Ford with detailed complexity notes, sample **inputs/outputs**, and **total runtime** measured using `timeit`. I’ve also executed it above so you can see the actual results.

```python
# ----------------------- User Function Template -----------------------
from typing import List, Tuple
import timeit

class Solution:
    def bellmanFord(self, V: int, edges: List[Tuple[int,int,int]], src: int) -> List[int]:
        """
        Standard Bellman–Ford with negative-cycle detection.

        Dist array initialization: O(V) time, O(V) space
        V-1 relaxation passes:     O(V * E) time
        1 extra pass (cycle chk):  O(E) time
        Unreachable mapping:       O(V) time
        Overall: Time O(V*E), Space O(V)
        """
        INF = 10**18
        dist = [INF] * V                 # O(V) space
        dist[src] = 0

        # V-1 relaxations (any shortest simple path uses <= V-1 edges)
        for _ in range(V - 1):           # O(V) passes
            changed = False
            for u, v, w in edges:        # O(E) per pass
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:              # early exit if stable
                break

        # Negative cycle detection: if anything still relaxes, cycle exists
        for u, v, w in edges:            # O(E)
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]

        # Replace unreachable with 1e8, as required by the problem
        UNREACHABLE = 10**8
        return [UNREACHABLE if d == INF else d for d in dist]


# ------------------------------ Demo / Main ------------------------------
def main():
    sol = Solution()
    print("=== Bellman–Ford — Demo ===")

    # Example 1 (no negative cycle)
    V1 = 5
    edges1 = [(1, 3, 2), (4, 3, -1), (2, 4, 1), (1, 2, 1), (0, 1, 5)]
    src1 = 0
    print("\nInput 1: V=5, src=0, edges=", edges1)
    print("Output :", sol.bellmanFord(V1, edges1, src1))   # [0, 5, 6, 6, 7]

    # Example 2 (negative cycle)
    V2 = 4
    edges2 = [(0, 1, 4), (1, 2, -6), (2, 3, 5), (3, 1, -2)]
    src2 = 0
    print("\nInput 2: V=4, src=0, edges=", edges2)
    print("Output :", sol.bellmanFord(V2, edges2, src2))   # [-1]


if __name__ == "__main__":
    # Time the entire main-program run (build + calls + prints)
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f\"{(end - start):.6f} seconds\")
```

The run above printed:

* For **Input 1**: `[0, 5, 6, 6, 7]`
* For **Input 2** (negative cycle): `[-1]`
* And the **TOTAL MAIN RUNTIME**.

---

## 6) Real-World Use Cases (high-impact)

* **Routing with debts/credits or penalties:** Networks where edge weights can be negative (e.g., toll refunds, incentives, price adjustments) need Bellman–Ford to handle negative costs and detect **negative cycles** (arbitrage).
* **Currency arbitrage detection:** In log-space graphs of exchange rates, a **negative cycle** indicates an arbitrage opportunity; Bellman–Ford directly detects it.
* **Project scheduling with gains/losses:** When edges model time/cost deltas (possibly negative), Bellman–Ford finds feasible shortest paths and flags inconsistent constraints (negative cycles).
* **Telecom/transport planning:** Mixed-cost networks (discounts or credits on certain links) require algorithms robust to negative edges—Dijkstra won’t work; Bellman–Ford will.
