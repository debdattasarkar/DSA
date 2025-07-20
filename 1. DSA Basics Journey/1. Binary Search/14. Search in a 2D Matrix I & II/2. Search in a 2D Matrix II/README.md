Let’s dive into **Leetcode 240: Search a 2D Matrix II**, a **popular binary search pattern** used in sorted 2D grids.

---

## 🔍 Problem: Leetcode 240 — Search a 2D Matrix II

🔗 [View Problem](https://leetcode.com/problems/search-a-2d-matrix-ii/)

---

### 🧩 Problem Statement

You are given a matrix where:

* Each **row is sorted in ascending order**
* Each **column is also sorted in ascending order**

Determine if a **target** value exists in the matrix.

---

### 📌 Example

```python
Input: matrix = [
  [1,  4,  7, 11, 15],
  [2,  5,  8, 12, 19],
  [3,  6,  9, 16, 22],
  [10,13, 14,17, 24],
  [18,21, 23,26, 30]
], target = 5

Output: True
```

---

## ✅ Optimal Approach: Start from Top-Right or Bottom-Left

### 🎯 Intuition:

At top-right corner:

* If value > target → eliminate that **column**
* If value < target → eliminate that **row**

➡️ Each step **eliminates a row or column**, leading to `O(m + n)` time.

---

### ✅ Python Code

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1  # Start at top-right

        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1

        return False
```

---

## 🔁 Dry Run

### Input:

```python
matrix = [
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
target = 6
```

### Steps:

* Start at (0,2): 7 → 7 > 6 → move left
* (0,1): 4 → 4 < 6 → move down
* (1,1): 5 → 5 < 6 → move down
* (2,1): 6 → ✅ found

---

## ⏱️ Time and Space Complexity

| Metric | Value      |
| ------ | ---------- |
| Time   | `O(m + n)` |
| Space  | `O(1)`     |

Where `m` is rows and `n` is columns.

---

## 🧠 Interview Tip: Why This Works

* The matrix isn’t fully sorted, so a single binary search won’t work.
* But partial sorting lets us **prune search space from one corner**.
* Think of it like searching in a BST — choose direction based on comparison.

---

## ❓ Would Binary Search on Each Row Work?

Yes, but:

* Time = `O(m log n)` — binary search each row
* Less efficient than the top-right search

---

## ✅ Real-World Use Cases

* **Geospatial search** (sorted heatmaps, terrain maps)
* **Market data tables** (sorted by time and price)
* **2D sensor arrays** (each row/column sorted by signal intensity)

---

Would you like:

* Interview-style Q\&A for this problem?
* A variant where you return the coordinates of all matching values?
* An implementation comparison: row-wise binary search vs top-right walk?

---

---

Great question!

### ❓ Is the solution to Leetcode 240 (Search in a 2D Matrix II) a **binary search** approach?

---

### ✅ **Short Answer:**

**No**, the standard optimal solution is **not traditional binary search**, but rather a **greedy elimination strategy** that uses the sorted properties of rows and columns.

---

### 🧠 **Explanation:**

**Binary Search** means:

* Halving the search space each time (like in a sorted array)
* Using midpoints (`mid = (low + high) // 2`)

---

### 🔎 In Leetcode 240, we:

* Start at the **top-right corner** (or bottom-left).
* At each step:

  * If `matrix[row][col] > target`, we **move left** (eliminate column).
  * If `matrix[row][col] < target`, we **move down** (eliminate row).
* This reduces the search space linearly — one row or one column at a time.

➡️ It uses a **greedy + matrix pruning strategy**, **not binary halving**.

---

### ✅ Time Complexity:

* **Top-right approach:** `O(m + n)`
* **Binary search per row:** `O(m × log n)` → still acceptable but slower

---

### ✅ When Binary Search *is* applicable:

In **Leetcode 74**, the matrix is **fully sorted** in row-major order (like a flattened array).
There, binary search over the full `m × n` range **is appropriate and optimal**.

---

### 📌 Summary:

| Problem      | Sorted Matrix Type     | Technique                | Time        |
| ------------ | ---------------------- | ------------------------ | ----------- |
| Leetcode 74  | Fully row-major sorted | Full binary search       | `O(log mn)` |
| Leetcode 240 | Row and column sorted  | Top-right prune (greedy) | `O(m + n)`  |

---

Perfect! Let's now implement **binary search** approaches for **Leetcode 240: Search a 2D Matrix II** and compare them.

---

## ✅ Binary Search Approaches

We'll explore **two versions**:

### 🔹1. Binary Search on Each Row (Straightforward)

### 🔹2. 2D Binary Search (Divide and Conquer)

---

## 🔹1. Row-Wise Binary Search (O(m log n))

This works because each **row is sorted** in ascending order.

### ✅ Python Code

```python
from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        for row in matrix:
            # Binary search in the current row
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
```

### ⏱️ Time Complexity:

* `O(m log n)` → where `m` = number of rows, `n` = columns

---

## 🔹2. Divide and Conquer Binary Search (Advanced 2D Binary Search)

This method works recursively by treating the matrix like a 2D search space.

### ✅ Python Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_rec(row_start, row_end, col_start, col_end) -> bool:
            if row_start > row_end or col_start > col_end:
                return False

            mid_row = (row_start + row_end) // 2
            mid_col = (col_start + col_end) // 2
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            elif mid_val < target:
                return (
                    search_rec(mid_row + 1, row_end, col_start, col_end) or
                    search_rec(row_start, row_end, mid_col + 1, col_end)
                )
            else:
                return (
                    search_rec(row_start, mid_row - 1, col_start, col_end) or
                    search_rec(row_start, row_end, col_start, mid_col - 1)
                )

        if not matrix or not matrix[0]:
            return False

        return search_rec(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
```

### ⏱️ Time Complexity:

* Average: `O(log m * log n)`
* Worst case: `O(m + n)` due to overlapping subproblems

---

## 🔍 Comparison Table

| Method                      | Time                     | Space                      | Notes                                 |
| --------------------------- | ------------------------ | -------------------------- | ------------------------------------- |
| Top-right greedy (standard) | `O(m + n)`               | `O(1)`                     | Most efficient, simplest              |
| Row-wise binary search      | `O(m log n)`             | `O(1)`                     | Works well for wide matrices          |
| 2D divide & conquer         | `O(log m * log n)` (avg) | `O(log m + log n)` (stack) | Elegant but can degrade to `O(m + n)` |

---

