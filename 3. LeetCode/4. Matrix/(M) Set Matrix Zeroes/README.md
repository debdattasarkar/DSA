
---

# 73. Set Matrix Zeroes

**Difficulty:** Medium
**Tags:** Array, Hash Table, Matrix
**Companies:** \[Top Interviewed Companies]

---

## Problem Statement

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You **must do it in place**.

---

## Examples

### Example 1:

```
Input:  matrix = [[1,1,1],
                  [1,0,1],
                  [1,1,1]]
Output:          [[1,0,1],
                  [0,0,0],
                  [1,0,1]]
```

### Example 2:

```
Input:  matrix = [[0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]]
Output:          [[0,0,0,0],
                  [0,4,5,0],
                  [0,3,1,0]]
```

---

## Constraints:

* `m == matrix.length`
* `n == matrix[0].length`
* `1 <= m, n <= 200`
* `-2³¹ <= matrix[i][j] <= 2³¹ - 1`

---

## Follow Up:

* A straightforward solution using `O(mn)` space is probably a bad idea.
* A simple improvement uses `O(m + n)` space, but still not the best solution.
* **Could you devise a constant space solution?**

---

## Hints

💡 **Hint 1**:
If any cell of the matrix has a zero, we can record its row and column number using additional memory. But if you don't want to use extra memory then you can manipulate the array instead. i.e., simulating exactly what the question says.

💡 **Hint 2**:
Setting cell values to zero on the fly while iterating might lead to discrepancies. What if you use some other integer value as your marker? There is still a better approach for this problem with `O(1)` space.

💡 **Hint 3**:
We could have used two sets to keep a record of rows/columns which need to be set to zero. But for an `O(1)` space solution, you can use one of the rows and one of the columns to keep track of this information.

💡 **Hint 4**:
We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

---

Here's the full solution in the required format for **Leetcode 73: Set Matrix Zeroes**, including:

---

## ✅ 1. Text Explanation with Step-by-Step Dry Run

### 🔍 **Problem Summary**

Given an `m x n` matrix, if an element is `0`, you must set its entire row and column to `0`, in-place.

### 🚀 **Goal**

* Modify the matrix **in-place**.
* Do **not** use extra space if possible (follow-up).

---

### 👣 **Step-by-Step Dry Run**

Example:

```
Input:
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

**Step 1:** Detect if first row and first column need to be zeroed.

* Store `first_row_zero = False`, `first_col_zero = False`.

**Step 2:** Use first row and column as markers.

* Traverse the matrix, if `matrix[i][j] == 0`, mark:

  * `matrix[0][j] = 0`  ➝ marks the column
  * `matrix[i][0] = 0`  ➝ marks the row

Result after marking:

```
[[1, 0, 1],
 [0, 0, 1],
 [1, 1, 1]]
```

**Step 3:** Use markers to set zeroes (skip first row & col for now).

* For `i=1 to m-1`, `j=1 to n-1`:

  * If `matrix[i][0] == 0` or `matrix[0][j] == 0`, set `matrix[i][j] = 0`.

Intermediate:

```
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
```

**Step 4:** Zero out first row/column if needed.

* If `first_row_zero`, zero entire first row.
* If `first_col_zero`, zero entire first column.

Final Output:

```
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
```

---

## ✅ 2. Code in 3 Languages

---

### ✅ Python

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set matrix cells to 0 based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row and column to 0 if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

---

### ✅ C++

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool first_row = false, first_col = false;

        // Check if first row or column should be zeroed
        for (int j = 0; j < n; ++j)
            if (matrix[0][j] == 0) first_row = true;
        for (int i = 0; i < m; ++i)
            if (matrix[i][0] == 0) first_col = true;

        // Use matrix as markers
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

        // Set zeroes based on markers
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;

        // Update first row and column
        if (first_row)
            for (int j = 0; j < n; ++j)
                matrix[0][j] = 0;
        if (first_col)
            for (int i = 0; i < m; ++i)
                matrix[i][0] = 0;
    }
};
```

---

### ✅ JavaScript

```javascript
var setZeroes = function(matrix) {
    let m = matrix.length, n = matrix[0].length;
    let firstRowZero = false, firstColZero = false;

    // Check first row and column
    for (let j = 0; j < n; j++)
        if (matrix[0][j] === 0) firstRowZero = true;
    for (let i = 0; i < m; i++)
        if (matrix[i][0] === 0) firstColZero = true;

    // Mark rows and columns
    for (let i = 1; i < m; i++)
        for (let j = 1; j < n; j++)
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }

    // Set cells to 0 based on markers
    for (let i = 1; i < m; i++)
        for (let j = 1; j < n; j++)
            if (matrix[i][0] === 0 || matrix[0][j] === 0)
                matrix[i][j] = 0;

    // Zero out first row and column
    if (firstRowZero)
        for (let j = 0; j < n; j++)
            matrix[0][j] = 0;
    if (firstColZero)
        for (let i = 0; i < m; i++)
            matrix[i][0] = 0;
};
```

---

## ✅ 3. Interview Q\&A

### 🔹Q1: Why do we need to store the first row/column status before using them as markers?

**A:** Because once we overwrite the first row/column with 0s as markers, we lose original information. Hence, we preserve them in two boolean flags.

---

### 🔹Q2: What are the possible approaches for this problem?

* Brute Force with extra space: `O(m*n)` space.
* HashSet to store zero locations: `O(m + n)` space.
* **Optimized** in-place: use first row/col as marker → `O(1)` extra space.

---

### 🔹Q3: What are some common edge cases?

* No 0s in the matrix.
* All elements are 0.
* First row/col contains zero.

---

### 🔹Q4: Is the input matrix square?

**A:** No. The problem works for general `m x n` rectangular matrices.

---
