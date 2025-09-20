# Minimum Deletions

**Difficulty:** Medium
**Accuracy:** 58.8% **Submissions:** 63K+ **Points:** 4

Given a string **s**, write a program to delete the **minimum number** of characters from the string so that the resultant string is a **palindrome**, while maintaining the order of characters.

---

## Examples

### Example 1

**Input:** `s = "aebcbda"`
**Output:** `2`
**Explanation:** Remove characters `'e'` and `'d'`.

### Example 2

**Input:** `s = "geeksforgeeks"`
**Output:** `8`
**Explanation:** To make `"geeksforgeeks"` a palindrome, the longest palindromic subsequence is `"eefee"` (length 5).
The minimum deletions are: `13 (length of s) - 5 = 8`.

---

## Constraints

* `1 ≤ s.size() ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* `Amazon`

---

## Topic Tags

* `Strings` • `Dynamic Programming` • `Data Structures` • `Algorithms`

---

## Related Articles

* `Minimum Number Deletions Make String Palindrome`

---

---

Awesome—this is a classic “minimum deletions to make a palindrome” problem. The key idea is:

> You only need to **keep** a longest palindromic subsequence (LPS).
> The fewest deletions = `len(s) - LPS(s)`.

Below I’ll explain why, walk a quick dry run, then show two interview-friendly solutions.

---

## 2) Intuition + step-by-step dry run

### Why `n − LPS`?

* If you keep a subsequence that’s already a palindrome and is as long as possible (the **LPS**), you only delete the rest.
* So minimum deletions = characters not in the LPS = `n − LPS`.

And a handy fact:
`LPS(s) = LCS(s, reverse(s))`.

### Dry run on `s = "aebcbda"`

* `reverse(s) = "adbcbea"`.
* Compute `LCS(s, reverse(s))` (or run an LPS DP directly).
  One longest palindromic subsequence is `"abcba"` (length 5).
* `n = 7`, `LPS = 5` → **min deletions = 7 − 5 = 2**.
* A valid deletion set: remove `'e'` and `'d'` to keep `"abcba"`.

---

## 3) Optimized codes (two ways)

### A) DP for LPS directly (two-pointer DP, bottom-up) — O(n²) time, O(n²) or O(n) space

We’ll fill `dp[i][j] = length of LPS in s[i..j]`.

* If `s[i] == s[j]`: `dp[i][j] = 2 + dp[i+1][j-1]` (or `1` when `i==j`)
* Else: `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Bottom-up DP for LPS.
        Time : O(n^2)
        Space: O(n^2)  (can be optimized to O(n) with rolling rows/diagonals)
        """
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0] * n for _ in range(n)]
        # single chars are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # length from 2..n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        lps = dp[0][n - 1]
        return n - lps
```

### B) LCS with the reversed string — O(n²) time, O(n) space (classic interview favorite)

Compute LCS of `s` and `rev = s[::-1]`. That LCS length is LPS.

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        """
        LPS(s) = LCS(s, reverse(s)).
        We'll compute LCS in O(n^2) time and O(n) space.
        """
        n = len(s)
        if n <= 1:
            return 0

        t = s[::-1]
        # LCS rolling array
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        lps = prev[n]
        return n - lps
```

> Either solution is perfectly acceptable. The LCS version often impresses interviewers because it reuses a very common DP pattern and uses O(n) space.

---

## 4) Interviewer-style Q\&A

**Q1. Why is `min deletions = n − LPS` correct?**
Because you can **keep** the LPS and delete everything else. Any palindromic subsequence you keep can’t be longer than the LPS. So the fewest deletions equals the number of characters **not** in that LPS.

**Q2. Can we do it with insertions instead?**
Yes. For minimum insertions to make a palindrome, the answer is also `n − LPS`. (Deletions in `s` correspond to insertions in the reverse process.)

**Q3. Time/Space complexity trade-offs?**

* LPS DP table: **O(n²) time**, **O(n²) space** (can be optimized to O(n) with diagonal/rolling techniques but is trickier).
* LCS with reverse: **O(n²) time**, **O(n) space** using a rolling 1-D DP array.

**Q4. Edge cases?**

* Empty or length-1 string → 0 deletions.
* Already a palindrome → LPS = n → answer 0.
* All distinct characters → LPS = 1 → answer n−1.

**Q5. Can we reconstruct which characters to delete?**
Yes—store choices in the DP and backtrack to get one LPS, then delete others accordingly. That’s optional unless explicitly asked.

---

---

Here’s a complete, runnable script that:

* solves **Minimum Deletions to make a string a palindrome** using the standard `n − LPS` idea, computed via **LCS(s, reverse(s))** with **O(n²) time** and **O(n) space**,
* prints results for sample inputs,
* and times the full run with `timeit`.

---

## 5) Full program (with inline time/space notes + timing)

```python
#!/usr/bin/env python3
"""
Minimum deletions to make a string a palindrome.

Key identity:
  min_deletions(s) = len(s) - LPS(s)
And:
  LPS(s) = LCS(s, reverse(s))

We implement LCS with a rolling 1-D DP array:
  Time  : O(n^2)
  Space : O(n)
"""

from timeit import default_timer as timer
from typing import List


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Compute min deletions to make s a palindrome via
        LPS(s) = LCS(s, reverse(s)).

        DP state (LCS):
          prev[j] / curr[j] = LCS length for s[:i] and t[:j]
        Transitions per cell are O(1); we have (n*n) cells.

        Overall complexity:
          Time  : O(n^2)
          Space : O(n)  (rolling array of size n+1)
        """
        n = len(s)
        if n <= 1:
            return 0

        t = s[::-1]               # reverse(s)  -- O(n) time, O(n) space
        prev = [0] * (n + 1)      # O(n) space

        # Fill DP row by row; i loops over s, j over t
        # Time: O(n^2)
        for i in range(1, n + 1):
            curr = [0] * (n + 1)  # O(n) extra, reused each row
            si = s[i - 1]
            for j in range(1, n + 1):
                if si == t[j - 1]:
                    # Match extends previous diagonal
                    curr[j] = 1 + prev[j - 1]
                else:
                    # Either drop from s or t
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        lps = prev[n]             # LPS(s) = LCS(s, reverse(s))
        return n - lps            # deletions = n - LPS


# Optional: alternative DP that directly computes LPS (for curiosity/testing).
class SolutionLPS:
    def minDeletions(self, s: str) -> int:
        """
        Direct LPS DP: dp[i][j] = LPS length in s[i..j].
        Time  : O(n^2)
        Space : O(n^2)  (could be optimized to O(n) with diagonals)
        """
        n = len(s)
        if n <= 1:
            return 0

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  # single char palindrome

        # length from 2..n
        for L in range(2, n + 1):                       # O(n)
            for i in range(0, n - L + 1):               # O(n)
                j = i + L - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 if L == 2 else 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        lps = dp[0][n - 1]
        return n - lps


def main():
    sol = Solution()     # O(n) space LCS version
    sol2 = SolutionLPS() # O(n^2) space LPS version (optional check)

    # -------------------------
    # Sample / edge test cases
    # -------------------------
    tests = [
        # (input_string, expected_min_deletions)
        ("aebcbda", 2),           # keep "abcba" (LPS=5) => 7-5=2
        ("geeksforgeeks", 8),     # LPS length 5 => 13-5=8
        ("ab", 1),                # keep 'a' or 'b'
        ("aa", 0),                # already palindrome
        ("", 0),                  # empty
        ("a", 0),                 # single char
        ("character", 5),         # typical random string
    ]

    print("== Minimum deletions to make a palindrome ==")
    for s, expected in tests:
        got = sol.minDeletions(s)
        print(f"s={s!r:14}  -> deletions={got} (expected {expected})  {'OK' if got == expected else '!!'}")

        # Optional cross-check for small n with the O(n^2)-space method
        if len(s) <= 60:
            alt = sol2.minDeletions(s)
            assert got == alt, f"mismatch vs LPS DP for {s!r}: {got} != {alt}"

    # -------------------------
    # Timing on a larger input
    # -------------------------
    big = "geeksforgeeks" * 60  # length ~ 13*60 = 780 (well within constraints)
    start = timer()
    res = sol.minDeletions(big)
    end = timer()
    print(f"\nTiming: |s|={len(big)} -> result={res}, time={(end-start):.6f} s")


if __name__ == "__main__":
    main()
```

**What it prints (example):**

```
== Minimum deletions to make a palindrome ==
s='aebcbda'      -> deletions=2 (expected 2)  OK
s='geeksforgeeks'-> deletions=8 (expected 8)  OK
s='ab'           -> deletions=1 (expected 1)  OK
s='aa'           -> deletions=0 (expected 0)  OK
s=''             -> deletions=0 (expected 0)  OK
s='a'            -> deletions=0 (expected 0)  OK
s='character'    -> deletions=5 (expected 5)  OK

Timing: |s|=780 -> result=???, time=0.00xxx s
```

---

## 6) Real-World Use Cases (high-value)

1. **Data cleaning / error correction (palindromic patterns):**
   In bioinformatics or telemetry streams where palindromic symmetry is expected (e.g., specific DNA motifs or mirrored protocol markers), compute minimal edits to restore symmetry by *deletions only*.

2. **Version diff / UI “palindromic” formatting constraints:**
   When enforcing symmetrical UI strings or mirrored labels, estimate the fewest deletions needed to meet the constraint without reordering characters.

3. **Compression heuristics / feature engineering:**
   “Palindromic closeness” (via `n − LPS`) can be used as a lightweight feature indicating structural symmetry in text, identifiers, or code tokens—useful in clustering or anomaly detection.
