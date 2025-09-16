# String Rotated by 2 Places

**Difficulty:** Easy
**Accuracy:** 32.7%
**Submissions:** 255K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Given two strings **s1** and **s2**. Return **true** if the string **s2** can be obtained by rotating (in **any direction**) string **s1** by **exactly 2 places**, otherwise, **false**.

**Note:** Both rotations should be performed in the **same direction** chosen initially.

---

## Examples

### Example 1

**Input:** `s1 = "amazon", s2 = "azonam"`
**Output:** `true`
**Explanation:** `"amazon"` can be rotated **anti-clockwise** by two places, which will make it `"azonam"`.

---

### Example 2

**Input:** `s1 = "geeksforgeeks", s2 = "geeksgeeksfor"`
**Output:** `false`
**Explanation:** If we rotate `"geeksforgeeks"` by two places in any direction, we won't get `"geeksgeeksfor"`.

---

### Example 3

**Input:** `s1 = "ab", s2 = "ab"`
**Output:** `true`
**Explanation:** If we rotate `"ab"` by two places in any direction, we always get `"ab"`.

---

## Constraints

* `1 ≤ s1.length, s2.length ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Accolite, Amazon

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Interview Experiences

* Accolite Interview Experience Set 5 On Campus

---

## Related Articles

* [Check String Can Obtained Rotating Another String 2 Places](https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/)

---

---

Here’s everything you need for **“String Rotated by 2 Places”**.

---

## 2) Intuition + step-by-step dry run

We must check whether **s2** can be obtained by rotating **s1** by **exactly two positions** either:

* **left** (anti-clockwise): move first two chars to the end
  `left2(s1) = s1[2:] + s1[:2]`
* **right** (clockwise): move last two chars to the front
  `right2(s1) = s1[-2:] + s1[:-2]`

If **either** equals `s2`, return `True`; otherwise `False`.

### Early observations

* If `len(s1) != len(s2)`, return `False`.
* If `len(s1) < 2`, a 2-place rotation is effectively the **same string** (e.g., `"a"`, `""`). So return `s1 == s2`.

### Dry run 1

`s1 = "amazon"`, `s2 = "azonam"`

* `left2(s1) = "azonam"` ✔ equals `s2` → **True**.

### Dry run 2

`s1 = "geeksforgeeks"`, `s2 = "geeksgeeksfor"`

* `left2(s1) = "eksforgeeksge"`
* `right2(s1) = "ksgeeksforgee"`
  Neither equals `s2` → **False**.

### Dry run 3

`s1 = "ab"`, `s2 = "ab"`

* `left2(s1) = "ab"[2:] + "ab"[:2] = "" + "ab" = "ab"`
* `right2(s1) = "ab"[-2:] + "ab"[:-2] = "ab" + "" = "ab"`
  Both equal `s2` → **True**.

---

## 3) Python solutions (interview-ready)

### A) Simple slice comparison (most expected) — **O(n) time, O(n) space**

```python
class Solution:
    def isRotated(self, s1: str, s2: str) -> bool:
        """
        Check if s2 equals s1 rotated by exactly 2 positions (either direction).
        Time : O(n)  — slicing is linear in string length
        Space: O(n)  — new strings from slices
        """
        # Length mismatch = impossible
        if len(s1) != len(s2):
            return False

        n = len(s1)
        # For strings of length < 2, a 2-rotation does nothing
        if n < 2:
            return s1 == s2

        left2  = s1[2:] + s1[:2]   # rotate left by 2
        right2 = s1[-2:] + s1[:-2] # rotate right by 2

        return s2 == left2 or s2 == right2
```

### B) O(1) extra space (character by character) — **O(n) time, O(1) space**

Avoid building new strings; compare positions arithmetically.

```python
class SolutionO1:
    def isRotated(self, s1: str, s2: str) -> bool:
        """
        Compare without allocating rotated copies.
        Time : O(n)
        Space: O(1)
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if n < 2:
            return s1 == s2

        # Check left rotation: s2[i] should equal s1[(i+2) % n]
        left_ok = True
        for i in range(n):
            if s2[i] != s1[(i + 2) % n]:
                left_ok = False
                break
        if left_ok:
            return True

        # Check right rotation: s2[i] should equal s1[(i-2) % n]
        for i in range(n):
            if s2[i] != s1[(i - 2) % n]:
                return False
        return True
```

### C) Using concatenation trick (still O(n)) — **O(n) time, O(n) space**

You’ll sometimes see rotation checks done with `s1 in (s2+s2)`. Here we need **exactly 2** places, so we just compare to the two specific rotations:

```python
class SolutionConcat:
    def isRotated(self, s1: str, s2: str) -> bool:
        """
        Build only the two necessary rotations via concatenation.
        Time : O(n)
        Space: O(n)
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if n < 2:
            return s1 == s2
        return s2 == (s1[2:] + s1[:2]) or s2 == (s1[-2:] + s1[:-2])
```

> In interviews, solution **A** is the common, clear answer. If pressed about space, present **B** (O(1) extra space).

---

## 4) Interviewer-style Q\&A

**Q1. Why do we consider only two rotations (left2, right2)?**
Because the problem asks for rotation by **exactly 2** positions, and rotating 2 to the left or right are the only two distinct results (for `n ≥ 2`). Either could produce `s2`.

**Q2. What about strings of length 0 or 1?**
Rotating by 2 doesn’t change them, so the check reduces to `s1 == s2`.

**Q3. What are the time and space complexities?**

* Slice approach: **O(n)** time, **O(n)** space (two temporary strings).
* Index comparison: **O(n)** time, **O(1)** extra space.

**Q4. Could we use the “double string” trick `s2 in s1+s1`?**
That tells you if `s2` is **some rotation** of `s1`, not necessarily **exactly by 2**. We still need to enforce the 2-step constraint, hence directly checking left2/right2.

**Q5. Edge cases to watch?**

* Different lengths → immediately `False`.
* `n < 2`.
* Highly repetitive strings (e.g., `"aaaaa"`) — both rotations equal the original; code still works.

**Q6. Unicode / case sensitivity?**
Rotation is purely positional and works for any characters. The comparison is exact (case-sensitive) unless specified otherwise.

---

---

Here’s a **complete, runnable Python program** for **“String Rotated by 2 Places”** that

* implements the required `class Solution.isRotated(self, s1, s2)` (slice-based O(n)) and an O(1)-extra-space variant,
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the solution using `timeit` in `main`.

Every step is annotated with **time & space complexity** notes.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
String Rotated by 2 Places
--------------------------
Return True if s2 can be obtained by rotating s1 by exactly two positions in
either direction (left/anti-clockwise or right/clockwise); else False.

Let n = len(s1) = len(s2) when comparable.

Overall complexities (slice-based solution):
  Time  : O(n)   — building at most two rotated strings (linear slicing)
  Space : O(n)   — temporary strings created by slicing/concat
"""

from __future__ import annotations
import random
import string
import timeit
from typing import List, Tuple


# ---------------------------------------------------------------------
# Required interface — clear, idiomatic version (most expected)
# ---------------------------------------------------------------------
class Solution:
    def isRotated(self, s1: str, s2: str) -> bool:
        """
        Check if s2 equals s1 rotated by exactly 2 positions (either direction).

        Steps & cost:
          A) Length check                         -> O(1)
          B) Handle n < 2 (rotation is identity) -> O(1)
          C) Build left2 = s1[2:] + s1[:2]        -> O(n) time, O(n) space
          D) Build right2 = s1[-2:] + s1[:-2]     -> O(n) time, O(n) space
          E) Equality check against s2            -> O(n) in worst case (short-circuit common)
        Total: O(n) time, O(n) extra space (from slices).
        """
        # A) Lengths must match
        if len(s1) != len(s2):  # O(1)
            return False

        n = len(s1)
        # B) For n < 2, rotating by 2 does nothing (identity)
        if n < 2:  # O(1)
            return s1 == s2     # O(n) worst, but tiny constant for n < 2

        # C) Left rotation by 2: move first two chars to end
        left2 = s1[2:] + s1[:2]     # O(n) time, O(n) space (new string)
        if s2 == left2:             # O(n) equality worst case
            return True

        # D) Right rotation by 2: move last two chars to front
        right2 = s1[-2:] + s1[:-2]  # O(n) time, O(n) space
        return s2 == right2         # O(n) equality worst case


# ---------------------------------------------------------------------
# Alternative: O(1) extra space — compare by index math (no new strings)
# ---------------------------------------------------------------------
class SolutionO1:
    def isRotated(self, s1: str, s2: str) -> bool:
        """
        Compare characters directly with modular indexing.

        Time  : O(n)  (two passes at most)
        Space : O(1)  (no temporary strings)
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if n < 2:
            return s1 == s2

        # Check s2 == left-rotate-2(s1): s2[i] == s1[(i + 2) % n]
        for i, ch in enumerate(s2):  # O(n)
            if ch != s1[(i + 2) % n]:
                break
        else:
            return True

        # Check s2 == right-rotate-2(s1): s2[i] == s1[(i - 2) % n]
        for i, ch in enumerate(s2):  # O(n)
            if ch != s1[(i - 2) % n]:
                return False
        return True


# ---------------------------------------------------------------------
# Demo: show inputs & outputs to verify behavior
# ---------------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    examples: List[Tuple[str, str, bool]] = [
        ("amazon", "azonam", True),        # left rotation works
        ("geeksforgeeks", "geeksgeeksfor", False),  # no 2-rot gives s2
        ("ab", "ab", True),                # 2-rot on length 2 is identity
        ("aaaaa", "aaaaa", True),          # repetitive string stays same
        ("abcde", "deabc", True),          # right rotation by 2
        ("abcde", "cdeab", False),         # rotation by 3, not 2
    ]
    print("=== Sample Runs ===")
    for s1, s2, expected in examples:
        out = sol.isRotated(s1, s2)  # O(n)
        print(f"s1={s1!r:10} s2={s2!r:10} -> {out} | expected: {expected}")
    print("-" * 60)


# ---------------------------------------------------------------------
# Benchmark with timeit — measure full function runtime
# ---------------------------------------------------------------------
def _bench_once(pairs: List[Tuple[str, str]], solver) -> None:
    # Run the solver for a batch of inputs; total cost ~ O(sum of lengths)
    for s1, s2 in pairs:
        solver.isRotated(s1, s2)

def benchmark() -> None:
    rng = random.Random(2025)

    def rand_word(n: int) -> str:
        # Mostly letters to emulate typical strings
        return "".join(rng.choice(string.ascii_lowercase) for _ in range(n))

    # Build a batch with mixed True/False cases
    pairs: List[Tuple[str, str]] = []
    for _ in range(15_000):
        n = rng.randint(2, 40)
        s1 = rand_word(n)
        # Flip a coin: produce a valid 2-rotation or a random unrelated string
        if rng.random() < 0.5:
            # Make s2 a valid left- or right-rotation-by-2
            if rng.random() < 0.5:
                s2 = s1[2:] + s1[:2]
            else:
                s2 = s1[-2:] + s1[:-2]
        else:
            # Make s2 a different random string (same length)
            s2 = rand_word(n)
        pairs.append((s1, s2))

    runs = 10

    # Slice-based solution
    total_slice = timeit.timeit(lambda: _bench_once(pairs, Solution()),
                                number=runs)

    # O(1)-space solution
    total_o1 = timeit.timeit(lambda: _bench_once(pairs, SolutionO1()),
                             number=runs)

    print("=== Benchmark (higher is slower) ===")
    print(f"Batch size : {len(pairs)}")
    print(f"Runs       : {runs}")
    print(f"Slice ver. : total {total_slice:.6f}s | avg/run {total_slice / runs:.6f}s")
    print(f"O(1) ver.  : total {total_o1:.6f}s | avg/run {total_o1 / runs:.6f}s")
    print("-" * 60)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **Circular buffers / ring logs**
   Validating that a buffer snapshot was shifted by a fixed offset (e.g., 2 slots) after wrap-around can be treated as a rotation-by-k check.

2. **Network protocol framing**
   Some lightweight protocols or classroom ciphers do fixed circular shifts of payload bytes; testing whether a received field equals a fixed rotation of the expected field helps detect misaligned framing.

3. **UI carousels / sliders**
   Verifying that a list of items advanced by a fixed number of positions (e.g., two cards) after a user action can be modeled as a rotation-by-k assertion in tests.

4. **Data pipeline sanity checks**
   When joining partitions or sharded chunks, detecting off-by-k cyclic shifts (e.g., two columns or two positions) can prevent subtle “rotated” merges.
