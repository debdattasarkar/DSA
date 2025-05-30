Here's the complete README for the **Minimum Cost Path** problem based on the provided GeeksforGeeks question:

---

# Minimum Cost Path

Given a square grid of size **N x N**, where each cell contains an integer cost to traverse that cell, the task is to find a **path from the top-left cell to the bottom-right cell** such that the **total traversal cost is minimized**.

From each cell `(i, j)`, you can move in four possible directions:

* Up `(i - 1, j)`
* Down `(i + 1, j)`
* Left `(i, j - 1)`
* Right `(i, j + 1)`

---

## 🧪 Examples

### Example 1

**Input:**

```plaintext
grid = {
    {9, 4, 9, 9},
    {6, 7, 6, 4},
    {8, 3, 3, 7},
    {7, 4, 9, 10}
}
```

**Output:**

```
43
```

**Explanation:**
The grid is:

```
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
```

One of the minimum cost paths is: `9 → 4 → 7 → 3 → 3 → 7 → 10 = 43`.

---

### Example 2

**Input:**

```plaintext
grid = {
    {4, 4},
    {3, 7}
}
```

**Output:**

```
14
```

**Explanation:**
The grid is:

```
4 4
3 7
```

Minimum cost path: `4 → 4 → 7 = 14`.

---

## ✅ Constraints

* `1 ≤ n ≤ 500`
* `1 ≤ cost of cells ≤ 500`

---

## 🧮 Expected Time and Space Complexity

* **Time Complexity:** `O(n² * log(n))`
* **Auxiliary Space:** `O(n²)`

---

## 💡 Approach

This problem is a classical application of **Dijkstra's Algorithm** on a grid, where each cell is treated as a node. A min-heap (priority queue) is used to greedily pick the path with the minimum accumulated cost at each step.

---

## 💻 Solution Implementations

### Python

```python
import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            if x == n - 1 and y == n - 1:
                return cost
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(min_heap, (cost + grid[nx][ny], nx, ny))
```

---

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int minimumCostPath(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dist(n, vector<int>(n, INT_MAX));
        priority_queue<pair<int, pair<int, int>>, 
                       vector<pair<int, pair<int, int>>>, 
                       greater<pair<int, pair<int, int>>>> pq;
                       
        dist[0][0] = grid[0][0];
        pq.push({grid[0][0], {0, 0}});
        vector<int> dx = {-1, 1, 0, 0};
        vector<int> dy = {0, 0, -1, 1};

        while (!pq.empty()) {
            auto [cost, cell] = pq.top(); pq.pop();
            int x = cell.first, y = cell.second;

            if (x == n - 1 && y == n - 1) return cost;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    int newCost = cost + grid[nx][ny];
                    if (newCost < dist[nx][ny]) {
                        dist[nx][ny] = newCost;
                        pq.push({newCost, {nx, ny}});
                    }
                }
            }
        }
        return dist[n - 1][n - 1];
    }
};
```

---

### JavaScript

```javascript
class Solution {
    minimumCostPath(grid) {
        const n = grid.length;
        const directions = [[-1,0],[1,0],[0,-1],[0,1]];
        const visited = Array.from({length: n}, () => Array(n).fill(false));
        const minHeap = [[grid[0][0], 0, 0]];
        
        while (minHeap.length > 0) {
            minHeap.sort((a, b) => a[0] - b[0]); // emulate min-heap
            const [cost, x, y] = minHeap.shift();

            if (x === n - 1 && y === n - 1) return cost;
            if (visited[x][y]) continue;
            visited[x][y] = true;

            for (let [dx, dy] of directions) {
                let nx = x + dx, ny = y + dy;
                if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
                    minHeap.push([cost + grid[nx][ny], nx, ny]);
                }
            }
        }
    }
}
```

---

## 🧠 Key Concepts

* **Graph Traversal** on a grid
* **Greedy Algorithm**
* **Dijkstra’s Algorithm**
* **Min-Heap / Priority Queue**

---

## 📁 Related Topics

* Graph
* Heap / Priority Queue
* Dynamic Programming (Alternative approach)
* Grid Traversal

---
