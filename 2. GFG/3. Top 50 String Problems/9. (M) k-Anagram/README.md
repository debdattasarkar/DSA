# k-Anagram

**Difficulty:** Medium
**Accuracy:** 26.28%
**Submissions:** 72K+
**Points:** 4

---

## Problem Statement

Two strings are called **k-anagrams** if both of the following conditions are true:

1. Both have the **same number of characters**.
2. The two strings can become **anagrams** by **changing at most `k` characters in one of the strings**.

Given two strings of lowercase alphabets and an integer value `k`, determine whether the two strings are **k-anagrams** of each other.

---

## Examples

### Example 1

**Input:** `s1 = "fodr", s2 = "gork", k = 2`
**Output:** `true`
**Explanation:** We can change `'f' → 'g'` and `'d' → 'k'` in `s1`.

---

### Example 2

**Input:** `s1 = "geeks", s2 = "eggkf", k = 1`
**Output:** `false`
**Explanation:** We can update/modify only 1 value but we need to modify **2** characters (e.g., `'g'` and `'f'`) in `s2`.

---

### Example 3

**Input:** `s1 = "adb", s2 = "fdab", k = 2`
**Output:** `false`
**Explanation:** The strings have **different lengths**, so they cannot be k-anagrams.

---

## Constraints

* `1 ≤ s1.size(), s2.size() ≤ 10^5`
* `1 ≤ k ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* `Accolite`, `Amazon`, `Microsoft`, `Google`

---

## Topic Tags

* `Hash`, `Strings`, `Data Structures`

---

## Related Articles

* [Check Two Strings K Anagrams Not](https://www.geeksforgeeks.org/check-two-strings-k-anagrams-not/)

---

---

Here’s a tight, interview-ready guide for **k-Anagram**.

---

## 2) Idea + step-by-step dry run

### What does “k-anagram” mean?

Two strings `s1`, `s2` (lowercase) are **k-anagrams** iff:

1. `len(s1) == len(s2)`, and
2. You can change **at most `k` characters in `s1`** so that `s1` becomes an anagram of `s2`.

### Key observation

The **minimum** number of changes in `s1` needed to match `s2` equals the count of characters that are **extra** in `s1` relative to `s2`.

If `cnt1[c]` and `cnt2[c]` are frequencies, the needed changes are:

```
changes = Σ over letters c of max(0, cnt1[c] - cnt2[c])
```

(Those are exactly the surplus characters in `s1` that must be replaced.)

If `changes <= k` ⇒ `True`, else `False`.

Time: `O(n)`
Space: `O(1)` (26 letters) or `O(Σ alphabet)`.

---

### Dry run (from prompt)

#### Example A

`s1="fodr"`, `s2="gork"`, `k=2`
Counts:

* s1: {f:1, o:1, d:1, r:1}
* s2: {g:1, o:1, r:1, k:1}

Surplus in s1:

* f (1 vs 0) → +1
* d (1 vs 0) → +1
* o (1 vs 1) → 0
* r (1 vs 1) → 0
  `changes = 2` → `changes <= k` → **True**.

#### Example B

`s1="geeks"`, `s2="eggkf"`, `k=1`
Counts:

* s1: g:1, e:2, k:1, s:1
* s2: e:1, g:2, g again: (total g:2), k:1, f:1

Surplus in s1:

* e: max(0, 2−1) = 1
* g: max(0, 1−2) = 0
* k: max(0, 1−1) = 0
* s: max(0, 1−0) = 1
  Total `changes = 2` > `k` → **False**.

#### Example C

`s1="adb"`, `s2="fdab"`, `k=2`
Lengths differ → immediately **False**.

---

## 3) Python solutions (optimized + alternatives)

### A) Optimal counting with fixed alphabet (most expected)

```python
#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        """
        Count surplus letters in s1 relative to s2.
        Time : O(n)   (one pass to count, one pass to compare 26 letters)
        Space: O(1)   (26-int array for lowercase)
        """
        if len(s1) != len(s2):
            return False  # must be same length

        # Frequency arrays for 'a'..'z'
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        base = ord('a')

        for ch in s1:           # O(n)
            cnt1[ord(ch) - base] += 1
        for ch in s2:           # O(n)
            cnt2[ord(ch) - base] += 1

        # Surplus in s1 only
        changes = 0
        for c in range(26):     # O(26) == O(1)
            if cnt1[c] > cnt2[c]:
                changes += cnt1[c] - cnt2[c]

        return changes <= k
```

### B) Clean, dictionary/Counter version (same complexity, easier to read)

```python
from collections import Counter

class SolutionCounter:
    def areKAnagrams(self, s1, s2, k):
        """
        Time : O(n)
        Space: O(Σ alphabet)  (still small)
        """
        if len(s1) != len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2)

        # count surplus occurrences in s1
        changes = 0
        for ch, v in c1.items():
            if v > c2.get(ch, 0):
                changes += v - c2.get(ch, 0)

        return changes <= k
```

### C) “Brute-ish” baseline using multiset consumption (O(n), but conceptually brute)

For each `ch` in `s1`, try to “match” it using `c2` (counts of `s2`). If not found, that’s a change.
(Still O(n), but useful as a clear baseline.)

```python
from collections import Counter

class SolutionGreedy:
    def areKAnagrams(self, s1, s2, k):
        """
        Greedily consume matches from s2's counts; leftover in s1 are changes.
        Time : O(n)
        Space: O(Σ alphabet)
        """
        if len(s1) != len(s2):
            return False

        need = Counter(s2)
        changes = 0
        for ch in s1:
            if need[ch] > 0:
                need[ch] -= 1  # matched with s2
            else:
                changes += 1   # must change this char in s1

        return changes <= k
```

> In interviews, code **A** (array) or **B** (Counter). Mention **C** as an intuitive way to reason about surplus.

---

## 4) Interviewer-style Q\&A

**Q1. Why must the strings have the same length?**
Anagrams are permutations with identical counts; if lengths differ, you can’t reach an anagram with character **replacements only** (no insertions/deletions allowed).

**Q2. Why is the number of needed changes `Σ max(0, cnt1[c] − cnt2[c])`?**
Those are exactly the **extra** occurrences in `s1` that have no counterpart in `s2`; each such extra must be **changed** to some missing character. Changing an extra in `s1` fixes both a surplus and a deficit simultaneously.

**Q3. Is it equivalent to count `Σ max(0, cnt2[c] − cnt1[c])` instead?**
Yes—the totals are equal because both strings have the same length. You can compute either surplus side; both equal the minimum changes.

**Q4. Time/space complexity?**

* Counting approach: **O(n)** time, **O(1)** space for 26 letters (or **O(Σ alphabet)** in general).
* Sorting both strings and comparing would be `O(n log n)` and doesn’t directly give the minimal replace count.

**Q5. What about uppercase / Unicode?**
Use `Counter` (solution **B**). For ASCII lowercase, the 26-bucket array is faster and **O(1)**.

**Q6. Can we decide “change in s2” instead of “in s1”?**
Yes—minimum replacements are symmetric given equal length. The computed minimum is the same.

**Q7. Edge cases?**

* `k >= n` → always True if lengths equal (you could change everything).
* Strings already anagrams → `changes = 0` → True for any `k ≥ 0`.
* Repeated characters and `k = 0` → True only if they’re already anagrams.

---

---

Here’s a tight, interview-ready guide for **k-Anagram**.

---

## 2) Idea + step-by-step dry run

### What does “k-anagram” mean?

Two strings `s1`, `s2` (lowercase) are **k-anagrams** iff:

1. `len(s1) == len(s2)`, and
2. You can change **at most `k` characters in `s1`** so that `s1` becomes an anagram of `s2`.

### Key observation

The **minimum** number of changes in `s1` needed to match `s2` equals the count of characters that are **extra** in `s1` relative to `s2`.

If `cnt1[c]` and `cnt2[c]` are frequencies, the needed changes are:

```
changes = Σ over letters c of max(0, cnt1[c] - cnt2[c])
```

(Those are exactly the surplus characters in `s1` that must be replaced.)

If `changes <= k` ⇒ `True`, else `False`.

Time: `O(n)`
Space: `O(1)` (26 letters) or `O(Σ alphabet)`.

---

### Dry run (from prompt)

#### Example A

`s1="fodr"`, `s2="gork"`, `k=2`
Counts:

* s1: {f:1, o:1, d:1, r:1}
* s2: {g:1, o:1, r:1, k:1}

Surplus in s1:

* f (1 vs 0) → +1
* d (1 vs 0) → +1
* o (1 vs 1) → 0
* r (1 vs 1) → 0
  `changes = 2` → `changes <= k` → **True**.

#### Example B

`s1="geeks"`, `s2="eggkf"`, `k=1`
Counts:

* s1: g:1, e:2, k:1, s:1
* s2: e:1, g:2, g again: (total g:2), k:1, f:1

Surplus in s1:

* e: max(0, 2−1) = 1
* g: max(0, 1−2) = 0
* k: max(0, 1−1) = 0
* s: max(0, 1−0) = 1
  Total `changes = 2` > `k` → **False**.

#### Example C

`s1="adb"`, `s2="fdab"`, `k=2`
Lengths differ → immediately **False**.

---

## 3) Python solutions (optimized + alternatives)

### A) Optimal counting with fixed alphabet (most expected)

```python
#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        """
        Count surplus letters in s1 relative to s2.
        Time : O(n)   (one pass to count, one pass to compare 26 letters)
        Space: O(1)   (26-int array for lowercase)
        """
        if len(s1) != len(s2):
            return False  # must be same length

        # Frequency arrays for 'a'..'z'
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        base = ord('a')

        for ch in s1:           # O(n)
            cnt1[ord(ch) - base] += 1
        for ch in s2:           # O(n)
            cnt2[ord(ch) - base] += 1

        # Surplus in s1 only
        changes = 0
        for c in range(26):     # O(26) == O(1)
            if cnt1[c] > cnt2[c]:
                changes += cnt1[c] - cnt2[c]

        return changes <= k
```

### B) Clean, dictionary/Counter version (same complexity, easier to read)

```python
from collections import Counter

class SolutionCounter:
    def areKAnagrams(self, s1, s2, k):
        """
        Time : O(n)
        Space: O(Σ alphabet)  (still small)
        """
        if len(s1) != len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2)

        # count surplus occurrences in s1
        changes = 0
        for ch, v in c1.items():
            if v > c2.get(ch, 0):
                changes += v - c2.get(ch, 0)

        return changes <= k
```

### C) “Brute-ish” baseline using multiset consumption (O(n), but conceptually brute)

For each `ch` in `s1`, try to “match” it using `c2` (counts of `s2`). If not found, that’s a change.
(Still O(n), but useful as a clear baseline.)

```python
from collections import Counter

class SolutionGreedy:
    def areKAnagrams(self, s1, s2, k):
        """
        Greedily consume matches from s2's counts; leftover in s1 are changes.
        Time : O(n)
        Space: O(Σ alphabet)
        """
        if len(s1) != len(s2):
            return False

        need = Counter(s2)
        changes = 0
        for ch in s1:
            if need[ch] > 0:
                need[ch] -= 1  # matched with s2
            else:
                changes += 1   # must change this char in s1

        return changes <= k
```

> In interviews, code **A** (array) or **B** (Counter). Mention **C** as an intuitive way to reason about surplus.

---

## 4) Interviewer-style Q\&A

**Q1. Why must the strings have the same length?**
Anagrams are permutations with identical counts; if lengths differ, you can’t reach an anagram with character **replacements only** (no insertions/deletions allowed).

**Q2. Why is the number of needed changes `Σ max(0, cnt1[c] − cnt2[c])`?**
Those are exactly the **extra** occurrences in `s1` that have no counterpart in `s2`; each such extra must be **changed** to some missing character. Changing an extra in `s1` fixes both a surplus and a deficit simultaneously.

**Q3. Is it equivalent to count `Σ max(0, cnt2[c] − cnt1[c])` instead?**
Yes—the totals are equal because both strings have the same length. You can compute either surplus side; both equal the minimum changes.

**Q4. Time/space complexity?**

* Counting approach: **O(n)** time, **O(1)** space for 26 letters (or **O(Σ alphabet)** in general).
* Sorting both strings and comparing would be `O(n log n)` and doesn’t directly give the minimal replace count.

**Q5. What about uppercase / Unicode?**
Use `Counter` (solution **B**). For ASCII lowercase, the 26-bucket array is faster and **O(1)**.

**Q6. Can we decide “change in s2” instead of “in s1”?**
Yes—minimum replacements are symmetric given equal length. The computed minimum is the same.

**Q7. Edge cases?**

* `k >= n` → always True if lengths equal (you could change everything).
* Strings already anagrams → `changes = 0` → True for any `k ≥ 0`.
* Repeated characters and `k = 0` → True only if they’re already anagrams.

---

---

Absolutely — here’s a **complete, runnable Python program** for **k-Anagram** that

* implements the optimal **O(n)** counting solution (array of 26 buckets),
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the function using `timeit` right in `main`.

Each step is annotated with **time/space complexity** notes.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
k-Anagram — Full Program with Benchmark
---------------------------------------
Two strings s1 and s2 are k-anagrams if:
  1) len(s1) == len(s2), and
  2) s1 can be turned into an anagram of s2 by changing at most k characters.

Let n = len(s1) = len(s2) when valid.

Primary approach used below (array counting for lowercase a–z):
  Time  : O(n)   — one pass per string to count + O(26) to sum surplus
  Space : O(1)   — two fixed-size arrays of length 26

Also included: a Counter-based variant (same big-O, easier to read).
"""

from __future__ import annotations
from collections import Counter
import random
import string
import timeit
from typing import List


# ---------------------------------------------------------------------
# User function template for Python 3 — Optimal array-count solution
# ---------------------------------------------------------------------
class Solution:
    def areKAnagrams(self, s1: str, s2: str, k: int) -> bool:
        """
        Return True if s1 and s2 are k-anagrams, else False.

        Steps (with complexity):
          A) Length check                          -> O(1)
          B) Build two 26-length freq arrays       -> O(n)
          C) Sum surplus in s1 over s2 (only +ve)  -> O(26) == O(1)
          D) Compare with k                        -> O(1)
        Total: O(n) time, O(1) space.
        """
        # A) Must be same length — O(1)
        if len(s1) != len(s2):
            return False

        # B) Count frequencies using fixed-size arrays — O(n) time, O(1) space
        base = ord('a')
        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for ch in s1:                   # O(n)
            cnt1[ord(ch) - base] += 1
        for ch in s2:                   # O(n)
            cnt2[ord(ch) - base] += 1

        # C) Minimum replacements = sum of surpluses in s1 relative to s2 — O(26)
        changes_needed = 0
        for i in range(26):             # O(1) since alphabet size is fixed
            if cnt1[i] > cnt2[i]:
                changes_needed += cnt1[i] - cnt2[i]

        # D) Decision — O(1)
        return changes_needed <= k


# ---------------------------------------------------------------------
# Alternative readable solution with Counter (same asymptotics)
# ---------------------------------------------------------------------
class SolutionCounter:
    def areKAnagrams(self, s1: str, s2: str, k: int) -> bool:
        if len(s1) != len(s2):              # O(1)
            return False

        c1 = Counter(s1)                    # O(n)
        c2 = Counter(s2)                    # O(n)

        changes_needed = 0
        for ch, v in c1.items():            # O(Σ alphabet) → small
            if v > c2.get(ch, 0):
                changes_needed += v - c2.get(ch, 0)

        return changes_needed <= k


# ---------------------------------------------------------------------
# Demo: show inputs and outputs for a few test cases
# ---------------------------------------------------------------------
def demo_on_samples() -> None:
    sol = Solution()

    samples = [
        ("fodr",  "gork", 2, True),
        ("geeks", "eggkf", 1, False),
        ("adb",   "fdab", 2, False),
        ("aaaa",  "bbbb", 4, True),
        ("abc",   "cba",  0, True),
    ]

    print("=== Sample Runs (Optimal O(n) array-count solution) ===")
    for s1, s2, k, expected in samples:
        out = sol.areKAnagrams(s1, s2, k)   # O(n)
        print(f"s1={s1!r}, s2={s2!r}, k={k} -> Output: {out} | Expected: {expected}")
    print("-" * 60)


# ---------------------------------------------------------------------
# Benchmark with timeit (measures full function runtime)
# ---------------------------------------------------------------------
def _bench_once(s1: str, s2: str, k: int) -> None:
    Solution().areKAnagrams(s1, s2, k)      # O(n)

def _random_same_length_pair(n: int, rng: random.Random) -> tuple[str, str, int]:
    """
    Generate two random lowercase strings of equal length and a random k.
    Data generation is O(n). Kept simple and safe for benchmarking.
    """
    alphabet = string.ascii_lowercase
    s1 = "".join(rng.choice(alphabet) for _ in range(n))   # O(n)
    # Make s2 similar to s1 with some noise so k isn't trivial
    s2_list = list(s1)
    for _ in range(n // 10):                               # flip ~10% chars
        i = rng.randrange(n)
        s2_list[i] = rng.choice(alphabet)
    s2 = "".join(s2_list)                                   # O(n)
    k = rng.randint(0, n)                                   # any k in [0, n]
    return s1, s2, k

def benchmark() -> None:
    rng = random.Random(2025)
    n = 100_000  # up to 1e5 per constraints

    s1, s2, k = _random_same_length_pair(n, rng)            # O(n) data prep

    runs = 10
    total = timeit.timeit(lambda: _bench_once(s1, s2, k), number=runs)

    print("=== Benchmark (k-Anagram, O(n) solution) ===")
    print(f"n        : {n}")
    print(f"k        : {k}")
    print(f"runs     : {runs}")
    print(f"total (s): {total:.6f}")
    print(f"avg/run  : {total / runs:.6f}")
    print("-" * 60)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main() -> None:
    # 1) Demonstrate correctness on hand-picked cases
    demo_on_samples()

    # 2) Benchmark the O(n) solution with a large random instance
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (the heavy-hitters)

1. **Fuzzy name/product matching (substitution-only tolerance)**
   When harmonizing catalogs or user directories, treat two strings as the “same” if one can be transformed into an anagram of the other with ≤ k substitutions (no insert/delete). This approximates small **character-mistake** divergences while ignoring order.

2. **Plagiarism / token obfuscation checks**
   In short identifiers or tokens where order is unimportant (e.g., scrambled codes), a k-anagram threshold can flag **minor obfuscations** that only substitute a few characters.

3. **Genomics (substitution mutations only)**
   For short markers where only **SNP-like** (single-nucleotide) substitutions are relevant (no insertions/deletions), k-anagram acts as a quick screen for **k substitutions** between two sequences disregarding order.

4. **Security & license keys (permutation-insensitive)**
   Some keys are order-insensitive sets/multisets of characters; k-anagram matching detects **near-miss keys** with limited substitution errors without caring about order.

