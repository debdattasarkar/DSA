Here’s the **complete README-style conversion** of your provided image — no parts omitted:

---

# 💰 Number of Paths in a Matrix with K Coins

### Difficulty: Medium

**Accuracy:** 16.96%
**Submissions:** 59K+
**Points:** 4

---

## 🧠 Problem Statement

You are given a matrix **mat[][]** of size **n × m**, where each of its cells contains some coins.
Count the number of ways to collect **exactly k coins** while moving from the **top-left cell** of the matrix to the **bottom-right cell**.

From a cell **(i, j)**, you can only move to cell **(i+1, j)** or **(i, j+1)**.

---

### Note:

It is guaranteed that the answer will not exceed 32-bit integer limits.

---

## 🧩 Examples

### Example 1

**Input:**

```
k = 12  
mat = [[1, 2, 3],
       [4, 6, 5],
       [3, 2, 1]]
```

**Output:**

```
2
```

**Explanation:**
There are **2 possible paths** with exactly **12 coins**:
1️⃣ (1 → 2 → 6 → 2 → 1)
2️⃣ (1 → 2 → 3 → 5 → 1)

---

### Example 2

**Input:**

```
k = 16  
mat = [[1, 2, 3],
       [4, 6, 5],
       [9, 8, 7]]
```

**Output:**

```
0
```

**Explanation:**
There are **no possible paths** that lead to a total sum of **16**.

---

## ⚙️ Constraints

* ( 1 \leq k \leq 100 )
* ( 1 \leq n, m \leq 100 )
* ( 0 \leq mat[i][j] \leq 200 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** ( O(n \times m \times k) )
* **Auxiliary Space:** ( O(n \times m \times k) )

---

## 🏢 Company Tags

* **Amazon**

---

## 🧩 Topic Tags

* Dynamic Programming
* Recursion
* Matrix
* Backtracking
* Data Structures
* Algorithms

---

## 📚 Related Articles

* [**Number of Paths with Exactly K Coins**](https://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/)

---

---

awesome — let’s make **“Number of paths in a matrix with exactly K coins”** interview-ready.

# 2) Explanation + step-by-step dry run

## Problem in one line

Given an `n × m` grid `mat`, each cell has coins. Starting at `(0,0)` you can only move **Right** `(i, j+1)` or **Down** `(i+1, j)`. Count paths that end at `(n-1, m-1)` with **sum of cell values exactly `k`**.

## Recurrence (key idea)

Let `f(i, j, s)` = number of paths from cell `(i, j)` to the bottom-right that collect **exactly `s`** coins **including** `mat[i][j]`.

If `s < mat[i][j]` → 0 ways (can’t reach `s`).

Otherwise:

```
f(i, j, s) = f(i+1, j, s - mat[i][j])   # go Down
           + f(i, j+1, s - mat[i][j])   # go Right
Base:
- If (i, j) == (n-1, m-1): return 1 if mat[i][j] == s else 0
- If i or j is out of bounds: return 0
```

Answer = `f(0, 0, k)`.

## Dry run (Example 1)

```
k = 12
mat = [[1,2,3],
       [4,6,5],
       [3,2,1]]
Two valid paths:

Path A: 1 → 2 → 6 → 2 → 1 = 12
Path B: 1 → 2 → 3 → 5 → 1 = 12
Total = 2
```

If you memoize `f(i,j,s)`, overlapping subproblems (same `(i,j)` and remaining sum) are reused.

---

# 3) Python solutions (brute ➜ memo ➜ bottom-up ➜ space-optimized)

All use the exact signature you asked for:

```python
class Solution:
    def numberOfPath(self, mat, k):
        # code here
```

### A) Brute Force DFS (teaching aid; exponential)

* Explore all paths (at most `C(n+m-2, n-1)`), prune when running sum exceeds `k`.
* Time: exponential in `n+m` (worst case), Space: O(n+m) recursion.

```python
class Solution:
    def numberOfPath(self, mat, k):
        n, m = len(mat), len(mat[0])
        target = k
        ways = 0

        def dfs(i, j, curr_sum):
            nonlocal ways
            if i >= n or j >= m:
                return
            curr_sum += mat[i][j]
            if curr_sum > target:      # prune
                return
            if i == n - 1 and j == m - 1:
                if curr_sum == target:
                    ways += 1
                return
            dfs(i + 1, j, curr_sum)    # Down
            dfs(i, j + 1, curr_sum)    # Right

        dfs(0, 0, 0)
        return ways
```

### B) Top-Down DP (Memoized Recursion) — **O(n·m·k)**

* Memoize on `(i, j, remaining_sum)`.
* Safe for constraints (`n,m ≤ 100`, `k ≤ 100`).

```python
class Solution:
    def numberOfPath(self, mat, k):
        n, m = len(mat), len(mat[0])

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def ways_from(i, j, remain):
            # Out of bounds
            if i >= n or j >= m:
                return 0
            val = mat[i][j]
            if remain < val:
                return 0
            # Destination cell
            if i == n - 1 and j == m - 1:
                return 1 if remain == val else 0

            remain2 = remain - val
            down  = ways_from(i + 1, j, remain2)
            right = ways_from(i, j + 1, remain2)
            return down + right

        return ways_from(0, 0, k)
```

### C) Bottom-Up 3-D DP (tabulation) — **O(n·m·k)** time & space

* `dp[i][j][s]` = number of ways to reach cell `(i,j)` with sum exactly `s`.
* Transition: from **Top** `(i-1,j)` and **Left** `(i,j-1)`.

```python
class Solution:
    def numberOfPath(self, mat, k):
        n, m = len(mat), len(mat[0])
        # dp[i][j][s] — paths to (i,j) with sum s
        dp = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]

        # Initialize start cell
        v0 = mat[0][0]
        if v0 <= k:
            dp[0][0][v0] = 1

        for i in range(n):
            for j in range(m):
                v = mat[i][j]
                # skip start cell already initialized
                if i == 0 and j == 0:
                    continue
                for s in range(v, k+1):
                    from_top  = dp[i-1][j][s - v] if i > 0 else 0
                    from_left = dp[i][j-1][s - v] if j > 0 else 0
                    dp[i][j][s] = from_top + from_left

        return dp[n-1][m-1][k]
```

### D) Bottom-Up with **O(m·k)** space (row-by-row rolling)

* Keep, for each column, a length-`k+1` array of sums for the **previous row**; while scanning left→right you also have the **current row’s left neighbor**.
* Time: `O(n·m·k)`, Space: `O(m·k)`.

```python
class Solution:
    def numberOfPath(self, mat, k):
        n, m = len(mat), len(mat[0])
        # prev_row[j] holds an array counts[s] for cell (i-1, j)
        prev_row = [ [0]*(k+1) for _ in range(m) ]

        for i in range(n):
            curr_row = [ [0]*(k+1) for _ in range(m) ]
            for j in range(m):
                val = mat[i][j]
                if i == 0 and j == 0:
                    if val <= k:
                        curr_row[0][val] = 1
                    continue

                for s in range(val, k+1):
                    from_top  = prev_row[j][s - val] if i > 0 else 0
                    from_left = curr_row[j-1][s - val] if j > 0 else 0
                    curr_row[j][s] = from_top + from_left

            prev_row = curr_row  # slide window to next row

        return prev_row[m-1][k]
```

**Which one to use in interviews?**

* If they want clarity and constraints allow: **Top-Down (B)**.
* If they prefer iterative DP and complexity discussion: **Bottom-Up (C)** or **(D)** with space optimization.

---

# 4) Interview quick-recall + Q&A

## 10-second mnemonic — **“Take cell, Reduce K, Go R/D”**

1. Read cell value `v`.
2. Recurse/DP on **remaining sum** `k - v`.
3. Move **Right** or **Down**.
4. Count ways that hit the target exactly at the end.

## 5-line pseudo (top-down)

```
ways(i,j,rem):
  if out: return 0
  if last: return rem == mat[i][j]
  if rem < mat[i][j]: return 0
  return ways(i+1,j, rem-mat[i][j]) + ways(i,j+1, rem-mat[i][j])
answer = ways(0,0,k)
```

## Likely questions & crisp answers

**Q1. State and transition?**
`f(i,j,s)` = ways from `(i,j)` to end collecting exactly `s`.
`f(i,j,s) = f(i+1,j,s-v) + f(i,j+1,s-v)` with `v = mat[i][j]`.
Base: at destination return `1` if `s == v` else `0`.

**Q2. Complexity?**
With memo/tabulation: **Time `O(n·m·k)`**, **Space `O(n·m·k)`** (or `O(m·k)` with rolling rows).

**Q3. Why subtract current cell from `k`?**
It avoids carrying a partial sum; we test equality **only at the last cell**, making termination and memo keys simple.

**Q4. Can we prune?**
Yes—if `s < v`, return `0` immediately. (Optionally precompute min/max possible sums from `(i,j)` to end to prune more, but not needed here.)

**Q5. What about large values or modulo?**
If output needs modulo (e.g., `1e9+7`), take `%MOD` at every addition. With the given constraints, 32-bit return is guaranteed.

**Q6. How to reconstruct one valid path?**
During DP, if `down > 0` choose down; else if `right > 0` choose right; continue subtracting values accordingly.

You’re set—explain the **remaining-sum DP**, show the short base cases, and code either memoized recursion or the `O(m·k)` rolling DP on the spot.

---

---

awesome — here are the last two pieces you asked for.

# 5) Real-World Use Cases (quick + relatable)

* **Robot path planning with battery budget:** Each cell cost = energy to traverse. Robot can only move right or down and must finish with **exactly** `k` energy used (e.g., battery swap constraints).
* **Warehouse picking with weight limit:** Grid aisles (right/down). Each bin adds weight; picker must reach dispatch point with **exactly** `k` units loaded (truck slot constraint).
* **Game level scoring routes:** Tiles have points; player moves right/down from start to finish and must end with a **target score** `k` for a bonus/star.

All mirror the DP: at each tile, subtract tile value from the **remaining target** and continue right/down.

---

# 6) Full Python Program (timed, with inline complexity notes)

This uses **Top-Down DP with memoization** (clear and optimal for the constraints). I also add a **Bottom-Up (rolling)** version you can switch to by toggling a flag.

```python
"""
Number of paths in a matrix with exactly K coins
------------------------------------------------
We move only Right or Down from (0,0) to (n-1,m-1). Each cell has coins.
Count paths whose collected sum equals K.

Main idea:
f(i,j,remain) = f(i+1,j, remain - mat[i][j]) + f(i,j+1, remain - mat[i][j])
Base: at (n-1,m-1), return 1 if remain == mat[i][j] else 0.

Complexities (Top-Down Memo):
- States: i in [0..n-1], j in [0..m-1], remain in [0..k]  → O(n*m*k)
- Per state work: O(1)
- Time:  O(n*m*k)
- Space: O(n*m*k) for memo + O(n+m) recursion stack

Complexities (Bottom-Up Rolling, optional):
- Time:  O(n*m*k)
- Space: O(m*k)
"""

from functools import lru_cache
import timeit

class Solution:
    # --------- Version A: Top-Down Memoized (default) ----------
    def numberOfPath(self, mat, k):
        """
        Args:
            mat: List[List[int]]  (n x m grid)
            k:   int              target sum
        Returns:
            int: number of right/down paths summing to k
        """
        n, m = len(mat), len(mat[0])

        @lru_cache(maxsize=None)
        def ways(i, j, remain):
            # Out-of-bounds guard: O(1) time
            if i >= n or j >= m:
                return 0

            val = mat[i][j]

            # Early prune: if current cell already exceeds remain, impossible
            if remain < val:
                return 0

            # Destination cell: O(1)
            if i == n - 1 and j == m - 1:
                return 1 if remain == val else 0

            next_rem = remain - val
            # Recurse to Down and Right: each O(1) work besides memo lookup
            return ways(i + 1, j, next_rem) + ways(i, j + 1, next_rem)

        return ways(0, 0, k)

    # --------- Version B: Bottom-Up Rolling (optional) ----------
    def numberOfPath_bottomup(self, mat, k):
        """
        Row-by-row rolling DP.
        dp[j][s] = ways to reach current row's column j with sum s.
        Time:  O(n*m*k)    Space: O(m*k)
        """
        n, m = len(mat), len(mat[0])
        prev_row = [[0] * (k + 1) for _ in range(m)]  # space O(m*k)

        for i in range(n):
            curr_row = [[0] * (k + 1) for _ in range(m)]
            for j in range(m):
                v = mat[i][j]
                if i == 0 and j == 0:
                    if v <= k:
                        curr_row[0][v] = 1  # base seed at start
                    continue

                # For every achievable sum s, accumulate from top/left
                for s in range(v, k + 1):  # O(k)
                    from_top  = prev_row[j][s - v] if i > 0 else 0
                    from_left = curr_row[j - 1][s - v] if j > 0 else 0
                    curr_row[j][s] = from_top + from_left

            prev_row = curr_row  # slide window to next row

        return prev_row[m - 1][k]


# ------------------------------ Demo + Timing ------------------------------
if __name__ == "__main__":
    # Example 1
    k1 = 12
    mat1 = [
        [1, 2, 3],
        [4, 6, 5],
        [3, 2, 1],
    ]

    # Example 2
    k2 = 16
    mat2 = [
        [1, 2, 3],
        [4, 6, 5],
        [9, 8, 7],
    ]

    sol = Solution()

    # ---- Run & time Top-Down Memo version ----
    t1 = timeit.timeit(lambda: sol.numberOfPath(mat1, k1), number=1)
    ans1 = sol.numberOfPath(mat1, k1)

    t2 = timeit.timeit(lambda: sol.numberOfPath(mat2, k2), number=1)
    ans2 = sol.numberOfPath(mat2, k2)

    print("Top-Down Memoized DP")
    print(f"Input 1: k={k1}, mat={mat1}")
    print(f"Output 1: {ans1}")
    print(f"Execution Time 1: {t1:.8f} s\n")

    print(f"Input 2: k={k2}, mat={mat2}")
    print(f"Output 2: {ans2}")
    print(f"Execution Time 2: {t2:.8f} s\n")

    # ---- Optional: also time the Bottom-Up Rolling version ----
    tb1 = timeit.timeit(lambda: sol.numberOfPath_bottomup(mat1, k1), number=1)
    ab1 = sol.numberOfPath_bottomup(mat1, k1)

    tb2 = timeit.timeit(lambda: sol.numberOfPath_bottomup(mat2, k2), number=1)
    ab2 = sol.numberOfPath_bottomup(mat2, k2)

    print("Bottom-Up Rolling DP")
    print(f"Output 1 (BU): {ab1} | Time: {tb1:.8f} s")
    print(f"Output 2 (BU): {ab2} | Time: {tb2:.8f} s")
```

### Sample output

```
Top-Down Memoized DP
Input 1: k=12, mat=[[1, 2, 3], [4, 6, 5], [3, 2, 1]]
Output 1: 2
Execution Time 1: 0.00000xx s

Input 2: k=16, mat=[[1, 2, 3], [4, 6, 5], [9, 8, 7]]
Output 2: 0
Execution Time 2: 0.00000xx s

Bottom-Up Rolling DP
Output 1 (BU): 2 | Time: 0.00000xx s
Output 2 (BU): 0 | Time: 0.00000xx s
```

