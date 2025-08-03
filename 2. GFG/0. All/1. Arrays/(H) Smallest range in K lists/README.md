
# Smallest Range in K Lists

## Introduction

The **Smallest Range in K Lists** problem is a common algorithmic challenge often solved with a combination of heaps and pointers. Given multiple sorted lists, the task is to find the **smallest range** that includes **at least one number from each of the lists**. If there are multiple such ranges, the **first one** encountered should be returned.

This problem is especially useful in understanding advanced data structures and heap manipulation.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

Given a 2D integer array `arr[ ][ ]` of size `k * n`, where:

* Each of the `k` rows contains `n` integers sorted in **ascending order**.

Find the smallest range `[l, r]` such that:

* The range includes **at least one element** from each of the `k` lists.

If multiple such ranges exist, return the **first one** found.

---

## Examples

### Example 1

```
Input:
n = 5, k = 3
arr[][] = [[4, 7, 9, 12, 15],
           [0, 8, 10, 14, 20],
           [6, 12, 16, 30, 50]]

Output: [6, 8]

Explanation: Range [6, 8] includes 7 from the first list, 8 from the second, and 6 from the third.
```

### Example 2

```
Input:
n = 5, k = 3
arr[][] = [[1, 3, 5, 7, 9],
           [0, 2, 4, 6, 8],
           [2, 3, 5, 7, 11]]

Output: [1, 2]

Explanation: 1 from the first list, and 2 from both second and third lists.
```

### Example 3

```
Input:
n = 2, k = 3
arr[][] = [[2, 4],
           [1, 7],
           [20, 40]]

Output: [4, 20]

Explanation: Includes 4 (first list), 7 (second), 20 (third).
```

---

## Constraints

* `1 ≤ k, n ≤ 500`
* `0 ≤ arr[i][j] ≤ 10^5`

---

## Expected Complexity

* **Time Complexity**: O(n \* k \* log k)
* **Auxiliary Space**: O(k)

---

## Tags

### Company Tags

`Flipkart`, `Amazon`

### Topic Tags

`Arrays`, `Heap`, `Data Structures`

---

## Related Content

* **Interview Experience**: Flipkart Interview Set 8 SDE 1
* **Article**: Find Smallest Range Containing Elements From K Lists

---

Here's the full explanation, dry run, and code implementations (Python, C++, JavaScript) for the **"Smallest Range in K Lists"** problem.

---

### ✅ Problem Summary

Given `k` sorted lists of size `n`, find the smallest range `[l, r]` that includes at least one element from each of the `k` lists.

---

### 💡 Key Idea

Use a **min-heap** to maintain the smallest current element from each list. At each step:

1. Push the next element from the list whose element was popped.
2. Track the current **max element** in the heap.
3. Update the result if the current range is smaller than the previous best.

---

### 🧪 Dry Run

Input:

```python
arr = [
    [4, 7, 9, 12, 15],
    [0, 8, 10, 14, 20],
    [6, 12, 16, 30, 50]
]
```

Initial heap:

```
(4, 0, 0), (0, 1, 0), (6, 2, 0)
max = 6 → range = [0, 6] → min = 0 (from list 1)
→ push 8 (from list 1) → heap = (4, 0, 0), (6, 2, 0), (8, 1, 1) → max = 8
→ new range = [4, 8] → better than previous
→ continue until best = [6, 8]
```

---

### 🐍 Python Code

```python
import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])

        heap = []
        max_val = float('-inf')

        # Initialize heap with first element from each list
        for i in range(k):
            heapq.heappush(heap, (arr[i][0], i, 0))
            max_val = max(max_val, arr[i][0])

        best_range = [float('-inf'), float('inf')]

        while True:
            min_val, row, idx = heapq.heappop(heap)

            # Update range if smaller
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]

            # Move to next element in the same list
            if idx + 1 == n:
                break
            next_val = arr[row][idx + 1]
            heapq.heappush(heap, (next_val, row, idx + 1))
            max_val = max(max_val, next_val)

        return best_range
```

---

### 💻 C++ Code

```cpp
class Solution {
  public:
    vector<int> findSmallestRange(vector<vector<int>>& arr) {
        int k = arr.size(), n = arr[0].size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> minHeap;

        int maxVal = INT_MIN;
        for (int i = 0; i < k; ++i) {
            minHeap.emplace(arr[i][0], i, 0);
            maxVal = max(maxVal, arr[i][0]);
        }

        int rangeStart = 0, rangeEnd = INT_MAX;

        while (true) {
            auto [minVal, row, idx] = minHeap.top();
            minHeap.pop();

            if (maxVal - minVal < rangeEnd - rangeStart) {
                rangeStart = minVal;
                rangeEnd = maxVal;
            }

            if (idx + 1 == n) break;

            int nextVal = arr[row][idx + 1];
            minHeap.emplace(nextVal, row, idx + 1);
            maxVal = max(maxVal, nextVal);
        }

        return {rangeStart, rangeEnd};
    }
};
```

---

### 🌐 JavaScript Code

```javascript
class Solution {
    findSmallestRange(arr) {
        let k = arr.length, n = arr[0].length;
        let minHeap = [];
        let maxVal = -Infinity;

        for (let i = 0; i < k; i++) {
            minHeap.push([arr[i][0], i, 0]);
            maxVal = Math.max(maxVal, arr[i][0]);
        }

        minHeap.sort((a, b) => a[0] - b[0]);

        let bestRange = [-Infinity, Infinity];

        while (true) {
            let [minVal, row, idx] = minHeap.shift();
            if (maxVal - minVal < bestRange[1] - bestRange[0]) {
                bestRange = [minVal, maxVal];
            }

            if (idx + 1 === n) break;

            let nextVal = arr[row][idx + 1];
            minHeap.push([nextVal, row, idx + 1]);
            maxVal = Math.max(maxVal, nextVal);
            minHeap.sort((a, b) => a[0] - b[0]);
        }

        return bestRange;
    }
}
```

---

### 📊 Time & Space Complexity

* **Time Complexity:** `O(n * k * log k)` — where `k` is number of lists and `n` is size of each list.
* **Space Complexity:** `O(k)` for the heap.
