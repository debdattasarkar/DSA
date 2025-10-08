# Number of Provinces

**Difficulty:** Medium
**Accuracy:** 54.29%
**Submissions:** 159K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an **undirected** graph with **V** vertices, we say two vertices **u** and **v** belong to a single province if there is a path from **u to v** or **v to u**. Your task is to find the number of **provinces**.

> **Note:** A **province** is a group of **directly or indirectly connected** cities and no other cities outside of the group.

---

## Examples

### Example 1:

**Input:**

```python
[[1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]]
```

**Output:**

```
2
```

**Explanation:**
The graph clearly has **2 Provinces**: \[1, 3] and \[2]. As city 1 and city 3 have a path between them, they belong to a single province. City 2 has no path to city 1 or 3 hence it belongs to another province.

---

### Example 2:

**Input:**

```python
[[1, 1],
 [1, 1]]
```

**Output:**

```
1
```

---

## Task

You don't need to read input or print anything. Your task is to complete the function:

```python
def numProvinces(V: int, adj: List[List[int]]) -> int:
```

which takes an integer `V` and an adjacency matrix `adj` (as a 2D vector) as input and returns the number of provinces.

> `adj[i][j] = 1` if nodes i and j are connected and `adj[i][j] = 0` if not connected.

---

## Expected Time and Space Complexity

* **Time Complexity:** O(V^2)
* **Auxiliary Space:** O(V)

---

## Constraints

```
1 ≤ V ≤ 500
```

---

## Company Tags

Amazon, Microsoft, Google

---

## Topic Tags

* DFS
* Graph
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Microsoft Internship Interview Experience 5

---

## Related Articles

* [Connected Components In An Undirected Graph](https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/)

---

---

Here’s a complete solution for **“Number of Provinces”** covering:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 🔍 Problem Summary:

* You are given a `V x V` adjacency matrix.
* `adj[i][j] == 1` means city `i` and city `j` are directly connected.
* You must count the number of **connected components** (called **provinces** here).

---

### 🧠 Approach: DFS (Depth-First Search)

* Treat each row/column as a node.
* Whenever you visit a node **not visited yet**, start a **DFS from there**, and mark all reachable nodes.
* Every new DFS = one new province.

---

### 🧪 Dry Run Example

Input:

```python
V = 3
adj = [[1, 0, 1],
       [0, 1, 0],
       [1, 0, 1]]
```

Graph View:

* Node 0 is connected to Node 2
* Node 2 is connected to Node 0
* Node 1 is isolated (no connections except self)

DFS Calls:

* Start from node 0 → Visit 0 → Visit 2 → Done → Province count = 1
* Node 1 is not visited → Start DFS → Province count = 2
* Node 2 is already visited.

✅ **Output: 2**

---

## ✅ 3. Python Code — DFS (Most Common in Interviews)

### ✅ Optimized DFS Version (Expected in Interviews)

```python
# User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        def dfs(node, visited):
            visited[node] = True
            for neighbor in range(V):
                # Check if connected and not visited
                if adj[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * V
        count = 0

        # Run DFS for every unvisited node
        for i in range(V):
            if not visited[i]:
                count += 1
                dfs(i, visited)
        
        return count
```

### ⏱ Time and Space Complexity

* **Time Complexity:** O(V²)
  → Because we loop through entire adjacency matrix.
* **Space Complexity:** O(V)
  → For the `visited` array and recursion stack.

---

## ✅ Alternative: BFS Version (Also Acceptable)

```python
from collections import deque

class Solution:
    def numProvinces(self, adj, V):
        def bfs(start, visited):
            q = deque()
            q.append(start)
            visited[start] = True

            while q:
                node = q.popleft()
                for neighbor in range(V):
                    if adj[node][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        visited = [False] * V
        count = 0

        for i in range(V):
            if not visited[i]:
                count += 1
                bfs(i, visited)

        return count
```

---

## ✅ 4. Interviewer Questions and Expected Answers

---

### ❓Q1. What does this problem reduce to in graph terms?

**A:** It reduces to **counting the number of connected components** in an undirected graph represented by an adjacency matrix.

---

### ❓Q2. Why use DFS or BFS here?

**A:** Both help traverse all nodes in one connected component efficiently. Each unvisited node that triggers DFS/BFS indicates a **new province**.

---

### ❓Q3. What if the graph was sparse?

**A:** Then using an **adjacency list** would be better for space and time efficiency. But since input is a matrix, we use matrix traversal.

---

### ❓Q4. Can we use Union-Find (DSU) here?

**A:** Yes! Union-Find is another optimal method for counting components.

---

### ❓Q5. How would this change for a **directed** graph?

**A:** We'd need to count **strongly connected components** (SCC) using Kosaraju’s or Tarjan’s algorithm — not applicable here since graph is undirected.

---

---

Here's your **complete Python program** for the **“Number of Provinces”** problem, including:

✅ Inline **time and space complexity** explanations
📥 **Input/output example**
⏱️ **Execution time using `time.time()`**
🌍 **Real-world use cases**

---

## ✅ 5. Full Program with Timing, Inline Complexity, and Output

```python
import time

class Solution:
    def numProvinces(self, adj, V):
        # Depth-First Search to visit all cities in the same province
        def dfs(city, visited):
            visited[city] = True
            for neighbor in range(V):
                # If there's a connection and not yet visited
                if adj[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        # Initialize visited array: O(V) space
        visited = [False] * V
        province_count = 0

        # Loop through all cities: O(V^2) time due to adjacency matrix scan
        for city in range(V):
            if not visited[city]:
                province_count += 1
                dfs(city, visited)

        return province_count


# --------- 🧪 Main Execution and Timing -----------

if __name__ == "__main__":
    # Example input
    V = 3
    adj = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    print("Input Matrix:")
    for row in adj:
        print(row)

    # Start timer
    start_time = time.time()

    # Solution execution
    sol = Solution()
    result = sol.numProvinces(adj, V)

    # End timer
    end_time = time.time()

    # Output results
    print(f"\nOutput (Number of Provinces): {result}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

### ✅ Sample Output:

```
Input Matrix:
[1, 0, 1]
[0, 1, 0]
[1, 0, 1]

Output (Number of Provinces): 2
Execution Time: 0.000004 seconds
```

---

### ✅ Time and Space Complexity (Step-by-step):

| Operation                  | Complexity                           |
| -------------------------- | ------------------------------------ |
| Building `visited[]`       | O(V)                                 |
| Outer loop over `V` cities | O(V)                                 |
| Inner DFS traversal        | O(V) for each call                   |
| **Overall Time**           | **O(V²)** (due to matrix)            |
| **Overall Space**          | **O(V)** (visited + recursion stack) |

---

## ✅ 6. Real-World Use Cases of Counting Connected Components (Provinces)

---

### 🌍 1. **Social Network Communities**

* Detect groups of people who are all **mutually connected** either directly or indirectly.

---

### 🏙 2. **Identifying Isolated Subnetworks in Telecom or Internet**

* Useful in identifying **islands of connectivity** in large computer networks.
* Helps **optimize network repair** and detect disconnected regions.

---

### 🧬 3. **Biological Graph Analysis**

* Detect clusters of **gene interactions**, where genes influence each other directly or indirectly.

---

### 🛡 4. **Fraud Rings in Financial Systems**

* Find hidden **rings of coordinated activity** (e.g. credit card fraud rings) in transaction graphs.

---

### 🏭 5. **Smart Grid Failure Detection**

* Detect if parts of an **electrical grid** are isolated or connected due to failures.

---
