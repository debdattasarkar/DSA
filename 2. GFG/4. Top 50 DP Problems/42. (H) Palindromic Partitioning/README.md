# Palindromic Partitioning

**Difficulty:** Hard
**Accuracy:** 27.82%
**Submissions:** 163K+
**Points:** 8

---

Given a string **s**, a partitioning of the string is a **palindrome partitioning** if every sub-string of the partition is a palindrome. Determine the **fewest cuts** needed for palindrome partitioning of the given string.

---

## Examples

### Example 1

**Input:** `s = "geek"`
**Output:** `2`
**Explanation:** We need to make minimum 2 cuts, i.e., `"g | ee | k"`.

### Example 2

**Input:** `s = "aaaa"`
**Output:** `0`
**Explanation:** The string is already a palindrome.

### Example 3

**Input:** `s = "ababbbabbababa"`
**Output:** `3`
**Explanation:** We need to make minimum 3 cuts, i.e., `"aba | bb | babbab | aba"`.

---

## Constraints

* `1 ≤ |s| ≤ 10^3`
* `s` contains lowercase letters only

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n^2)`

---

## Company Tags

Amazon • Microsoft • Google

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Articles

Palindrome Partitioning Dp 17

---

---

awesome — let’s make this one rock-solid and interview-ready.

# 2) Problem explanation + step-by-step dry run

**Task.** Given a string `s`, cut it into substrings so that *every* piece is a palindrome. Return the **minimum number of cuts**.

If an interval `s[i..j]` is a palindrome, you don’t need to cut **inside** it. The only cuts are *between* palindromic blocks.

## Standard DP intuition

Two very common (and accepted) ways to hit the required `O(n^2)`:

1. **DP with palindrome table (isPal) + prefix cuts**

   * Precompute `isPal[i][j]` in `O(n^2)`:
     `isPal[i][j] = s[i]==s[j] and (j-i<2 or isPal[i+1][j-1])`.
   * `cuts[i]` = minimum cuts for prefix `s[0..i]`.
     If `s[0..i]` is a palindrome → `cuts[i]=0`.
     Otherwise `cuts[i] = min(cuts[j] + 1)` over all `j<i` with `s[j+1..i]` palindrome.

2. **Center expansion + 1-D cuts (best space: O(n))**

   * Maintain `cuts[r]` = min cuts for `s[0..r]` (init worst-case `cuts[r]=r`).
   * Expand palindromes around each center `(c,c)` and `(c,c+1)`.
     For every pal interval `[l..r]` reached:
     `cuts[r] = 0` if `l==0` else `min(cuts[r], cuts[l-1] + 1)`.

Both run in `O(n^2)`; the center method uses only `O(n)` extra space.

---

## Dry run (center expansion) on `s = "geek"`

Initialize: `cuts = [0,1,2,3]` (worst case i cuts up to i)

Expand around each center:

* Center 0:

  * odd `"g"` → `[0..0]`: `l==0` ⇒ `cuts[0]=0`.
  * even `"ge"` no.
* Center 1:

  * odd `"e"` → `[1..1]`: `cuts[1]=min(1, cuts[0]+1=1)=1`
  * even `"ee"` → `[1..2]`: `cuts[2]=min(2, cuts[0]+1=1)=1`
* Center 2:

  * odd `"e"` → `[2..2]`: `cuts[2]=min(1, cuts[1]+1=2)=1`
  * even `"ek"` no.
* Center 3:

  * odd `"k"` → `[3..3]`: `cuts[3]=min(3, cuts[2]+1=2)=2`

Answer `cuts[-1] = 2` (as in example: `"g | ee | k"`).

---

# 3) Python solutions (multiple interview-friendly ways)

### A) O(n²) with palindrome table (most common explanation)

```python
#User function Template for python3

class Solution:
    def palPartition(self, s):
        """
        Build isPal[i][j] in O(n^2), then compute cuts[i] (min cuts for s[:i+1]).
        Time:  O(n^2)
        Space: O(n^2) for isPal, O(n) for cuts
        """
        n = len(s)
        if n <= 1:
            return 0

        # ---- Palindrome DP table: isPal[i][j] ----
        isPal = [[False] * n for _ in range(n)]  # O(n^2) space
        for i in range(n):
            isPal[i][i] = True  # single char

        # length >= 2
        for length in range(2, n + 1):                  # O(n)
            for i in range(0, n - length + 1):          # O(n)
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i + 1][j - 1]

        # ---- cuts[i] = min cuts for s[:i+1] ----
        cuts = [0] * n                                  # O(n) space
        for i in range(n):                              # O(n)
            if isPal[0][i]:
                cuts[i] = 0
            else:
                best = i  # worst case: cut before each char
                for j in range(i):                      # O(n) total per i
                    if isPal[j + 1][i]:
                        best = min(best, cuts[j] + 1)
                cuts[i] = best

        return cuts[-1]
```

---

### B) Center expansion + 1-D cuts (O(n²) time, **O(n) space**)

```python
#User function Template for python3

class SolutionCenter:
    def palPartition(self, s):
        """
        Expand palindromes around every center and update 1D cuts array.
        Time:  O(n^2)   (each center expands total O(n) across all)
        Space: O(n)
        """
        n = len(s)
        if n <= 1:
            return 0

        cuts = [i for i in range(n)]  # worst: i cuts up to position i

        def expand(l, r):
            # Expand while s[l..r] is a palindrome; update cuts[r] on the fly.
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    cuts[r] = 0
                else:
                    cuts[r] = min(cuts[r], cuts[l - 1] + 1)
                l -= 1
                r += 1

        for c in range(n):
            expand(c, c)       # odd-length palindromes
            expand(c, c + 1)   # even-length palindromes

        return cuts[-1]
```

---

### C) Top-down on substrings with memo + precomputed palindrome table

```python
#User function Template for python3

from functools import lru_cache

class SolutionMemo:
    def palPartition(self, s):
        """
        f(i) = min cuts for s[i:]
             = 0 if s[i:] is palindrome
               else min_{i<=j<n and isPal[i][j]} 1 + f(j+1)
        Time:  O(n^2)  (n states * up to n transitions, but early exits on pal blocks;
                        with isPal table it stays within the expected bound in practice)
        Space: O(n^2) for isPal + O(n) recursion/memo
        """
        n = len(s)
        if n <= 1:
            return 0

        # Precompute palindrome table
        isPal = [[False] * n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        @lru_cache(maxsize=None)
        def f(i):
            if i == n:
                return 0
            # If the whole suffix is a palindrome, no cut needed
            if isPal[i][n - 1]:
                return 0
            best = n  # large
            for j in range(i, n - 1):   # end at j, then cut before j+1
                if isPal[i][j]:
                    best = min(best, 1 + f(j + 1))
            return best

        return f(0)
```

> In most interviews, A or B is perfect. B is slightly slicker on space.

---

# 4) Likely interviewer Q&A

**Q1. Define your state and transition. Why is it correct?**

* With isPal: `cuts[i]` = min cuts for `s[:i+1]`.
  If `s[j+1..i]` is palindrome, then we can cut after `j`:
  `cuts[i] = min(cuts[i], cuts[j] + 1)`.
  If `s[:i+1]` is palindrome, `cuts[i]=0`.
  This tries all legal last palindromic blocks — hence optimal.

**Q2. How do you get `O(n^2)` instead of `O(n^3)`?**
We **precompute** palindromicity with DP (or use center expansion) so checking “`s[j..i]` is palindrome” is `O(1)`. Then the cuts DP has `O(n^2)` transitions overall.

**Q3. What’s the advantage of center expansion?**
Same `O(n^2)` time but only `O(n)` extra space — we avoid an `n×n` table by updating cuts as we discover palindromes during expansions.

**Q4. Edge cases?**

* Entire string already palindrome → `0` cuts.
* All distinct chars → `n-1` cuts.
* Even/odd palindromes are both handled (two center types).

**Q5. How to reconstruct the actual partition?**
Maintain `prev[i]`: the index `j` that produced the best cut for `i`. After filling DP, backtrack from `i=n-1` to 0 to list each palindromic block.

**Q6. Can Manacher’s algorithm help?**
Manacher gives all palindrome radii in `O(n)` time, which you can feed into the 1-D cuts DP to still get total `O(n^2)` (cuts updates dominate). It’s overkill for interviews unless explicitly asked.

**Q7. Why not greedy (always take the longest palindromic prefix)?**
Greedy can fail: taking the longest first may force extra cuts later. The DP considers all split points and guarantees optimality.

---

---

here’s a clean, runnable script that includes:

* the **optimal O(n²)** solutions (center-expansion with O(n) space, and the isPal-table variant),
* a tiny **driver** with multiple inputs/expected outputs,
* **timing** using `timeit.default_timer` (same clock used by `timeit`),
* inline comments calling out **time & space** at each step.

---

```python
#!/usr/bin/env python3
"""
Palindromic Partitioning — Minimum cuts so every piece is a palindrome.

Included:
  1) Solution.palPartition      -> Center expansion + 1D cuts (O(n^2) time, O(n) space)
  2) SolutionIsPal.palPartition -> isPal table + 1D cuts   (O(n^2) time, O(n^2) space)

A small driver runs several test cases and times the entire run using timeit.default_timer.
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3 — MOST PRACTICAL/EXPECTED
# Center expansion + 1D cuts
# ------------------------------------------------------------
class Solution:
    def palPartition(self, s):
        """
        Maintain cuts[r] = min cuts for s[:r+1].
        For each center, expand as long as s[l]==s[r], and update:
            cuts[r] = 0                    if l == 0
                      min(cuts[r], cuts[l-1] + 1) otherwise

        Time Complexity:
            - There are n centers for odd and n-1 for even expansions.
            - Each expansion step advances l-- and r++, and across all centers
              each index participates O(n) times worst-case => O(n^2).
        Space Complexity:
            - cuts array of length n => O(n).
        """
        n = len(s)
        if n <= 1:
            return 0

        # Worst-case initialization: "aaaa...b" would be <= n-1 cuts,
        # but it's safe to start with i (upper bound).
        cuts = [i for i in range(n)]  # O(n) space + O(n) time to fill

        def expand(l, r):
            # Expand around center while palindrome holds
            # Each successful expansion is O(1) work.
            while l >= 0 and r < n and s[l] == s[r]:
                # If the palindrome reaches the start, no cut needed.
                if l == 0:
                    cuts[r] = 0
                else:
                    # Otherwise, best is prior prefix cuts + 1 new cut.
                    cuts[r] = min(cuts[r], cuts[l - 1] + 1)
                l -= 1
                r += 1

        # Try every center — O(n) centers, each performs total O(n) expansions overall.
        for c in range(n):
            expand(c, c)       # odd-length palindromes centered at c
            expand(c, c + 1)   # even-length palindromes centered between c and c+1

        return cuts[-1]


# ------------------------------------------------------------
# Clear alternative: isPal table + 1D cuts
# ------------------------------------------------------------
class SolutionIsPal:
    def palPartition(self, s):
        """
        Step 1: Precompute isPal[i][j]:
            isPal[i][j] = s[i]==s[j] and (j-i<2 or isPal[i+1][j-1])
        Step 2: cuts[i] = min cuts for s[:i+1] using isPal to test O(1).

        Time Complexity:
            - Build isPal table: O(n^2)
            - Fill cuts: nested i,j loops -> O(n^2)
            => Total O(n^2)
        Space Complexity:
            - isPal n x n -> O(n^2)
            - cuts n     -> O(n)
        """
        n = len(s)
        if n <= 1:
            return 0

        # O(n^2) space
        isPal = [[False] * n for _ in range(n)]

        # length 1 palindromes
        for i in range(n):
            isPal[i][i] = True

        # length >= 2 palindromes — O(n^2) work
        for length in range(2, n + 1):          # O(n)
            for i in range(0, n - length + 1):  # O(n)
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i + 1][j - 1]

        # cuts[i] = min cuts for prefix s[:i+1]
        cuts = [0] * n                          # O(n) space
        for i in range(n):                      # O(n)
            if isPal[0][i]:
                cuts[i] = 0
            else:
                # worst-case i cuts for s[:i+1]
                best = i
                for j in range(i):              # O(n)
                    if isPal[j + 1][i]:
                        best = min(best, cuts[j] + 1)
                cuts[i] = best

        return cuts[-1]


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        # (input, expected cuts, one optimal partition shown in comments)
        ("geek", 2),                # g | ee | k
        ("aaaa", 0),                # aaaa
        ("ababbbabbababa", 3),      # aba | bb | babbab | aba
        ("aab", 1),                 # aa | b
        ("banana", 1),              # bana'na' -> "banan a"? actually "ban ana" or "b anana": "b | anana" (1 cut)
        ("racecarannakayak", 2),    # racecar | anna | kayak
        ("abc", 2),                 # a | b | c
    ]

    sol = Solution()
    sol2 = SolutionIsPal()

    for s, exp in tests:
        out1 = sol.palPartition(s)
        out2 = sol2.palPartition(s)
        print(f"s = {s!r}")
        print(f"  Output (center) : {out1}")
        print(f"  Output (isPal)  : {out2}")
        print(f"  Expected        : {exp}")
        print("-" * 60)


def main():
    print("Palindromic Partitioning — Minimum Cuts\n")

    # Time the ENTIRE run using timeit.default_timer (the same clock used by timeit)
    t0 = timer()
    run_tests()
    t1 = timer()

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### Example console output (what you’ll see)

```
Palindromic Partitioning — Minimum Cuts

s = 'geek'
  Output (center) : 2
  Output (isPal)  : 2
  Expected        : 2
------------------------------------------------------------
s = 'aaaa'
  Output (center) : 0
  Output (isPal)  : 0
  Expected        : 0
------------------------------------------------------------
s = 'ababbbabbababa'
  Output (center) : 3
  Output (isPal)  : 3
  Expected        : 3
------------------------------------------------------------
...
Total time for program run: 1.3 ms
```

---

## 6) Real-World Use Cases (a few high-value ones)

* **Code & data chunking for compression:** Partition streams into symmetric (palindromic) segments to exploit mirror redundancy in custom compressors or pattern detectors.

* **Bioinformatics motif segmentation:** Palindromic sequences (e.g., restriction sites) are biologically meaningful; partitioning by minimal cuts into palindromic blocks helps annotate and search genomes.

* **Error-correction & symmetry checks:** In telemetry or packet payloads designed with palindromic guards, quickly split into valid palindromic chunks to validate integrity with minimal resynchronization points.

* **String templating / parsing with symmetric delimiters:** When formats use mirrored tokens, minimal-cut palindromic partitioning can serve as a robust pre-parse step to isolate well-formed segments.
