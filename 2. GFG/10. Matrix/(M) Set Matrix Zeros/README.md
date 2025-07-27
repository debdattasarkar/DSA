
---

# 🧮 Set Matrix Zeros

**Difficulty**: Medium
**Accuracy**: 52.54%
**Submissions**: 48K+
**Points**: 4

---

## 📝 Problem Statement

You are given a 2D matrix `mat[][]` of size `n x m`.
The task is to modify the matrix such that if `mat[i][j]` is 0, **all the elements in the `i`-th row and `j`-th column are set to 0**.

---

## 🔍 Examples

### Example 1

```
Input:
mat[][] = 
[
 [  1, -1,  1],
 [ -1,  0,  1],
 [  1, -1,  1]
]

Output:
[
 [ 1,  0, 1],
 [ 0,  0, 0],
 [ 1,  0, 1]
]

Explanation:
mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.
```

---

### Example 2

```
Input:
mat[][] =
[
 [ 0, 1, 2, 0],
 [ 1, 2, 6, 2],
 [ 1, 3, 1, 8]
]

Output:
[
 [ 0, 0, 0, 0],
 [ 0, 2, 6, 0],
 [ 0, 3, 1, 0]
]

Explanation:
mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.
```

---

## 📏 Constraints

* `1 ≤ n, m ≤ 500`
* `-2^31 ≤ mat[i][j] ≤ 2^31 - 1`

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity**: `O(n * m)`
* **Auxiliary Space**: `O(1)` (without using extra matrices for marking)

---

## 🏷 Company Tags

* Expedia
* Amazon
* Yahoo
* TCS
* ServiceNow
* Google
* Oracle

---

## 🧠 Topic Tags

* Greedy
* Matrix

---

## 📚 Related Articles

* [Set Entire Matrix Row And Column As Zeroes](https://www.geeksforgeeks.org/a-space-efficient-solution-to-set-matrix-zeroes-in-place/)

---

---

Here's a complete breakdown for the **"Set Matrix Zeroes"** problem as typically asked in interviews:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### 💡 Problem Summary

> Given an `n x m` matrix, if any element is `0`, then set its entire **row** and **column** to `0`. You must **do it in-place**, with **O(1)** extra space (optimal version).

---

### 🧠 Naive Approach

* Traverse the matrix.
* Store positions of all `0` values.
* In second pass, set full row and column of those positions to `0`.

❌ Extra space: `O(n + m)` or `O(n*m)` for flag matrix.

---

### ✅ Optimal Approach (In-place with O(1) space)

We use the **first row and column as markers**.

### Steps:

1. Create variables:

   * `row0`: track if first row needs to be zeroed.
   * `col0`: track if first column needs to be zeroed.

2. First pass:

   * Iterate the matrix.
   * If `mat[i][j] == 0`, mark:

     * `mat[i][0] = 0`
     * `mat[0][j] = 0`
   * Also update `row0` and `col0` as needed.

3. Second pass (reverse order to avoid overwriting markers too early):

   * From `bottom-right` to `top-left`, set `mat[i][j] = 0` if `mat[i][0] == 0` or `mat[0][j] == 0`.

4. Finally, use `row0` and `col0` to zero out first row/column if needed.

---

### 🧪 Dry Run Example

```
Input:
[ [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1] ]

Step 1: First row & column marker:
→ mat[1][0] = 0, mat[0][1] = 0
→ row0 = False, col0 = False

Matrix after marking:
[ [1, 0, 1],
  [0, 0, 1],
  [1, 1, 1] ]

Step 2: Reverse fill:
→ i=2, j=2 → no change
→ i=2, j=1 → mat[0][1] == 0 ⇒ set to 0
→ ...

Final:
[ [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1] ]
```

---

## ✅ 3. Python Code (Optimal + Brute Expected in Interviews)

### 🔹 Optimal Code – O(n \* m) time, O(1) space

```python
class Solution:
    def setMatrixZeroes(self, mat):
        rows, cols = len(mat), len(mat[0])
        row0 = col0 = False

        # Step 1: Mark rows and columns
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True
                    mat[i][0] = 0
                    mat[0][j] = 0

        # Step 2: Update the matrix using the markers
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Step 3: Handle first row
        if row0:
            for j in range(cols):
                mat[0][j] = 0

        # Step 4: Handle first column
        if col0:
            for i in range(rows):
                mat[i][0] = 0

        return mat
```

---

### 🔹 Brute Force Code – O(n*m*(n+m)) Time, O(1) Space

```python
class Solution:
    def setMatrixZeroes(self, mat):
        rows, cols = len(mat), len(mat[0])

        # Step 1: Traverse and mark -1 for rows and cols to be updated
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    for k in range(rows):
                        if mat[k][j] != 0:
                            mat[k][j] = -1
                    for k in range(cols):
                        if mat[i][k] != 0:
                            mat[i][k] = -1

        # Step 2: Replace -1 with 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == -1:
                    mat[i][j] = 0

        return mat
```

---

### 🧪 Sample Input/Output

```python
mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setMatrixZeroes(mat)
# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]
```

---

## 💬 4. Expected Interview Questions & Answers

### 🔹 Q1: What is the brute force time complexity?

**A:** `O(n * m * (n + m))` due to row+column update for every zero.

---

### 🔹 Q2: Can you solve this in O(1) extra space?

**A:** Yes. Use the first row and column of the matrix to mark which rows/cols should be zeroed.

---

### 🔹 Q3: What if you use a separate matrix to mark? Will it still be in-place?

**A:** No. That would require O(n\*m) space, violating the in-place requirement.

---

### 🔹 Q4: How do you handle conflict in using the first row and column as markers?

**A:** Use two separate booleans: `row0` and `col0` to track if first row or column needs to be zeroed.

---

### 🔹 Q5: Why process from bottom-right in the second pass?

**A:** To avoid overwriting the first row/column markers before using them.

---
