# Minimum times A has to be repeated such that B is a substring of it

**Difficulty:** Medium
**Accuracy:** 47.6%
**Submissions:** 17K+
**Points:** 4

---

## Problem Statement

Given two strings **A** and **B**. Find the **minimum number of times** A has to be **repeated** such that **B is a substring** of it.
If **B** can never be a substring then return **-1**.

---

## Examples

### Example 1

**Input:**
A = `"abcd"`
B = `"cdabcdab"`
**Output:** `3`
**Explanation:** Repeating A three times (`"abcdabcdabcd"`), B is a substring of it. B is not a substring of A when it is repeated less than 3 times.

### Example 2

**Input:**
A = `"ab"`
B = `"cab"`
**Output:** `-1`
**Explanation:** No matter how many times we repeat A, we can't get a string such that B is a substring of it.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`minRepeats()`** which takes 2 strings **A** and **B** respectively and returns the **minimum number of times A has to be repeated** such that B is a substring of it. **Return -1 if it's not possible.**

---

## Expected Complexities

* **Time Complexity:** `O(|A| * |B|)`
* **Expected Auxiliary Space:** `O(|B|)`

---

## Constraints

* `1 ≤ |A|, |B| ≤ 10^3`
* String **A** and **B** consist of **lower case alphabets**.

---

## Company Tags

Google

---

## Topic Tags

Searching, Strings, Pattern Searching, Data Structures, Algorithms

---

## Related Interview Experiences

* Google Interview Experience Set 7 Software Engineering Intern

---

## Related Articles

* [Minimum Number Of Times A Has To Be Repeated Such That B Is A Substring Of It](https://www.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/)


---

---

Here’s an interview-ready bundle for **“Minimum times A has to be repeated such that B is a substring of it.”**

---

## 2) Explanation + step-by-step dry run

### Core idea

Let `n = len(A)`, `m = len(B)`.
If `B` is a substring of `A` repeated some number of times, then it must appear **entirely inside**:

* `A` repeated `k = ceil(m / n)` times (enough total length to cover `B`), **or**
* one more copy (to handle when `B` starts near the end of some `A` and spills into the next).

Hence we only need to test **`k`** and **`k + 1`** repeats.
(Equivalently: make a string of length at least `m` and at most `m + n`, and check membership once or twice.)

If neither contains `B`, return **`-1`**.

### Dry run 1

`A="abcd"`, `B="cdabcdab"`, `n=4`, `m=8`, `k=ceil(8/4)=2`

* `A*k = "abcdabcd"` → does **not** contain `B`
* `(A*(k+1)) = "abcdabcdabcd"` → **contains** `"cdabcdab"` (starts at index 2)
  Answer: **3**.

### Dry run 2

`A="ab"`, `B="cab"`, `n=2`, `m=3`, `k=ceil(3/2)=2`

* `"abab"` → no `"cab"`
* `"ababab"` → still no `"cab"`
  Answer: **-1**.

---

## 3) Python solutions (optimized + alternatives)

### A) Minimal, interview-standard (test `k` and `k+1`) — **O(|A| + |B|)** average

```python
# User function Template for python3

import math

class Solution:
    def minRepeats(self, A, B):
        """
        Repeat A just enough to cover B, then one more time for overlap.
        Check substring membership using Python's 'in' (efficient under the hood).

        Let n = len(A), m = len(B), k = ceil(m / n).
        Time : O(n * k + m) overall for building + membership (amortized ~ O(m))
        Space: O(n * k) to hold the repeated string (up to m + n chars)
        """
        n, m = len(A), len(B)
        # Quick impossible check (optional micro-optimization):
        # if any char in B not in A, early -1 (not sufficient but prunes many)
        if set(B) - set(A):
            return -1

        k = (m + n - 1) // n            # ceil(m / n)
        s = A * k
        if B in s:
            return k
        s += A                           # one more repeat to catch wrap-around
        if B in s:
            return k + 1
        return -1
```

### B) “Grow until long enough” — same idea, no math needed

```python
class SolutionGrow:
    def minRepeats(self, A, B):
        """
        Keep appending A until length >= len(B), then check once more append.
        Time : O(m + n) for building + membership
        Space: O(m + n)
        """
        if set(B) - set(A):
            return -1
        rep = 1
        s = A
        while len(s) < len(B):
            s += A
            rep += 1
        if B in s:
            return rep
        s += A
        if B in s:
            return rep + 1
        return -1
```

### C) KMP search on at-most `m + n` text (explicit pattern matching) — **O(m + (m+n))**

```python
class SolutionKMP:
    def _lps(self, pat: str):
        """Build LPS array for KMP. Time O(len(pat)), Space O(len(pat))."""
        lps = [0]*len(pat)
        i = 1
        ln = 0
        while i < len(pat):
            if pat[i] == pat[ln]:
                ln += 1
                lps[i] = ln
                i += 1
            elif ln:
                ln = lps[ln - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    def minRepeats(self, A: str, B: str) -> int:
        """
        Build T = A repeated until len(T) >= len(B) and <= len(B)+len(A),
        then KMP-search B in T; return repeats if found, else -1.
        Time : O(len(B) + len(T))  Space: O(len(B))
        """
        if set(B) - set(A):
            return -1

        # Build text T with length in [m, m+n]
        T = A
        rep = 1
        while len(T) < len(B):
            T += A
            rep += 1
        if len(T) < len(B) + len(A):
            T += A
            rep += 1

        # KMP: search B in T
        lps = self._lps(B)
        i = j = 0
        while i < len(T):
            if T[i] == B[j]:
                i += 1; j += 1
                if j == len(B):  # found
                    # How many copies were actually used?
                    # index i-1 is last char of match
                    used = (i + len(A) - 1) // len(A)
                    return used
            else:
                if j:
                    j = lps[j-1]
                else:
                    i += 1
        return -1
```

### D) Naive check (educational baseline)

Brute-force build `S = A` and keep appending `A` while length < `m + n`; each time do a **naive substring check** (two nested loops).
Time is **O((m+n) \* m)** worst-case. In interviews, prefer **A** or **C**.

---

## 4) Interviewer-style Q\&A

**Q1. Why is checking only `ceil(m/n)` and `ceil(m/n)+1` repeats sufficient?**
Because any occurrence of `B` in repeated copies of `A` either:

* fits entirely within `k = ceil(m/n)` copies (total length ≥ m), or
* starts near the end of one copy and ends in the next → needs **one extra** copy at most.
  No alignment can require more than one extra copy.

**Q2. What’s the overall complexity?**
Using approach **A**: building strings up to size `≤ m + n`, and substring test (`in`) is linear w\.r.t. text+pattern on average → **O(m + n)** time, **O(m + n)** space.

**Q3. When can we early-return `-1`?**
If `B` contains any character not appearing in `A` at all (quick set check). Not sufficient in theory, but it prunes obvious impossibilities.

**Q4. Why might KMP be preferred?**
If you want a deterministic **O(m + n)** substring search and to avoid relying on language-specific `in` implementation, or if you’re asked to implement pattern matching explicitly.

**Q5. Do we ever need `k+2` repeats?**
No. At most one extra copy beyond `ceil(m/n)` is enough: the match can start anywhere inside the last copy and extend at most `n-1` characters past its end—one more copy covers that entire overhang.

**Q6. Edge cases to test?**

* `B` already inside `A` → answer `1`.
* `A` and `B` same string → `1`.
* `B` much longer than `A` → should return `k` or `k+1`.
* Repetitive patterns (e.g., `A="aa"`, `B="aaaaa"` → `3`).
* Impossible misalignment (e.g., `A="ab"`, `B="baaa"` → `-1`).

---

---

Absolutely — here’s a **full, runnable Python program** for **“Minimum times A has to be repeated such that B is a substring of it”** that:

* implements the expected interview solution,
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the algorithm using `timeit` right in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Minimum times A must be repeated so that B is a substring.

Algorithm (interview-standard):
  Let n=len(A), m=len(B).
  If B appears in A repeated k = ceil(m/n) times, return k.
  Else if B appears in A repeated k+1 times, return k+1.
  Otherwise, return -1.

Rationale: Any match of B in A^∞ must fall entirely within a window of size
[m, m+n] of A's repetitions (enough to cover B + at most one extra A for overlap).

Complexities:
  Build string up to length ≤ (m + n), and do at most two membership checks.
  • Time  : O(m + n) average (substring check linear to text+pattern)
  • Space : O(m + n) to hold the repeated string
"""

from __future__ import annotations
import random
import timeit
from typing import List


# -------------------------------------------------------------------
# User function Template for python3
# -------------------------------------------------------------------
class Solution:
    def minRepeats(self, A: str, B: str) -> int:
        """
        Repeat A just enough to cover B, then one extra time for overlap.

        Steps (with local time/space notes):
          A) Guard/set pruning: if B uses a char not in A -> impossible  -> O(|A|+|B|) set build
          B) k = ceil(m/n)                                          -> O(1)
          C) s = A * k      (length ≤ m)                             -> O(m)   time/space
             if B in s: return k                                    -> O(m) average check
          D) s += A         (length ≤ m+n)                           -> O(n)   time/space
             if B in s: return k+1                                  -> O(m+n) average check
          E) else return -1                                         -> O(1)

        Overall: Time O(m + n), Space O(m + n)
        """
        n, m = len(A), len(B)

        # A) optional quick prune; not sufficient but kills obvious impossibilities
        if set(B) - set(A):
            return -1

        # B) minimum repeats to reach length ≥ m
        k = (m + n - 1) // n

        # C) try exactly k repeats
        s = A * k
        if B in s:
            return k

        # D) one extra repeat to cover overlap across a boundary
        s += A
        if B in s:
            return k + 1

        # E) not possible
        return -1


# --------------------------- Demo & Benchmark ---------------------------

def demo_on_samples() -> None:
    """
    Demonstrate correctness on a few inputs.
    Total time is tiny; each call runs in O(|A|+|B|). Space per case O(|A|+|B|).
    """
    samples = [
        # From prompt
        ("abcd", "cdabcdab", 3),
        ("ab",   "cab",     -1),
        # Easy cases
        ("abc",  "abc",      1),
        ("a",    "aaaaa",    5),
        # Overlap-required case (needs k+1)
        ("abcd", "dabcdab",  3),  # "abcdabcdabcd" contains "dabcdab"
        # Random-ish hand checks
        ("aba",  "baab",    -1),
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for A, B, expected in samples:
        out = sol.minRepeats(A, B)  # O(|A|+|B|)
        print(f"A = {A!r}, B = {B!r}")
        print(f"Output  : {out}")
        print(f"Expected: {expected}")
        print("-" * 60)


def _bench_once(A: str, B: str) -> None:
    """
    Helper for timeit: run the algorithm once.
    Measures the full O(|A|+|B|) work (building string + membership).
    """
    Solution().minRepeats(A, B)


def benchmark() -> None:
    """
    Benchmark with timeit.

    We generate one non-trivial case within constraints (|A|,|B| ≤ 1e3):
      - A: random letters from a small alphabet
      - B: random letters from the same alphabet (to avoid early pruning)
    We then call the solver multiple times on the SAME inputs (typical micro-bench).
    """
    rng = random.Random(2025)

    # Build A and B once (outside timing)
    alpha = "abcde"                           # small alphabet keeps membership realistic
    A_len, B_len = 23, 1000                   # within constraints
    A = "".join(rng.choice(alpha) for _ in range(A_len))
    B = "".join(rng.choice(alpha) for _ in range(B_len))

    runs = 500
    total = timeit.timeit(lambda: _bench_once(A, B), number=runs)

    print("=== Benchmark (O(|A|+|B|) per run) ===")
    print(f"|A|={len(A)}, |B|={len(B)}, alphabet={set(A)}")
    print(f"Runs     : {runs}")
    print(f"Total(s) : {total:.6f}")
    print(f"Avg/run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for explicit inputs (includes input values and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (short & important)

1. **Cyclic / periodic streams**
   Determine if a pattern **B** can appear in an infinite repetition of a base frame **A** (e.g., telemetry frames, network beacons), and how many frames are needed before it can occur.

2. **String tiling & template matching**
   When a longer motif must be matched against a **repeating template** (UI patterns, music loops), this check tells you the **minimum loop repeats** required for alignment.

3. **Circular rotation checks**
   For equal lengths (`|A| == |B|`), testing `B in A+A` is the classic **rotation** test. This problem generalizes it to longer B and asks for the **minimal repeats**.

4. **Manufacturing / labeling with periodic codes**
   Verifying a target code **B** can be observed within repeated print cycles of base pattern **A**, and after how many cycles it first becomes observable.

