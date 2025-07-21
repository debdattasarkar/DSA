Let's walk through **Leetcode 74: Search a 2D Matrix**, which is a **binary search** problem disguised inside a matrix!

---

## 🔍 Problem: Leetcode 74 — Search a 2D Matrix

🔗 [View Problem](https://leetcode.com/problems/search-a-2d-matrix/)

### 🧩 Statement:

You are given a `m x n` matrix where:

* Integers in each **row are sorted from left to right**
* The **first integer of each row is greater than the last integer of the previous row**

➡️ Think of this as a **flattened 1D sorted array**.

**Task:** Determine whether a target value exists in the matrix.

---

### 📌 Example:

```python
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  
Output: True
```

```python
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13  
Output: False
```

---

## ✅ Optimized Approach: Binary Search on Flattened Matrix

### 🎯 Idea:

* Matrix is sorted in row-major order ⇒ behaves like a sorted 1D array.
* Perform binary search over range `0` to `m*n - 1`.
* Convert virtual index to 2D index using:

  ```
  row = mid // n
  col = mid % n
  ```

---

### ✅ Python Code

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

---

### ⏱️ Time and Space Complexity

| Metric | Value                                          |
| ------ | ---------------------------------------------- |
| Time   | `O(log(m × n))` — Binary search on full matrix |
| Space  | `O(1)` — Constant                              |

---

## 🔁 Dry Run Example:

### Input:

```python
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
```

* `m = 3`, `n = 4`
* Virtual array: `[1,3,5,7,10,11,16,20,23,30,34,60]`
* Binary search:

  * mid = 5 → 11 → match ✅

---

## 🧠 Real-World Use Cases:

* Searching in time-indexed event tables.
* Efficient memory-mapped DB/table lookup.
* Grid-based simulation search (e.g., game states, geographic tiles).

---

---

Here are the **top interview-style questions and answers** for **Leetcode 74: Search a 2D Matrix**, often asked to assess binary search understanding in multidimensional contexts.

---

## ✅ Leetcode 74 — Interview Q\&A

---

### 🔹1. **Why can this 2D matrix be treated like a 1D sorted array?**

🧠 **Answer:**
Because:

* Each row is sorted left to right, and
* The first element of a row is **greater than** the last element of the previous row.
  These properties ensure that the matrix is **row-major sorted**, which behaves like a **flattened sorted array**.

---

### 🔹2. **How do you convert a 1D index to 2D coordinates?**

🧠 **Answer:**
Let `n` be the number of columns:

* Row: `row = index // n`
* Column: `col = index % n`

This mapping allows binary search over a 2D array using 1D indices.

---

### 🔹3. **What is the time complexity and why?**

🧠 **Answer:**

* Time: `O(log(m × n))` → log of the total number of elements
* Because we apply binary search over a conceptual 1D array of `m*n` elements.

---

### 🔹4. **What would be a brute-force approach, and why is it worse?**

🧠 **Answer:**

* Brute-force: Iterate through all elements → `O(m × n)` time.
* It wastes the sorted property. Binary search exploits sorted structure and is much faster for large matrices.

---

### 🔹5. **What if the matrix is empty or has empty rows?**

🧠 **Answer:**
Check for edge cases:

```python
if not matrix or not matrix[0]:
    return False
```

This avoids `IndexError` on `matrix[0][0]`.

---

### 🔹6. **Can we apply binary search row-by-row instead?**

🧠 **Answer:**
Yes, but it’s less optimal:

* First: Use binary search on rows to find the row that may contain the target.
* Then: Binary search on that row.

This gives:

* Time: `O(log m + log n)`
  → Still logarithmic, but slower than `O(log(m*n))` in practice.

---

### 🔹7. **What if the matrix loses the property that first of a row > last of previous row?**

🧠 **Answer:**
Then **Leetcode 240** applies — the matrix is only **row-wise and column-wise sorted**, not globally.
➡️ Use a search from top-right or bottom-left, reducing one dimension per step.

---

### 🔹8. **Is this binary search approach cache-friendly or memory-efficient?**

🧠 **Answer:**
Yes — it avoids allocating any extra arrays.
It also only accesses a **small number of matrix cells**, so it can be **cache-efficient** for large datasets.

---

## ✅ Summary of Good Answers in Interviews:

| Interviewer Question      | What You Should Emphasize                       |
| ------------------------- | ----------------------------------------------- |
| Why binary search works   | Matrix is globally sorted (row-major)           |
| 1D index to 2D conversion | `row = idx // n`, `col = idx % n`               |
| Time complexity           | `O(log(m × n))`                                 |
| Alternate method          | 2-step binary search on rows then row elements  |
| Matrix variant handling   | Different logic for Leetcode 240 style matrices |

---
