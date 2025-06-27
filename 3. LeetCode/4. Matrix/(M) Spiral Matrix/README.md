Here is the complete README-style conversion of **Leetcode 54: Spiral Matrix**, based on the uploaded image:

---

# Leetcode 54. Spiral Matrix

**Difficulty:** Medium
**Tags:** Array, Matrix, Simulation

---

## 📝 Problem Statement

Given an `m x n` matrix, return **all elements of the matrix in spiral order**.

---

## 🧪 Examples

### Example 1:

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2:

```
Input:  matrix = [[1,  2,  3,  4],
                  [5,  6,  7,  8],
                  [9, 10, 11, 12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## 🔒 Constraints:

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

---

## 💡 Hints

* **Hint 1:** Simulate what the problem is asking for. Think algorithmically in terms of moving directions.
* **Hint 2:** Go layer by layer. Traverse top row → right column → bottom row → left column, then shrink boundaries and repeat.
* **Hint 3:** Switch direction when a boundary is hit. Keep track of how many rows and columns are still unvisited.

---

## ✅ Text Explanation

We need to extract the matrix in spiral order. For this:

* Keep track of four boundaries:

  * `top`, `bottom`, `left`, `right`
* Move in four directions:

  1. Left to right (top row)
  2. Top to bottom (right column)
  3. Right to left (bottom row)
  4. Bottom to top (left column)
* After each traversal, update the corresponding boundary to "shrink" the unvisited part of the matrix.
* Stop when all elements have been visited.

---

## 🔁 Dry Run Example

Given:

```
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

* Initial top=0, bottom=2, left=0, right=2
* Step 1: → 1,2,3 → top++
* Step 2: ↓ 6,9 → right--
* Step 3: ← 8,7 → bottom--
* Step 4: ↑ 4 → left++
* Step 5: → 5 → top++

Result: `[1,2,3,6,9,8,7,4,5]`

---

## 🔧 Python Code

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse downwards
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse from Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse upwards
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
```

---

## 🔧 C++ Code

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int top = 0, bottom = matrix.size() - 1;
        int left = 0, right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            // Left to Right
            for (int i = left; i <= right; ++i)
                result.push_back(matrix[top][i]);
            top++;

            // Top to Bottom
            for (int i = top; i <= bottom; ++i)
                result.push_back(matrix[i][right]);
            right--;

            // Right to Left
            if (top <= bottom) {
                for (int i = right; i >= left; --i)
                    result.push_back(matrix[bottom][i]);
                bottom--;
            }

            // Bottom to Top
            if (left <= right) {
                for (int i = bottom; i >= top; --i)
                    result.push_back(matrix[i][left]);
                left++;
            }
        }

        return result;
    }
};
```

---

## 🔧 JavaScript Code

```javascript
var spiralOrder = function(matrix) {
    let result = [];
    let top = 0, bottom = matrix.length - 1;
    let left = 0, right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        // Left to Right
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top++;

        // Top to Bottom
        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right--;

        // Right to Left
        if (top <= bottom) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }

        // Bottom to Top
        if (left <= right) {
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left++;
        }
    }

    return result;
};
```

---

## 💬 Interview Q\&A

**Q1: Time Complexity?**
→ `O(m * n)` where `m` = rows, `n` = columns (visit every element once)

**Q2: Space Complexity?**
→ `O(1)` extra space (excluding output)

**Q3: What if matrix is empty?**
→ Return `[]` immediately

**Q4: Can you handle single row or single column?**
→ Yes, logic works due to boundary checks

**Q5: How is direction managed?**
→ Via incrementing/decrementing the four boundary variables (`top`, `bottom`, `left`, `right`)

---
