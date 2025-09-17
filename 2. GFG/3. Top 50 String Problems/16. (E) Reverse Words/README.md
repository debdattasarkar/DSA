# Reverse Words

**Difficulty:** Easy
**Accuracy:** 56.08%
**Submissions:** 387K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Given a string `s`, reverse the string **without reversing its individual words**. Words are separated by spaces.

**Note:**

* The string may contain **leading or trailing spaces**, or **multiple spaces between two words**.
* The returned string should have **a single space** separating the words, and **no extra spaces** should be included.

---

## Examples

### Example 1

**Input:** `s = " i like this program very much "`
**Output:** `"much very program this like i"`
**Explanation:** After removing extra spaces and reversing the whole string (not individual words), the input string becomes `"much very program this like i"`.

---

### Example 2

**Input:** `s = " pqr mno "`
**Output:** `"mno pqr"`
**Explanation:** After removing extra spaces and reversing the whole string, the input string becomes `"mno pqr"`.

---

### Example 3

**Input:** `s = " a "`
**Output:** `"a"`
**Explanation:** The input string contains only one word with extra spaces around it. After removing the extra spaces, the output is `"a"`.

---

## Constraints

* `1 ≤ s.size() ≤ 10^6`
* String `s` contains only **lowercase English alphabets** and **spaces**.

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Paytm, Accolite, Amazon, Microsoft, Samsung, MakeMyTrip, Goldman Sachs, Adobe, SAP Labs, Cisco

---

## Topic Tags

Strings, Data Structures

---

## Related Interview Experiences

* Accolite Interview Experience Set 3 On Campus
* Paytm Interview Experience Set 6 Recruitment Drive
* Paytm Interview Experience Set 11 2 Years Experienced
* Makemytrip Interview Experience Set 6 Online Coding
* Samsung R D Bangalore Intern Interview Experience

---

## Related Articles

* [Reverse Words In A Given String](https://www.geeksforgeeks.org/reverse-words-in-a-given-string/)

---

---

Awesome—let’s lock in the **dot-separated** version (e.g., `i.like.this.program`) and base everything on the **single scan from the end** approach that you validated.

---

## 2) Intuition + step-by-step dry run

### Problem

Reverse the **order of words** in a string where words are separated by **dots (`.`)**.

* Do **not** reverse characters inside a word.
* Collapse multiple dots: no leading, trailing, or consecutive dots in the result.

### Idea (why scanning from the end works)

* Walk right → left.
* Skip dots.
* Read one word (continuous non-dot chars).
* Append that word to the output list.
* Repeat until the start.
* Join collected words with single dots.

This naturally:

* reverses word order,
* ignores extra dots,
* avoids building big intermediate structures beyond the final output.

### Dry run

`s = "i.like.this.program.very.much"`

* Start `i` at the last index.
* Skip dots (none at end).
* Read `much` → add `"much"`.
* Skip dot.
* Read `very` → add `"very"`.
* Skip dot.
* Read `program` → add `"program"`.
* Skip dot.
* Read `this` → add `"this"`.
* Skip dot.
* Read `like` → add `"like"`.
* Skip dot.
* Read `i` → add `"i"`.

Collected words: `["much", "very", "program", "this", "like", "i"]`
Join with dots → **`"much.very.program.this.like.i"`**

Edge dry run (multiple dots):

`s = "a..b...c."`

* Read `c` → add `"c"`
* (skip 1 dot) → (skip 2 more dots)
* Read `b` → add `"b"`
* (skip 2 dots)
* Read `a` → add `"a"`

Result: `"c.b.a"` (no consecutive dots).

---

## 3) Python solutions (brute & optimal)

All versions meet the interview expectations; the first is the one you confirmed.

### A) Single scan from the **end** (no `split`; O(1) aux besides output) ✅

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse order of dot-separated words by scanning from right to left.

        Time  : O(n)  — each character visited at most twice
        Space : O(n)  — for the output; list used as a builder
        """
        n = len(s)
        out_parts = []
        i = n - 1

        while i >= 0:
            # 1) Skip dots (collapses multiple dots)
            while i >= 0 and s[i] == '.':
                i -= 1
            if i < 0:
                break

            # 2) 'j' is the end of the word; find its start
            j = i
            while i >= 0 and s[i] != '.':
                i -= 1

            # 3) Slice the word and append
            out_parts.append(s[i + 1 : j + 1])

        # 4) Join with single dots; no extra dots introduced
        return ".".join(out_parts)
```

### B) Idiomatic one-liner using `split` (concise & accepted in Python)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Use split on '.' and reverse the tokens.
        We filter out empty tokens to collapse multiple dots.

        Time  : O(n)  — split + join
        Space : O(n)  — list of tokens + result
        """
        words = [w for w in s.split('.') if w]  # remove empty chunks from '..'
        return ".".join(words[::-1])
```

### C) Stack approach (clear logic; similar complexity)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Parse left->right, push words to a stack, pop in reverse.

        Time  : O(n)
        Space : O(n)
        """
        stack = []
        i, n = 0, len(s)

        while i < n:
            # Skip dots
            while i < n and s[i] == '.':
                i += 1
            if i >= n:
                break

            # Capture a word
            start = i
            while i < n and s[i] != '.':
                i += 1
            stack.append(s[start:i])

        return ".".join(reversed(stack))
```

> In interviews, **A** shows mastery without relying on `split`, **B** shows Pythonic fluency, and **C** is a good middle ground for clarity.

---

## 4) Interviewer-style Q\&A

**Q1. What’s the time and space complexity?**

* All shown solutions are **O(n)** time.
* Space is **O(n)** due to the output string and (for B/C) the list of words.

**Q2. How do you handle multiple consecutive dots or leading/trailing dots?**

* By skipping dots during parsing (A/C) or filtering empty tokens (B).
  Example: `"a..b...c." → "c.b.a"`.

**Q3. Could you do it “in place”?**

* Python strings are immutable—true in-place is not possible.
* In languages with mutable arrays, you can:

  1. reverse the whole array,
  2. then reverse each word in place,
  3. optionally compact delimiters.

**Q4. Why scan from the end instead of using `split`?**

* To avoid creating a large intermediate token list if memory is tight, and to demonstrate manual parsing—often preferred in interviews for control and robustness.

**Q5. What corner cases would you test?**

* Empty string: `"" → ""`
* Only dots: `"...." → ""`
* Single word: `"abc" → "abc"`
* Leading/trailing/multiple dots: `"..a..b." → "b.a"`
* Very long input (performance check).

---

---

Here’s a complete, runnable program for **Reverse Words (dot-separated)** that:

* Implements the validated **right-to-left single scan** solution.
* Prints sample **inputs → outputs**.
* Benchmarks the function with **`timeit`** (so you get a timing for the full program run).
* Contains **inline comments** explaining **time & space** at each step.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse Words (dot-separated)

Goal:
  Reverse the order of words in a string where words are separated by '.'.
  - Do NOT reverse letters inside words.
  - Collapse multiple dots: no leading/trailing/consecutive dots in the result.

Let n = len(s).

Overall Complexity Targets:
  Time  : O(n)
  Space : O(n)  (you must at least hold the output string)
"""

from __future__ import annotations
import random
import string
import timeit
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse order of dot-separated words by scanning from right to left.

        Time  : O(n) — Each character is visited at most twice:
                        once when skipping '.' and once when reading a word.
        Space : O(n) — For the output; we collect words in a list (builder)
                       and join once at the end (amortized linear).
        """
        n = len(s)                       # O(1)
        out_parts: List[str] = []        # O(1) initially; grows up to O(n) total chars
        i = n - 1                        # O(1) start from the end

        # Main loop: O(n) total
        while i >= 0:
            # 1) Skip any dots (collapses multiple dots)
            #    Each character is tested a constant number of times -> O(n) overall.
            while i >= 0 and s[i] == '.':
                i -= 1
            if i < 0:                    # Only dots or reached beginning
                break

            # 2) j marks the end of a word; move i left to find the word start
            j = i
            while i >= 0 and s[i] != '.':
                i -= 1
            #    Slice the word; slicing copies the substring -> O(k) for that word
            #    Summed across all words equals O(n).
            out_parts.append(s[i + 1 : j + 1])

        # 3) Join words with single dots; join is O(n) over total chars in out_parts
        return ".".join(out_parts)


# -------------- Demo: Sample inputs & outputs -----------------
def demo() -> None:
    sol = Solution()
    samples = [
        "i.like.this.program.very.much",
        "a..b...c.",
        ".single.",
        "....",
        "abc",
        "",
        "geeks.for.geeks",
    ]
    print("=== Sample Runs ===")
    for s in samples:
        print(f"in : {s!r}")
        print(f"out: {sol.reverseWords(s)}")
        print("-" * 40)


# -------------- Benchmark with timeit -------------------------
def _bench_once(batch: List[str], solver: Solution) -> None:
    # Total time is proportional to the sum of lengths of strings in the batch
    for s in batch:
        solver.reverseWords(s)

def _random_dot_string(rng: random.Random, max_words: int, max_word_len: int) -> str:
    # Build a random dot-separated string; inject random runs of dots
    words = []
    for _ in range(rng.randint(0, max_words)):
        wlen = rng.randint(1, max_word_len)
        words.append("".join(rng.choice(string.ascii_lowercase) for _ in range(wlen)))
        # maybe insert extra dots
        if rng.random() < 0.35:
            words.append("." * rng.randint(1, 4))
    # join and then maybe sprinkle leading/trailing dots
    s = ".".join(w for w in words if w and w[0] != '.')
    if rng.random() < 0.5:
        s = "." * rng.randint(1, 3) + s
    if rng.random() < 0.5:
        s = s + "." * rng.randint(1, 3)
    return s

def benchmark() -> None:
    rng = random.Random(2025)
    batch: List[str] = []

    # A balanced batch with small-to-medium strings
    for _ in range(10_000):
        batch.append(_random_dot_string(rng, max_words=6, max_word_len=8))

    # Add a few longer strings to simulate heavy cases
    long_words = ["".join("a" for _ in range(5000)),
                  "".join("b" for _ in range(5000)),
                  "".join("c" for _ in range(5000))]
    long_str = ".".join(long_words) + "...." + ".".join(long_words[::-1])
    batch += [long_str] * 5

    runs = 5
    total = timeit.timeit(lambda: _bench_once(batch, Solution()), number=runs)

    print("=== Benchmark (timeit) ===")
    print(f"Batch size : {len(batch)}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f}s")
    print(f"Avg / run  : {total / runs:.6f}s")
    print("-" * 40)


# -------------- Main ------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **File path / URL component flipping**
   Reverse domain components (`a.b.c.com → com.c.b.a`) or path segments for routing/analytics.

2. **Log parsing & reformatting**
   Reverse dotted identifiers (e.g., `service.region.env`) to prioritize higher-level grouping in dashboards.

3. **Telemetry tag normalization**
   Reverse and normalize tag sequences like `layer.module.component` for consistent sorting/aggregation.

4. **Language processing with custom delimiters**
   Reorder token groups in DSLs or config strings where sections are dot-separated (e.g., feature flags or namespaced keys).

5. **Security/obfuscation utilities**
   Lightweight reordering of dotted tokens before hashing or storing, without altering token content.
