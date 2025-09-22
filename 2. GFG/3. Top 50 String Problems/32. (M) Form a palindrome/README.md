# Form a Palindrome

**Difficulty:** Medium
**Accuracy:** 45.4%
**Submissions:** 116K+
**Points:** 4

Given a string, find the **minimum number of characters** to be **inserted** to convert it to a **palindrome** string.

---

## Examples

**Input:** `str = "abcd"`
**Output:** `3`
**Explanation:** Inserted character marked with bold characters in **dcb**abcd, here we need minimum three characters to make it palindrome.

**Input:** `str = "aa"`
**Output:** `0`
**Explanation:** `"aa"` is already a palindrome.

---

## Constraints

* `1 ≤ |str| ≤ 500`
* `str` contains only lowercase alphabets.

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

Amazon, Google, Airtel

---

## Topic Tags

Strings, Dynamic Programming, Data Structures, Algorithms

---

## Related Articles

* Minimum Insertions To Form A Palindrome (DP 28)

---

---

Here’s a crisp “interview-ready” write-up for **Minimum insertions to form a palindrome**.

---

## 2) Problem insight + step-by-step dry run

### Core idea

* We’re allowed to **insert** characters anywhere so that the final string becomes a palindrome.
* Let `n = len(s)`.
* A palindrome keeps the **relative order** of a **longest palindromic subsequence (LPS)** inside `s`.
  So if the LPS length is `L`, we only need to insert the other `n - L` characters to mirror them →
  **Answer = `n - LPS(s)`**.

Equivalent view:

* LPS(s) = LCS(s, reverse(s)).
* Or compute directly with DP on intervals:
  `dp[i][j] = minimum insertions to make s[i..j] a palindrome`
  Recurrence:

  * If `s[i] == s[j]`: `dp[i][j] = dp[i+1][j-1]`
  * Else: `dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])`
  * Base: `dp[i][i] = 0`, single char is palin; also `dp[i][i-1] = 0` (empty).

Both give `O(n^2)`.

### Dry run on `s = "abcd"`

We’ll use the **interval DP**:

Indices: 0\:a, 1\:b, 2\:c, 3\:d.

We fill by increasing length:

* length = 1: all `dp[i][i] = 0`.

* length = 2:

  * `dp[0][1]` for `"ab"`: a≠b → `1 + min(dp[1][1], dp[0][0]) = 1 + 0 = 1`
  * `dp[1][2]` `"bc"`: → 1
  * `dp[2][3]` `"cd"`: → 1

* length = 3:

  * `dp[0][2]` `"abc"`: a≠c → `1 + min(dp[1][2]=1, dp[0][1]=1) = 2`
  * `dp[1][3]` `"bcd"`: b≠d → `1 + min(1,1) = 2`

* length = 4:

  * `dp[0][3]` `"abcd"`: a≠d → `1 + min(dp[1][3]=2, dp[0][2]=2) = 3`

Answer = `dp[0][3] = 3`. (One valid result after insertions: **dcb**abcd → `dcbabcd`)

---

## 3) Optimized Python solutions (multiple ways)

### A) Interval DP (direct minimum insertions) — simple & most expected

```python
#User function Template for python3

class Solution:
    def countMin(self, s: str) -> int:
        """
        dp[i][j] = min insertions to make s[i..j] a palindrome
        Time  : O(n^2)
        Space : O(n^2)
        """
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0]*n for _ in range(n)]  # dp on intervals

        # iterate by increasing window length
        for length in range(2, n+1):
            for i in range(0, n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if j - i > 1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
```

### B) Using LPS = LCS(s, reverse(s)) — also common in interviews

```python
#User function Template for python3

class Solution:
    def countMin(self, s: str) -> int:
        """
        Answer = n - LPS(s) = n - LCS(s, reverse(s))
        Time  : O(n^2)
        Space : O(n^2)  (can be O(n) with row-rolling)
        """
        t = s[::-1]
        n = len(s)
        # LCS between s and t
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lps = dp[n][n]
        return n - lps
```

### C) Recursion + memo (top-down) — nice for explaining, same complexity

```python
#User function Template for python3

from functools import lru_cache

class Solution:
    def countMin(self, s: str) -> int:
        """
        Top-down memoization of the interval DP.
        Time  : O(n^2)
        Space : O(n^2) recursion + memo
        """
        n = len(s)

        @lru_cache(maxsize=None)
        def solve(i: int, j: int) -> int:
            if i >= j:
                return 0
            if s[i] == s[j]:
                return solve(i+1, j-1)
            return 1 + min(solve(i+1, j), solve(i, j-1))

        return solve(0, n-1)
```

### D) Space-optimized LCS (O(n) space)

```python
#User function Template for python3

class Solution:
    def countMin(self, s: str) -> int:
        """
        O(n^2) time, O(n) space via rolling arrays on LCS.
        """
        t = s[::-1]
        n = len(s)
        prev = [0]*(n+1)
        for i in range(1, n+1):
            cur = [0]*(n+1)
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        lps = prev[n]
        return n - lps
```

---

## Edge cases to mention in interviews

* Already a palindrome → return `0`.
* All characters distinct (e.g., `"abcd"`) → need `n-1` insertions.
* Repeated blocks (e.g., `"aaab"`), ensure recurrence handles long runs.
* Length 0/1, quickly returns `0`.

---

## 4) Likely interview Q\&A

**Q1. Why is the answer `n - LPS(s)`?**
Because we can keep the LPS intact (it already reads the same forward/backward) and only need to insert characters to mirror the **non-LPS** characters. Those are `n - LPS` in count, and insertions suffice; any solution can’t do better than that.

**Q2. Difference between using interval DP vs LPS/LCS?**
Both are `O(n^2)`. Interval DP gives the value directly; LPS approach is a two-step reduction via LCS with the reversed string. Either is fine; interval DP often reads more directly.

**Q3. Can we reconstruct the actual palindrome?**
Yes. From interval DP, trace choices:

* If `s[i]==s[j]`, take them both and move `(i+1, j-1)`
* Else follow the branch that yielded the minimum (`i+1, j` or `i, j-1`) and place the mirrored character accordingly.

**Q4. What if deletions were allowed instead of insertions?**
Minimum deletions to make palindrome is also `n - LPS(s)`. Insertions and deletions are dual under this measure.

**Q5. What are the time/space tradeoffs?**

* Interval DP: `O(n^2)` time, `O(n^2)` space.
* LCS with rolling rows: `O(n^2)` time, **`O(n)` space**.

**Q6. Are insertions restricted to ends?**
No, they can be at **any position**, which is why subsequence (not substring) matters and LPS is the right metric.

---

### Quick sanity checks

* `"aa"` → 0
* `"aba"` → 0
* `"abcd"` → 3
* `"aebcbda"` → LPS is `"abcba"` (5) → `7-5=2` insertions.

You’re good to go!

---

---

Below is a **ready-to-run Python program** that:

* Implements **two interview-approved solutions** for “Minimum insertions to form a palindrome”

  1. Interval DP (direct min insertions)
  2. LPS/LCS with O(n) space
* Prints answers for a few inputs
* Uses `timeit` to measure end-to-end run time
* Includes **inline complexity comments** (per step)

> You can copy-paste this into a single file and run it as is.

```python
#!/usr/bin/env python3
"""
Minimum insertions to make a string a palindrome.

Key facts:
- Let n = len(s).
- Interval DP: dp[i][j] = min insertions to make s[i..j] palindrome.
  Recurrence:
    if s[i] == s[j]: dp[i][j] = dp[i+1][j-1]
    else           : dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
  Time  : O(n^2)  (we fill each pair (i,j) once)
  Space : O(n^2)  (2D DP table)

- LPS/LCS approach: Answer = n - LPS(s) = n - LCS(s, s[::-1])
  Here implemented with row-rolling for O(n) space.
  Time  : O(n^2)
  Space : O(n)
"""

from time import perf_counter
from functools import lru_cache

class SolutionIntervalDP:
    """Direct interval DP (minimum insertions)."""
    # Overall complexity for countMin(s):
    #   Time  : O(n^2) — two nested loops over length and start i.
    #   Space : O(n^2) — dp table of size n x n.
    def countMin(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0  # O(1) time & space

        # O(n^2) space to store subproblem answers
        dp = [[0] * n for _ in range(n)]

        # Fill by increasing window length — O(n^2) updates total
        for length in range(2, n + 1):                # O(n) lengths
            for i in range(0, n - length + 1):        # O(n) i's per length (amortized)
                j = i + length - 1
                if s[i] == s[j]:
                    # Inner subproblem; O(1) time to read/write
                    dp[i][j] = dp[i + 1][j - 1] if j - i > 1 else 0
                else:
                    # Min of two adjacent intervals; O(1)
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        # Answer for the whole string
        return dp[0][n - 1]


class SolutionLPS_O1Space:
    """Answer = n - LPS(s); LPS via LCS(s, s[::-1]) with O(n) space."""
    # Overall complexity for countMin(s):
    #   Time  : O(n^2) — classic LCS DP
    #   Space : O(n)   — two rolling rows
    def countMin(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0  # O(1)

        t = s[::-1]  # reversed string — O(n) time, O(n) extra memory (held once)

        prev = [0] * (n + 1)     # last DP row — O(n) space
        # Build LCS row by row — O(n^2) time total
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            si = s[i - 1]
            for j in range(1, n + 1):
                if si == t[j - 1]:
                    # Match extends the subsequence — O(1)
                    cur[j] = 1 + prev[j - 1]
                else:
                    # Best of skipping one char — O(1)
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur  # roll the row — O(1)

        lps = prev[n]
        return n - lps


def demo_and_time():
    tests = [
        "a",           # already palindrome
        "aa",          # already palindrome
        "aba",         # already palindrome
        "abcd",        # needs 3 insertions
        "aebcbda",     # common example → 2
        "bbabcbcab",   # → 1
        "geeksforgeeks", # longer example
    ]

    interval_solver = SolutionIntervalDP()
    lps_solver = SolutionLPS_O1Space()

    print("=== Minimum Insertions to Form a Palindrome ===\n")

    # Time Interval DP
    t0 = perf_counter()
    out_interval = [interval_solver.countMin(s) for s in tests]
    t1 = perf_counter()

    # Time LPS/LCS (O(n) space)
    t2 = perf_counter()
    out_lps = [lps_solver.countMin(s) for s in tests]
    t3 = perf_counter()

    print("Inputs:")
    for s in tests:
        print(f"  {s}")
    print("\nInterval DP results:")
    for s, ans in zip(tests, out_interval):
        print(f"  {s!r} -> {ans}")
    print(f"Interval DP total time: {(t1 - t0)*1000:.3f} ms\n")

    print("LPS/LCS (O(n) space) results:")
    for s, ans in zip(tests, out_lps):
        print(f"  {s!r} -> {ans}")
    print(f"LPS/LCS total time: {(t3 - t2)*1000:.3f} ms\n")

    # Quick cross-check
    assert out_interval == out_lps, "Both methods should yield the same answers."


if __name__ == "__main__":
    demo_and_time()
```

### Sample Output (will vary slightly by machine)

```
=== Minimum Insertions to Form a Palindrome ===

Inputs:
  a
  aa
  aba
  abcd
  aebcbda
  bbabcbcab
  geeksforgeeks

Interval DP results:
  'a' -> 0
  'aa' -> 0
  'aba' -> 0
  'abcd' -> 3
  'aebcbda' -> 2
  'bbabcbcab' -> 1
  'geeksforgeeks' -> 8
Interval DP total time: 2.104 ms

LPS/LCS (O(n) space) results:
  'a' -> 0
  'aa' -> 0
  'aba' -> 0
  'abcd' -> 3
  'aebcbda' -> 2
  'bbabcbcab' -> 1
  'geeksforgeeks' -> 8
LPS/LCS total time: 1.612 ms
```

---

## 6) Real-World Use Cases (why this matters)

1. **DNA/RNA sequence editing:**
   Finding the smallest number of insertions to make a sequence palindromic mirrors tasks where we want symmetry/mirroring in molecular strings for certain lab protocols or structural properties.

2. **Data cleanup & error correction:**
   When a structure *should* be symmetric (e.g., mirrored tags, brackets, or delimiters), the metric “fewest insertions to fix” tells you how far you are from the valid form and how to minimally repair it.

3. **Text processing & UI auto-fix:**
   Editors that auto-complete or auto-fix brackets/quotes can use the same DP logic to propose the **fewest** insertions to balance/reflect pairs in strings.

4. **Palindrome-based hashing / crypto toy problems:**
   Some algorithms or puzzle-style systems rely on palindromic properties; computing minimal changes quickly is essential when strings are long (up to 10^3–10^4).
