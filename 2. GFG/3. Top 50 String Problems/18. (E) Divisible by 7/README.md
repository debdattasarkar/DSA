# Divisible by 7

**Difficulty:** Easy
**Accuracy:** 49.98%
**Submissions:** 25K+
**Points:** 2

---

## Problem Statement

Given an n-digit large number `n` in the form of a string, check whether it is divisible by 7 or not. Return `1` if divisible by 7, otherwise `0`.

---

## Examples

### Example 1

**Input:** `n = "49"`
**Output:** `1`
**Explanation:** 49 is divisible by 7.

### Example 2

**Input:** `n = "1000"`
**Output:** `0`
**Explanation:** 1000 is not divisible by 7.

---

## Constraints

* `1 ≤ num.size() ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `|n|`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Articles

* [Check Whether Large Number Divisible 7](https://www.geeksforgeeks.org/check-whether-large-number-divisible-7/)

---

---

Here’s a crisp, interview-ready write-up for **Divisible by 7 (number given as a string)**.

---

## 2) Intuition + step-by-step dry run

### Core idea (mod stream)

For a (possibly huge) decimal string `num`, compute the remainder modulo 7 without ever converting the whole thing to an integer:

If `r` is the remainder so far, and the next digit is `d`,
the new remainder is:

```
r' = (r * 10 + d) % 7
```

Why? Because appending a digit in base-10 multiplies the number by 10 and adds `d`. Since `10 ≡ 3 (mod 7)`, this is equivalent to summing digits with powers of 10 mod 7. We only keep the remainder, so memory stays O(1).

Return `1` if the final remainder is `0`, else `0`.

### Dry run 1: `num = "49"`

* Start `r = 0`.
* See `'4'` → `r = (0*10 + 4) % 7 = 4`.
* See `'9'` → `r = (4*10 + 9) % 7 = 49 % 7 = 0`.
* Final remainder is `0` ⇒ **divisible** ⇒ return `1`.

### Dry run 2: `num = "1000"`

* Start `r = 0`.
* `'1'` → `r = 1`.
* `'0'` → `r = (1*10 + 0) % 7 = 10 % 7 = 3`.
* `'0'` → `r = (3*10 + 0) % 7 = 30 % 7 = 2`.
* `'0'` → `r = (2*10 + 0) % 7 = 20 % 7 = 6`.
* Final remainder `6` ⇒ **not divisible** ⇒ return `0`.

> Works for up to 10^5 digits in a single pass, O(1) extra space.

---

## 3) Python solutions (brute & optimal)

### A) Optimal single-pass modulo (most expected)

```python
#User function Template for python3

class Solution:
    def isdivisible7(self, num: str) -> int:
        """
        Stream the digits and keep a running remainder modulo 7.
        Time  : O(n) where n = len(num)
        Space : O(1)
        """
        r = 0
        for ch in num:
            # convert char to digit
            d = ord(ch) - ord('0')      # O(1)
            r = (r * 10 + d) % 7        # O(1)
        return 1 if r == 0 else 0
```

### B) Same logic, a tiny micro-opt (avoid ord in tight loop)

Python’s `int(ch)` is fast enough and readable:

```python
class Solution:
    def isdivisible7(self, num: str) -> int:
        r = 0
        for ch in num:
            r = (r * 10 + int(ch)) % 7
        return 1 if r == 0 else 0
```

### C) “Divisibility rule of 7” flavor (educational, still O(n))

The classic rule says: **remove the last digit, double it, subtract from the rest**; repeat until small. Algebraically this is the same modulo computation, so we can implement it in a streaming way without string arithmetic:

```python
class Solution:
    def isdivisible7(self, num: str) -> int:
        """
        Equivalent to the 'double the last digit and subtract' rule,
        but streamed left->right via modular arithmetic.
        Time : O(n), Space : O(1)
        """
        rem = 0
        for ch in num:
            # appending a digit is rem*10 + d
            d = int(ch)
            rem = (rem * 10 + d) % 7
        return 1 if rem == 0 else 0
```

> In interviews, show **A/B**. If asked about the paper-and-pencil rule, you can explain the equivalence (since 10 ≡ 3 mod 7, keeping remainders suffices).

---

## 4) Interviewer-style Q\&A

**Q1. Why not convert the whole string to an integer and do `% 7`?**
For very large `num` (up to 10^5 digits), conversion can be heavy or disallowed. The streaming remainder method is **O(n) time, O(1) space**, language-agnostic, and scale-friendly. (Python big ints would work but are not ideal in interviews.)

**Q2. Complexity?**

* **Time:** O(n) — one pass over the digits.
* **Space:** O(1) — only a few integer variables.

**Q3. Does it handle leading zeros?**
Yes. Leading zeros contribute nothing: remainder remains correct.

**Q4. What if the input can be negative or has a sign?**
If allowed, strip the sign first. Mod test depends on absolute value; the streaming method is unchanged.

**Q5. Why does the recurrence `r' = (r*10 + d) % 7` work?**
Because appending `d` in base-10 is `10*r + d`. Modulo arithmetic preserves divisibility: `(a + b) % 7 = 0` iff the full number is divisible by 7.

**Q6. Any quick sanity tests?**

* `"0" → 1`, `"7" → 1`, `"14" → 1`, `"21" → 1`, `"28" → 1`, `"49" → 1`
* `"1" → 0`, `"2" → 0`, `"1000" → 0`, `"9999999" → ?` (compute)

---

---

Here’s a complete, runnable program for **Divisible by 7 (string input)** that:

* Implements the expected `class Solution.isdivisible7(self, num)` API
* Has **inline time/space complexity** notes right where work happens
* Prints sample **inputs → outputs**
* Benchmarks with **timeit** for a batch of large random numbers

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Divisible by 7 (string form)

We are given a (possibly huge) non-negative integer as a string.
Return 1 if it is divisible by 7, else 0.

Let n = len(num).

Overall complexities:
  Time  : O(n) — single pass across digits
  Space : O(1) — only a few integer vars; no big-int conversion
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    def isdivisible7(self, num: str) -> int:
        """
        Stream digits and keep a running remainder modulo 7.

        Time (per char): O(1)  (constant work: convert digit + 2 ops + mod)
        Total time     : O(n)  (n = len(num))
        Space          : O(1)  (r and d only)
        """
        r = 0  # O(1) storage
        for ch in num:                 # O(n) iterations
            d = ord(ch) - ord('0')     # O(1) convert character to digit
            r = (r * 10 + d) % 7       # O(1) update remainder
        return 1 if r == 0 else 0


# ------------------------- Demo & Tests -------------------------

def demo() -> None:
    sol = Solution()
    samples = [
        "49",           # -> 1 (49 % 7 == 0)
        "1000",         # -> 0
        "0",            # -> 1
        "7",            # -> 1
        "700",          # -> 1
        "9999999",      # -> ?
        "12345678901234567890",    # large but fits in Python; we still stream
    ]
    print("=== Sample Runs ===")
    for s in samples:
        print(f"in : {s}")
        out = sol.isdivisible7(s)      # O(len(s)) time; O(1) extra space
        print(f"out: {out}")
        print("-" * 32)


# ------------------------- Benchmark ---------------------------

def _random_numeric_string(length: int, *, leading_nonzero: bool = True) -> str:
    """Generate a random numeric string of given length."""
    if length <= 0:
        return "0"
    digits = "0123456789"
    if leading_nonzero:
        first = random.choice("123456789")
        rem = "".join(random.choice(digits) for _ in range(length - 1))
        return first + rem
    else:
        return "".join(random.choice(digits) for _ in range(length))


def _bench_once(batch: List[str]) -> None:
    sol = Solution()
    f = sol.isdivisible7
    for s in batch:     # O(Σ len(s)) time
        f(s)


def benchmark() -> None:
    random.seed(42)

    # Build a mixed batch including long inputs.
    # Keep lengths reasonable for your environment; 50k is typical for this task.
    batch: List[str] = []
    for _ in range(500):
        batch.append(_random_numeric_string(20))
    for _ in range(200):
        batch.append(_random_numeric_string(1_000))
    for _ in range(20):
        batch.append(_random_numeric_string(50_000))

    runs = 5
    total = timeit.timeit(lambda: _bench_once(batch), number=runs)

    print("=== Benchmark (timeit) ===")
    print(f"Batch size : {len(batch)} strings")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f}s")
    print(f"Avg / run  : {total / runs:.6f}s")
    print("-" * 32)


# --------------------------- Main ------------------------------

def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (important ones)

1. **Sharding & Load Balancing on IDs**
   Route huge numeric IDs (possibly string-encoded) across **7 shards** by computing the ID mod 7 in a streaming fashion—no big-int construction, constant memory.

2. **Validation Rules on Large Identifiers**
   Some business pipelines require “ID must be divisible by 7” (or any modulus) before processing; streaming modulo handles **100k-digit** strings safely and quickly.

3. **Memory-Constrained Environments**
   Embedded/edge devices can check divisibility without allocating big integers—**O(1)** memory and one pass over the digits.

4. **Data Ingestion & Normalization**
   While parsing large CSV/JSON logs with numeric fields stored as strings, you can compute remainders inline to pre-bucket or filter records efficiently.
