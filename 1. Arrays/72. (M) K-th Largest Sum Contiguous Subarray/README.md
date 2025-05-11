To solve the **K-th Largest Sum Contiguous Subarray** problem, we need to compute the sum of all contiguous subarrays, sort them in descending order, and return the K-th largest sum.

---

### ✅ Problem Breakdown

Given an array `arr[]` and integer `k`, we want the K-th largest sum from **all possible contiguous subarrays**.

#### Naive Strategy:

1. Generate **all subarray sums** (O(n²) total).
2. Sort and pick the K-th largest (O(n² log n)).

But since **K can be much smaller than total subarrays**, we **optimize with a Min-Heap**:

* Maintain a min-heap of size `k`.
* Traverse all subarrays and push their sums:

  * If the heap has less than `k` elements, push.
  * If more, only push if the new sum is larger than the smallest in heap.

---

### 🔍 Dry Run Example

**Input:**

```
arr = [3, 2, 1], k = 2
All contiguous subarrays: [3], [3,2], [3,2,1], [2], [2,1], [1]
Subarray sums: 3, 5, 6, 2, 3, 1
Sorted descending: 6, 5, 3, 3, 2, 1
→ 2nd largest = 5 ✅
```

---

## ✅ Python Implementation

```python
import heapq

class Solution:
    def kthLargest(self, arr, k) -> int:
        minHeap = []

        n = len(arr)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]

                if len(minHeap) < k:
                    heapq.heappush(minHeap, curr_sum)
                else:
                    if curr_sum > minHeap[0]:
                        heapq.heappushpop(minHeap, curr_sum)

        return minHeap[0]
```

---

## ✅ C++ Implementation

```cpp
class Solution {
  public:
    int kthLargest(vector<int> &arr, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        int n = arr.size();

        for (int i = 0; i < n; i++) {
            int currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += arr[j];
                if (minHeap.size() < k) {
                    minHeap.push(currSum);
                } else if (currSum > minHeap.top()) {
                    minHeap.pop();
                    minHeap.push(currSum);
                }
            }
        }

        return minHeap.top();
    }
};
```

---

## ✅ JavaScript Implementation

```javascript
class Solution {
    kthLargest(arr, k) {
        const MinHeap = [];
        const pushHeap = (val) => {
            MinHeap.push(val);
            MinHeap.sort((a, b) => a - b);
            if (MinHeap.length > k) MinHeap.shift();
        };

        const n = arr.length;
        for (let i = 0; i < n; i++) {
            let currSum = 0;
            for (let j = i; j < n; j++) {
                currSum += arr[j];
                pushHeap(currSum);
            }
        }

        return MinHeap[0];
    }
}
```

---

### ⏱️ Time & Space Complexity

* **Time Complexity:** `O(n² log k)` — generating subarrays × heap ops
* **Space Complexity:** `O(k)` — for the heap

