
---

# **Shortest Path Using At Most One Curved Edge**

**Difficulty:** Hard
**Accuracy:** 59.43%
**Submissions:** 19K+
**Points:** 8

---

## **Problem Statement**

You are given an undirected, connected graph with **V** vertices numbered from **0 to V–1** and **E double-edges**, represented as a 2D array `edges[][]`.

Each double-edge is represented by a tuple:

```
(x, y, w1, w2)
```

This indicates:

* There are **two edges** between vertices `x` and `y`:

  * A **straight edge** with weight **w1**
  * A **curved edge** with weight **w2**

You are given two vertices **a** and **b**, and your task is to find the **shortest possible path** from `a` to `b` such that **in the entire path, you use at most ONE curved edge**.

If no such path exists under this restriction, return **-1**.

> **Note:** It is guaranteed that the shortest path value will fit in a 32-bit integer.

---

## **Examples**

---

### **Example 1**

**Input:**

```
V = 4, E = 4, a = 1, b = 3
edges[][] = [
  [0, 1, 1, 4],
  [0, 2, 2, 4],
  [0, 3, 3, 1],
  [1, 3, 6, 5]
]
```

**Output:**

```
2
```

**Explanation:**

* Straight path:
  `1 → 0 → 3` gives distance `1 + 3 = 4`.
* Using the curved edge:
  take curved edge `0 → 3` of weight `1`, resulting in total = `1 + 1 = 2`.

So the optimal path uses **exactly one curved edge**.

---

### **Example 2**

**Input:**

```
V = 2, E = 1, a = 0, b = 1
edges[][] = [
  [0, 1, 4, 1]
]
```

**Output:**

```
1
```

**Explanation:**
Take the **curved** edge from `0 → 1` with cost `1`.

---

## **Constraints**

* `1 ≤ V ≤ 10⁶`
* `0 ≤ E ≤ 10⁶`
* `0 ≤ a, b ≤ V - 1`
* `0 ≤ edges[i][0], edges[i][1] ≤ V - 1`
* `0 ≤ edges[i][2], edges[i][3] ≤ 10⁴`

---

## **Expected Complexities**

* **Time Complexity:** `O((V + E) * log(V))`
* **Auxiliary Space:** `O(V + E)`

---

## **Company Tags**

* Uber

---

## **Topic Tags**

* Graph
* Shortest Path
* Data Structures
* Algorithms

---

## **Related Interview Experiences**

* Uber Interview Experience On Campus For Internship 2018–19

---

## **Related Articles**

* [*Shortest Path With One Curved Edge In An Undirected Graph*](https://www.geeksforgeeks.org/shortest-path-with-one-curved-edge-in-an-undirected-graph/)

---

---

I’ll walk through:

1. Intuition + step-by-step dry run
2. Optimized Python solutions (two variants) in your required format
3. Interview memory trick + likely Q&A

---

## 2. Intuition + Step-by-Step Explanation

### Problem recap

* Graph is **undirected**.
* For every pair of connected vertices `x` and `y`, we have **two parallel edges**:

  * a **straight** edge with weight `w1`
  * a **curved** edge with weight `w2`
* You must go from **a** to **b** using a path that has **at most one curved edge** (0 or 1).
* Goal: **minimum total weight** of such a path, or `-1` if impossible.

Key thinking:

Any valid path falls into exactly one of these types:

1. **Type 0:** uses **only straight edges**
2. **Type 1:** uses **exactly one curved edge** somewhere

So:

> Answer = min(
> *shortest straight-only path a→b*,
> *best path a→…→x –(curved x–y)– …→b*
> )

Let’s reason about Type-1 path:

* Suppose the optimal path uses **one curved edge** between `x` and `y`.
* Everything **before** that curved edge must use only straight edges.
* Everything **after** that curved edge must use only straight edges.
* So its cost is:

```text
distStraight(a → x) + w_curved(x,y) + distStraight(y → b)
```

or, because graph is undirected and you don’t know which direction you enter the curved edge:

```text
min(
    distA[x] + w2(x,y) + distB[y],
    distA[y] + w2(x,y) + distB[x]
)
```

where:

* `distA[v]` = shortest distance from `a` to `v` **using only straight edges**
* `distB[v]` = shortest distance from `b` to `v` **using only straight edges**

So algorithm:

1. Build graph using **only straight edges** (w1).
2. Run **Dijkstra from `a`** → `distA`.
3. Run **Dijkstra from `b`** → `distB`.
4. Candidate 0-curved answer: `distA[b]`.
5. For each edge `(x, y, w1, w2)`:

   * consider using its curved edge once:
   * `cand1 = distA[x] + w2 + distB[y]`
   * `cand2 = distA[y] + w2 + distB[x]`
   * take the minimum of all candidates.
6. Overall answer = min(0-curved answer, best curved candidate).
   If everything is infinite → return `-1`.

Dijkstra is needed because weights are arbitrary positive (`≤ 10^4`), graph up to `10^6` vertices and edges.

---

### Dry Run – Example 1

> `V = 4, E = 4, a = 1, b = 3`
> `edges = [ [0,1,1,4], [0,2,2,4], [0,3,3,1], [1,3,6,5] ]`

Interpretation:

* Straight edges:

  * 0–1 (1), 0–2 (2), 0–3 (3), 1–3 (6)
* Curved edges:

  * 0–1 (4), 0–2 (4), 0–3 (1), 1–3 (5)

We need shortest path from `1` to `3` using **≤ 1 curved edge**.

---

#### Step 1: Dijkstra from `a = 1` using only straight edges

Initialize:

* `distA = [∞, 0, ∞, ∞]`
* PQ = `[(0,1)]`

Pop `(0,1)`:

* Neighbors via straight edges from 1:

  * 1–0 (1): `distA[0] = 0 + 1 = 1`
  * 1–3 (6): `distA[3] = 0 + 6 = 6`
* PQ = `[(1,0), (6,3)]`

Pop `(1,0)`:

* From 0:

  * 0–1 (1): would give 2 > distA[1]=0 → ignore
  * 0–2 (2): `distA[2] = 1 + 2 = 3`
  * 0–3 (3): `distA[3]` can be improved: `1 + 3 = 4` < 6 → update
* PQ = `[(3,2), (4,3), (6,3)]`

Pop `(3,2)`:

* From 2:

  * only straight edge is 2–0 (2)
  * would give `3 + 2 = 5` for `distA[0]`, but 1 is better → ignore
* PQ = `[(4,3), (6,3)]`

Pop `(4,3)`:

* From 3:

  * 3–0 (3) → candidate 7 vs 1 : ignore
  * 3–1 (6) → candidate 10 vs 0: ignore
* PQ exhausted (remaining is outdated 6).

So:

```text
distA = [1, 0, 3, 4]
```

Interpretation:

* shortest straight-only distance from 1:

  * to 0: 1
  * to 2: 3
  * to 3: 4

---

#### Step 2: Dijkstra from `b = 3` using only straight edges

`distB = [∞, ∞, ∞, 0]`
PQ = `[(0,3)]`

Pop `(0,3)`:

* 3–0 (3): `distB[0] = 3`
* 3–1 (6): `distB[1] = 6`
  PQ = `[(3,0), (6,1)]`

Pop `(3,0)`:

* 0–1 (1): candidate 4 < 6 → `distB[1] = 4`
* 0–2 (2): `distB[2] = 3 + 2 = 5`
  PQ = `[(4,1), (5,2), (6,1)]`

Pop `(4,1)`:

* 1–0 (1): candidate 5 > 3 → ignore
* 1–3 (6): candidate 10 > 0 → ignore

Remaining are outdated. Final:

```text
distB = [3, 4, 5, 0]
```

---

#### Step 3: Zero-curved candidate

* straight-only path from 1 to 3 = `distA[3] = 4`

---

#### Step 4: Try each curved edge

For each tuple `(x, y, w1, w2)`:

1. Edge (0,1,1,4), curved weight 4

   * cand1 (a→0, curved 0→1, 1→b): `distA[0] + 4 + distB[1] = 1 + 4 + 4 = 9`
   * cand2 (a→1, curved 1→0, 0→b): `distA[1] + 4 + distB[0] = 0 + 4 + 3 = 7`

2. Edge (0,2,2,4), curved 4

   * cand1: `distA[0] + 4 + distB[2] = 1 + 4 + 5 = 10`
   * cand2: `distA[2] + 4 + distB[0] = 3 + 4 + 3 = 10`

3. Edge (0,3,3,1), curved 1

   * cand1: `distA[0] + 1 + distB[3] = 1 + 1 + 0 = 2`  ✅
   * cand2: `distA[3] + 1 + distB[0] = 4 + 1 + 3 = 8`

4. Edge (1,3,6,5), curved 5

   * cand1: `distA[1] + 5 + distB[3] = 0 + 5 + 0 = 5`
   * cand2: `distA[3] + 5 + distB[1] = 4 + 5 + 4 = 13`

Best curved candidate = **2** (using curved edge between 0 and 3).

---

#### Step 5: Final answer

`min(4, 2) = 2`, which matches the expected output.

Path:
`1 --(straight,1)--> 0 --(curved,1)--> 3`
Total = 1 + 1 = 2.

---

## 3. Optimized Python Solutions

### 3.1 Recommended solution – **Two Dijkstras + scan curved edges**

This is usually the **cleanest interview answer**.

```python
import heapq
from typing import List

class Solution:
    def shortestPath(self, V: int, a: int, b: int,
                     edges: List[List[int]]) -> int:
        """
        Compute the shortest path from a to b using at most one curved edge.

        V      : number of vertices (0..V-1)
        a, b   : source and destination vertices
        edges  : list of [x, y, w1, w2]
                 - w1 = weight of straight edge x<->y
                 - w2 = weight of curved edge  x<->y

        Approach:
        ---------
        1) Build adjacency for STRAIGHT edges only (using w1).
        2) Run Dijkstra from 'a' on straight graph -> dist_from_a.
        3) Run Dijkstra from 'b' on straight graph -> dist_from_b.
        4) Candidate 0-curved: dist_from_a[b].
        5) For each edge (x,y,w1,w2), evaluate using its curved edge once:
               cand1 = dist_from_a[x] + w2 + dist_from_b[y]
               cand2 = dist_from_a[y] + w2 + dist_from_b[x]
           Take minimum over all such candidates.
        6) Answer = min(0-curved candidate, best curved candidate).
           If answer is INF, return -1.

        Time Complexity:
            - Building adjacency: O(E)
            - Each Dijkstra:      O((V + E) log V)
            - Edge scan:          O(E)
            => Overall:           O((V + E) log V)

        Space Complexity:
            - Adjacency + distance arrays: O(V + E)
        """

        # ---------------- helper: Dijkstra on straight-edge graph -----------
        def dijkstra(start: int, adj: List[List[tuple]]) -> List[int]:
            INF = 10**18
            dist = [INF] * V
            dist[start] = 0
            min_heap = [(0, start)]          # (distance, vertex)

            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                if current_dist > dist[u]:
                    continue  # outdated entry

                for v, weight in adj[u]:
                    new_dist = current_dist + weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))

            return dist

        # Build adjacency list for straight edges (w1)
        # Time: O(E), Space: O(V + E)
        adj_straight = [[] for _ in range(V)]
        for x, y, w1, w2 in edges:
            adj_straight[x].append((y, w1))
            adj_straight[y].append((x, w1))

        INF = 10**18

        # Dijkstra from a and from b on straight edges only
        dist_from_a = dijkstra(a, adj_straight)
        dist_from_b = dijkstra(b, adj_straight)

        # Candidate using NO curved edges
        answer = dist_from_a[b]

        # Consider paths using exactly ONE curved edge
        # Time: O(E)
        best_with_curved = INF
        for x, y, w1, w2 in edges:
            # if either end is unreachable via straight edges, skip
            if dist_from_a[x] != INF and dist_from_b[y] != INF:
                cand1 = dist_from_a[x] + w2 + dist_from_b[y]
                if cand1 < best_with_curved:
                    best_with_curved = cand1
            if dist_from_a[y] != INF and dist_from_b[x] != INF:
                cand2 = dist_from_a[y] + w2 + dist_from_b[x]
                if cand2 < best_with_curved:
                    best_with_curved = cand2

        answer = min(answer, best_with_curved)

        return -1 if answer >= INF else answer
```

---

### 3.2 Alternate solution – **State-graph Dijkstra (vertex, usedCurved)**

This is a nice conceptual solution: treat “have we used the curved edge yet?” as part of the state.

* State = `(node, used)`, where:

  * `used = 0` → we haven’t used a curved edge yet
  * `used = 1` → we’ve already used one curved edge
* Straight edges:

  * from `(u, used)` to `(v, used)` with cost `w1`
* Curved edges:

  * from `(u, 0)` to `(v, 1)` with cost `w2`
  * from `(v, 0)` to `(u, 1)` with cost `w2`
  * (no curved edge if `used == 1`, we already spent our allowance)

Then run Dijkstra from `(a, 0)` to `(b, 0)` or `(b, 1)` (whichever smaller).

```python
import heapq
from typing import List

class SolutionStateDijkstra:
    def shortestPath(self, V: int, a: int, b: int,
                     edges: List[List[int]]) -> int:
        """
        Dijkstra on 'expanded' graph with state (node, usedCurved).

        Nodes:
            0..V-1  with usedCurved = 0 (no curved used yet)
            0..V-1  with usedCurved = 1 (already used curved)

        Edges:
            - Straight edge x--y with cost w1:
                (x,used) -> (y,used)
                (y,used) -> (x,used)
            - Curved edge x--y with cost w2:
                only allowed if usedCurved == 0:
                (x,0) -> (y,1), (y,0) -> (x,1)
        """

        # Build adjacency on-the-fly: we will treat 'used' dimension in Dijkstra.
        # To avoid doubling graph storage, we just store original edges and expand during traversal.
        straight_adj = [[] for _ in range(V)]
        curved_edges = []

        for x, y, w1, w2 in edges:
            straight_adj[x].append((y, w1))
            straight_adj[y].append((x, w1))
            curved_edges.append((x, y, w2))

        INF = 10**18
        # dist[node][used] : used in {0,1}
        dist = [[INF, INF] for _ in range(V)]
        dist[a][0] = 0

        # State in PQ: (distance, node, usedCurved)
        heap = [(0, a, 0)]

        while heap:
            current_dist, u, used = heapq.heappop(heap)
            if current_dist > dist[u][used]:
                continue

            # Straight edges: always allowed
            for v, w1 in straight_adj[u]:
                new_dist = current_dist + w1
                if new_dist < dist[v][used]:
                    dist[v][used] = new_dist
                    heapq.heappush(heap, (new_dist, v, used))

            # Curved edges: only if we have not yet used one
            if used == 0:
                for x, y, w2 in curved_edges:
                    if x == u:
                        v = y
                    elif y == u:
                        v = x
                    else:
                        continue
                    new_dist = current_dist + w2
                    if new_dist < dist[v][1]:
                        dist[v][1] = new_dist
                        heapq.heappush(heap, (new_dist, v, 1))

        # answer is best of reaching b with or without curved usage
        best = min(dist[b][0], dist[b][1])
        return -1 if best >= INF else best
```

> Note: From a performance point of view, this second version loops over `curved_edges` for each node, which is **O(V * E)** in the worst case, so it’s more of a **conceptual / brute-ish approach**, not ideal for 1e6 edges. The first solution (two Dijkstras) is what you should present as the final optimized answer.

---

## 4. Interview “How to Remember” + Expected Q&A

### 4.1 5-line template + mnemonic

**Mental 5-line algorithm:**

1. **Run Dijkstra from `a` using only straight edges → `distA`**
2. **Run Dijkstra from `b` using only straight edges → `distB`**
3. **ans = distA[b] (no curved)**
4. **For each edge (x,y, w1,w2):**
   `ans = min(ans, distA[x] + w2 + distB[y], distA[y] + w2 + distB[x])`
5. **If ans is INF → -1 else ans**

Easy mnemonic: **“Two D’s + Curved Scan”**

* **Two D’s** = two Dijkstras (from a and from b)
* **Curved Scan** = scan each edge’s curved weight once

Say this to yourself before you walk into the interview.

---

### 4.2 60-second spoken explanation

> “We’re allowed at most one curved edge, but any number of straight edges.
> So an optimal path either uses only straight edges, or uses exactly one curved edge between some x and y.
> If it uses a curved edge, then the path is: a → … → x (only straights), curved x–y, then y → … → b (only straights).
> That means we just need the shortest straight-only distances from a to every node, and from b to every node.
> I run Dijkstra twice on the graph formed only by the straight weights.
> Then I consider each curved edge (x,y,w2) and evaluate distA[x] + w2 + distB[y] and distA[y] + w2 + distB[x].
> The minimum of these values and the straight-only distance a→b is the answer.
> Complexity is O((V+E) log V) due to the two Dijkstras.”

---

### 4.3 Likely Interview Questions & Good Answers

---

**Q1. Why is it enough to run Dijkstra only on straight edges?**

Because any valid path can use **at most one curved edge**.
In a path with one curved edge (x–y):

* everything from `a` to that curved edge must be straight edges only;
* everything from that curved edge to `b` must be straight edges only.

So the cost decomposes as:

```text
distStraight(a,x) + w_curved(x,y) + distStraight(y,b)
```

We just need all `distStraight(a, *)` and `distStraight(b, *)`, which Dijkstra provides.

---

**Q2. Why do you run Dijkstra from both `a` and `b`?**

From `a`, I need `distA[x]` for every potential curved-edge endpoint `x`.
From `b`, I need `distB[x]` for distances from `x` to `b`.

The curved edge can be used in either direction, so for each curved edge (x,y):

```text
a -> x (straight), curved x–y, y -> b (straight)
or
a -> y (straight), curved y–x, x -> b (straight)
```

Hence `distA` and `distB` together cover all possibilities.

---

**Q3. Time and space complexity?**

* Building straight adjacency: `O(E)`
* Dijkstra from `a`: `O((V + E) log V)`
* Dijkstra from `b`: `O((V + E) log V)`
* Scanning all edges for curved candidate: `O(E)`

So total time is `O((V + E) log V)`.
Space is `O(V + E)` for adjacency and distance arrays.

---

**Q4. Why do we compare with the pure straight-path `distA[b]`?**

Because the best path might legitimately use **zero** curved edges.
Example: all curved edges are extremely expensive, or there are no curved edges at all.
`distA[b]` is the shortest straight-only path, so we must include it in the minimum.

---

**Q5. How do you handle the case where there is no valid path?**

We initialize all distances as `INF`.
If after Dijkstra, `distA[b]` is INF and for all curved edges either `distA[x]` or `distB[y]` is INF, then no valid path with ≤1 curved edge exists. We detect this because `answer` stays ≥ `INF`, and we return `-1`.

---

**Q6. Could we do it with a single Dijkstra?**

Yes, conceptually we can extend the state to `(node, usedCurved ∈ {0,1})` and run Dijkstra on this doubled graph.
But it’s a bit more complex and slightly heavier. The **two-Dijkstra + scan** method is simpler and very efficient for these constraints.

---

---

Alright, let’s finish this one nicely.

---

## 5. Real-World Use Cases (easy to explain in an interview)

Think of **two types of connections** between the same pair of nodes:

* **Straight edge** = normal / cheap / always allowed
* **Curved edge** = special / risky / discounted / “promo” connection
* We’re allowed to use **at most one special edge**.

Here are a few relatable scenarios:

### a) Road Navigation with One Toll / Express Segment

* Cities are vertices, roads are edges.
* For some road pairs, you have:

  * normal road (straight edge) with certain travel time
  * toll/express lane (curved edge) with different time (often shorter) but you want to pay toll at most once.
* “Find the fastest path from A to B if you can take **at most one toll road**.”

Maps perfectly: normal roads = straight edges; toll roads = curved, at most one.

---

### b) Network Routing with One Premium Link

* Servers are vertices, links are edges.
* Between some servers you have:

  * regular link (straight)
  * premium high-bandwidth link (curved) that costs extra money.
* You’re allowed to use at most one premium link in a route to keep cost controlled, but want minimal latency.

---

### c) Public Transport with One High-Speed Segment

* Stations are vertices.
* Between two stations, you may have:

  * regular train (straight edge)
  * high-speed train (curved edge).
* Ticket allows **only one high-speed ride**; find shortest travel time from station A to B.

---

### d) Data Processing Pipeline with One “Expensive Acceleration”

* Nodes are processing stages, edges are options between stages.
* For some stage transitions, you can:

  * use normal CPU processing
  * or use a GPU/accelerator call that is faster but expensive / limited.
* You’re allowed to call the accelerator at most once.

---

### e) Shipping / Logistics with One Air Cargo Leg

* Locations are nodes.
* Edges:

  * ground shipping (truck/train)
  * air cargo between some hubs (faster but expensive / limited).
* Business rule: at most one air leg per shipment; minimize total time or cost.

All of these map directly to:

> “Shortest path if you can upgrade *one* segment to a special kind.”

Mentioning one of these in an interview makes the model very concrete.

---

## 6. Full Python Program with Timing & Complexity Comments

This is a *complete* script:

* Uses the **two Dijkstra + curved scan** method.
* Includes inline comments with time/space notes.
* Uses the sample from the statement and times the run using `timeit.default_timer`.

```python
"""
Shortest Path Using At Most One Curved Edge

We have an undirected graph with V vertices (0..V-1).
Each edge is given as [x, y, w1, w2]:
    - Straight edge  x <-> y with weight w1
    - Curved  edge  x <-> y with weight w2

Task:
    Find the minimum distance from a to b if we are allowed to use
    at most ONE curved edge in the entire path (0 or 1 curved edges).

Key idea:
    Any valid path is either:
      - only straight edges, or
      - exactly one curved edge (x,y) plus straights on both sides.

Algorithm (optimized):
    1) Build adjacency list for STRAIGHT edges only.
    2) Run Dijkstra from 'a' on straight graph  -> dist_from_a[v]
    3) Run Dijkstra from 'b' on straight graph  -> dist_from_b[v]
    4) Candidate answer with 0 curved edges = dist_from_a[b]
    5) For each edge (x, y, w1, w2), try using its curved edge once:
         dist_from_a[x] + w2 + dist_from_b[y]
         dist_from_a[y] + w2 + dist_from_b[x]
       Take minimum over all.
    6) Answer = min(candidate0, best_with_curved), or -1 if unreachable.

Complexities:
    Time:  O((V + E) * log V)   (two Dijkstras + O(E) scan)
    Space: O(V + E)             (adjacency list + distance arrays)
"""

from typing import List
import heapq
from timeit import default_timer as timer


class Solution:
    def shortestPath(self, V: int, a: int, b: int,
                     edges: List[List[int]]) -> int:
        """
        Compute the shortest path from node 'a' to node 'b'
        using at most ONE curved edge.

        Parameters
        ----------
        V : int
            Number of vertices (0 .. V-1)
        a, b : int
            Source and destination nodes
        edges : List[List[int]]
            Each entry is [x, y, w1, w2]
              - x, y : endpoints of edge (undirected)
              - w1   : weight of straight edge
              - w2   : weight of curved edge

        Returns
        -------
        int
            Minimal distance, or -1 if no valid path exists.

        High-level Complexity
        ---------------------
        Time:
          - Build straight adjacency: O(E)
          - Dijkstra from a:          O((V + E) * log V)
          - Dijkstra from b:          O((V + E) * log V)
          - For-loop over edges:      O(E)
          => Overall: O((V + E) * log V)

        Space:
          - Adjacency list: O(V + E)
          - Distance arrays: O(V)
        """

        # ---------- Helper: Dijkstra on straight-edge graph ----------
        def dijkstra(source: int, adj: List[List[tuple]]) -> List[int]:
            """
            Standard Dijkstra from 'source' on given adjacency list.

            adj[u] = list of (v, weight) for STRAIGHT edges only.

            Time per call:
                O((V + E) * log V) using binary heap.
            Space:
                O(V) for 'dist' + heap overhead.
            """
            INF = 10**18
            dist = [INF] * V
            dist[source] = 0

            # Min-heap of (distance_so_far, vertex)
            min_heap = [(0, source)]

            while min_heap:
                current_dist, u = heapq.heappop(min_heap)

                # Skip outdated heap entries
                if current_dist > dist[u]:
                    continue

                # Relax outgoing straight edges
                for v, w in adj[u]:
                    new_dist = current_dist + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))

            return dist

        # ------------------------------------------------------------
        # 1) Build adjacency list for STRAIGHT edges using w1
        #
        #    Time:  O(E)
        #    Space: O(V + E)
        # ------------------------------------------------------------
        adj_straight: List[List[tuple]] = [[] for _ in range(V)]
        for x, y, w1, w2 in edges:
            adj_straight[x].append((y, w1))
            adj_straight[y].append((x, w1))

        INF = 10**18

        # ------------------------------------------------------------
        # 2) & 3) Dijkstra from a and from b (straight edges only)
        #
        #    Time:  O((V + E) * log V) each
        #    Space: O(V) each for distance arrays
        # ------------------------------------------------------------
        dist_from_a = dijkstra(a, adj_straight)
        dist_from_b = dijkstra(b, adj_straight)

        # ------------------------------------------------------------
        # 4) Candidate using NO curved edges:
        #    just the straight-only shortest path a -> b
        # ------------------------------------------------------------
        answer = dist_from_a[b]

        # ------------------------------------------------------------
        # 5) Consider paths that use exactly ONE curved edge.
        #
        #    For each edge (x, y, w1, w2):
        #       - if dist_from_a[x] and dist_from_b[y] are finite,
        #            cand1 = dist_from_a[x] + w2 + dist_from_b[y]
        #       - similarly for reversed direction.
        #
        #    Time:  O(E)
        #    Space: O(1) extra
        # ------------------------------------------------------------
        best_with_curved = INF

        for x, y, w1, w2 in edges:
            # Option 1: ... a -> x (straight), curved x-y, y -> b (straight)
            if dist_from_a[x] < INF and dist_from_b[y] < INF:
                candidate = dist_from_a[x] + w2 + dist_from_b[y]
                if candidate < best_with_curved:
                    best_with_curved = candidate

            # Option 2: ... a -> y, curved y-x, x -> b
            if dist_from_a[y] < INF and dist_from_b[x] < INF:
                candidate = dist_from_a[y] + w2 + dist_from_b[x]
                if candidate < best_with_curved:
                    best_with_curved = candidate

        # Combine straight-only and curved-using candidates
        if best_with_curved < answer:
            answer = best_with_curved

        # If still INF, no valid path with ≤ 1 curved edge exists
        return -1 if answer >= INF else answer


# ---------------------------------------------------------------------
# Example usage + timing
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Example from the problem statement
    V = 4
    a = 1
    b = 3
    edges = [
        [0, 1, 1, 4],
        [0, 2, 2, 4],
        [0, 3, 3, 1],
        [1, 3, 6, 5]
    ]

    print("Input:")
    print("V     =", V)
    print("a, b  =", a, b)
    print("edges =", edges)

    # Measure time for one call of shortestPath
    start_time = timer()
    sol = Solution()
    result = sol.shortestPath(V, a, b, edges)
    end_time = timer()

    print("\nOutput:")
    print("Shortest path using at most one curved edge:", result)

    elapsed = end_time - start_time
    print("\nElapsed time (seconds):", elapsed)
```

If you run this script, you’ll see something like:

```text
Input:
V     = 4
a, b  = 1 3
edges = [[0, 1, 1, 4], [0, 2, 2, 4], [0, 3, 3, 1], [1, 3, 6, 5]]

Output:
Shortest path using at most one curved edge: 2

Elapsed time (seconds): 3.1e-05
```

