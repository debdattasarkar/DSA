Below is a **complete README-style conversion** of the entire problem statement from your screenshot.
✨ *No content omitted. Everything converted into clean and structured Markdown.*

---

# Maximum Stone Removal 🪨

**Difficulty:** Medium
**Accuracy:** 49.82%
**Submissions:** 20K+
**Points:** 4
**Average Time:** 30m

---

## 🧩 Problem Statement

Given a 2D array of non-negative integers `stones[][]` where `stones[i] = [xi, yi]` represents the location of the `i`-th stone on a 2D plane, the task is to return the **maximum possible number of stones that you can remove**.

A stone **can be removed** if it shares either the **same row** or the **same column** as another stone that has **not** been removed.

📌 **Note:**
Each coordinate point may have at most one stone.

---

## 🧪 Examples

---

### **Example 1**

**Input:**

```
stones[][] = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
```

**Output:**

```
5
```

### Explanation:

```
0   1   2
------------
| S | S |   |   row 0
| S |   | S |   row 1
|   | S | S |   row 2
```

One way to remove **5 stones** is as follows:

1. Remove stone `[2, 2]` because it shares the same row as `[2, 1]`.
2. Remove stone `[2, 1]` because it shares the same column as `[0, 1]`.
3. Remove stone `[1, 2]` because it shares the same row as `[1, 0]`.
4. Remove stone `[1, 0]` because it shares the same column as `[0, 0]`.
5. Remove stone `[0, 1]` because it shares the same row as `[0, 0]`.

Stone `[0, 0]` **cannot** be removed since it does not share any row/column with another stone still on the plane.

---

### **Example 2**

**Input:**

```
stones[][] = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
```

**Output:**

```
3
```

### Explanation:

```
0   1   2
------------
| S |   | S |   row 0
|   | S |   |   row 1
| S |   | S |   row 2
```

One way to remove **3 stones** is as follows:

1. Remove stone `[2, 2]` because it shares the same row as `[2, 0]`.
2. Remove stone `[2, 0]` because it shares the same column as `[0, 0]`.
3. Remove stone `[0, 2]` because it shares the same row as `[0, 0]`.

Stones `[0, 0]` and `[1, 1]` cannot be removed since they do not share any row/column with another stone still present.

---

## 📏 Constraints

* `1 ≤ stones.size() ≤ 1000`
* `0 ≤ xi, yi ≤ 10⁴`
* No two stones are at the same position.

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

---

I’ll break this into:

1. Text explanation + core idea
2. Step-by-step dry run
3. Python solutions (brute DFS + optimized DSU), in your requested format
4. Interview “memory hooks” + common Q&A

---

## 1️⃣ Intuition + Explanation

We are given `n` stones, each at `(x, y)` on a grid.

* You can **remove a stone** if there is **another stone** in the same **row** or **column** that is still on the board.
* We want to remove the **maximum** number of stones.

### Key Observation

Think of each stone as a **node in a graph**:

* There is an **edge** between two stones if they share **row** or **column**.

Then:

* In one **connected component** (cluster of stones connected via rows/columns),
  you can keep removing stones as long as there are **≥ 2** stones left in that component.
* Eventually, each connected component must be left with **exactly 1 stone** (no more moves possible).

👉 So for a component with `k` stones, we can remove `k - 1` stones.

If there are `C` connected components in total, and `N` stones:

[
\text{Answer} = N - C
]

So the whole problem becomes:

> **Count how many connected components there are in this “shares row/column” graph.**

We’ll do that either by:

* DFS/BFS on stones (brute but OK for n ≤ 1000), or
* DSU (Disjoint Set Union / Union-Find) using rows and columns as nodes (more scalable & interview-friendly).

---

## 2️⃣ Step-by-Step Dry Run (DFS idea)

Use the first example:

```python
stones = [
    [0, 0],  # S0
    [0, 1],  # S1
    [1, 0],  # S2
    [1, 2],  # S3
    [2, 1],  # S4
    [2, 2],  # S5
]
N = 6
```

We build a graph: stones are nodes, edges between stones sharing row or column.

We won’t explicitly build an adjacency matrix; we’ll just determine neighbors on the fly (check all other stones).

### DFS to count components

Maintain:

* `visited = [False] * N`
* `components = 0`

#### Start with i = 0  (stone S0 at [0,0])

* `visited[0]` is False → new component.
* `components = 1`
* Start DFS(0):

  * Mark `visited[0] = True`
  * For every other stone `j`:

    * `j = 1`: `[0,1]` shares **row 0** → neighbor. DFS(1)
    * `j = 2`: `[1,0]` shares **column 0** → neighbor. DFS(2)
    * `j = 3`: `[1,2]` does not share row/column with `[0,0]` → skip.
    * `j = 4`: `[2,1]` no common row/column → skip.
    * `j = 5`: `[2,2]` no common row/column → skip.

  **DFS(1)** (stone `[0,1]`):

  * `visited[1] = True`
  * Check neighbors:

    * `j = 0` already visited.
    * `j = 2`: `[1,0]` no same row/column.
    * `j = 3`: `[1,2]` no same row/column.
    * `j = 4`: `[2,1]` shares **column 1** → DFS(4)
    * `j = 5`: `[2,2]` no same row/column.

  **DFS(4)** (stone `[2,1]`):

  * `visited[4] = True`
  * Check neighbors:

    * `j = 0`: `[0,0]` no row/column
    * `j = 1`: `[0,1]` same column 1 → already visited
    * `j = 2`: `[1,0]` no row/column
    * `j = 3`: `[1,2]` no row/column
    * `j = 5`: `[2,2]` shares **row 2** → DFS(5)

  **DFS(5)** (stone `[2,2]`):

  * `visited[5] = True`
  * Check neighbors:

    * `j = 0`: no row/column
    * `j = 1`: no row/column
    * `j = 2`: no row/column
    * `j = 3`: `[1,2]` shares **column 2** → DFS(3)
    * `j = 4`: already visited

  **DFS(3)** (stone `[1,2]`):

  * `visited[3] = True`
  * Check neighbors:

    * `j = 0`: no row/column
    * `j = 1`: no row/column
    * `j = 2`: `[1,0]` shares **row 1** → DFS(2)
    * `j = 4`, `j = 5`: already visited or no new link.

  **DFS(2)** (stone `[1,0]`):

  * `visited[2] = True`
  * Neighbors: `[0,0]` (same column 0), `[1,2]` (same row 1), but both already visited.

End of DFS(0): we have visited **all stones** (indices 0..5).

#### Continue outer loop

* i from 1 to 5 → every stone already visited → no new component.

So:

* `components = 1`
* `N = 6`
* Answer = `N - components = 6 - 1 = 5`

Which matches the problem’s answer.

---

## 3️⃣ Python Solutions

We’ll implement `class Solution: def maxRemove(self, stones): ...` as requested.

### 3.1 Brute but clean DFS solution (O(n²))

**Idea:**

* Build an implicit graph: stones are nodes.
* Two nodes connected if same row or same column.
* Count connected components via DFS/BFS (checking neighbors by looping all stones).
* Result = `len(stones) - components`.

This is very interview-acceptable for `n ≤ 1000` and easy to remember.

```python
class Solution:
    def maxRemove(self, stones):
        """
        Brute-force graph + DFS
        Time: O(n^2) because for each stone we may compare with all others.
        Space: O(n) for visited array and recursion stack.
        """
        n = len(stones)
        visited = [False] * n

        def are_connected(i, j):
            """Return True if stone i and j share same row or same column."""
            return (
                stones[i][0] == stones[j][0] or  # same row
                stones[i][1] == stones[j][1]     # same column
            )

        def dfs(start_index):
            """Mark all stones in the same connected component as visited."""
            stack = [start_index]
            visited[start_index] = True

            while stack:
                current = stack.pop()
                # Try to connect to every other stone
                for neighbor in range(n):
                    if not visited[neighbor] and are_connected(current, neighbor):
                        visited[neighbor] = True
                        stack.append(neighbor)

        component_count = 0

        for i in range(n):
            if not visited[i]:
                component_count += 1
                dfs(i)

        # In each component with k stones, we can remove k - 1 stones.
        # So total removable stones = total_stones - number_of_components.
        return n - component_count
```

This is the “easy to code on the whiteboard” version.

---

### 3.2 Optimized DFS using row/column maps (still O(n²) worst-case, but faster in practice)

Instead of checking **every** other stone, we map:

* `row → list of indices in that row`
* `col → list of indices in that column`

Then during DFS you only jump along same row/same column lists.

```python
from collections import defaultdict, deque

class Solution:
    def maxRemove(self, stones):
        """
        Graph + BFS with row/column maps.
        Still O(n^2) worst-case, but usually much faster.
        """
        n = len(stones)
        visited = [False] * n

        # Build maps from row and column to indices of stones
        row_to_indices = defaultdict(list)
        col_to_indices = defaultdict(list)
        for index, (row, col) in enumerate(stones):
            row_to_indices[row].append(index)
            col_to_indices[col].append(index)

        def bfs(start_index):
            queue = deque([start_index])
            visited[start_index] = True

            while queue:
                current = queue.popleft()
                r, c = stones[current]

                # All stones in the same row
                for neighbor in row_to_indices[r]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

                # All stones in the same column
                for neighbor in col_to_indices[c]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        component_count = 0
        for i in range(n):
            if not visited[i]:
                component_count += 1
                bfs(i)

        return n - component_count
```

---

### 3.3 DSU / Union-Find over rows and columns (optimized & very interview-friendly)

**Key trick:**

* Instead of treating each stone as a node, treat each **row** and each **column** as nodes.
* For stone at `(x, y)`:

  * Union node `row_x` with node `col_y`.
* All stones whose rows/columns are connected form **one component**.
* Number of components = number of distinct roots among all used row/column nodes.

Then answer:

[
\text{removable stones} = N - \text{components}
]

Why? Because each connected row/column component corresponds to one connected stone component.

We need to map rows and columns to **disjoint sets**:

* Row IDs: `0 .. max_row`
* Column IDs: `offset + 0 .. offset + max_col`

```python
class Solution:
    def maxRemove(self, stones):
        """
        Union-Find / DSU solution.
        Time: O(n * α(n)) ~ O(n)
        Space: O(U) where U is number of distinct rows + columns used.
        """
        if not stones:
            return 0

        # Find maximum row index to set offset for columns
        max_row = max(x for x, _ in stones)
        offset = max_row + 1  # columns will start from this index

        # DSU: parent and rank dictionaries (sparse, only for used nodes)
        parent = {}
        rank = {}

        def find(node):
            # Create node lazily if not present
            if node not in parent:
                parent[node] = node
                rank[node] = 0
            # Path compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            # Union by rank
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        # Set of all nodes (rows and columns) that are actually used
        used_nodes = set()

        for row, col in stones:
            row_node = row                   # keep row as is
            col_node = offset + col         # shift column to avoid clash
            union(row_node, col_node)
            used_nodes.add(row_node)
            used_nodes.add(col_node)

        # Count distinct roots (connected components) among used nodes
        root_set = set()
        for node in used_nodes:
            root_set.add(find(node))

        number_of_components = len(root_set)
        total_stones = len(stones)

        return total_stones - number_of_components
```

This version is what many interviewers love, because:

* It scales better
* Shows you know DSU
* Uses the elegant rows/columns trick.

---

## 4️⃣ Interview Strategy: How to Recall & Explain

### Mental steps you can follow in the interview

1. **Rephrase the problem out loud**

   > “We can remove a stone if it has another stone in its row or column. Eventually, we get stuck when each remaining stone is isolated.”

2. **Graph modeling**

   > “Let’s treat each stone as a node in a graph. Two stones are connected if they share row or column.”

3. **Component insight**

   > “Within one connected component with `k` stones, we can always remove `k - 1` and leave one stone. So the maximum removable stones = total stones − number of components.”

4. **Plan for counting components**

   * Approach A (simpler): DFS/BFS over all stones → O(n²) (checking all pairs).
   * Approach B (nice): DSU on rows and columns.

5. **State complexity**

   * DFS: `O(n²)` time, `O(n)` space — OK for `n ≤ 1000`.
   * DSU: near `O(n)` time, `O(n)` space.

If you narrate these steps, the interviewer sees good reasoning immediately.

---

### Common Interview Q&A for this Problem

**Q1. How did you come up with `answer = N - components`?**

> In each connected component (cluster of stones that are linked via shared rows/columns), as long as there are at least two stones, you can remove one that shares a row/column with another. You can keep doing this until only **one stone** remains in that component.
> So a component of size `k` yields `k - 1` removable stones.
> Summing over all components:
> [
> \sum (k_i - 1) = \left( \sum k_i \right) - \text{number_of_components} = N - C
> ]

---

**Q2. Why do you model this as a graph problem?**

> The removal rule is based on **relationships** (“shares row or column”). This is naturally a graph: stones are nodes, edges represent that relationship.
> Once modeled as a graph problem, many operations like counting components become standard via DFS/BFS/Union-Find.

---

**Q3. What is the time and space complexity of your DFS solution?**

> * We explore neighbors by comparing a stone to all others → `O(n)` per stone in the worst case.
> * Overall `O(n²)` time, `O(n)` space (visited array + recursion/stack).
>   Given `n ≤ 1000`, `n² = 10^6` operations, which is fine.

---

**Q4. Can we optimize it further?**

> Yes, we can. Instead of comparing with all stones directly, we can use:
>
> * `row → list of stones`
> * `col → list of stones`
>
> Or even better, build a **Union-Find** structure where:
>
> * Each row and each column is a node.
> * For stone `(x, y)`, we union row `x` with column `y`.
>   Then we count how many disjoint sets there are among used rows/columns.

---

**Q5. Explain the DSU idea more clearly.**

> If two stones share a row, their row nodes are the same, so they’re connected through that row.
> If they share a column, their column nodes are the same.
> When we connect `row_x` with `col_y` for each stone `(x, y)`, all stones in the same logical component will be inside the same DSU set.
> Counting distinct DSU parents among all used rows/columns gives the number of connected components.
> Finally, answer = total stones − number of these components.

---

**Q6. Why do you shift the column IDs (`offset + col`)?**

> Rows and columns might have the same numeric value (e.g., row 0 and column 0), but they are logically different nodes.
> To avoid collision, I map:
>
> * row `r` → `r`
> * column `c` → `offset + c`
>   where `offset = max_row + 1`.
>   That guarantees all column IDs are distinct from all row IDs.

---

**Q7. What if the constraints were much higher (e.g., n = 10^5)?**

> The `O(n²)` DFS would not work; we must avoid pairwise comparisons.
> We would prefer:
>
> * DSU on rows and columns, or
> * Map from row and column to adjacency lists and run BFS.
>   DSU is especially nice because each union/find operation is almost `O(1)` amortized.

---

**Q8. How would you handle recursion depth in Python?**

> For DFS I would likely use an **iterative DFS/BFS with a stack/queue** instead of recursion to avoid maximum recursion depth issues, especially if `n` could be large.
> In the DSU approach there is no recursion during traversal, only union-find operations.

---

---

Let’s add the last pieces:

---

## 5️⃣ Real-World Use Cases (easy to explain in an interview)

You don’t have to force a “stones on grid” analogy; just map it to **connected components where you can safely remove all but one element per component**.

Here are a few crisp, relatable examples:

1. **Data center / server racks (rows & columns)**

   * Each stone = a **server** at `(rack, row)` in a data center.
   * Servers in the same rack (row) or same power line / network switch (column) are “connected”.
   * You want to **decommission as many redundant servers as possible**, but each connected group must keep at least one server alive for redundancy.
   * Maximum removable servers = total servers − number of connected groups.

2. **Social groups & deduplication**

   * Each stone = a **user**.
   * Row = city, column = company (for example).
   * If two users share a city or company, they’re part of the same “reach” group.
   * When doing marketing or sampling, you might want to **keep only one representative** per connected group to reduce redundancy while preserving coverage.
   * The algorithm tells you how many users you can safely drop.

3. **Sensor network consolidation**

   * Each stone = a sensor, placed in a grid of zones & layers (row = zone, column = layer).
   * Sensors that share a row or column can communicate/inter-relay data, forming a connected monitoring region.
   * For cost reduction, you can remove all but one sensor per connected region while keeping the **monitoring coverage**.

4. **Redundant database replicas across regions and racks**

   * Row = data center region, column = rack ID.
   * Each stone = a replica of a database.
   * As long as at least one replica per connected row/column group remains, data is still accessible.
   * We can remove `N - components` replicas and still have at least one copy per connected region.

These are quick and interviewer-friendly: you’re basically saying:

> “Any time we have **redundant items** connected by some sharing rule (same rack / same city / same network), and we can remove everything in a connected cluster except one, this problem applies.”

---

## 6️⃣ Full Python Program with Timing + Inline Complexity Comments

Below is a **self-contained script** using the **DSU (Union–Find)** solution, with:

* Clear variable names
* Inline comments describing **time & space** where it matters
* Example inputs (the two from the problem)
* Simple timing using `time.perf_counter()`

You can paste this into a file like `max_stone_removal.py` and run it directly.

```python
import time

class Solution:
    def maxRemove(self, stones):
        """
        Main function: returns maximum number of removable stones.

        Uses Disjoint Set Union (Union-Find) on rows and columns.

        Let n = number of stones, U = number of distinct rows + columns.

        Time Complexity:
            - For each stone we do 2 find() + 1 union() → O(alpha(U)) amortized.
            - Overall ≈ O(n * α(U)) ~ O(n) for all practical purposes.

        Space Complexity:
            - parent, rank maps and used_nodes set store at most U elements.
            - Overall O(U), typically O(n) because each stone introduces ≤ 2 nodes.
        """
        if not stones:
            return 0

        # 1️⃣ Compute an offset so row ids and column ids don't collide.
        #    We treat each row and each column as separate DSU nodes.
        #
        #    Complexity: O(n) to scan all stones once.
        max_row_index = max(x for x, _ in stones)
        col_offset = max_row_index + 1  # all columns will start from here

        # 2️⃣ DSU internal storage (sparse, using dicts instead of fixed arrays)
        parent = {}   # parent[node] = parent of node in DSU tree
        rank = {}     # rank[node] = approx depth for union-by-rank

        def find(node):
            """
            Find with path compression.

            Time (amortized): α(U) (inverse Ackermann, ~constant).
            Space: O(1) extra, but modifies parent dict in-place.
            """
            # Lazily initialize node if not present
            if node not in parent:
                parent[node] = node
                rank[node] = 0

            # Path compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            """
            Union two nodes by rank.

            Time (amortized): α(U)
            Space: O(1) extra.
            """
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return  # already in the same set

            # Union by rank keeps tree shallow → better find() performance.
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

        # 3️⃣ For each stone (row, col):
        #    - Create DSU nodes for row and column.
        #    - Union them.
        #
        #    Time: O(n * α(U))
        #    Space: O(U) for parent/rank + used_nodes.
        used_nodes = set()

        for row, col in stones:
            row_node = row               # use row index as is
            col_node = col_offset + col  # shift column index to avoid clash

            union(row_node, col_node)

            used_nodes.add(row_node)
            used_nodes.add(col_node)

        # 4️⃣ Count distinct DSU roots among all used nodes.
        #
        #    Time: O(U * α(U)) ~ O(U)
        #    Space: O(U) for root_set.
        root_set = set()
        for node in used_nodes:
            root_set.add(find(node))

        number_of_components = len(root_set)
        total_stones = len(stones)

        # 5️⃣ Formula: in each component of size k, you can remove k - 1 stones.
        #    So total removable = total_stones - number_of_components.
        #
        #    Time: O(1)
        #    Space: O(1)
        return total_stones - number_of_components


# ----------------------------------------------------------------------
# Demo + Timing
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Example 1
    stones_example_1 = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 2],
        [2, 1],
        [2, 2],
    ]  # Expected output: 5

    # Example 2
    stones_example_2 = [
        [0, 0],
        [0, 2],
        [1, 1],
        [2, 0],
        [2, 2],
    ]  # Expected output: 3

    solver = Solution()

    # Measure time for example 1
    start_time = time.perf_counter()
    result1 = solver.maxRemove(stones_example_1)
    end_time = time.perf_counter()
    elapsed_us1 = (end_time - start_time) * 1e6  # microseconds

    print("Example 1 Input:", stones_example_1)
    print("Example 1 Output:", result1)
    print(f"Example 1 Time taken: {elapsed_us1:.2f} µs\n")

    # Measure time for example 2
    start_time = time.perf_counter()
    result2 = solver.maxRemove(stones_example_2)
    end_time = time.perf_counter()
    elapsed_us2 = (end_time - start_time) * 1e6  # microseconds

    print("Example 2 Input:", stones_example_2)
    print("Example 2 Output:", result2)
    print(f"Example 2 Time taken: {elapsed_us2:.2f} µs")
```

### What this prints (conceptually)

When you run the script, you’ll see something like:

```text
Example 1 Input: [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
Example 1 Output: 5
Example 1 Time taken: 150.23 µs

Example 2 Input: [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
Example 2 Output: 3
Example 2 Time taken: 120.47 µs
```

(Times will vary per machine, but they’ll be tiny for such small inputs.)

If you want, I can also add:

* A quick **random test generator** to stress the function and time it on larger inputs.
* Or a **brute-force checker** to verify correctness against the DSU solution.
