
---

# 📘 2D Difference Array

**Difficulty:** Medium
**Accuracy:** 62.66%
**Submissions:** 9K+
**Points:** 4
**Average Time:** 14 minutes

---

## 🧠 Problem Statement

You are given a 2D integer matrix `mat[][]` of size `n x m` and a list of `q` operations `opr[][]`.
Each operation is represented as an array `[v, r1, c1, r2, c2]`, where:

* `v` is the value to be added.
* `(r1, c1)` is the **top-left** cell of a submatrix.
* `(r2, c2)` is the **bottom-right** cell of the submatrix (inclusive).

Your task is to:

🔁 For each of the `q` operations, **add** `v` to every element in the submatrix from `(r1, c1)` to `(r2, c2)`.
📤 Return the **final matrix** after applying all operations.

---

## 🧪 Examples

### Example 1:

**Input:**

```python
mat = [
  [1, 2, 3],
  [1, 1, 0],
  [4, -2, 2]
]
opr = [
  [2, 0, 0, 1, 1],
  [-1, 1, 0, 2, 2]
]
```

**Output:**

```python
[
  [3, 4, 3],
  [2, 2, -1],
  [3, -3, 1]
]
```

**Explanation:**

* **Operation 1:** Add 2 to all cells from (0,0) to (1,1).
* **Operation 2:** Add -1 to all cells from (1,0) to (2,2).

Step-by-step visual (after each operation):

* After Op 1:

  ```
  [3, 4, 3]
  [3, 3, 0]
  [4, -2, 2]
  ```
* After Op 2:

  ```
  [3, 4, 3]
  [2, 2, -1]
  [3, -3, 1]
  ```

---

## 🧮 Constraints

```
1 ≤ n × m, q ≤ 10^5  
0 ≤ r1 ≤ r2 ≤ n-1  
0 ≤ c1 ≤ c2 ≤ m-1  
-10^4 ≤ mat[i][j], v ≤ 10^4
```

---

## ⏱️ Expected Time and Space Complexity

* **Time Complexity:** O(n × m)
* **Auxiliary Space:** O(n × m)

---

## 🏷️ Tags

* prefix-sum
* inclusion-exclusion
* algorithms
* arrays
* data structures

---

## 📚 Related Articles

* [Two Dimensional Difference Array](https://www.geeksforgeeks.org/two-dimensional-difference-array/)

---

---

Absolutely! Let's walk through everything step-by-step based on the **correct solution to the 2D Difference Array problem**:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### **Problem Summary:**

You're given:

* A matrix `mat` of size `n x m`
* A list `opr`, where each operation is of the form `[v, r1, c1, r2, c2]`
  Your task: Efficiently **add `v` to all elements in submatrix from (r1, c1) to (r2, c2)** for all operations, and return the final matrix.

---

### ✅ **Why brute-force is inefficient**

Doing each operation in O(r×c) leads to time complexity **O(q × n × m)** — too slow for constraints (q ≤ 10⁵, n×m ≤ 10⁵)

---

### ✅ **Optimized Approach — Using a 2D Difference Matrix**

1. **Create a difference matrix `diff`** that is 2 rows and columns larger than `mat` (i.e., size `(n+2) x (m+2)`).
2. **Apply each operation with inclusion-exclusion principle:**

   ```python
   diff[r1][c1] += v
   diff[r1][c2 + 1] -= v
   diff[r2 + 1][c1] -= v
   diff[r2 + 1][c2 + 1] += v
   ```
3. **Compute prefix sum row-wise**, then column-wise on `diff`
4. **Apply the cumulative result in `diff` back into the original matrix**

---

### 🔁 Dry Run for Example

Input:

```python
mat = [[1, 2, 3], 
       [1, 1, 0], 
       [4, -2, 2]]

opr = [[2, 0, 0, 1, 1], 
       [-1, 1, 0, 2, 2]]
```

#### ➤ Step 1: Apply Operation 1: `+2` to (0,0)-(1,1)

```
diff[0][0] += 2     -> +2
diff[0][2] -= 2     -> -2
diff[2][0] -= 2     -> -2
diff[2][2] += 2     -> +2
```

#### ➤ Step 2: Apply Operation 2: `-1` to (1,0)-(2,2)

```
diff[1][0] += -1    -> -1
diff[1][3] -= -1    -> +1
diff[3][0] -= -1    -> +1
diff[3][3] += -1    -> -1
```

#### ➤ Step 3: Prefix sums on rows and columns

This builds the actual change at each cell.

#### ➤ Step 4: Add to original matrix

Final matrix after applying all operations:

```python
[[3, 4, 3], 
 [2, 2, -1], 
 [3, -3, 1]]
```

---

## ✅ 3. Optimized Code for Interviews (Expected Format)

```python
class Solution:
    def applyDiff2D(self, mat, opr):
        n, m = len(mat), len(mat[0])

        # Step 1: Initialize diff matrix
        diff = [[0] * (m + 2) for _ in range(n + 2)]

        # Step 2: Apply all operations using difference array technique
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            diff[r1][c2 + 1] -= v
            diff[r2 + 1][c1] -= v
            diff[r2 + 1][c2 + 1] += v

        # Step 3: Row-wise prefix sum
        for i in range(n + 1):
            for j in range(1, m + 1):
                diff[i][j] += diff[i][j - 1]

        # Step 4: Column-wise prefix sum
        for j in range(m + 1):
            for i in range(1, n + 1):
                diff[i][j] += diff[i - 1][j]

        # Step 5: Add the difference values to original matrix
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]

        return mat
```

### ✅ Time and Space Complexity

* **Time Complexity:** O(n \* m + q)

  * q = number of operations
  * n \* m = prefix sums and update
* **Space Complexity:** O(n \* m)

---

## ✅ 4. Interview Q\&A

### 🔸Q1. Why use a difference matrix?

**A:** Applying each update individually would be O(n×m×q). A difference matrix lets us apply all q operations in O(q), then use prefix sums to finalize the result in O(n×m).

---

### 🔸Q2. What’s the size of the diff matrix and why is it (n+2)x(m+2)?

**A:** It’s 2 rows and columns larger to safely handle boundary cases where we apply `+v` and `-v` at `r2+1` or `c2+1` without going out of bounds.

---

### 🔸Q3. What is the intuition behind inclusion-exclusion in 2D?

**A:** We mark:

* `+v` at top-left,
* `-v` at right cell (to stop row contribution),
* `-v` at bottom cell (to stop column contribution),
* `+v` at diagonal bottom-right (to counter over-subtraction)

---

### 🔸Q4. What would you change if the number of operations was very small?

**A:** Use brute-force and directly add to each cell in the affected submatrix. But for large q, brute-force becomes inefficient.

---

### 🔸Q5. Can this approach be extended to 3D?

**A:** Yes. You can use a 3D difference matrix and apply similar inclusion-exclusion logic over cuboids. Prefix sum logic becomes more complex but follows same principles.

---

# 🌍 Real-World Use Cases

### 1. **Image Processing / Heatmap Updates**

* **Use Case:** Updating brightness or applying filters to rectangular regions of an image.
* **Why:** A 2D image is a matrix of pixel values. Performing frequent rectangular updates (e.g., increase brightness in a zone) becomes efficient using 2D diff array instead of per-pixel looping.
* **Example:** Increase intensity in region (x1, y1) to (x2, y2) of an image.

---

### 2. **Geospatial / Map Range Modifications**

* **Use Case:** Efficiently updating values on a 2D map grid (e.g., terrain, population density).
* **Why:** Operations like "increase population in a square" or "add elevation in a region" can be made O(1) per update using difference arrays.
* **Example:** Simulate flooding or construction over rectangular zones.

---

### 3. **Game Development – Grid Effects**

* **Use Case:** Applying damage, buffs, or environmental effects over rectangular areas in strategy or grid-based games.
* **Why:** Game engines often deal with 2D grids (like chessboards or RTS maps). Updating entire zones quickly is important for real-time performance.
* **Example:** Bomb explosion affecting a square radius or AOE spells.

---

### 4. **Data Visualization – Cumulative Statistics**

* **Use Case:** Precomputing interaction heatmaps or user-click zones.
* **Why:** UI tracking systems record actions in zones, and efficient 2D range additions allow fast analysis (e.g., for A/B testing dashboards).
* **Example:** Count interactions in a UI grid across multiple user sessions.

---

### 5. **Spreadsheet Range Editing (e.g., Excel Backend)**

* **Use Case:** Applying formulas or increment operations to a rectangular range of cells.
* **Why:** Spreadsheet backends can use this to propagate bulk updates efficiently without touching every cell.
* **Example:** “Increase all sales in region B2\:E5 by 10%” → diff array stores updates, computed later.

---
