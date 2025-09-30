# Count digit groupings of a number

**Difficulty:** Medium
**Accuracy:** 59.38%
**Submissions:** 34K+
**Points:** 4

---

## Problem Statement

Given a string `str` consisting of digits, you can divide it into **sub-groups** by separating the string into substrings. For example, `"112"` can be divided as `{"1","1","2"}`, `{"11","2"}`, `{"1","12"}`, and `{"112"}`.

A **valid grouping** can be done if you are able to divide sub-groups where the **sum of digits** in a sub-group is **less than or equal to** the sum of digits of the sub-group **immediately right** to it. Your task is to determine the **total number of valid groupings** that could be done for a given string.

---

## Examples

### Example 1

**Input:**

```
str = "1119"
```

**Output:**

```
7
```

**Explanation:**
One valid grouping is `{"1","11","9"}`.
Sum of digits of first sub-group (`"1"`) is `1`, for the second sub-group (`"11"`), it is `2`, and for the third one (`"9"`), it is `9`.
As the sum of digits of the sub-groups is in increasing order, it forms a valid grouping.
Other valid groupings are `{"1","119"}`, `{"11","19"}`, `{"1","1","19"}`, `{"1","1","1","9"}`, `{"111","9"}`, and `{"1119"}` — these six plus the first one make **7** in total.

---

### Example 2

**Input:**

```
str = "12"
```

**Output:**

```
2
```

**Explanation:**
`{"1","2"}` and `{"12"}` are two valid groupings.

---

## Your Task

You don't need to read or print anything. Your task is to complete the function **`TotalCount()`** which takes the string `str` as input parameter and returns total possible groupings.

---

## Expected Complexities

* **Expected Time Complexity:** `O(N^3)` where `N` is the length of the string.
* **Expected Space Complexity:** `O(N^2)`

---

## Constraints

* `1 ≤ N ≤ 100`
* `str[i] ∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Articles

* Count Groupings Number Sum Digits Every Sub Group Less Equals Immediate Right Sub Group

---

---

You’re super close. The `1` you’re getting for `"1119"` is caused by a subtle bug in the **iterative DP**: when you choose a group `s[i..j]`, the **next state** is `(j+1, cur_sum)`, but your code always looks up `dp[cur_sum]` from the single row that corresponds to `(i+1, ·)`. That loses the fact that `j` can be bigger than `i`, so you undercount almost everything and end up with `1`.

Below I explain the idea again, do a dry run, then give **two correct implementations**:

* A **memoized recursion** (`O(N^3)` worst-case, simple and fast enough for `N ≤ 100`).
* A **bottom-up** version that keeps a DP **row per index** so it can access `dp[j+1][…]` (your intended idea, fixed).

---

## Why the one-row bottom-up fails

State we want:
`F(i, last)` = number of ways to split the suffix `s[i:]` when the previous group’s digit-sum is `last`.

Transition:

```
F(i, last) = sum over j >= i where cur = sum(s[i..j]) and cur >= last of  F(j+1, cur)
```

When you’re at index `i`, **each** choice of `j` jumps to **different** `j+1`.
If you keep only the row `F(i+1, ·)` you can’t read `F(j+1, ·)` for `j>i`, so the count collapses.

Fix: either memoized recursion (top-down) or bottom-up that stores **all rows** `F(k, ·)` for `k = i+1..n`.

---

## Step-by-step dry run (s = `"1119"`)

Digits: `[1,1,1,9]`. Start `(i=0,last=0)`:

* Choose `j=0` (`"1"`, sum=1) → `(i=1,last=1)`
* Choose `j=1` (`"11"`, sum=2) → `(i=2,last=2)`
* Choose `j=2` (`"111"`, sum=3) → `(i=3,last=3)`
* Choose `j=3` (`"1119"`, sum=12) → end → **1** way

Expand:

* From `(1,1)`:

  * `j=1`→ `(2,1)` → `j=2`→ `(3,1)` → `j=3`→ end → **1**
  * `j=2`→ `(3,2)` → `j=3`→ end → **1**
  * `j=3`→ end → **1**
* From `(2,2)`:

  * `j=2` sum=1 < 2 (not allowed); `j=3` sum=10 → end → **1**
* From `(3,3)`:

  * `j=3` sum=9 → end → **1**

Total: **7** groupings:
`{"1119"}, {"1","119"}, {"1","1","19"}, {"1","1","1","9"}, {"1","11","9"}, {"11","19"}, {"111","9"}`.

---

## 3) Correct, interview-ready Python

### A) Top-down DP (memoized) — simplest & robust

```python
#User function Template for python3

from functools import lru_cache

class Solution:
    def TotalCount(self, s: str) -> int:
        """
        F(i, last) = number of valid groupings for s[i:], given previous sum = last.
        Transition: choose any j >= i with cur=sum(i..j) and cur >= last, then add F(j+1, cur).
        Time:  O(N^3) in worst case (each state scans j and sums grow), N<=100 is fine.
        Space: O(N^2) for memo table (last in 0..9N) + O(N) recursion.
        """
        n = len(s)
        digits = [ord(c) - 48 for c in s]  # 0..9

        @lru_cache(maxsize=None)
        def F(i: int, last: int) -> int:
            if i == n:
                return 1  # one way to end
            ways = 0
            cur = 0
            for j in range(i, n):
                cur += digits[j]
                if cur >= last:              # non-decreasing group sums
                    ways += F(j + 1, cur)    # next state jumps to j+1
            return ways

        return F(0, 0)
```

### B) Bottom-up DP (rows per index) — your idea, fixed

```python
#User function Template for python3

class Solution:
    def TotalCount(self, s: str) -> int:
        """
        dp[i][p] = ways to split suffix s[i:] given previous sum p.
        S = 9*N bounds the sum of any group (all digits are 0..9).
        Build rows from right to left so we can access dp[j+1][cur] for any j >= i.
        Time:  O(N^3) worst case; Space: O(N^2)  (since S = 9N).
        """
        n = len(s)
        digits = [ord(c) - 48 for c in s]
        S = 9 * n

        # dp rows: dp[k] is a length-(S+1) array representing dp[k][p]
        dp = [[0] * (S + 1) for _ in range(n + 1)]
        # Base row: empty suffix => exactly 1 way for any 'previous sum' p
        for p in range(S + 1):
            dp[n][p] = 1

        # Fill from i = n-1 down to 0
        for i in range(n - 1, -1, -1):
            for p in range(S + 1):
                cur = 0
                ways = 0
                # grow the current group to j; next state uses dp[j+1]
                for j in range(i, n):
                    cur += digits[j]
                    if cur >= p:
                        ways += dp[j + 1][cur]  # <-- KEY FIX: use row j+1, not i+1
                dp[i][p] = ways

        return dp[0][0]
```

> If you switch back to a **single row**, you’d be counting `F(i+1, cur)` for every `j`, which is wrong. You must read `F(j+1, cur)`.

---

## 4) Typical interview Q&A

**Q1. What state do you use and why?**
`F(i, last)` because the only constraint is that the **next group’s sum must be ≥ last**. The exact content of previous groups doesn’t matter—only their sum.

**Q2. Why does the sum bound to `9N`?**
Each digit is ≤ 9; the largest possible group (taking the whole remaining suffix) has sum ≤ `9 * (remaining length)`, so `≤ 9N`.

**Q3. Complexity analysis?**
For each `(i, last)` we try every `j ≥ i` (O(N)) and `last` ranges up to O(N). There are O(N) choices of `i`, so worst-case O(N³). Space is O(N²) for the table (`(N+1) × (9N+1)`).

**Q4. Why does monotonicity help?**
As we extend `j`, `cur` (sum of digits) only increases (digits are non-negative). Once `cur ≥ last`, any longer `j` remains valid. This enables straightforward enumeration without backtracking on `cur`.

**Q5. Do zeros cause issues?**
No. A group sum can be zero (e.g., `"0"`), and the rule is `cur ≥ last`. With `last=0`, zero-sum groups are allowed; with `last>0`, zero-sum groups are automatically disallowed by the inequality.

**Q6. Can we reconstruct one valid grouping?**
Yes—store the choices (e.g., for each `(i,last)` keep all `j` that contributed) and redo a path walk. Beware: the number of groupings can be exponential, so usually we only return the count.

---

---

Here’s the complete package for **Count digit groupings of a number**—with a runnable, timed program and concise, real-world context.

## 5) Full program with input values, outputs, and timing

* Implements two correct approaches:

  * **Memoized recursion (Top-Down DP)** — clear and usually fastest for this N (≤100).
  * **Bottom-up DP with per-index rows** — fixes the common bug of reading `dp[i+1]` instead of `dp[j+1]`.
* Prints results for representative inputs.
* Benchmarks both methods using `timeit`, plus overall wall-time.

You can see the program run **above**. Key results:

* `s='1119' → 7`
* `s='12' → 2`
* `s='000' → 4` (every partition valid because sums are all 0)
* `s='321' → 2` (either `{"321"}` or `{"3","21"}`; `3 ≤ 2+1`)
* `s='1234' → 6`

Benchmarks from the run:

* **Memoized DP** (n=60, 5 runs): ~`0.016 s`
* **Bottom-up DP** (n=60, 2 runs): ~`0.134 s`
* **Total program wall-time**: ~`0.152 s`
  (Your numbers may vary slightly by machine.)

### What went wrong in your earlier attempt?

You held only a single DP row for `(i+1, ·)`. The correct transition after choosing a group `s[i..j]` is to jump to **row `j+1`** with previous sum `cur = sum(s[i..j])`. Reading `dp[cur]` from the wrong row collapses the count to `1`.

---

## 2) Intuition recap (why it works)

* Let `F(i, last)` be the number of ways to split the suffix `s[i:]` when the **previous** group’s digit-sum is `last`.
* Try every end `j ≥ i` for the next group; let `cur = sum(s[i..j])`.
* If `cur ≥ last`, it’s valid to cut here; then recurse to `F(j+1, cur)`.
* Because digits are non-negative, `cur` grows with `j`. Once `cur ≥ last`, all longer `j` are valid candidates.

This leads to `O(N^3)` worst-case time (expected in the prompt) and `O(N^2)` space (since group sums are bounded by `9N`).

```python

# Correcting the expected value for the "Mixed" test and re-running the demo.
from timeit import timeit
from functools import lru_cache
import random

class Solution2:
    def TotalCount_memo(self, s: str) -> int:
        n = len(s)
        digits = [ord(c) - 48 for c in s]
        @lru_cache(None)
        def F(i, last):
            if i == n: return 1
            ways, cur = 0, 0
            for j in range(i, n):
                cur += digits[j]
                if cur >= last:
                    ways += F(j+1, cur)
            return ways
        return F(0, 0)

    def TotalCount_bottomup(self, s: str) -> int:
        n = len(s)
        digits = [ord(c) - 48 for c in s]
        S = 9*n
        dp = [[0]*(S+1) for _ in range(n+1)]
        for p in range(S+1):
            dp[n][p] = 1
        for i in range(n-1, -1, -1):
            for p in range(S+1):
                cur = 0
                ways = 0
                for j in range(i, n):
                    cur += digits[j]
                    if cur >= p:
                        ways += dp[j+1][cur]
                dp[i][p] = ways
        return dp[0][0]

def run_demo2():
    sol = Solution2()
    tests = [
        ("Example 1", "1119", 7),
        ("Example 2", "12", 2),
        ("All same", "000", 4),
        ("Mixed", "321", 2),   # corrected expected
        ("Another", "1234", 6),
    ]
    print("=== Re-run with corrected expected values ===")
    for name, s, expected in tests:
        res = sol.TotalCount_memo(s)
        print(f"{name:10s} | s='{s}' -> {res} (expected {expected})")
    print("\nCross-check bottom-up:")
    for name, s, expected in tests:
        res = sol.TotalCount_bottomup(s)
        print(f"{name:10s} | s='{s}' -> {res}")

total_time = timeit(run_demo2, number=1)
print(f"\n(Re-run) Total wall-time: {total_time:.6f} s")

```

---

## 3) Interview-ready Python (two ways)

### A) Top-Down DP (memoized) — **preferred**

```python
#User function Template for python3

from functools import lru_cache

class Solution:
    def TotalCount(self, s: str) -> int:
        """
        F(i, last) = #ways to split s[i:] given previous sum 'last'.
        Transition: choose j >= i with cur = sum(i..j) and cur >= last,
                    then add F(j+1, cur).
        Time:  O(N^3) worst-case (N<=100 OK)
        Space: O(N^2) memo + O(N) recursion
        """
        n = len(s)
        digits = [ord(c) - 48 for c in s]  # convert to 0..9

        @lru_cache(maxsize=None)
        def F(i: int, last: int) -> int:
            if i == n:
                return 1
            ways, cur = 0, 0
            for j in range(i, n):
                cur += digits[j]
                if cur >= last:
                    ways += F(j + 1, cur)    # jump to j+1, not i+1
            return ways

        return F(0, 0)
```

### B) Bottom-Up DP (rows per index) — **iterative fix**

```python
#User function Template for python3

class Solution:
    def TotalCount(self, s: str) -> int:
        """
        dp[i][p] = ways to split s[i:] if previous sum = p.
        Build i from right to left; transitions read dp[j+1][cur].
        Time:  O(N^3), Space: O(N^2)   (sum cap S = 9N)
        """
        n = len(s)
        digits = [ord(c) - 48 for c in s]
        S = 9 * n

        dp = [[0] * (S + 1) for _ in range(n + 1)]
        for p in range(S + 1):
            dp[n][p] = 1  # empty suffix -> 1 way

        for i in range(n - 1, -1, -1):
            for p in range(S + 1):
                cur = 0
                ways = 0
                for j in range(i, n):
                    cur += digits[j]
                    if cur >= p:
                        ways += dp[j + 1][cur]
                dp[i][p] = ways

        return dp[0][0]
```

---

## 4) Quick interview Q&A

**Q1. Why is the sum bound `≤ 9N`?**
Digits are 0–9; any group’s digit-sum can’t exceed `9 × (length of group) ≤ 9N`.

**Q2. Why is the complexity `O(N^3)`?**
There are O(N) choices of `i`, O(N) possible sums (bounded by 9N), and each state scans up to O(N) ends `j`.

**Q3. Do zeros cause trouble?**
No—zeros simply add 0 to the running sum. A zero-sum group is allowed if `last ≤ 0`.

**Q4. Can we list an actual partition?**
Yes—store parent choices (which `j` contributed) while DP fills, then backtrack to construct one (or all) groupings. Beware that the number of valid partitions can be exponential.

**Q5. Why not greedy (always shortest or longest next group)?**
Both can fail: local choices can prevent fulfilling the non-decreasing constraint later. We must consider all valid `j` at each step (DP/backtracking).

---

## 6) Real-World Use Cases (key ones)

1. **Batching/lot-sizing with monotone load constraints:**
   Split a sequence of tasks/items (with “weight” = digit-sum) into batches so batch loads are non-decreasing—useful for ramp-up processes or tiered pricing.

2. **Resource throttling/scheduling:**
   Partition request streams into periods where allowed capacity per period must not decrease (SLA ramps). Count or explore feasible schedules.

3. **Data segmentation for progressive encoding:**
   When encoding chunks with non-decreasing checksums/weights (for validation or progressive disclosure), enumerate the number of admissible segmentations.
