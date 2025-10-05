
---

# 🧠 Course Schedule

**Difficulty:** Medium
**Accuracy:** 51.77%
**Submissions:** 844K+
**Points:** 4
**Average Time:** 25m

---

## 📝 Problem Statement

There are a total of **n tasks** you have to pick, labelled from **0 to n-1**.
Some tasks may have **prerequisites[][]** — tasks that must be completed before others.

For example, to pick task `0`, you have to first finish task `1`.
This relationship is expressed as a pair: `[0, 1]`.

Given:

* The total number of tasks `n`
* A list of prerequisite pairs of size `m`

Your task is to **find an ordering of tasks** you should pick to finish all tasks.

---

### 🧩 Notes

* There may be **multiple correct orders** — you just need to return **any one of them**.
* If it is **impossible** to finish all tasks, return an **empty array**.
* Returning any correct order gives an output of **true**, whereas an invalid order should give **false**.

---

## 📘 Examples

### Example 1

**Input:**

```
n = 2
prerequisites[][] = [[1, 0]]
```

**Output:**

```
true
```

**Explanation:**
Only possible order is `[0, 1]`.

---

### Example 2

**Input:**

```
n = 4
prerequisites[][] = [[1, 0], [2, 0], [3, 1], [3, 2]]
```

**Output:**

```
true
```

**Explanation:**
There are a total of 4 tasks to pick.
To pick task `3`, you should have finished both tasks `1` and `2`.
Both tasks `1` and `2` should be picked **after** you finished task `0`.

So one correct task order is: `[0, 1, 2, 3]`.
Another correct ordering is `[0, 2, 1, 3]`.

Returning **any of these orders** will result in an output of **true**.

---

## ⚙️ Constraints

```
1 ≤ n ≤ 10⁵
0 ≤ prerequisites[i][0], prerequisites[i][1] < n
All prerequisite pairs are unique
prerequisites[i][0] ≠ prerequisites[i][1]
```

---

## ⏱️ Expected Complexities

**Time Complexity:** O(n + m)
**Auxiliary Space:** O(n + m)

---

## 🏢 Company Tags

* Google

---

## 🧮 Topic Tags

* DFS
* Graph
* BFS
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [Find Course Schedule I](https://www.geeksforgeeks.org/find-course-schedule-ii/)
* [Find Whether It Is Possible To Finish All Tasks Or Not From Given Dependencies](https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/)

---

---

awesome — let’s solve **Course Schedule (return any valid order or empty if impossible)** the interview way.

---

## 2) Intuition + Step-by-step dry run

### What we’re doing

Each pair `[a, b]` means **to take course `a`, you must first take `b`**.
So it’s a directed edge **b → a**. The problem asks for **a topological ordering** of this DAG.
If there’s a **cycle**, no ordering exists → return `[]`.

Two standard approaches:

1. **Kahn’s algorithm (BFS with in-degrees)** — most common and iterative.
2. **DFS postorder (with cycle detection using colors)** — also standard.

Both run in **O(n + m)** time, **O(n + m)** space.

---

### Dry run (Example 2)

```
n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Interpretation (b → a):
0→1, 0→2, 1→3, 2→3
```

**Kahn’s algorithm:**

* Build indegrees:

  * indeg[0]=0; indeg[1]=1 (0→1); indeg[2]=1 (0→2); indeg[3]=2 (1→3,2→3)
* Queue initially: nodes with indeg 0 → `[0]`
* Pop 0 → order = `[0]`; reduce indeg[1], indeg[2] → both become 0 → push 1,2 → queue `[1,2]`
* Pop 1 → order = `[0,1]`; reduce indeg[3] → now 1 → queue `[2]`
* Pop 2 → order = `[0,1,2]`; reduce indeg[3] → now 0 → push 3 → queue `[3]`
* Pop 3 → order = `[0,1,2,3]`
* Length == n → valid. Another possible order: `[0,2,1,3]` (depends on queue order).

If a cycle existed, you’d get stuck with some nodes never reaching indegree 0 → order length < n → return `[]`.

---

## 3) Python solutions (interview-ready)

### A) Kahn’s Algorithm (BFS) — **most expected**

```python
class Solution:
    def findOrder(self, n, prerequisites):
        """
        Return any topological order of courses (0..n-1) or [] if impossible.
        Each pair [a, b] means b -> a (b is a prereq for a).

        Time  : O(n + m)  where m = len(prerequisites)
        Space : O(n + m)
        """
        # Build adjacency and indegree
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for a, b in prerequisites:
            adj[b].append(a)   # edge b -> a
            indeg[a] += 1

        # Start with all nodes with indegree 0
        from collections import deque
        q = deque([i for i in range(n) if indeg[i] == 0])

        order = []
        while q:
            u = q.popleft()
            order.append(u)
            # Decrease indegree of neighbors; push new zeros
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If we processed all nodes, we found an order; otherwise there's a cycle
        return order if len(order) == n else []
```

#### Why interviewers like this

* Simple to reason about: pull nodes with zero prerequisites, keep removing edges.
* Immediately detects impossibility when `len(order) < n`.

---

### B) DFS Topological Sort (with cycle detection)

```python
class Solution:
    def findOrder(self, n, prerequisites):
        """
        DFS postorder topological sort with 3-color cycle detection.
        0 = unvisited, 1 = visiting, 2 = done.

        Time  : O(n + m)
        Space : O(n + m) + O(n) recursion
        """
        adj = [[] for _ in range(n)]
        for a, b in prerequisites:
            adj[b].append(a)   # b -> a

        color = [0] * n
        order = []
        has_cycle = False

        def dfs(u):
            nonlocal has_cycle
            color[u] = 1  # visiting
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                    if has_cycle: return
                elif color[v] == 1:
                    # back edge -> cycle
                    has_cycle = True
                    return
            color[u] = 2  # done
            order.append(u)  # postorder push

        for i in range(n):
            if color[i] == 0:
                dfs(i)
                if has_cycle:
                    return []

        order.reverse()  # postorder to topo order
        return order
```

---

### C) (Optional) Brute-ish idea (why not to use)

Repeatedly scan all courses and pick one whose prerequisites are all already chosen, removing it from the set.

* Worst case: **O(n² + n·m)** due to repeated scans — not good at scale.
* It’s essentially Kahn’s algorithm but implemented inefficiently.

---

## 4) Interview Q&A (high-yield)

**Q1. Why is this a topological sort?**
Because prerequisites define a partial order. A valid course order is a **linear extension** (topological order) of that DAG.

**Q2. How do you detect impossibility?**

* **Kahn:** if you can’t process all nodes (queue becomes empty but `order` length `< n`), there’s a **cycle**.
* **DFS:** if you find a **back edge** (visit an already “visiting/GRAY” node), there’s a cycle.

**Q3. Why orient edges as `b → a` from `[a,b]`?**
`[a,b]` means **b is a prerequisite of a**, i.e., b must come before a → directed edge **b → a**.

**Q4. Can there be multiple valid orders?**
Yes, any topological ordering is acceptable. Different queue/stack orders lead to different valid outputs.

**Q5. Complexity?**
Both approaches build adjacency once and traverse each edge/node at most once: **O(n + m)** time, **O(n + m)** space.

**Q6. What about self-prerequisites or duplicated pairs?**
Constraints usually exclude `a == b` and duplicates. If they appear, a self-edge is an immediate cycle; duplicates are harmless.

**Q7. When to prefer DFS vs Kahn?**

* **Kahn:** iterative, no recursion depth risk, easy cycle detection via count.
* **DFS:** natural when you already use recursion and want postorder stack; returns order via reverse(postorder).

---

---

sweet — here’s a **runnable, interview-style full program** for **Course Schedule (return any valid order or `[]` if impossible)** that:

* implements your required signature `findOrder(n, prerequisites)` in two flavors:

  * **Kahn’s algorithm (BFS/topological sort)** — primary solution
  * **DFS postorder with 3-color cycle detection** — alt solution
* prints outputs for sample inputs,
* benchmarks both with **timeit** on a moderate random DAG.

I’ve added **inline comments** calling out **time & space complexity** at each step.

---

## 5) Full Python program (with inline complexity notes + timings)

```python
"""
Course Schedule — Find any valid order or return [] if impossible
-----------------------------------------------------------------
We provide two standard solutions with the exact requested signature:

  1) Kahn's algorithm (BFS / indegree) — iterative, commonly expected
  2) DFS postorder with 3-color cycle detection (0/1/2)

Both:
  Time  : O(n + m)     where n = number of courses, m = number of prereq pairs
  Space : O(n + m)
"""

from collections import deque
from typing import List
import random
import timeit


# ============================ Kahn's Algorithm (BFS) ============================ #
class SolutionKahn:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Return any topological order of [0..n-1] or [] if there's a cycle.

        Build graph as edges b->a for pair [a,b] ("b is prerequisite of a").

        Steps:
          (1) Build adjacency + indegree arrays: O(n + m) time, O(n + m) space
          (2) Push all indegree-0 nodes to queue: O(n)
          (3) Pop nodes, reduce neighbors' indegree; push new zeros: O(n + m)
          (4) If processed < n => cycle => return []

        Overall:
          Time  : O(n + m)
          Space : O(n + m)
        """
        # (1) Build adjacency and indegree
        adj = [[] for _ in range(n)]     # O(n) lists, overall O(n + m) storage
        indeg = [0] * n                  # O(n) space
        for a, b in prerequisites:       # O(m)
            adj[b].append(a)             # edge b -> a
            indeg[a] += 1

        # (2) Initial queue with zero-indegree vertices
        q = deque([i for i in range(n) if indeg[i] == 0])  # O(n)

        order = []
        # (3) Standard Kahn processing — total O(n + m)
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # (4) If not all processed, there is a directed cycle
        return order if len(order) == n else []


# ===================== DFS Postorder + 3-Color Cycle Detection ===================== #
class SolutionDFS:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS Topological Sort (postorder) with 3-color cycle detection.
        color: 0=unvisited, 1=visiting, 2=done

        Steps:
          (1) Build adjacency b->a: O(n + m)
          (2) DFS each unvisited node:
                - If we see an edge to a "visiting" node => cycle => return []
                - On exit, push node to list (postorder)
          (3) Reverse postorder to get topo order

        Time  : O(n + m)
        Space : O(n + m) adjacency + O(n) recursion/aux arrays
        """
        # (1) Build graph
        adj = [[] for _ in range(n)]
        for a, b in prerequisites:
            adj[b].append(a)

        color = [0] * n    # O(n)
        out = []           # postorder stack
        cycle = False

        def dfs(u: int):
            nonlocal cycle
            color[u] = 1  # visiting
            for v in adj[u]:
                if color[v] == 0:
                    dfs(v)
                    if cycle:
                        return
                elif color[v] == 1:
                    cycle = True  # found back edge
                    return
            color[u] = 2  # done
            out.append(u)

        for i in range(n):
            if color[i] == 0:
                dfs(i)
                if cycle:
                    return []

        out.reverse()
        return out


# ================================ tiny helpers ================================= #
def bench(func, *args, number=100) -> float:
    """Return average seconds per run using timeit (for relative comparison)."""
    total = timeit.timeit(lambda: func(*args), number=number)
    return total / number


def make_random_DAG(n: int, density: float = 0.002) -> List[List[int]]:
    """
    Make a random DAG of n nodes by adding edges i->j for i<j with some probability.
    Return as prerequisites [a,b] where edge is b->a (i.e., [j, i]).
    Expected edges ~ density * n*(n-1)/2.
    """
    rng = random.Random(42)
    prereqs = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < density:
                # add i->j (i must come before j) => prereq pair is [j, i]
                prereqs.append([j, i])
    return prereqs


# =================================== demo & timings =================================== #
if __name__ == "__main__":
    print("=== Course Schedule — Kahn vs DFS (Topological Ordering) ===\n")

    # Example 1 (from prompt): n=2, [[1,0]]
    n1 = 2
    p1 = [[1, 0]]
    print(">>> Example 1")
    print("n =", n1, "prerequisites =", p1)
    print("Kahn ->", SolutionKahn().findOrder(n1, p1))
    print("DFS  ->", SolutionDFS().findOrder(n1, p1))
    print("Expected: any topo order, e.g., [0,1]\n")

    # Example 2 (from prompt): n=4, [[1,0],[2,0],[3,1],[3,2]]
    n2 = 4
    p2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(">>> Example 2")
    print("n =", n2, "prerequisites =", p2)
    print("Kahn ->", SolutionKahn().findOrder(n2, p2))
    print("DFS  ->", SolutionDFS().findOrder(n2, p2))
    print("Expected: e.g., [0,1,2,3] or [0,2,1,3]\n")

    # Example 3: cycle present (impossible)
    # 0<-1<-2<-0  (pairs [a,b] => b->a)
    n3 = 3
    p3 = [[0, 1], [1, 2], [2, 0]]
    print(">>> Example 3 (cycle)")
    print("n =", n3, "prerequisites =", p3)
    print("Kahn ->", SolutionKahn().findOrder(n3, p3))
    print("DFS  ->", SolutionDFS().findOrder(n3, p3))
    print("Expected: []\n")

    # -------- Timings on a moderate random DAG --------
    print("=== Timings (average seconds per call) ===")
    n = 8000
    prereqs = make_random_DAG(n, density=0.0008)  # sparse DAG (~25k edges on average)
    runs = 5

    t_kahn = bench(SolutionKahn().findOrder, n, prereqs, number=runs)
    t_dfs  = bench(SolutionDFS().findOrder,  n, prereqs, number=runs)

    print(f"Random DAG: n={n}, m≈{len(prereqs)} edges  runs={runs}")
    print(f"Kahn : {t_kahn:.6f} s/run")
    print(f"DFS  : {t_dfs :.6f} s/run")

    print("\nNotes:")
    print(" • Both solutions are O(n+m); Kahn is iterative and avoids recursion depth limits.")
    print(" • DFS is elegant and often similar speed; beware very deep graphs on Python recursion.")
    print(" • Space is O(n+m) for adjacency; plus O(n) for indeg/queue (Kahn) or color/stack (DFS).")
```

### What you’ll see

* Example 1 prints a valid order like `[0, 1]`.
* Example 2 prints something like `[0, 1, 2, 3]` (or `[0, 2, 1, 3]`).
* Example 3 prints `[]`.
* Then timing lines comparing Kahn vs DFS on a moderate random DAG (exact times vary by machine).

---

## 6) Real-World Use Cases (the important ones)

1. **Build/Deploy Pipelines & Task Scheduling**

   * Targets/jobs with prerequisites must be executed in **topological order**; if there’s a cycle, the pipeline must fail.

2. **Course/Module Prerequisites**

   * Academic planners and MOOC platforms validate that planned curricula are **acyclic** and generate feasible **study orders**.

3. **Package Managers / Dependency Resolution**

   * Installing packages requires resolving dependencies first; cycles must be detected to prevent **deadlocks**.

4. **Data/ETL Workflows**

   * DAG-based data pipelines (Airflow, etc.) execute tasks respecting upstream/downstream dependencies; cycles invalidate the workflow.