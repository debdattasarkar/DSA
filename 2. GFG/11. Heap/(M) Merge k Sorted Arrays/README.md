# Merge k Sorted Arrays

## Problem Statement

Given **k** sorted arrays arranged in the form of a matrix of size `k × k`, the task is to merge them into one sorted array.

### Objective

Merge all the given `k` sorted arrays into a single sorted array and return the final array:

* As a **list** in Python
* As a **pointer to array** in C++
* As an **ArrayList** in Java

---

## Examples

### Example 1

**Input:**
`k = 3`
`arr[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

**Output:**
`1 2 3 4 5 6 7 8 9`

**Explanation:**
We merge 3 sorted arrays:

* \[1, 2, 3]
* \[4, 5, 6]
* \[7, 8, 9]

The final merged array is:
`[1, 2, 3, 4, 5, 6, 7, 8, 9]`

---

### Example 2

**Input:**
`k = 4`
`arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9]]`

**Output:**
`1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9`

**Explanation:**
The merged array from 4 sorted arrays results in:
`[1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]`

---

## Constraints

* `1 <= k <= 100`
* Each array is sorted

---

## Expected Time and Space Complexity

* **Time Complexity:** O(k² \* log(k))
* **Auxiliary Space:** O(k²)

---

## Approach

* Use a **Min Heap (Priority Queue)** to efficiently extract the smallest elements.
* Push the first element of each of the `k` arrays into the heap.
* Pop the smallest element and insert the next element of the same array.
* Continue until all elements are processed.

---

## Python Code

```python
import heapq

class Solution:
    def mergeKArrays(self, arr, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, (arr[i][0], i, 0))
        
        result = []
        while heap:
            val, row, col = heapq.heappop(heap)
            result.append(val)
            if col + 1 < k:
                heapq.heappush(heap, (arr[row][col + 1], row, col + 1))
        
        return result
```

---

## C++ Code

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> mergeKArrays(vector<vector<int>> arr, int k) {
        vector<int> result;

        using T = tuple<int, int, int>; // {value, row, col}
        priority_queue<T, vector<T>, greater<T>> pq;

        for (int i = 0; i < k; i++) {
            pq.emplace(arr[i][0], i, 0);
        }

        while (!pq.empty()) {
            auto [val, row, col] = pq.top();
            pq.pop();
            result.push_back(val);
            if (col + 1 < k) {
                pq.emplace(arr[row][col + 1], row, col + 1);
            }
        }

        return result;
    }
};
```

---

## JavaScript Code

```javascript
class Solution {
    mergeKArrays(arr, k) {
        const minHeap = new MinPriorityQueue({ priority: x => x[0] });
        const result = [];

        for (let i = 0; i < k; i++) {
            minHeap.enqueue([arr[i][0], i, 0]);
        }

        while (!minHeap.isEmpty()) {
            const [val, r, c] = minHeap.dequeue().element;
            result.push(val);
            if (c + 1 < k) {
                minHeap.enqueue([arr[r][c + 1], r, c + 1]);
            }
        }

        return result;
    }
}
```

*Note: You may need to use a library like `@datastructures-js/priority-queue` in JavaScript.*

---

## Tags

* Arrays
* Heap
* Sorting
* Algorithms
* Data Structures

---
