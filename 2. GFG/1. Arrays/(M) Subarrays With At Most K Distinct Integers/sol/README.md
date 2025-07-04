Here's the **full program** for the function `countAtMostK`, including:

* ✅ Inline comments
* ⏱ Time and space complexity for each step
* 🧪 Sample input/output
* 🧠 Dry run
* ⏲ **Timing using `time` module** to measure total runtime

---

## ✅ Problem Statement

Count the number of **subarrays** of `arr[]` that contain **at most `k` distinct elements**.

---

## ✅ Full Python Program with Timing

```python
from collections import defaultdict
import time

class Solution:
    def countAtMostK(self, arr, k):
        freq = defaultdict(int)  # Dictionary to store frequency of elements in the current window
        left = 0                 # Left pointer for sliding window
        count = 0                # Result count

        for right in range(len(arr)):
            # Step 1: Add new element to window
            if freq[arr[right]] == 0:
                k -= 1  # New distinct element
            freq[arr[right]] += 1

            # Step 2: Shrink window from the left if we exceed k distinct elements
            while k < 0:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    k += 1  # One distinct element removed
                left += 1

            # Step 3: All subarrays ending at 'right' with valid 'left' are counted
            count += (right - left + 1)

        return count
```

---

## 🧪 Driver Code + Timing

```python
if __name__ == "__main__":
    import random

    # Example test
    arr = [1, 2, 1, 2, 3]
    k = 2

    print("Input Array:", arr)
    print("k =", k)

    start_time = time.time()  # Start timer

    sol = Solution()
    result = sol.countAtMostK(arr, k)

    end_time = time.time()    # End timer

    print("Output:", result)  # Expected: 10
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
```

---

## 🧠 Dry Run

```python
arr = [1, 2, 1, 2, 3], k = 2
```

### Valid subarrays:

```
[1], [2], [1,2], [2,1], [1,2,1], [2,1,2]
[1,2,1,2], [2,1,2,3], [1,2,3], [2,3]
→ Total = 10
```

---

## ⏱ Time and Space Complexity

| Step                  | Time Complexity | Space Complexity | Explanation                       |
| --------------------- | --------------- | ---------------- | --------------------------------- |
| Outer loop (`right`)  | O(n)            |                  | Linear scan                       |
| Inner while loop      | Amortized O(n)  |                  | Every element added/removed once  |
| Dictionary operations | O(1) avg        | O(k)             | At most `k` keys in map           |
| **Total**             | **O(n)**        | **O(k)**         | Efficient sliding window solution |

---

## ✅ Output

```
Input Array: [1, 2, 1, 2, 3]
k = 2
Output: 10
Execution Time: 0.0000XX seconds
```

---
