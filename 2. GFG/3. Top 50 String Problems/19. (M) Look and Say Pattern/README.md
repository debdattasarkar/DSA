# Look and Say Pattern

**Difficulty:** Medium
**Accuracy:** 62.54%
**Submissions:** 47K+
**Points:** 4

---

## Problem Statement

Given an integer **n**, return the **n**th row of the following look-and-say pattern.

```
1
11
21
1211
111221
```

### Look-and-Say Pattern:

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

* `1` is read off as **"one 1"** → `11`.
* `11` is read off as **"two 1s"** → `21`.
* `21` is read off as **"one 2, then one 1"** → `1211`.
* `1211` is read off as **"one 1, one 2, then two 1s"** → `111221`.
* `111221` is read off as **"three 1s, two 2s, then one 1"** → `312211`.

---

## Examples

### Example 1

**Input:** `n = 5`
**Output:** `111221`
**Explanation:** The **5**th row of the given pattern will be `111221`.

### Example 2

**Input:** `n = 3`
**Output:** `21`
**Explanation:** The **3**rd row of the given pattern will be `21`.

---

## Constraints

* `1 ≤ n ≤ 30`

---

## Expected Complexities

* **Time Complexity:** `O(2^n)`
* **Auxiliary Space:** `O(2^n)`

---

## Company Tags

Zoho, Amazon, Microsoft, Facebook

---

## Topic Tags

Strings, pattern-printing, Data Structures

---

## Related Articles

* [Look And Say Sequence](https://www.geeksforgeeks.org/look-and-say-sequence/)

---

---

Here’s a compact, interview-ready guide to the **Look-and-Say** / **Count-and-Say** problem.

---

## 2) Intuition + step-by-step dry run

### Problem recap

Start from `"1"`. To get the next row, **read the previous row aloud** by counting **consecutive equal digits** and writing `count + digit`.

Example progression:

```
1
11          # one 1
21          # two 1s
1211        # one 2, one 1
111221      # one 1, one 2, two 1s
```

### How to build “next” from a row

Scan left → right:

* keep a `count` of the current run of identical digits,
* when the digit changes (or at the end), append `str(count)` and the digit to a builder,
* reset `count = 1` for the new digit.

### Dry run for n = 5

We iterate 4 times starting from `"1"`:

1. start = `"1"`

* row 1 → `"1"`

2. build next from `"1"`

* run: `'1'` occurs 1 time ⇒ append `"11"`
* row 2 → `"11"`

3. build next from `"11"`

* run: `'1'` occurs 2 times ⇒ append `"21"`
* row 3 → `"21"`

4. build next from `"21"`

* `'2'` occurs 1 → append `"12"`
* `'1'` occurs 1 → append `"11"`
* row 4 → `"1211"`

5. build next from `"1211"`

* `'1'` occurs 1 → `"11"`
* `'2'` occurs 1 → `"12"`
* `'1'` occurs 2 → `"21"`
* row 5 → **`"111221"`**

---

## 3) Python solutions (two common ways)

### A) Iterative build with a single pass per row (most expected)

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term by iterating from the seed "1".

        Let L_k be the length of the k-th term; L_k grows ~ O(1.3^k).
        Time  : proportional to total characters processed
                = sum_{i=1..n} L_i  (≈ exponential in n; n ≤ 30 is fine)
        Space : O(L_n) for the final string / current builder
        """
        term = "1"                           # row 1
        for _ in range(1, n):                # build n-1 times
            i, m = 0, len(term)
            out_parts = []                   # use list builder (amortized O(1) append)
            while i < m:
                j = i
                # count run of the same digit
                while j < m and term[j] == term[i]:
                    j += 1
                count = j - i
                out_parts.append(str(count)) # append "count" then the digit
                out_parts.append(term[i])
                i = j
            term = "".join(out_parts)        # O(length of next term)
        return term
```

### B) Using `itertools.groupby` (concise & pythonic)

```python
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Same complexity profile; groupby clusters consecutive equal chars.
        """
        term = "1"
        for _ in range(1, n):
            pieces = []
            for digit, group in groupby(term):    # each group is a run of 'digit'
                cnt = sum(1 for _ in group)       # size of that run
                pieces.append(str(cnt))
                pieces.append(digit)
            term = "".join(pieces)
        return term
```

> Notes for interviews
> • The **iterative run-count** method (A) is the standard approach.
> • Use a **list builder + join** to avoid O(n²) string concatenations.
> • Time is dominated by the size of generated strings (exponential growth), but `n ≤ 30` is well within limits.

---

## 4) Interviewer-style Q\&A

**Q1. What’s the time and space complexity?**
Let `L_k` be the length of the k-th term. The work to build row `k+1` is `Θ(L_k)`. So total time is `Θ(Σ L_i)` for `i=1..n-1`. Empirically, `L_k` grows by \~1.3× each step (Conway’s constant ≈ 1.30357 for asymptotics). Space is `Θ(L_n)` to hold the final row and the current builder.

**Q2. Why use a list and then `"".join()` instead of concatenating strings?**
In Python, repeated `s += piece` can be quadratic due to immutability. Appending to a list and joining once is linear in the final length.

**Q3. Any off-by-one pitfalls?**
Yes—ensure you flush the last run when the loop ends. The two-pointer or `groupby` patterns naturally do this.

**Q4. Can we do it recursively?**
You can (define `f(1)="1"` and `f(n)=say(f(n-1))`), but you’ll still materialize intermediate strings; iterative is simpler and avoids recursion depth concerns.

**Q5. Will digits other than 1 and 2 appear?**
Yes—later rows will include other digits (e.g., `3` from “three 1s”), but the process still counts runs of **equal digits**, not numeric values.

**Q6. Memory optimizations?**
Beyond list builders and reusing buffers, not much—each term depends on the full previous term, so you must store at least `O(L_{k})` characters while generating `L_{k+1}`.

---

---

Below is a complete, runnable **Look-and-Say / Count-and-Say** program that:

* Implements the expected `class Solution.countAndSay(self, n)` API
* Clearly marks **time/space complexity** at each step
* Runs a **demo** with inputs → outputs
* Benchmarks with **timeit**

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Look-and-Say / Count-and-Say

Given n (1 ≤ n ≤ 30), return the nth term of the sequence beginning at "1",
where each next term is formed by reading the previous term as counts of
consecutive equal digits (run-length speak).

Let L_k denote the length of the k-th term. Empirically L_k grows by ~1.30357^k
(Conway's constant). For n ≤ 30 this is totally fine.

Overall complexity when generating up to n:
  Time  : Θ(sum_{i=1..n-1} L_i)  ~ exponential in n
  Space : Θ(L_n)                 (must hold current and next term)
"""

from __future__ import annotations
import timeit
from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Iteratively build the sequence from the seed "1".

        For each step k -> k+1:
          - We make a single left-to-right pass over the current term (length L_k).
          - We build the next term with a list builder and one final join.

        Per-step complexity:
          Time  : Θ(L_k)   (scan runs and append two small strings per run)
          Space : Θ(L_{k+1}) for the builder of the next term
        """
        term = "1"                      # Start (k = 1), O(1) space
        for _ in range(1, n):           # Repeat n-1 times to reach term n
            i, m = 0, len(term)         # O(1)
            out: List[str] = []         # Builder; amortized O(1) per append
            # ---- Single pass over current term: Θ(L_k) ----
            while i < m:
                j = i
                # Count a run of the same digit: moves i forward once total
                while j < m and term[j] == term[i]:
                    j += 1
                run_len = j - i         # O(1)
                out.append(str(run_len))
                out.append(term[i])
                i = j
            # Join builder to produce the next term in Θ(L_{k+1}) time
            term = "".join(out)
        return term


# ------------------------- Demo -------------------------

def demo() -> None:
    sol = Solution()
    tests = [1, 2, 3, 4, 5, 6, 7, 10]
    print("=== Sample Runs ===")
    for n in tests:
        out = sol.countAndSay(n)  # Θ(Σ L_i) up to i=n-1
        print(f"n = {n:>2}  ->  {out}")
    print("-" * 50)


# ----------------------- Benchmark ----------------------

def _bench_once(ns: List[int]) -> None:
    sol = Solution()
    for n in ns:
        sol.countAndSay(n)

def benchmark() -> None:
    # Mix several n values (repeat to get a stable measurement)
    ns = [5, 10, 15, 20, 25, 30] * 10  # adjust if you want faster/slower runs
    runs = 5
    total = timeit.timeit(lambda: _bench_once(ns), number=runs)

    print("=== Benchmark (timeit) ===")
    print(f"Calls   : {len(ns)} per run")
    print(f"Runs    : {runs}")
    print(f"Total   : {total:.6f}s")
    print(f"Avg/run : {total / runs:.6f}s")
    print("-" * 50)


# ------------------------- Main -------------------------

def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (important ones)

1. **Run-Length “Speech” / Descriptive Encoding**
   The transformation is a cousin of run-length encoding (RLE): count consecutive equal symbols and emit `(count, symbol)`. While Look-and-Say is a toy sequence, understanding and implementing it cleanly maps directly to designing efficient **RLE compressors**, log summarizers, or histogram-by-runs tools.

2. **Streaming Parsers for Token Runs**
   The “read consecutive equal tokens, then flush” pattern appears in **parsers**, **lexers**, and **data cleaners** (e.g., collapsing repeated spaces, merging identical events). The same two-pointer technique keeps code linear and memory-friendly.

3. **Data Generation / Testing**
   Look-and-Say rapidly generates structured, growing test data that stresses string builders, joins, and memory usage—useful for **performance tests** of text pipelines or UI components.
