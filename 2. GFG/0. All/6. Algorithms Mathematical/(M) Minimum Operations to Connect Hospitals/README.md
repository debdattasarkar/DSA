
---

# **Minimum Operations to Connect Hospitals**

**Difficulty:** Medium
**Accuracy:** 58.54%
**Submissions:** 4K+
**Points:** 4

---

## **Problem Statement**

You are given an undirected network of **V hospitals** numbered from **0 to V−1**, represented as a 2D array `edges[][]`, where each element `edges[i] = [u, v]` denotes a direct connection between hospital **u** and hospital **v**.

In **one operation**, you are allowed to:

* **Remove** any existing link, and
* **Reconnect** it between two hospitals that are currently **not directly or indirectly connected**.

Your task is to determine the **minimum number of operations** required to make sure that **all hospitals become connected**, either directly or indirectly, using the given links.

> **Note:**
> If it is impossible to connect all hospitals into a single network, return **-1**.

---

## **Examples**

---

### **Example 1**

**Input:**

```
V = 4, E = 3
edges[][] = [
  [0, 1],
  [0, 2],
  [1, 2]
]
```

**Output:**

```
1
```

**Explanation:**
Remove the connection between hospitals **1 and 2**, and use that link to connect hospitals **1 and 3**.

---

### **Example 2**

**Input:**

```
V = 5, E = 4
edges[][] = [
  [0, 1],
  [0, 2],
  [2, 3],
  [3, 4]
]
```

**Output:**

```
0
```

**Explanation:**
All hospitals are already connected directly or indirectly.
No rearrangement of connections is required.

---

## **Constraints**

* `1 ≤ V ≤ 10³`
* `0 ≤ E ≤ V*(V−1)/2`
* `0 ≤ edges[i][0], edges[i][1] < V`

---

## **Expected Complexities**

* **Time Complexity:** `O(V + E)`
* **Auxiliary Space:** `O(V + E)`

---

## **Company Tags**

* Amazon
* Microsoft
* Intuit
* Salesforce
* IBM

---

## **Topic Tags**

* Graph
* Disjoint Set
* Algorithms

---

## **Related Articles**

* [*Minimize Count Of Connections Required To Be Rearranged To Make All The Computers Connected*](https://www.geeksforgeeks.org/minimize-count-of-connections-required-to-be-rearranged-to-make-all-the-computers-connected/)

---

---

I’ll break it into:

1. Intuition + step-by-step dry run
2. Python solutions (DSU / Union-Find + a simple DFS variant) in your format
3. Interview memory tricks + typical Q&A

---

## 2. Intuition & Step-by-Step Explanation

### Rephrase the problem

* We have **V hospitals (0..V-1)** and **E undirected links**.
* In **one operation** we can:

  * remove an existing link, and
  * reconnect that *same* link between two hospitals that are not already in the same connected component.
* Goal: **minimum operations** to make the entire graph a **single connected component**.
* If impossible → return **-1**.

Key idea:
A connected graph with V nodes needs **at least V−1 edges** (a tree).
Any extra edge beyond that creates a **cycle**. Edges in cycles are **redundant** and can be repurposed.

So:

1. We need the number of **connected components** = `components`.
2. To connect `components` components, we need at least `components - 1` new links.
3. We can create these new links only by **reusing redundant edges** (edges that were part of cycles).
4. If `redundantEdges >= components - 1` → answer is `components - 1`.
   Else → `-1`.

Perfect fit for **Disjoint Set Union (DSU / Union-Find)**.

---

### Dry Run – Example 1

Input:

```text
V = 4
edges = [[0, 1], [0, 2], [1, 2]]
```

Graph:

* 0 connected to 1 and 2
* 1 connected to 2 (triangle among {0,1,2})
* Node 3 is isolated

#### DSU setup

`parent = [0, 1, 2, 3]`
Each node is its own component.

Let:

* `components = V = 4`  (initially each node separate)
* `redundant = 0`

We process each edge:

---

1. Edge `[0,1]`

* Find(0) = 0, Find(1) = 1 → **different components**.
* We **union(0,1)**:

  * After union, say parent of 1 becomes 0.
* `components` becomes 3.
* Edge is **used to connect**, not redundant.

State:

* parent ~ `{0:0, 1:0, 2:2, 3:3}`
* `components = 3`, `redundant = 0`

---

2. Edge `[0,2]`

* Find(0) = 0, Find(2) = 2 → **different**.
* Union(0,2):

  * parent[2] becomes 0.
* `components` becomes 2.

State:

* `{0:0, 1:0, 2:0, 3:3}`
* `components = 2`, `redundant = 0`

Now hospitals {0,1,2} in one component, 3 alone.

---

3. Edge `[1,2]`

* Find(1) → 0
* Find(2) → 0
* **Same component** → this edge forms a **cycle**.
* We **cannot decrease components** anymore; instead this edge is **redundant**.

So:

* `redundant = 1`
* `components = 2` (unchanged)

---

After all edges:

* Number of components = 2  → we need `components - 1 = 1` new link.
* We have `redundant = 1` spare edge.
* Since `redundant >= components - 1`, it **is possible**.

Minimum operations = `components - 1 = 1`.

Interpretation: remove `[1,2]` and reconnect as `[1,3]`.

Matches the example.

---

### Quick check – Example 2

```text
V = 5
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
```

This is already a simple chain:

`0–1`, `0–2–3–4`

Processing with DSU:

* Each edge connects different components, no cycles.
* `components` goes from 5 → 1.
* `redundant = 0`.

Now:

* `components - 1 = 0`, `redundant = 0`
* We already have a single component → **0 operations**.

---

## 3. Python Solutions

### 3.1 Optimized DSU / Union-Find Solution (recommended in interviews)

```python
from typing import List

class Solution:
    def minConnect(self, V: int, edges: List[List[int]]) -> int:
        """
        Minimum operations to connect all hospitals into a single component,
        given that we can remove any existing edge and reconnect it elsewhere.

        Approach (Union-Find / Disjoint Set):
        -------------------------------------
        - Treat each hospital as a node in an undirected graph.
        - As we add edges:
            * If edge connects two DIFFERENT components => we UNION them.
            * If edge connects two nodes in the SAME component => it's REDUNDANT.
        - After processing all edges:
            components = number of DSU roots
            redundant = count of redundant edges
        - To connect `components` components, we need `components - 1` edges.
        - If `redundant >= components - 1`:
              return components - 1
          else:
              return -1

        Time Complexity:
            - DSU 'find'/'union' with path compression + union-by-size:
              ~ O(α(V)) per operation (α = inverse Ackermann, almost constant).
            - We process E edges => O((V + E) * α(V)) ≈ O(V + E).
        Space Complexity:
            - parent + size arrays: O(V).
        """

        # ---------- Disjoint Set / Union-Find implementation ----------
        parent = list(range(V))
        size = [1] * V     # or rank, both fine

        def find(x: int) -> int:
            """
            Find with path compression.
            Amortized time ~ O(α(V)).
            """
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            """
            Union by size.
            Returns True if a merge happened (distinct components),
            False if x and y were already in the same component.
            """
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False  # no merge; edge is redundant

            # Attach smaller tree under larger
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            size[root_x] += size[root_y]
            return True

        # Initially each node is its own component
        components = V
        redundant = 0

        # Process all edges
        # Time: O(E * α(V)) ~ O(E)
        for u, v in edges:
            if union(u, v):
                # merged two components → one less component now
                components -= 1
            else:
                # Did not merge → edge is inside same component => redundant
                redundant += 1

        # Need (components - 1) edges to connect all components
        required = components - 1

        # If we have enough redundant edges, we can rewire them
        if redundant >= required:
            return required
        else:
            return -1
```

---

### 3.2 Alternative using DFS / BFS (conceptually simple)

Here we:

1. Build adjacency from all given edges.
2. Run DFS/BFS to count **components**.
3. Count **redundant edges** with formula:

   * A forest with `V` nodes and `components` trees has exactly `V - components` edges.
   * So any extra edges are `redundant = E - (V - components)`.

Same decision rule as before.

```python
from typing import List
from collections import defaultdict, deque

class SolutionDFS:
    def minConnect(self, V: int, edges: List[List[int]]) -> int:
        """
        Alternative solution using DFS to find number of components
        and a simple formula for redundant edges.

        Steps:
        ------
        1) Build adjacency list for the entire graph.
        2) Run DFS/BFS to count how many connected components we have.
        3) Let components = C.
           A spanning forest on V nodes and C components needs (V - C) edges.
           But we actually have E edges.
           So redundantEdges = E - (V - C).
        4) To connect C components, we need (C - 1) edges.
           If redundantEdges >= C - 1, answer = C - 1; else -1.

        Time Complexity:
            - Build adjacency: O(E)
            - DFS/BFS over all nodes/edges: O(V + E)
            => Total: O(V + E)
        Space Complexity:
            - Adjacency list + visited: O(V + E)
        """

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * V

        def bfs(start: int):
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)

        # Count connected components
        components = 0
        for node in range(V):
            if not visited[node]:
                components += 1
                bfs(node)

        E = len(edges)
        # edges needed in a spanning forest of C components
        min_edges_for_forest = V - components
        redundant_edges = E - min_edges_for_forest

        required = components - 1
        if redundant_edges >= required:
            return required
        else:
            return -1
```

In interviews, the **DSU version** is usually preferred because:

* It directly counts redundant edges as we go.
* It’s a classic pattern for similar problems (“Make Graph Connected”, etc.).

---

## 4. Interview Cheat Sheet

### 4.1 Core pattern to remember

**Phrase to memorize:**

> **“Components minus one, paid for by extra edges.”**

Concrete mental steps:

1. **Use DSU** to merge endpoints of every edge.
2. If an edge connects already-connected nodes → **redundant++**.
3. Track `components` = number of disjoint sets.
4. To fully connect: need `components - 1` edges.
5. If `redundant >= components - 1` → answer is `components - 1`; else `-1`.

You can rehearse this tiny **5-line pseudo-code**:

```text
components = V
redundant = 0
for each edge (u,v):
    if union(u,v) merged: components--
    else: redundant++

need = components - 1
if redundant >= need: return need
else: return -1
```

That’s the entire logic.

---

### 4.2 60-second explanation you can say out loud

> “We have an undirected graph and we can remove and reattach edges. Any edge that lies on a cycle is effectively spare, because we can delete it without disconnecting that component and reattach it somewhere else.
> I use a Disjoint Set Union structure to process each edge. When an edge connects two different components, I merge them and decrease the component count. When it connects two nodes already in the same set, it’s a redundant edge I can reuse.
> At the end, if there are `C` components, I need at least `C−1` links to fully connect the graph. If I have at least `C−1` redundant edges, I can rewire them, so the answer is `C−1`. Otherwise it’s impossible, and I return `-1`.
> DSU gives almost O(1) per edge, so the total time is O((V + E) α(V)) ≈ O(V + E).”

---

### 4.3 Likely Interview Questions & Strong Answers

---

**Q1. Why do you use DSU / Union-Find here?**

> DSU is ideal when we repeatedly ask “Are these two nodes already connected?” and “If not, connect them.”
> It lets me detect whether an edge forms a cycle in almost O(1) time. That’s exactly what I need to distinguish **useful** edges (that connect components) from **redundant** ones (within a component).

---

**Q2. Why is the answer `components - 1` when possible?**

> To connect `C` disconnected components into a single connected component, we need at least `C−1` edges: that’s the size of a spanning tree on `C` super-nodes. Each added edge merges two components, so with `C−1` edges we can connect them all, and it’s also necessary—you can’t connect `C` parts with less than `C−1` edges.

---

**Q3. How do you know how many redundant edges you have?**

> When I process an edge `(u, v)`:
>
> * If `find(u) != find(v)`, I union them; that edge reduces the component count.
> * If `find(u) == find(v)`, the edge is inside a single component and creates a cycle; removing it wouldn’t disconnect anything. That edge is counted as **redundant**.
>   So by counting such cycle edges, I know how many edges I’m free to rewire.

---

**Q4. What’s the time and space complexity of your solution?**

> With DSU using path compression and union-by-size/rank, each `find`/`union` is amortized O(α(V)), where α is the inverse Ackermann function (practically constant).
> We do at most one union per edge, so the total time is `O((V + E) * α(V))`, which is effectively linear in practice.
> Space is `O(V)` for the DSU arrays, plus `O(E)` if we also keep adjacency, but my final solution only needs the edge list and DSU, so `O(V)` extra space.

---

**Q5. What if there are fewer edges than V−1 at the start?**

> If `E < V−1`, it’s impossible to have a connected graph, even if we rearrange edges, because you need at least `V−1` edges for any connected graph with V nodes.
> DSU would eventually also show `redundant = 0` and `components > 1`. Then `components - 1 > redundant`, so the function returns `-1`.

---

**Q6. Could you solve this without DSU?**

> Yes. You can run DFS/BFS to count the connected components `C`.
> A forest with `V` nodes and `C` components has exactly `V−C` edges.
> If we actually have `E` edges, then the number of redundant edges is `E − (V−C)`.
> If this number is at least `C−1`, we can connect all; otherwise we can’t.
> That’s O(V+E) with slightly more math instead of on-the-fly DSU.

---

---

Great, let’s lock this one in your brain.

---

## 5. Real-World Use Cases (easy to explain to interviewer)

Think: **network of things + limited ability to add new cables, but we can rewire existing ones.**

### a) Hospital / Clinic Network Cabling (exact story of the problem)

* Each hospital = node, network cable = edge.
* Laying a *new* cable is expensive, but you can **unplug a cable and plug it elsewhere** at small cost.
* You want **all hospitals connected** (for record sharing, telemedicine, etc.).
* Some cables form **loops** between already-connected hospitals → these are **spare cables**.
* Question: *Are there enough spare cables to connect every isolated region into one network? If yes, what’s the minimum rewires?*

Perfect match to this problem.

---

### b) Corporate Office Network / LAN

* Offices (or floors) are nodes; Ethernet links are edges.
* Some floors are connected in rings (redundant topology), other floors are isolated.
* You’re allowed to **remove** cables from redundant rings and **reuse** them to connect isolated segments.
* Want to know minimum **rewiring operations** to make the whole office LAN connected.

---

### c) Computer Clusters or Data Centers

* Servers or racks are nodes; direct connections are edges.
* A data center may have **clusters** that are internally over-connected (many cycles), and some other racks that are disconnected.
* Instead of buying new switches/cables, you want to know if you can **repurpose redundant links** to get a fully connected topology.

---

### d) Social / Collaboration Networks with Limited Partnerships

* Think of teams, departments, or labs as nodes and active collaborations as edges.
* Some groups collaborate in dense clusters (cycles), others are isolated.
* You can “reassign” a collaboration from one pair to another (i.e., move resources).
* You want to know **minimum collaboration shifts** to make sure everyone is at least indirectly connected.

Mentioning any of these quickly in an interview shows you understand the *structure* of the problem, not just the code.

---

## 6. Full Python Program with Timing & Complexity Comments

Below is a **standalone script** using the **DSU approach** (the one you should present in interviews).

* Includes:

  * Full `Solution` class in the requested format.
  * Inline comments with time/space complexity at each major step.
  * A `main` block with example input.
  * Timing via `timeit.default_timer`.

```python
"""
Minimum Operations to Connect Hospitals
---------------------------------------

We have V hospitals (0 .. V-1) and E undirected edges "edges",
where edges[i] = [u, v] is a direct connection between u and v.

In one operation, we can remove an existing edge and reconnect it
between two *currently disconnected* hospitals.

Goal:
    Find the minimum number of such operations required to connect
    all hospitals into a single network (i.e., the graph becomes connected).
    Return -1 if this is impossible.

Core Idea (Union-Find / DSU):
    - A connected graph with V nodes needs at least (V - 1) edges.
    - Any extra edges beyond this are "redundant" (they form cycles)
      and can be repurposed elsewhere.
    - Use DSU to:
        * Count the number of connected components (C).
        * Count the number of redundant edges.
    - To connect C components we need (C - 1) edges.
    - If redundant_edges >= (C - 1) -> answer = (C - 1)
      else -> -1.

Asymptotic Complexity:
    Time:  O((V + E) * α(V))  ~ O(V + E)  (α is inverse Ackermann)
    Space: O(V)  for DSU arrays, plus the given edges.
"""

from typing import List
from timeit import default_timer as timer


class Solution:
    def minConnect(self, V: int, edges: List[List[int]]) -> int:
        """
        Compute the minimum number of operations to connect all hospitals.

        Parameters
        ----------
        V : int
            Number of hospitals (nodes)
        edges : List[List[int]]
            List of undirected edges [u, v]

        Returns
        -------
        int
            Minimum number of operations needed, or -1 if impossible.

        Detailed Complexity
        -------------------
        - DSU initialization:
              parent, size arrays -> O(V) time, O(V) space
        - For each edge, we do at most one union + a few finds:
              E edges -> O(E * α(V)) time (almost linear)
        - Overall:
              Time  = O((V + E) * α(V))  ≈ O(V + E)
              Space = O(V)
        """

        # ------------------- Disjoint Set (Union-Find) --------------------

        # parent[i] = parent of node i in the DSU forest
        # Initially each node is its own parent.
        parent = list(range(V))      # Time: O(V), Space: O(V)

        # size[i] = size of the tree whose root is i
        size = [1] * V               # Time: O(V), Space: O(V)

        def find(x: int) -> int:
            """
            Find the representative (root) of set containing x.
            Uses path compression to flatten the tree.

            Amortized time: O(α(V)), almost constant.
            """
            if parent[x] != x:
                parent[x] = find(parent[x])   # path compression
            return parent[x]

        def union(x: int, y: int) -> bool:
            """
            Union the sets containing x and y.
            Uses union-by-size to keep trees shallow.

            Returns:
                True  if a merge happened (two different components joined).
                False if x and y were already in the same component.
            """
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                # Already in same component -> edge is redundant
                return False

            # Attach smaller tree under larger tree root
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            size[root_x] += size[root_y]
            return True

        # ------------------- Main logic using DSU ------------------------

        components = V   # start with V isolated nodes
        redundant = 0    # count of edges that form cycles

        # Process each edge in the graph
        # Time: O(E * α(V))
        for u, v in edges:
            if union(u, v):
                # Edge connected two previously separate components
                components -= 1
            else:
                # Edge is inside the same component (cycle) -> redundant
                redundant += 1

        # To connect 'components' disconnected parts, we need (components - 1) edges
        required_edges = components - 1

        # If we have enough redundant edges, we can rewire them
        if redundant >= required_edges:
            return required_edges
        else:
            return -1


# ---------------------------- Example + Timing ----------------------------

if __name__ == "__main__":
    # Example 1 from the problem statement
    V = 4
    edges = [
        [0, 1],
        [0, 2],
        [1, 2]
    ]

    print("Input:")
    print("V     =", V)
    print("edges =", edges)

    # Time the method for this input
    start_time = timer()
    sol = Solution()
    result = sol.minConnect(V, edges)
    end_time = timer()

    print("\nOutput:")
    print("Minimum operations to connect all hospitals:", result)

    elapsed = end_time - start_time
    print("\nElapsed time (seconds):", elapsed)
```

If you run this program, you’ll get something like:

```text
Input:
V     = 4
edges = [[0, 1], [0, 2], [1, 2]]

Output:
Minimum operations to connect all hospitals: 1

Elapsed time (seconds): 2.8e-05
```

(Time will vary slightly, but will be tiny.)

