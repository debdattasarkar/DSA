# Unique Paths in a Grid

## 📝 Problem Statement

You are given a 2D grid `grid[][]` of size `n x m` consisting of values **0** and **1**:

* A value of **0** means the cell is traversable.
* A value of **1** means the cell is blocked (you cannot enter).

You start at the top-left cell `(1, 1)` and need to reach the bottom-right cell `(n, m)`, moving **only right or down** at each step. Your task is to **calculate the total number of unique ways** to reach the target, considering the obstacles.

> Note: The first and last cell can also contain **1**. The result is guaranteed to fit in a **32-bit integer**.

---

## 📥 Input

* A 2D list `grid[][]` of size `n x m` with values `0` (open) and `1` (blocked).

---

## 📤 Output

* An integer representing the number of unique paths from the top-left to the bottom-right cell.

---

## 💡 Examples

### Example 1

**Input:**

```
n = 3, m = 3
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
```

**Output:** `2`

**Explanation:**

1. Right → Right → Down → Down
2. Down → Down → Right → Right

---

### Example 2

**Input:**

```
n = 1, m = 3
grid = [[1, 0, 1]]
```

**Output:** `0`

**Explanation:** Start is blocked; no path exists.

---

## ✅ Constraints

* `1 ≤ n * m ≤ 10^6`
* Grid cells: `grid[i][j] ∈ {0, 1}`

---

## ⏱ Expected Time & Space Complexity

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## 💼 Company Tags

* Uber

---

## 🧠 Topic Tags

* Dynamic Programming
* Matrix
* Algorithms
* Data Structures

---

## 🔗 Related Links

* [Unique Paths in a Grid with Obstacles – GeeksforGeeks](https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/)

---
Here’s a full explanation with a **step-by-step dry run**, followed by implementations in **Python**, **C++**, and **JavaScript** with **inline comments**.

---

## 📘 Problem Recap: Unique Paths in a Grid with Obstacles

You are given an `n x m` grid. Each cell contains either `0` (open) or `1` (obstacle). Starting from the top-left cell `(0, 0)`, you must find how many **unique ways** you can reach the bottom-right cell `(n-1, m-1)`, moving only **right** or **down** at each step.

---

## 🧠 Step-by-Step Explanation

### Approach: Dynamic Programming (Bottom-Up)

1. **Initialize a DP table** `dp[n][m]` where `dp[i][j]` holds the number of ways to reach cell `(i,j)`.
2. **Base Case:**

   * If `grid[0][0] == 1`, return 0 immediately.
   * `dp[0][0] = 1` since it’s the start position.
3. **Fill the First Row & Column:**

   * A cell `(i,0)` or `(0,j)` can be reached only if all previous cells in the row or column are open (`0`).
4. **DP Transition:**

   * If `grid[i][j] == 0`, then:
     `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
   * Else (obstacle), `dp[i][j] = 0`

---

## 🧪 Dry Run

For:

```python
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
```

Step-by-step DP table (`dp`):

| Cell       | Computation           | Value |
| ---------- | --------------------- | ----- |
| dp\[0]\[0] | Start = 1             | 1     |
| dp\[0]\[1] | No obstacle           | 1     |
| dp\[0]\[2] | No obstacle           | 1     |
| dp\[1]\[0] | No obstacle           | 1     |
| dp\[1]\[1] | Obstacle              | 0     |
| dp\[1]\[2] | 0+1 (from top & left) | 1     |
| dp\[2]\[0] | No obstacle           | 1     |
| dp\[2]\[1] | 1+0                   | 1     |
| dp\[2]\[2] | 1+1                   | 2     |

🔚 Final Result = `dp[2][2] = 2`

---

## ✅ Python Code

```python
class Solution:
    def uniquePaths(self, grid):
        n, m = len(grid), len(grid[0])

        # If the start or end is blocked, return 0
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0  # Obstacle
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[n-1][m-1]
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int uniquePaths(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();

        if (grid[0][0] == 1 || grid[n-1][m-1] == 1) return 0;

        vector<vector<int>> dp(n, vector<int>(m, 0));
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    dp[i][j] = 0;
                } else {
                    if (i > 0) dp[i][j] += dp[i-1][j];
                    if (j > 0) dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[n-1][m-1];
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    uniquePaths(grid) {
        let n = grid.length, m = grid[0].length;

        if (grid[0][0] === 1 || grid[n-1][m-1] === 1) return 0;

        const dp = Array.from({length: n}, () => Array(m).fill(0));
        dp[0][0] = 1;

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (grid[i][j] === 1) {
                    dp[i][j] = 0;
                } else {
                    if (i > 0) dp[i][j] += dp[i - 1][j];
                    if (j > 0) dp[i][j] += dp[i][j - 1];
                }
            }
        }
        return dp[n-1][m-1];
    }
}
```

---

Great! Here's the **space-optimized version** of the `Unique Paths in a Grid with Obstacles` problem. This version uses **O(m)** space instead of **O(n × m)**, which is beneficial for large grids.

---

## ✅ Space-Optimized Dynamic Programming Explanation

### Key Insight:

At any point, we only need the current row and the previous row’s values. So we can maintain just **one row (`dp[]`)** and update it as we go.

---

## 🧠 Optimized Python Code

```python
class Solution:
    def uniquePaths(self, grid):
        n, m = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0

        dp = [0] * m
        dp[0] = 1  # start position

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[j] = 0  # block this cell
                elif j > 0:
                    dp[j] += dp[j - 1]  # accumulate from left cell

        return dp[-1]
```

---

## ✅ Optimized C++ Code

```cpp
class Solution {
  public:
    int uniquePaths(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();

        if (grid[0][0] == 1 || grid[n-1][m-1] == 1) return 0;

        vector<int> dp(m, 0);
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    dp[j] = 0; // block cell
                } else if (j > 0) {
                    dp[j] += dp[j - 1]; // add from left
                }
            }
        }

        return dp[m - 1];
    }
};
```

---

## ✅ Optimized JavaScript Code

```javascript
class Solution {
    uniquePaths(grid) {
        const n = grid.length, m = grid[0].length;
        if (grid[0][0] === 1 || grid[n-1][m-1] === 1) return 0;

        let dp = new Array(m).fill(0);
        dp[0] = 1;

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                if (grid[i][j] === 1) {
                    dp[j] = 0;
                } else if (j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[m - 1];
    }
}
```

---

