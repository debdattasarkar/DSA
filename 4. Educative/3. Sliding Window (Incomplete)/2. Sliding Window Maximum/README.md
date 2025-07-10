
---

## 📊 Problem: Sliding Window Maximum

**Statement**:
Given an array `nums` and an integer `k`, return the maximum value in every contiguous subarray (window) of size `k`.

---

### 🧠 Understand the Problem

* You're asked to move a **fixed-size sliding window** across the array.
* For each window, you must compute the **maximum** element.
* This is a classic **monotonic deque** problem.

---

### 🔍 Constraints

* `1 <= len(nums) <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `1 <= k <= len(nums)`

---

## ✅ Optimal Approach: Monotonic Deque

Use a **deque** to store indices of array elements.
Maintain the deque in such a way that the elements it refers to are in **decreasing order**.

### 🔄 Steps:

1. Iterate over the array using index `i`.
2. For each index `i`:

   * Remove indices from the **back** of the deque if `nums[i]` ≥ `nums[deque[-1]]`.
   * Append index `i` to the **back**.
   * Remove indices from the **front** if they are **outside the window** `(i - k + 1)`.
   * If `i ≥ k - 1`, append `nums[deque[0]]` (the maximum of the window) to the result.

---

### 🧠 Python Code with Comments & Time Measurement

```python
from collections import deque
import time

def find_max_sliding_window(nums, k):
    n = len(nums)
    dq = deque()
    max_windows = []

    for i in range(n):
        # Remove elements out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the end
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Add maximum for this window
        if i >= k - 1:
            max_windows.append(nums[dq[0]])

    return max_windows


# Test runner with timing
def main():
    import timeit

    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1], 1),
        ([9, 11], 2),
        ([4, 5, 4, 4, 4, 6, 7, 20], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    ]

    for i, (nums, k) in enumerate(test_cases, 1):
        print(f"Test case {i}: nums = {nums}, k = {k}")
        start = time.time()
        result = find_max_sliding_window(nums, k)
        end = time.time()
        print(f"Output: {result}")
        print(f"Time taken: {(end - start):.6f} seconds\n{'-'*50}")

if __name__ == "__main__":
    main()
```

---

### ⏱️ Complexity Analysis

| Metric           | Value                                           |
| ---------------- | ----------------------------------------------- |
| Time Complexity  | O(n) — each index is pushed/popped at most once |
| Space Complexity | O(k) for deque + O(n) for result                |

---

### 💡 Interview Tips

* **Deque** is the key structure; **don’t use heaps** — they are O(n log k).
* Be ready to explain:

  * Why the deque stores indices (not values).
  * How the window maintains decreasing order.

---

### 🧪 Sample Dry Run

#### Input:

`nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`

#### Output:

`[3, 3, 5, 5, 6, 7]`

#### Explanation:

| Window     | Max |
| ---------- | --- |
| \[1,3,-1]  | 3   |
| \[3,-1,-3] | 3   |
| \[-1,-3,5] | 5   |
| \[-3,5,3]  | 5   |
| \[5,3,6]   | 6   |
| \[3,6,7]   | 7   |

---

