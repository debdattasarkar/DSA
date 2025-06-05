# 🧩 Find Rectangle with Corners as 1

## Problem Statement

Given an `n x m` binary matrix `mat[][]` containing only `0`s and `1`s, determine if there exists a rectangle within the matrix such that all four corners of the rectangle are `1`. If such a rectangle exists, return `true`; otherwise, return `false`.

## 🧠 Example

### Example 1

**Input:**

```text
mat[][] = [
  [1, 0, 0, 1, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [1, 0, 1, 0, 1]
]
```

**Output:** `true`

**Explanation:**
Valid corners exist at indices:

* (1,2), (1,4), (3,2), (3,4)

### Example 2

**Input:**

```text
mat[][] = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
```

**Output:** `false`

**Explanation:**
No four corners in a rectangle are all `1`.

---

## 🔍 Constraints

* `1 <= n, m <= 200`
* `mat[i][j]` is either `0` or `1`

---

## ⏱ Expected Time and Space Complexity

* **Time Complexity:** O(n \* m²)
* **Auxiliary Space:** O(m²)

---

## 🧮 Approach

We want to find four `1`s at the corners of a rectangle. For any two columns `c1` and `c2`, if there exist at least two rows `r1` and `r2` such that:

```text
mat[r1][c1] == 1 and mat[r1][c2] == 1
mat[r2][c1] == 1 and mat[r2][c2] == 1
```

Then, they form the corners of a rectangle.

### ✅ Steps:

1. Iterate over each row.
2. For every pair of columns `(i, j)` in that row:

   * If both columns are `1`, check if this pair was seen in a previous row.
   * If yes, return `true`.
   * If not, store this pair for the current row.
3. If no rectangle is found, return `false`.

---

## 🧪 Dry Run

Using the matrix from Example 1:

* First row: \[1, 0, 0, 1, 0] → store pair (0,3)
* Second row: \[0, 0, 1, 0, 1] → store pair (2,4)
* Third row: \[0, 0, 0, 1, 0] → no 1-pair to store
* Fourth row: \[1, 0, 1, 0, 1] → see pair (2,4) again → rectangle confirmed ✅

---

## 💻 Function Signature

### Python

```python
class Solution:
    def hasRectangle(self, mat: List[List[int]]) -> bool:
        # code here
```

### C++

```cpp
class Solution {
  public:
    bool hasRectangle(vector<vector<int>>& mat) {
        // code here
    }
};
```

### JavaScript

```javascript
class Solution {
    /**
     * @param {number[][]} mat
     * @return {boolean}
     */
    hasRectangle(mat) {
        // code here
    }
}
```

---

## 🏷 Tags

* Matrix
* Data Structures

---

## 🏢 Company Tags

* Flipkart

---

## 📚 Related Articles

* [Find Rectangle Binary Matrix Corners 1](https://www.geeksforgeeks.org/find-rectangle-binary-matrix-corners-1/)

---
Here is a **text explanation with a step-by-step dry run** of the problem “Find rectangle with corners as 1”, followed by **working code implementations** in **Python**, **C++**, and **JavaScript** with inline comments.

---

## 🧠 Problem Summary

We are given a binary matrix. We need to find **any rectangle** whose **four corners are all 1**.

A rectangle is valid if:

* It spans two or more rows.
* It spans two or more columns.
* The values at the four corners (top-left, top-right, bottom-left, bottom-right) are all `1`.

---

## 🔍 Step-by-Step Explanation

### Key Idea:

If for **any two columns**, there are **two or more rows** that have `1`s at those two columns, then a rectangle exists.

### 🔄 Dry Run

Given matrix:

```
mat = [
 [1, 0, 0, 1],
 [0, 0, 1, 0],
 [0, 0, 1, 0],
 [1, 0, 1, 1]
]
```

Go row-by-row and look for **column pairs** with both elements as `1`.

* Row 0: (0,3) → record seen pair (0,3)
* Row 1: no pairs
* Row 2: no new pairs
* Row 3: pairs are (0,2), (0,3), (2,3)

Now we check:

* Row 0 had (0,3)
* Row 3 again has (0,3) ⇒ found a rectangle with corners at those columns ⇒ ✅ return `True`

---

## ✅ Python Code

```python
class Solution:    
    def ValidCorner(self, mat): 
        rows = len(mat)
        cols = len(mat[0]) if rows else 0
        seen = set()

        for r in range(rows):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols):
                    # If current row has 1s in columns c1 and c2
                    if mat[r][c1] == 1 and mat[r][c2] == 1:
                        # Check if this pair has been seen before
                        if (c1, c2) in seen:
                            return True
                        # Mark this pair as seen
                        seen.add((c1, c2))
        return False
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    bool ValidCorner(vector<vector<int>> &mat) {
        int rows = mat.size();
        if (rows == 0) return false;
        int cols = mat[0].size();

        unordered_set<string> seen;

        for (int r = 0; r < rows; ++r) {
            for (int c1 = 0; c1 < cols; ++c1) {
                for (int c2 = c1 + 1; c2 < cols; ++c2) {
                    if (mat[r][c1] == 1 && mat[r][c2] == 1) {
                        string key = to_string(c1) + "," + to_string(c2);
                        if (seen.count(key)) return true;
                        seen.insert(key);
                    }
                }
            }
        }
        return false;
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    /**
     * @param {number[][]} mat
     * @returns {boolean}
     */
    ValidCorner(mat) {
        const rows = mat.length;
        const cols = mat[0].length;
        const seen = new Set();

        for (let r = 0; r < rows; r++) {
            for (let c1 = 0; c1 < cols; c1++) {
                for (let c2 = c1 + 1; c2 < cols; c2++) {
                    if (mat[r][c1] === 1 && mat[r][c2] === 1) {
                        const key = `${c1},${c2}`;
                        if (seen.has(key)) return true;
                        seen.add(key);
                    }
                }
            }
        }
        return false;
    }
}
```

---

Great! Here's a **visualized dry run** of the logic applied to the given **example input**:

---

### 🧪 Input Matrix:

```
mat = [
 [1, 0, 0, 1],
 [0, 0, 1, 0],
 [0, 0, 1, 0],
 [1, 0, 1, 1]
]
```

---

### 🧠 Strategy

We track **column pairs** where two 1s appear on the same row.

---

### 🔍 Step-by-Step Dry Run

#### Row 0: \[1, 0, 0, 1]

* Check all pairs (i, j) where i < j:

  * (0, 1) → 1, 0 → skip
  * (0, 2) → 1, 0 → skip
  * ✅ (0, 3) → 1, 1 → **add to set** → seen = { (0, 3) }
  * (1, 2) → 0, 0 → skip
  * (1, 3) → 0, 1 → skip
  * (2, 3) → 0, 1 → skip

#### Row 1: \[0, 0, 1, 0]

* Valid pairs: none → move on

#### Row 2: \[0, 0, 1, 0]

* Valid pairs: none → move on

#### Row 3: \[1, 0, 1, 1]

* Check all column pairs:

  * ✅ (0, 2) → 1, 1 → add to set
  * ✅ (0, 3) → 1, 1 → already in set! ⇒ ✅ **Rectangle Found**
  * ✅ (2, 3) → 1, 1 → doesn't matter, we've already succeeded

---

### ✅ Output

Since **(0, 3)** is repeated in two rows, it means we have:

```
Row A: [1, -, -, 1]
Row B: [1, -, -, 1]
         ↑       ↑
   Column 0     Column 3
```

This forms a **rectangle with 1s at all four corners**.

---

### 🟩 Final Answer: `true`

---

