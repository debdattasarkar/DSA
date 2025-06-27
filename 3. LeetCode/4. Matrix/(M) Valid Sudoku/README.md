
---

# 36. Valid Sudoku

**Difficulty:** Medium
**Tags:** `Array`, `Hash Table`, `Matrix`
**Companies:** Multiple

---

## 🧩 Problem Statement

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each **row** must contain the digits `1–9` **without repetition**.
2. Each **column** must contain the digits `1–9` **without repetition**.
3. Each of the **nine 3 × 3** sub-boxes of the grid must contain the digits `1–9` **without repetition**.

> **Note:**
>
> * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
> * Only the filled cells need to be validated according to the mentioned rules.

---

## 🔢 Examples

### Example 1:

```
Input:
board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

### Example 2:

```
Input:
board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation:
Same as Example 1, except the `5` in the top left corner is replaced by `8`.
This causes two `8`s in the top-left 3x3 sub-box, which violates the rule.
```

---

## 🧾 Constraints

* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit `1–9` or `'.'`

---

## 🧠 Approach Summary

We check three conditions for each cell:

1. Is the value repeated in the **same row**?
2. Is the value repeated in the **same column**?
3. Is the value repeated in the **same 3x3 sub-grid**?

We can track this using three sets (or hash maps):

* One for rows,
* One for columns,
* One for 3x3 boxes (indexed by `i//3, j//3`).

If any condition fails, the board is **invalid**.

---

### ✅ Problem: 36. Valid Sudoku

You are given a partially filled 9x9 Sudoku board. The task is to **determine if it is valid**, meaning it obeys these rules:

### ✅ Rules:

1. Each row must contain digits **1–9** **without repetition**.
2. Each column must contain digits **1–9** **without repetition**.
3. Each of the 3×3 sub-boxes must also contain digits **1–9** **without repetition**.

> Empty cells are denoted as `"."`.

---

### 🧠 Step-by-Step Explanation & Dry Run:

#### Input:

```python
board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
```

#### Dry Run:

* Loop through each row:

  * Store digits in a set.
  * If a digit appears again → return False.
* Loop through each column:

  * Same as above.
* Loop through each 3x3 box (top-left corners: (0,0), (0,3), (0,6), ..., (6,6)):

  * Check 3x3 window for duplicates.

✅ No duplicates found → return True.

---

## ✅ Optimized Code

### 🔹 Python

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box_idx = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

        return True
```

---

### 🔹 C++

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9), cols(9), boxes(9);

        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j) {
                char num = board[i][j];
                if (num == '.') continue;
                int box_idx = (i / 3) * 3 + j / 3;
                if (rows[i].count(num) || cols[j].count(num) || boxes[box_idx].count(num))
                    return false;
                rows[i].insert(num);
                cols[j].insert(num);
                boxes[box_idx].insert(num);
            }

        return true;
    }
};
```

---

### 🔹 JavaScript

```javascript
var isValidSudoku = function(board) {
    let rows = Array.from({ length: 9 }, () => new Set());
    let cols = Array.from({ length: 9 }, () => new Set());
    let boxes = Array.from({ length: 9 }, () => new Set());

    for (let i = 0; i < 9; i++)
        for (let j = 0; j < 9; j++) {
            let num = board[i][j];
            if (num === '.') continue;
            let boxIdx = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (rows[i].has(num) || cols[j].has(num) || boxes[boxIdx].has(num))
                return false;
            rows[i].add(num);
            cols[j].add(num);
            boxes[boxIdx].add(num);
        }

    return true;
};
```

---

## 💬 Expected Interview Q\&A:

**Q1: What is the time complexity?**

* **O(1)** → Because the grid is fixed size (9x9), even if you check every cell, it's constant time.

**Q2: What data structure is used?**

* Sets for fast duplicate detection.

**Q3: How are the 3x3 boxes indexed?**

* Box index = `(i // 3) * 3 + (j // 3)` to flatten 3x3 grids into index 0–8.

**Q4: What is the space complexity?**

* **O(1)** constant space, since max size is fixed.

**Q5: Why don't we care about empty cells?**

* Because the problem only validates filled cells.

---
