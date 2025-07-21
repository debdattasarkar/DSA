
---

## 🧩 Problem Summary:

**Leetcode 378: Kth Smallest Element in a Sorted Matrix**
🔗 [Leetcode Link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)

### 🧠 Problem Statement:

You are given an `n x n` matrix where:

* Each row is sorted in **ascending order**,
* Each column is also sorted in **ascending order**.

Return the **k-th smallest element** in the matrix.

---

### 📌 Example:

```python
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8  
Output: 13

Explanation:
The sorted elements are [1, 5, 9, 10, 11, 12, 13, 13, 15]
→ 8th smallest is 13
```

---

## 🚀 Strategy: Binary Search on Answer Range

Instead of scanning the matrix directly, we **binary search the value space**, not the indices.

* Min possible value = matrix\[0]\[0]
* Max possible value = matrix\[n-1]\[n-1]

At each step, check:

> “How many elements ≤ `mid` exist in the matrix?”

If count ≥ `k`, we can try a smaller candidate.

---

### ✅ Python Code (Optimized)

```python
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def countLessEqual(mid):
            count = 0
            row, col = n - 1, 0  # start from bottom-left
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1  # all elements in this row up to current
                    col += 1
                else:
                    row -= 1
            return count

        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
```

---

## ⏱️ Time and Space Complexity

| Metric | Value                 |
| ------ | --------------------- |
| Time   | `O(n log(max - min))` |
| Space  | `O(1)`                |

---

## 🔁 Dry Run Example

**Matrix**:

```
1   5   9  
10  11  13  
12  13  15
```

**k = 8**

Try `mid = 10`, count = 5
Try `mid = 13`, count = 8 → just enough ✅
Answer = 13

---

## ✅ Real-World Use Cases

1. **Top-k query in sorted matrix/table**
2. **Live dashboards** for rankings or analytics
3. **Database pagination/streaming with bounds**

---
