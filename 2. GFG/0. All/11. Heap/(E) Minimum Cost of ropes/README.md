# Minimum Cost of Ropes

## Problem Statement

Given an array `arr[]` representing lengths of ropes, the goal is to connect all ropes into a single rope with the **minimum total cost**. The **cost** to connect two ropes is equal to the **sum of their lengths**.

To achieve this with minimum cost, always connect the **two smallest ropes** first, and use a **Min-Heap (Priority Queue)** to manage the rope lengths efficiently.

---

## Examples

### Example 1

**Input:**
`arr[] = [4, 3, 2, 6]`
**Output:**
`29`
**Explanation:**

* Combine 2 and 3 → Cost = 5 → Array becomes \[4, 5, 6]
* Combine 4 and 5 → Cost = 9 → Array becomes \[6, 9]
* Combine 6 and 9 → Cost = 15
* **Total cost = 5 + 9 + 15 = 29**

### Example 2

**Input:**
`arr[] = [4, 2, 7, 6, 9]`
**Output:**
`62`
**Explanation:**

* Combine 2 and 4 → Cost = 6 → \[6, 7, 6, 9]
* Combine 6 and 6 → Cost = 12 → \[7, 9, 12]
* Combine 7 and 9 → Cost = 16 → \[12, 16]
* Combine 12 and 16 → Cost = 28
* **Total cost = 6 + 12 + 16 + 28 = 62**

### Example 3

**Input:**
`arr[] = [10]`
**Output:**
`0`
**Explanation:**
Only one rope, so no cost.

---

## Constraints

* 1 ≤ `arr.size()` ≤ 10⁵
* 1 ≤ `arr[i]` ≤ 10⁴

---

## Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## Approach

Use a Min Heap (Priority Queue):

1. Insert all rope lengths into the heap.
2. While heap size > 1:

   * Extract two smallest ropes.
   * Combine them and compute cost.
   * Push the combined rope back into heap.
3. Sum up all intermediate costs.

---

## C++ Code

```cpp
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    long long minCost(long long arr[], long long n) {
        priority_queue<long long, vector<long long>, greater<long long>> pq(arr, arr + n);
        long long totalCost = 0;

        while (pq.size() > 1) {
            long long first = pq.top(); pq.pop();
            long long second = pq.top(); pq.pop();
            long long cost = first + second;
            totalCost += cost;
            pq.push(cost);
        }

        return totalCost;
    }
};
```

---

## Python Code

```python
import heapq

class Solution:
    def minCost(self, arr):
        heapq.heapify(arr)
        total_cost = 0
        
        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            cost = first + second
            total_cost += cost
            heapq.heappush(arr, cost)
        
        return total_cost
```

---

## JavaScript Code

```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        this.bubbleUp();
    }

    pop() {
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.bubbleDown();
        }
        return min;
    }

    bubbleUp() {
        let idx = this.heap.length - 1;
        const element = this.heap[idx];

        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.heap[parentIdx];

            if (element >= parent) break;

            this.heap[parentIdx] = element;
            this.heap[idx] = parent;
            idx = parentIdx;
        }
    }

    bubbleDown() {
        let idx = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let left = 2 * idx + 1;
            let right = 2 * idx + 2;
            let swap = null;

            if (left < length && this.heap[left] < element) {
                swap = left;
            }

            if (right < length && this.heap[right] < (swap === null ? element : this.heap[left])) {
                swap = right;
            }

            if (swap === null) break;
            this.heap[idx] = this.heap[swap];
            this.heap[swap] = element;
            idx = swap;
        }
    }

    size() {
        return this.heap.length;
    }
}

class Solution {
    minCost(arr) {
        const heap = new MinHeap();
        arr.forEach(num => heap.push(num));
        let totalCost = 0;

        while (heap.size() > 1) {
            const first = heap.pop();
            const second = heap.pop();
            const cost = first + second;
            totalCost += cost;
            heap.push(cost);
        }

        return totalCost;
    }
}
```

---

## Related Topics

* Heap
* Priority Queue
* Greedy Algorithms
* Data Structures

---
