
---

# 🧮 Make Matrix Beautiful

**Difficulty:** Medium
**Accuracy:** 64.75%
**Submissions:** 57K+
**Points:** 4
**Average Time:** 20 min

---

## 📝 Problem Statement

A **beautiful matrix** is defined as a square matrix in which the **sum of elements in every row and every column is equal**.

You are given a **square matrix `mat[][]`**. Your task is to determine the **minimum number of operations** required to make the matrix beautiful.

In **one operation**, you are allowed to **increment the value of any single cell by 1**.

---

## 🔍 Examples

### Example 1:

**Input:**

```
mat[][] = [[1, 2],
           [3, 4]]
```

**Output:** `4`

**Explanation:**

* Increment value of `mat[0][0]` by 3
* Increment value of `mat[0][1]` by 1
* Final matrix:

  ```
  [[4, 3],
   [3, 4]]
  ```
* Sum of each row and column = 7
* Hence, **total 4 operations** are required.

---

### Example 2:

**Input:**

```
mat[][] = [[1, 2, 3],
           [4, 2, 3],
           [3, 2, 1]]
```

**Output:** `6`

**Explanation:**

* Increment `mat[0][0]` by 1
* Increment `mat[0][1]` by 2
* Increment `mat[2][1]` by 1
* Increment `mat[2][2]` by 2
* Final matrix:

  ```
  [[2, 4, 3],
   [4, 2, 3],
   [3, 3, 3]]
  ```
* Sum of each row and column = 9
* Hence, **6 operations** are required.

---

## 📋 Constraints

* `1 ≤ mat.size() ≤ 900`
* `0 ≤ mat[i][j] ≤ 10⁶`

---

## ⏱️ Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(1)`

---

## 🏷️ Tags

* `Matrix`
* `Data Structures`

---

## 📚 Related Articles

* [Minimum Operations Required to Make Row and Column Matrix Equals](https://www.geeksforgeeks.org/minimum-operations-required-make-row-column-matrix-equals/)

---

---

Sure! Here's the full detailed explanation and implementation for the **“Make Matrix Beautiful”** problem:

---

## ✅ 2. Text Explanation with Step-by-Step Dry Run

### **Problem Summary**

You're given an **n x n square matrix**. A matrix is *beautiful* if all **row sums** and **column sums** are **equal**. In **one operation**, you can increment **any cell by 1**. Your task is to **find the minimum number of operations** to make the matrix beautiful.

---

### 🔁 **Approach Summary**

1. Calculate the **sum of each row and column**.
2. The **target sum** for all rows and columns should be the **maximum sum among all rows and columns**.
3. For each cell, add values so that each row and column match the target.
4. **Only row-wise correction is enough** — updating any cell affects both a row and a column. So we focus on adjusting rows to the target.

---

### 🧮 Dry Run

For input:

```
mat = [
  [1, 2],
  [3, 4]
]
```

Step-by-step:

* Row sums = \[3, 7]
* Col sums = \[4, 6]
* Maximum sum = **7**

We need all rows/cols to sum to **7**.

Operations:

* Row 0 sum = 3 → needs **4 more**
* Update: `mat[0][0] += 3`, `mat[0][1] += 1`
  Final matrix:

  ```
  [4, 3]
  [3, 4]
  ```

All row and column sums are 7.
✅ **Answer = 4 operations**

---

## 🐍 3. Optimized Python Code with Comments (Interview-Ready)

### ✅ Efficient Implementation – Time: O(n²), Space: O(1)

```python
class Solution:
    def balanceSums(self, mat):
        n = len(mat)  # since it's a square matrix

        # Step 1: Compute row and column sums
        rowSum = [0] * n
        colSum = [0] * n

        for i in range(n):
            for j in range(n):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]

        # Step 2: Determine the maximum row/column sum (target sum)
        maxSum = max(max(rowSum), max(colSum))

        # Step 3: Traverse each cell and adjust towards maxSum
        i = j = 0
        ops = 0

        while i < n and j < n:
            # Determine minimum increment we can apply at (i, j)
            diff = min(maxSum - rowSum[i], maxSum - colSum[j])
            mat[i][j] += diff
            rowSum[i] += diff
            colSum[j] += diff
            ops += diff  # count operations

            # Move to next row/col that needs work
            if rowSum[i] == maxSum:
                i += 1
            if colSum[j] == maxSum:
                j += 1

        return ops
```

---

### 🧪 Sample Input/Output

```python
mat = [
    [1, 2],
    [3, 4]
]
sol = Solution()
print(sol.balanceSums(mat))  # Output: 4
```

---

## ❓ 4. Interview Questions & Answers

### 🔹 Q1. Why do we choose max of row and column sums as the target?

**A:** To minimize the number of increments. Every row and column must be raised to the *same level*, and the highest current sum is the minimum feasible target.

---

### 🔹 Q2. Why can we just update rows instead of columns too?

**A:** Incrementing a single cell contributes to **both** row and column. So by incrementing row-wise strategically, columns get adjusted as well.

---

### 🔹 Q3. What’s the time and space complexity?

* **Time:** O(n²) for traversing the matrix and updating
* **Space:** O(n) for storing row and column sums (can be optimized to O(1))

---

### 🔹 Q4. Can we use brute-force?

**Yes**, but not recommended. Brute-force checks every combination to balance the matrix and is exponential.

---

### 🔹 Q5. Is this related to Greedy?

**Yes.** We greedily match rows/columns with the max sum to minimize operations.

---

## 🌍 Real-World Use Cases

* **Data consistency in distributed grids** (equalizing row/col loads).
* **Balancing resource allocation** in matrix-shaped models (like seating, power grids).
* **Image processing**: Equalizing pixel intensities in rows and columns.
* **Excel Sheet Validation** where rows and columns must sum to same target.

---
