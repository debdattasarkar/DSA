
---

# 🔗 Strongly Connected Components

**Difficulty:** Medium
**Accuracy:** 50.61%
**Submissions:** 118K+
**Points:** 4
**Average Time:** 20 minutes

---

## 🧾 Problem Statement

Given an adjacency list `adj[]` of a **Directed Graph**, find the **number of Strongly Connected Components** (SCCs) in the graph.

---

## 🔎 Definition

A **Strongly Connected Component (SCC)** in a directed graph is a maximal set of vertices such that every vertex is reachable from every other vertex in the set.

---

## 📥 Input Format

* Adjacency List `adj[][]` of size `V`

  * `adj[i]` contains the list of nodes directly reachable from vertex `i`.

---

## 📤 Output Format

* Return the number of strongly connected components.

---

## 🧪 Examples

### Example 1:

```
Input:
adj[][] = [[2, 3], [0], [0], [1], [4], []]

Graph Representation:
0 → 2, 3
1 → 0
2 → 0
3 → 1
4 → 4
5 → (no outgoing edge)

Output: 3

Explanation:
There are 3 SCCs:
- {0, 1, 2, 3}
- {4}
- {5}
```

---

### Example 2:

```
Input:
adj[][] = [[1], [2], [0]]

Graph Representation:
0 → 1
1 → 2
2 → 0

Output: 1

Explanation:
All nodes are reachable from each other, forming 1 single SCC.
```

---

### Example 3:

```
Input:
adj[][] = [[1], []]

Graph Representation:
0 → 1

Output: 2

Explanation:
- Node 1 can't reach node 0.
- So, two individual SCCs: {0}, {1}
```

---

## 📏 Constraints

```
2 ≤ adj.size() ≤ 10^6
0 ≤ edges ≤ adj.size() - 1
```

---

## 📊 Expected Complexities

| Complexity Type | Value    |
| --------------- | -------- |
| Time Complexity | O(V + E) |
| Auxiliary Space | O(V + E) |

---

## 🏷️ Tags

* Graph
* Strongly Connected Components
* Kosaraju Algorithm
* Tarjan Algorithm
* DFS
* Data Structures

---

## 📚 Related Articles

* [Strongly Connected Components](https://www.geeksforgeeks.org/strongly-connected-components/)

---

---

# 🔗 Strongly Connected Components (SCC) in Directed Graphs

## 📘 Problem Summary

Given a directed graph represented by an adjacency list `adj[]`, your task is to count how many **strongly connected components** (SCCs) exist in the graph. A strongly connected component is a maximal set of nodes such that every node is reachable from every other node in the same set.

---

## 📊 Step-by-Step Explanation with Dry Run

We will use **Kosaraju’s Algorithm** — a two-pass DFS-based method.

### 🔁 Kosaraju's Algorithm Steps

1. **First DFS Pass (Original Graph):**

   * Do a DFS traversal of the original graph and push nodes onto a stack in order of **completion** (post-order).

2. **Reverse the Graph:**

   * Reverse all edges of the graph.

3. **Second DFS Pass (Transposed Graph):**

   * Pop vertices from the stack and do DFS on the reversed graph. Each DFS call represents one SCC.

### 🧪 Dry Run: Example

Input:

```python
adj = [[2, 3], [0], [0], [1], [4], []]
```

Graph:

```
0 → 2, 3
1 → 0
2 → 0
3 → 1
4 → 4
5 → (no edges)
```

#### Step 1: First DFS to fill stack (post-order)

Start from node 0:

```
0 → 2 → 0 (already visited), → 3 → 1 → 0
Stack = [5, 4, 1, 3, 2, 0]
```

#### Step 2: Reverse the Graph

New adj:

```python
rev_adj = [[1, 2], [3], [], [0], [4], []]
```

#### Step 3: Second DFS on reversed graph using stack order

Stack pop order: 0, 2, 3, 1, 4, 5

* DFS from 0 → covers 0, 1, 2, 3 → 1st SCC
* DFS from 4 → covers 4 → 2nd SCC
* DFS from 5 → covers 5 → 3rd SCC

✅ Output: 3 SCCs

---

## 💡 Optimized Python Code (Kosaraju's Algorithm)

```python
class Solution:
    def kosaraju(self, V, adj):
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(v)

        def reverse_graph():
            rev = [[] for _ in range(V)]
            for u in range(V):
                for v in adj[u]:
                    rev[v].append(u)
            return rev

        def dfs_reverse(v, visited, rev):
            visited[v] = True
            for neighbor in rev[v]:
                if not visited[neighbor]:
                    dfs_reverse(neighbor, visited, rev)

        # 1. First pass
        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)

        # 2. Reverse the graph
        rev = reverse_graph()

        # 3. Second pass
        visited = [False] * V
        scc_count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs_reverse(node, visited, rev)
                scc_count += 1

        return scc_count
```

---

## ❓ Expected Interview Questions & Answers

### Q1. Why do we use Kosaraju's algorithm?

**A:** It's efficient (O(V + E)) and uses two DFS passes. It’s conceptually simpler than Tarjan’s if you understand post-order.

---

### Q2. What is the intuition behind the reverse graph?

**A:** In the reversed graph, all nodes from one SCC point inward, making them easier to collect via DFS.

---

### Q3. Can we use BFS instead of DFS?

**A:** No, DFS is essential to capture **finishing times**, which drive SCC detection in Kosaraju.

---

### Q4. What if the graph is undirected?

**A:** SCCs apply to **directed** graphs. For undirected graphs, use Union-Find or DFS to find connected components.

---

### Q5. What’s the time and space complexity?

* **Time Complexity:** O(V + E)
* **Space Complexity:** O(V + E) for the reverse graph and recursion

---

## 💡 Optimized Python Code (Kosaraju's Algorithm)

```python
import time

class Solution:
    def kosaraju(self, V, adj):

        # Step 1: DFS to fill finishing times in a stack
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(v)  # Post-order

        # Step 2: Reverse the graph
        def reverse_graph():
            rev = [[] for _ in range(V)]
            for u in range(V):
                for v in adj[u]:
                    rev[v].append(u)
            return rev

        # Step 3: DFS on reversed graph to find SCCs
        def dfs_reverse(v, visited, rev):
            visited[v] = True
            for neighbor in rev[v]:
                if not visited[neighbor]:
                    dfs_reverse(neighbor, visited, rev)

        # Time complexity: O(V + E)
        visited = [False] * V
        stack = []

        # First DFS pass
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)

        # Reverse the graph
        rev = reverse_graph()

        # Second DFS pass on reversed graph
        visited = [False] * V
        scc_count = 0

        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs_reverse(node, visited, rev)
                scc_count += 1

        return scc_count

# ⏱️ Benchmarking with time
if __name__ == '__main__':
    import timeit

    # Input: Directed graph with 6 vertices
    V = 6
    adj = [[2, 3], [0], [0], [1], [4], []]

    start = timeit.default_timer()
    obj = Solution()
    result = obj.kosaraju(V, adj)
    end = timeit.default_timer()

    print("Number of SCCs:", result)
    print("Execution Time (seconds):", end - start)
```


---

## 🌍 Real-World Use Cases

1. **Deadlock Detection in Operating Systems**

   * SCCs can detect cycles in the wait-for graph to identify deadlocks.

2. **Control Flow Analysis in Compilers**

   * Find regions of mutual reachability for optimization and loop detection.

3. **Social Networks**

   * Detect tightly-knit communities where every member is connected to every other.

4. **Web Crawlers**

   * Identify sets of pages with mutual linkage (like Wikipedia loops).

5. **Recommendation Engines**

   * Detect clusters where preferences or transitions form feedback loops.

---
