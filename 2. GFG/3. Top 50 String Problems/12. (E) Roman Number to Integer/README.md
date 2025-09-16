# Roman Number to Integer

**Difficulty:** Easy
**Accuracy:** 43.31%
**Submissions:** 206K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Given a string `s` in **Roman number** format, your task is to **convert it to an integer**.
Various symbols and their values are given below.

**Note:**
`I = 1`, `V = 5`, `X = 10`, `L = 50`, `C = 100`, `D = 500`, `M = 1000`

---

## Examples

### Example 1

**Input:** `s = "IX"`
**Output:** `9`
**Explanation:** `IX` is a Roman symbol which represents `10 − 1 = 9`.

---

### Example 2

**Input:** `s = "XL"`
**Output:** `40`
**Explanation:** `XL` is a Roman symbol which represents `50 − 10 = 40`.

---

### Example 3

**Input:** `s = "MCMIV"`
**Output:** `1904`
**Explanation:** `M` is `1000`, `CM` is `1000 − 100 = 900`, and `IV` is `4`.
Total = `1000 + 900 + 4 = 1904`.

---

## Constraints

* `1 ≤` roman number `≤ 3999`
* `s[i]` belongs to `{I, V, X, L, C, D, M}`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Zoho, Amazon, Microsoft, Facebook, Twitter, Uber

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Articles

* [Roman Number To Integer](https://www.geeksforgeeks.org/roman-number-to-integer/)


---

---

Here’s a tight, interview-ready pack for **“Roman Number to Integer”**.

---

## 2) Intuition + step-by-step dry run

### Rules recap

Roman symbols (values):
`I=1, V=5, X=10, L=50, C=100, D=500, M=1000`

**Subtractive rule:** if a smaller symbol appears **before** a larger one, subtract it (e.g., `IV = 5−1`, `CM = 1000−100`). Otherwise, **add**.

### Most common evaluation trick

Scan the string; for each character `s[i]`:

* If the **next** symbol has a **greater** value, **subtract** `value(s[i])`.
* Else, **add** `value(s[i])`.

This works because subtractive forms are exactly those spots where a smaller value is followed by a larger one.

### Dry runs

#### Example: `s = "MCMIV"` → 1904

| Index | Char | Val  | Next    | Rule                  | Running total |
| ----- | ---- | ---- | ------- | --------------------- | ------------- |
| 0     | M    | 1000 | C(100)  | 1000 ≥ 100 → add      | 1000          |
| 1     | C    | 100  | M(1000) | 100 < 1000 → subtract | 900           |
| 2     | M    | 1000 | I(1)    | 1000 ≥ 1 → add        | 1900          |
| 3     | I    | 1    | V(5)    | 1 < 5 → subtract      | 1899          |
| 4     | V    | 5    | —       | add                   | **1904**      |

#### Example: `s = "IX"` → 9

* `I (1)` before `X (10)` → subtract 1 → total = −1
* `X (10)` last → add 10 → total = **9**

#### Example: `s = "XL"` → 40

* `X (10)` before `L (50)` → subtract 10
* `L (50)` → add 50 → **40**

---

## 3) Python solutions (optimized + alternatives)

### A) Look-ahead scan (most expected) — **O(n) time, O(1) space**

```python
class Solution:
    def romanToDecimal(self, s: str) -> int:
        """
        Scan left→right. If current < next, subtract; else add.
        Time : O(n)  (single pass)
        Space: O(1)  (constant mapping)
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        n = len(s)
        total = 0
        for i, ch in enumerate(s):
            v = val[ch]                     # O(1)
            # If a larger value follows, this is a subtractive position.
            if i + 1 < n and v < val[s[i + 1]]:
                total -= v
            else:
                total += v
        return total
```

### B) Reverse scan (no look-ahead) — **O(n) / O(1)**

Keep the last (rightmost) value seen. If current < last, subtract; else add.

```python
class SolutionReverse:
    def romanToDecimal(self, s: str) -> int:
        """
        Scan right→left. If current < previous (to the right), subtract; else add.
        Time : O(n)
        Space: O(1)
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        last = 0
        for ch in reversed(s):
            v = val[ch]
            if v < last:
                total -= v
            else:
                total += v
                last = v
        return total
```

### C) “Brute-ish” expand subtractives then sum — **O(n) / O(1)**

Replace subtractive pairs with equivalent additive sequences; then sum all symbols.
(Conceptually simple, less elegant; still linear.)

```python
class SolutionExpand:
    def romanToDecimal(self, s: str) -> int:
        """
        Expand subtractive pairs into additive runs, then sum.
        Time : O(n)  (constant number of replaces + one pass)
        Space: O(1)
        """
        # Replace subtractive pairs with their additive equivalents.
        s = (s.replace("CM", "DCCCC")
               .replace("CD", "CCCC")
               .replace("XC", "LXXXX")
               .replace("XL", "XXXX")
               .replace("IX", "VIIII")
               .replace("IV", "IIII"))

        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        for ch in s:
            total += val[ch]
        return total
```

> In interviews, write **A** (or **B**) — simple, robust, and idiomatic. Mention **C** as an intuitive baseline.

---

## 4) Interviewer-style Q\&A

**Q1. Why does the subtract-if-current-less-than-next rule work?**
Because valid subtractive notation only occurs when a smaller value precedes a larger one (e.g., `IV, IX, XL, XC, CD, CM`). Everywhere else, values are non-increasing, so you add.

**Q2. What are the complexities?**
All approaches above are **O(n)** time and **O(1)** extra space (the mapping is constant size).

**Q3. Do we need to validate invalid Romans like `"IL"` or `"VX"`?**
Many coding problems **guarantee valid input**. If validation is required, you must enforce grammar constraints (e.g., I before V/X only, X before L/C only, etc.) or parse with a small FSM/regex.

**Q4. What’s the numeric range?**
Typical Roman numerals represent **1–3999** without overlines. (With overlines, larger values can be expressed but are usually out of scope.)

**Q5. Are Roman numerals case-sensitive?**
Yes, by convention they’re uppercase. If mixed case can appear, normalize with `s = s.upper()`.

**Q6. Any pitfalls?**

* Confusing additive vs subtractive cases.
* Forgetting pairs like `CM (900)` and `CD (400)`.
* Assuming input always sorted non-increasing (not true due to subtractives).

---

---

Below is a **complete, runnable Python program** for **Roman → Integer** that:

* implements the optimal **O(n)** solutions (look-ahead and reverse scans),
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the primary solution with `timeit` in `main`.

I’ve annotated each step with **time/space complexity** comments.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Roman Number to Integer
-----------------------
Convert a Roman numeral string s (1..3999) to an integer.

Let n = len(s).

Overall complexities for the decoding algorithm:
  Time  : O(n)      (single linear scan)
  Space : O(1)      (fixed-size symbol map)
"""

from __future__ import annotations
import random
import timeit
from typing import List


# ---------------------------------------------------------------
# Primary solution: left-to-right look-ahead (most expected)
# ---------------------------------------------------------------
class Solution:
    def romanToDecimal(self, s: str) -> int:
        """
        Scan left→right; subtract if current value < next value, else add.

        For each i:
          - lookup current value v = val[s[i]]                 -> O(1)
          - compare with next value (if exists)                -> O(1)
          - add/subtract v                                     -> O(1)
        All i once -> O(n) time. Map is constant -> O(1) space.
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        n = len(s)             # O(1)
        total = 0              # O(1)
        for i, ch in enumerate(s):  # O(n) iterations
            v = val[ch]        # O(1)
            # If a larger value follows, this is a subtractive position.
            if i + 1 < n and v < val[s[i + 1]]:
                total -= v     # O(1)
            else:
                total += v     # O(1)
        return total


# ---------------------------------------------------------------
# Alternative solution: right-to-left (no look-ahead)
# ---------------------------------------------------------------
class SolutionReverse:
    def romanToDecimal(self, s: str) -> int:
        """
        Scan right→left; keep last (rightmost) value seen.
        If current < last, subtract; else add and update last.
        Time O(n), Space O(1).
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        last = 0
        for ch in reversed(s):   # O(n)
            v = val[ch]
            if v < last:
                total -= v
            else:
                total += v
                last = v
        return total


# ---------------------------------------------------------------
# Helper: integer -> Roman (for generating random valid test data)
# (Also O(1); used only to build inputs for the benchmark)
# ---------------------------------------------------------------
def int_to_roman(n: int) -> str:
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
    ]
    out: List[str] = []
    for v, sym in vals:
        if n == 0:
            break
        cnt = n // v
        if cnt:
            out.append(sym * cnt)
            n -= v * cnt
    return "".join(out)


# ---------------------------------------------------------------
# Demo: sample runs (prints input values and outputs)
# ---------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    cases = [
        ("IX", 9),
        ("XL", 40),
        ("MCMIV", 1904),
        ("LVIII", 58),
        ("III", 3),
        ("MMXXV", 2025),
    ]
    print("=== Sample Runs (Roman -> Integer) ===")
    for s, expected in cases:
        out = sol.romanToDecimal(s)  # O(n)
        print(f"s={s!r:<8} -> {out:<5} | expected: {expected}")
    print("-" * 60)


# ---------------------------------------------------------------
# Benchmark with timeit: measure full function runtime
# ---------------------------------------------------------------
def _bench_once(romans: List[str]) -> None:
    # Convert a batch inside the timed region; overall O(sum len(romans))
    sol = Solution()
    for r in romans:
        sol.romanToDecimal(r)

def benchmark() -> None:
    # Prepare random valid Roman numerals (data prep excluded from timing)
    rng = random.Random(2025)
    nums = [rng.randint(1, 3999) for _ in range(20_000)]        # O(1) per item
    romans = [int_to_roman(x) for x in nums]                    # O(1) avg per item

    runs = 10
    total = timeit.timeit(lambda: _bench_once(romans), number=runs)

    print("=== Benchmark (Roman -> Integer) ===")
    print(f"Batch size : {len(romans)}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-impact)

1. **Parsing years and editions**
   Extract numeric years/volumes from credits, books, and events (e.g., *MMXXV* → 2025, *Vol. XLII* → 42) for indexing and search.

2. **Document & legal processing**
   Headings/clauses and enumerations often use Roman numerals (I, II, III…). Automated parsing converts them to integers for sorting and references.

3. **UI/Typesetting pipelines**
   Converting Roman labels to integers (and back) for pagination, outlines, and watch/clock dials in design and rendering tools.

4. **Data cleaning / normalization**
   Normalize mixed numeral formats (e.g., “Chapter IX” → 9) in ETL processes to unify analytics across sources.
