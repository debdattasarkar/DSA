
---

# 🧩 Prerequisite Tasks

**Difficulty:** Medium
**Accuracy:** 37.81%
**Submissions:** 82K+
**Points:** 4
**Average Time:** 25m

---

## 📝 Problem Statement

There are a total of **N tasks**, labeled from **0 to N-1**.
Some tasks may have **prerequisites**, for example:

> To do task 0 you have to first complete task 1,
> which is expressed as a pair: `[0, 1]`.

Given the total number of tasks `N` and a list of `P` **prerequisite pairs**, determine whether it is possible to finish all tasks.

---

## 🧠 Examples

### Example 1

```
Input:
N = 4, P = 3, prerequisites = [[1,0],[2,1],[3,2]]

Output:
Yes
```

**Explanation:**
To do task 1 you should have completed task 0,
to do task 2 you should have finished task 1,
and to do task 3 you should have finished task 2.

So, it is possible to finish all tasks in the order **0 → 1 → 2 → 3**.

---

### Example 2

```
Input:
N = 2, P = 2, prerequisites = [[1,0],[0,1]]

Output:
No
```

**Explanation:**
To do task 1 you should have completed task 0,
and to do task 0 you should have finished task 1 —
This creates a **cycle**, making it **impossible** to complete all tasks.

---

## ⚙️ Constraints

```
1 ≤ N ≤ 10⁴
1 ≤ P ≤ 10⁵
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(N + P)
* **Auxiliary Space:** O(N + P)

---

## 🏢 Company Tags

* Amazon
* Microsoft
* Google
* Facebook
* Twitter
* Apple

---

## 🏷️ Topic Tags

* Graph
* Data Structures

---

## 📚 Related Articles

* [Find Whether It Is Possible To Finish All Tasks Or Not From Given Dependencies](https://www.geeksforgeeks.org/find-whether-it-is-possible-to-finish-all-tasks-or-not-from-given-dependencies/)

---

---

Below is an interview-ready guide to **Prerequisite Tasks** (aka “can we finish all tasks?”).
Core idea: model tasks as a **directed graph**; the question is **whether the graph is acyclic**.

---

## 2) Intuition + Step-by-Step Dry Run

### Problem restated

* You have `N` tasks `0..N-1`.
* Each pair `[a, b]` means **to do `a` you must finish `b` first** ⇒ edge `b → a`.
* Can we finish all tasks? **Yes** iff the directed graph has **no cycle**.

### Standard approaches

1. **Kahn’s Algorithm (BFS topological sort)**

   * Compute `indegree[v]` for every node.
   * Push all nodes with `indegree = 0` into a queue.
   * Repeatedly pop a node, “take” it, and decrease indegree of its neighbors; if any hits 0, push it.
   * Count how many nodes you popped. If count == N ⇒ **possible**; else there was a cycle.

2. **DFS Cycle Detection (colors / recursion stack)**

   * Do DFS; mark nodes `0:unseen, 1:visiting, 2:done`.
   * If you ever go to a `visiting` node, a **back edge** (cycle) exists ⇒ **impossible**.

Both are O(N + P). BFS is usually preferred in interviews for clarity.

---

### Dry run 1 (possible)

```
N = 4
prerequisites = [[1,0], [2,1], [3,2]]
Edges: 0→1, 1→2, 2→3

indegree: [0,1,1,1]
queue: [0]
Take 0: reduce indegree[1]→0, push 1
Take 1: reduce indegree[2]→0, push 2
Take 2: reduce indegree[3]→0, push 3
Take 3: (no neighbors)
popped count = 4 == N ⇒ YES (no cycle)
```

### Dry run 2 (impossible)

```
N = 2
prerequisites = [[1,0], [0,1]]
Edges: 0→1, 1→0

indegree: [1,1]
queue: []   (no node with indegree 0)
popped count = 0 < N ⇒ NO (cycle exists)
```

---

## 3) Python solutions in interview style

### A) Kahn’s Algorithm (BFS Topological Sort) — recommended

```python
#User function Template for python3

from collections import deque, defaultdict

class Solution:
    def isPossible(self, N, P, prerequisites):
        """
        Return True if all tasks can be finished (i.e., graph has no cycle).
        Build graph with edges b->a for each pair [a,b].
        Time : O(N + P)
        Space: O(N + P)
        """
        # Build adjacency list and indegree counts
        adj = defaultdict(list)
        indeg = [0] * N
        for a, b in prerequisites:
            adj[b].append(a)   # b must precede a: edge b->a
            indeg[a] += 1

        # Push all nodes with 0 indegree
        q = deque([v for v in range(N) if indeg[v] == 0])

        # Pop and relax edges
        seen = 0
        while q:
            u = q.popleft()
            seen += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If we processed all nodes, no cycle
        return seen == N
```

### B) DFS with coloring (detect a back edge) — equally accepted

```python
from collections import defaultdict
import sys

class Solution:
    def isPossible(self, N, P, prerequisites):
        """
        DFS cycle detection via colors:
          0 = unvisited, 1 = visiting, 2 = done
        Back-edge to 'visiting' means a cycle.
        Time : O(N + P)
        Space: O(N + P) including recursion stack
        """
        sys.setrecursionlimit(1_000_000)
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)  # b -> a

        color = [0] * N  # 0,1,2

        def dfs(u):
            color[u] = 1  # visiting
            for v in adj[u]:
                if color[v] == 1:    # back edge => cycle
                    return False
                if color[v] == 0 and not dfs(v):
                    return False
            color[u] = 2  # done
            return True

        for u in range(N):
            if color[u] == 0 and not dfs(u):
                return False
        return True
```

> Either solution is fine in interviews. If asked to **return an order**, extend the BFS to output the popped sequence.

---

## 4) Common Interview Q&A

**Q1. What does the problem reduce to?**
A: Detecting whether a **directed graph** has a **cycle**. If no cycle → tasks can be completed.

**Q2. Why does Kahn’s algorithm prove there’s no cycle?**
A: Nodes in cycles **never** reach indegree 0; hence if after processing you pop fewer than N nodes, a cycle prevented progress.

**Q3. Time/Space complexity?**
A: Both Kahn’s and DFS are **O(N + P)** time and **O(N + P)** space.

**Q4. What if there are tasks with no prerequisites and no dependents?**
A: They start with indegree 0, get processed immediately; they don’t affect correctness.

**Q5. How to modify to return a valid order?**
A: In Kahn’s algorithm, collect the popped nodes into a list; if its length is N, that’s a valid topological ordering.

**Q6. Edge direction — which way?**
A: For pair `[a, b]` (“to do `a` you must do `b` first”), add edge **`b → a`**.

**Q7. Corner cases?**
A:

* `P = 0` ⇒ trivially possible.
* Duplicate edges: treat normally; indegree increments accordingly.
* Disconnected components: algorithm still works.

---

---

Below is a **complete, runnable script** for **Prerequisite Tasks** that:

* Builds the dependency graph.
* Solves with **Kahn’s BFS topological sort** (recommended).
* Also includes a **DFS coloring** variant for reference.
* Prints results for the two sample inputs.
* Uses **timeit** to show average runtime.
* Has **inline comments** calling out **time/space complexity** step-by-step.

---

### 5) Full program (with sample I/O + timing)

```python
"""
Prerequisite Tasks — Can we finish all tasks?
=============================================

Given N tasks (0..N-1) and prerequisite pairs [a, b] meaning "do b before a"
(edge b -> a), determine if it's possible to finish all tasks.

We solve via Kahn's Algorithm (BFS topological sort).

Global Asymptotics for the solver:
  Time  : O(N + P)    (build graph + process each edge once)
  Space : O(N + P)    (adjacency list, indegree array, queue)
"""

from collections import defaultdict, deque
import timeit


# -------------------------- BFS (Kahn) Solution -------------------------- #
def can_finish_kahn(N, prerequisites):
    """
    Return True if all tasks can be finished (graph has no cycle).

    Steps:
    1) Build adjacency list 'adj' and indegree array 'indeg'
       - Building adj: O(P) time; Space: O(N + P)
       - Computing indeg: O(P) time; Space: O(N)

    2) Initialize a queue with all vertices whose indegree == 0
       - O(N) time to scan; Space: O(N) worst-case

    3) Pop vertices, "take" the course, relax outgoing edges and
       push any neighbor that becomes indegree 0
       - Each vertex popped once; each edge relaxed once
       - O(N + P) time; queue Space up to O(N)

    4) If we popped all N vertices (seen == N) => acyclic => possible
       Else => cycle => impossible
    """
    adj = defaultdict(list)
    indeg = [0] * N

    # Build the graph: edge b -> a for pair [a, b]
    # O(P) time
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1

    # Initialize queue with all nodes of indegree 0
    # O(N) time
    q = deque([v for v in range(N) if indeg[v] == 0])

    seen = 0  # how many vertices we "took"
    while q:
        u = q.popleft()  # O(1)
        seen += 1
        # Relax all outgoing edges once overall -> total O(P)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return seen == N  # O(1)


# ----------------------------- DFS Variant ------------------------------ #
def can_finish_dfs(N, prerequisites):
    """
    DFS cycle detection using colors:
      0 = unvisited, 1 = visiting, 2 = done
    Any edge to a 'visiting' node => back edge => cycle.

    Time  : O(N + P)
    Space : O(N + P) including recursion stack and adjacency.
    """
    adj = defaultdict(list)
    for a, b in prerequisites:
        adj[b].append(a)

    color = [0] * N  # 0,1,2

    def dfs(u):
        color[u] = 1  # visiting
        for v in adj[u]:
            if color[v] == 1:      # back edge -> cycle
                return False
            if color[v] == 0 and not dfs(v):
                return False
        color[u] = 2  # done
        return True

    for u in range(N):
        if color[u] == 0 and not dfs(u):
            return False
    return True


# ----------------------------- Demo + Timing ---------------------------- #
def run_example(N, prerequisites, title):
    print(f"\n{title}")
    print("N =", N, "Prerequisites =", prerequisites)
    ans_bfs = can_finish_kahn(N, prerequisites)
    ans_dfs = can_finish_dfs(N, prerequisites)
    print("Kahn/BFS says :", "Yes" if ans_bfs else "No")
    print("DFS  says     :", "Yes" if ans_dfs else "No")


def benchmark(N, prerequisites, repeat=100):
    # Time only the BFS (Kahn) solver; DFS is similar O(N+P)
    def once():
        can_finish_kahn(N, prerequisites)

    avg = timeit.timeit(once, number=repeat) / repeat
    print(f"\n[timeit] Average over {repeat} runs: {avg:.6f} s per call (O(N+P)).")


if __name__ == "__main__":
    # Example 1 (possible): chain 0->1->2->3
    N1 = 4
    P1 = [[1, 0], [2, 1], [3, 2]]
    run_example(N1, P1, "Example 1 (expected: Yes)")

    # Example 2 (impossible): 0->1 and 1->0 (cycle)
    N2 = 2
    P2 = [[1, 0], [0, 1]]
    run_example(N2, P2, "Example 2 (expected: No)")

    # Quick timing on Example 1
    benchmark(N1, P1, repeat=200)
```

**Typical Output (illustrative)**

```
Example 1 (expected: Yes)
N = 4 Prerequisites = [[1, 0], [2, 1], [3, 2]]
Kahn/BFS says : Yes
DFS  says     : Yes

Example 2 (expected: No)
N = 2 Prerequisites = [[1, 0], [0, 1]]
Kahn/BFS says : No
DFS  says     : No

[timeit] Average over 200 runs: 0.0000xx s per call (O(N+P)).
```

---

### 6) Real-World Use Cases (high-impact)

1. **Build/Compilation Systems**
   Targets depend on other targets; a cycle means your build graph is invalid. Topological order determines a valid build sequence.

2. **University Course Planning**
   Courses with prerequisites form a DAG. Detecting a cycle prevents impossible curricula; topological order gives a valid term-by-term plan.

3. **Task Scheduling / Job Orchestration**
   In CI/CD pipelines, workflows, or data processing DAGs, tasks depend on prior tasks. Detect cycles and produce a safe execution order.

4. **Package Managers / Dependency Resolution**
   Library dependencies must be acyclic for consistent installs. Detecting cycles avoids deadlocks or partial states.