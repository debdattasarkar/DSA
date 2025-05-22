Here’s the **README** file based on the GeeksforGeeks problem "Merge K Sorted Arrays":

---

# Merge K Sorted Arrays

## 🧩 Problem Statement

Given **K sorted arrays** arranged in the form of a matrix of size `k * k`, the task is to merge them into one **sorted array**.

Return the merged sorted array:

* as a pointer to the merged array in **C++**,
* as an **ArrayList** in **Java**,
* and as a **list** in **Python**.

---

## 📥 Input Format

* An integer `k` representing the number of sorted arrays.
* A 2D list `arr[][]` of size `k * k`, where each row represents a sorted array.

---

## 📤 Output Format

* A single sorted list containing all the elements from the K arrays.

---

## 🧪 Examples

### Example 1

```
Input:
k = 3
arr[][] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
}

Output:
1 2 3 4 5 6 7 8 9

Explanation:
Merged array of the three sorted arrays is [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 2

```
Input:
k = 4
arr[][] = {
  {1, 2, 2, 3},
  {2, 2, 3, 4},
  {5, 5, 6, 6},
  {7, 8, 9, 9}
}

Output:
1 2 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9
```

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity**: O(k² \* log(k))
* **Auxiliary Space**: O(k²)

---

## 🔒 Constraints

* 1 ≤ k ≤ 100

---

## 🧠 Approach

* Use a **min heap** to efficiently get the smallest among the current elements of all arrays.
* Store tuple (element, array index, element index) in the heap.
* Continue popping the minimum element and pushing the next element from the same array into the heap.

---

## 🛠️ Languages Supported

* **Python**
* **C++**
* **Java**

---

## 💼 Company Tags

* VMWare
* Flipkart
* Amazon
* Microsoft
* Citrix

---

## 🏷️ Topic Tags

* Arrays
* Sorting
* Heap
* Data Structures
* Algorithms

---

## 📚 Related Resources

* [Merge K Sorted Arrays](https://www.geeksforgeeks.org/merge-k-sorted-arrays/)
* [Sort Numbers Stored On Different Machines](https://www.geeksforgeeks.org/sort-numbers-stored-on-different-machines/)

---

Sure! Here's a **step-by-step dry run explanation**, followed by complete **Python, C++, and JavaScript** solutions with inline comments for the **"Merge K Sorted Arrays"** problem from GeeksforGeeks.

---

## 📘 Problem Summary

Given `k` sorted arrays (each of size `k`), merge them into one sorted array.

---

## 🧠 Step-by-Step Explanation

We use a **Min Heap** to track the smallest available elements across all the arrays.

### Dry Run

**Input:**

```python
arr = [
  [1, 3, 5],
  [2, 4, 6],
  [0, 8, 9]
]
K = 3
```

### Initial Heap Insertion:

We insert the first element of each array along with its (array index, element index):

```
Heap: [(1, 0, 0), (2, 1, 0), (0, 2, 0)]
```

**Step-by-step Extraction and Insertion:**

* Pop (0, 2, 0): Add 0 to result → Push (8, 2, 1)
* Pop (1, 0, 0): Add 1 → Push (3, 0, 1)
* Pop (2, 1, 0): Add 2 → Push (4, 1, 1)
* Pop (3, 0, 1): Add 3 → Push (5, 0, 2)
* Pop (4, 1, 1): Add 4 → Push (6, 1, 2)
* Pop (5, 0, 2): Add 5 → no more elements in array 0
* Pop (6, 1, 2): Add 6 → no more elements in array 1
* Pop (8, 2, 1): Add 8 → Push (9, 2, 2)
* Pop (9, 2, 2): Add 9 → Done

### ✅ Output:

```python
[0, 1, 2, 3, 4, 5, 6, 8, 9]
```

---

## ✅ Python Code (with Comments)

```python
import heapq

class Solution:
    def mergeKArrays(self, arr, K):
        # Min heap to keep track of the minimum element
        min_heap = []
        
        # Step 1: Push the first element of each array into the heap
        for i in range(K):
            heapq.heappush(min_heap, (arr[i][0], i, 0))  # (value, row, col)
        
        result = []
        
        # Step 2: Extract min and insert next element from the same row
        while min_heap:
            val, row, col = heapq.heappop(min_heap)
            result.append(val)
            if col + 1 < K:
                heapq.heappush(min_heap, (arr[row][col + 1], row, col + 1))
        
        return result
```

---

## ✅ C++ Code (with Comments)

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
  public:
    vector<int> mergeKArrays(vector<vector<int>> arr, int K) {
        // Min heap using priority_queue with custom comparator
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        
        // Step 1: Insert first element of each array
        for (int i = 0; i < K; ++i) {
            pq.push({arr[i][0], i, 0});
        }

        vector<int> result;

        // Step 2: Extract min and insert next element from same row
        while (!pq.empty()) {
            auto [val, row, col] = pq.top(); pq.pop();
            result.push_back(val);
            if (col + 1 < K) {
                pq.push({arr[row][col + 1], row, col + 1});
            }
        }

        return result;
    }
};
```

---

## ✅ JavaScript Code (with Comments)

```javascript
class MinHeap {
    constructor() {
        this.heap = [];
    }

    insert(val) {
        this.heap.push(val);
        this.bubbleUp();
    }

    extractMin() {
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown();
        }
        return min;
    }

    bubbleUp() {
        let idx = this.heap.length - 1;
        const element = this.heap[idx];

        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.heap[parentIdx];
            if (element[0] >= parent[0]) break;
            this.heap[idx] = parent;
            this.heap[parentIdx] = element;
            idx = parentIdx;
        }
    }

    sinkDown() {
        let idx = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftIdx = 2 * idx + 1;
            let rightIdx = 2 * idx + 2;
            let left, right;
            let swap = null;

            if (leftIdx < length) {
                left = this.heap[leftIdx];
                if (left[0] < element[0]) swap = leftIdx;
            }

            if (rightIdx < length) {
                right = this.heap[rightIdx];
                if (
                    (swap === null && right[0] < element[0]) ||
                    (swap !== null && right[0] < left[0])
                ) {
                    swap = rightIdx;
                }
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
    mergeKArrays(arr, K) {
        const heap = new MinHeap();

        // Step 1: Add first element of each array
        for (let i = 0; i < K; i++) {
            heap.insert([arr[i][0], i, 0]); // [value, row, col]
        }

        const result = [];

        // Step 2: Continue extracting min and pushing next
        while (heap.size() > 0) {
            let [val, row, col] = heap.extractMin();
            result.push(val);
            if (col + 1 < K) {
                heap.insert([arr[row][col + 1], row, col + 1]);
            }
        }

        return result;
    }
}
```

---

Let me know if you'd like this wrapped into a README or tested with your own custom input.
