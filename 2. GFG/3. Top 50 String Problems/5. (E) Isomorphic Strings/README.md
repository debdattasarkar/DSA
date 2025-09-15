# Isomorphic Strings

**Difficulty:** Easy
**Accuracy:** 34.21%
**Submissions:** 208K+
**Points:** 2
**Average Time:** 30m

---

## Problem Statement

Given two strings **s1** and **s2** consisting of only lowercase English letters and of **equal length**, check if these two strings are **isomorphic** to each other.
If the characters in **s1** can be changed to get **s2**, then two strings, **s1** and **s2** are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but **no two characters may map to the same character**.

---

## Examples

### Example 1

**Input:** `s1 = "aab", s2 = "xxy"`
**Output:** `true`
**Explanation:** Each character in **s1** can be consistently mapped to a unique character in **s2** (`a → x`, `b → y`).

### Example 2

**Input:** `s1 = "aab", s2 = "xyz"`
**Output:** `false`
**Explanation:** Same character `a` in **s1** maps to two different characters `x` and `y` in **s2**.

### Example 3

**Input:** `s1 = "abc", s2 = "xxz"`
**Output:** `false`
**Explanation:** Two different characters `a` and `b` in **s1** map to the same character `x` in **s2**.

---

## Constraints

`1 ≤ s1.size() = s2.size() ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Google

---

## Topic Tags

Strings, Data Structures, Hash

---

## Related Articles

* [Check If Two Given Strings Are Isomorphic To Each Other](https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/)

---

---

Here’s an interview-ready guide for **Isomorphic Strings**.

---

## 2) Explanation (what & why) + step-by-step dry run

### Problem in one line

Two strings `s1` and `s2` (same length) are **isomorphic** iff there exists a **bijective** (one-to-one & onto) mapping from characters in `s1` to characters in `s2` that preserves order.
A char may map to itself; but **no two different chars in `s1` may map to the same char in `s2`**.

### Key idea (O(n))

Walk both strings together and maintain:

* `map12[c1] = c2`   (what `c1` must map to)
* `map21[c2] = c1`   (what `c2` must come from)

Whenever you see a pair `(c1, c2)`:

* If we’ve seen `c1` before, it **must** map to the same `c2`.
* If we’ve seen `c2` before, it **must not** come from a different `c1`.

If any rule is violated → not isomorphic.
Why both maps? Because checking only `s1→s2` allows many-to-one mistakes (e.g., `"ab"` vs `"aa"`).

#### Dry run 1 — `s1="aab"`, `s2="xxy"`  → **True**

* i=0: `a↔x` — set `map12[a]=x`, `map21[x]=a`
* i=1: `a↔x` — consistent (a already → x, x already ← a)
* i=2: `b↔y` — new consistent pair
  All consistent → True.

#### Dry run 2 — `s1="aab"`, `s2="xyz"`  → **False**

* i=0: `a↔x` — map
* i=1: `a↔y` — violates `a`→`x` (existing mapping) → False.

#### Dry run 3 — `s1="abc"`, `s2="xxz"`  → **False**

* i=0: `a↔x` — map
* i=1: `b↔x` — `x` already mapped from `a` (many-to-one) → False.

---

## 3) Python solutions (multiple interview-friendly ways)

### A) Two hash maps (most expected). O(n) time, O(1) extra space (constant alphabet)

```python
class Solution:
    def areIsomorphic(self, s1, s2):
        """
        Check bijection by keeping both forward (s1->s2) and reverse (s2->s1) maps.
        Time : O(n)
        Space: O(1) for fixed alphabet (or O(k) with k distinct chars)
        """
        if len(s1) != len(s2):
            return False

        map12 = {}
        map21 = {}

        for c1, c2 in zip(s1, s2):
            # If c1 seen before, it must map to c2
            if c1 in map12 and map12[c1] != c2:
                return False
            # If c2 seen before, it must come from c1
            if c2 in map21 and map21[c2] != c1:
                return False

            map12[c1] = c2
            map21[c2] = c1

        return True
```

### B) Fixed-size arrays (fast & strictly O(1) space).

(Works for lowercase/ASCII; for general Unicode prefer dicts.)

```python
class SolutionArray:
    def areIsomorphic(self, s1, s2):
        """
        Use two arrays of size 256 storing last-seen mapping (or -1).
        Time : O(n)
        Space: O(1)
        """
        if len(s1) != len(s2):
            return False

        M = 256
        fwd = [-1] * M   # s1 char -> s2 code
        rev = [-1] * M   # s2 char -> s1 code

        for c1, c2 in zip(s1, s2):
            i1, i2 = ord(c1), ord(c2)

            if fwd[i1] == -1 and rev[i2] == -1:
                fwd[i1] = i2
                rev[i2] = i1
            else:
                # must be consistent in both directions
                if fwd[i1] != i2 or rev[i2] != i1:
                    return False

        return True
```

### C) Canonical pattern encoding (very clean).

Encode each string by the order of **first occurrences**, then compare encodings.

```python
class SolutionPattern:
    def _encode(self, s: str):
        """
        Map first-seen characters to 0,1,2,... and output the sequence.
        Example: "paper" -> [0,1,0,2,3], "title" -> [0,1,0,2,3]
        """
        code = {}
        out = []
        nxt = 0
        for ch in s:
            if ch not in code:
                code[ch] = nxt
                nxt += 1
            out.append(code[ch])
        return tuple(out)

    def areIsomorphic(self, s1, s2):
        """
        Two strings are isomorphic iff their encodings match.
        Time : O(n)
        Space: O(k) for distinct chars (k ≤ n, constant for fixed alphabet)
        """
        if len(s1) != len(s2):
            return False
        return self._encode(s1) == self._encode(s2)
```

### D) Brute / “naive” (educational). O(n²)

For each index `i`, scan all previous positions to ensure pairwise consistency.

```python
class SolutionBrute:
    def areIsomorphic(self, s1, s2):
        """
        For each i, check all j<i: (s1[i]==s1[j]) == (s2[i]==s2[j]).
        Time : O(n^2)
        Space: O(1)
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        for i in range(n):
            for j in range(i):
                if (s1[i] == s1[j]) != (s2[i] == s2[j]):
                    return False
        return True
```

---

## 4) Interviewer-style Q\&A

**Q1. Why do we need two maps?**
To enforce a **bijection**. A single forward map (`s1→s2`) doesn’t prevent many-to-one mappings (`"ab"` vs `"aa"` would wrongly pass). The reverse map (`s2→s1`) forbids that.

**Q2. What are the complexities?**

* Two-map / array / pattern encoding: **O(n)** time, **O(1)** extra space for fixed alphabet (or **O(k)** where `k` is number of distinct characters).
* Brute: **O(n²)** time.

**Q3. How does the pattern encoding prove isomorphism?**
Encoding replaces each char with the index of its **first appearance**. Two strings are isomorphic iff they induce the **same equality pattern** across positions, so their encodings are identical.

**Q4. Edge cases?**

* Different lengths → immediately False.
* Repeated characters mapping inconsistently (e.g., `aab` vs `xyz`).
* Many-to-one collisions (e.g., `abc` vs `xxz`).
* Very large `n` (up to `1e5`) → O(n) approach required.

**Q5. Can characters map to themselves?**
Yes. The only restriction is **uniqueness** of the mapping in both directions.

**Q6. How to handle non-ASCII / Unicode?**
Use the dictionary implementation (Solution A). Fixed-array version assumes bounded small alphabet.

**Q7. Difference from anagrams?**
Anagrams compare **multisets** of characters (order irrelevant). Isomorphism checks for a **structure-preserving one-to-one mapping** while preserving order.

---

---

Here’s a **full, runnable Python program** for **Isomorphic Strings** that:

* implements the standard **O(n)** two-map check (plus an alternative “pattern encoding” version),
* prints **inputs & outputs** for sample cases,
* and **benchmarks** the implementations with `timeit` in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Isomorphic Strings
------------------
Two strings s1 and s2 (same length) are isomorphic iff there exists a bijection
(one-to-one mapping) from characters in s1 to characters in s2 that preserves
order. A character may map to itself; no two different characters in s1 can map
to the same character in s2.

Primary approach below: keep both forward and reverse maps while scanning.

Complexity overview (n = len(s1) = len(s2)):
  • Time  : O(n)  — single pass through both strings
  • Space : O(1)  — for fixed lowercase alphabet; otherwise O(k) for k distinct chars
"""

from __future__ import annotations
import random
import string
import timeit
from typing import Dict


# -----------------------------------------------------------------------------
# Primary interview solution: two hash maps (O(n) time, O(1) extra for fixed alphabet)
# -----------------------------------------------------------------------------
class Solution:
    def areIsomorphic(self, s1: str, s2: str) -> bool:
        """
        Check bijection using both directions:
          map12[c1] = c2  and  map21[c2] = c1

        Steps with complexity:
          A) Length check -> O(1)
          B) Init two dicts -> O(1)
          C) Single pass over zipped characters:
             - O(1) average-time lookups/inserts per char
             - ensure consistency in both directions
          D) If never violated, return True

        Overall: Time O(n), Space O(1) for fixed alphabet (else O(k)).
        """
        # A) Trivial reject if sizes differ (O(1))
        if len(s1) != len(s2):
            return False

        # B) Two maps to enforce a bijection (O(1))
        map12: Dict[str, str] = {}
        map21: Dict[str, str] = {}

        # C) Single pass (O(n))
        for c1, c2 in zip(s1, s2):
            # If c1 already mapped, it must map to c2 (O(1) average)
            if c1 in map12 and map12[c1] != c2:
                return False
            # If c2 already mapped from someone, it must be c1 (O(1) average)
            if c2 in map21 and map21[c2] != c1:
                return False
            # Record/refresh mapping (O(1) average)
            map12[c1] = c2
            map21[c2] = c1

        # D) All constraints satisfied (O(1))
        return True


# -----------------------------------------------------------------------------
# Alternative: canonical pattern encoding (clean equality-of-structure check)
# -----------------------------------------------------------------------------
class SolutionPattern:
    def _encode(self, s: str):
        """
        Encode string by the order of first occurrences.
        Example: "paper" -> [0,1,0,2,3]; "title" -> [0,1,0,2,3]
        Time O(n), Space O(k) for distinct chars.
        """
        code: Dict[str, int] = {}
        seq = []
        next_id = 0
        for ch in s:
            if ch not in code:
                code[ch] = next_id
                next_id += 1
            seq.append(code[ch])
        return tuple(seq)

    def areIsomorphic(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        # Two strings are isomorphic iff their encodings match
        return self._encode(s1) == self._encode(s2)


# -----------------------------------------------------------------------------
# Demo: explicit sample runs (prints input values and outputs)
# -----------------------------------------------------------------------------
def demo_on_samples() -> None:
    """
    Shows correctness on several examples.
    Each call runs in O(n), space O(1)/O(k) depending on implementation.
    """
    cases = [
        ("aab", "xxy", True),
        ("aab", "xyz", False),
        ("abc", "xxz", False),
        ("paper", "title", True),
        ("foo", "bar", False),
        ("egg", "add", True),
        ("badc", "baba", False),
        ("", "", True),  # edge: empty strings are vacuously isomorphic
    ]

    sol = Solution()
    print("=== Sample Runs (Two-Map Solution) ===")
    for s1, s2, expected in cases:
        out = sol.areIsomorphic(s1, s2)
        print(f"s1={s1!r}, s2={s2!r} -> Output: {out} | Expected: {expected}")
    print("-" * 60)


# -----------------------------------------------------------------------------
# Benchmark: compare two-map vs pattern-encoding using timeit
# -----------------------------------------------------------------------------
def _bench_two_map(s1: str, s2: str) -> None:
    Solution().areIsomorphic(s1, s2)

def _bench_pattern(s1: str, s2: str) -> None:
    SolutionPattern().areIsomorphic(s1, s2)

def benchmark() -> None:
    """
    Build random lowercase strings of equal length and time the solutions.
    n chosen so the run is quick but non-trivial.
    """
    rng = random.Random(2025)
    n = 100_000  # size of test strings (≤ 1e5 per constraints)
    alphabet = string.ascii_lowercase  # 26 letters

    # Generate random s1; s2 is s1 passed through a random permutation
    s1 = "".join(rng.choice(alphabet) for _ in range(n))
    perm = list(alphabet)
    rng.shuffle(perm)
    mapping = {a: b for a, b in zip(alphabet, perm)}
    s2 = "".join(mapping[ch] for ch in s1)

    runs = 3
    t_two_map = timeit.timeit(lambda: _bench_two_map(s1, s2), number=runs)
    t_pattern = timeit.timeit(lambda: _bench_pattern(s1, s2), number=runs)

    print("=== Benchmark (n = {:,}) ===".format(n))
    print(f"Two-Map     total: {t_two_map:.6f} s | avg/run: {t_two_map / runs:.6f} s")
    print(f"Pattern Enc total: {t_pattern:.6f} s | avg/run: {t_pattern / runs:.6f} s")
    print("-" * 60)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> None:
    # 1) Demonstrate outputs for hand-picked cases (includes inputs & outputs)
    demo_on_samples()

    # 2) Benchmark implementations using timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (only the big ones)

1. **Compiler/Interpreter Renaming (α-equivalence lite)**
   Check whether two token streams are the same **up to consistent renaming** of identifiers (e.g., comparing code fragments while ignoring specific variable names).

2. **Log Template Matching**
   Determine if log lines conform to the **same structural template** where actual entities (IDs, usernames) can be consistently substituted.

3. **Pattern-Invariant Matching in NLP**
   Compare sentences ignoring **consistent re-labeling** (e.g., “Alice likes Bob” vs “X likes Y”) to match relational structures independent of surface names.

4. **Graph/Schema Label Normalization (string form)**
   When node labels are serialized as strings, quickly verify if two linearized encodings correspond **up to relabeling** with a one-to-one mapping.
