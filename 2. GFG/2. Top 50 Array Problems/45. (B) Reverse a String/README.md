# Reverse a String

**Difficulty:** Basic
**Accuracy:** 69.49%
**Submissions:** 427K+
**Points:** 1
**Average Time:** 15m

---

## Problem Statement

You are given a string `s`, and your task is to **reverse** the string.

---

## Examples

### Example 1

**Input:** `s = "Geeks"`
**Output:** `"skeeG"`

### Example 2

**Input:** `s = "for"`
**Output:** `"rof"`

### Example 3

**Input:** `s = "a"`
**Output:** `"a"`

---

## Constraints

* `1 ≤ s.size() ≤ 10^6`
* `s` contains only alphabetic characters (both uppercase and lowercase).

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

Strings, Data Structures

---

## Related Articles

* Cpp Program To Print Reverse Of A String Using Recursion
* Reverse A String In C Cpp Different Methods
* Reverse A String In Java
* String Reverse


---

---

here’s a crisp, interview-ready pack for **Reverse a String**.

---

# 2) Explanation + dry run

## Idea (two-pointers)

Strings in Python are **immutable**, so we can’t swap characters in place on the string.
Convert to a list of chars, reverse with two pointers, then `''.join(...)`.

* Set `l = 0`, `r = n-1`.
* While `l < r`: swap `a[l]` and `a[r]`, `l += 1`, `r -= 1`.

### Dry run on `s = "Geeks"`

```
a = ['G','e','e','k','s'],  l=0, r=4
swap a[0], a[4] -> ['s','e','e','k','G']       (l=1, r=3)
swap a[1], a[3] -> ['s','k','e','e','G']       (l=2, r=2)
stop; join -> "skeeG"
```

Time is **O(n)** (each index visited at most once). Any method must build a new string of length `n`, so **O(n)** extra output memory is unavoidable.

---

# 3) Python solutions (several ways)

### (A) Two-pointers on a list (classic interview answer)

```python
# User function Template for python3
class Solution:
    def reverseString(self, s: str) -> str:
        """
        Two-pointer swap on a char list.
        Time:  O(n)   (each index touched ≤ 1 time)
        Space: O(n)   (list + the new output string)
        """
        a = list(s)                  # O(n) to build list of characters
        l, r = 0, len(a) - 1
        while l < r:                 # O(n/2) swaps
            a[l], a[r] = a[r], a[l]
            l += 1; r -= 1
        return ''.join(a)            # O(n) to build result
```

### (B) Pythonic slice (fast & simple)

```python
class SolutionSlicing:
    def reverseString(self, s: str) -> str:
        """
        Python slicing creates a new reversed string.
        Time:  O(n)
        Space: O(n)
        """
        return s[::-1]
```

### (C) Built-in `reversed()` + join (readable)

```python
class SolutionReversed:
    def reverseString(self, s: str) -> str:
        """
        reversed(s) returns an iterator from end to start.
        Time:  O(n)
        Space: O(n)
        """
        return ''.join(reversed(s))
```

### (D) Recursion (educational; avoid for large n)

```python
class SolutionRecursive:
    def reverseString(self, s: str) -> str:
        """
        Recursive split: rev(left) + rev(right).
        Time:  O(n) expected (but larger constants)
        Space: O(n) recursion stack -> can overflow for big inputs.
        """
        if len(s) <= 1: return s
        mid = len(s) // 2
        return self.reverseString(s[mid:]) + self.reverseString(s[:mid])
```

### (E) Brute / Anti-pattern (O(n²)) – **don’t** do this

```python
class SolutionBrute:
    def reverseString(self, s: str) -> str:
        """
        Builds result by repeated string concatenation from the left.
        Time:  O(n^2) due to repeated reallocation; Space: O(n).
        Included only as a contrast to show why we avoid it.
        """
        out = ''
        for ch in s:
            out = ch + out   # re-copies every time -> quadratic
        return out
```

---

# 4) Interviewer-style Q\&A

**Q1. Why can’t we reverse in place on the string?**
Python strings are **immutable**—any change creates a new string. Convert to a list (mutable) if you need swaps, then join.

**Q2. What are time/space of your preferred solution?**
All good solutions are **O(n)** time and **O(n)** extra space (you must allocate a new string of length `n`). The two-pointer version also uses an `O(n)` list.

**Q3. Which is fastest in Python?**
`slice` (`s[::-1]`) and `''.join(reversed(s))` are both highly optimized C-level paths and typically faster than Python-level loops. Use them unless the interviewer explicitly wants the algorithmic two-pointer.

**Q4. Any pitfalls?**

* **Quadratic concatenation** in a loop—avoid `out = ch + out` or `out += ch` when building from the front.
* Reversing **Unicode grapheme clusters** (e.g., emojis with modifiers/diacritics) may break visual characters; this problem restricts to alphabetic ASCII so it’s fine.

**Q5. Can we reverse in place if the input is a list of chars (like in C/C++)?**
Yes—apply the two-pointer swap directly on the list to achieve **O(1)** extra space.

**Q6. How would you handle streaming data?**
If the entire payload doesn’t fit in memory, reverse in **chunks** and write backward to a file, or use a deque and rotate; not needed here.

---

---

Here’s a **full, runnable Python program** for **Reverse a String** that:

* shows outputs for several **inputs** (input → output),
* includes **inline time/space complexity** notes at each step, and
* **benchmarks** the main solution using `timeit` in `main`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse a String

Primary method below uses the classic **two-pointer swap** on a char list
(Python strings are immutable), then joins back to a string.

Complexities (for any correct method):
  • Time:  O(n)     — you must touch each character at least once
  • Space: O(n)     — a new string of length n must be produced

This script:
  1) Implements class Solution.reverseString (two-pointers).
  2) Also includes a Pythonic slicing variant for reference.
  3) Prints results for sample inputs (input → output).
  4) Benchmarks the function using timeit.
"""

from __future__ import annotations
import random
import string
import timeit
from typing import List


# -------------------------------------------------------------------
# User function Template for python3
# -------------------------------------------------------------------
class Solution:
    def reverseString(self, s: str) -> str:
        """
        Two-pointer swap over a list of characters.

        Steps:
          A) Convert to list (mutable)                       -> Time O(n), Space O(n)
          B) Swap a[l] and a[r] while l < r (walk inward)    -> Time O(n), Space O(1) extra
          C) Join list back to string                        -> Time O(n), Space O(n) output

        Overall: Time O(n), Space O(n) (due to output string)
        """
        a = list(s)                         # A) O(n)/O(n)
        l, r = 0, len(a) - 1
        # B) O(n) swaps; in-place on the list
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return ''.join(a)                   # C) O(n)/O(n)


# Optional: built-in style (fast & concise)
class SolutionSlicing:
    def reverseString(self, s: str) -> str:
        """
        Pythonic slicing (implemented in C).
        Time: O(n) | Space: O(n)
        """
        return s[::-1]


# ------------------------------- Demo & Benchmark -------------------------------

def demo_on_samples() -> None:
    """
    Demonstrate correctness on a few inputs.
    Time here is proportional to the total length of all samples (O(sum n_i)).
    """
    samples = [
        "Geeks",            # -> "skeeG"
        "for",              # -> "rof"
        "a",                # -> "a"
        "AaBbCc",           # mixed case
        "",                 # empty string (edge case, length 0)
    ]

    sol = Solution()
    print("=== Sample Runs (Input → Output) ===")
    for s in samples:
        out = sol.reverseString(s)          # O(n)
        print(f'Input : "{s}"')
        print(f'Output: "{out}"')
        print("-" * 60)


def _bench_once(s: str) -> None:
    """
    Helper for timeit: run only the O(n) reverse.
    Function is pure (does not mutate input), so we reuse the same string each run.
    """
    Solution().reverseString(s)


def benchmark() -> None:
    """
    Benchmark the reverse function using timeit.

    Prep (outside timing):
      - Build a random alphabetic string of length SIZE  -> Time O(SIZE), Space O(SIZE)

    Timed region:
      - Each run reverses the string (O(SIZE)).
    """
    SIZE = 1_000_000                         # within stated constraints (<= 1e6)
    rng = random.Random(2025)
    letters = string.ascii_letters
    test_str = ''.join(rng.choice(letters) for _ in range(SIZE))  # O(SIZE)

    runs = 5
    total = timeit.timeit(lambda: _bench_once(test_str), number=runs)

    print("=== Benchmark (Reverse string, O(n) time / O(n) space) ===")
    print(f"Length : {SIZE}")
    print(f"Runs   : {runs}")
    print(f"Total  : {total:.6f} s")
    print(f"Avg/run: {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Show outputs for specific inputs (includes inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method (two-pointers) with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Parsing & text processing**
   Reverse to process suffix-oriented patterns efficiently (e.g., scan from the end, reverse → treat like prefix).

2. **Palindromic checks / normalization**
   Compare a string with its reverse to test palindromes after cleaning punctuation/case.

3. **Data structures / algorithms**
   Reversing paths or operations (e.g., reverse Polish notation to infix transformations, reversing sequences in editors, undo logs).

4. **Cryptographic / encoding exercises**
   Although not security, reversing is common in simple ciphers/obfuscation or as a preprocessing step in coding challenges.
