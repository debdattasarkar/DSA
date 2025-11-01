
---

# 🎓 Course Schedule II

**Difficulty:** Medium
**Accuracy:** 51.77%
**Submissions:** 88K+
**Points:** 4
**Average Time:** 25m

---

## 📘 Problem Statement

You are given `n` courses, labeled from `0` to `n - 1` and a 2D array `prerequisites[][]`, where
`prerequisites[i] = [x, y]` indicates that we need to take course **y first** if we want to take course **x**.

Find the **ordering of courses** we should take to complete all the courses.

---

### 🧩 Important Note

There may be **multiple correct orders** — you only need to return any **one** of them.

If it is **impossible to finish** all tasks, return an **empty array**.

The driver code will print **true** if you return any **correct order** of courses; otherwise, it will print **false**.

---

## 🧠 Examples

### Example 1

**Input:**

```
n = 3  
prerequisites = [[1, 0], [2, 1]]
```

**Output:**

```
true
```

**Explanation:**
To take course `1`, you must finish course `0`.
To take course `2`, you must finish course `1`.
So the only valid order is `[0, 1, 2]`.

---

### Example 2

**Input:**

```
n = 4  
prerequisites = [[2, 0], [2, 1], [3, 2]]
```

**Output:**

```
true
```

**Explanation:**
Course `2` requires both `0` and `1`.
Course `3` requires course `2`.

Hence, both `[0, 1, 2, 3]` and `[1, 0, 2, 3]` are valid topological orderings.

---

## ⚙️ Constraints

```
1 ≤ n ≤ 10⁴  
0 ≤ prerequisites.size() ≤ 10⁵  
0 ≤ prerequisites[i][0], prerequisites[i][1] < n  
All prerequisite pairs are unique  
prerequisites[i][0] != prerequisites[i][1]
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n + m)   |
| **Auxiliary Space** | O(n + m)   |

---

## 🏢 Company Tags

`Google`

---

## 🧵 Topic Tags

`DFS` • `Graph` • `BFS` • `Data Structures` • `Algorithms`

---

## 🔗 Related Articles

* [Find Course Schedule I](https://www.geeksforgeeks.org/find-course-schedule-i/)
* [Find Whether It Is Possible To Finish All Tasks Or Not From Given Dependencies](https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/)

---

---

Classic **Course Schedule II** (return any valid order of courses).
Below you’ll get: a crisp intuition, a small dry run, two interview-ready solutions (BFS/Kahn and DFS topo) in your exact signature, plus a quick recall sheet and Q&A.

---

## 2) Intuition + step-by-step dry run

### Problem in one line

We have `n` courses `0..n-1`. Each prerequisite pair `[x, y]` means **y → x** (take `y` before `x`).
Return **any topological ordering** of this directed graph. If a cycle exists, return **[]**.

### Core idea

* This is the **topological sort** problem.
* Two standard ways:

  1. **BFS (Kahn’s Algorithm)** using **in-degrees**.
  2. **DFS** with **postorder** (and a 3-color cycle check).

Either one passes interviews. Kahn’s is usually the “easy & expected” route.

---

### Tiny dry run (Kahn’s Algorithm)

Input:

```
n = 4
prerequisites = [[2,0], [2,1], [3,2]]   # edges: 0→2, 1→2, 2→3
```

1. Build adjacency & in-degree

* adj[0] = [2], adj[1] = [2], adj[2] = [3]
* indeg = [0, 0, 2, 1]

2. Push all zero-in-degree nodes into queue: `q = [0, 1]`

3. Pop 0 → order = [0]

   * Decrease indeg[2] from 2→1

4. Pop 1 → order = [0, 1]

   * Decrease indeg[2] from 1→0 → push 2

5. Pop 2 → order = [0, 1, 2]

   * Decrease indeg[3] from 1→0 → push 3

6. Pop 3 → order = [0, 1, 2, 3]

7. Size of order == n → **valid**.
   If at the end order length < n, there’s a **cycle** → return `[]`.

---

## 3) Python solutions (brute-ish idea + the two standard, with clear comments)

### A) BFS Topological Sort (Kahn’s Algorithm) — **most expected**

```python
from collections import deque, defaultdict

class Solution:
    def findOrder(self, n, prerequisites):
        """
        Kahn's Algorithm (BFS over zero in-degree nodes).
        Steps:
          1) Build graph y->x for each [x,y]; compute in-degrees of x.
          2) Push all nodes with in-degree 0 to a queue.
          3) Repeatedly pop, append to order, and decrement neighbors' in-degrees.
          4) If a neighbor in-degree hits 0, push it.
          5) If we processed all n nodes -> order is valid; else -> cycle -> [].

        Time  : O(n + m)  where m=len(prerequisites)
        Space : O(n + m)  for adjacency + in-degree + queue + output
        """
        # 1) Build adjacency list and in-degree array
        adj = defaultdict(list)
        indeg = [0] * n
        for x, y in prerequisites:
            adj[y].append(x)     # y -> x
            indeg[x] += 1

        # 2) Queue of all zero in-degree nodes
        q = deque([i for i in range(n) if indeg[i] == 0])

        order = []
        # 3) BFS pop
        while q:
            u = q.popleft()
            order.append(u)
            # 4) Relax neighbors
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # 5) If we placed all courses, return order; else cycle -> []
        return order if len(order) == n else []
```

### B) DFS Topological Sort with 3-color cycle check — **equally standard**

```python
from collections import defaultdict

class SolutionDFS:
    def findOrder(self, n, prerequisites):
        """
        DFS with 3-color marking:
           0 = unvisited, 1 = visiting (in recursion stack), 2 = visited (done).
        If we ever see a neighbor with color=1, it's a cycle -> return [].
        Append node to output AFTER exploring neighbors (postorder), then reverse.

        Time  : O(n + m)
        Space : O(n + m)  recursion + graph + output
        """
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[y].append(x)  # y -> x

        color = [0] * n  # 0=white,1=gray,2=black
        order_post = []
        has_cycle = False

        def dfs(u):
            nonlocal has_cycle
            color[u] = 1      # entering
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                    if has_cycle:   # propagate early
                        return
                elif color[v] == 1:
                    has_cycle = True
                    return
            color[u] = 2      # exiting
            order_post.append(u)  # postorder push

        for node in range(n):
            if color[node] == 0:
                dfs(node)
                if has_cycle:
                    return []

        # reverse postorder = topological order
        return order_post[::-1]
```

### C) “Brute-ish” educational idea (not for production, but good to articulate)

Try to **greedily pick any course with all prereqs satisfied** using a loop that rescans the list (simulating indegrees without a queue). It’s `O(n^2 + m)` in worst case and less robust, so stick to A/B in interviews. (No code needed unless asked; just mention why Kahn’s is better.)

---

## 4) Interview quick-recall + Q&A

### 15-second recall (BFS/Kahn)

> “Compute in-degrees, queue all zeros, pop and append to answer while decrementing neighbor in-degrees; push new zeros. If we placed all `n`, done; else cycle → [].”

### 5-line pseudo (write from memory)

```
build adj + indeg
q = all nodes with indeg 0
while q: pop u; add u; for v in adj[u]: indeg[v]-=1; if indeg[v]==0: q.push(v)
if len(order)==n: return order
return []
```

### Mnemonics

* **“0-in first”** → start with nodes that depend on nobody.
* **“Pull & relax”** → pop a course and relax its dependents by 1.
* **“Empty or all?”** → if you can’t place all, there’s a cycle.

### High-yield Q&A

**Q1. Why does Kahn’s algorithm detect cycles?**
Because if a cycle exists, some nodes never reach in-degree 0. When the queue empties early, `len(order) < n`.

**Q2. Time/Space complexity?**
`O(n + m)` time to process all nodes/edges once; `O(n + m)` space for graph, indegrees, queue, and result.

**Q3. Why adjacency y→x (not x→y)?**
Because `[x, y]` means **y must be taken before x** (edge goes from prerequisite to dependent).

**Q4. What if multiple valid orders exist?**
Any is fine. Kahn’s order depends on queue order; using a min-heap yields lexicographically smallest if asked.

**Q5. When would you prefer DFS?**
When recursion is comfortable and you want explicit cycle detection (3-color). Both are accepted; BFS is often simpler to implement iteratively.

**Q6. What about disconnected graphs?**
Both methods handle them: Kahn’s starts with *all* zero-in-degree nodes; DFS iterates through all nodes.

---

---

Great—here are (5) crisp, interview-friendly use cases and then a **complete runnable script** for Course Schedule II (Kahn’s BFS + DFS), with inline complexity notes, sample inputs/outputs, and timings.

---

## 5) Real-World Use Cases (easy to relate)

1. **Build systems / CI pipelines**
   Compile targets depend on others; topological order gives a valid build sequence.

2. **Project planning (tasks with prerequisites)**
   Tasks (courses) depend on prior tasks; topo order is the schedule.

3. **Package managers / microservices rollout**
   Install/deploy artifacts only after their dependencies are present.

4. **Database migrations**
   Run schema changes in a dependency-respecting order (FKs before dependents).

5. **ML / Data pipelines (DAGs)**
   Feature jobs → model training → evaluation → deployment; execute nodes when inputs are ready.

---

## 6) Full program (BFS Kahn + DFS Topo) with timings

```python
#!/usr/bin/env python3
"""
Course Schedule II (Topological Sort)
-------------------------------------
We return any valid order of courses given prerequisite pairs [x, y] meaning y -> x.

We implement:
  * Solution (Kahn's BFS)   : O(n + m) time, O(n + m) space
  * SolutionDFS (DFS topo)  : O(n + m) time, O(n + m) space

We also:
  * validate an order against prerequisites
  * print sample outputs
  * show timings with perf_counter (single run) and timeit (average)
"""

from collections import deque, defaultdict
from time import perf_counter
import timeit
from typing import List, Tuple


# ------------------------------
# 1) Kahn's Algorithm (BFS)
# ------------------------------
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Kahn's algorithm:
          1) Build graph y->x for each [x, y], compute in-degree[x]  (O(n + m))
          2) Push all 0-in-degree nodes to queue                      (O(n))
          3) Pop -> append to order, decrement neighbors' in-degree   (O(n + m))
          4) Push neighbor when in-degree hits 0
        If we placed all n courses, return order; else cycle -> [].

        Time  : O(n + m)
        Space : O(n + m)
        """
        # Build adjacency & indegree  (O(n + m))
        adj = defaultdict(list)
        indeg = [0] * n
        for x, y in prerequisites:   # y must come before x  => edge y->x
            adj[y].append(x)
            indeg[x] += 1

        # Queue of sources (in-degree 0)  (O(n))
        q = deque([i for i in range(n) if indeg[i] == 0])

        order: List[int] = []
        # BFS over "ready" courses  (O(n + m))
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If all scheduled, success; else cycle -> []  (O(1))
        return order if len(order) == n else []


# ------------------------------
# 2) DFS Topological Sort
# ------------------------------
class SolutionDFS:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS with 3-color cycle detection:
            color[u]=0 unvisited, 1 visiting, 2 done.
        On back-edge to a gray node => cycle -> [].
        Push node after exploring neighbors (postorder), then reverse.

        Time  : O(n + m)
        Space : O(n + m) (graph + recursion + result)
        """
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[y].append(x)

        color = [0] * n  # 0=white, 1=gray, 2=black
        post: List[int] = []
        has_cycle = False

        def dfs(u: int) -> None:
            nonlocal has_cycle
            color[u] = 1
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                    if has_cycle:
                        return
                elif color[v] == 1:
                    has_cycle = True
                    return
            color[u] = 2
            post.append(u)

        for u in range(n):
            if color[u] == 0:
                dfs(u)
                if has_cycle:
                    return []
        return post[::-1]  # reverse postorder


# ------------------------------
# Utilities
# ------------------------------
def is_valid_order(n: int, prerequisites: List[List[int]], order: List[int]) -> bool:
    """Check that `order` respects all edges y->x (y appears before x).  O(n + m)."""
    if len(order) != n:
        return False
    pos = {course: i for i in range(n)}       # O(n)
    for x, y in prerequisites:                # O(m)
        if pos[y] > pos[x]:
            return False
    return True


def run_case(title: str, n: int, prerequisites: List[Tuple[int, int]]):
    print(f"\n-- {title} --")
    print("n =", n)
    print("prerequisites =", prerequisites)

    # Single-run timings
    t0 = perf_counter()
    ans_kahn = Solution().findOrder(n, prerequisites)
    t1 = perf_counter()

    t2 = perf_counter()
    ans_dfs = SolutionDFS().findOrder(n, prerequisites)
    t3 = perf_counter()

    print("Kahn order :", ans_kahn, " | valid:", is_valid_order(n, prerequisites, ans_kahn))
    print("DFS  order :", ans_dfs,  " | valid:", is_valid_order(n, prerequisites, ans_dfs))
    print(f"Single-run: Kahn { (t1 - t0)*1e6:.2f} µs | DFS { (t3 - t2)*1e6:.2f} µs")

    # Average timings with timeit (avoid including print costs)
    def call_kahn():
        Solution().findOrder(n, prerequisites)

    def call_dfs():
        SolutionDFS().findOrder(n, prerequisites)

    reps = 1000
    avg_kahn = timeit.timeit(call_kahn, number=reps) / reps
    avg_dfs  = timeit.timeit(call_dfs,  number=reps) / reps
    print(f"Avg over {reps} runs: Kahn {avg_kahn*1e6:.2f} µs/run | DFS {avg_dfs*1e6:.2f} µs/run")


# ------------------------------
# Demo / Main
# ------------------------------
def main():
    # Example 1 from prompt (only one valid order)
    n1 = 3
    pre1 = [(1, 0), (2, 1)]          # 0->1->2
    run_case("Example 1", n1, pre1)

    # Example 2 from prompt (multiple valid orders)
    n2 = 4
    pre2 = [(2, 0), (2, 1), (3, 2)]  # 0,1 -> 2 -> 3
    run_case("Example 2", n2, pre2)

    # Extra: has cycle -> should return []
    n3 = 3
    pre3 = [(0, 1), (1, 2), (2, 0)]  # cycle 0->1->2->0
    run_case("Cycle case", n3, pre3)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"\n==== TOTAL PROGRAM RUNTIME: {(end - start):.6f} s ====")
```

**What you’ll see when you run it**

* For each case: the order returned by **Kahn** and **DFS**, and a `valid: True/False` check.
* **Single-run** microsecond timings and **average** timings via `timeit`.
* Inline comments explain **time/space complexity** right where they matter—perfect for interviews.

