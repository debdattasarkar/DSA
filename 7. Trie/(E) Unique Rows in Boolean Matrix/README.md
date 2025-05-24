# Unique Rows in Boolean Matrix

## 🧩 Problem Statement

Given a binary matrix `M[][]`, the task is to find **all unique rows** of the given matrix in the **order of their appearance**.

---

## 🧪 Examples

### Example 1

**Input:**

```
row = 3, col = 4
M[][] = {
  {1, 1, 0, 1},
  {1, 0, 0, 1},
  {1, 1, 0, 1}
}
```

**Output:**

```
$1 1 0 1 $1 0 0 1 $
```

**Explanation:**
Only two unique rows:

* `1 1 0 1` (appears first)
* `1 0 0 1` (appears second)

### Example 2

**Input:**

```
row = 2, col = 4
M[][] = {
  {0, 0, 0, 1},
  {0, 0, 0, 1}
}
```

**Output:**

```
$0 0 0 1 $
```

---

## 🚀 Function Signature

Implement the function:

```python
def uniqueRow(M: List[List[int]], row: int, col: int) -> List[List[int]]:
```

---

## ✅ Constraints

* 1 ≤ row, col ≤ 40
* 0 ≤ M\[i]\[j] ≤ 1

---

## 💡 Expected Time & Space Complexity

* **Time Complexity:** O(row × col)
* **Auxiliary Space:** O(row × col)

---

## 🧠 Approach

* Use a **set** to store already seen rows.
* Iterate through each row:

  * If it is not in the set, add it to the result and mark it as seen.

---

## 🧪 Dry Run

For input:

```plaintext
M = [
  [1, 1, 0, 1],
  [1, 0, 0, 1],
  [1, 1, 0, 1]
]
```

* Start from row 0: `[1, 1, 0, 1]` → unique → add to result
* Row 1: `[1, 0, 0, 1]` → unique → add to result
* Row 2: `[1, 1, 0, 1]` → already seen → skip

**Result:**
`[[1, 1, 0, 1], [1, 0, 0, 1]]`

---

## 🐍 Python Code

```python
class Solution:
    def uniqueRow(self, M, row, col):
        seen = set()
        result = []

        for r in M:
            row_tuple = tuple(r)
            if row_tuple not in seen:
                seen.add(row_tuple)
                result.append(r)
        return result
```

---

## 💻 C++ Code

```cpp
class Solution {
public:
    vector<vector<int>> uniqueRow(vector<vector<int>> &M, int row, int col) {
        set<vector<int>> seen;
        vector<vector<int>> result;

        for (int i = 0; i < row; ++i) {
            if (seen.find(M[i]) == seen.end()) {
                seen.insert(M[i]);
                result.push_back(M[i]);
            }
        }
        return result;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    uniqueRow(M, row, col) {
        const seen = new Set();
        const result = [];

        for (let i = 0; i < row; i++) {
            const key = M[i].join(',');
            if (!seen.has(key)) {
                seen.add(key);
                result.push(M[i]);
            }
        }
        return result;
    }
}
```

---

## 🏷️ Tags

* `Set`
* `Matrix`
* `Trie`
* `Data Structures`
* `Advanced Data Structure`

---

## 🏢 Company Tags

* Zoho
* Amazon

---

## 📚 Related Articles

* [Print Unique Rows](https://www.geeksforgeeks.org/print-unique-rows-binary-matrix/)

---

Here's a **complete text explanation with a step-by-step dry run** for the **"Unique Rows in Boolean Matrix"** problem from GeeksforGeeks, followed by **working code with inline comments** in **Python**, **C++**, and **JavaScript**.

---

## 📘 Problem Summary

Given a binary matrix of dimensions `row × col`, return **all unique rows** in the **order of their appearance**.

---

## 🧠 Approach

1. Traverse each row of the matrix.
2. Convert each row into a tuple (or string for JavaScript).
3. Use a set to track rows already seen.
4. If the row hasn’t been seen before, add it to the result and mark it as seen.

---

## 🧪 Dry Run

**Input:**

```plaintext
M = [
  [1, 1, 0, 1],
  [1, 0, 0, 1],
  [1, 1, 0, 1]
]
```

**Step-by-step:**

* Initialize: `seen = set()`, `result = []`
* Row 0 → (1,1,0,1) → not in seen → add to result, mark seen
  → result = \[\[1,1,0,1]]
* Row 1 → (1,0,0,1) → not in seen → add to result, mark seen
  → result = \[\[1,1,0,1], \[1,0,0,1]]
* Row 2 → (1,1,0,1) → already in seen → skip

**Output:**

```plaintext
[[1, 1, 0, 1], [1, 0, 0, 1]]
```

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def uniqueRow(self, row: int, col: int, M: List[List[int]]) -> List[List[int]]:
        seen = set()
        result = []

        for i in range(row):
            current_row = tuple(M[i])  # Convert list to tuple to make it hashable
            if current_row not in seen:
                seen.add(current_row)
                result.append(M[i])  # Keep as list for output
        return result
```

---

## 💻 C++ Code

```cpp
#define MAX 1000
#include <vector>
#include <set>
using namespace std;

class Solution {
  public:
    vector<vector<int>> uniqueRow(int M[MAX][MAX], int row, int col) {
        set<vector<int>> seen;
        vector<vector<int>> result;

        for (int i = 0; i < row; i++) {
            vector<int> current;
            for (int j = 0; j < col; j++) {
                current.push_back(M[i][j]);
            }

            if (seen.find(current) == seen.end()) {
                seen.insert(current);
                result.push_back(current);
            }
        }

        return result;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
class Solution {
    /**
     * @param {number[][]} arr - Matrix
     * @param {number} n - Number of rows
     * @param {number} m - Number of columns
     * @returns {number[][]}
     */
    uniqueRow(arr, n, m) {
        const seen = new Set();
        const result = [];

        for (let i = 0; i < n; i++) {
            const rowStr = arr[i].join(","); // Convert row to string
            if (!seen.has(rowStr)) {
                seen.add(rowStr);
                result.push(arr[i]);
            }
        }

        return result;
    }
}
```

---
