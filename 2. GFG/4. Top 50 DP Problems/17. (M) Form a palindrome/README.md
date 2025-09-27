# Form a palindrome

**Difficulty:** Medium
**Accuracy:** 54.84%
**Submissions:** 26K+
**Points:** 4

---

Given a string `s`, the task is to find the **minimum number of characters** to be inserted to convert it to a **palindrome**.

**Note:** A palindrome is a string that reads the same backward as forward; for example, strings `"aba"`, `"abccba"` are palindromes.

---

## Examples

### Example 1

**Input:** `s = "abcd"`
**Output:** `3`
**Explanation:** Here we can append 3 characters in the beginning and the resultant string will be a palindrome `"dcbabcd"`.

### Example 2

**Input:** `s = "aba"`
**Output:** `0`
**Explanation:** Given string is already a palindrome hence no insertions are required.

---

## Constraints

* `1 ≤ s.size() ≤ 500`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Amazon • Microsoft • Google • Airtel

---

## Topic Tags

Strings • Dynamic Programming • Data Structures • Algorithms

---

## Related Articles

* Minimum Insertions To Form A Palindrome Dp 28

---

---

# Form a Palindrome — Explanation + Dry Run + Python Solutions

## 2) Intuition & Step-by-Step Dry Run

**Problem recap.**
Given a string `s`, insert characters *anywhere* so that the final string is a palindrome, using the **minimum** number of insertions. Return that minimum count.

### Two classic views

1. **Substring DP (direct).**
   Let `dp[i][j]` be the minimum insertions to make `s[i..j]` a palindrome.

* If `i >= j` (empty or single char) → `dp[i][j] = 0`.
* If `s[i] == s[j]` → ends already match → `dp[i][j] = dp[i+1][j-1]`.
* Else we must insert near `i` or near `j` →
  `dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])`.

Compute by increasing window length (`gap`), answer is `dp[0][n-1]`.
**Time:** `O(n^2)`; **Space:** `O(n^2)` (can be reduced but this is the clearest).

2. **LPS/LCS view (very interview-popular).**
   Minimum insertions = `n - LPS(s)`, where **LPS** is the length of the **Longest Palindromic Subsequence**.
   And `LPS(s) = LCS(s, reverse(s))` (longest common subsequence between the string and its reverse).
   We can compute LCS in `O(n^2)` time and **`O(n)` space** using rolling arrays.

---

### Dry run (Substring DP) for `s = "abcd"`

`n = 4`, indices `0..3`. We fill `dp` by increasing length.

* Length 1 (gap 0): `dp[i][i] = 0` for all `i`.
* Length 2 (gap 1):

  * `i=0,j=1` (“ab”): `a != b` → `dp=1 + min(dp[1][1],dp[0][0]) = 1 + 0 = 1`
  * `i=1,j=2` (“bc”): `b != c` → `1`
  * `i=2,j=3` (“cd”): `c != d` → `1`
* Length 3 (gap 2):

  * `i=0,j=2` (“abc”): `a != c` → `1 + min(dp[1][2]=1, dp[0][1]=1) = 2`
  * `i=1,j=3` (“bcd”): `b != d` → `1 + min(dp[2][3]=1, dp[1][2]=1) = 2`
* Length 4 (gap 3):

  * `i=0,j=3` (“abcd”): `a != d` → `1 + min(dp[1][3]=2, dp[0][2]=2) = 3`

Answer `dp[0][3] = 3`. Example construction: insert “dcb” at the front → `"dcbabcd"`.

Quick sanity: `s="aba"`

* Ends match throughout, so `dp[0][2] = 0`. No insertions needed.

---

## 3) Python solutions (with interview-style inline comments)

All versions return the **minimum insertions**. Pick whichever interface your interviewer prefers. The most common “clean” answer is the **LCS with rolling rows**.

### A) Naïve recursion (for understanding) — Exponential time

```python
class Solution:
    def findMinInsertions(self, s: str) -> int:
        # Pure recursion; not for production — O(2^n) in worst case.
        # Shows the underlying recurrence clearly.

        def solve(i: int, j: int) -> int:
            if i >= j:                     # empty or single char
                return 0
            if s[i] == s[j]:               # ends already match
                return solve(i + 1, j - 1)
            # insert near i or near j (one insertion + best of the two options)
            return 1 + min(solve(i + 1, j), solve(i, j - 1))

        return solve(0, len(s) - 1)
```

---

### B) Top-down DP (memoized recursion) — `O(n^2)` time, `O(n^2)` space

```python
from functools import lru_cache

class Solution:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def solve(i: int, j: int) -> int:
            # States: O(n^2)
            if i >= j:
                return 0
            if s[i] == s[j]:
                return solve(i + 1, j - 1)         # reuse overlapping subproblems
            return 1 + min(solve(i + 1, j), solve(i, j - 1))

        # Time: O(n^2) unique (i,j) pairs; each computed once.
        # Space: O(n^2) for cache + recursion stack O(n).
        return solve(0, n - 1)
```

---

### C) Bottom-up Substring DP — `O(n^2)` time, `O(n^2)` space

```python
class Solution:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        # dp[i][j] = min insertions to make s[i..j] a palindrome
        dp = [[0] * n for _ in range(n)]  # Space: O(n^2)

        # Build by increasing window length (gap)
        for gap in range(1, n):           # Time: O(n^2)
            for i in range(0, n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
```

---

### D) LPS via LCS(s, reverse(s)) — `O(n^2)` time, **`O(n)` space** (recommended)

```python
class Solution:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]                   # reversed string
        # Compute LCS(s, t) with rolling arrays (2 rows)
        prev = [0] * (n + 1)          # Space: O(n)
        # Time: O(n^2)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        lps = prev[n]
        return n - lps                # min insertions = n - LPS
```

**Why this works:** a palindrome reads the same forwards/backwards, so any palindromic subsequence of `s` appears as a common subsequence in `s` and `reverse(s)`. Keeping the **longest** such subsequence minimizes how many characters we still need to insert to “mirror” the rest.

---

## 4) Interview-style Q&A

**Q1. What’s the recurrence for the direct DP?**
**A.**

* `dp[i][j] = 0` if `i >= j`.
* If `s[i] == s[j]` → `dp[i][j] = dp[i+1][j-1]`.
* Else → `dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])`.

**Q2. Why does `n - LPS(s)` equal the minimum insertions?**
**A.** The LPS is the largest part that’s already palindromic. To make the entire string a palindrome, you only need to insert mirror characters for the **non-LPS** positions. Thus minimum insertions is exactly how many characters are **outside** the LPS, i.e., `n - LPS`.

**Q3. Why is `LPS(s) = LCS(s, reverse(s))`?**
**A.** Any palindromic subsequence reads the same forwards/backwards, so it appears unchanged in `reverse(s)`. Conversely, any common subsequence of `s` and `reverse(s)` reads identically in both directions, so it is palindromic.

**Q4. Time/space complexities?**
**A.**

* Direct DP (bottom-up or memoized): `O(n^2)` time, `O(n^2)` space.
* LCS with rolling arrays: `O(n^2)` time, **`O(n)`** space.

**Q5. Can we reconstruct an actual palindrome, not just the count?**
**A.** Yes. Either keep parent pointers in the `dp[i][j]` table (direct DP) or reconstruct the LCS string and then mirror around it to build one valid palindrome.

**Q6. Are insertions restricted to the beginning or end?**
**A.** No, insertions can be anywhere. The DP already accounts for the optimal positions (possibly both ends many times).

**Q7. How does this relate to “minimum deletions to make a palindrome”?**
**A.** They share the same answer: `n - LPS(s)`. Insertions in one direction correspond to deletions in the other.

**Q8. Edge cases?**
**A.** Empty string or single character → `0`. Already palindrome → `0`. Strings with all identical characters → `0`. Size bound here is small (`≤500`), so `O(n^2)` is easily fine.

**Q9. Why LCS vs direct DP?**
**A.** Both are `O(n^2)`, but LCS with rolling rows gives **`O(n)` space** and is often faster in practice due to good cache locality and simple transitions.

**Q10. How would you optimize memory for the direct DP?**
**A.** You can reduce to `O(n)` by computing diagonals with careful overwriting, but it’s trickier to implement correctly. LCS rolling arrays are simpler and safer for `O(n)` memory.

---

---

All set! The notebook above ran a **full program** that:

* Implements two interview-grade solutions

  * **Substring DP** (`O(n^2)` time, `O(n^2)` space)
  * **LPS via LCS (rolling rows)** (`O(n^2)` time, **`O(n)` space**)
* Prints **inputs, outputs, expected answers**, and **best timings** using `timeit`.
* Contains **inline comments** calling out time/space for each key step.

```python

# Re-run after kernel reset: include all code again and execute.
from typing import List
import timeit

class SolutionSubstringDP:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        dp = [[0]*n for _ in range(n)]
        for gap in range(1, n):
            for i in range(0, n - gap):
                j = i + gap
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if j - i > 1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

class SolutionLCSRolling:
    def findMinInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        t = s[::-1]
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        lps = prev[n]
        return n - lps

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"s": "abcd", "expected": 3},
    {"s": "aba", "expected": 0},
    {"s": "race", "expected": 3},
    {"s": "a", "expected": 0},
    {"s": "aaab", "expected": 1},
    {"s": "leetcode", "expected": 5},
]

def run_and_report():
    print("=== Form a Palindrome — Full Program ===\n")
    subdp = SolutionSubstringDP()
    lcsro = SolutionLCSRolling()

    for idx, t in enumerate(tests, 1):
        s, exp = t["s"], t["expected"]
        print(f"Test #{idx}: s='{s}' (n={len(s)})")
        res1, t1 = time_call(lambda x: subdp.findMinInsertions(x), s)
        print(f"  Substring-DP: result={res1}, expected={exp}, best={t1:.6f}s")
        res2, t2 = time_call(lambda x: lcsro.findMinInsertions(x), s)
        print(f"  LCS-Rolling : result={res2}, expected={exp}, best={t2:.6f}s\n")

run_and_report()


```

---

## Real-World Use Cases (just the heavy hitters)

1. **DNA/RNA sequence correction & palindromic motifs**
   Many biological analyses look for palindromic structures (e.g., restriction sites). Minimizing insertions to form a palindrome can model the least number of edits to restore or engineer symmetric motifs.

2. **Error correction in mirrored data formats**
   Some storage/encoding schemes use symmetric (palindromic) headers/footers for robustness. Computing minimal insertions helps determine the smallest repair to regain the expected symmetry after corruption.

3. **Text normalization for reversible parsing**
   When building reversible parsers or bidirectional protocols, palindromic or symmetric delimiters simplify checks. Finding minimal edits provides the smallest change to make a token stream symmetric and thus valid.

4. **Bio-inspired pattern generation / synthetic design**
   In design tools that must enforce reflective symmetry (palindromic constraints), this DP gives the minimal additions needed to meet symmetry without changing existing elements.
