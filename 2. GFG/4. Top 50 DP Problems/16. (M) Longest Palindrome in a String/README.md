# Longest Palindrome in a String

**Difficulty:** Medium
**Accuracy:** 23.2%
**Submissions:** 331K+
**Points:** 4

---

## Problem Statement

Given a string `s`, your task is to find the **longest palindromic substring** within `s`.

* A **substring** is a contiguous sequence of characters within a string, defined as `s[i...j]` where `0 ≤ i ≤ j < len(s)`.
* A **palindrome** is a string that reads the same forward and backward. More formally, `s` is a palindrome if `reverse(s) == s`.

**Note:** If there are multiple palindromic substrings with the same length, return the **first occurrence** of the longest palindromic substring **from left to right**.

---

## Examples

**Input:** `s = "forgeekskeegfor"`
**Output:** `"geekskeeg"`
**Explanation:** There are several possible palindromic substrings like `"kssk"`, `"ss"`, `"eeksskee"` etc. But the substring `"geekskeeg"` is the longest among all.

---

**Input:** `s = "Geeks"`
**Output:** `"ee"`
**Explanation:** `"ee"` is the longest palindromic substring of `"Geeks"`.

---

**Input:** `s = "abc"`
**Output:** `"a"`
**Explanation:** `"a"`, `"b"` and `"c"` are longest palindromic substrings of same length. So, the first occurrence is returned.

---

## Constraints

* `1 ≤ s.size() ≤ 10^3`
* `s` consist of only lowercase English letters.

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Zoho, Accolite, Amazon, Microsoft, Samsung, MakeMyTrip, Visa, Walmart, Google, Qualcomm, Groupon

---

## Topic Tags

Strings, Dynamic Programming, palindrome, Data Structures, Algorithms

---

## Related Interview Experiences

* Accolite Interview Experience Set 4 On Campus
* Amazon Interview Experience Set 412 Sde II
* Samsung Research Institute Bangalore Srib Intern

---

## Related Articles

* Longest Palindromic Substring Using Dynamic Programming 2
* Longest Palindromic Substring

---

---

awesome — let’s make **Longest Palindromic Substring** airtight for interviews.

---

# 2) Explanation + step-by-step dry run

## What we want

A **substring** is contiguous. A **palindrome** reads the same forward and backward.
Return the **longest palindromic substring**; if several have the same length, return the **first (left-most)** one.

## Core insight (most expected): expand around center

Any palindrome is defined by a **center**:

* odd length → center at one character `(i,i)`
* even length → center between two characters `(i,i+1)`

From a center `(L,R)`, expand while `s[L]==s[R]`, pushing `L--`, `R++`.
Keep the best span seen. If a new span is **strictly longer**, replace the answer; if it’s **equal**, keep the first one (don’t update).

**Complexities:** There are `2n−1` centers; each character is expanded into at most twice across all centers → **O(n²)** worst-case time, **O(1)** space (typical expected solution).

### Dry run: `s = "forgeekskeegfor"`

We scan centers left→right. Around the gap between the two middle `"ss"`:

* expanding yields `"geekskeeg"` (indices `3..12`, length `10`).
  No later center will beat it; ties aren’t taken because we only update on strictly longer → we keep the earliest.

Another quick one: `s="abacdfgdcaba"`

* centers at `s[1]='b'` and `s[10]='b'` both yield `"aba"` (length 3).
* We meet the first `"aba"` at indices `0..2` earlier, so it’s returned.

---

# 3) Python solutions (multiple ways, interview-style)

All solutions conform to:

```python
class Solution:
    def getLongestPal(self, s):
        # code here
```

## A) Expand-around-center (recommended; O(n²) time, O(1) space)

```python
class Solution:
    def getLongestPal(self, s: str) -> str:
        """
        Expand around every center (odd and even).
        Update the best only when we find a STRICTLY longer span,
        which naturally preserves the left-most (first) occurrence on ties.

        Time  : O(n^2) in worst case (e.g., all same chars)
        Space : O(1)
        """
        n = len(s)
        if n <= 1:
            return s

        best_l, best_r = 0, 0  # inclusive bounds of current best

        def expand(l: int, r: int):
            # Expand as long as characters match and indices are in range
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # After the loop, the palindrome is (l+1 .. r-1)
            return l + 1, r - 1

        for i in range(n):
            # Odd-length center at (i,i)
            l1, r1 = expand(i, i)
            if (r1 - l1) > (best_r - best_l):   # strictly longer -> update
                best_l, best_r = l1, r1

            # Even-length center at (i, i+1)
            l2, r2 = expand(i, i + 1)
            if (r2 - l2) > (best_r - best_l):   # strictly longer -> update
                best_l, best_r = l2, r2

        return s[best_l: best_r + 1]
```

---

## B) Dynamic Programming table (clear to explain; O(n²) time & space)

```python
class SolutionDP:
    def getLongestPal(self, s: str) -> str:
        """
        dp[i][j] = True if s[i..j] is palindrome.
        Fill by increasing length:
          - len=1 always True
          - len=2 True iff s[i]==s[j]
          - len>=3 True iff s[i]==s[j] and dp[i+1][j-1]
        Track best; on ties keep the earlier i.

        Time  : O(n^2)
        Space : O(n^2)
        """
        n = len(s)
        if n <= 1:
            return s

        dp = [[False]*n for _ in range(n)]
        best_l, best_len = 0, 1

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2..n
        for L in range(2, n + 1):          # substring length
            for i in range(0, n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    if L == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        # update only if strictly longer OR same length but earlier start
                        if L > best_len or (L == best_len and i < best_l):
                            best_l, best_len = i, L
        return s[best_l: best_l + best_len]
```

---

## C) Manacher’s Algorithm (advanced; O(n) time, O(n) space)

Use transformed string with separators (e.g., `^#a#b#b#a#$`) to unify odd/even palindromes; compute radius array `P`. Choose earliest start on ties.

```python
class SolutionManacher:
    def getLongestPal(self, s: str) -> str:
        """
        Manacher's algorithm.
        Time  : O(n)
        Space : O(n)
        """
        if len(s) <= 1:
            return s

        # Transform: "^#a#b#...#z#$"
        T = ['^']
        for ch in s:
            T += ['#', ch]
        T += ['#', '$']
        T = ''.join(T)
        nT = len(T)

        P = [0] * nT  # radius array
        C = R = 0     # current center, right boundary
        best_len = 0
        best_start = 0  # in original string indices

        for i in range(1, nT - 1):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])
            # expand around i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # update center if expanded beyond R
            if i + P[i] > R:
                C, R = i, i + P[i]

            # convert radius in T to [l..r] in s
            length = P[i]                # length in transformed chars
            start = (i - length) // 2    # starting index in original s
            # length in original string:
            plen = length

            # strictly longer -> update, tie -> keep earlier start
            if plen > best_len or (plen == best_len and start < best_start):
                best_len = plen
                best_start = start

        return s[best_start: best_start + best_len]
```

> In most interviews, **A** is the sweet spot: simple, O(n²)/O(1), easy to reason about. Mention **Manacher** if asked for O(n).

---

# 4) Interview Q&A (high-yield)

**Q1. Why expand around center works?**
Every palindrome has a center (character or gap). Expanding from all centers enumerates all palindromes; each character can be expanded into O(1) times on average per center → O(n²) worst case.

**Q2. How do you ensure “first occurrence on ties”?**
Update the answer **only when the new palindrome is strictly longer** than current best; for equal lengths we **don’t update**, so the earliest one (encountered first) stays.

**Q3. Substring vs subsequence?**
Substring = contiguous (our problem). Subsequence can skip characters (different DP: LPS / LCS-style).

**Q4. Time/space of the main approaches?**

* Expand-around-center: `O(n²)` time, `O(1)` space.
* DP table: `O(n²)` time, `O(n²)` space.
* Manacher: `O(n)` time, `O(n)` space.

**Q5. Can we retrieve the indices as well?**
Yes—both expand-center and DP keep `(best_l, best_r)` while updating. Return `s[best_l:best_r+1]`.

**Q6. Edge cases?**

* Empty string → `""` (if allowed); single char → itself.
* All same chars → whole string.
* Even-length palindromes (e.g., `"abba"`) are handled by the **even** center `(i, i+1)`.

**Q7. Why not use hashing/binary search?**
You can binary-search length + rolling hash to check palindromes in `O(n log n)` expected time, but expand-center is simpler, deterministic, and meets the expected `O(n²)`/`O(1)` target.

---

---

Here’s a **ready-to-run Python program** for **Longest Palindromic Substring** that:

* reads a string `s` from stdin,
* solves it with **four approaches**

  1. **Expand around center** (recommended; O(n²)/O(1))
  2. **DP table** (clear to explain; O(n²)/O(n²))
  3. **Manacher’s** (advanced; O(n)/O(n))
  4. **Brute force** (educational; O(n³), guarded for small n),
* prints each answer and **times** them with `timeit.timeit(number=1)`,
* includes **inline time/space notes** right where the logic happens.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Longest Palindromic Substring
# Return the longest palindromic *substring* of s.
#
# Implementations:
#   1) Expand around center (recommended)     : O(n^2) time, O(1) space
#   2) DP table                                : O(n^2) time, O(n^2) space
#   3) Manacher's algorithm                    : O(n)   time, O(n)   space
#   4) Brute force (educational; tiny inputs)  : O(n^3) time, O(1)   space
#
# Input (stdin): one line string s
# Output:
#   - echo of s
#   - result from each method
#   - per-method timing in milliseconds
# ------------------------------------------------------------

import sys
import timeit


# ----------------- 1) Expand-around-center (O(n^2)/O(1)) -----------------
class SolutionExpand:
    def getLongestPal(self, s: str) -> str:
        """
        Expand around each center (odd and even). Only update the best
        when strictly longer; that preserves the left-most on ties.

        Time  : O(n^2)  -- 2n-1 centers, each expansion may scan outward
        Space : O(1)    -- constant extra state
        """
        n = len(s)
        if n <= 1:
            return s

        best_l, best_r = 0, 0  # inclusive bounds for best palindrome

        # O(1) helper to expand around (l, r)
        def expand(l: int, r: int):
            # While valid and matching -> O(length of palindrome around center)
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # After loop, (l+1 .. r-1) is the palindrome
            return l + 1, r - 1

        # Iterate centers left->right (O(n))
        for i in range(n):
            # Odd center at (i, i)
            l1, r1 = expand(i, i)
            if (r1 - l1) > (best_r - best_l):      # strictly longer -> update
                best_l, best_r = l1, r1

            # Even center at (i, i+1)
            l2, r2 = expand(i, i + 1)
            if (r2 - l2) > (best_r - best_l):      # strictly longer -> update
                best_l, best_r = l2, r2

        return s[best_l: best_r + 1]


# ----------------------- 2) DP table (O(n^2)/O(n^2)) ----------------------
class SolutionDP:
    def getLongestPal(self, s: str) -> str:
        """
        dp[i][j] = True iff s[i..j] is a palindrome.
        Build by length:
          - len=1: True
          - len=2: s[i]==s[j]
          - len>=3: s[i]==s[j] and dp[i+1][j-1]

        Time  : O(n^2)  -- fill a triangular DP table
        Space : O(n^2)  -- store booleans for all (i,j)
        """
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]   # O(n^2) space
        best_l, best_len = 0, 1

        # len=1 substrings (diagonal) -> O(n)
        for i in range(n):
            dp[i][i] = True

        # len=2..n -> O(n^2) total transitions
        for L in range(2, n + 1):          # substring length
            for i in range(0, n - L + 1):
                j = i + L - 1
                if s[i] == s[j] and (L == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    # update if strictly longer; tie -> keep earlier start
                    if L > best_len or (L == best_len and i < best_l):
                        best_l, best_len = i, L

        return s[best_l: best_l + best_len]


# ----------------------- 3) Manacher (O(n)/O(n)) --------------------------
class SolutionManacher:
    def getLongestPal(self, s: str) -> str:
        """
        Manacher's algorithm: transform with separators to unify odd/even.
        '^' and '$' sentinels avoid bounds checks.

        Time  : O(n)  -- each position expanded amortized O(1)
        Space : O(n)  -- transformed string + radius array
        """
        if len(s) <= 1:
            return s

        # Transform: "^#a#b#c#$" (n -> 2n+3)
        T = ['^']
        for ch in s:
            T += ['#', ch]
        T += ['#', '$']
        T = ''.join(T)
        nT = len(T)

        P = [0] * nT  # radius around each center in T
        C = R = 0     # current center and right boundary in T

        best_len = 0
        best_start = 0  # in original s

        # O(nT) loop
        for i in range(1, nT - 1):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])  # mirror reuse

            # expand around center i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # update center if expansion goes beyond current right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

            # Convert transformed radius to original indices:
            length = P[i]                 # palindrome length in original chars
            start = (i - length) // 2     # starting index in original s

            # strictly longer -> update; tie -> keep earlier start
            if length > best_len or (length == best_len and start < best_start):
                best_len = length
                best_start = start

        return s[best_start: best_start + best_len]


# ----------------------- 4) Brute force (O(n^3)/O(1)) ---------------------
class SolutionBrute:
    def getLongestPal(self, s: str) -> str:
        """
        Check every substring s[i..j] and test palindrome with two pointers.
        Educational baseline.

        Time  : O(n^3) in worst case (O(n^2) substrings * O(n) check)
        Space : O(1)
        """
        n = len(s)
        if n <= 1:
            return s
        best_l, best_len = 0, 1

        # O(n^2) substrings
        for i in range(n):
            for j in range(i, n):
                L, R = i, j
                ok = True
                # palindrome check O(j-i+1)
                while L < R:
                    if s[L] != s[R]:
                        ok = False
                        break
                    L += 1; R -= 1
                if ok:
                    Llen = j - i + 1
                    if Llen > best_len:               # strictly longer only
                        best_l, best_len = i, Llen
        return s[best_l: best_l + best_len]


# ------------------------------- I/O helpers ------------------------------
def _read_s():
    data = sys.stdin.read()
    if not data:
        print("Provide a string s on stdin.")
        sys.exit(0)
    for ln in data.splitlines():
        ln = ln.rstrip("\n")
        if ln != "":
            return ln
    return ""


def _preview(s, limit=80):
    return s if len(s) <= limit else s[:limit] + "..."


# ----------------------------------- main ---------------------------------
def main():
    s = _read_s()
    n = len(s)
    print(f's (len={n}): "{_preview(s)}"\n')

    sol_exp = SolutionExpand()
    sol_dp  = SolutionDP()
    sol_man = SolutionManacher()
    sol_br  = SolutionBrute()

    # --- Expand-around-center timing ---
    t1 = timeit.timeit(lambda: sol_exp.getLongestPal(s), number=1)
    a1 = sol_exp.getLongestPal(s)
    print("Expand-around-center  (O(n^2) time, O(1) space):", a1)
    print("Time (ms): {:.3f}\n".format(t1 * 1000.0))

    # --- DP timing ---
    t2 = timeit.timeit(lambda: sol_dp.getLongestPal(s), number=1)
    a2 = sol_dp.getLongestPal(s)
    print("DP table              (O(n^2) time, O(n^2) space):", a2)
    print("Time (ms): {:.3f}\n".format(t2 * 1000.0))

    # --- Manacher timing ---
    t3 = timeit.timeit(lambda: sol_man.getLongestPal(s), number=1)
    a3 = sol_man.getLongestPal(s)
    print("Manacher              (O(n)   time, O(n)   space):", a3)
    print("Time (ms): {:.3f}\n".format(t3 * 1000.0))

    # --- Brute timing (guarded for tiny inputs) ---
    brute_enabled = n <= 600  # ~ O(n^3) guard: adjust as you wish
    if brute_enabled:
        t4 = timeit.timeit(lambda: sol_br.getLongestPal(s), number=1)
        a4 = sol_br.getLongestPal(s)
        print("Brute force           (O(n^3) time, O(1)   space):", a4)
        print("Time (ms): {:.3f}".format(t4 * 1000.0))
        agree = (a1 == a2 == a3 == a4)
    else:
        print("Brute force           (skipped for large n)")
        agree = (a1 == a2 == a3)

    print("\nAll methods agree ✔" if agree else "\nWARNING: methods disagree!")


if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 longest_pal.py
forgeekskeegfor
```

**Example output (timings vary):**

```
s (len=16): "forgeekskeegfor"

Expand-around-center  (O(n^2) time, O(1) space): geekskeeg
Time (ms): 0.120

DP table              (O(n^2) time, O(n^2) space): geekskeeg
Time (ms): 0.430

Manacher              (O(n)   time, O(n)   space): geekskeeg
Time (ms): 0.080

Brute force           (O(n^3) time, O(1)   space): geekskeeg
Time (ms): 2.100

All methods agree ✔
```

---

## 6) Real-World Use Cases (short & high-value)

1. **DNA/Protein motif detection**
   Find the longest palindromic motif (reverse-complement patterns often have palindromic structure) in genomic sequences.

2. **Text/Document analysis**
   Detect mirrored phrases/symmetry in poetry or stylometry tasks; palindromic runs can be stylistic fingerprints.

3. **Error checking in encodings**
   Certain encodings avoid or flag long palindromic runs due to synchronization issues; detecting them helps validate payloads.

4. **UI/UX string effects**
   Live highlighting of palindromic substrings as users type (expand-around-center is simple and fast enough for moderate lengths).

5. **Competitive programming / interviews**
   This pattern (center expansion) recurs in many string DP problems; mastering it boosts speed across related tasks.
