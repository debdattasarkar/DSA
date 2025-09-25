# Get Minimum Squares

**Difficulty:** Medium
**Accuracy:** 45.22%
**Submissions:** 42K+
**Points:** 4

---

## Problem Statement

Given a number `n`, find the **minimum number of perfect squares** (square of an integer) that sum up to `n`.

---

## Examples

### Example 1

**Input:** `n = 100`
**Output:** `1`
**Explanation:** `10 * 10 = 100`

### Example 2

**Input:** `n = 6`
**Output:** `3`
**Explanation:** `1 * 1 + 1 * 1 + 2 * 2 = 6`

---

## Expected Time Complexity

`O(n * sqrt(n))`

## Expected Space Complexity

`O(n)`

---

## Constraints

`1 <= n <= 10^4`

---

## Company Tags

* Amazon
* Microsoft
* Wipro

---

## Topic Tags

* Dynamic Programming
* Algorithms
* Arrays

---

## Related Articles

* [Minimum Number Of Squares Whose Sum Equals To Given Number N](https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/)

---

---

awesome—here’s the full, interview-ready pack for **Get Minimum Squares**.

---

# 2) Explanation + step-by-step dry run

## Problem

Given `n`, return the **minimum count** of perfect squares whose sum is exactly `n`.

> Examples:
> `n=100 → 1 (10²)`
> `n=6 → 3 (1² + 1² + 2²)`

---

## Approach A (most expected): Bottom-up DP — `O(n·√n)`

Let `dp[x]` = minimum squares to form `x`.
Transition:

```
dp[0] = 0
dp[x] = 1 + min( dp[x - s] )  for all perfect squares s ≤ x
```

Why correct? The last square used has value `s`; then we need the best for the remainder `x - s`.

### Dry run for `n = 6`

Perfect squares ≤ 6: {1, 4}

* `dp[0]=0`
* `dp[1]=1 + dp[0]=1`
* `dp[2]=1 + min(dp[1]) = 2`  (1+1)
* `dp[3]=1 + min(dp[2]) = 3`  (1+1+1)
* `dp[4]=1 + min(dp[0]) = 1`  (4)
* `dp[5]=1 + min(dp[4], dp[1]) = 1 + min(1,1) = 2`  (4+1)
* `dp[6]=1 + min(dp[5], dp[2]) = 1 + min(2,2) = 3`  ✔

### Dry run for `n = 12`

Squares ≤ 12: {1,4,9}

* `dp[9]=1` (9)
* `dp[10]=1 + min(dp[9],dp[6],dp[1]) = 2`
* `dp[11]=1 + min(dp[10],dp[7],dp[2]) = 3`
* `dp[12]=1 + min(dp[11],dp[8],dp[3]) = 1 + min(3,2,3) = 3`  (4+4+4) ✔

---

## Approach B (math shortcut): 1/2/3/4 answer using number theory — `O(√n)`

Facts:

* **Lagrange’s four-square theorem:** every `n` is sum of ≤ 4 squares.
* **Legendre’s three-square theorem (easy test for 4):**
  If repeatedly divide `n` by 4 until it’s not divisible by 4 and the result is `(8b + 7)`, then **answer is 4**.
* If `n` is itself a perfect square → **1**.
* If `n = a² + b²` for some `a,b` → **2** (check `a` from 0..√n).
* Otherwise (not 1, not 2, not forced 4) → **3**.

This gives a super fast solution.

---

## Approach C (BFS over residuals) — `O(n·√n)` but intuitive

Think of nodes as integers `0..n`. From `x`, edges go to `x - s` for squares `s`.
The shortest path (number of edges) from `n` to `0` equals the minimum count. (Same complexity as DP; good for explaining breadth-first optimality.)

---

# 3) Python solutions (with inline comments)

All match the required interface:

```python
#User function Template for python3

class Solution:
    def MinSquares(self, n):
        # Code here
```

## A) Bottom-up DP (recommended baseline)

```python
#User function Template for python3

import math

class Solution:
    def MinSquares(self, n: int) -> int:
        """
        Bottom-up DP:
          dp[x] = 1 + min_{s in squares, s<=x} dp[x - s]
        Time : O(n * sqrt(n))  -- ~sqrt(n) squares per x
        Space: O(n)
        """
        # Precompute all perfect squares ≤ n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [10**9] * n     # dp[0]=0, others large
        for x in range(1, n + 1):  # O(n)
            # Try every square ≤ x
            for s in squares:      # up to O(sqrt(n)) per x
                if s > x:
                    break
                dp[x] = min(dp[x], 1 + dp[x - s])
        return dp[n]
```

---

## B) Number-theory shortcut (fastest)

```python
#User function Template for python3

import math

class SolutionMath:
    def MinSquares(self, n: int) -> int:
        """
        Math-based:
          1) If n is a perfect square -> 1
          2) Reduce m = n by removing factors of 4; if m % 8 == 7 -> 4 (Legendre)
          3) If n = a^2 + b^2 for some a -> 2
          4) Else -> 3
        Time : O(sqrt(n))
        Space: O(1)
        """
        def is_square(x: int) -> bool:
            r = int(math.isqrt(x))
            return r * r == x

        if is_square(n):
            return 1

        # Check the 4-squares necessity quickly
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # Check if sum of two squares
        r = int(math.isqrt(n))
        for a in range(r + 1):   # O(sqrt(n))
            if is_square(n - a * a):
                return 2

        # If not 1, not 2, not forced 4 => must be 3
        return 3
```

---

## C) Top-down memo (same as DP, recursive flavor)

```python
#User function Template for python3

import math
from functools import lru_cache

class SolutionMemo:
    def MinSquares(self, n: int) -> int:
        """
        Top-down recursion with memo.
        Time : O(n * sqrt(n))
        Space: O(n) recursion + memo
        """
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        @lru_cache(None)
        def solve(x: int) -> int:
            if x == 0:
                return 0
            best = 10**9
            for s in squares:
                if s > x:
                    break
                best = min(best, 1 + solve(x - s))
            return best

        return solve(n)
```

> What to present in an interview:
>
> * Start with the **DP** (clear correctness, fits constraints).
> * Mention the **math shortcut** for elegance and speed.
> * Optionally note the **BFS** viewpoint equals the DP recurrence.

---

# 4) Interview Q&A (high-yield)

**Q1. Why does the DP recurrence work?**
*A:* The last term in the optimal representation is some square `s`. Removing it leaves `x - s`, whose optimal answer is `dp[x - s]`. Minimizing over all possible `s` gives `dp[x]`.

**Q2. Complexity of DP?**
*A:* For each `x` we iterate over `⌊√x⌋` squares ⇒ `O(n·√n)` time, `O(n)` space.

**Q3. Is a greedy (“take the largest square each time”) correct?**
*A:* No. Example: `n=12`. Greedy picks `9 -> 3 more` (total 4), but optimal is `4+4+4` (3 terms).

**Q4. Explain the `4^a(8b+7)` check.**
*A:* By **Legendre’s three-square theorem**, numbers of the form `4^a(8b+7)` **cannot** be written as the sum of three squares, so they need **exactly 4**. We strip factors of 4 and test `mod 8`.

**Q5. Order of checks in the math solution?**
*A:* Typically:

1. If perfect square → 1.
2. If of the `4^a(8b+7)` form → 4.
3. If sum of two squares → 2.
4. Else → 3.
   This covers all cases (by Lagrange: ≤4).

**Q6. Can we precompute squares smartly?**
*A:* Yes—generate once up to `√n`. For multiple queries with varying `n` up to `N`, precompute squares up to `√N` and reuse.

**Q7. BFS correctness sketch?**
*A:* Interpreting edges as “subtract a square,” the shortest path from `n` to `0` counts square selections. BFS explores by layer count, returning the minimal number.

---

---

here’s a **ready-to-run program** for **Get Minimum Squares** that:

* reads `n` from stdin,
* solves it **three ways** (DP, Math shortcut, and BFS),
* prints the results, and
* **times** each using `timeit`.

I’ve added tight **time/space comments** inline where it counts.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Get Minimum Squares
# Find min number of perfect squares that sum to n
#
# Methods:
#   1) Bottom-up DP (O(n * sqrt(n)) time, O(n) space)  <-- recommended baseline
#   2) Number-theory shortcut (O(sqrt(n)) time, O(1) space)
#   3) BFS on residuals (O(n * sqrt(n)) time, O(n) space)  <-- educational
#
# Input  (stdin): a single integer n
# Output: each method's answer and run time (ms)
# ------------------------------------------------------------

import sys
import timeit
import math
from collections import deque

# ---------------------- 1) Bottom-up DP ----------------------
class SolutionDP:
    def MinSquares(self, n: int) -> int:
        """
        dp[x] = 1 + min_{s in squares, s<=x} dp[x - s]

        Time : O(n * sqrt(n))  -- ~sqrt(n) squares per x
        Space: O(n)            -- dp array of size n+1
        """
        # Precompute all perfect squares <= n (O(sqrt(n)) numbers)
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # dp[0] = 0 (zero sum needs zero squares); init others to +inf
        dp = [0] + [10**9] * n

        # Fill bottom-up (O(n * sqrt(n)))
        for x in range(1, n + 1):
            for s in squares:
                if s > x:
                    break
                # One square 's' + best for remainder (x - s)
                cand = 1 + dp[x - s]
                if cand < dp[x]:
                    dp[x] = cand
        return dp[n]


# ------------------ 2) Number-theory shortcut ----------------
class SolutionMath:
    def MinSquares(self, n: int) -> int:
        """
        Uses classic results:
          - If n is perfect square           -> 1
          - Strip factors of 4; if m % 8==7  -> 4  (Legendre)
          - If n = a^2 + b^2 for some a      -> 2
          - Otherwise                        -> 3  (Lagrange ensures <=4)

        Time : O(sqrt(n))
        Space: O(1)
        """
        def is_square(x: int) -> bool:
            r = int(math.isqrt(x))
            return r * r == x

        # Case 1: 1 square
        if is_square(n):
            return 1

        # Quick 4-test: n = 4^a * (8b + 7)  => needs exactly 4 squares
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # Case 2: sum of two squares?
        r = int(math.isqrt(n))
        for a in range(r + 1):
            if is_square(n - a * a):
                return 2

        # Case 3: otherwise it must be 3
        return 3


# --------------------------- 3) BFS ---------------------------
class SolutionBFS:
    def MinSquares(self, n: int) -> int:
        """
        BFS over residuals:
          Nodes = {0..n}, edges x->x-s for each square s<=x.
          Shortest path length from n to 0 = answer.

        Time : O(n * sqrt(n))   -- each x explores ~sqrt(x) edges
        Space: O(n)             -- visited array / queue
        """
        if n == 0:
            return 0

        squares = [i * i for i in range(1, int(math.isqrt(n)) + 1)]
        q = deque([n])
        dist = 0
        visited = [False] * (n + 1)
        visited[n] = True

        # Standard BFS layers count the number of squares used
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == 0:
                    return dist
                for s in squares:
                    if s > x:
                        break
                    nxt = x - s
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            dist += 1
        return dist  # unreachable in theory (Lagrange)

# ----------------------------- I/O ---------------------------
def _read_n():
    data = sys.stdin.read().strip().split()
    if not data:
        print("Please provide n (1 <= n <= 10000).")
        sys.exit(0)
    return int(data[0])

def main():
    n = _read_n()

    dp_solver   = SolutionDP()
    math_solver = SolutionMath()
    bfs_solver  = SolutionBFS()

    # ---- time each method once with timeit (full run) ----
    t_dp   = timeit.timeit(lambda: dp_solver.MinSquares(n),   number=1)
    ans_dp = dp_solver.MinSquares(n)

    t_math   = timeit.timeit(lambda: math_solver.MinSquares(n), number=1)
    ans_math = math_solver.MinSquares(n)

    # BFS can be slower; still fine for n <= 1e4
    t_bfs   = timeit.timeit(lambda: bfs_solver.MinSquares(n),  number=1)
    ans_bfs = bfs_solver.MinSquares(n)

    print(f"n: {n}\n")
    print(f"DP (O(n·√n)) answer        : {ans_dp}")
    print(f"DP time (ms)               : {t_dp*1000:.3f}\n")

    print(f"Math shortcut (O(√n)) ans  : {ans_math}")
    print(f"Math shortcut time (ms)    : {t_math*1000:.3f}\n")

    print(f"BFS (O(n·√n)) answer       : {ans_bfs}")
    print(f"BFS time (ms)              : {t_bfs*1000:.3f}\n")

    ok = (ans_dp == ans_math == ans_bfs)
    print("All methods agree ✔" if ok else "WARNING: Methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 min_squares.py
6
```

**Example output (timings vary by machine):**

```
n: 6

DP (O(n·√n)) answer        : 3
DP time (ms)               : 0.170

Math shortcut (O(√n)) ans  : 3
Math shortcut time (ms)    : 0.025

BFS (O(n·√n)) answer       : 3
BFS time (ms)              : 0.210

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact)

1. **Shortest-steps problems with square moves:** Modeling minimal jumps where allowed step sizes are perfect squares (e.g., board games, grid hops). The DP/BFS formulation transfers directly.

2. **Compiler/code-gen & optimization pedagogy:** A canonical “unbounded coin change” variant; teaches building optimal substructure, bottom-up DP tables, and BFS shortest-path equivalence.

3. **Cryptography/number theory tooling:** Fast characterization of representations of integers as sums of squares (Legendre/Lagrange checks) used in math software and primality/representation explorations.

4. **Heuristic resource packing:** When resource chunks naturally come in squared units (e.g., tiling square blocks, binning pixels), the minimal count perspective offers a clean baseline for greedy-vs-DP comparisons.
