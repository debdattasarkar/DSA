# Longest Common Substring

**Difficulty:** Medium
**Accuracy:** 42.69%
**Submissions:** 304K+
**Points:** 4

---

## Problem Statement

You are given two strings `s1` and `s2`. Your task is to find the **length of the longest common substring** among the given strings.

---

## Examples

### Example 1

**Input:** `s1 = "ABCDGH", s2 = "ACDGHR"`
**Output:** `4`
**Explanation:** The longest common substring is `"CDGH"` with a length of `4`.

---

### Example 2

**Input:** `s1 = "abc", s2 = "acb"`
**Output:** `1`
**Explanation:** The longest common substrings are `"a"`, `"b"`, `"c"` all having length `1`.

---

### Example 3

**Input:** `s1 = "YZ", s2 = "yz"`
**Output:** `0`

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 10^3`
* Both strings may contain upper and lower case alphabets.

---

## Expected Complexities

* **Time Complexity:** `O(n * m)`
* **Auxiliary Space:** `O(n * m)`

---

## Company Tags

* Morgan Stanley
* Amazon
* Microsoft

---

## Topic Tags

* Strings
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* Longest Common Substring DP 29
* Longest Common Substring Space Optimized DP Solution

---

---

awesome — let’s make **Longest Common Substring** interview-ready.

---

# 2) Explanation + step-by-step dry run

**Goal:** Given `s1`, `s2`, return the **length** of the longest string that appears *contiguously* in **both**.

### Classic DP idea (most expected)

Let `dp[i][j]` be the **length of the longest common substring that ends at** `s1[i-1]` and `s2[j-1]`.

Transition:

```
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = 0              # must reset because substring must be contiguous
```

Answer is `max(dp[i][j])` over all `i, j`.

We can compress to **O(min(n,m))** space with a rolling row.

### Dry run (Example 1)

`s1="ABCDGH", s2="ACDGHR"`

We only keep previous row. Start with all zeros.

* When processing `C` vs `C` → `dp=1`
* Then `D` vs `D` extends → `dp=2`
* Then `G` vs `G` extends → `dp=3`
* Then `H` vs `H` extends → `dp=4`
  Any mismatch resets to `0`. Max seen is **4** → `"CDGH"`.

---

# 3) Python solutions (brute & optimized)

All snippets conform to:

```python
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
```

## A) Optimized DP with rolling array — **O(n·m) time, O(min(n,m)) space** ✅

```python
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        """
        DP definition:
          dp[j] = length of LCSuffix ending at current s1 char and s2[j-1]
        We keep only one row (rolling), and a 'prev' cell for dp[i-1][j-1].

        Time : O(n * m)  -- every pair (i,j) visited once
        Space: O(min(n, m))  -- we make the shorter string the columns
        """
        # Ensure s2 is the shorter to minimize space
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)      # dp[0]=0 is sentinel
        best = 0

        for i in range(1, n + 1):
            prev_diag = 0       # this holds dp[j-1] from previous row (dp[i-1][j-1])
            for j in range(1, m + 1):
                temp = dp[j]    # save current dp[j] before overwriting; it's dp[i-1][j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev_diag + 1
                    if dp[j] > best:
                        best = dp[j]
                else:
                    dp[j] = 0   # reset because substring must be contiguous
                prev_diag = temp
        return best
```

---

## B) Brute force (educational) — **O(n·m·L)** time, **O(1)** space

Try every starting pair and extend while characters match (`L` ≤ `min(n,m)`).

```python
class SolutionBrute:
    def longestCommonSubstr(self, s1, s2):
        """
        For each (i,j), extend k while s1[i+k]==s2[j+k].
        Time : O(n * m * min(n,m))
        Space: O(1)
        """
        n, m = len(s1), len(s2)
        best = 0
        for i in range(n):
            for j in range(m):
                k = 0
                while i + k < n and j + k < m and s1[i + k] == s2[j + k]:
                    k += 1
                if k > best:
                    best = k
        return best
```

---

## C) Diagonal scan (no table) — **O(n·m) time, O(1) space**

Walk all diagonals of the `n×m` grid; keep a rolling `len` counter that resets on mismatch.

```python
class SolutionDiagonal:
    def longestCommonSubstr(self, s1, s2):
        """
        Scan all (i-j) diagonals. Along a diagonal we compare aligned chars.
        We maintain current run length and reset on mismatch.

        Time : O(n * m)
        Space: O(1)
        """
        n, m = len(s1), len(s2)
        best = 0
        # Offsets from -(m-1) .. (n-1)
        for off in range(-(m - 1), n):
            i = max(0, off)
            j = max(0, -off)
            run = 0
            while i < n and j < m:
                if s1[i] == s2[j]:
                    run += 1
                    if run > best:
                        best = run
                else:
                    run = 0
                i += 1
                j += 1
        return best
```

> In interviews, lead with **A (rolling DP)**. If nudged for variants, mention **C (diagonal O(1) space)** or a **binary search + rolling hash** solution for very long strings (tradeoff: complexity, hashing collisions).

---

# 4) Interview Q&A (high-yield)

**Q1. Substring vs subsequence?**
Substring = contiguous block; subsequence can skip characters. This problem is **substring**; hence mismatches **reset to 0** in DP.

**Q2. Relation to LCS (Longest Common Subsequence)?**
Different DP: LCS allows skipping and uses `max(dp[i-1][j], dp[i][j-1])`; here we use `dp[i-1][j-1]+1` on match and **0 on mismatch**.

**Q3. Why does rolling DP work?**
`dp[i][j]` depends only on `dp[i-1][j-1]`. Keep one row `dp[j]` (which stores `dp[i-1][j]`) and a variable `prev_diag` to hold `dp[i-1][j-1]`.

**Q4. Time/space complexity?**
DP visits each cell once ⇒ **O(n·m)** time. With rolling array it’s **O(min(n,m))** space (or **O(1)** in diagonal scan).

**Q5. How to retrieve the substring itself (not only length)?**
Track `best` and the `(i,j)` where it occurs; with DP keep `end_pos = i` whenever `dp[j]` updates `best`. Return `s1[end_pos-best:end_pos]`.

**Q6. Case sensitivity / alphabet?**
As given, uppercase and lowercase are distinct. If a case-insensitive variant is desired, pre-normalize (`lower()`).

**Q7. What happens on empty strings?**
If either string is empty, answer is `0`. (The code naturally handles it.)

---

---

here’s a **ready-to-run program** for **Longest Common Substring** that:

* reads two strings from stdin (first two non-empty lines),
* solves it via **three approaches**

  1. **Rolling DP** (recommended) – `O(n·m)` time, `O(min(n,m))` space
  2. **Diagonal scan** – `O(n·m)` time, `O(1)` space
  3. **Brute force** (tiny inputs only) – `O(n·m·min(n,m))` time, `O(1)` space
* prints the answers and **times each** using `timeit.timeit(number=1)`.

Inline comments spell out the **time/space complexity** at each step.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Longest Common Substring (length only)
#
# Goal: Given s1, s2, compute the length of the longest string that appears
#       contiguously in both s1 and s2.
#
# Implementations:
#   1) Rolling DP (recommended)
#        Time : O(n * m)       -- visit each (i,j) cell once
#        Space: O(min(n, m))   -- keep only one row over shorter string
#   2) Diagonal scan (no table)
#        Time : O(n * m)
#        Space: O(1)
#   3) Brute force (educational; for tiny inputs)
#        Time : O(n * m * min(n,m))  -- extend from every (i,j)
#        Space: O(1)
#
# Input (stdin):
#   Two non-empty lines: s1, s2
#
# Output:
#   - Echo input sizes
#   - Answer from each method
#   - Per-method timing (ms) using timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit

# -------------------------- Method 1: Rolling DP --------------------------
class Solution:
    def longestCommonSubstr(self, s1: str, s2: str) -> int:
        """
        DP definition:
          dp[j] = LCSuffix length ending at current s1[i-1] and s2[j-1]
        Transition (contiguity => reset to 0 on mismatch):
          if s1[i-1] == s2[j-1]: dp[j] = prev_diag + 1
          else                 : dp[j] = 0
        We maintain:
          - dp[j] as the previous-row value at column j (dp[i-1][j]),
          - prev_diag = dp[i-1][j-1] carried across the row.

        Time  : O(n * m)  -- the double loop visits each (i,j) once
        Space : O(min(n, m))  -- we store one row sized by the shorter string
        """
        # Ensure columns correspond to the shorter string to minimize memory
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        n, m = len(s1), len(s2)
        if m == 0 or n == 0:
            return 0

        dp = [0] * (m + 1)  # dp[0] is a sentinel; dp[j] ~ dp[i-1][j]
        best = 0

        # Outer loop over s1 characters (rows) -> O(n)
        for i in range(1, n + 1):
            prev_diag = 0  # holds dp[i-1][j-1]
            # Inner loop over s2 characters (columns) -> O(m)
            for j in range(1, m + 1):
                tmp_prev_row_same_col = dp[j]  # save dp[i-1][j] before overwrite
                if s1[i - 1] == s2[j - 1]:
                    # extend common suffix by 1
                    dp[j] = prev_diag + 1
                    if dp[j] > best:
                        best = dp[j]  # track global maximum
                else:
                    # mismatch breaks a contiguous substring; reset to 0
                    dp[j] = 0
                prev_diag = tmp_prev_row_same_col  # move diagonal for next j
        return best


# ----------------------- Method 2: Diagonal scan --------------------------
class SolutionDiagonal:
    def longestCommonSubstr(self, s1: str, s2: str) -> int:
        """
        Observe that (i,j) pairs with constant (i-j) lie on a diagonal. Scan
        each diagonal once while maintaining the current run length.
        On mismatch, reset run to 0. Keep the maximum run.

        Time  : O(n * m)  -- each pair (i,j) touched exactly once
        Space : O(1)      -- only a few integers
        """
        n, m = len(s1), len(s2)
        if n == 0 or m == 0:
            return 0
        best = 0

        # Offsets range so each diagonal intersects the grid
        for off in range(-(m - 1), n):
            i = max(0, off)   # starting row index on this diagonal
            j = max(0, -off)  # starting col index on this diagonal
            run = 0
            # Walk down-right along the diagonal -> O(length of this diagonal)
            while i < n and j < m:
                if s1[i] == s2[j]:
                    run += 1
                    if run > best:
                        best = run
                else:
                    run = 0  # contiguous requirement => reset
                i += 1
                j += 1
        return best


# --------------------------- Method 3: Brute ------------------------------
class SolutionBrute:
    def longestCommonSubstr(self, s1: str, s2: str) -> int:
        """
        Try every starting pair (i,j) and extend k while chars match.
        Educational; impractical for large strings.

        Time  : O(n * m * min(n, m))  -- triple-nested in worst-case
        Space : O(1)
        """
        n, m = len(s1), len(s2)
        best = 0
        for i in range(n):           # O(n)
            for j in range(m):       # O(m)
                k = 0
                # extend while equal; O(min(n-i, m-j))
                while i + k < n and j + k < m and s1[i + k] == s2[j + k]:
                    k += 1
                if k > best:
                    best = k
        return best


# ------------------------------- I/O utils -------------------------------
def _read_two_strings():
    """
    Read first two non-empty lines from stdin as s1 and s2.
    """
    lines = [ln.strip() for ln in sys.stdin.read().splitlines()]
    lines = [ln for ln in lines if ln != ""]
    if len(lines) < 2:
        print("Please provide two non-empty lines: s1 (newline) s2")
        sys.exit(0)
    return lines[0], lines[1]

def _preview(s, limit=60):
    return s if len(s) <= limit else s[:limit] + "..."

# --------------------------------- main ----------------------------------
def main():
    s1, s2 = _read_two_strings()
    n, m = len(s1), len(s2)
    print(f"s1 (len={n}): \"{_preview(s1)}\"")
    print(f"s2 (len={m}): \"{_preview(s2)}\"\n")

    sol_dp = Solution()
    sol_dg = SolutionDiagonal()
    sol_br = SolutionBrute()

    # Time each method once with timeit; then compute the result to print.
    t_dp  = timeit.timeit(lambda: sol_dp.longestCommonSubstr(s1, s2), number=1)
    a_dp  = sol_dp.longestCommonSubstr(s1, s2)

    t_dg  = timeit.timeit(lambda: sol_dg.longestCommonSubstr(s1, s2), number=1)
    a_dg  = sol_dg.longestCommonSubstr(s1, s2)

    # Brute guarded to avoid very long runs
    brute_enabled = n * m <= 40_000  # e.g., up to ~200x200 worst-case comfortably
    if brute_enabled:
        t_br  = timeit.timeit(lambda: sol_br.longestCommonSubstr(s1, s2), number=1)
        a_br  = sol_br.longestCommonSubstr(s1, s2)
        brute_line = f"{a_br}\nTime (ms): {t_br * 1000.0:.3f}"
    else:
        brute_line = "(skipped: input too large)"

    print("Rolling DP     (O(n*m) time, O(min) space):", a_dp)
    print("Time (ms): {:.3f}\n".format(t_dp * 1000.0))

    print("Diagonal scan  (O(n*m) time, O(1)   space):", a_dg)
    print("Time (ms): {:.3f}\n".format(t_dg * 1000.0))

    print("Brute force    (O(n*m*L) time)         :", brute_line)

    # Basic agreement check if brute ran
    if brute_enabled:
        print("\nAll methods agree ✔" if (a_dp == a_dg == a_br) else "\nWARNING: methods disagree!")
    else:
        print("\nAgreement (DP vs Diagonal):", "✔" if a_dp == a_dg else "❌")

if __name__ == "__main__":
    main()
```

### How to run

```
python3 lcs_substring.py
ABCDGH
ACDGHR
```

**Example output (timings vary):**

```
s1 (len=6): "ABCDGH"
s2 (len=6): "ACDGHR"

Rolling DP     (O(n*m) time, O(min) space): 4
Time (ms): 0.090

Diagonal scan  (O(n*m) time, O(1)   space): 4
Time (ms): 0.080

Brute force    (O(n*m*L) time)         : 4
Time (ms): 0.410

All methods agree ✔
```

---

## 6) Real-World Use Cases (short & important)

1. **Plagiarism / near-duplicate detection**
   Longest common substring length is a strong signal of shared contiguous text between documents.

2. **DNA/protein sequence analysis**
   Finding longest exact matching segments across sequences (e.g., shared motifs) before applying more sophisticated alignment.

3. **Diff/merge tools**
   As a primitive for aligning lines/characters when computing edits; contiguous matches anchor more robust diffs.

4. **Autocomplete / search ranking**
   Boost exact contiguous matches between user queries and documents or product titles.

5. **Malware signature matching**
   Detecting longest exact byte substrings common between binaries and known signatures for faster candidate filtering.
