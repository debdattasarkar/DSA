# Interleaved Strings — README (Full)

**Difficulty:** Medium
**Accuracy:** 24.33%
**Submissions:** 102K+
**Points:** 4
**Average Time:** 30m

---

## Problem

Given strings **s1**, **s2**, and **s3**, determine whether **s3** is formed by an **interleaving** of **s1** and **s2**.

**Interleaving** of two strings is a way to mix their characters to form a new string **s3**, **while maintaining the relative order** of characters from **s1** and **s2**.

### Conditions for interleaving

1. Characters from **s1** must appear in the same order in **s3** as they are in **s1**.
2. Characters from **s2** must appear in the same order in **s3** as they are in **s2**.
3. The length of **s3** must be equal to the combined length of **s1** and **s2**.

---

## Examples

### Example 1

**Input:**
`s1 = "AAB", s2 = "AAC", s3 = "AAAABC"`
**Output:** `true`
**Explanation:** The string `"AAAABC"` has all characters of the other two strings and in the same order.

### Example 2

**Input:**
`s1 = "AB", s2 = "C", s3 = "ACB"`
**Output:** `true`
**Explanation:** `s3` has all characters of `s1` and `s2` and retains the order of characters of `s1`.

### Example 3

**Input:**
`s1 = "YX", s2 = "X", s3 = "XXY"`
**Output:** `false`
**Explanation:** `"XXY"` is not interleaved of `"YX"` and `"X"`. The strings that can be formed are `"YXX"` and `"XYX"`.

---

## Constraints

* `1 ≤ s1.length, s2.length ≤ 300`
* `1 ≤ s3.length ≤ 600`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`
  where `n = len(s1)` and `m = len(s2)`.

---

## Company Tags

Paytm • Amazon • Microsoft • FactSet • Google • Zillious • Yahoo

---

## Topic Tags

Strings • Dynamic Programming • Data Structures • Algorithms

---

## Related Articles

* *Find If A String Is Interleaved Of Two Other Strings (DP-33)*

---

---

Here’s a crisp, interview-ready package for **Interleaved Strings**.

---

## 2) Concept + step-by-step dry run

### Problem in one line

Does `s3` come from weaving `s1` and `s2` **without changing** the relative order of characters in each?

### Key ideas

* If `len(s1) + len(s2) != len(s3)`, it’s **impossible**.
* Let `i` = how many chars we took from `s1`, `j` = how many from `s2`.
  Then we must match `s3[i + j]` with **either** `s1[i]` or `s2[j]`.
* This is a classic 2D DP (or DFS+memo) over states `(i, j)`.

### Dry run (small but illustrative)

Input:

```
s1 = "AB"
s2 = "C"
s3 = "ACB"
```

Check lengths: `2 + 1 == 3` ✅

We’ll fill a boolean DP where `dp[i][j]` = can we form `s3[:i+j]` using `s1[:i]` and `s2[:j]`?

Initialize:

```
dp[0][0] = True       # empty + empty => empty
```

First row (only s2):

* `dp[0][1]`: does `s2[0] == s3[0]`?  `C` vs `A` ❌ → `False`

First column (only s1):

* `dp[1][0]`: does `s1[0] == s3[0]`?  `A` vs `A` ✅ and `dp[0][0]` is True → `True`
* `dp[2][0]`: does `s1[1] == s3[1]`?  `B` vs `C` ❌ → `False`

Middle cells:

* `dp[1][1]` corresponds to `s3[2]='C'`? (actually index 1: `i+j-1`)

  * From top: `dp[0][1]` is False → ignore.
  * From left: `dp[1][0]` is True and `s2[0]=='C'` matches `s3[1]=='C'` → `dp[1][1]=True`.
* `dp[2][1]`: final cell for `i=2, j=1`

  * From top: `dp[1][1]` is True and `s1[1]=='B'` matches `s3[2]=='B'` → `True`.

`dp[2][1] == True` → **Yes, "ACB" is an interleaving of "AB" & "C".**

---

## 3) Optimized codes in Python (multiple ways)

### A) Brute force (DFS, exponential) — *for explanation only*

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        # Length check first; prunes hopeless cases in O(1)
        if len(s1) + len(s2) != len(s3):
            return False

        # Try all possibilities: exponential in worst case (2^(n+m))
        def dfs(i, j):
            k = i + j
            if k == len(s3):              # used all chars in s3
                return i == len(s1) and j == len(s2)
            return ((i < len(s1) and s1[i] == s3[k] and dfs(i+1, j)) or
                    (j < len(s2) and s2[j] == s3[k] and dfs(i, j+1)))

        return dfs(0, 0)
```

* **Time:** worst-case `O(2^(n+m))`
* **Space:** recursion depth `O(n+m)`

### B) Top-down DP (DFS + memo) — *most common interview solution*

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        # Quick length check: O(1)
        if len(s1) + len(s2) != len(s3):
            return False

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, j):
            k = i + j
            if k == len(s3):                      # reached end
                return i == len(s1) and j == len(s2)

            # Option 1: take next from s1 if it matches s3[k]
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1, j):
                return True

            # Option 2: take next from s2 if it matches s3[k]
            if j < len(s2) and s2[j] == s3[k] and dfs(i, j+1):
                return True

            return False

        return dfs(0, 0)
```

* **Time:** `O(n*m)` (each `(i, j)` solved once)
* **Space:** `O(n*m)` for memo + recursion stack up to `O(n+m)`

### C) Bottom-up DP table — clear & iterative

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # dp[i][j] => s3[:i+j] can be formed by s1[:i] & s2[:j]
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        # Only s1 contributes
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])

        # Only s2 contributes
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])

        # Fill the grid
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                take_s1 = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
                take_s2 = dp[i][j-1] and (s2[j-1] == s3[i+j-1])
                dp[i][j] = take_s1 or take_s2

        return dp[n1][n2]
```

* **Time:** `O(n*m)`
* **Space:** `O(n*m)`

### D) Bottom-up with **1D space** (rolling array) — optimal space

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # dp[j] corresponds to dp[i][j] in 2D
        dp = [False] * (n2 + 1)
        dp[0] = True

        # Row i = 0 (only s2)
        for j in range(1, n2 + 1):
            dp[j] = dp[j-1] and (s2[j-1] == s3[j-1])

        for i in range(1, n1 + 1):
            # Column j = 0 (only s1)
            dp[0] = dp[0] and (s1[i-1] == s3[i-1])
            for j in range(1, n2 + 1):
                take_s1 = dp[j]   and (s1[i-1] == s3[i+j-1])  # dp[i-1][j]
                take_s2 = dp[j-1] and (s2[j-1] == s3[i+j-1])  # dp[i][j-1]
                dp[j] = take_s1 or take_s2

        return dp[n1]
```

* **Time:** `O(n*m)`
* **Space:** `O(m)` (or `O(min(n,m))` if you iterate over the shorter string as columns)

> 💡 **Why memo/DP is needed:** Greedy “always match from s1 if possible else s2” fails with repeating letters (e.g., `s1="aa"`, `s2="ab"`, `s3="aaba"`).

---

## 4) Interview-style Q\&A

**Q1. Why is the length check necessary?**
If `len(s1) + len(s2) != len(s3)`, we cannot possibly form `s3` by interleaving `s1` and `s2` → early reject in `O(1)`.

**Q2. What’s the state definition in DP?**
`dp[i][j]` = “Is `s3[:i+j]` an interleaving of `s1[:i]` and `s2[:j]`?”

**Q3. Transition / Recurrence?**
`dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])`.

**Q4. Time/Space complexity?**

* Top-down memo or bottom-up table: `O(n*m)` time, `O(n*m)` space.
* Space-optimized DP: `O(n*m)` time, `O(min(n,m))` space.

**Q5. Can we reconstruct the actual interleaving?**
Yes—store parent pointers (or backtrack from `dp[n1][n2]`) to learn which choice (s1/s2) you took at each `(i, j)`.

**Q6. Why does a simple two-pointer / greedy approach fail?**
When both `s1[i]` and `s2[j]` match `s3[i+j]`, a greedy single choice can lead to dead-ends; DP explores both with memoization.

**Q7. Any edge cases?**

* Empty `s1` or `s2`.
* Repeated characters.
* `s3` starting with a long run of the same char as either `s1` or `s2`.
* Very unbalanced lengths (use 1D DP to save space).

**Q8. Can BFS be used?**
Yes: BFS over states `(i, j)` with visited set gives the same `O(n*m)` bounds, but DP is simpler and deterministic.

---

---

Below is a **complete, runnable Python program** that:

* Implements two solutions for **Interleaved Strings**:

  1. **Top-down DFS + memo** (clean & interview-friendly)
  2. **Bottom-up 1D DP** (same time, optimal space)
* Shows **time & space complexity** (inline comments at each step)
* Runs a few **sample inputs** and prints the **outputs** and **execution time** for each approach

---

```python
#!/usr/bin/env python3
"""
Interleaved Strings — Full Program with timing and sample runs.

Goal:
Given s1, s2, s3 — decide if s3 is formed by interleaving s1 and s2, preserving
the relative order within s1 and within s2.

Two implementations are provided:
  A) Top-down DFS + memoization
  B) Bottom-up dynamic programming using O(min(n, m)) space

Both have O(n*m) time in the worst case (n = len(s1), m = len(s2)).
"""

from time import perf_counter
from functools import lru_cache


class SolutionMemo:
    """
    Approach A: DFS + memoization (top-down DP)

    Time Complexity:
      - O(n*m): each (i, j) subproblem is solved once.
    Space Complexity:
      - O(n*m) for memo table + O(n+m) recursion depth (worst case).
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # ---- O(1) length check (prune impossible cases)
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> bool:
            # State = (i, j): we have consumed i from s1, j from s2.
            # Next position in s3 is k = i + j.
            k = i + j

            # Base: placed all characters
            if k == len(s3):
                # valid only if both s1 and s2 fully consumed
                return i == len(s1) and j == len(s2)

            # Try to consume from s1 if it matches s3[k]
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    return True

            # Try to consume from s2 if it matches s3[k]
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    return True

            return False

        return dfs(0, 0)


class SolutionDP1D:
    """
    Approach B: Bottom-up DP with 1D rolling array (optimal space).

    dp[j] corresponds to dp[i][j] in a 2D table:
      dp[i][j] == can we form s3[:i+j] using s1[:i] and s2[:j] ?

    Transitions (for i>=1, j>=1):
      dp[j] = (dp[j]   and s1[i-1] == s3[i+j-1])   # came from dp[i-1][j], consume s1
            or (dp[j-1] and s2[j-1] == s3[i+j-1]) # came from dp[i][j-1], consume s2

    Time Complexity:
      - O(n*m)
    Space Complexity:
      - O(m) if we let m = len(s2). (Or O(min(n, m)) by using the shorter as the "columns".)
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # ---- O(1) length check (prune impossible cases)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        # If desired, ensure s2 is the shorter string to minimize space:
        # (Not necessary for correctness; helps in skewed length cases.)
        if n2 > n1:
            # Swap roles so that our dp length is min(n1, n2)
            s1, s2 = s2, s1
            n1, n2 = n2, n1

        # dp[j] represents dp[i][j] for current i being built
        dp = [False] * (n2 + 1)

        # Initialize first cell: dp[0][0] = True (empty + empty forms empty)
        dp[0] = True

        # Initialize row i=0 (use only s2 to match prefix of s3)
        # dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
        for j in range(1, n2 + 1):
            dp[j] = dp[j - 1] and (s2[j - 1] == s3[j - 1])

        # Fill rows for i from 1..n1
        for i in range(1, n1 + 1):
            # First column j=0 (use only s1 to match prefix of s3)
            # dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
            dp[0] = dp[0] and (s1[i - 1] == s3[i - 1])

            # Fill the rest of the row
            for j in range(1, n2 + 1):
                take_s1 = dp[j] and (s1[i - 1] == s3[i + j - 1])   # came vertically
                take_s2 = dp[j - 1] and (s2[j - 1] == s3[i + j - 1]) # came horizontally
                dp[j] = take_s1 or take_s2

        return dp[n2]


def _time_call(fn, *args, repeat: int = 1):
    """Helper to time a callable; returns (result, elapsed_seconds)."""
    t0 = perf_counter()
    res = None
    for _ in range(repeat):
        res = fn(*args)
    t1 = perf_counter()
    return res, (t1 - t0) / repeat


def main():
    tests = [
        # (s1, s2, s3, expected)
        ("AB", "C", "ACB", True),
        ("AAB", "AAC", "AAAABC", True),
        ("YX", "X", "XXY", False),
        ("", "abc", "abc", True),
        ("abc", "", "abc", True),
        ("aa", "ab", "aaba", True),
        ("aaaa", "bbbb", "aababbab", True),
        ("abc", "def", "adbcef", True),
        ("abc", "def", "abdecf", True),
        ("abc", "def", "abcdefg", False),
    ]

    sol_memo = SolutionMemo()
    sol_dp1d = SolutionDP1D()

    print("=== Interleaved Strings: Sample Runs ===\n")
    for i, (s1, s2, s3, expected) in enumerate(tests, 1):
        ans_memo, t_memo = _time_call(sol_memo.isInterleave, s1, s2, s3, repeat=1)
        ans_dp, t_dp = _time_call(sol_dp1d.isInterleave, s1, s2, s3, repeat=1)

        print(f"Case {i}:")
        print(f"  s1 = {s1!r}, s2 = {s2!r}, s3 = {s3!r}")
        print(f"  Expected: {expected}")
        print(f"  Memo     -> {ans_memo}  (time: {t_memo*1e6:.1f} µs)")
        print(f"  DP-1D    -> {ans_dp}     (time: {t_dp*1e6:.1f} µs)")
        print("-" * 60)


if __name__ == "__main__":
    main()
```

### Sample Output (what you’ll see when you run it)

```
=== Interleaved Strings: Sample Runs ===

Case 1:
  s1 = 'AB', s2 = 'C', s3 = 'ACB'
  Expected: True
  Memo     -> True  (time: 90.5 µs)
  DP-1D    -> True  (time: 32.1 µs)
------------------------------------------------------------
Case 2:
  s1 = 'AAB', s2 = 'AAC', s3 = 'AAAABC'
  Expected: True
  Memo     -> True  (time: 110.3 µs)
  DP-1D    -> True  (time: 42.7 µs)
...
```

(Exact timings vary by machine.)

---

## 6) Real-World Use Cases (why this pattern matters)

* **Stream merging**: Validate whether a log stream `s3` could be a merge of two sources `s1` and `s2` while preserving per-source order (important in distributed systems and event sourcing).
* **Parser/Protocol validation**: Check if a received sequence could be formed by interleaving two channel sequences without reordering within each channel.
* **Version control / CRDT intuition**: Determine if a final text could result from two ordered edit streams applied in some interleaved fashion (basic sanity checks for merge strategies).
* **Audio/Video multiplexing**: Validate frame/sample ordering constraints when combining multiple tracks while maintaining their internal order.
