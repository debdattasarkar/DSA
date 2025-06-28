
---

# 289. Game of Life

**Difficulty:** Medium
**Topics:** Array, Matrix, Simulation
**Companies Asked In:** Common in simulations and system modeling interviews

---

According to [Wikipedia’s article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

> The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

---

## Problem Statement

The board is made up of an `m x n` grid of cells, where each cell has an initial state:

* `1` → **Live**
* `0` → **Dead**

Each cell interacts with its **eight neighbors** (horizontal, vertical, diagonal) using the following four rules:

1. Any live cell with fewer than two live neighbors **dies**, as if by under-population.
2. Any live cell with two or three live neighbors **lives** on to the next generation.
3. Any live cell with more than three live neighbors **dies**, as if by over-population.
4. Any dead cell with exactly three live neighbors **becomes a live cell**, as if by reproduction.

> All cells update **simultaneously** using the above rules.

---

### Goal

Given the current state of the `m x n` grid `board`, **update the board in-place** to reflect its **next state**.

📝 *Note:* You do not need to return anything.

---

## Example 1

```
Input:
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

---

## Example 2

```
Input:
board = [
  [1,1],
  [1,0]
]

Output:
[
  [1,1],
  [1,1]
]
```

---

## Constraints

* `m == board.length`
* `n == board[i].length`
* `1 <= m, n <= 25`
* `board[i][j]` is `0` or `1`

---

## Follow-up

* Could you solve it **in-place**?

  > The board needs to be updated simultaneously:
  > You cannot update some cells first and then use their updated values to update other cells.

* How would you model an **infinite board** using a 2D array?

  > The board is theoretically infinite. How would you handle active cells near the borders?

---

## Tags

`Array` `Matrix` `Simulation`

---

Here's a complete breakdown of **Leetcode 289: Game of Life** with:

---

## ✅ 1. Text Explanation + Step-by-Step Dry Run

### **Problem Summary**:

You are given a 2D grid of `0`s (dead) and `1`s (alive). Update the board in-place according to these rules **simultaneously** for each cell:

* **< 2** live neighbors → dies (underpopulation)
* **2 or 3** live neighbors → lives (stable)
* **> 3** live neighbors → dies (overpopulation)
* **== 3** live neighbors → becomes alive (reproduction)

> To do this **in-place**, we use **state encoding** to remember previous values.

---

### **State Encoding Strategy (for O(1) space)**:

We encode transitions:

* `0 → 1`: Dead → Live → **mark as `2`**
* `1 → 0`: Live → Dead → **mark as `-1`**

Then in a **second pass**, we finalize:

* `2` → `1`
* `-1` → `0`

---

### **Step-by-Step Dry Run**

#### Input:

```
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
```

#### Count Neighbors at (1,1):

* Neighbors: (0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)
* Values: 0,1,0,0,1,1,1,1 → **Total = 5**
* Current = 0 → Dead → Not becoming alive → Stay 0

Continue similarly for all cells...

---

## ✅ 2. Code Implementations

---

### 🔹 Python Code

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def count_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),         (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Consider 1 and -1 as live (before update)
                    if abs(board[nr][nc]) == 1:
                        count += 1
            return count

        # First pass: mark changes with temp values
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_neighbors(r, c)

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # 1 -> 0
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2   # 0 -> 1

        # Second pass: finalize
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
```

---

### 🔹 C++ Code

```cpp
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int rows = board.size(), cols = board[0].size();
        vector<int> dirs = {-1, 0, 1};

        auto count_neighbors = [&](int r, int c) {
            int count = 0;
            for (int dr : dirs) {
                for (int dc : dirs) {
                    if (dr == 0 && dc == 0) continue;
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && abs(board[nr][nc]) == 1)
                        count++;
                }
            }
            return count;
        };

        // First pass
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                int live_neighbors = count_neighbors(r, c);
                if (board[r][c] == 1 && (live_neighbors < 2 || live_neighbors > 3))
                    board[r][c] = -1; // live → dead
                else if (board[r][c] == 0 && live_neighbors == 3)
                    board[r][c] = 2;  // dead → live
            }
        }

        // Second pass
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c)
                board[r][c] = board[r][c] > 0 ? 1 : 0;
        }
    }
};
```

---

### 🔹 JavaScript Code

```javascript
var gameOfLife = function(board) {
    const rows = board.length, cols = board[0].length;
    const dirs = [-1, 0, 1];

    function countNeighbors(r, c) {
        let count = 0;
        for (let dr of dirs) {
            for (let dc of dirs) {
                if (dr === 0 && dc === 0) continue;
                let nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    if (Math.abs(board[nr][nc]) === 1) count++;
                }
            }
        }
        return count;
    }

    // First pass
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            let live = countNeighbors(r, c);
            if (board[r][c] === 1 && (live < 2 || live > 3)) {
                board[r][c] = -1;  // 1 → 0
            } else if (board[r][c] === 0 && live === 3) {
                board[r][c] = 2;   // 0 → 1
            }
        }
    }

    // Finalize
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            board[r][c] = board[r][c] > 0 ? 1 : 0;
        }
    }
};
```

---

## ✅ 3. Expected Interview Q\&A

**Q1.** How do you update the board in-place without using extra space?
**A:** Use temporary encodings:

* `1 → 0` becomes `-1`
* `0 → 1` becomes `2`
  And then finalize in a second pass.

---

**Q2.** Why can't we just directly update values?
**A:** Because all updates must happen **simultaneously**. Early updates affect neighbor calculations. Temporary states solve this.

---

**Q3.** What's the space and time complexity?

* **Time:** O(m × n)
* **Space:** O(1) (excluding input), due to in-place updates.

---

**Q4.** How do you handle boundaries in the grid?
**A:** Check bounds while visiting neighbors (`0 <= r < rows`, `0 <= c < cols`).

---

**Q5.** Can this be extended to an infinite board?
**A:** Use a hash set or sparse map for live cells only. Model only live/neighboring cells to avoid full infinite representation.

---
