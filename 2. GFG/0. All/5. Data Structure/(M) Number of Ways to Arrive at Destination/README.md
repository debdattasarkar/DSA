
---

# 🚦 Number of Ways to Arrive at Destination

**Difficulty:** Medium
**Accuracy:** 61.13%
**Submissions:** 83K+
**Points:** 4
**Average Time:** 30m

---

## 🧠 Problem Statement

You are given an **undirected weighted graph** with **V vertices** numbered **from 0 to V−1** and **E edges**, represented as a 2D array `edges[][]`.

Each element

```
edges[i] = [uᵢ, vᵢ, timeᵢ]
```

means there is an undirected edge between nodes **uᵢ** and **vᵢ**, and it takes **timeᵢ** minutes to travel.

Your task is to return **in how many ways you can travel from node 0 to node V−1** *in the shortest possible time*.

---

## 🧩 Examples

### Example 1

**Input:**

```
V = 4,
edges = [
  [0, 1, 2],
  [1, 2, 3],
  [0, 3, 5],
  [1, 3, 3],
  [2, 3, 4]
]
```

**Output:**

```
2
```

**Explanation:**
Shortest path from **0 → 3** is **5 minutes**.
There are **two** such shortest paths:

```
0 → 3       (time = 5)
0 → 1 → 3   (time = 2 + 3 = 5)
```

---

### Example 2

**Input:**

```
V = 6,
edges = [
  [0, 2, 3],
  [0, 4, 2],
  [0, 5, 7],
  [2, 3, 1],
  [2, 5, 5],
  [5, 3, 3],
  [5, 1, 4],
  [1, 4, 1],
  [4, 5, 5]
]
```

**Output:**

```
4
```

**Explanation:**
Shortest time from **0 → 5** is **7 minutes**.
Four ways to do this:

```
0 → 5
0 → 4 → 5
0 → 4 → 1 → 5
0 → 2 → 3 → 5
```

---

## 📌 Constraints

```
1 ≤ V ≤ 200
V − 1 ≤ edges.size() ≤ V * (V − 1) / 2
0 ≤ uᵢ, vᵢ ≤ V − 1
1 ≤ timeᵢ ≤ 10⁵
uᵢ ≠ vᵢ
```

---

## ⏱ Expected Complexities

* **Time Complexity:**
  [
  O(V + E \log E)
  ]
* **Auxiliary Space:**
  [
  O(V + E)
  ]

---

## 🏢 Company Tags

* Bloomberg
* Google
* Microsoft
* Amazon

---

## 🧵 Topic Tags

* Graph
* Shortest Path
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [**Number Of Ways To Reach At Destination In Shortest Time**](https://www.geeksforgeeks.org/number-of-ways-to-reach-at-destination-in-shortest-time/)

---

---

Let’s make this one rock-solid for interviews. 🚦

---

## 2. Explanation + Step-by-step Dry Run

### Problem in plain words

* You have an **undirected weighted graph** with vertices `0 .. V-1`.
* Each edge `[u, v, time]` = road between `u` and `v` that takes `time` minutes.
* You must go from **node 0** to **node V-1** using **minimum total time**.
* Question: **In how many different ways** can you reach `V-1` using such *shortest* paths?

> We are not counting all paths, only those whose total time equals the **shortest distance** from `0` to `V-1`.

Most platforms also say: return answer **mod 1e9+7** (I’ll include that).

---

### Key idea: Dijkstra + “number of ways” DP

We want **two things at once**:

1. `dist[u]` = shortest distance from `0` to `u`.
2. `ways[u]` = number of shortest paths from `0` to `u`.

We can use **Dijkstra’s algorithm** (min-heap) and slightly extend it:

* Initialize:

  * `dist[0] = 0`, `ways[0] = 1`
  * all other `dist[i] = +∞`, `ways[i] = 0`

* Use a min-heap `(distance_so_far, node)` starting with `(0, 0)`.

* When we **relax** an edge `u --time--> v`:

  * Let `new_dist = dist[u] + time`.

  1. **Found a strictly better distance:**

     * If `new_dist < dist[v]`:

       * Update `dist[v] = new_dist`.
       * Reset `ways[v] = ways[u]` (all best paths to `v` now go via `u`).
       * Push `(dist[v], v)` into the heap.

  2. **Found another path with exactly the same best distance:**

     * If `new_dist == dist[v]`:

       * Add the number of ways:

         * `ways[v] = (ways[v] + ways[u]) % MOD`

* Ignore heap entries with distance > `dist[u]` (classic Dijkstra optimization).

* At the end, `ways[V-1]` is the answer.

---

### Dry Run – Example 1

Graph:

```text
V = 4
edges = [
  [0, 1, 2],
  [1, 2, 3],
  [0, 3, 5],
  [1, 3, 3],
  [2, 3, 4]
]
```

Adjacency list (u: (v, time)):

```text
0: (1,2), (3,5)
1: (0,2), (2,3), (3,3)
2: (1,3), (3,4)
3: (0,5), (1,3), (2,4)
```

Initial:

```text
dist = [0,  inf, inf, inf]
ways = [1,    0,   0,   0]
heap = [(0, 0)]
```

---

#### Step 1: pop (0, 0)

Neighbors of `0`:

1. Edge `0 -> 1` (time 2)

```text
new_dist = 0 + 2 = 2  < dist[1] (inf)
=> better: dist[1] = 2; ways[1] = ways[0] = 1
push (2, 1)
```

2. Edge `0 -> 3` (time 5)

```text
new_dist = 0 + 5 = 5 < dist[3] (inf)
=> dist[3] = 5; ways[3] = ways[0] = 1
push (5, 3)
```

Now:

```text
dist = [0, 2, inf, 5]
ways = [1, 1,  0, 1]
heap = [(2,1), (5,3)]
```

---

#### Step 2: pop (2, 1)

Neighbors of `1`:

1. `1 -> 0` (time 2)

```text
new_dist = 2 + 2 = 4 > dist[0] (0)
=> ignore (longer)
```

2. `1 -> 2` (time 3)

```text
new_dist = 2 + 3 = 5 < dist[2] (inf)
=> better: dist[2] = 5; ways[2] = ways[1] = 1
push (5, 2)
```

3. `1 -> 3` (time 3)

```text
new_dist = 2 + 3 = 5 == dist[3] (5)
=> equal shortest distance!
   ways[3] = ways[3] + ways[1] = 1 + 1 = 2
(no need to push again for same distance, but OK if you do)
```

Now:

```text
dist = [0, 2, 5, 5]
ways = [1, 1, 1, 2]
heap = [(5,3), (5,2)]
```

Interpretation:

* There is **1 shortest path to 2** (0 → 1 → 2, distance 5).
* There are **2 shortest paths to 3**:

  * 0 → 3 (5)
  * 0 → 1 → 3 (2+3 = 5)

---

#### Step 3: pop (5, 2)

Neighbors of `2`:

* Any new path through 2 will have distance ≥ 5 + something →
  For 3:

  * `new_dist = 5 + 4 = 9 > dist[3] (5)` → ignore.

No updates.

---

#### Step 4: pop (5, 3)

Neighbors of 3 produce no shorter paths either.

Algorithm ends.
Answer = `ways[3] = 2`.

Matches sample. ✅

---

## 3. Python Codes

Required format:

```python
class Solution:
    def countPaths(self, V, edges):
        # code here
```

### 3.1 Conceptual Brute Force (DFS with pruning) – for understanding only

> ⚠️ This will blow up for large graphs (exponential in paths), but it’s good conceptually:
>
> * First find the shortest distance with Dijkstra.
> * Then do a DFS that only walks along edges consistent with that shortest distance and counts paths.

I’ll just outline the idea, not full brute DFS code, because the optimized Dijkstra-with-ways is what interviewers want.

---

### 3.2 Optimized Dijkstra + ways (expected solution)

```python
import heapq

MOD = 10**9 + 7

class Solution:
    def countPaths(self, V, edges):
        """
        Count the number of shortest paths from node 0 to node V-1.

        Approach:
          - Use Dijkstra's algorithm from node 0.
          - Maintain:
                dist[u] = shortest distance from 0 to u
                ways[u] = number of shortest paths achieving dist[u]
          - Relax edges:
                new_dist = dist[u] + w
                if new_dist < dist[v]:
                    we found a better path:
                      dist[v] = new_dist
                      ways[v] = ways[u]
                      push (dist[v], v)
                elif new_dist == dist[v]:
                    we found another shortest path:
                      ways[v] = (ways[v] + ways[u]) % MOD

        Time  : O(E log V)   (standard Dijkstra with heap)
        Space : O(V + E)     (adjacency list + arrays)
        """

        # Build adjacency list for undirected graph
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # Step 1: Initialize distance and ways arrays
        INF = 10**18
        dist = [INF] * V
        ways = [0] * V

        dist[0] = 0          # distance to source is 0
        ways[0] = 1          # exactly one way to be at source: stay there

        # Min-heap storing (distance_so_far, node)
        heap = [(0, 0)]

        while heap:
            curr_dist, u = heapq.heappop(heap)

            # If this entry is stale (we've already found a better dist), skip it.
            if curr_dist > dist[u]:
                continue

            # Relax all neighbors
            for v, w in adj[u]:
                new_dist = curr_dist + w

                # Case 1: Found shorter path to v
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]     # all best paths to v go through u
                    heapq.heappush(heap, (new_dist, v))

                # Case 2: Found another shortest path to v
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[V - 1] % MOD
```

This is the solution you should use in interviews.

---

## 4. Interview: How to Remember & What They Ask

### 5-line pseudo-code (core idea)

```text
init dist[i]=INF, ways[i]=0; dist[0]=0; ways[0]=1
minHeap = [(0,0)]

while heap not empty:
    d,u = pop_min()
    if d > dist[u]: continue
    for (v,w) in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd; ways[v] = ways[u]; push(nd,v)
        elif nd == dist[v]:
            ways[v] = (ways[v] + ways[u]) mod M

return ways[V-1]
```

### Mnemonic:

**“Dijkstra with a counter.”**

Say it as:

> “Run Dijkstra but keep `ways[u]`:
>
> * Better distance → copy ways
> * Same distance → add ways.”

---

### Likely Interview Questions & Good Answers

**Q1. Why use Dijkstra, not BFS?**

* We have **weighted edges** (times), not all equal.
* BFS only works for **unit weight** graphs.
* Dijkstra is the classic algorithm for non-negative weighted shortest paths.

---

**Q2. How do you count multiple shortest paths correctly?**

> For each node `v`, we store:
>
> * `dist[v]`: best distance found so far
> * `ways[v]`: number of paths attaining `dist[v]`
>
> When relaxing an edge `u→v`:
>
> * If we find a **strictly better** distance:
>   `dist[v] = new_dist`, `ways[v] = ways[u]` (new best routes all come via `u`).
> * If we find a distance **equal** to the best:
>   `ways[v] += ways[u]` (we found additional shortest paths to `v`).

---

**Q3. Why can we skip `(d, u)` when `d > dist[u]`?**

> Because Dijkstra may have pushed an outdated pair into the heap before discovering a shorter path to `u`.
> When we see `d > dist[u]`, we know a better path already exists; exploring neighbors from this longer path cannot improve anything.

---

**Q4. What’s the complexity?**

> * Building adjacency list: `O(E)`.
> * Dijkstra + heap:
>
>   * Each edge is relaxed at most once in effective sense.
>   * Heap operations: `O((V + E) log V)`.
> * For dense graphs `E ≈ V²`, this is `O(E log V)`.

---

**Q5. Why modulus `1e9+7`?**

> The number of shortest paths can grow very large. Many platforms specify to return the result modulo `1e9+7` to avoid overflow and to keep the value within 32/64-bit limits.

---

### 60-second recall before coding

1. **Recognize**: “Weighted undirected graph, count ways of shortest path → Dijkstra + ways.”
2. **Say**:

   > “I’ll run Dijkstra from 0, maintain `dist[]` and `ways[]`.
   > When `new_dist < dist[v]`, update dist & copy ways.
   > When `new_dist == dist[v]`, add ways.”
3. **Write skeleton** for distance + heap.
4. **Fill relax logic** with the two cases.
5. **Return** `ways[V-1] % MOD`.

You’re now completely prepared to explain and implement this in an interview.

---
---

Nice, let’s finish this one properly.

---

## 5. Real-World Use Cases (easy to mention to an interviewer)

Think of **shortest path + number of optimal routes**:

1. **Navigation / Map Routing (multiple equally-short routes)**

   * City map with travel times between intersections.
   * Query: “How many *equally fast* ways can I go from A (0) to B (V-1)?”
   * Our algorithm is exactly: Dijkstra to get shortest time, and we count how many routes achieve that time.

2. **Network Routing / Load Balancing**

   * Graph = network of routers, edge weights = latency.
   * You want **all shortest-latency paths** so you can split traffic or have backup routes.
   * `ways[target]` tells how many distinct minimal-latency paths exist.

3. **Project / Workflow Planning**

   * Nodes = milestones, edges = time between tasks.
   * You might want to know how many different critical paths (minimum completion time paths) exist between start and finish to understand risk redundancy.

These are all simple to explain and map directly onto “weighted graph, shortest time, count of shortest paths.”

---

## 6. Full Python Program (with complexity comments + timing)

Below is a complete, runnable script:

* Implements `class Solution.countPaths` using **Dijkstra + ways**.
* Includes **inline complexity comments**.
* Runs the **sample test cases** from the problem.
* Uses `timeit` to measure runtime for each test.

```python
"""
Number of Ways to Arrive at Destination
---------------------------------------
We have an undirected weighted graph with V nodes (0..V-1) and edges [u, v, time].
We must count the number of DISTINCT paths from node 0 to node V-1 that have
MINIMUM possible total time.

Algorithm:
    Dijkstra's algorithm extended with a "ways" array.

For each node u:
    dist[u] = length of the shortest path from 0 to u
    ways[u] = number of shortest paths from 0 to u

Relaxation rule when we consider edge u --w--> v:
    new_dist = dist[u] + w

    if new_dist < dist[v]:
        # Found a better (shorter) path to v
        dist[v] = new_dist
        ways[v] = ways[u]      # All shortest paths to v currently go via u

    elif new_dist == dist[v]:
        # Found an additional shortest path to v
        ways[v] = (ways[v] + ways[u]) % MOD

We run standard Dijkstra with a min-heap.

Time complexity:
    - Building adjacency list:   O(V + E)
    - Dijkstra with heap:        O((V + E) log V)  ~ O(E log V)
Space complexity:
    - Adjacency list:            O(V + E)
    - dist[], ways[], heap:      O(V + E) overall

"""

from typing import List, Tuple
import heapq
import timeit

MOD = 10**9 + 7


class Solution:
    def countPaths(self, V: int, edges: List[List[int]]) -> int:
        """
        Count number of shortest paths from node 0 to node V-1.

        Parameters:
            V     : number of vertices (0 .. V-1)
            edges : list of [u, v, time] undirected weighted edges

        Returns:
            Number of shortest paths from 0 to V-1 modulo 1e9+7.
        """

        # -------- Build adjacency list (O(V + E) time & space) --------
        adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # -------- Initialize dist[] and ways[] (O(V)) --------
        INF = 10**18
        dist = [INF] * V   # dist[u] = shortest distance from 0 to u
        ways = [0] * V     # ways[u] = number of shortest paths to u

        dist[0] = 0
        ways[0] = 1

        # Min-heap of (distance_so_far, node); start from source 0.
        # Heap operations: O(log V) each.
        heap: List[Tuple[int, int]] = [(0, 0)]

        # -------- Dijkstra main loop (O((V+E) log V)) --------
        while heap:
            curr_dist, u = heapq.heappop(heap)

            # If we have already found a better path to u, skip.
            # This check ensures each edge is processed effectively once.
            if curr_dist > dist[u]:
                continue

            # Relax edges from u
            for v, w in adj[u]:
                new_dist = curr_dist + w

                # Case 1: new shortest path to v
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]               # inherit count of paths
                    heapq.heappush(heap, (new_dist, v))

                # Case 2: another shortest path to v
                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        # ways[V-1] holds number of shortest paths from 0 to V-1
        return ways[V - 1] % MOD


# ----------------------- Demo & Timing ----------------------- #
if __name__ == "__main__":
    solver = Solution()

    # Example 1 from problem
    V1 = 4
    edges1 = [
        [0, 1, 2],
        [1, 2, 3],
        [0, 3, 5],
        [1, 3, 3],
        [2, 3, 4],
    ]
    expected1 = 2  # from statement

    # Example 2 from problem
    V2 = 6
    edges2 = [
        [0, 2, 3],
        [0, 4, 2],
        [0, 5, 7],
        [2, 3, 1],
        [2, 5, 5],
        [5, 3, 3],
        [5, 1, 4],
        [1, 4, 1],
        [4, 5, 5],
    ]
    expected2 = 4  # from statement

    tests = [
        (V1, edges1, expected1, "Example 1"),
        (V2, edges2, expected2, "Example 2"),
    ]

    for V, edges, expected, label in tests:
        print(f"\n=== {label} ===")
        print(f"V = {V}")
        print("Edges [u, v, time]:")
        for e in edges:
            print("  ", e)

        # Time the run for this test
        elapsed = timeit.timeit(
            lambda: solver.countPaths(V, edges),
            number=1
        )
        result = solver.countPaths(V, edges)

        print(f"\nShortest-path count from 0 to {V-1}: {result}")
        print(f"Expected: {expected}")
        print(f"Time taken for countPaths(): {elapsed:.8f} seconds")
```

### What this program gives you

* Clean `Solution.countPaths` implementation with:

  * **Adjacency list build**
  * **Dijkstra + ways logic**
  * Clear **time/space annotations** in comments.
* A small **main section** that:

  * Prints the input graph.
  * Runs `countPaths`.
  * Shows the result vs expected.
  * Uses `timeit` to print how long the call took.

You can paste this into any Python file and run it directly.