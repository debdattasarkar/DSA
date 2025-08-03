# Find Median in a Stream

## Problem Statement

Given a stream of integers (`arr[]`), where numbers are read one by one, the task is to determine the **median of the elements** encountered so far after each new integer is read.

There are **two cases** for determining the median:

1. If the data set has an **odd number** of elements, the **middle** one is considered the median.
2. If the data set has an **even number** of elements, the **arithmetic mean** of the two middle values is the median.

---

## Examples

### Example 1

**Input:**
`arr[] = [5, 15, 1, 3, 2, 8]`

**Output:**
`[5.0, 10.0, 5.0, 4.0, 3.0, 4.0]`

**Explanation:**

* After reading 1st: `[5]` → median = 5.0
* After 2nd: `[5, 15]` → median = (5+15)/2 = 10.0
* After 3rd: `[5, 15, 1]` → median = 5.0
* After 4th: `[5, 15, 1, 3]` → median = (3+5)/2 = 4.0
* After 5th: `[5, 15, 1, 3, 2]` → median = 3.0
* After 6th: `[5, 15, 1, 3, 2, 8]` → median = (3+5)/2 = 4.0

---

### Example 2

**Input:**
`arr[] = [2, 2, 2, 2]`
**Output:**
`[2.0, 2.0, 2.0, 2.0]`

**Explanation:**
All values are equal. So, the median is always 2.0.

---

## Constraints

* `1 <= arr.size() <= 10^5`
* `1 <= arr[i] <= 10^6`

---

## Expected Time and Space Complexity

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## Approach

This problem is optimally solved using **two heaps**:

* A **max-heap** (`low`) to store the smaller half of the elements.
* A **min-heap** (`high`) to store the larger half of the elements.

### Steps:

1. For each element:

   * Add to the appropriate heap.
   * Balance the two heaps (their sizes differ by at most 1).
   * Extract the median:

     * If both heaps are of equal size → average of roots.
     * Else → root of the heap with more elements.

---

## Tags

* Heap
* Design-Pattern
* Data Structures

---

Here’s a **complete explanation with a step-by-step dry run** for the **Find Median in a Stream** problem, followed by the **correct implementations** in **Python**, **C++**, and **JavaScript**, with **inline comments**.

---

## 🔍 Problem Overview

You are given a stream of integers (an array `arr[]`). Your task is to **return a list of medians** as new elements arrive one by one.

### Median Rules:

* If the count of numbers is **odd**, the median is the **middle number**.
* If the count is **even**, the median is the **average of the two middle numbers**.

---

## ✅ Step-by-Step Dry Run

### Input:

```
arr = [5, 15, 1, 3, 2, 8]
```

### Heaps used:

* `low` (Max Heap): to store the **lower half**.
* `high` (Min Heap): to store the **higher half**.

### Iteration-wise State:

```
1. Insert 5:
   - low = [5]
   - median = 5.0

2. Insert 15:
   - low = [5], high = [15]
   - median = (5+15)/2 = 10.0

3. Insert 1:
   - low = [5, 1], high = [15]
   - balance → move 5 to high
   - low = [1], high = [5, 15]
   - rebalance → move 5 back to low
   - median = 5.0

4. Insert 3:
   - low = [5, 1, 3], high = [15]
   - balance → move 5 to high
   - low = [3, 1], high = [5, 15]
   - median = (3+5)/2 = 4.0

5. Insert 2:
   - low = [3, 1, 2], high = [5, 15]
   - median = 3.0

6. Insert 8:
   - low = [3, 1, 2], high = [5, 15, 8]
   - median = (3+5)/2 = 4.0
```

### Output:

```
[5.0, 10.0, 5.0, 4.0, 3.0, 4.0]
```

---

## ✅ Python Code

```python
import heapq

class Solution:
    def getMedian(self, arr):
        low = []  # max-heap (invert values)
        high = []  # min-heap
        result = []

        for num in arr:
            # Insert into max heap (as negative number)
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
            else:
                heapq.heappush(high, num)

            # Rebalance heaps
            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            elif len(high) > len(low):
                heapq.heappush(low, -heapq.heappop(high))

            # Get median
            if len(low) == len(high):
                median = (-low[0] + high[0]) / 2.0
            else:
                median = float(-low[0])
            result.append(median)

        return result
```

---

## ✅ C++ Code

```cpp
#include <queue>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<double> getMedian(vector<int> &arr) {
        priority_queue<int> low; // max-heap
        priority_queue<int, vector<int>, greater<int>> high; // min-heap
        vector<double> result;

        for (int num : arr) {
            if (low.empty() || num <= low.top()) {
                low.push(num);
            } else {
                high.push(num);
            }

            // Balance the heaps
            if (low.size() > high.size() + 1) {
                high.push(low.top());
                low.pop();
            } else if (high.size() > low.size()) {
                low.push(high.top());
                high.pop();
            }

            // Calculate median
            if (low.size() == high.size()) {
                result.push_back((low.top() + high.top()) / 2.0);
            } else {
                result.push_back(low.top());
            }
        }
        return result;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class MinHeap {
    constructor() { this.data = []; }
    push(val) {
        this.data.push(val);
        this.data.sort((a, b) => a - b);
    }
    pop() { return this.data.shift(); }
    top() { return this.data[0]; }
    size() { return this.data.length; }
}

class MaxHeap {
    constructor() { this.data = []; }
    push(val) {
        this.data.push(val);
        this.data.sort((a, b) => b - a);
    }
    pop() { return this.data.shift(); }
    top() { return this.data[0]; }
    size() { return this.data.length; }
}

class Solution {
    getMedian(arr) {
        let low = new MaxHeap();  // max-heap
        let high = new MinHeap(); // min-heap
        let result = [];

        for (let num of arr) {
            if (low.size() === 0 || num <= low.top()) {
                low.push(num);
            } else {
                high.push(num);
            }

            if (low.size() > high.size() + 1) {
                high.push(low.pop());
            } else if (high.size() > low.size()) {
                low.push(high.pop());
            }

            if (low.size() === high.size()) {
                result.push((low.top() + high.top()) / 2);
            } else {
                result.push(low.top());
            }
        }

        return result;
    }
}
```

---
