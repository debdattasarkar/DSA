# Matrix Chain Multiplication

**Difficulty:** Hard
**Accuracy:** 49.64%
**Submissions:** 174K+
**Points:** 8

---

## Problem Statement

Given an array `arr[]` which represents the dimensions of a sequence of matrices where the `iᵗʰ` matrix has the dimensions `(arr[i-1] x arr[i])` for `i >= 1`, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the **least number of multiplications**.

---

## Examples

### Example 1

**Input:** `arr[] = [2, 1, 3, 4]`
**Output:** `20`
**Explanation:**
There are 3 matrices of dimensions `2×1`, `1×3`, and `3×4`. Let these 3 input matrices be `M1, M2, M3`.
There are two ways to multiply:

* `((M1 × M2) × M3)` and `(M1 × (M2 × M3))`
  Note that the result of `(M1 × M2)` is a `2×3` matrix and result of `(M2 × M3)` is a `1×4` matrix.
  `((M1 × M2) × M3)` requires `(2×1×3) + (2×3×4) = 30`
  `(M1 × (M2 × M3))` requires `(1×3×4) + (2×1×4) = 20`
  The minimum of these two is **20**.

---

### Example 2

**Input:** `arr[] = [1, 2, 3, 4, 3]`
**Output:** `30`
**Explanation:**
There are 4 matrices of dimensions `1×2`, `2×3`, `3×4`, `4×3`. Let these input matrices be `M1, M2, M3, M4`.
The minimum number of multiplications are obtained by `((M1 × M2) × M3) × M4`.
The minimum number is `(1×2×3) + (1×3×4) + (1×4×3) = 30`.

---

### Example 3

**Input:** `arr[] = [1, 2, 3, 4, 3]`
**Output:** `30`
**Explanation:**
There are 4 matrices of dimensions `1×2`, `2×3`, `3×4`, `4×3`. Let these input matrices be `M1, M2, M3, M4`.
The minimum number of multiplications are obtained by `((M1 × M2) × M3) × M4`.
The minimum number is `(1×2×3) + (1×3×4) + (1×4×3) = 30`.

---

### Example 4

**Input:** `arr[] = [3, 4]`
**Output:** `0`
**Explanation:**
As there is only one matrix, there is **no cost** of multiplication.

---

## Constraints

* `2 ≤ arr.size() ≤ 100`
* `1 ≤ arr[i] ≤ 200`

---

## Expected Complexities

* **Time Complexity:** `O(n^3)`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

* Flipkart
* Microsoft
* FactSet

---

## Topic Tags

* Dynamic Programming
* Matrix
* Data Structures
* Algorithms

---

## Related Interview Experiences

* Microsoft Interview Experience Set 128 Campus Internship

---

## Related Articles

* [Matrix Chain Multiplication DP 8](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)

---

---

awesome — here’s your interview-ready pack for **Matrix Chain Multiplication (MCM)**.

---

# 2) Explanation + step-by-step dry run

## Problem recap

You’re given an array `arr` of dimensions. Matrix `Mi` has size
`arr[i-1] × arr[i]` (so there are `n-1` matrices when `n = len(arr)`).
We must parenthesize the product `M1 M2 … M(n-1)` to **minimize the number of scalar multiplications**. We do **not** actually multiply matrices—just count operations.

## Optimal substructure (classic DP)

Let `dp[i][j]` = **minimum** number of scalar multiplications needed to multiply the subchain `Mi … Mj` (1-indexed matrices).

* **Base:** `dp[i][i] = 0` (a single matrix needs no multiplication).
* **Transition (try the last split at k):**

```
dp[i][j] = min over k in [i..j-1] of
           dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[k] * arr[j])
```

The last term is the cost to multiply the two resulting matrices:
left result is `(arr[i-1] × arr[k])`, right result is `(arr[k] × arr[j])`,
multiplying them costs `arr[i-1] * arr[k] * arr[j]`.

Compute `dp` **bottom-up by chain length** (a.k.a. gap DP) or **top-down with memo**.

### Dry run: `arr = [2, 1, 3, 4]`

Matrices:
`M1: 2×1`, `M2: 1×3`, `M3: 3×4`.

We want `dp[1][3]`:

* `dp[1][1]=dp[2][2]=dp[3][3]=0`
* For `i=1, j=2` (chain M1..M2):

  * only `k=1`: cost = `0 + 0 + 2*1*3 = 6` → `dp[1][2]=6`
* For `i=2, j=3` (chain M2..M3):

  * only `k=2`: cost = `0 + 0 + 1*3*4 = 12` → `dp[2][3]=12`
* For `i=1, j=3` (whole chain):

  * `k=1`: `dp[1][1] + dp[2][3] + 2*1*4 = 0 + 12 + 8 = 20`
  * `k=2`: `dp[1][2] + dp[3][3] + 2*3*4 = 6 + 0 + 24 = 30`
    → **min = 20**, achieved by `(M1 × (M2 × M3))`. ✔

---

# 3) Python solutions (brute → memo → bottom-up)

All fit your required interface:

```python
class Solution:
    def matrixMultiplication(self, arr):
        # code here
```

## A) Brute force recursion (exponential; for exposition)

```python
class SolutionBrute:
    def matrixMultiplication(self, arr):
        """
        Exponential recursion: try every split.
        Time  : super-exponential in practice (~Catalan growth)
        Space : O(n) recursion
        """
        n = len(arr) - 1  # number of matrices
        if n <= 1:
            return 0

        def solve(i, j):
            if i == j:              # one matrix: no cost
                return 0
            best = float("inf")
            for k in range(i, j):   # last multiplication split position
                cost = (solve(i, k) +
                        solve(k + 1, j) +
                        arr[i - 1] * arr[k] * arr[j])
                best = min(best, cost)
            return best

        return solve(1, n)
```

---

## B) Top-down DP with memo (interview-friendly; **O(n³)** time, **O(n²)** space)

```python
from functools import lru_cache

class SolutionMemo:
    def matrixMultiplication(self, arr):
        """
        Classic MCM with recursion + memo.
        Time  : O(n^3)  -- states O(n^2), each tries O(n) splits
        Space : O(n^2)  -- memo; recursion depth O(n)
        """
        n = len(arr) - 1
        if n <= 1:
            return 0

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = float("inf")
            # try all k as the final split
            for k in range(i, j):
                best = min(best,
                           dp(i, k) + dp(k + 1, j) + arr[i - 1] * arr[k] * arr[j])
            return best

        return dp(1, n)
```

---

## C) Bottom-up gap DP (most expected in interviews; **O(n³)** / **O(n²)**)

```python
class Solution:
    def matrixMultiplication(self, arr):
        """
        Bottom-up dynamic programming by chain length.
        dp[i][j] = min cost to multiply Mi..Mj (1-indexed matrices)

        Time  : O(n^3)
        Space : O(n^2)
        """
        n = len(arr) - 1               # number of matrices
        if n <= 1:
            return 0

        # 1-based indexing DP table
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # len is the chain length (number of matrices in subchain)
        for length in range(2, n + 1):            # start from 2 matrices
            for i in range(1, n - length + 2):    # i..j is the subchain
                j = i + length - 1
                dp[i][j] = float("inf")
                # try every split k between i..j-1
                for k in range(i, j):
                    cost = (dp[i][k] +
                            dp[k + 1][j] +
                            arr[i - 1] * arr[k] * arr[j])
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        return dp[1][n]
```

> Tip: if an interviewer asks for the **parenthesization**, keep another table `opt[i][j]` storing the arg-min split `k` and backtrack to print the parentheses. (Function above returns only the cost.)

---

# 4) Interview Q&A (the ones that actually get asked)

**Q1. Why is the cost term `arr[i-1] * arr[k] * arr[j]`?**
Because after splitting at `k`, left result is `(arr[i-1] × arr[k])`, right result is `(arr[k] × arr[j])`. Multiplying them uses exactly that many scalar multiplications.

**Q2. Why does optimal substructure hold?**
Any optimal parenthesization must make a final split at some `k`. The two subchains on each side must themselves be optimally parenthesized (otherwise we could improve the total), hence the recurrence.

**Q3. Time and space complexity?**
`O(n³)` time (≈ `n²` states × `n` splits), `O(n²)` space for the DP table/memo.

**Q4. Is there a greedy strategy?**
No—local choices (e.g., smallest dimension product first) don’t guarantee global optimality. Counterexamples exist.

**Q5. Can we improve below `O(n³)`?**
For general MCM, the classic DP is `O(n³)`. Some specialized cases (e.g., nearly diagonal chains, bounded dimension ranges) admit optimizations (Knuth, Monge) but not for arbitrary MCM.

**Q6. What does `arr` represent exactly?**
If there are `p` matrices, `arr` has length `p+1`. Matrix `Mi` is `arr[i-1] × arr[i]`. If `arr = [10, 20, 30]`, there are two matrices: `10×20` and `20×30`.

**Q7. Edge cases?**

* Single matrix (`len(arr) == 2`) → cost `0`.
* Very large answers: use Python `int` (unbounded); in fixed languages, use 64-bit.
* Dimensions must align (they do by construction via `arr`).

---

---

here’s a **ready-to-run program** for **Matrix Chain Multiplication (MCM)** that:

* reads the dimension array `arr` from stdin,
* solves it 3 ways (**bottom-up DP**, **memoized recursion**, **brute force**),
* prints outputs, and
* **times** each with `timeit.timeit(number=1)`.

Inline comments call out the **time/space complexity** right where they apply.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Matrix Chain Multiplication (MCM)
# arr = [p0, p1, p2, ..., pn]   => there are n matrices:
#   M1 is p0 x p1,  M2 is p1 x p2, ..., Mn is p(n-1) x pn
# Goal: parenthesize M1..Mn to minimize scalar multiplications.
#
# Methods:
#   1) Bottom-up DP (recommended)         : O(n^3) time, O(n^2) space
#   2) Top-down DP with memoization       : O(n^3) time, O(n^2) space
#   3) Brute force recursion (educational): exponential time, O(n) stack
#
# Input (stdin):
#   One line containing arr (space/comma separated, brackets allowed)
#
# Output:
#   - Echo parsed arr
#   - Minimal costs from each method
#   - Per-method timings (ms) with timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit
from functools import lru_cache

# ---------------------------- Method 1 ----------------------------
class Solution:
    def matrixMultiplication(self, arr):
        """
        Bottom-up gap DP.
        dp[i][j] = min cost to multiply Mi..Mj (1-indexed matrices).
        Transition:
          dp[i][j] = min_{k in [i..j-1]} dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]

        n   : number of matrices = len(arr) - 1
        Time : O(n^3)  -- ~n^2 states (i,j), each tries O(n) splits
        Space: O(n^2)  -- table dp of size (n+1) x (n+1)
        """
        n = len(arr) - 1
        if n <= 1:
            return 0

        # dp is (n+1)x(n+1) to use 1-based matrix indices conveniently
        dp = [[0] * (n + 1) for _ in range(n + 1)]  # O(n^2) space

        # length = number of matrices in the subchain
        for length in range(2, n + 1):                  # O(n) lengths
            for i in range(1, n - length + 2):          # O(n) starts
                j = i + length - 1
                best = float('inf')
                # try all final split positions k
                for k in range(i, j):                   # O(n) splits
                    cost = (dp[i][k]
                            + dp[k + 1][j]
                            + arr[i - 1] * arr[k] * arr[j])  # scalar mults of last step
                    if cost < best:
                        best = cost
                dp[i][j] = best

        return dp[1][n]


# ---------------------------- Method 2 ----------------------------
class SolutionMemo:
    def matrixMultiplication(self, arr):
        """
        Top-down recursion with memo (same recurrence as bottom-up).

        Time : O(n^3)  -- each (i,j) computed once, each tries O(n) k's
        Space: O(n^2)  -- memo table; recursion depth O(n)
        """
        n = len(arr) - 1
        if n <= 1:
            return 0

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            best = float('inf')
            for k in range(i, j):  # try last split at k
                best = min(best,
                           dp(i, k) + dp(k + 1, j) + arr[i - 1] * arr[k] * arr[j])
            return best

        return dp(1, n)


# ---------------------------- Method 3 ----------------------------
class SolutionBrute:
    def matrixMultiplication(self, arr):
        """
        Brute-force recursion (no memoization).
        Tries every parenthesization.

        Time : Exponential (Catalan growth) -- for tiny n only
        Space: O(n) recursion stack
        """
        n = len(arr) - 1
        if n <= 1:
            return 0

        def solve(i, j):
            if i == j:
                return 0
            best = float('inf')
            for k in range(i, j):
                cost = (solve(i, k)
                        + solve(k + 1, j)
                        + arr[i - 1] * arr[k] * arr[j])
                best = min(best, cost)
            return best

        return solve(1, n)


# ------------------------------ I/O ------------------------------
def _parse_arr():
    """
    Accepts inputs like:
      2 1 3 4
      [2,1,3,4]
      2,1,3,4
    """
    line = sys.stdin.read().strip()
    if not line:
        print("Please provide one line with arr, e.g. '2 1 3 4' or '[2,1,3,4]'.")
        sys.exit(0)
    for ch in "[],":
        line = line.replace(ch, " ")
    parts = [p for p in line.split() if p]
    try:
        arr = list(map(int, parts))
    except Exception:
        print("Failed to parse integers from input.")
        sys.exit(1)
    if len(arr) < 2:
        print("arr must contain at least 2 numbers (one matrix => 2 dims).")
        sys.exit(1)
    return arr

def _preview(arr, limit=80):
    s = " ".join(map(str, arr))
    if len(s) <= limit:
        return f"arr (len={len(arr)}): [{s}]"
    return f"arr (len={len(arr)}): [{s[:limit]}...]"

# ------------------------------ Main ------------------------------
def main():
    arr = _parse_arr()
    print(_preview(arr))
    print()

    sol_dp   = Solution()
    sol_mem  = SolutionMemo()
    sol_brut = SolutionBrute()

    # time each method once; then compute result again for printing clarity
    t_dp   = timeit.timeit(lambda: sol_dp.matrixMultiplication(arr), number=1)
    ans_dp = sol_dp.matrixMultiplication(arr)

    t_mem   = timeit.timeit(lambda: sol_mem.matrixMultiplication(arr), number=1)
    ans_mem = sol_mem.matrixMultiplication(arr)

    # Brute is only safe for small n; guard to avoid long runs
    n = len(arr) - 1
    if n <= 12:  # generous but safe-ish
        t_brut   = timeit.timeit(lambda: sol_brut.matrixMultiplication(arr), number=1)
        ans_brut = sol_brut.matrixMultiplication(arr)
        brute_line = f"{ans_brut}\nTime (ms): {t_brut * 1000.0:.3f}"
    else:
        brute_line = "(skipped for n>12)"

    print("Bottom-up DP     (O(n^3) time, O(n^2) space):", ans_dp)
    print("Time (ms): {:.3f}\n".format(t_dp * 1000.0))

    print("Top-down + memo  (O(n^3) time, O(n^2) space):", ans_mem)
    print("Time (ms): {:.3f}\n".format(t_mem * 1000.0))

    print("Brute recursion  (exp time, O(n) stack)     :", brute_line)

    agree = True
    if n <= 12:
        agree = (ans_dp == ans_mem == ans_brut)
    else:
        agree = (ans_dp == ans_mem)
    print("\nAll methods agree ✔" if agree else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 mcm.py
2 1 3 4
```

**Example output (timings vary):**

```
arr (len=4): [2 1 3 4]

Bottom-up DP     (O(n^3) time, O(n^2) space): 20
Time (ms): 0.120

Top-down + memo  (O(n^3) time, O(n^2) space): 20
Time (ms): 0.145

Brute recursion  (exp time, O(n) stack)     : 20
Time (ms): 0.090

All methods agree ✔
```

Another sample:

```bash
python3 mcm.py
1 2 3 4 3
```

Output:

```
arr (len=5): [1 2 3 4 3]

Bottom-up DP     (O(n^3) time, O(n^2) space): 30
Time (ms): 0.180

Top-down + memo  (O(n^3) time, O(n^2) space): 30
Time (ms): 0.205

Brute recursion  (exp time, O(n) stack)     : 30
Time (ms): 0.160

All methods agree ✔
```

---

## 6) Real-World Use Cases (concise + high-value)

1. **Relational database query optimization**
   Choosing the order of associative binary operations (e.g., join trees) to minimize cost mirrors MCM: “dimensions” ≈ row counts/widths; “cost” ≈ estimated I/O/CPU.

2. **Automatic differentiation / expression compilation**
   Compilers and ML frameworks decide evaluation order of chained linear ops (e.g., `(((A·B)·C)·D)` vs `(A·(B·(C·D)))`) to reduce FLOPs and memory.

3. **Graphics/robotics transform chains**
   Long chains of coordinate transforms / homogeneous matrices benefit from optimal regrouping to reduce computation when sizes differ.

4. **Signal processing pipelines**
   Multiplying/filtering blocks of differing shapes (FFT blocks, convolution lowering) where the order can change arithmetic cost substantially.
