# Longest Common Subsequence

**Difficulty:** Medium
**Accuracy:** 41.68%
**Submissions:** 320K+
**Points:** 4

---

## Problem Statement

Given two strings `s1` and `s2`, return the length of their **longest common subsequence (LCS)**. If there is no common subsequence, return `0`.

A subsequence is a sequence that can be derived from the given string by deleting some or no elements **without changing the order** of the remaining elements. For example, `"ABE"` is a subsequence of `"ABCDE"`.

---

## Examples

### Example 1

**Input:** `s1 = "ABCDGH", s2 = "AEDFHR"`
**Output:** `3`
**Explanation:** The longest common subsequence of `"ABCDGH"` and `"AEDFHR"` is `"ADH"`, which has a length of `3`.

---

### Example 2

**Input:** `s1 = "ABC", s2 = "AC"`
**Output:** `2`
**Explanation:** The longest common subsequence of `"ABC"` and `"AC"` is `"AC"`, which has a length of `2`.

---

### Example 3

**Input:** `s1 = "XYZW", s2 = "XYWZ"`
**Output:** `3`
**Explanation:** The longest common subsequences of `"XYZW"` and `"XYWZ"` are `"XYZ"` and `"XYW"`, both of length `3`.

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 10^3`
* Both strings `s1` and `s2` contain **only uppercase English letters**.

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Paytm
* VMWare
* Amazon
* Microsoft
* Citrix
* MakeMyTrip

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Interview Experiences

* Vmware Interview Experience Set 8 Campus Mts Propel Program
* Makemytrip Interview Experience Set 7 On Campus

---

## Related Articles

* Longest Common Subsequence Dp 4
* Space Optimized Solution Lcs

---

---

Here’s an interview-ready guide for **Longest Common Subsequence (LCS)**.

---

## 2) Intuition + step-by-step dry run

We need the **length of the LCS** of two strings `s1` and `s2`.
Classic DP idea:

Let `dp[i][j]` = LCS length of prefixes `s1[:i]` and `s2[:j]`.

Recurrence:

* If `s1[i-1] == s2[j-1]` → `dp[i][j] = 1 + dp[i-1][j-1]`
* Else → `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

Base row/col with empty string are zeros.

### Dry run (small but complete): `s1 = "ABC"`, `s2 = "AC"`

We tabulate with a leading empty row/col:

```
        j→   0  1  2
             ''  A  C
i  ''   0 |  0  0  0
↓  A    1 |  0  1  1
   B    2 |  0  1  1
   C    3 |  0  1  2
```

Fill order (row by row):

* i=1 ('A'), j=1 ('A') → match → 1 + dp\[0]\[0] = 1
* i=1, j=2 ('C') → no match → max(dp\[0]\[2], dp\[1]\[1]) = 1
* i=2 ('B'), j=1 → no match → max(1,0)=1
* i=2, j=2 → no match → max(1,1)=1
* i=3 ('C'), j=1 → no match → max(1,0)=1
* i=3, j=2 ('C') → match → 1 + dp\[2]\[1] = 2

Answer `dp[3][2] = 2` (LCS is `"AC"`).

> For the larger example `("ABCDGH","AEDFHR")` the same rules yield 3 (`"ADH"`).

---

## 3) Python solutions (brute → optimized), interview-style

```python
# ------------------------------------------------------------
# Expected interface
# ------------------------------------------------------------
class Solution:
    def lcs(self, s1, s2):
        """
        Space-optimized bottom-up DP.
        Time:  O(n*m)
        Space: O(min(n, m))    # because we keep only previous and current rows
        """
        n, m = len(s1), len(s2)
        if n == 0 or m == 0:
            return 0

        # Always make 'b' the shorter string to minimize memory
        a, b = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
        na, nb = len(a), len(b)

        prev = [0] * (nb + 1)            # dp for previous row  -> O(min(n,m)) space
        for i in range(1, na + 1):       # O(n)
            curr = [0] * (nb + 1)
            ai = a[i - 1]
            for j in range(1, nb + 1):   # O(m)
                if ai == b[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[nb]
```

### Alternative 1: Full DP table (easiest to explain)

```python
class SolutionFullTable:
    def lcs(self, s1, s2):
        """
        Bottom-up DP with full table.
        Time:  O(n*m)
        Space: O(n*m)
        """
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
```

### Alternative 2: Top-down recursion + memoization

```python
class SolutionMemo:
    def lcs(self, s1, s2):
        """
        Top-down with memo to avoid exponential blowup.
        Time:  O(n*m) states
        Space: O(n*m) for memo + recursion stack O(n+m)
        """
        from functools import lru_cache
        n, m = len(s1), len(s2)

        @lru_cache(maxsize=None)
        def solve(i, j):  # LCS of s1[i:], s2[j:]
            if i == n or j == m:
                return 0
            if s1[i] == s2[j]:
                return 1 + solve(i+1, j+1)
            return max(solve(i+1, j), solve(i, j+1))

        return solve(0, 0)
```

### (Educational) Brute force recursion (exponential)

```python
class SolutionBrute:
    def lcs(self, s1, s2):
        """
        Exponential: explores both skip-branches at each step.
        Time:  O(2^(n+m)) in worst case. Use only for teaching.
        """
        def rec(i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + rec(i+1, j+1)
            return max(rec(i+1, j), rec(i, j+1))
        return rec(0, 0)
```

> If they ask to **reconstruct the LCS string**, use the full table and walk backwards:
>
> * If `s1[i-1]==s2[j-1]`, put that char into the answer and move `(i-1, j-1)`.
> * Else move to the neighbor with larger `dp` value.

---

## 4) Likely interviewer Q\&A

**Q1. Why does the DP recurrence work?**
Because the last char of the optimal solution either:

* **matches** (`s1[i-1]==s2[j-1]`), contributing `1 + LCS(s1[:i-1], s2[:j-1])`, or
* **doesn’t match**, so the LCS is the best of skipping one char:
  `max(LCS(s1[:i-1], s2[:j]), LCS(s1[:i], s2[:j-1]))`.

**Q2. Time/space complexities?**

* Standard DP: `O(n*m)` time, `O(n*m)` space.
* **Space optimized** DP: `O(n*m)` time, **`O(min(n,m))`** space (keep only two rows).

**Q3. How do you get the **actual LCS string**?**
Keep the full `dp` table, then backtrack from `(n, m)` as described above. (Space `O(n*m)`, time `O(n+m)` to reconstruct.)

**Q4. Difference between **LCS** and **Longest Common Substring**?**

* LCS allows **skips**; substring requires **contiguity**.
* Longest Common Substring uses a different DP (`dp[i][j]=dp[i-1][j-1]+1` if chars match else `0`) and tracks a **maximum**; LCS uses the **max of neighbors** on mismatch.

**Q5. Can we lower time below `O(n*m)`?**
Not in general for arbitrary strings over large alphabets; `Θ(n*m)` is essentially tight. For special cases (e.g., small alphabet + bitset trick) you can get good constants.

**Q6. Common pitfalls?**

* Off-by-one when indexing prefixes (`i-1`, `j-1`).
* Forgetting to ensure `bisect_left` style tie-breaking—(not relevant to LCS, but to LIS).
* Mixing up LCS with substring logic (resetting to zero on mismatch is **substring**, not subsequence).

---

---

All set! I’ve run a **full inline Python program** for LCS that:

* Implements three approaches:

  * **Space-optimized bottom-up DP** (`O(n*m)` time, `O(min(n,m))` space) — used by `Solution.lcs`.
  * **Full table DP** (`O(n*m)` time/space) for clarity and reconstruction scenarios.
  * **Top-down memoized recursion** (also `O(n*m)` time; `O(n*m)` memo + stack).
* Prints outputs for the sample inputs and compares methods.
* Benchmarks both DP variants on random uppercase strings of length **1000** each.
* Prints the **TOTAL MAIN RUNTIME** using `timeit.default_timer()`.


```python

# Re-run so outputs are visible
from functools import lru_cache
from typing import List, Tuple
import random, string, timeit, sys

sys.setrecursionlimit(10000)

class Solution:
    def lcs(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n == 0 or m == 0:
            return 0
        a, b = (s1, s2) if len(s2) <= len(s1) else (s2, s1)
        na, nb = len(a), len(b)
        prev = [0] * (nb + 1)
        for i in range(1, na + 1):
            curr = [0] * (nb + 1)
            ai = a[i - 1]
            for j in range(1, nb + 1):
                if ai == b[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[nb]

    def lcs_full_table(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

    def lcs_memo(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @lru_cache(maxsize=None)
        def solve(i: int, j: int) -> int:
            if i == n or j == m:
                return 0
            if s1[i] == s2[j]:
                return 1 + solve(i+1, j+1)
            return max(solve(i+1, j), solve(i, j+1))
        return solve(0, 0)

def main():
    sol = Solution()
    print("=== Longest Common Subsequence — Demo & Timing ===")
    tests = [
        ("ABCDGH", "AEDFHR", 3),
        ("ABC", "AC", 2),
        ("XYZW", "XYWZ", 3),
    ]
    for s1, s2, exp in tests:
        ans = sol.lcs(s1, s2)
        print(f"\nInput: s1='{s1}', s2='{s2}'")
        print("LCS length (space-optimized DP):", ans, "| expected:", exp)

    s1 = "ABCBDAB"
    s2 = "BDCABA"
    print(f"\nCompare on s1='{s1}', s2='{s2}'")
    print("  lcs()             :", sol.lcs(s1, s2))
    print("  lcs_full_table()  :", sol.lcs_full_table(s1, s2))
    print("  lcs_memo()        :", sol.lcs_memo(s1, s2))

    n, m = 1000, 1000
    rng = random.Random(7)
    letters = string.ascii_uppercase
    s1_big = "".join(rng.choice(letters) for _ in range(n))
    s2_big = "".join(rng.choice(letters) for _ in range(m))

    t0 = timeit.default_timer()
    ans_opt = sol.lcs(s1_big, s2_big)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    ans_full = sol.lcs_full_table(s1_big, s2_big)
    t3 = timeit.default_timer()

    print("\nTiming on random strings of length 1000 each:")
    print(f"  Space-optimized DP: length={ans_opt}, time={(t1 - t0):.3f}s")
    print(f"  Full-table DP     : length={ans_full}, time={(t3 - t2):.3f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.3f} seconds")


```

---

## 6) Real-World Use Cases (essential ones)

* **Diff / Version control** (git, svn): LCS underlies computing the minimal set of insert/delete edits to transform one file into another.
* **DNA / protein sequence analysis:** Find similarity between biological sequences where insertions/deletions are common.
* **Plagiarism / document similarity:** Measure structural overlap between texts while allowing gaps (unlike contiguous substring).
* **Error-tolerant matching / spell checking:** Align strings by edits; LCS is a building block for edit distance and alignment scoring.
* **Data synchronization:** Identify common subsequences to minimize data transmitted as deltas between devices.
