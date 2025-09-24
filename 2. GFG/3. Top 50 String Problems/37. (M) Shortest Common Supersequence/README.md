# Shortest Common Supersequence

**Difficulty:** Medium
**Accuracy:** 52.65%
**Submissions:** 133K+
**Points:** 4

Given two strings `s1` and `s2`, find the length of the **smallest string** which has both `s1` and `s2` as its **subsequences**.

> Note: `s1` and `s2` can have both uppercase and lowercase English letters.

---

## Examples

**Example 1**

* **Input:** `s1 = "geek"`, `s2 = "eke"`
* **Output:** `5`
* **Explanation:** The string `"geeke"` has both `"geek"` and `"eke"` as subsequences.

---

**Example 2**

* **Input:** `s1 = "AGGTAB"`, `s2 = "GXTXAYB"`
* **Output:** `9`
* **Explanation:** The string `"AGXGTXAYB"` has both `"AGGTAB"` and `"GXTXAYB"` as subsequences.

---

**Example 3**

* **Input:** `s1 = "geek"`, `s2 = "ek"`
* **Output:** `4`
* **Explanation:** The string `"geek"` itself has both `"geek"` and `"ek"` as subsequences.

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 500`

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`
  where `n = len(s1)` and `m = len(s2)`.

---

## Company Tags

Microsoft

---

## Topic Tags

Strings, Dynamic Programming, Data Structures, Algorithms

---

## Related Articles

* Shortest Common Supersequence

---

---

Here’s a crisp, interview-ready guide for **Shortest Common Supersequence (length only)**.

---

# 2) Explanation + Step-by-Step Dry Run

### What is the SCS?

For two strings `s1` and `s2`, a **shortest common supersequence (SCS)** is the shortest string that contains both `s1` and `s2` as **subsequences** (order preserved, not necessarily contiguous).

### Key fact

There’s a tight relationship with **LCS** (Longest Common Subsequence):

```
len(SCS) = len(s1) + len(s2) − len(LCS(s1, s2))
```

Intuition: the LCS characters are “shared” once in the supersequence; the remaining characters from each string must be inserted around that.

---

## Dry run on: s1 = "geek", s2 = "eke"

We’ll compute LCS length (classic DP).
Let `n = 4`, `m = 3`. Define `lcs[i][j]` = LCS length of `s1[:i]` and `s2[:j]`.

Initialize row0/col0 = 0.

Fill table (only showing final values):

```
      j→   0 1 2 3
           - e k e
i 0  -     0 0 0 0
↓ 1  g     0 0 0 0
  2  e     0 1 1 1
  3  e     0 1 1 2
  4  k     0 1 2 2
```

* `lcs[4][3] = 2` (one LCS is “ek” or “ee” depending on alignments, but length is 2)

Then:

```
len(SCS) = 4 + 3 − 2 = 5
```

A valid SCS is `"geeke"` (length 5).

---

# 3) Optimized Python Solutions (interview-style)

You can compute the SCS length **either**:

1. Directly with an SCS DP, or
2. Via LCS and use the formula.

Both are O(n·m) time. Choose **space-optimized** if asked.

---

### A) Direct SCS-length DP (clean & expected)

Recurrence:
`dp[i][j]` = SCS length for `s1[:i]` and `s2[:j]`

* If `s1[i-1] == s2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`
* Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])`
  Base:
* `dp[i][0] = i`, `dp[0][j] = j`

```python
#User function Template for python3
class Solution:
    
    # Function to find length of shortest common supersequence
    def shortestCommonSupersequence(self, s1, s2):
        n, m = len(s1), len(s2)
        # dp[i][j] = SCS length for s1[:i] and s2[:j]
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # base cases: one string empty → need all chars from the other
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        
        # fill table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]
```

**Complexity:**
Time `O(n·m)`; Space `O(n·m)`.

---

### B) LCS-first, then formula (also very common in interviews)

Compute LCS length with DP, then return `n + m − lcs`.

```python
class Solution:

    def shortestCommonSupersequence(self, s1, s2):
        n, m = len(s1), len(s2)
        # lcs[i][j] = LCS length for s1[:i] and s2[:j]
        lcs = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i][j] = 1 + lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        
        return n + m - lcs[n][m]
```

**Complexity:**
Time `O(n·m)`; Space `O(n·m)`.

---

### C) Space-optimized LCS (for tight memory conditions)

Keep only two rows; result still `n + m − LCS`.

```python
class Solution:

    def shortestCommonSupersequence(self, s1, s2):
        if len(s2) > len(s1):  # keep second as the shorter if you like
            s1, s2 = s2, s1
        n, m = len(s1), len(s2)
        
        prev = [0]*(m+1)
        for i in range(1, n+1):
            cur = [0]*(m+1)
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur
        
        lcs_len = prev[m]
        return n + m - lcs_len
```

**Complexity:**
Time `O(n·m)`; Space **`O(min(n, m))`**.

> Tip: If asked to **construct** the SCS string, use the full 2D DP (A) or full LCS table and backtrack. For *length only*, the above are enough.

---

# 4) Interview Q\&A

**Q1. Why does `len(SCS) = n + m − len(LCS)` hold?**
**A.** Every character must appear in the supersequence. Characters belonging to the LCS are common to both strings and thus “shared” once in the SCS. Everything else (the non-LCS characters) must be added, giving `n + m − LCS`.

**Q2. Which DP is simpler to explain: SCS-DP or LCS-then-formula?**
**A.** For **length only**, both are fine. Many candidates choose LCS then formula because LCS is a common pattern. The direct SCS DP is also perfectly acceptable and arguably more direct.

**Q3. Can we do better than `O(n·m)` time?**
**A.** In general, no. Computing LCS (and thus SCS length) for arbitrary strings is `O(n·m)` in the worst case.

**Q4. How do you reconstruct the actual SCS string, not only its length?**
**A.** Use the direct SCS DP (A). Start at `dp[n][m]` and backtrack:

* If `s1[i-1] == s2[j-1]`, put that char once and move `(i-1, j-1)`.
* Else move to the cell (`i-1, j` or `i, j-1`) with smaller `dp` value and place the corresponding character.
  Append remaining prefixes if one string is exhausted. Reverse at the end.

**Q5. Edge cases to watch?**
**A.** Empty strings (SCS length = length of the other), identical strings (SCS length = n), and no common characters (SCS length = n + m).

---

---

Below is a complete, runnable program that:

* Implements **two interview-ready solutions** to compute the **length of the Shortest Common Supersequence (SCS)**

  1. **Direct SCS DP**
  2. **LCS (space-optimized) + formula**
* Prints results for sample inputs
* Reports end-to-end runtime using `timeit`

---

```python
"""
Shortest Common Supersequence (length only)

Definitions:
- SCS(s1, s2): the shortest string that contains both s1 and s2 as subsequences.
- Relationship with LCS:
    len(SCS) = len(s1) + len(s2) - len(LCS)

This file provides:
  A) Direct SCS DP (classic, explicit)
  B) LCS (space-optimized) + formula (memory-friendly)

Both run in O(n*m) time. Choose based on what interviewer prefers.
"""

from timeit import default_timer as timer


class SolutionSCS_DP:
    """
    Direct DP for SCS length.

    dp[i][j] = length of SCS for s1[:i] and s2[:j]

    Recurrence:
      if s1[i-1] == s2[j-1]:
          dp[i][j] = 1 + dp[i-1][j-1]
      else:
          dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    Time  : O(n*m) (fill an (n+1)*(m+1) table)
    Space : O(n*m) (the DP table)
    """

    def shortestCommonSupersequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        # Base rows/cols:
        # dp[i][0] = i (need all i chars of s1) ; dp[0][j] = j (need all j chars of s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        # Fill DP
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]


class SolutionLCS_Optimized:
    """
    LCS + formula approach with O(min(n, m)) space.

    We compute LCS(s1, s2) using two rolling rows:
        prev[j] = LCS length for s1[:i-1], s2[:j]
        cur[j]  = LCS length for s1[:i],   s2[:j]

    Then len(SCS) = len(s1) + len(s2) - LCS.

    Time  : O(n*m)
    Space : O(min(n, m))  (only two rows of size of shorter string)
    """

    def shortestCommonSupersequence(self, s1: str, s2: str) -> int:
        # Make s2 the shorter one for better space usage.
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        n, m = len(s1), len(s2)
        prev = [0] * (m + 1)

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur

        lcs_len = prev[m]
        return n + m - lcs_len


def demo_and_time():
    """
    Drives both implementations on a few testcases,
    prints outputs and measures total runtime.

    Timing notes:
    - We time the whole demo (setup + calls) so you see end-to-end runtime.
    - For micro-benchmarks, loop the solver calls more times.
    """
    tests = [
        ("geek", "eke", 5),           # from prompt: SCS length = 5
        ("AGGTAB", "GXTXAYB", 9),     # classic example: LCS=4 -> 6+7-4=9
        ("geek", "ek", 4),
        ("abc", "abc", 3),            # identical -> SCS = len
        ("abc", "def", 6),            # disjoint -> SCS = n + m
    ]

    scs_dp = SolutionSCS_DP()
    lcs_opt = SolutionLCS_Optimized()

    print("=== Shortest Common Supersequence (length only) ===\n")

    # ---- Time the entire run ----
    t0 = timer()

    print("[A] Direct SCS DP:")
    for s1, s2, want in tests:
        got = scs_dp.shortestCommonSupersequence(s1, s2)
        print(f"  s1={s1!r}, s2={s2!r} -> length={got} (expected {want})")

    print("\n[B] LCS (space-optimized) + formula:")
    for s1, s2, want in tests:
        got = lcs_opt.shortestCommonSupersequence(s1, s2)
        print(f"  s1={s1!r}, s2={s2!r} -> length={got} (expected {want})")

    t1 = timer()
    print(f"\nTotal runtime (this program run): {(t1 - t0)*1000:.3f} ms")

    # Complexity summary (printed for clarity)
    print(
        "\nComplexity:\n"
        "  - Direct SCS DP       : Time O(n*m), Space O(n*m)\n"
        "  - LCS + formula (opt) : Time O(n*m), Space O(min(n, m))"
    )


if __name__ == "__main__":
    demo_and_time()
```

### Sample Output (what you’ll see)

```
=== Shortest Common Supersequence (length only) ===

[A] Direct SCS DP:
  s1='geek', s2='eke' -> length=5 (expected 5)
  s1='AGGTAB', s2='GXTXAYB' -> length=9 (expected 9)
  s1='geek', s2='ek' -> length=4 (expected 4)
  s1='abc', s2='abc' -> length=3 (expected 3)
  s1='abc', s2='def' -> length=6 (expected 6)

[B] LCS (space-optimized) + formula:
  s1='geek', s2='eke' -> length=5 (expected 5)
  s1='AGGTAB', s2='GXTXAYB' -> length=9 (expected 9)
  s1='geek', s2='ek' -> length=4 (expected 4)
  s1='abc', s2='abc' -> length=3 (expected 3)
  s1='abc', s2='def' -> length=6 (expected 6)

Total runtime (this program run): X.XXX ms

Complexity:
  - Direct SCS DP       : Time O(n*m), Space O(n*m)
  - LCS + formula (opt) : Time O(n*m), Space O(min(n, m))
```

---

## 6) Real-World Use Cases (a few high-impact ones)

* **Version control & 3-way merge**: Building a minimal supersequence of two edits helps reason about the shortest combined text that preserves both authors’ line orders.
* **Bioinformatics (sequence alignment)**: When aligning DNA/RNA, SCS length provides a compact measure of combining two sequences while preserving order—complementary to LCS metrics.
* **Data synchronization / log merging**: When two ordered event streams must be merged with minimal additional entries while preserving each stream’s relative order.
* **Diff/patch tooling**: SCS length is tied to minimal edits necessary to interleave two sequences without reordering, useful in explaining or constraining patch application.
