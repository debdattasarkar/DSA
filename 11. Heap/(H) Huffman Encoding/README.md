Here's a comprehensive `README.md` file for the problem **"Minimum Cost Path"** as described in the uploaded image:

---

# Minimum Cost Path

## Introduction

Given a square grid of size **N**, where each cell contains an integer representing the **cost** to traverse that cell, the goal is to find the path from the **top-left** cell to the **bottom-right** cell such that the total cost incurred is **minimum**. Movements are allowed in **4 directions**: up, down, left, and right.

---

## Table of Contents

* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Time and Space Complexity](#expected-time-and-space-complexity)
* [Approach](#approach)
* [Code](#code)

  * [Python](#python)
  * [C++](#c)
  * [JavaScript](#javascript)

---

## Examples

### Example 1

**Input**:

```
grid = {
    {9, 4, 9, 9},
    {6, 7, 6, 4},
    {8, 3, 3, 7},
    {7, 4, 9, 10}
}
```

**Output**: `43`

**Explanation**: The minimum path is 9 → 4 → 7 → 3 → 3 → 7 → 10 = **43**

---

### Example 2

**Input**:

```
grid = {
    {4, 4},
    {3, 7}
}
```

**Output**: `14`

**Explanation**: The minimum path is 4 → 3 → 7 = **14**

---

## Constraints

* $1 \leq n \leq 500$
* $1 \leq \text{cost of cells} \leq 500$

---

## Expected Time and Space Complexity

* **Time Complexity**: $O(n^2 \cdot \log n)$
* **Auxiliary Space**: $O(n^2)$

---

## Approach

We apply **Dijkstra's Algorithm** using a **min-heap (priority queue)** to always expand the least costly path first.

1. Start at cell (0,0) with its own cost.
2. Use a priority queue to push the next candidate cells.
3. Maintain a 2D `distance` matrix to store the minimum cost to reach each cell.
4. At each step, update the cost of adjacent cells (up, down, left, right) if a cheaper path is found.
5. Continue until you reach the bottom-right cell.

---

## Code

### Python

```python
import heapq

class Solution:
    def minimumCostPath(self, grid):
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            cost, x, y = heapq.heappop(heap)
            if x == n - 1 and y == n - 1:
                return cost
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))
```

---

### C++

```cpp
#include <vector>
#include <queue>
#include <climits>
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

        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};

        while (!pq.empty()) {
            auto [cost, coords] = pq.top();
            int x = coords.first;
            int y = coords.second;
            pq.pop();

            if (x == n - 1 && y == n - 1) return cost;

            for (int i = 0; i < 4; ++i) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                    int new_cost = cost + grid[nx][ny];
                    if (new_cost < dist[nx][ny]) {
                        dist[nx][ny] = new_cost;
                        pq.push({new_cost, {nx, ny}});
                    }
                }
            }
        }
        return -1;
    }
};
```

---

### JavaScript

```javascript
class Solution {
    minimumCostPath(grid) {
        const n = grid.length;
        const dist = Array.from({ length: n }, () => Array(n).fill(Infinity));
        dist[0][0] = grid[0][0];

        const minHeap = new MinPriorityQueue({ priority: x => x[0] });
        minHeap.enqueue([grid[0][0], 0, 0]);

        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        while (!minHeap.isEmpty()) {
            const [cost, x, y] = minHeap.dequeue().element;

            if (x === n - 1 && y === n - 1) return cost;

            for (const [dx, dy] of directions) {
                const nx = x + dx, ny = y + dy;
                if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                    const newCost = cost + grid[nx][ny];
                    if (newCost < dist[nx][ny]) {
                        dist[nx][ny] = newCost;
                        minHeap.enqueue([newCost, nx, ny]);
                    }
                }
            }
        }

        return -1;
    }
}
```

---

## Related

* [Minimum Cost Path Left Right Bottom Moves Allowed](https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/)
* Topics: Graph, Heap, Dijkstra, DP

---