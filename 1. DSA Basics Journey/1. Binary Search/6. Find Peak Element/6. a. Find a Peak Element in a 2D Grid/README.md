Awesome — let’s tackle **Leetcode 1901: Find a Peak Element in a 2D Grid**, the **2D extension** of the 1D peak-finding problem!

---

## 🧩 Leetcode 1901: Find a Peak Element in a 2D Grid

🔗 [Leetcode 1901](https://leetcode.com/problems/find-a-peak-element-ii)

> You are given a 2D matrix `grid`, and you must find a **peak** element such that:
>
> * `grid[i][j]` is **strictly greater than** its **up/down/left/right neighbors**
> * Return **any one** such position `[i, j]`

### Constraints:

* You may assume `grid[i][j]` is always surrounded by `-∞` beyond boundaries.
* The peak is **guaranteed** to exist.

---

## 🧠 Example

```txt
Input:
grid = [
  [1, 4],
  [3, 2]
]

Output: [0,1]  # Because 4 > 1, 2
```

---

## ✅ Optimal Solution: **Greedy Binary Search on Columns**

### Idea:

* Pick a column `mid`
* Find the **maximum element in that column** → `(row, mid)`
* Check left and right neighbors:

  * If this element is greater than both → 🎯 it’s a peak
  * Else move to the **side with the greater neighbor** (like slope in 1D)

---

### ✅ Time Complexity

* **O(m × log n)** → where `m` = rows, `n` = columns
* Why? Logarithmic columns + linear row scan for max

---

## ✅ Python Code

```python
from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        left, right = 0, cols - 1

        while left <= right:
            mid_col = (left + right) // 2
            max_row = 0
            # Find the row with the max element in mid_col
            for row in range(rows):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row

            mid_val = mat[max_row][mid_col]
            left_val = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else float('-inf')
            right_val = mat[max_row][mid_col + 1] if mid_col + 1 < cols else float('-inf')

            if mid_val > left_val and mid_val > right_val:
                return [max_row, mid_col]
            elif right_val > mid_val:
                left = mid_col + 1  # Move right
            else:
                right = mid_col - 1  # Move left

        return [-1, -1]  # Should never happen
```

---

## 🔁 Dry Run

For:

```python
grid = [
  [10, 8, 10],
  [14, 13, 12],
  [15, 9, 11]
]
```

* First mid\_col = 1
* max in col 1 is at row 1: value = 13
* Compare 13 with left = 14, right = 12
* 14 > 13 → move left

Next mid\_col = 0 → max = 15 → no larger neighbor → 🎯 return \[2, 0]

---

## ✅ Interview Follow-ups

| Question                           | Insight                                             |
| ---------------------------------- | --------------------------------------------------- |
| Can there be multiple 2D peaks?    | Yes, return any                                     |
| Can you do better than O(m log n)? | Only with extra constraints (e.g., unimodal rows)   |
| Can you adapt this to 3D grids?    | Yes, by applying similar greedy selection on slices |

---

---

Absolutely! Let's do a **step-by-step dry run** for the input:

---

### 🧪 Input:

```python
mat = [
  [10, 20, 15],
  [21, 30, 14],
  [ 7, 16, 32]
]
```

---

### 🎯 Goal:

Find **any peak** such that `mat[i][j] > up, down, left, right`.

Peaks here:

* `mat[1][1] = 30` (since 30 > 20, 21, 14, 16)
* `mat[2][2] = 32` (since 32 > 14 and 16)

Expected output: either `[1, 1]` or `[2, 2]`

---

## 🔍 Dry Run Using Column-wise Binary Search

We start with:

```python
left = 0
right = 2  # column count - 1
```

---

### 🌀 Step 1: mid\_col = (0 + 2) // 2 = **1**

We search for the max in column 1:

```python
col[1] = [20, 30, 16] → max is 30 at row 1
```

**Neighbors of mat\[1]\[1] = 30**

* Left: mat\[1]\[0] = 21
* Right: mat\[1]\[2] = 14

✅ 30 > 21 and 30 > 14 → **it's a peak!**

---

### ✅ Output:

```python
[1, 1]
```

---

## 🧠 Why this is correct?

The algorithm always selects the column's max and moves in the direction of higher adjacent values. If both neighbors are smaller, it guarantees a peak.

So in this case:

* First column chosen: **1**
* Max in col 1: **30**
* Neighbors smaller → ✅ return immediately

---

---

Yes ✅ — the method used for Leetcode 1901 (binary search on columns with max-row selection) is the **optimized and expected approach**.

---

## ✅ Why Is It Optimized?

### 🎯 **Goal**: Find any peak in a 2D grid

A brute-force method scans all cells → **O(m × n)**
But we can do better by **binary searching on columns**:

---

## 🚀 Optimized Algorithm

### Steps:

1. Binary search on column index:

   * `mid_col = (left + right) // 2`
2. Find the **maximum element** in `mid_col` → row `max_row`
3. Check its **left and right neighbors**

   * If `mat[max_row][mid_col] > both neighbors` → 🎯 peak found
   * Else move search to **larger neighbor side**

---

## 🧮 Time Complexity

| Step                      | Cost             |
| ------------------------- | ---------------- |
| Finding max in a column   | O(m)             |
| Binary search across cols | O(log n)         |
| **Total Time**            | **O(m × log n)** |

Where:

* `m` = number of rows
* `n` = number of columns

---

## 🆚 Compared to Other Approaches

| Approach                   | Time Complexity | Notes                       |
| -------------------------- | --------------- | --------------------------- |
| Brute force (check all)    | O(m × n)        | Too slow for large grids    |
| Optimized (binary on cols) | O(m × log n)    | Best general solution       |
| Optimized (binary on rows) | O(n × log m)    | Also valid, but less common |
| Divide-and-conquer (rec.)  | O(m + n) worst  | Hard to implement cleanly   |

---

## 🧠 When Is This the Optimal Choice?

* When no assumptions are made on sorted rows/cols
* When grid is large (1000×1000 or more)
* When asked for **any peak**, not the global max

---

### ✅ So yes: **This is the optimal method** Leetcode expects.

Here are the **top interview questions** and follow-ups based on **Leetcode 1901: Find a Peak Element in a 2D Grid** — used to test advanced binary search reasoning in 2D space.

---

## 🔹 Basic Concept

### 1. **What is a peak in a 2D grid?**

A cell `(i, j)` is a **peak** if:

```python
grid[i][j] > grid[i±1][j] and grid[i][j] > grid[i][j±1]
```

Only **up, down, left, right** neighbors matter — **not diagonals**.

---

### 2. **Can there be multiple peaks?**

Yes. There can be **many peaks**. You're only asked to return **any one** of them.

---

### 3. **What’s the brute-force approach?**

Loop through every element, compare neighbors:

* Time: `O(m × n)`
* Not acceptable for large inputs

---

## 🔸 Binary Search Strategy

### 4. **How do you reduce the 2D problem to 1D?**

By performing **binary search on columns** (or rows):

* At each column, find the row with the **maximum value**
* Use neighbors (left/right) to decide which half to move to

---

### 5. **Why is it valid to move toward the larger neighbor?**

Because a **larger neighbor suggests a slope**, and we are guaranteed that **a peak must lie in that direction**.

---

### 6. **What’s the time complexity of your solution?**

* Finding max in a column → O(m)
* Binary search over n columns → O(log n)
* ✅ Total: `O(m × log n)`

---

## 🔺 Edge Cases

### 7. **What if the grid has only one row or column?**

* You can apply regular 1D peak finding
* Binary search becomes trivial

---

### 8. **What if multiple elements have the same max value?**

* Return **any one** — the problem guarantees **at least one valid peak**

---

## 🔁 Follow-Up Questions

### 9. **Can you find all peaks in the grid?**

Yes — brute-force version:

```python
for i in range(m):
    for j in range(n):
        if grid[i][j] > all 4 neighbors:
            peaks.append((i, j))
```

Time: `O(m × n)`

---

### 10. **Can you binary search on rows instead of columns?**

Yes. It will be `O(n × log m)` — valid but less cache-friendly if `m ≫ n`

---

### 11. **What are some real-world applications of this?**

* Image processing (local brightness peaks)
* Terrain elevation maps (local mountains)
* Optimization surface finding

---

## 🧠 Advanced/Discussion Questions

### 12. **How would you handle diagonals as neighbors?**

Now you must check 8 directions instead of 4 → peak detection logic becomes:

```python
grid[i][j] > all 8 neighbors
```

Brute-force becomes necessary (unless grid has helpful structure)

---

### 13. **How would you solve this in 3D (cube)?**

* Similar strategy: Binary search one dimension (e.g., z-axis)
* At each slice, find max element and move in the increasing direction
* Time: `O(n² × log d)` where d is depth

---
