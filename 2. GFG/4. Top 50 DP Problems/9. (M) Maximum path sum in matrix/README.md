# Maximum path sum in matrix

**Difficulty:** Medium
**Accuracy:** 42.59%
**Submissions:** 118K+
**Points:** 4

---

## Problem Statement

You are given a matrix `mat[][]` of size `n x m` where each element is a positive integer. Starting from any cell in the first row, you are allowed to move to the next row, but with specific movement constraints. From any cell `(r, c)` in the current row, you can move to any of the three possible positions:

1. `(r+1, c-1)` — move diagonally to the left.
2. `(r+1, c)` — move directly down.
3. `(r+1, c+1)` — move diagonally to the right.

Find the **maximum sum** of any path starting from **any column in the first row** and ending at **any column in the last row**, following the above movement constraints.

---

## Examples

### Example 1

**Input:** `mat[][] = [[3, 6, 1], [2, 3, 4], [5, 5, 1]]`
**Output:** `15`
**Explanation:** The best path is `(0, 1) -> (1, 2) -> (2, 1)`. It gives the maximum sum as `15`.

---

### Example 2

**Input:** `mat[][] = [[2, 1, 1], [1, 2, 2]]`
**Output:** `4`
**Explanation:** The best path is `(0, 0) -> (1, 1)`. It gives the maximum sum as `4`.

---

### Example 3

**Input:** `mat[][] = [[25]]`
**Output:** `25`
**Explanation:** `(0, 0)` is the only cell in `mat[][]`, so maximum path sum will be `25`.

---

## Constraints

* `1 ≤ mat.size() ≤ 500`
* `1 ≤ mat[i].size() ≤ 500`
* `1 ≤ mat[i][j] ≤ 1000`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## Company Tags

Flipkart, Amazon, Microsoft, OYO Rooms, Samsung, MakeMyTrip

---

## Topic Tags

Dynamic Programming, Matrix, Data Structures, Algorithms

---

## Related Interview Experiences

* Flipkart Interview Set 8 Sde 1

---

## Related Articles

* Find The Longest Path In A Matrix With Given Constraints
* Maximum Path Sum Matrix

---

---

awesome — let’s make **Maximum path sum in matrix** crystal-clear and interview-ready.

---

# 2) Explanation + step-by-step dry run

**You can move** from cell `(r, c)` to one of:
`(r+1, c-1)`, `(r+1, c)`, `(r+1, c+1)` (down-left, down, down-right).
Start anywhere on the **first row**; end anywhere on the **last row**. Maximize the sum along the path.

## DP idea (most expected)

Let

```
dp[r][c] = maximum path sum to reach cell (r,c) from some cell in row 0
```

Then for `r > 0`:

```
dp[r][c] = mat[r][c] + max(
               dp[r-1][c],          # from above
               dp[r-1][c-1] if c>0 else -inf,
               dp[r-1][c+1] if c<m-1 else -inf)
```

Initialize first row: `dp[0][c] = mat[0][c]`.
**Answer**: `max(dp[n-1][0..m-1])`.
This is `O(n*m)` time, `O(n*m)` space; can be reduced to **O(m)** with a rolling row.

You can also define it bottom-up from the bottom row (symmetric).

## Dry run (Example 1)

`mat = [[3, 6, 1], [2, 3, 4], [5, 5, 1]]`

* Row 0 (base): `dp0 = [3, 6, 1]`
* Row 1:

  * `dp[1][0] = 2 + max(3, 6) = 8`
  * `dp[1][1] = 3 + max(3, 6, 1) = 9`
  * `dp[1][2] = 4 + max(6, 1) = 10`
* Row 2:

  * `dp[2][0] = 5 + max(8, 9) = 14`
  * `dp[2][1] = 5 + max(8, 9, 10) = 15`
  * `dp[2][2] = 1 + max(9, 10) = 11`

Answer: `max(14, 15, 11) = 15` ✔

---

# 3) Python solutions (multiple ways, interview-style)

All follow:

```python
#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        # code here
```

## A) Bottom-up with **rolling row** (recommended; O(n*m) time, O(m) space)

```python
#User function Template for python3
class Solution:
    def maximumPath(self, mat):
        """
        DP by rows:
          curr[c] = mat[r][c] + max(prev[c-1], prev[c], prev[c+1])
        Keep only prev row -> O(m) space.

        Time : O(n*m)
        Space: O(m)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        prev = mat[0][:]                      # dp for row 0

        for r in range(1, n):
            curr = [0] * m
            for c in range(m):
                best_above = prev[c]
                if c > 0:
                    best_above = max(best_above, prev[c-1])
                if c+1 < m:
                    best_above = max(best_above, prev[c+1])
                curr[c] = mat[r][c] + best_above
            prev = curr                        # roll
        return max(prev)                       # best in last row
```

---

## B) Bottom-up full table (clear to explain; O(n*m) time & space)

```python
class SolutionFull:
    def maximumPath(self, mat):
        """
        Build the whole dp table for clarity.
        Time : O(n*m)
        Space: O(n*m)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        dp = [[0]*m for _ in range(n)]
        dp[0] = mat[0][:]

        for r in range(1, n):
            for c in range(m):
                best = dp[r-1][c]
                if c > 0:
                    best = max(best, dp[r-1][c-1])
                if c+1 < m:
                    best = max(best, dp[r-1][c+1])
                dp[r][c] = mat[r][c] + best

        return max(dp[-1])
```

---

## C) Top-down recursion with memo (same complexity; good for reasoning)

```python
from functools import lru_cache

class SolutionMemo:
    def maximumPath(self, mat):
        """
        f(r,c) = mat[r][c] + max(f(r+1,c-1), f(r+1,c), f(r+1,c+1))
        Answer = max_c f(0,c)
        Time : O(n*m)
        Space: O(n*m) memo + recursion depth O(n)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        @lru_cache(None)
        def f(r, c):
            if c < 0 or c >= m:
                return float("-inf")      # invalid move
            if r == n-1:
                return mat[r][c]
            return mat[r][c] + max(f(r+1, c-1), f(r+1, c), f(r+1, c+1))

        return max(f(0, c) for c in range(m))
```

---

## D) (For completeness) Naïve recursion without memo (**exponential**)

```python
class SolutionBrute:
    def maximumPath(self, mat):
        """
        Exponential; only for very small matrices.
        """
        n = len(mat)
        m = len(mat[0]) if n else 0

        def f(r, c):
            if c < 0 or c >= m:
                return float("-inf")
            if r == n-1:
                return mat[r][c]
            return mat[r][c] + max(f(r+1, c-1), f(r+1, c), f(r+1, c+1))

        return max(f(0, c) for c in range(m))
```

---

# 4) Interview Q&A (high-yield)

**Q1. State the recurrence.**
`dp[r][c] = mat[r][c] + max(dp[r-1][c], dp[r-1][c-1], dp[r-1][c+1])` (handle boundaries).
Or top-down: `f(r,c) = mat[r][c] + max(f(r+1,c-1), f(r+1,c), f(r+1,c+1))`.

**Q2. Why does DP work here?**
Optimal substructure: the best path to `(r,c)` must come from the best among the three allowed predecessors in row `r-1` (or successors if top-down), and overlapping subproblems across columns/rows.

**Q3. Time/space complexity?**
All DP variants visit each cell O(1) times → **O(n*m)** time.
Space: full table **O(n*m)**; rolling row **O(m)**; memo **O(n*m)**.

**Q4. How do you handle boundaries (`c=0` or `c=m-1`)?**
Ignore invalid predecessors/successors or treat them as `-∞` so they never get chosen.

**Q5. What if numbers are negative?**
Algorithms still work — using `-∞` guards is essential so invalid moves aren’t picked.

**Q6. Can you reconstruct the actual path?**
Yes. Keep a `parent[r][c]` pointer to the predecessor that achieved the max while filling `dp`, then backtrack from the argmax in the last row to the first.

**Q7. Relation to other problems?**
This is a standard “grid DP with constrained moves,” akin to **falling path sum**. The O(m) rolling-row pattern is a frequent interview motif.

---

---

here’s a **ready-to-run program** for **Maximum Path Sum in Matrix** that:

* reads a matrix from stdin (supports either `n m` + rows **or** a bracketed Python-like matrix),
* computes the answer with **three approaches** (rolling-row DP, full-table DP, and memoized recursion),
* prints the answer from each and **times** them with `timeit.timeit(number=1)`.

I’ve put tight **time/space complexity notes** inline.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Maximum Path Sum in Matrix
# Move constraints from (r,c): (r+1,c-1), (r+1,c), (r+1,c+1)
# Start in any column of first row, end anywhere in last row.
#
# Methods:
#   1) Rolling-row DP (recommended)    : O(n*m) time, O(m)   space
#   2) Full-table DP (educational)     : O(n*m) time, O(n*m) space
#   3) Top-down + memo (same bounds)   : O(n*m) time, O(n*m) space (+ recursion)
#
# Input options (stdin):
#   A) First line: "n m"
#      Next n lines: m integers each
#   B) One line: a bracketed matrix like "[[3,6,1],[2,3,4],[5,5,1]]"
#
# Output:
#   - Echo of parsed input
#   - Answers from each method
#   - Per-method timings in ms (timeit.timeit(number=1))
# ------------------------------------------------------------

import sys
import ast
import timeit
from functools import lru_cache

# ---------------------------- Method 1 ----------------------------
class SolutionRolling:
    def maximumPath(self, mat):
        """
        Rolling-row DP:
          prev[c] stores best sum reaching row r-1, col c.
          curr[c] = mat[r][c] + max(prev[c-1], prev[c], prev[c+1])
        Keep only 1 previous row -> O(m) space.

        Time  : O(n*m)  -- touch each cell once with O(1) work
        Space : O(m)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        prev = mat[0][:]  # dp for row 0

        for r in range(1, n):
            curr = [0] * m
            for c in range(m):
                best_above = prev[c]                     # from directly above
                if c > 0:
                    best_above = max(best_above, prev[c-1])  # from up-left
                if c + 1 < m:
                    best_above = max(best_above, prev[c+1])  # from up-right
                curr[c] = mat[r][c] + best_above
            prev = curr  # roll
        return max(prev)  # best in last row


# ---------------------------- Method 2 ----------------------------
class SolutionFull:
    def maximumPath(self, mat):
        """
        Full DP table for clarity:
          dp[r][c] = mat[r][c] + max(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1])

        Time  : O(n*m)
        Space : O(n*m)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        dp = [[0] * m for _ in range(n)]
        dp[0] = mat[0][:]

        for r in range(1, n):
            for c in range(m):
                best = dp[r-1][c]
                if c > 0:
                    best = max(best, dp[r-1][c-1])
                if c + 1 < m:
                    best = max(best, dp[r-1][c+1])
                dp[r][c] = mat[r][c] + best

        return max(dp[-1])


# ---------------------------- Method 3 ----------------------------
class SolutionMemo:
    def maximumPath(self, mat):
        """
        Top-down recursion with memo:
          f(r,c) = mat[r][c] + max(f(r+1,c-1), f(r+1,c), f(r+1,c+1))
        Answer = max_c f(0,c)

        Time  : O(n*m)   -- each state computed once
        Space : O(n*m)   -- memo; recursion depth O(n)
        """
        n = len(mat)
        m = len(mat[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        @lru_cache(None)
        def f(r, c):
            if c < 0 or c >= m:
                return float("-inf")  # invalid
            if r == n - 1:
                return mat[r][c]
            return mat[r][c] + max(f(r + 1, c - 1), f(r + 1, c), f(r + 1, c + 1))

        return max(f(0, c) for c in range(m))


# ------------------------------ I/O ------------------------------
def _parse_matrix_from_stdin():
    """
    Supports:
      1) "n m" on first line followed by n rows of m ints
      2) one-line Python-like list "[[...], [...], ...]"
    """
    text = sys.stdin.read().strip()
    if not text:
        print("Please provide a matrix.\nExamples:\n  3 3\n  3 6 1\n  2 3 4\n  5 5 1\nor\n  [[3,6,1],[2,3,4],[5,5,1]]")
        sys.exit(0)

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    # case 2: bracketed matrix
    if len(lines) == 1 and "[" in lines[0]:
        try:
            mat = ast.literal_eval(lines[0])
            # Basic validation
            if not isinstance(mat, list) or (mat and not isinstance(mat[0], list)):
                raise ValueError
            return mat
        except Exception:
            print("Failed to parse bracketed matrix.")
            sys.exit(1)

    # case 1: n m + rows
    head = lines[0].replace(",", " ").split()
    if len(head) >= 2 and all(tok.lstrip("-").isdigit() for tok in head[:2]):
        n, m = map(int, head[:2])
        if len(lines) < 1 + n:
            print(f"Expected {n} rows after 'n m'.")
            sys.exit(1)
        mat = []
        for i in range(n):
            row = list(map(int, lines[1 + i].replace(",", " ").split()))
            if len(row) != m:
                print(f"Row {i} must have {m} integers.")
                sys.exit(1)
            mat.append(row)
        return mat

    # Fallback: try parse all lines as equal-length rows
    mat = [list(map(int, ln.replace(",", " ").split())) for ln in lines]
    m = len(mat[0])
    if any(len(r) != m for r in mat):
        print("Rows have inconsistent lengths; unable to parse.")
        sys.exit(1)
    return mat

def _preview(mat, limit=80):
    n = len(mat)
    m = len(mat[0]) if n else 0
    flat = " | ".join(" ".join(map(str, row)) for row in mat)
    if len(flat) > limit:
        flat = flat[:limit] + "..."
    return f"matrix {n}x{m}: {flat}"

# ------------------------------ main ------------------------------
def main():
    mat = _parse_matrix_from_stdin()
    print(_preview(mat))
    print()

    s1 = SolutionRolling()
    s2 = SolutionFull()
    s3 = SolutionMemo()

    # Time each method once using timeit.timeit(number=1)
    t1 = timeit.timeit(lambda: s1.maximumPath(mat), number=1)
    a1 = s1.maximumPath(mat)

    t2 = timeit.timeit(lambda: s2.maximumPath(mat), number=1)
    a2 = s2.maximumPath(mat)

    t3 = timeit.timeit(lambda: s3.maximumPath(mat), number=1)
    a3 = s3.maximumPath(mat)

    print("Rolling-row DP  (O(n*m) time, O(m) space)   :", a1)
    print("Time (ms): {:.3f}\n".format(t1 * 1000.0))
    print("Full-table DP   (O(n*m) time, O(n*m) space) :", a2)
    print("Time (ms): {:.3f}\n".format(t2 * 1000.0))
    print("Top-down + memo (O(n*m) time, O(n*m) space) :", a3)
    print("Time (ms): {:.3f}".format(t3 * 1000.0))

    ok = (a1 == a2 == a3)
    print("\nAll methods agree ✔" if ok else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

**Option A – n m + rows**

```
python3 maximum_path_sum.py
3 3
3 6 1
2 3 4
5 5 1
```

**Option B – bracketed**

```
python3 maximum_path_sum.py
[[3,6,1],[2,3,4],[5,5,1]]
```

**Example output (timings vary):**

```
matrix 3x3: 3 6 1 | 2 3 4 | 5 5 1

Rolling-row DP  (O(n*m) time, O(m) space)   : 15
Time (ms): 0.060

Full-table DP   (O(n*m) time, O(n*m) space) : 15
Time (ms): 0.075

Top-down + memo (O(n*m) time, O(n*m) space) : 15
Time (ms): 0.092

All methods agree ✔
```

---

## 6) Real-World Use Cases (short & important)

1. **Seam/stripe scoring in images or terrain**
   When evaluating the *best* (maximum score) downward path subject to adjacent/diagonal step constraints (e.g., energy/reward maps, ridge detection, terrain traversal heuristics).

2. **Stage-wise decision pipelines**
   Rows model *stages* in a pipeline (e.g., days, time steps); columns model alternative choices with adjacency constraints between stages. We want the path maximizing aggregate reward.

3. **Game AI / grid scoring**
   In grid-based games where movement to the next row is restricted to the three neighbors, compute the maximum collectible reward from top to bottom.

4. **Financial roll-over with adjacency limits**
   Select one instrument per period (row) with allowed transitions only to nearby “risk buckets” (columns), maximizing total return under transition limits.
