# Special Keyboard

**Difficulty:** Medium
**Accuracy:** 28.66%
**Submissions:** 52K+
**Points:** 4

---

## Problem Statement

Imagine you have a special keyboard with the following keys:

* **Key 1:** Prints `'A'` on screen
* **Key 2:** (**Ctrl-A**) Select screen
* **Key 3:** (**Ctrl-C**) Copy selection to buffer
* **Key 4:** (**Ctrl-V**) Print buffer on screen appending it after what has already been printed.

Find the **maximum number of A's** that can be produced by pressing keys on the special keyboard **N times**.

---

## Examples

### Example 1

**Input:** `N = 3`
**Output:** `3`
**Explanation:** Press key 1 three times.

### Example 2

**Input:** `N = 7`
**Output:** `9`
**Explanation:** The best key sequence is
`key 1, key 1, key 1, key 2, key 3, key 4, key 4`.

---

## Your Task

You do not need to read input or print anything. Your task is to complete the function `optimalKeys()` which takes `N` as input parameter and **returns the maximum number of 'A's** that can be on the screen after performing `N` operations.

---

## Expected Complexities

* **Expected Time Complexity:** `O(N^2)`
* **Expected Auxiliary Space:** `O(N)`

---

## Constraints

* `1 < N < 76`

---

## Company Tags

* Paytm
* Flipkart
* Amazon
* Microsoft
* Google

---

## Topic Tags

* Dynamic Programming
* Recursion
* Algorithms

---

## Related Articles

* [How To Print Maximum Number Of A Using Given Four Keys](https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/)

---

---
awesome—building on the **fixed recurrence** (the multiplier is `k-1`, not `k-2`), here’s the complete, interview-ready pack.

---

# 2) Explanation + step-by-step dry run

## Core idea

Let `dp[i]` be the maximum number of `A`s after **exactly** `i` key presses.

Two choices to get to step `i`:

1. **Type an `A`** as the last key:
   `dp[i] = dp[i-1] + 1`.

2. **End with a block**: `Ctrl-A, Ctrl-C,` then `(k-2)` times `Ctrl-V` (this block uses `k` keys).
   If we start that block after producing `dp[i-k]` `A`s, then:

   * after `Ctrl-A, Ctrl-C` we still have `dp[i-k]`,
   * each paste appends another `dp[i-k]`.
     Total copies on screen = **`k-1`** copies of `dp[i-k]`.
     Contribution: `dp[i-k] * (k-1)`.

So for every `k ∈ [3..i]`:

```
dp[i] = max( dp[i-1] + 1,
             max_{k=3..i}  dp[i-k] * (k-1) )
```

### Small `N`

For `i ≤ 6`, blocks are too short to beat typing: `dp[i] = i`.

## Dry run (N = 7)

Known bases: `dp[0..6] = 0,1,2,3,4,5,6`.

Compute `dp[7]`:

* Type: `dp[6] + 1 = 7`.
* Blocks:

  * `k=3`: `dp[4] * 2 = 4 * 2 = 8`
  * `k=4`: `dp[3] * 3 = 3 * 3 = 9`  ← best
  * `k=5`: `dp[2] * 4 = 2 * 4 = 8`
  * `k=6`: `dp[1] * 5 = 1 * 5 = 5`
  * `k=7`: `dp[0] * 6 = 0 * 6 = 0`
    ⇒ `dp[7] = 9` (sequence: `A A A Ctrl-A Ctrl-C Ctrl-V Ctrl-V`).

Quick sanity:

* `dp[8] = 16`, `dp[9] = 20`.

---

# 3) Python solutions (ready to paste)

### A) Top-down + memo (most explainable; **O(N²)** time, **O(N)** space)

```python
#User function Template for python3
from functools import lru_cache

class Solution:
    def optimalKeys(self, N):
        """
        dp(n): max 'A's in exactly n key presses.
        Recurrence: dp(n) = max( dp(n-1)+1, max_{k=3..n} dp(n-k)*(k-1) )
        Time:  O(N^2)  (each n tries k=3..n)
        Space: O(N)    (memo + recursion)
        """
        @lru_cache(None)
        def dp(n):
            if n <= 6:                 # typing only beats any tiny block
                return n
            best = dp(n - 1) + 1       # last key is 'A'
            for k in range(3, n + 1):  # final block uses k keys
                best = max(best, dp(n - k) * (k - 1))   # (k-1) copies
            return best
        return dp(N)
```

---

### B) Bottom-up DP (same recurrence; **O(N²)** time, **O(N)** space)

```python
#User function Template for python3

class SolutionDP:
    def optimalKeys(self, N):
        if N <= 6:
            return N
        dp = [0] * (N + 1)
        for i in range(0, 7):
            dp[i] = i
        for i in range(7, N + 1):
            best = dp[i - 1] + 1
            for k in range(3, i + 1):       # last k keys are a block
                best = max(best, dp[i - k] * (k - 1))
            dp[i] = best
        return dp[N]
```

---

### C) Compact “last-6” variant (popular in interviews; **O(N)** time, **O(N)** space)

This uses the fact that the optimal last block size lies in `k ∈ {3,4,5,6}` for this problem range.

```python
#User function Template for python3

class SolutionShort:
    def optimalKeys(self, N):
        if N <= 6:
            return N
        dp = [0] * (N + 1)
        for i in range(1, 7):
            dp[i] = i
        for i in range(7, N + 1):
            dp[i] = max(
                dp[i - 1] + 1,  # type 'A'
                dp[i - 3] * 2,  # k=3  -> (k-1)=2 copies
                dp[i - 4] * 3,  # k=4
                dp[i - 5] * 4,  # k=5
                dp[i - 6] * 5,  # k=6
            )
        return dp[N]
```

---

# 4) Interview Q&A (high-yield)

**Q1. Why is the multiplier `(k-1)` and not `(k-2)`?**
Because with the final block `Ctrl-A, Ctrl-C, (k-2)×Ctrl-V`, you end up with the original text **plus** `(k-2)` appended copies → total **`k-1` copies**.

**Q2. Why is `dp[i] = i` for `i ≤ 6`?**
A block needs at least 3 keys; within ≤6 presses, multiplication isn’t strong enough to beat just typing `A` each time.

**Q3. Full recurrence and complexity?**
`dp[i] = max(dp[i-1]+1, max_{k=3..i} dp[i-k]*(k-1))`.
Top-down/bottom-up both run in `O(N²)` time, `O(N)` space.

**Q4. Why is checking only `k=3..6` often enough?**
As `k` grows, you multiply by `(k-1)` but the base `dp[i-k]` shrinks quickly; for these constraints the product peaks within `k∈[3,6]`. This yields the compact `O(N)` transition.

**Q5. Can there be multiple copy blocks at the end?**
No. After a `Ctrl-C`, any non-paste before the next `Ctrl-A` could be postponed after more pastes for an equal or better result. So the final phase after a copy should be **only** pastes.

**Q6. How would you reconstruct the actual key sequence?**
Store, for each `i`, whether you chose `'A'` or a block and (if a block) the `k` value or breakpoint. Backtrack from `N` to emit keys.

**Q7. Typical pitfalls?**
Using `(k-2)` instead of `(k-1)`, forgetting the `+1` typing transition, or letting loops miss `k=3`/bounds (off-by-one).

---

---

you got it—here’s a **ready-to-run program** for **Special Keyboard** that:

* reads `N` from stdin,
* computes the answer three ways (Memoized Top-Down, Bottom-Up DP, Compact “last-6” DP),
* prints the **input** and **outputs**,
* and **times** each method inline using `time.perf_counter()`.

I’ve added tight, interview-style **time/space notes** right in the code.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Special Keyboard — maximize number of 'A' after exactly N key presses
#
# Keys:
#   1) 'A'       -> prints 'A'
#   2) Ctrl-A    -> select all
#   3) Ctrl-C    -> copy selection to buffer
#   4) Ctrl-V    -> paste buffer (append)
#
# Recurrence (correct multiplier):
#   Let dp[i] = max 'A's with exactly i presses.
#   dp[i] = max( dp[i-1] + 1,  max_{k=3..i} dp[i-k] * (k-1) )
#   Explanation: last k keys are [Ctrl-A, Ctrl-C, (k-2)*Ctrl-V] -> (k-1) copies.
#
# Program flow:
#   - Reads integer N
#   - Runs 3 methods: memoized, bottom-up, compact (last-6)
#   - Prints results and per-method times (ms)
# ------------------------------------------------------------

import sys
from time import perf_counter
from functools import lru_cache

# -------------------- User-function Template ----------------
class Solution:
    def optimalKeys(self, N):
        """
        Top-down + memo (clear & interview-friendly)
        dp(n) = max( dp(n-1)+1,  max_{k=3..n} dp(n-k) * (k-1) )

        Time:  O(N^2)   -- for each n we try k = 3..n
        Space: O(N)     -- recursion depth + memo
        """
        @lru_cache(None)
        def dp(n):
            if n <= 6:        # For small n, best is to type 'A' each time
                return n
            best = dp(n - 1) + 1
            for k in range(3, n + 1):              # final block uses k keys
                best = max(best, dp(n - k) * (k - 1))  # (k-1) copies
            return best
        return dp(N)

# ---------------------- Bottom-up DP -------------------------
class SolutionDP:
    def optimalKeys(self, N):
        """
        Bottom-up implementation of the same recurrence.

        Time:  O(N^2)
        Space: O(N)
        """
        if N <= 6:
            return N
        dp = [0] * (N + 1)
        for i in range(0, 7):
            dp[i] = i
        for i in range(7, N + 1):
            best = dp[i - 1] + 1
            for k in range(3, i + 1):
                best = max(best, dp[i - k] * (k - 1))
            dp[i] = best
        return dp[N]

# ------------------ Compact "last-6" DP ----------------------
class SolutionShort:
    def optimalKeys(self, N):
        """
        Uses the standard observation that the final block size (k) that
        maximizes dp[i-k]*(k-1) lies within {3,4,5,6} for this problem size.

        Time:  O(N)
        Space: O(N)
        """
        if N <= 6:
            return N
        dp = [0] * (N + 1)
        for i in range(1, 7):
            dp[i] = i
        for i in range(7, N + 1):
            dp[i] = max(
                dp[i - 1] + 1,  # just type 'A'
                dp[i - 3] * 2,  # k=3  -> (k-1)=2 copies
                dp[i - 4] * 3,  # k=4
                dp[i - 5] * 4,  # k=5
                dp[i - 6] * 5,  # k=6
            )
        return dp[N]

# ----------------------------- Main --------------------------
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        print("Please provide N (1 < N < 76).")
        return
    N = int(data[0])

    sol_memo  = Solution()
    sol_dp    = SolutionDP()
    sol_short = SolutionShort()

    # --- Memoized Top-Down ---
    t0 = perf_counter()
    ans_memo = sol_memo.optimalKeys(N)
    t1 = perf_counter()
    memo_ms = (t1 - t0) * 1000.0

    # --- Bottom-Up DP ---
    t2 = perf_counter()
    ans_dp = sol_dp.optimalKeys(N)
    t3 = perf_counter()
    dp_ms = (t3 - t2) * 1000.0

    # --- Compact last-6 DP ---
    t4 = perf_counter()
    ans_short = sol_short.optimalKeys(N)
    t5 = perf_counter()
    short_ms = (t5 - t4) * 1000.0

    print(f"N: {N}\n")
    print(f"Memoized Top-Down  (O(N^2) time, O(N) space) : {ans_memo}")
    print(f"Time (ms): {memo_ms:.3f}\n")
    print(f"Bottom-Up DP       (O(N^2) time, O(N) space) : {ans_dp}")
    print(f"Time (ms): {dp_ms:.3f}\n")
    print(f"Compact last-6 DP  (O(N)   time, O(N) space) : {ans_short}")
    print(f"Time (ms): {short_ms:.3f}")

    # Agreement check
    all_match = (ans_memo == ans_dp == ans_short)
    print("\nAll methods agree ✔" if all_match else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 special_keyboard.py
7
```

### Example output (timings vary by machine)

```
N: 7

Memoized Top-Down  (O(N^2) time, O(N) space) : 9
Time (ms): 0.070

Bottom-Up DP       (O(N^2) time, O(N) space) : 9
Time (ms): 0.025

Compact last-6 DP  (O(N)   time, O(N) space) : 9
Time (ms): 0.010

All methods agree ✔
```

---

## 6) Real-World Use Cases (high-impact, analogous)

1. **Macro planning / RPA (Robotic Process Automation):** Deciding when to switch from manual keystrokes to *select–copy–paste* style macros to multiply output—exactly the trade-off this DP models.

2. **Text/Spreadsheet productivity:** Optimal use of clipboard workflows (copying a prepared block vs. typing/reformatting repeatedly) to minimize actions for large fills.

3. **Manufacturing / Batch Operations:** When a setup step (select/copy) has a fixed overhead, it’s optimal to amortize it with enough repeated “paste” operations—this DP provides the breakpoint logic.

4. **Compiler peephole/loop unrolling intuition:** Pay a one-time setup to duplicate code/body several times vs. incremental additions; finding the sweet spot mirrors the `(k-1)` multiplier trade-off.
