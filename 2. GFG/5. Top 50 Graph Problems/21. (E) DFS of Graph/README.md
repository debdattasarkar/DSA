
---

# **DFS of Graph**

**Difficulty:** Easy
**Accuracy:** 63.07%
**Submissions:** 368K+
**Points:** 2
**Average Time:** 5m

---

## **Problem Statement**

Given a **connected undirected graph** containing **V** vertices represented by a 2-D adjacency list `adj[][]`, where each `adj[i]` represents the list of vertices connected to vertex `i`, perform a **Depth First Search (DFS)** traversal starting from **vertex 0**, visiting vertices from **left to right as per the given adjacency list**, and return a list containing the DFS traversal of the graph.

> **Note:** Do traverse in the **same order** as they are in the given **adjacency list**.

---

## **Examples**

### Example 1:

**Input:**

```python
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
```

**Graph Structure:**

```
     0
   / | \
  2  3  1
  |
  4
```

**Output:**

```
[0, 2, 4, 3, 1]
```

**Explanation:**
Starting from 0, the DFS traversal proceeds as follows:

* Visit 0 → Output: `[0]`
* Visit 2 (the first neighbor of 0) → Output: `[0, 2]`
* Visit 4 (the first neighbor of 2) → Output: `[0, 2, 4]`
* Backtrack to 2, then backtrack to 0, and visit 3 → Output: `[0, 2, 4, 3]`
* Finally, backtrack to 0 and visit 1 → Final Output: `[0, 2, 4, 3, 1]`

---

### Example 2:

**Input:**

```python
adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
```

**Graph Structure:**

```
     0
    / \
   1   2
      / \
     3   4
```

**Output:**

```
[0, 1, 2, 3, 4]
```

**Explanation:**
Starting from 0, the DFS traversal proceeds as follows:

* Visit 0 → Output: `[0]`
* Visit 1 (the first neighbor of 0) → Output: `[0, 1]`
* Visit 2 (the first neighbor of 1) → Output: `[0, 1, 2]`
* Visit 3 (the first neighbor of 2) → Output: `[0, 1, 2, 3]`
* Backtrack to 2 and visit 4 → Final Output: `[0, 1, 2, 3, 4]`

---

## **Constraints**

* $1 \leq V = \text{adj.size()} \leq 10^4$
* $1 \leq \text{adj}[i][j] \leq 10^4$

---

## **Expected Complexities**

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V + E)

---

## **Company Tags**

* Accolite
* Amazon
* Samsung
* Intuit

---

## **Topic Tags**

* DFS
* Graph
* Data Structures
* Algorithms

---

## **Related Articles**

* [Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

---

---

Here’s the complete breakdown for the **"DFS of Graph"** problem:

---

## ✅ 2. **Text Explanation + Step-by-Step Dry Run**

### 🔍 Problem Summary:

You are given an **undirected**, **connected graph** represented as an **adjacency list**, and you need to return the **DFS traversal** starting from vertex `0`, visiting vertices **in the order provided** in the adjacency list.

---

### 🌳 DFS Traversal: Key Points

* Uses **recursion or stack**.
* Marks nodes as **visited** to avoid infinite loops.
* **Order matters** – follow adjacency list as-is.
* Start from **vertex 0**.

---

### 🧪 Example:

**Input:**

```python
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
```

### Step-by-step DFS traversal:

```
Start from 0 → visited = {0}, result = [0]
- Neighbors of 0 = [2, 3, 1]
- Go to 2 → visited = {0, 2}, result = [0, 2]
    - Neighbors of 2 = [0, 4]
    - 0 already visited → Go to 4 → visited = {0, 2, 4}, result = [0, 2, 4]
        - Neighbors of 4 = [2] → already visited → return
- Backtrack to 0 → Next is 3 → visited = {0, 2, 4, 3}, result = [0, 2, 4, 3]
    - Neighbors of 3 = [0] → already visited → return
- Backtrack to 0 → Next is 1 → visited = {0, 2, 4, 3, 1}, result = [0, 2, 4, 3, 1]
    - Neighbors of 1 = [0] → already visited
```

### ✅ Final Output:

```
[0, 2, 4, 3, 1]
```

---

## ✅ 3. Python Code – Brute and Optimized (with Inline Comments)

### 🔹 **Optimized DFS using Recursion (Most Common in Interviews)**

```python
class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V       # Track visited nodes
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(0)  # Start DFS from node 0
        return result
```

---

### 🔹 **DFS using Iterative Approach (using Stack)**

```python
class Solution:

    # Iterative DFS using explicit stack
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V
        result = []

        stack = [0]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                # Add neighbors in reverse order to preserve original order when popped
                for neighbor in reversed(adj[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return result
```

---

### 🔹 **Brute Force (For Understanding – Not recommended in interviews)**

```python
class Solution:

    def dfs(self, adj):
        V = len(adj)
        result = []
        visited = set()

        def recurse(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in adj[node]:
                recurse(neighbor)

        recurse(0)
        return result
```

---

## ✅ 4. **Expected Interview Questions & Answers**

### ❓ Q1: What is DFS?

**✅ A:** DFS (Depth First Search) is a graph traversal algorithm that starts from a source node and explores as far as possible along each branch before backtracking.

---

### ❓ Q2: What’s the time and space complexity of DFS?

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V)` for visited + call stack (or explicit stack)

---

### ❓ Q3: How is DFS different from BFS?

| DFS                                | BFS                                         |
| ---------------------------------- | ------------------------------------------- |
| Uses Stack (recursion or explicit) | Uses Queue                                  |
| Explores depth-wise                | Explores level-wise                         |
| May not find the shortest path     | Finds the shortest path (unweighted graphs) |

---

### ❓ Q4: How do you avoid revisiting nodes in DFS?

**✅ A:** By maintaining a `visited[]` array or `set` to mark nodes already visited.

---

### ❓ Q5: Is DFS recursive or iterative?

**✅ A:** DFS is naturally recursive but can be implemented iteratively using a stack.

---

### ❓ Q6: What kind of graphs work with this DFS function?

* Connected
* Undirected
* Adjacency list representation
* No self-loops or parallel edges assumed unless mentioned

---

### ❓ Q7: Why do we traverse in the same order as adjacency list?

**✅ A:** Because the problem explicitly says so. It affects the DFS output. This is important for deterministic DFS output.

---

---

Sure! Here's the **complete Python program** for the **DFS of a Graph**, including:

1. **Input values**
2. **Output traversal**
3. **Inline comments for time and space complexity per step**
4. **Actual execution time** using `time` module
5. **Real-World Use Cases**

---

## ✅ 5. Full Program with Time & Space Complexity Annotations

```python
import time

class Solution:
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        V = len(adj)  # Number of vertices → O(1)
        visited = [False] * V  # Visited array → Space: O(V)
        result = []

        # DFS utility function (recursive) → Time: O(V + E) in total
        def dfs_util(v):
            visited[v] = True  # Mark node visited → O(1)
            result.append(v)   # Append to result → O(1)
            for neighbor in adj[v]:  # Traverse neighbors → O(degree of v)
                if not visited[neighbor]:
                    dfs_util(neighbor)  # Recursive DFS call

        dfs_util(0)  # Start DFS from node 0
        return result


# ------------------ Main Execution Block ------------------

if __name__ == "__main__":
    # Sample input graph (adjacency list)
    adj = [
        [2, 3, 1],  # Connections from node 0
        [0],        # Connections from node 1
        [0, 4],     # Connections from node 2
        [0],        # Connections from node 3
        [2]         # Connections from node 4
    ]

    print("Input Graph (Adjacency List):")
    for i, neighbors in enumerate(adj):
        print(f"Vertex {i}: {neighbors}")
    
    # Start timing
    start_time = time.time()

    # Create Solution instance and run DFS
    sol = Solution()
    output = sol.dfs(adj)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nDFS Traversal Output:")
    print(output)

    print(f"\nExecution Time: {elapsed_time:.6f} seconds")
```

---

### ✅ Example Output:

```
Input Graph (Adjacency List):
Vertex 0: [2, 3, 1]
Vertex 1: [0]
Vertex 2: [0, 4]
Vertex 3: [0]
Vertex 4: [2]

DFS Traversal Output:
[0, 2, 4, 3, 1]

Execution Time: 0.000003 seconds
```

---

### ✅ Time and Space Complexity (Detailed):

| Step                 | Time Complexity     | Space Complexity       |
| -------------------- | ------------------- | ---------------------- |
| `visited` array      | O(V)                | O(V)                   |
| DFS traversal        | O(V + E)            | O(V + E) (stack + adj) |
| Recursive call stack | Up to O(V) in depth | O(V)                   |
| `result` array       | O(V)                | O(V)                   |
| Overall              | ✅ **O(V + E)**      | ✅ **O(V + E)**         |

---

## ✅ 6. Real-World Use Cases of DFS (Very Important)

Here are a few **practical and critical applications** of DFS in the real world:

---

### 1. **Detecting Cycles in Graphs**

* Used in **compilers**, **deadlock detection**, and **network loops**.

---

### 2. **Topological Sorting (Precursor)**

* DFS helps in topological sort for **task scheduling**, **build systems**, and **dependency resolution** (e.g., `apt`, `npm`).

---

### 3. **Maze Solving & Path Finding**

* Used in **robot path planning**, **game AI**, and **navigation** when full exploration is needed.

---

### 4. **Web Crawlers**

* DFS-like approach is used to **traverse links deeply** from a given starting URL.

---

### 5. **Connected Component Detection**

* In **social networks** or **image segmentation**, DFS is used to find clusters or regions.

---
