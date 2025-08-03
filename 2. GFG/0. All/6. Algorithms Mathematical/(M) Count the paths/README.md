
# 🔢 Count the Paths
---

## 🧾 Problem Statement

Given a **Directed Acyclic Graph (DAG)** with `V` nodes labeled from `0` to `V-1` and a list of directed edges, count the **total number of distinct paths** from a given `start` node to a `destination` node.

Each edge is represented as:
`edges[i] = [u, v]`
indicating a directed edge from node `u` to node `v`.

---

## 🧪 Examples

### Example 1:

```text
Input: 
edges = [[0,1], [0,3], [2,0], [2,1], [1,3]], 
V = 4, src = 2, dest = 3

Output: 
3

Explanation: 
There are three paths from node 2 to 3:
2 → 1 → 3  
2 → 0 → 3  
2 → 0 → 1 → 3
```

### Example 2:

```text
Input:
edges = [[0,1], [1,2], [1,3], [2,3]], 
V = 4, src = 0, dest = 3

Output:
2

Explanation:
There are two paths from 0 to 3:
0 → 1 → 2 → 3  
0 → 1 → 3
```

---

## 📌 Constraints

* 2 ≤ V ≤ 10³
* 1 ≤ E = edges.size() ≤ (V × (V - 1)) / 2

---

## ⏱ Expected Complexities

* **Time Complexity:** O(V + E)
* **Auxiliary Space:** O(V + E)

---

## 🏷️ Topic Tags

`Dynamic Programming` `DFS` `Graph` `Data Structures` `Algorithms`

---

## 📚 Related Articles

* [Find Paths Given Source Destination](#)
* [Number of Paths from Source to Destination in a DAG](#)

---
Here's the **detailed explanation with dry run** followed by the implementation in **Python**, **C++**, and **JavaScript**.

---

## 🧠 Problem Understanding: Count Paths in DAG

You are given a **Directed Acyclic Graph (DAG)** represented by `V` vertices and a list of directed edges. You need to **count the number of distinct paths** from a **source** node (`src`) to a **destination** node (`dest`).

---

## 🪜 Approach: DFS + Memoization (Top-Down DP)

### Idea:

* Build an **adjacency list** from edges.
* Use **DFS traversal** from `src` to `dest`.
* Use **memoization** (`dp[node]`) to store number of paths from each node to `dest`.

---

## 🧪 Dry Run Example

### Input:

```
edges = [[0,1],[0,3],[2,0],[2,1],[1,3]]
V = 4, src = 2, dest = 3
```

### Paths from 2 to 3:

1. 2 → 0 → 3
2. 2 → 0 → 1 → 3
3. 2 → 1 → 3
   **Total = 3 paths**

---

## ✅ Python Code

```python
class Solution:
    def countPaths(self, edges, V, src, dest):
        from collections import defaultdict

        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        memo = [-1] * V  # dp[node] = number of paths from node to dest

        def dfs(node):
            if node == dest:
                return 1
            if memo[node] != -1:
                return memo[node]
            total = 0
            for neighbor in graph[node]:
                total += dfs(neighbor)
            memo[node] = total
            return total

        return dfs(src)
```

---

## 💠 C++ Code

```cpp
class Solution {
  public:
    int countPaths(vector<vector<int>>& edges, int V, int src, int dest) {
        vector<vector<int>> graph(V);
        for (auto& edge : edges)
            graph[edge[0]].push_back(edge[1]);

        vector<int> memo(V, -1);

        function<int(int)> dfs = [&](int node) {
            if (node == dest) return 1;
            if (memo[node] != -1) return memo[node];

            int total = 0;
            for (int neighbor : graph[node])
                total += dfs(neighbor);

            return memo[node] = total;
        };

        return dfs(src);
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    countPaths(edges, V, src, dest) {
        const graph = Array.from({ length: V }, () => []);
        for (let [u, v] of edges) {
            graph[u].push(v);
        }

        const memo = Array(V).fill(-1);

        const dfs = (node) => {
            if (node === dest) return 1;
            if (memo[node] !== -1) return memo[node];

            let total = 0;
            for (let neighbor of graph[node]) {
                total += dfs(neighbor);
            }

            memo[node] = total;
            return total;
        };

        return dfs(src);
    }
}
```

---

## ⏱ Time and Space Complexity

| Type              | Complexity |
| ----------------- | ---------- |
| Time Complexity   | O(V + E)   |
| Space Complexity  | O(V + E)   |
| Memoization Space | O(V)       |

---

