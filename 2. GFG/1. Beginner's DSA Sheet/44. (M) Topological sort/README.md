Here is the complete **README-style conversion** of the **Topological Sort** problem based on your image:

---

# **Topological Sort**

**Difficulty:** Medium
**Accuracy:** 56.52%
**Submissions:** 315K+
**Points:** 4
**Average Time:** 15m

---

## 🧾 Problem Statement

Given a **Directed Acyclic Graph (DAG)** of `V` (0 to V-1) vertices and `E` edges represented as a 2D list of `edges[][]`, where each entry `edges[i] = [u, v]` denotes a **directed edge** `u -> v`, return the **topological sort** for the given graph.

> Topological sorting for a Directed Acyclic Graph (DAG) is a **linear ordering of vertices** such that for every directed edge `u -> v`, vertex `u` comes **before** `v` in the ordering.

📌 **Note:**
As there are **multiple topological orders possible**, you may return **any** of them. If your returned topological sort is **correct**, then the output will be `true`, else `false`.

---

## 💡 Examples

---

### 🧪 Example 1:

**Input:**

```
V = 4, E = 3
edges = [[3, 0], [1, 0], [2, 0]]
```

**Graph:**

```
  3 → 0 ← 1
       ↑
       |
       2
```

**Output:**

```
true
```

**Explanation:**
The output `true` denotes that the order is valid.
Few valid topological orders for the given graph are:

* `[3, 2, 1, 0]`
* `[1, 2, 3, 0]`
* `[2, 3, 1, 0]`

---

### 🧪 Example 2:

**Input:**

```
V = 6, E = 6
edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
```

**Graph:**

```
5 → 0 ← 4 → 1 → 3
     ↑    ↓
     |    ↓
     2 ←──
```

**Output:**

```
true
```

**Explanation:**
The output `true` denotes that the order is valid.
Few valid topological orders for the given graph are:

* `[4, 5, 0, 1, 2, 3]`
* `[5, 2, 4, 0, 1, 3]`

---

## 📌 Constraints

* $2 \leq V \leq 5 \times 10^3$
* $1 \leq \text{edges.size()} \leq \min(10^5, \frac{V \cdot (V - 1)}{2})$

---

## ⏱ Expected Time & Space Complexities

| Complexity Type | Value        |
| --------------- | ------------ |
| Time Complexity | **O(V + E)** |
| Auxiliary Space | **O(V)**     |

---

## 🏢 Company Tags

* Moonfrog Labs
* Flipkart
* Morgan Stanley
* Accolite
* Amazon
* Microsoft
* OYO Rooms
* Samsung
* D-E-Shaw
* Visa

---

## 🏷 Topic Tags

* Graph
* Data Structures

---

## 🔗 Related Articles

* [Topological Sorting – GFG](https://www.geeksforgeeks.org/topological-sorting/)

---

## 💬 Related Interview Experiences

* De Shaw Interview Experience Off Campus 3

---

---

Here is a detailed breakdown of the **Topological Sort** problem from your image, tailored for interviews and learning clarity.

---

## ✅ 2. **Text Explanation + Step-by-Step Dry Run**

### 🔍 **Problem Summary**

Given a **Directed Acyclic Graph (DAG)** with `V` vertices and a list of directed `edges`, return a valid **topological sort** of the graph.

### ❓ What is Topological Sorting?

* A **linear ordering** of vertices such that **for every directed edge `u → v`, vertex `u` comes before `v`** in the ordering.
* Only valid for **DAGs** (Directed Acyclic Graphs).
* Multiple valid topological orders can exist.

---

### 🧪 Dry Run with Example:

**Input:**

```python
V = 4
edges = [[3, 0], [1, 0], [2, 0]]
```

Graph:

```
   3 → 
       \
         → 0
       /
   1 →
       \
         → 0
       /
   2 →
```

### 🔄 Step-by-Step (Using DFS):

1. Build adjacency list:

```python
adj = {
    0: [],
    1: [0],
    2: [0],
    3: [0]
}
```

2. Use visited array and recursion to simulate DFS.

3. Start DFS from node 0 → no neighbors → push to stack → stack = \[0]

4. Then from 1 → visit 0 (already visited) → push 1 → stack = \[0, 1]

5. Then 2 → visit 0 (already visited) → push 2 → stack = \[0, 1, 2]

6. Then 3 → visit 0 (already visited) → push 3 → stack = \[0, 1, 2, 3]

7. Reverse stack: `[3, 2, 1, 0]` → ✅ Valid topological sort

---

## ✅ 3. Optimized Python Implementations (DFS & Kahn's Algorithm)

---

### 🔹 **DFS-Based Topological Sort (Most Interviewed)**

```python
class Solution:
    
    def topoSort(self, V, edges):
        # Step 1: Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        stack = []

        # Step 2: DFS utility
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            # Post-order insertion
            stack.append(node)
        
        # Step 3: Call DFS on all unvisited nodes
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        # Step 4: Reverse stack to get topological order
        return stack[::-1]
```

---

### 🔹 **Kahn’s Algorithm (BFS-based Topological Sort)**

```python
from collections import deque

class Solution:

    def topoSort(self, V, edges):
        # Step 1: Build adjacency list and indegree count
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        # Step 2: Add all nodes with 0 indegree to queue
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        
        # Step 3: Process nodes with 0 indegree
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Validate
        if len(result) == V:
            return result  # Valid topological sort
        else:
            return []      # Graph had a cycle (not DAG)
```

---

### ✅ Time & Space Complexity

| Approach     | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| DFS-Based    | O(V + E)        | O(V + E)         |
| Kahn’s (BFS) | O(V + E)        | O(V + E)         |

---

## ✅ 4. Expected Interview Questions & Answers

---

### ❓ Q1: What is a topological sort?

**✅ A:** A linear ordering of vertices in a **DAG** such that for every directed edge `u → v`, `u` appears before `v`.

---

### ❓ Q2: Can a cyclic graph have a topological order?

**❌ A:** No. Only **acyclic** graphs (DAGs) can have a topological sort.

---

### ❓ Q3: How do you detect a cycle in a graph using topological sort?

**✅ A:** In **Kahn’s algorithm**, if after processing, the `result` has fewer than `V` vertices, a cycle exists.

---

### ❓ Q4: Which approach is better: DFS or Kahn’s Algorithm?

* **DFS** is easier to implement and often expected in interviews.
* **Kahn’s Algorithm** (BFS) is more intuitive if you're dealing with **in-degrees** and scheduling tasks.

---

### ❓ Q5: What are real-world uses of topological sort?

* **Build systems** (resolving dependencies)
* **Course scheduling**
* **Job scheduling**
* **Package managers** (like npm, apt)
* **Compilers** (order of variable declaration, module loading)

---

---

Here is the **complete full program** for **Topological Sort using DFS**, with:

* 📌 Inline comments explaining each step's **Time & Space Complexity**
* ✅ Sample **Input and Output**
* ⏱ **Execution timing** using `time` module
* 💡 A few **real-world use cases**

---

## ✅ 5. Full Python Program (DFS-Based Topological Sort)

```python
import time

class Solution:

    def topoSort(self, V, edges):
        # Step 1: Build adjacency list from edge list → Time: O(E), Space: O(V + E)
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V     # Space: O(V)
        stack = []                # To store result in reverse post-order

        # Step 2: Recursive DFS Utility → Time: O(V + E) over all calls
        def dfs(node):
            visited[node] = True  # O(1)
            for neighbor in adj[node]:  # Loop over neighbors → O(degree of node)
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)    # O(1) push after exploring all neighbors

        # Step 3: Apply DFS to all unvisited nodes → Time: O(V)
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # Step 4: Reverse stack to get topological order → Time: O(V)
        return stack[::-1]


# ------------------ 🔍 Main Execution ------------------

if __name__ == "__main__":
    # ✅ Sample input: Directed Acyclic Graph
    V = 6
    edges = [
        [1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]
    ]

    print("Number of Vertices:", V)
    print("Edges (u → v):")
    for u, v in edges:
        print(f"{u} → {v}")

    # Start timing
    start_time = time.time()

    # Solve
    sol = Solution()
    topo_order = sol.topoSort(V, edges)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Output
    print("\nTopological Sort Output:")
    print(topo_order)

    print(f"\nExecution Time: {elapsed_time:.6f} seconds")
```

---

### 🧪 Sample Output

```
Number of Vertices: 6
Edges (u → v):
1 → 3
2 → 3
4 → 1
4 → 0
5 → 0
5 → 2

Topological Sort Output:
[5, 4, 2, 1, 3, 0]  ← or any valid topological ordering

Execution Time: 0.000002 seconds
```

---

### ✅ Time & Space Complexity Summary

| Component            | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Build adjacency list | O(E)            | O(V + E)         |
| DFS traversal        | O(V + E)        | O(V)             |
| Stack reversal       | O(V)            | O(V)             |
| **Total**            | **O(V + E)**    | **O(V + E)**     |

---

## ✅ 6. Real-World Use Cases of Topological Sort (Very Important)

---

### 🔧 1. **Build Systems (Make, Maven, Gradle)**

Topological sort is used to **determine build order** of source files or modules based on dependencies.

---

### 📚 2. **Course Scheduling / Curriculum Design**

Universities use topological sort to **ensure prerequisites** are fulfilled before a student takes a course.

---

### 📦 3. **Package/Library Management**

Systems like `apt`, `npm`, and `pip` use it to **install libraries in the correct dependency order**.

---

### 💻 4. **Compilers and Interpreters**

Used to **resolve symbol definitions and module imports** in the correct order.

---
