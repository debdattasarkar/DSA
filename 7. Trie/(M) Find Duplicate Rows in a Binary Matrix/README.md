# Find Duplicate Rows in a Binary Matrix

## 📝 Problem Statement

Given a **boolean matrix** of size `R x C` (each element is either `0` or `1`), your task is to **find the row indices (0-based)** of all **rows which are duplicates** of a previous row.

---

## 📌 Input

* `R`: Number of rows
* `C`: Number of columns
* `matrix[][]`: A 2D list with each cell containing either `0` or `1`.

---

## 🎯 Output

* Return a list of row indices (0-based) which are **duplicates** of a row already seen before.

---

## 📚 Examples

### Example 1:

**Input:**

```
R = 2, C = 2
matrix = [
  [1, 0],
  [1, 0]
]
```

**Output:**

```
[1]
```

**Explanation:**
Row 1 is a duplicate of Row 0.

---

### Example 2:

**Input:**

```
R = 4, C = 3
matrix = [
  [1, 0, 0],
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
```

**Output:**

```
[1, 3]
```

**Explanation:**
Row 1 is a duplicate of Row 0.
Row 3 is a duplicate of Row 2.

---

## ✅ Constraints

* $1 \leq R, C \leq 10^3$
* $0 \leq \text{matrix[i][j]} \leq 1$

---

## 🧠 Approach

1. Iterate over each row in the matrix.
2. Convert the row into a tuple (hashable).
3. Use a `set` to track unique rows.
4. If a row already exists in the set, record its index as a duplicate.

---

## 🧪 Dry Run

**Input:**

```
matrix = [
  [1, 0],
  [1, 0]
]
```

**Steps:**

* Row 0 → (1,0) → Not in set → Add to set
* Row 1 → (1,0) → In set → Add index 1 to result

**Output:**

```
[1]
```

---

## 💻 Time and Space Complexity

* **Time Complexity:** O(R × C)
* **Space Complexity:** O(R × C) (for storing unique rows)

---

## 🧑‍💻 Function Signature

### Python

```python
from typing import List

class Solution:
    def repeatedRows(self, matrix: List[List[int]], R: int, C: int) -> List[int]:
        # Your code here
```

### C++

```cpp
class Solution {
  public:
    vector<int> repeatedRows(vector<vector<int>>& matrix, int R, int C) {
        // Your code here
    }
};
```

### JavaScript

```javascript
class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} R
     * @param {number} C
     * @returns {number[]}
     */
    repeatedRows(matrix, R, C) {
        // Your code here
    }
}
```

---

## 🏷️ Tags

* Matrix
* Trie
* Data Structures
* Advanced Data Structure

---

## 🔗 Related Articles

* [Find Duplicate Rows Binary Matrix](https://www.geeksforgeeks.org/find-duplicate-rows-binary-matrix/)

---

Here's the **text explanation with step-by-step dry run** and **code implementations** in **Python**, **C++**, and **JavaScript** for the problem **"Find Duplicate Rows in a Binary Matrix"** from GeeksforGeeks.

---

## 🔍 Problem Explanation

You're given a binary matrix (containing only `0`s and `1`s). You need to find **indices of rows that are duplicates** of some **previous row**. Return these indices as a list.

---

## 🧠 Approach (Using Hashing)

1. Use a set to track rows you've seen before.
2. Convert each row into a tuple (so it’s hashable).
3. If it exists in the set, add its index to the result.
4. Otherwise, store it in the set.

---

## 🧪 Dry Run

### Input:

```
matrix = [
  [1, 0, 0],
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
```

### Step-by-Step:

* Seen = {}
* i = 0 → row = (1, 0, 0) → not in Seen → add to Seen
* i = 1 → row = (1, 0, 0) → in Seen → add `1` to result
* i = 2 → row = (0, 0, 0) → not in Seen → add to Seen
* i = 3 → row = (0, 0, 0) → in Seen → add `3` to result

### Output:

```
[1, 3]
```

---

## 🧮 Time and Space Complexity

* **Time Complexity:** O(R × C)
* **Auxiliary Space:** O(R × C)

---

## 🐍 Python Code

```python
# User function Template for python3
class Solution:
    def repeatedRows(self, arr, m ,n):
        seen = set()
        result = []
        
        for i in range(m):
            row_tuple = tuple(arr[i])
            if row_tuple in seen:
                result.append(i)
            else:
                seen.add(row_tuple)
        
        return result
```

---

## 💠 C++ Code

```cpp
// User function Template for C++
class Solution {
  public:
    vector<int> repeatedRows(vector<vector<int>> &matrix, int M, int N) {
        set<vector<int>> seen;
        vector<int> result;

        for (int i = 0; i < M; ++i) {
            if (seen.count(matrix[i])) {
                result.push_back(i);
            } else {
                seen.insert(matrix[i]);
            }
        }
        return result;
    }
};
```

---

## 💻 JavaScript Code

```javascript
// User function Template for javascript

/**
 * @param {number[][]} Matrix
 * @param {number} M
 * @param {number} N
 * @return {number[]}
 */

class Solution {
    repeatedRows(Matrix, M, N) {
        const seen = new Set();
        const result = [];

        for (let i = 0; i < M; i++) {
            const rowKey = Matrix[i].join('');
            if (seen.has(rowKey)) {
                result.push(i);
            } else {
                seen.add(rowKey);
            }
        }

        return result;
    }
}
```

---

Let me know if you'd like a version that uses Trie instead of hashing!

