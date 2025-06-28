
---

# 📘 Leetcode 48. Rotate Image

**Difficulty:** Medium
**Tags:** Array, Math, Matrix

---

## 📝 Problem Statement

You are given an `n x n` 2D matrix representing an image. Rotate the image by **90 degrees clockwise**.

You **must rotate the image in-place**, meaning you have to modify the input 2D matrix directly.
**DO NOT** allocate another 2D matrix.

---

## 🧪 Examples

### Example 1:

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

Output: [[7,4,1],
         [8,5,2],
         [9,6,3]]
```

### Example 2:

```
Input:  matrix = [[5, 1, 9,11],
                  [2, 4, 8,10],
                  [13,3, 6, 7],
                  [15,14,12,16]]

Output: [[15,13, 2, 5],
         [14, 3, 4, 1],
         [12, 6, 8, 9],
         [16, 7,10,11]]
```

---

## 🔒 Constraints

* `n == matrix.length == matrix[i].length`
* `1 <= n <= 20`
* `-1000 <= matrix[i][j] <= 1000`

---

## ✅ Explanation

### 🔁 Step-by-step Logic:

We rotate a matrix in-place in two steps:

1. **Transpose the Matrix**

   * Swap `matrix[i][j]` with `matrix[j][i]` for all `i < j`
   * Converts rows to columns.

2. **Reverse Each Row**

   * After transposing, reverse each row to achieve 90° clockwise rotation.

---

### 🧠 Dry Run Example:

Original:

```
1 2 3
4 5 6
7 8 9
```

After transpose:

```
1 4 7
2 5 8
3 6 9
```

After reversing rows:

```
7 4 1
8 5 2
9 6 3
```

---

## 🐍 Python Code

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // Step 1: Transpose the matrix
        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j){
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse each row
        for(int i = 0; i < n; ++i){
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

---

## 🌐 JavaScript Code

```javascript
var rotate = function(matrix) {
    let n = matrix.length;

    // Step 1: Transpose
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    // Step 2: Reverse rows
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
};
```

---

## 💬 Interview Q\&A

### Q1: Why do we use transpose + reverse to rotate?

→ This transforms row into column and adjusts the direction without extra space.

### Q2: Can we do it with extra space?

→ Yes, but the problem explicitly restricts it. Extra space solution is easier but violates the constraint.

### Q3: Time Complexity?

→ `O(n^2)` for both transpose and reverse operations.

### Q4: Space Complexity?

→ `O(1)` — All operations are done in-place.

### Q5: Can it be done for non-square matrix?

→ Not using this method. This approach is strictly for `n x n` matrices.

---

Let me know if you'd like a **visual walkthrough or diagram** for this solution!
