# Encrypt the string - 2

**Difficulty:** Easy
**Accuracy:** 42.25%
**Submissions:** 20K+
**Points:** 2

---

## Problem Statement

You are given a string **S**. Every sub-string of **identical letters** is replaced by:

* a single instance of that letter **followed by** the **hexadecimal representation** of the number of occurrences of that letter.

Then, the string thus obtained is **further encrypted by reversing it**.
Print the **Encrypted String**.

**Note:** All hexadecimal letters should be converted to **lowercase** letters.

---

## Examples

### Example 1

**Input:**
`S = "aaaaaaaaaaa"`

**Output:**
`ba`

**Explanation:**

```
aaaaaaaaaaa
Step1: a11   (a occurs 11 times)
Step2: a11 is ab  [since 11 is b in hexadecimal]
Step3: ba    [After reversing]
```

---

### Example 2

**Input:**
`S = "abc"`

**Output:**
`1c1b1a`

**Explanation:**

```
abc
Step1: a1b1c1
Step2: 1c1b1a [After reversing]
```

---

### Example 3

**Input:**
`S = "abc"`

**Output:**
`1c1b1a`

**Explanation:**

```
abc
Step1: a1b1c1
Step2: 1c1b1a [After reversing]
```

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`encryptString()`** which takes a String **S** and returns the answer.

---

## Expected Complexities

* **Time Complexity:** `O(|S|)`
* **Expected Auxiliary Space:** `O(1)`

---

## Constraints

`1 ≤ |S| ≤ 10^5`

---

## Topic Tags

Strings, Greedy, Data Structures, Algorithms

---

## Related Articles

* [Encrypt The String 2](https://www.geeksforgeeks.org/encrypt-the-string-2/)

---

---

Absolutely—let’s base everything on the **judge-passing approach** (build the final, reversed encoding directly from right→left so multi-digit hex counts keep their digit order).

---

## 2) Intuition + step-by-step dry run

### Problem recap

For a string `S`, compress each **maximal run** of the same character into
`<letter><hex(count)>` (hex digits must be **lowercase**).
Then **reverse the whole encoded string** and return it.

### Subtlety that breaks many solutions

If you “encode forward” to something like `a10` and then reverse the entire string, you get `01a` (digits reversed as well).
But the expected answer wants only the **order of runs** reversed—**not the order of the hex digits** inside a count.

### Clean trick

Build the final answer **directly from the end** of `S`:

* Scan **right → left**.
* For each backward run of character `c` with frequency `cnt`, **append** `hex(cnt)` and then `c`.
* Since you’re consuming runs from the end, the final string is already “reversed by runs”, and the **hex digits stay in order**.

### Dry run 1 (classic)

`S = "aaaaaaaaaaa"` (11 a’s)

* Rightmost run: `a × 11` → hex(11) = `"b"` → append `"b"` + `"a"` → `"ba"`
  Final: `"ba"`

### Dry run 2 (multi-digit hex, the pitfall)

`S = "a" * 16 + "b" * 2`

* Rightmost run: `b × 2` → `"2b"`
* Next run: `a × 16` → hex(16) = `"10"` → append `"10a"`
  Final: `"2b10a"`  ✅
  (Wrong approach would have produced `2b01a`.)

### Dry run 3 (mixed)

`S = "aabbbbccde"`
Backward runs:

* `e×1 → "1e"`
* `d×1 → "1d"`
* `c×2 → "2c"`
* `b×4 → "4b"`
* `a×2 → "2a"`
  Final: `"1e1d2c4b2a"`

---

## 3) Optimized Python solutions (expected in interviews)

### A) Judge-passing, one pass from the end (recommended)

```python
#User function Template for python3

class Solution:
    def encryptString(self, S):
        """
        Build the final (reversed) encoding directly:
          - Scan from right to left.
          - For each run, append hex(count) then the character.
        Time  : O(n)  (each character visited once)
        Space : O(n)  (output buffer; join is linear)
        """
        n = len(S)
        if n == 0:
            return ""

        out = []
        i = n - 1
        while i >= 0:
            j = i - 1
            # Count the backward run of S[i]
            while j >= 0 and S[j] == S[i]:
                j -= 1
            cnt = i - j                 # occurrences in this run
            out.append(format(cnt, "x"))  # lowercase hex (e.g., 16 -> "10")
            out.append(S[i])              # then the character
            i = j                         # move to previous run
        return "".join(out)
```

### B) Forward scan **without** the digit-reversal bug

Encode runs as pieces (e.g., `"a10"`, `"b2"`) into a list, then **reverse the list of pieces** (not the whole string). This reverses runs while preserving multi-digit hex order.

```python
class SolutionForwardPieces:
    def encryptString(self, S):
        """
        Forward RLE but reverse the LIST OF PIECES, not the final string.
        Time  : O(n)
        Space : O(n)
        """
        n = len(S)
        if n == 0:
            return ""

        pieces = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and S[j] == S[i]:
                j += 1
            cnt = j - i
            pieces.append(S[i] + format(cnt, "x"))  # 'a' + '10', etc.
            i = j

        # Reverse the order of runs only
        pieces.reverse()
        return "".join(pieces)
```

### C) Tuple runs → generate in reverse (clear intent)

Produce `(char, count)` tuples forward, then render them in reverse as `hex(count)+char`.

```python
class SolutionRuns:
    def encryptString(self, S):
        """
        Build (char, count) runs first; render reversed as hex(count)+char.
        Time  : O(n)
        Space : O(n)
        """
        n = len(S)
        if n == 0:
            return ""

        runs = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and S[j] == S[i]:
                j += 1
            runs.append((S[i], j - i))
            i = j

        out = []
        for ch, cnt in reversed(runs):
            out.append(format(cnt, "x"))
            out.append(ch)
        return "".join(out)
```

> In an interview, **A** is the most succinct and performant; **B/C** show you understand the pitfall and how to avoid it.

---

## 4) Interviewer-style Q\&A

**Q1. Why did the “encode-then-reverse” approach fail?**
Because reversing the **entire** string flips the **hex digits** inside multi-digit counts.
Example: `a×16 → "a10"` becomes `"01a"`, but the expected output wants runs reversed while **keeping digits in order** → `"10a"`.

**Q2. How do you ensure lowercase hex?**
Use `format(cnt, 'x')` (or `hex(cnt)[2:]` and `.lower()`). The `'x'` specifier emits lowercase.

**Q3. What are the time/space complexities?**
All provided solutions are **O(n)** time and **O(n)** space (you must at least store the output). Each character is visited a constant number of times.

**Q4. Any edge cases?**

* Empty string → `""`.
* Single char → `"1c"`.
* Very large counts (≥16, ≥256, …) produce multi-digit hex; the methods above preserve digit order.
* Mixed case or non-letters still work; the spec treats “identical letters” generally as identical characters.

**Q5. Can we do O(1) extra space?**
Beyond the output itself, yes: the algorithms only keep a few counters and a list for output. Python strings are immutable, so we collect in a list and `join()` once.

**Q6. How would you unit test this?**

* Minimal: `""`, `"a"`, `"aa"`, `"aaa"`.
* Multi-digit hex: `"a"*16`, `"a"*31`, `"a"*32 + "b"*16`.
* Mixed runs: `"aabbbbccde"`.
* Random long inputs to ensure linear performance.

---

---

Here’s a complete, runnable program for **Encrypt the string – 2** that:

* Implements the required `class Solution.encryptString(self, S)` (forward RLE + reverse).
* Also includes an optimized **one-pass-from-the-end** variant (produces reversed result directly).
* Prints sample **inputs → outputs**.
* Benchmarks both methods with **`timeit`**.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Encrypt the string – 2

Spec:
1) Replace each maximal run of identical letters with: letter + hex(count)  (hex in lowercase).
2) Reverse the whole resulting string.

Let n = len(S).
Overall target: O(n) time, O(n) output space.
"""

from __future__ import annotations
import random
import string
import timeit
from typing import List


# ------------------------------------------------------------
# Required interface (most expected in interviews)
# RLE forward, then reverse once at the end.
# ------------------------------------------------------------
class Solution:
    def encryptString(self, S: str) -> str:
        """
        Time  : O(n) — single pass to build runs + O(n) reverse
        Space : O(n) — output buffer (list -> joined string)
        """
        n = len(S)                # O(1)
        if n == 0:                # O(1) edge case
            return ""

        pieces: List[str] = []    # O(1) to allocate; grows to O(n) output
        i = 0
        while i < n:              # O(n) total iterations across all runs
            j = i + 1
            # Count run length for S[i]
            while j < n and S[j] == S[i]:  # Each char compared once overall -> O(n)
                j += 1
            cnt = j - i           # O(1)
            # Append letter + lowercase hex of count; format(..., 'x') is O(1)
            pieces.append(S[i] + format(cnt, "x"))
            i = j                 # Move to next run, O(1)

        encoded = "".join(pieces) # O(n) join of collected pieces
        return encoded[::-1]      # O(n) reverse


# ------------------------------------------------------------
# Alternative: scan from the END; produce reversed answer directly.
# (avoids the final reverse)
# ------------------------------------------------------------
class SolutionRevOnePass:
    def encryptString(self, S: str) -> str:
        """
        Time  : O(n) — single backward pass
        Space : O(n) — output only
        """
        n = len(S)                 # O(1)
        if n == 0:                 # O(1)
            return ""

        out: List[str] = []
        i = n - 1
        while i >= 0:              # O(n) total
            j = i - 1
            # Count backward run of S[i]
            while j >= 0 and S[j] == S[i]:   # Each char visited once overall -> O(n)
                j -= 1
            cnt = i - j            # O(1) occurrences in this run
            # For the reversed final string we need: hex(count) + char
            out.append(format(cnt, "x"))     # O(1)
            out.append(S[i])                 # O(1)
            i = j
        return "".join(out)         # O(n)


# ------------------------------------------------------------
# Demo: sample cases (prints input and output)
# ------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    sol2 = SolutionRevOnePass()

    samples = [
        "aaaaaaaaaaa",   # -> "ba"
        "abc",           # -> "1c1b1a"
        "aabbbbccde",    # -> "1e1d2c4b2a"
        "z",             # -> "1z"
        "",              # -> ""
        "aaaaaBBBBBccCCC"  # mixed case still works; counts use hex
    ]

    print("=== Sample Runs ===")
    for s in samples:
        out1 = sol.encryptString(s)
        out2 = sol2.encryptString(s)
        print(f"S={s!r}\n  forward+reverse -> {out1}\n  rev-one-pass    -> {out2}\n" + "-"*60)


# ------------------------------------------------------------
# Benchmark with timeit
# ------------------------------------------------------------
def _bench_once(batch: List[str], solver) -> None:
    # Total work ~ O(sum(len(S))) across the batch
    for s in batch:
        solver.encryptString(s)

def benchmark() -> None:
    rng = random.Random(2025)

    # Build a batch with varied lengths up to ~1e5 to reflect constraints
    batch: List[str] = []

    # Some small strings
    for _ in range(5000):
        n = rng.randint(1, 40)
        run_char = rng.choice(string.ascii_letters)
        # Mix runs so we exercise RLE logic
        s = "".join(run_char if rng.random() < 0.5 else rng.choice(string.ascii_letters)
                    for _ in range(n))
        batch.append(s)

    # A couple of near-worst-case long runs (close to 1e5)
    batch.append("a" * 100_000)
    batch.append(("ab" * 50_000))  # alternating runs of length 1

    runs = 5

    t1 = timeit.timeit(lambda: _bench_once(batch, Solution()), number=runs)
    t2 = timeit.timeit(lambda: _bench_once(batch, SolutionRevOnePass()), number=runs)

    print("=== Benchmark (higher is slower) ===")
    print(f"Batch size : {len(batch)}")
    print(f"Runs       : {runs}")
    print(f"Forward+Reverse : total {t1:.6f}s | avg/run {t1 / runs:.6f}s")
    print(f"Rev One-Pass    : total {t2:.6f}s | avg/run {t2 / runs:.6f}s")
    print("-"*60)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **Lightweight telemetry/log compaction**
   When fields often repeat characters (e.g., delimiter stretches, padding), a simple RLE-like transform plus a fixed post-processing step (reverse) can reduce size and provide mild obfuscation.

2. **Checksum-friendly tagging**
   Encoding counts in hex creates an ASCII-safe, deterministic tag for repeated symbols. Reversing ensures variation near the front (useful for prefix-based sampling/indexing).

3. **Stream sanity checks & fuzzing**
   RLE+hex offers a quick way to confirm that parsers correctly handle long runs, multi-digit counts (e.g., 0x10, 0x1f), and boundary cases—handy in robustness testing.

4. **Human-readable compact notations**
   For UI traces or diffs where repeated characters occur (e.g., whitespace runs), “char + hex(count)” yields short, readable summaries without binary encoders.

