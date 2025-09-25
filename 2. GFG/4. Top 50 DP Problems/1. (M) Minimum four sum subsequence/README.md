# Minimum four sum subsequence

**Difficulty:** Medium
**Accuracy:** 51.08%
**Submissions:** 6K+
**Points:** 4

---

## Problem Statement

You are given an array `arr[]` of positive integers. Your task is to find the **minimum sum of a subsequence** such that the subsequence includes **at least one element from every group of four consecutive elements** in the array.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 2, 3, 4, 5, 6, 7, 8]`
**Output:** `6`
**Explanation:** `6` is sum of output subsequence `{1, 5}`. Following length-4 subarrays are possible:
`(1, 2, 3, 4)`, `(2, 3, 4, 5)`, `(3, 4, 5, 6)`, `(4, 5, 6, 7)`, `(5, 6, 7, 8)`
Here, our subsequence `{1, 5}` has an element from all above groups of four consecutive elements.

---

### Example 2

**Input:** `arr[] = [2, 1, 3]`
**Output:** `1`
**Explanation:** The size of `arr` is less than 4, so the subsequence is `{1}`.

---

### Example 3

**Input:** `arr[] = [1, 2, 3, 3, 4, 5, 6, 1]`
**Output:** `4`
**Explanation:** The subsequence is `{3, 1}`. Here we consider the second `three`.

---

## Expected Time Complexity

`O(n)`

## Expected Auxiliary Space

`O(n)`

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `1 ≤ arr[i] ≤ 10^5`

---

## Topic Tags

* Arrays
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* [Minimum Sum Subsequence Least One Every Four Consecutive Elements Picked](https://www.geeksforgeeks.org/minimum-sum-subsequence-least-one-every-four-consecutive-elements-picked/)

---

---

awesome—let’s nail **Minimum four-sum subsequence** (pick a subsequence of minimum sum such that **every 4 consecutive elements** in the array contain **at least one picked element**).

---

# 2) Explanation + step-by-step dry run

## Key idea (k = 4)

Let’s call the array `arr[0..n-1]`. We must choose indices so that **no gap of 4** consecutive elements is left without a chosen element. Because all numbers are **positive**, picking fewer and smaller numbers is better.

Think in terms of **the first pick** in any suffix:

* If we pick element at index `i`, then the **next** pick must appear **within the next 4 positions** `[i+1 .. i+4]`, otherwise the 4-length window `[i+1 .. i+4]` would be empty.
* So, if we force-pick `i`, the best future cost is `min(dp[i+1], dp[i+2], dp[i+3], dp[i+4])`.

Define:

* `dp[i]` = **minimum sum** of a valid subsequence **starting by picking index `i`** and then continuing optimally to the right.
* Then
  `dp[i] = arr[i] + min(dp[i+1], dp[i+2], dp[i+3], dp[i+4])`,
  with `dp[j] = 0` for `j ≥ n` (no windows left past the end).

What is the **final answer**? The first chosen index must be in the **first 4 positions** `[0..3]` (otherwise the first window `[0..3]` would be empty). Therefore:

```
answer = min(dp[0], dp[1], dp[2], dp[3])        (use up to n-1 if n < 4)
```

Edge case: if `n < 4`, there are no windows of length 4, but by the problem’s examples we still need to pick **at least one** element — so we pick the **minimum element**, which is already captured by `min(dp[0..n-1])`.

---

## Dry run 1

`arr = [1,2,3,4,5,6,7,8]`, `n=8`

Compute `dp` from right to left. For convenience set `dp[8..11]=0`.

* `dp[7] = 8 + min(0,0,0,0) = 8`
* `dp[6] = 7 + min(8,0,0,0) = 7`
* `dp[5] = 6 + min(7,8,0,0) = 6`
* `dp[4] = 5 + min(6,7,8,0) = 5`
* `dp[3] = 4 + min(5,6,7,8) = 9`
* `dp[2] = 3 + min(9,5,6,7) = 8`
* `dp[1] = 2 + min(8,9,5,6) = 7`
* `dp[0] = 1 + min(7,8,9,5) = 6`

Answer = `min(dp[0..3]) = min(6,7,8,9) = 6` → pick indices `{0,4}` → `{1,5}` in 1-based, sum 6 ✔

---

## Dry run 2

`arr = [1,2,3,3,4,5,6,1]`, `n=8`

(again with `dp[8..11]=0`)

* `dp[7] = 1 + 0 = 1`
* `dp[6] = 6 + min(1,0,0,0) = 7`
* `dp[5] = 5 + min(7,1,0,0) = 5`
* `dp[4] = 4 + min(5,7,1,0) = 4`
* `dp[3] = 3 + min(4,5,7,1) = 4`
* `dp[2] = 3 + min(4,4,5,7) = 7`
* `dp[1] = 2 + min(7,4,4,5) = 6`
* `dp[0] = 1 + min(6,7,4,4) = 5`

Answer = `min(dp[0..3]) = min(5,6,7,4) = 4` → pick `{3, 7}` (0-based) → values `{3,1}`, sum 4 ✔

---

# 3) Python solutions (multiple ways)

The required signature:

```python
# Your task is to complete this function
# Function should return an integer
class Solution:
    def minSum(self,arr):
        # Code here 
```

### A) Clean DP (O(n) time, O(n) space) — easiest to explain

```python
# Your task is to complete this function
# Function should return an integer
class Solution:
    def minSum(self, arr):
        """
        dp[i] = arr[i] + min(dp[i+1], dp[i+2], dp[i+3], dp[i+4])
        Answer = min(dp[0], dp[1], dp[2], dp[3])  (use only existing indices)
        
        Time:  O(n)   (constant 4 lookups per i)
        Space: O(n)   (dp array)
        """
        n = len(arr)
        if n == 0:
            return 0  # not in constraints, but safe
        # Create dp with padding so slices beyond n are zero
        K = 4
        dp = [0] * (n + K)  # dp[n..n+3] = 0 acts as base
        
        # Fill from right to left
        for i in range(n - 1, -1, -1):
            # min over the next 4 dp's (constant-time since K=4)
            dp[i] = arr[i] + min(dp[i + 1], dp[i + 2], dp[i + 3], dp[i + 4])
        
        # The first pick must be within the first 4 indices (or all if n<4)
        upto = min(K, n)
        return min(dp[0:upto])
```

---

### B) Rolling window (O(n) time, **O(1) extra space**) — interview brownie points

We don’t need the whole `dp` array; at step `i`, we only need `dp[i+1..i+4]`. Keep a deque of **exactly 4** values (initially zeros) and slide it while walking from right to left.

```python
from collections import deque

class SolutionRolling:
    def minSum(self, arr):
        """
        Rolling window of size 4 over future dp values.
        Time:  O(n)     (min over 4 is constant-time)
        Space: O(1)     (only 4 future dp values kept)
        """
        n = len(arr)
        if n == 0:
            return 0
        K = 4
        
        # dp_future = [dp[i+1], dp[i+2], dp[i+3], dp[i+4]]
        dp_future = deque([0]*K, maxlen=K)
        best_first_block = float('inf')
        
        # Compute dp[i] right->left; track min(dp[0..min(3,n-1)]) as we go
        for i in range(n - 1, -1, -1):
            dp_i = arr[i] + min(dp_future)   # O(4) constant time
            if i < K:
                # candidate for starting within the first 4 indices
                best_first_block = min(best_first_block, dp_i)
            dp_future.appendleft(dp_i)  # maxlen pops the oldest automatically
        
        return best_first_block
```

---

### C) Top-down recursion with memo (still O(n), but “brute-like” to explain)

Define `solve(i)` as: we must choose the first pick in `[i .. min(i+3, n-1)]`, then recurse from `r+1`.

```python
from functools import lru_cache

class SolutionMemo:
    def minSum(self, arr):
        """
        solve(i) = min_{r in [i .. min(i+3, n-1)]} arr[r] + solve(r+1)
        Answer   = solve(0)
        
        Time:  O(n)  (each i tries up to 4 choices; memoized)
        Space: O(n)  (recursion + memo)
        """
        n = len(arr)
        if n == 0:
            return 0

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 0
            end = min(n - 1, i + 3)  # can pick within the next 4 positions
            best = float('inf')
            for r in range(i, end + 1):
                best = min(best, arr[r] + solve(r + 1))
            return best

        return solve(0)
```

> In interviews: present (A) first (clean & fast), mention (B) if they ask about space, and (C) if they like top-down reasoning.

---

# 4) Interview Q&A (high-yield)

**Q1. Derive the recurrence.**

* If we pick index `i`, the next pick must be within `[i+1..i+4]` to cover the window `[i+1..i+4]`.
* Therefore `dp[i] = arr[i] + min(dp[i+1..i+4])`.
* The first pick must be in `[0..3]` → final answer `min(dp[0..3])` (use `0..n-1` if `n<4`).

**Q2. Why do we add `dp[n..n+3] = 0`?**
Those positions represent “beyond the end,” where no 4-window exists anymore, so **no extra cost** is required.

**Q3. What about `n < 4`?**
No 4-length window exists, but the example shows we must pick **at least one** element. The formula `min(dp[0..n-1])` returns the minimum element automatically.

**Q4. Time/space complexities?**

* DP (A): `O(n)` time, `O(n)` space.
* Rolling (B): `O(n)` time, `O(1)` extra space.
* Memo (C): `O(n)` time, `O(n)` space.

**Q5. Can we generalize to “at least one in every `k` consecutive elements”?**
Yes—replace the constant `4` with `k`:
`dp[i] = arr[i] + min(dp[i+1..i+k])`, and answer is `min(dp[0..k-1])`. Use a **monotonic deque** to keep the window minimum in `O(1)` amortized per step → overall `O(n)`.

**Q6. Why does greedy (always pick current minimum) fail?**
A local minimum can force a future **gap ≥ 4** unless you pick again too soon, increasing the total. The DP considers “pick now and how it shifts the next allowed pick,” which greedy ignores.

---

---

here you go — a **ready-to-run program** for **Get Minimum Squares** that:

* reads `n` from stdin,
* solves it 3 ways (**DP**, **Math shortcut**, **Memoized recursion**),
* prints outputs, and
* **times** each with `timeit.timeit(number=1)`.

I’ve added tight, interview-style **time/space notes** inline.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Get Minimum Squares
# Given n, return the minimum number of perfect squares summing to n
#
# Methods:
#   1) Bottom-up DP (O(n * sqrt(n)) time, O(n) space)   <-- baseline
#   2) Number-theory shortcut (O(sqrt(n)) time, O(1) space)
#   3) Top-down memoized recursion (O(n * sqrt(n)) time, O(n) space)
#
# Input : single integer n (1 <= n <= 1e4)
# Output: answers from each method + per-method timings (ms) via timeit
# ------------------------------------------------------------

import sys
import timeit
import math
from functools import lru_cache

# ------------------ 1) Bottom-up DP (recommended) ------------------
class Solution:
    def MinSquares(self, n: int) -> int:
        """
        dp[x] = 1 + min(dp[x - s]) over all perfect squares s <= x
        Time : O(n * sqrt(n))  -- ~sqrt(n) candidate squares per x, for x=1..n
        Space: O(n)            -- dp array of size n+1
        """
        # Precompute all perfect squares <= n   (O(sqrt(n)) time/space)
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # dp[0]=0; others initialized large (sentinel)
        dp = [0] + [10**9] * n
        # Fill dp bottom-up for x=1..n         (O(n))
        for x in range(1, n + 1):
            # Try each square s <= x           (<= O(sqrt(n)) iters)
            for s in squares:
                if s > x:
                    break
                # Best using s as the last square
                dp[x] = min(dp[x], 1 + dp[x - s])
        return dp[n]


# ------------------ 2) Number-theory shortcut ----------------------
class SolutionMath:
    def MinSquares(self, n: int) -> int:
        """
        Math-based solution:
          • If n is a perfect square → 1
          • Let m = n with all factors of 4 removed; if m % 8 == 7 → 4  (Legendre)
          • If n = a^2 + b^2 for some a → 2
          • Else → 3  (Lagrange's four-square theorem guarantees ≤ 4)
        Time : O(sqrt(n))
        Space: O(1)
        """
        def is_square(x: int) -> bool:
            r = int(math.isqrt(x))
            return r * r == x

        if is_square(n):                      # quick 1-check
            return 1

        # Force-4 check: numbers of the form 4^a * (8b + 7) need exactly 4 squares
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # 2-check: n = a^2 + b^2 ?
        r = int(math.isqrt(n))
        for a in range(r + 1):                # O(sqrt(n))
            if is_square(n - a * a):
                return 2

        # If not 1, not 2, not forced 4 -> must be 3
        return 3


# ------------------ 3) Top-down memoized recursion -----------------
class SolutionMemo:
    def MinSquares(self, n: int) -> int:
        """
        Recursive definition with memo:
          solve(x) = 1 + min_{s square <= x} solve(x - s), solve(0)=0
        Time : O(n * sqrt(n))  -- each x considers ~sqrt(x) squares once
        Space: O(n)            -- memo + recursion stack
        """
        # Precompute squares once (O(sqrt(n)))
        squares = [i * i for i in range(1, int(math.isqrt(n)) + 1)]

        @lru_cache(None)
        def solve(x: int) -> int:
            if x == 0:
                return 0
            best = 10**9
            # Try using each square as the last term (<= O(sqrt(n)) iters)
            for s in squares:
                if s > x:
                    break
                best = min(best, 1 + solve(x - s))
            return best

        return solve(n)


# ------------------------------ I/O --------------------------------
def _read_n():
    data = sys.stdin.read().strip().split()
    if not data:
        print("Please provide an integer n (1 <= n <= 10000).")
        sys.exit(0)
    return int(data[0])

def main():
    n = _read_n()

    sol_dp   = Solution()
    sol_math = SolutionMath()
    sol_mem  = SolutionMemo()

    # --------- Time each method once using timeit.timeit(number=1) ---------
    # Note: timeit returns only timing; compute the answer again (cheap here).
    t_dp   = timeit.timeit(lambda: sol_dp.MinSquares(n), number=1)
    ans_dp = sol_dp.MinSquares(n)

    t_math   = timeit.timeit(lambda: sol_math.MinSquares(n), number=1)
    ans_math = sol_math.MinSquares(n)

    t_mem   = timeit.timeit(lambda: sol_mem.MinSquares(n), number=1)
    ans_mem = sol_mem.MinSquares(n)

    # ---------------------------- Output -----------------------------------
    print(f"n: {n}\n")
    print("Bottom-up DP        (O(n*sqrt(n)) time, O(n) space) :", ans_dp)
    print("Time (ms): {:.3f}".format(t_dp * 1000.0))
    print()
    print("Math shortcut       (O(sqrt(n)) time, O(1) space)   :", ans_math)
    print("Time (ms): {:.3f}".format(t_math * 1000.0))
    print()
    print("Top-down (memo)     (O(n*sqrt(n)) time, O(n) space) :", ans_mem)
    print("Time (ms): {:.3f}".format(t_mem * 1000.0))

    agree = (ans_dp == ans_math == ans_mem)
    print("\nAll methods agree ✔" if agree else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 min_squares.py
6
```

**Example output (timings vary):**

```
n: 6

Bottom-up DP        (O(n*sqrt(n)) time, O(n) space) : 3
Time (ms): 0.240

Math shortcut       (O(sqrt(n)) time, O(1) space)   : 3
Time (ms): 0.030

Top-down (memo)     (O(n*sqrt(n)) time, O(n) space) : 3
Time (ms): 0.215

All methods agree ✔
```

---

## 6) Real-World Use Cases (concise + relevant)

1. **Coin-change–like modeling with square denominations**
   When the “denominations” are perfect squares (e.g., scoring systems or energy units), this computes the fewest tokens needed to reach a target.

2. **Tiling/graphics with square tiles**
   Approximating an `n`-area using integer square tiles with the **fewest** tiles (idealized model). The math shortcut quickly bounds solutions.

3. **Algorithmic pattern**
   Classic DP archetype for “min parts to reach sum” problems (e.g., minimum perfect cubes, polygonal numbers), useful for teaching reductions and optimizing with number-theory shortcuts.
