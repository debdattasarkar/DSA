# Convert to Roman No

**Difficulty:** Easy
**Accuracy:** 51.57%
**Submissions:** 39K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Given an integer **n**, your task is to complete the function **`convertToRoman`** which prints the corresponding Roman number of **n**. Various symbols and their values are given below.

**Note:** There are a few exceptions for some numbers like **4** in Roman is **IV**, **9** in Roman is **IX**, similarly, **40** is **XL** while **90** is **XC**. Similarly, **400** is **CD** while **900** is **CM**.

```
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
```

---

## Examples

### Example 1

**Input:**
`n = 5`
**Output:**
`V`

### Example 2

**Input:**
`n = 3`
**Output:**
`III`

---

## Your Task

Complete the function **`convertToRoman()`** which takes an integer **N** as input parameter and returns the equivalent Roman.

---

## Expected Complexities

* **Time Complexity:** `O(log10 N)`
* **Auxiliary Space:** `O(log10 N * 10)`

---

## Constraints

`1 ≤ n ≤ 3999`

---

## Company Tags

* `Amazon`, `Microsoft`, `InfoEdge`, `Facebook`, `Twitter`

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Articles

* [Converting Decimal Number Lying Between 1 To 3999 To Roman Numerals](https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/)

---

---

Here’s a compact, interview-ready bundle for **“Convert Integer to Roman”**.

---

## 2) Explanation + step-by-step dry run

### Roman basics

Symbols and values (including subtractive forms):

```
M=1000, CM=900, D=500, CD=400,
C=100,  XC=90,  L=50,  XL=40,
X=10,   IX=9,   V=5,   IV=4,  I=1
```

**Greedy rule:**
Walk the list above from largest to smallest. For each value, use it as many times as possible, append its symbol, and subtract from `n`. This works because Roman numerals are canonical under this ordering (subtractive forms prevent 4, 9, 40, 90, 400, 900 from being expressed by repeating smaller symbols).

### Dry run (n = 1994)

Order: `M(1000), CM(900), D(500), CD(400), C(100), XC(90), L(50), XL(40), X(10), IX(9), V(5), IV(4), I(1)`

* `n=1994`: take `M` once → res=`"M"`, n=`994`
* `CM` fits once → res=`"MCM"`, n=`94`
* `XC` fits once → res=`"MCMXC"`, n=`4`
* `IV` fits once → res=`"MCMXCIV"`, n=`0` → done

Answer: **"MCMXCIV"**.

Another quick one (n = 3549):

* `MMM (3000)`, `D (500)`, `XL (40)`, `IX (9)` → **"MMMDXLIX"**.

---

## 3) Python solutions (most expected + alternatives)

### A) Greedy with (value, symbol) pairs — **O(1) time, O(1) space**

(“O(1)” because the list size is constant; work scales with number of digits, ≤ 15 iterations.)

```python
# User function template for Python 3
class Solution:
    def convertRoman(self, n: int) -> str:
        """
        Greedy over descending (value, symbol) pairs.
        Time  : O(1)   (constant-sized list; at most ~15 appends)
        Space : O(1)   (output excluded)
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
        ]
        out = []
        for v, sym in vals:
            if n == 0:
                break
            # how many times current value fits
            cnt = n // v                     # O(1)
            if cnt:
                out.append(sym * cnt)        # O(1) small constant
                n -= v * cnt                 # O(1)
        return "".join(out)
```

### B) Digit-table method (precomputed strings per place) — **O(1) / O(1)**

Fast and tidy: convert thousands, hundreds, tens, ones independently.

```python
class SolutionTable:
    def convertRoman(self, n: int) -> str:
        """
        Use precomputed tables for each decimal place.
        Time  : O(1)
        Space : O(1)
        """
        thousands = ["", "M", "MM", "MMM"]                 # 0..3  (n ≤ 3999)
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            thousands[n // 1000] +
            hundreds[(n % 1000) // 100] +
            tens[(n % 100) // 10] +
            ones[n % 10]
        )
```

### C) “Brute” repeat-subtraction (educational; same asymptotics)

Loop subtracting one value at a time (no division). Slightly slower constants, but conceptually simple.

```python
class SolutionBrute:
    def convertRoman(self, n: int) -> str:
        """
        Repeated subtraction while appending symbols.
        Time  : O(1) (bounded iterations), but more steps than greedy with //.
        Space : O(1)
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
        ]
        res = []
        i = 0
        while n > 0:
            v, sym = vals[i]
            if n >= v:
                res.append(sym)
                n -= v
            else:
                i += 1
        return "".join(res)
```

> In interviews, solution **A** or **B** is usually what they expect. **A** shows greedy correctness; **B** is the cleanest and fastest.

---

## 4) Interviewer-style Q\&A

**Q1. Why does the greedy approach always work?**
Because the Roman system is canonical with subtractive forms included. Picking the largest possible symbol at each step never blocks an optimal representation (there’s a unique standard form for 1–3999).

**Q2. What are the time/space complexities?**
All approaches are **O(1)** time and space (ignoring output), since the number of operations is bounded by a constant set of symbols and digits.

**Q3. Why include subtractive pairs (IV, IX, XL, XC, CD, CM) explicitly?**
Without them you’d generate invalid forms like `IIII` for 4 or `VIIII` for 9. The subtractive pairs encode those special cases directly.

**Q4. What inputs are valid and why is 3999 the upper limit?**
Standard Roman numerals (without overlines) typically represent 1–3999. Beyond that, you’d need overlines (multiplying by 1000) or non-standard extensions.

**Q5. How would you convert *from* Roman to integer?**
Scan left-to-right: if a symbol is less than the next, subtract it; otherwise add it (treat subtractive pairs). Complexity is also O(1).

**Q6. Any edge cases?**

* `n=1` → `"I"`, `n=3` → `"III"`, `n=4` → `"IV"` (subtractive), `n=9` → `"IX"`, `n=40` → `"XL"`, etc.
* Upper bound `n=3999` → `"MMMCMXCIX"`.

---

---

Absolutely! Here’s a **complete, runnable Python program** for **Convert Integer → Roman** that:

* Implements the optimal **greedy** solution (and a fast **digit-table** variant).
* Prints **inputs → outputs** for sample cases.
* Uses **`timeit`** to benchmark both implementations right in `main`.
* Includes **inline comments** about **time & space complexity** for each step.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convert Integer to Roman
------------------------
Given n (1..3999), return its Roman numeral.

Complexities (n is bounded; list of symbols is constant):
  • Time  : O(1)       (bounded number of steps; ~≤ 15 appends)
  • Space : O(1) extra (output string not counted)
"""

from __future__ import annotations
import random
import timeit


# ---------------------------------------------------------------
# User function template for Python 3 — Greedy (most expected)
# ---------------------------------------------------------------
class Solution:
    def convertRoman(self, n: int) -> str:
        """
        Greedy over descending (value, symbol) pairs.
        Steps per iteration are O(1); the set is constant size.
        Overall: O(1) time and O(1) extra space.

        Correctness: subtractive forms (CM, CD, XC, XL, IX, IV) are included,
        ensuring canonical Roman representation while greedy stays optimal.
        """
        vals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
        ]
        out = []  # O(1) extra; small bounded use
        for v, sym in vals:     # constant 13 iterations
            if n == 0:
                break           # O(1)
            cnt = n // v        # O(1) integer division
            if cnt:             # append at most a few times in total
                out.append(sym * cnt)  # O(1) small constant
                n -= v * cnt    # O(1)
        return "".join(out)     # O(1) bounded length (≤ 15 chars for n≤3999)


# ---------------------------------------------------------------
# Alternative: Digit-table method (also O(1) / O(1), very fast)
# ---------------------------------------------------------------
class SolutionTable:
    def convertRoman(self, n: int) -> str:
        """
        Use precomputed strings for thousands/hundreds/tens/ones.
        Time/Space: O(1).
        """
        thousands = ["", "M", "MM", "MMM"]  # n ≤ 3999
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            thousands[n // 1000] +
            hundreds[(n % 1000) // 100] +
            tens[(n % 100) // 10] +
            ones[n % 10]
        )


# ---------------------------------------------------------------
# Demo: Show inputs and outputs for a few values
# ---------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    tests = [
        (5, "V"),
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (944, "CMXLIV"),
        (3999, "MMMCMXCIX"),
    ]
    print("=== Sample Runs (Greedy) ===")
    for n, expected in tests:
        out = sol.convertRoman(n)
        print(f"n={n:<4} -> {out}   (expected: {expected})")
    print("-" * 60)


# ---------------------------------------------------------------
# Benchmark with timeit for both implementations
# ---------------------------------------------------------------
def _bench_once(nums, solver) -> None:
    # Convert a batch of numbers; the batch size controls work per run.
    for x in nums:
        solver.convertRoman(x)

def benchmark() -> None:
    rng = random.Random(2025)
    nums = [rng.randint(1, 3999) for _ in range(20_000)]  # batch; O(1) per n

    runs = 10

    greedy = Solution()
    total_greedy = timeit.timeit(lambda: _bench_once(nums, greedy), number=runs)

    table = SolutionTable()
    total_table = timeit.timeit(lambda: _bench_once(nums, table), number=runs)

    print("=== Benchmark (higher is slower) ===")
    print(f"Batch size : {len(nums)}")
    print(f"Runs       : {runs}")
    print(f"Greedy     : total {total_greedy:.6f}s | avg/run {total_greedy / runs:.6f}s")
    print(f"DigitTable : total {total_table:.6f}s | avg/run {total_table / runs:.6f}s")
    print("-" * 60)


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
def main() -> None:
    demo()        # prints inputs and outputs
    benchmark()   # prints timeit timings

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-impact)

1. **UI/UX numbering & branding**
   Display section numbers, chapter indices, or release names (e.g., *Super Bowl LVIII*, *Rocky II*). Roman numerals are a stylistic standard in kiosks, TV overlays, and print.

2. **Clocks & watches**
   Analog clock faces often use Roman numerals (e.g., IIII instead of IV). Converters help render dials correctly in digital/print designs.

3. **Document pagination & outlines**
   Academic/technical documents frequently use Roman numerals for front matter (i, ii, iii, …). A converter standardizes numbering across exports.

4. **Calendars & inscriptions**
   Year inscriptions (e.g., *MMXXV*) on monuments, event posters, film credits. Automatic conversion avoids human mistakes in subtractive notation.

5. **Localization & typesetting tools**
   Editors and templating engines offer numeral styles; Roman numeral conversion is a common formatting directive.

