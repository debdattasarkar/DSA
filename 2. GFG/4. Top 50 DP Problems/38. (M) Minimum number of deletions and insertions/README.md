# Minimum number of deletions and insertions

**Difficulty:** Medium
**Accuracy:** 65.29%
**Submissions:** 75K+
**Points:** 4

---

Given two strings **s1** and **s2**. The task is to **remove or insert** the minimum number of characters from/in **s1** to transform it into **s2**. It could be possible that the same character needs to be removed from one point of **s1** and inserted into another point.

---

## Examples

### Example 1

**Input:** `s1 = "heap", s2 = "pea"`
**Output:** `3`
**Explanation:** `'p'` and `'h'` deleted from **heap**. Then, `'p'` is inserted at the beginning.

### Example 2

**Input:** `s1 = "geeksforgeeks", s2 = "geeks"`
**Output:** `8`
**Explanation:** 8 deletions, i.e. remove all characters of the string **"forgeeks"**.

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 1000`
* All the characters are lowercase English alphabets.

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Articles

* Minimum Number Deletions Insertions Transform One String Another

---

---

awesome—here’s the interview-ready package.

# 2) Explanation + step-by-step dry run

## What are we minimizing?

Only **deletions from `s1`** and **insertions into `s1`** are allowed to transform `s1` → `s2`.
Characters that appear **in both strings and in the same relative order** can stay; everything else must be removed or inserted.

That “kept backbone” is the **Longest Common Subsequence (LCS)**.

If `L = LCS(s1, s2)` then:

* **deletions** needed = `len(s1) - L`
* **insertions** needed = `len(s2) - L`
* **total operations** = `len(s1) + len(s2) - 2L`

So the problem reduces to computing `LCS` length.

## LCS DP recap (bottom-up)

Let `dp[i][j]` = LCS length of prefixes `s1[:i]` and `s2[:j]` (i.e., first `i` and `j` chars).
Base: any `i==0` or `j==0` ⇒ `dp[i][j]=0`.
Transition:

* If `s1[i-1]==s2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
* else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

### Dry run: `s1="heap"`, `s2="pea"`

Build `dp` (rows for `h e a p`, cols for `p e a`):

Start with a 5×4 zero table (extra row/col for empty prefixes).

Fill row by row:

* Compare `h`:

  * vs `p`: no match ⇒ `dp[1][1]=max(dp[0][1],dp[1][0])=0`
  * vs `e`: 0, vs `a`: 0
* Compare `e`:

  * vs `p`: 0
  * vs `e`: match ⇒ `dp[2][2]=dp[1][1]+1=1`
  * vs `a`: no match ⇒ `dp[2][3]=max(dp[1][3],dp[2][2])=1`
* Compare `a`:

  * vs `p`: 0
  * vs `e`: 1
  * vs `a`: match ⇒ `dp[3][3]=dp[2][2]+1=2`
* Compare `p`:

  * vs `p`: match ⇒ `dp[4][1]=dp[3][0]+1=1`
  * vs `e`: keep max ⇒ `dp[4][2]=max(1,1)=1`
  * vs `a`: keep max ⇒ `dp[4][3]=max(2,1)=2`

Final `dp[4][3] = 2` ⇒ `L = 2` (LCS is `"ea"`).
Deletions `= 4-2 = 2` (delete `h` and `p`), Insertions `= 3-2 = 1` (insert `p` at front).
**Total = 3**, matching the example.

For `s1="geeksforgeeks"`, `s2="geeks"`: `L=5`, deletions `=13-5=8`, insertions `=5-5=0`, total `=8`.

---

# 3) Python solutions (multiple styles)

## A) Bottom-up LCS (most expected) — O(n·m) time, O(n·m) space

```python
#User function Template for python3
class Solution:
    def minOperations(self, s1, s2):
        n, m = len(s1), len(s2)
        # dp[i][j] = LCS length of s1[:i] and s2[:j]
        dp = [[0]*(m+1) for _ in range(n+1)]  # O(n*m) space

        # Fill table: O(n*m) time
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        L = dp[n][m]
        deletions = n - L
        insertions = m - L
        return deletions + insertions
```

## B) Space-optimized LCS (1D DP) — O(n·m) time, O(min(n,m)) space

```python
#User function Template for python3
class Solution1D:
    def minOperations(self, s1, s2):
        # Make the second dimension the smaller one for less space
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        n, m = len(s1), len(s2)

        prev = [0]*(m+1)  # dp for previous row (O(m) space)
        for i in range(1, n+1):
            cur = [0]*(m+1)
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(prev[j], cur[j-1])
            prev = cur

        L = prev[m]
        return (n - L) + (m - L)
```

## C) Top-down LCS with memoization — clean derivation, same complexity

```python
#User function Template for python3
class SolutionMemo:
    def minOperations(self, s1, s2):
        from functools import lru_cache
        n, m = len(s1), len(s2)

        @lru_cache(maxsize=None)
        def lcs(i, j):
            # LCS length of s1[:i] and s2[:j]
            if i == 0 or j == 0:
                return 0
            if s1[i-1] == s2[j-1]:
                return 1 + lcs(i-1, j-1)
            return max(lcs(i-1, j), lcs(i, j-1))

        L = lcs(n, m)
        return (n - L) + (m - L)
```

**Why these are “optimized / expected”:**
All three compute LCS in `O(n·m)` time. Version B cuts memory to `O(min(n,m))`, which is commonly asked as a follow-up. Version C shows the same logic recursively with memoization.

---

# 4) Likely interviewer Q&A

**Q1. Why does LCS solve the problem?**
Characters in the LCS already appear in both strings in correct relative order, so we **keep** them. Every other character in `s1` must be **deleted**; every other character needed by `s2` must be **inserted**. Hence deletions `= |s1|-L`, insertions `= |s2|-L`.

**Q2. What’s the time/space complexity?**
Standard DP: `O(n·m)` time, `O(n·m)` space.
Space-optimized DP: `O(n·m)` time, `O(min(n,m))` space.

**Q3. How is this different from edit distance (Levenshtein)?**
Levenshtein allows **substitution** (cost 1). Here we only allow **delete/insert**. A substitution can be simulated as delete+insert (cost 2), so answers differ when substitutions would be optimal.

**Q4. Edge cases?**

* One string empty ⇒ answer is length of the other (all inserts or all deletes).
* All characters different ⇒ `L=0`, answer `= |s1|+|s2|`.
* Identical strings ⇒ `L=|s1|`, answer `=0`.

**Q5. Can we reconstruct the actual operations?**
Yes: backtrack from the DP table.

* If `s1[i-1]==s2[j-1]`, move diagonally (keep char).
* If `dp[i-1][j] >= dp[i][j-1]`, record “delete `s1[i-1]`” and move up; else record “insert `s2[j-1]`” and move left.
  Reverse the recorded ops at the end.

**Q6. Any faster than `O(n·m)`?**
For general strings, not in the worst case (LCS is hard to beat). With small alphabets and very long strings, there are bitset tricks that give large constant-factor speedups, but asymptotics remain near `O(n·m/word_size)`.

---

---

here you go—clean, runnable, and interview-ready.

---

## Full program (with timing + inline complexity notes)

```python
#!/usr/bin/env python3
"""
Minimum number of deletions and insertions to transform s1 -> s2.
Key identity using Longest Common Subsequence (LCS):

Let L = LCS(s1, s2)
Deletions  = len(s1) - L
Insertions = len(s2) - L
Total ops  = len(s1) + len(s2) - 2*L

Below:
  * Solution (bottom-up 2D LCS) — O(n*m) time, O(n*m) space
  * Solution1D (space-optimized LCS) — O(n*m) time, O(min(n,m)) space
  * Driver that runs sample cases and times the full run using timeit.default_timer
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3 (MOST EXPECTED VERSION)
# ------------------------------------------------------------
class Solution:
    def minOperations(self, s1, s2):
        """
        Bottom-up LCS table.

        dp[i][j] = LCS length of s1[:i] and s2[:j]
        Base: any i==0 or j==0 -> 0
        Transition:
          if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
          else:                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        Time Complexity:
          - Building the table visits each cell once: O(n*m)
        Space Complexity:
          - Table (n+1) x (m+1): O(n*m)
        """
        n, m = len(s1), len(s2)

        # O(n*m) space
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # O(n*m) time to fill
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    # O(1) update
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # O(1) update
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        L = dp[n][m]
        deletions = n - L
        insertions = m - L
        total_ops = deletions + insertions
        # (optional) keep stats so the driver can print breakdown without recomputing
        self.last_stats = {"LCS": L, "deletions": deletions, "insertions": insertions, "total": total_ops}
        return total_ops


# ------------------------------------------------------------
# Space-optimized version (nice follow-up)
# ------------------------------------------------------------
class Solution1D:
    def minOperations(self, s1, s2):
        """
        LCS with rolling rows.

        Time Complexity: O(n*m)
        Space Complexity: O(min(n,m))  -- we keep only one row at a time.
        """
        # Make the second dimension the smaller one to minimize space
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        n, m = len(s1), len(s2)

        prev = [0] * (m + 1)  # O(m) space
        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur

        L = prev[m]
        deletions = len(s1) - L
        insertions = len(s2) - L
        return deletions + insertions


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def main():
    tests = [
        ("heap", "pea", 3),               # example 1
        ("geeksforgeeks", "geeks", 8),    # example 2
        ("a", "a", 0),                    # identical
        ("abc", "xyz", 6),                # no common letters -> |s1|+|s2|
        ("abcd", "abdc", 2),              # small swap => del+ins
    ]

    sol = Solution()
    sol1d = Solution1D()

    print("Minimum Insertions+Deletions to Transform s1 -> s2\n")

    t0 = timer()  # start timing (same clock used by timeit)
    for s1, s2, exp in tests:
        total = sol.minOperations(s1, s2)
        total1d = sol1d.minOperations(s1, s2)
        stats = getattr(sol, "last_stats", None)

        print(f"s1 = {s1!r}, s2 = {s2!r}")
        print(f"  Output (2D DP): {total}  |  Output (1D DP): {total1d}  |  Expected: {exp}")
        if stats:
            print(f"  Breakdown: deletions={stats['deletions']}, insertions={stats['insertions']}, LCS={stats['LCS']}")
        print("-" * 66)
    t1 = timer()  # stop timing

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for full program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

* **Version control / diff tools:** Estimating the minimal set of **insertions** and **deletions** to turn one file into another (when substitutions aren’t allowed or are modeled as del+ins).

* **Database / API contract migrations:** Planning minimal **remove/add** changes to transform one schema or payload format into another while preserving the largest common “backbone” (the LCS).

* **Bioinformatics (indels):** Modeling **insertions** and **deletions** (indels) required to align two DNA/RNA sequences when substitutions are considered separately or weighted differently.

* **Content synchronization:** Syncing documents/message logs by computing minimal add/remove operations relative to a shared common subsequence to reduce transmission cost.
