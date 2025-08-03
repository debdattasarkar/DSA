
---

# 🪙 Gold Mine Problem

**Difficulty**: Medium
**Accuracy**: 29.73%
**Submissions**: 128K+
**Points**: 4

---

## 📘 Problem Statement

Given a gold mine called `mat[][]`. Each field in this mine contains a **positive integer** which is the amount of gold in tons.

Initially, the miner can start from **any row in the first column**. From a given cell, the miner can move:

1. To the cell **diagonally up towards the right**
2. To the cell **to the right**
3. To the cell **diagonally down towards the right**

Find out the **maximum amount of gold** that the miner can collect **until he can no longer move**.

---

## 🧪 Examples

### Example 1:

**Input**:
`mat[][] = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]`
**Output**: `12`
**Explanation**:
The path is `(1, 0) -> (2, 1) -> (2, 2)`.
Total gold collected is `2 + 6 + 4 = 12`.

---

### Example 2:

**Input**:
`mat[][] = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]`
**Output**: `16`
**Explanation**:
The path is `(2, 0) -> (3, 1) -> (2, 2) -> (2, 3)` or `(2, 0) -> (1, 1) -> (1, 2) -> (0, 3)`.
Total gold collected is `5 + 6 + 2 + 3 = 16` or `5 + 2 + 4 + 5 = 16`.

---

### Example 3:

**Input**:
`mat[][] = [[1, 3, 3], [2, 1, 4], [0, 7, 5]]`
**Output**: `14`
**Explanation**:
The path is `(1, 0) -> (2, 1) -> (2, 2)`.
Total gold collected is `2 + 7 + 5 = 14`.

---

## 🔒 Constraints:

* $1 \leq \text{mat.size()}, \text{mat}[0].\text{size()} \leq 500$
* $0 \leq \text{mat}[i][j] \leq 100$

---

## ✅ Expected Time and Space Complexity

* **Time Complexity**: $O(n \times m)$
* **Auxiliary Space**: $O(1)$

---

## 🏢 Company Tags

* `Flipkart`, `Amazon`, `Samsung`

---

## 🏷️ Topic Tags

* `Dynamic Programming`, `Algorithms`

---

## 🧑‍💼 Related Interview Experiences

* Samsung R\&D Bangalore Interview Experience For Internship 2021 On Campus
* Flipkart Interview Experience Set 2 SDE 2

---

## 📚 Related Articles

* [Gold Mine Problem](https://www.geeksforgeeks.org/gold-mine-problem/)

---

---

Let's go step by step for the **Gold Mine Problem**:

---

## ✅ 2. Explanation with Step-by-Step Dry Run

### Problem Summary:

We are given a 2D matrix `mat[][]` where each cell represents gold in tons. A miner can start from any cell in the first column and can move:

* Diagonally **up-right**
* **Right**
* Diagonally **down-right**

We are to **find the maximum amount of gold** the miner can collect.

---

### Dry Run Example:

Input:

```python
mat = [[1, 3, 3],
       [2, 1, 4],
       [0, 6, 4]]
```

### Steps:

We fill a `dp` matrix from right to left:

1. Start from the last column, where `dp[i][j] = mat[i][j]` initially.
2. Then for each cell, look at the 3 possibilities to the right and update with max value.

Final `dp` will look like:

```python
[8, 7, 3]
[12, 10, 4]
[12, 10, 4]
```

Max gold = `12` (from cell `(1, 0)` → `(2, 1)` → `(2, 2)`)

---

## ✅ 3. Optimized Python Code (Expected in Interviews)

### ✅ Brute Force (DFS-style) – Not recommended

### ✅ Dynamic Programming (Right to Left Traversal)

```python
# import time

class Solution:
    def maxGold(self, mat):
        # start_time = time.time()

        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Create a dp table with same dimensions
        dp = [[0]*m for _ in range(n)]  # Time: O(n*m), Space: O(n*m)

        # Step 2: Traverse from rightmost column to left
        for col in range(m-1, -1, -1):  # O(m)
            for row in range(n):        # O(n)
                # Right
                right = dp[row][col+1] if col != m-1 else 0
                # Right-up
                right_up = dp[row-1][col+1] if row > 0 and col != m-1 else 0
                # Right-down
                right_down = dp[row+1][col+1] if row < n-1 and col != m-1 else 0

                # Max of the three directions + current cell's gold
                dp[row][col] = mat[row][col] + max(right, right_up, right_down)

        # Step 3: Answer is max in first column
        result = max(dp[row][0] for row in range(n))  # O(n)

        # print("Input:")
        # for r in mat:
        #     print(r)
        # print("Output:", result)

        # end_time = time.time()
        # print(f"\nTotal Time: {(end_time - start_time) * 1000:.2f} ms")
        return result

# Example run
if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 3, 3],
           [2, 1, 4],
           [0, 6, 4]]
    sol.maxGold(mat)
```

---

### Time & Space Complexity

* **Time**: O(n \* m) — every cell visited once.
* **Space**: O(n \* m) for `dp[][]` (can be optimized to O(n) using rolling arrays).

---

## ✅ 4. Interview Questions and Answers

### Q1: Why can't we use BFS or DFS directly?

**A:** DFS is exponential in worst case. DP memoizes overlapping subproblems, giving optimal substructure and reducing to O(n\*m).

---

### Q2: Can we optimize the space?

**A:** Yes. Since we only need the next column, we can keep two arrays of size `n` and alternate — space reduces to O(n).

---

### Q3: How do you handle boundaries (first row or last row)?

**A:** For top/bottom edges, conditionally skip `right_up` or `right_down` based on row index.

---

### Q4: Can we solve it from left to right?

**A:** It's possible, but harder to maintain valid transitions (especially diagonals). Right-to-left ensures all options are already computed.

---

---

Here is the **space optimized solution** to the **Gold Mine Problem** using dynamic programming with only two 1D arrays.

---

## ✅ Space Optimized Version (O(n) Space)

```python
import time

class Solution:
    def maxGold(self, mat):
        start_time = time.time()

        n = len(mat)        # number of rows
        m = len(mat[0])     # number of columns

        # Initialize current and next column dp values
        next_col = [0] * n  # dp for column j+1
        curr_col = [0] * n  # dp for current column j

        # Traverse from rightmost column to left
        for col in range(m - 1, -1, -1):  # Time: O(m)
            for row in range(n):          # Time: O(n)
                # Right
                right = next_col[row]

                # Right-up
                right_up = next_col[row - 1] if row > 0 else 0

                # Right-down
                right_down = next_col[row + 1] if row < n - 1 else 0

                # Calculate max gold for current cell
                curr_col[row] = mat[row][col] + max(right, right_up, right_down)

            # Prepare for next column iteration
            next_col = curr_col[:]

        # Final result is the max in the first column
        result = max(curr_col)

        print("Input Matrix:")
        for row in mat:
            print(row)
        print("\nMaximum Gold Collected:", result)

        end_time = time.time()
        print(f"Total Time: {(end_time - start_time) * 1000:.2f} ms")
        return result


# Example run
if __name__ == "__main__":
    sol = Solution()

    mat = [[1, 3, 3],
           [2, 1, 4],
           [0, 6, 4]]

    sol.maxGold(mat)
```

---

## ✅ Time & Space Complexity

| Step                       | Complexity   |
| -------------------------- | ------------ |
| Traversing matrix (n × m)  | **O(n × m)** |
| Space (2 arrays of size n) | **O(n)**     |

---

## 📌 Output for Input:

```python
[[1, 3, 3],
 [2, 1, 4],
 [0, 6, 4]]
```

**Explanation**: Best path is `(1,0) -> (2,1) -> (2,2)` → total = `2 + 6 + 4 = 12`

**Output**:

```
Maximum Gold Collected: 12
```
