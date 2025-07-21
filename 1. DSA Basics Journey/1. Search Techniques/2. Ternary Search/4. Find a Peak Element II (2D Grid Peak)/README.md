
---

## 🔍 Problem Summary

> Given a 2D matrix `mat`, where `mat[i][j] ≠ mat[i±1][j]` and `mat[i][j] ≠ mat[i][j±1]`, find a **peak element** such that it's **strictly greater** than its 4 neighbors (up/down/left/right).
> Return the coordinates `[i, j]` of **any one peak**.

---

## 📌 Constraints

* `mat` is **row-wise and column-wise unsorted**
* No two adjacent elements are equal
* A peak is **guaranteed to exist**

---

## ✅ Why Ternary (or Binary) Search Works in 2D

We can't do a full 2D binary search, but we can:

* **Fix a column `mid`** (binary/ternary-style)
* Find the **maximum in that column** (O(m))
* Compare with left/right neighbors
* Recur in the **better half** of the matrix (left or right)

This gives us **log(n)** steps across columns and **O(m)** time per step ⇒ **O(m log n)**

---

## 🧠 Core Idea (Column-Wise Search)

* Perform search on columns `left → right`
* At each step, pick `mid_col`
* Find `max_row` in `mid_col`
* Compare `mat[max_row][mid_col]` with neighbors:

  * If it’s greater than both neighbors → peak found
  * Else move in direction of larger neighbor (left or right)

---

## ✅ Python Code (Ternary/Binary Column Search)

```python
def findPeakGrid(mat):
    rows, cols = len(mat), len(mat[0])
    left, right = 0, cols - 1

    while left <= right:
        mid = (left + right) // 2

        # Step 1: Find max element in mid column
        max_row = 0
        for i in range(rows):
            if mat[i][mid] > mat[max_row][mid]:
                max_row = i

        # Step 2: Get left and right neighbors safely
        left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right_val = mat[max_row][mid + 1] if mid + 1 < cols else float('-inf')

        # Step 3: Compare with neighbors
        if mat[max_row][mid] >= left_val and mat[max_row][mid] >= right_val:
            return [max_row, mid]
        elif left_val > mat[max_row][mid]:
            right = mid - 1
        else:
            left = mid + 1

    return [-1, -1]  # guaranteed to exist
```

---

## 🔁 Dry Run

```python
Input: mat = [
    [10, 20, 15],
    [21, 30, 14],
    [7, 16, 32]
]
```

* Columns: `0-2`, mid = 1
* Column 1: max is 30 at row 1
* Left = 21, Right = 14 → 30 is greater → ✅ Return `[1, 1]`

---

## ⏱️ Time & Space Complexity

| Metric | Value         |
| ------ | ------------- |
| Time   | O(m \* log n) |
| Space  | O(1)          |

---

## 🧠 Interview Notes

| Question                                   | Expected Answer                                  |
| ------------------------------------------ | ------------------------------------------------ |
| Why column-based search?                   | Reduces time from O(mn) to O(m log n)            |
| Why compare only left/right (not up/down)? | Because we’re already maximizing within a column |
| Can multiple peaks exist?                  | Yes. Return any.                                 |
| Can this be extended to 3D matrix?         | Conceptually yes, becomes more complex           |

---

---

Let's walk through **Leetcode 1901: Find a Peak Element II** in detail.

---

## 🔍 Problem: [Leetcode 1901 - Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/)

> You are given an `m x n` 2D matrix `mat` where **no two adjacent elements are equal**.
> A **peak** is an element that is **strictly greater** than its 4 neighbors (top, bottom, left, right).
> Your task is to return the coordinates `[row, col]` of **any one peak**.

---

## ✅ Constraints

* `1 ≤ m, n ≤ 500`
* Time limit suggests **sublinear search**, not brute-force.

---

## ✅ Optimal Approach: Column-wise Binary Search (or Ternary Style)

We treat the matrix as a **set of vertical slices (columns)**.
Then use **binary or ternary-style search** on columns:

### Idea:

* At each step:

  1. Choose the middle column
  2. Find the max element in that column
  3. Compare it with neighbors (left/right)
  4. Move search window to side with greater neighbor

✅ This reduces the search to `O(m log n)`
Why? Because:

* Each column scan: O(m)
* Search log n columns

---

## 🧑‍💻 Python Code (Binary Search Version)

```python
def findPeakGrid(mat):
    rows, cols = len(mat), len(mat[0])
    left, right = 0, cols - 1

    while left <= right:
        mid_col = (left + right) // 2

        # Find row of max in mid_col
        max_row = 0
        for i in range(rows):
            if mat[i][mid_col] > mat[max_row][mid_col]:
                max_row = i

        # Get neighbors safely
        left_val = mat[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
        right_val = mat[max_row][mid_col + 1] if mid_col < cols - 1 else float('-inf')

        # Check peak
        if mat[max_row][mid_col] >= left_val and mat[max_row][mid_col] >= right_val:
            return [max_row, mid_col]
        elif right_val > mat[max_row][mid_col]:
            left = mid_col + 1
        else:
            right = mid_col - 1

    return [-1, -1]
```

---

## 🧪 Dry Run Example

**Input:**

```python
mat = [
  [10, 20, 15],
  [21, 30, 14],
  [7, 16, 32]
]
```

* Start: `left = 0`, `right = 2`
* `mid_col = 1`, max in col 1 is `30` at row 1
* Left = 21, Right = 14
* 30 > both → return `[1, 1]`

✅ Output: `[1, 1]` or `[2, 2]` (both are valid)

---

## 🧠 Time & Space Complexity

| Metric | Value        |
| ------ | ------------ |
| Time   | O(m × log n) |
| Space  | O(1)         |

---

## 🧠 Interview Q\&A

| Question                     | Answer                                                               |
| ---------------------------- | -------------------------------------------------------------------- |
| Why not brute-force?         | O(m×n) is too slow for m,n ≤ 500                                     |
| Why search columns not rows? | Works symmetrically, but columns are preferred in LC problem         |
| Can there be multiple peaks? | Yes, return any                                                      |
| Why compare only left/right? | We already select max in column, so only horizontal neighbors matter |
| Is this greedy?              | No, it's a binary/ternary search on structure                        |

---
