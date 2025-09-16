# Panagram Checking

**Difficulty:** Easy
**Accuracy:** 61.34%
**Submissions:** 90K+
**Points:** 2
**Average Time:** 30m

---

## Problem Statement

Given a string `s`, check if it is a **"Panagram"** or not. Return **true** if the string is a Panagram, else return **false**.
A **"Panagram"** is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.

---

## Examples

### Example 1

**Input:** `s = "Bawds jog, flick quartz, vex nymph"`
**Output:** `true`
**Explanation:** In the given string, there are all the letters of the English alphabet. Hence, the output is true.

### Example 2

**Input:** `s = "sdfs"`
**Output:** `false`
**Explanation:** In the given string, there aren't all the letters present in the English alphabet. Hence, the output is false.

---

## Constraints

* `1 ≤ |s| ≤ 10^4`
* `s` consists only lowercase and uppercase letters

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Articles

* [Pangram Checking](https://www.geeksforgeeks.org/pangram-checking/)

---

---

Here’s an interview-ready pack for **Pangram Checking**.

---

## 2) Intuition + dry run

A string is a **pangram** if it contains **every letter ‘a’..‘z’ at least once**, case-insensitive.

### Core idea

Scan once, mark which letters you’ve seen. When all **26** are seen, return `True`.

### Quick pruning

If `len(s) < 26` (and the alphabet is exactly 26 English letters), it can’t be a pangram → `False`.

### Step-by-step dry run (set version)

`s = "Bawds jog, flick quartz, vex nymph"`

* Normalize: treat letters case-insensitively and skip non-letters.
* Walk through characters, add their lowercase to a `seen` set.

Progress snapshots:

* After `"Bawds"` → `{a, b, d, s, w}` (size 5)
* After `" jog"` → `... ∪ {g, j, o}` (size 8)
* After `" flick"` → `... ∪ {c, f, i, k, l}` (size 13)
* After `" quartz"` → `... ∪ {q, r, t, u, z}` (size 18)
* After `" vex"` → `... ∪ {e, v, x}` (size 21)
* After `" nymph"` → `... ∪ {h, m, n, p, y}` (size **26**) → all letters present → **True**.

---

## 3) Python solutions (expected + alternatives)

### A) Set / early exit (most expected) — **O(n) time, O(1) space**

```python
class Solution:
    def checkPangram(self, s: str) -> bool:
        """
        Time : O(n) — single pass
        Space: O(1) — at most 26 letters in the set
        """
        if len(s) < 26:                 # quick prune for English alphabet
            return False

        seen = set()                    # holds lowercase letters found (≤26)
        for ch in s:
            if 'A' <= ch <= 'Z':        # uppercase letter → normalize
                ch = chr(ord(ch) + 32)  # to lowercase
            if 'a' <= ch <= 'z':        # ignore non-letters defensively
                seen.add(ch)
                if len(seen) == 26:     # early exit
                    return True
        return len(seen) == 26
```

### B) Bitmask (tight O(1) memory) — **O(n) / O(1)**

Use a 26-bit integer; set bit `i` when letter `i` appears.

```python
class SolutionBit:
    def checkPangram(self, s: str) -> bool:
        """
        Time : O(n)
        Space: O(1) — single integer bitmask
        """
        mask = 0
        full = (1 << 26) - 1            # all 26 bits set
        for ch in s:
            # normalize to lowercase letter index 0..25 if applicable
            if 'A' <= ch <= 'Z':
                idx = ord(ch) - ord('A')
            elif 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
            else:
                continue
            mask |= 1 << idx
            if mask == full:            # early exit once all letters seen
                return True
        return mask == full
```

### C) Boolean array (clear & fast) — **O(n) / O(1)**

```python
class SolutionArray:
    def checkPangram(self, s: str) -> bool:
        """
        Time : O(n)
        Space: O(1) — fixed 26-length array
        """
        seen = [False] * 26
        count = 0
        for ch in s:
            if 'A' <= ch <= 'Z':
                idx = ord(ch) - ord('A')
            elif 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
            else:
                continue
            if not seen[idx]:           # count each letter once
                seen[idx] = True
                count += 1
                if count == 26:         # early exit
                    return True
        return count == 26
```

> In interviews, **A (set)** is most common and perfectly acceptable. If you want to flex, mention **B (bitmask)** for constant-word memory and branchless tricks.

---

## 4) Interviewer-style Q\&A

**Q1. Why can we return `False` when `len(s) < 26`?**
Because you need at least 26 characters to cover 26 distinct letters (assuming only letters matter). Even with repeats, fewer than 26 total characters can’t supply 26 unique letters.

**Q2. Time and space complexity?**
All variants scan once → **O(n)** time. Space is **O(1)**: the set holds ≤26 letters; the array has fixed 26 slots; the bitmask is a single integer.

**Q3. How do you handle case and punctuation?**
Normalize with lowercase (or detect both ranges) and ignore non-alphabetic characters. If inputs are guaranteed letters only, the checks still work.

**Q4. What if the alphabet isn’t English or includes accented letters?**
Generalize: maintain a set of required characters and check coverage against that set (perhaps derived from locale). Complexity stays linear in string length.

**Q5. Can you short-circuit?**
Yes—once you’ve seen all 26 letters, return immediately (present in the code above).

**Q6. Why prefer bitmask over set?**
Bitmask uses **less overhead** (one integer) and is cache-friendly; it’s a nice optimization / systems-level demonstration. Sets are simpler to write and read.

**Q7. Edge cases?**

* Empty string → `False`.
* String with exactly 26 letters but with duplicates → might still be `False` if one letter is missing.
* Strings with unicode letters beyond ASCII: treat explicitly or normalize (`unicodedata.normalize`) if required.

---

---

Here’s a **complete, runnable Python program** for **Pangram Checking** that

* implements the required `class Solution.checkPangram(self, s)` (set-based O(n)),
* includes a bitmask variant for comparison,
* prints **inputs → outputs** for sample cases, and
* **benchmarks** the solution using `timeit` in `main`.

Inline comments call out **time & space complexity** at each step.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pangram Checking
----------------
Return True if a string contains every English letter 'a'..'z' at least once,
case-insensitively; otherwise False.

Let n = len(s).
Overall complexities (set-based solution):
  Time  : O(n)   — single pass, constant work per char
  Space : O(1)   — at most 26 letters stored (constant bound)
"""

from __future__ import annotations
import random
import string
import timeit
from typing import List


# -----------------------------------------------------------
# Required interface — set-based solution (most expected)
# -----------------------------------------------------------
class Solution:
    def checkPangram(self, s: str) -> bool:
        """
        Scan once; collect seen lowercase letters in a set.

        Steps and complexity:
          A) Quick length prune           -> O(1)
          B) Single pass over characters  -> O(n)
             - normalize case             -> O(1)
             - add letter to set          -> O(1) average
             - early exit when 26 seen    -> O(1)
          C) Final check                  -> O(1)
        Total: O(n) time, O(1) space.
        """
        # A) If fewer than 26 total chars, can't contain 26 distinct letters.
        # (Strictly speaking this is a heuristic prune; it's correct when s
        # contains only letters, but harmless and fast regardless.)
        if len(s) < 26:
            return False

        seen = set()  # holds unique letters; size is capped at 26 -> O(1) space
        for ch in s:  # B) O(n) iterations
            # Normalize to lowercase; ignore non-letters defensively
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + 32)  # to lowercase, O(1)
            if 'a' <= ch <= 'z':
                seen.add(ch)  # O(1) average
                if len(seen) == 26:  # early exit once all letters observed
                    return True

        # C) Return whether all 26 letters were seen
        return len(seen) == 26


# -----------------------------------------------------------
# Optional: bitmask variant (tight O(1) memory)
# -----------------------------------------------------------
class SolutionBit:
    def checkPangram(self, s: str) -> bool:
        """
        Maintain a 26-bit mask; set bit when letter appears.
        Time O(n), Space O(1) (single integer).
        """
        mask = 0
        full = (1 << 26) - 1  # all 26 bits set
        for ch in s:
            if 'A' <= ch <= 'Z':
                idx = ord(ch) - ord('A')  # O(1)
            elif 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')  # O(1)
            else:
                continue
            mask |= 1 << idx              # O(1)
            if mask == full:              # early exit
                return True
        return mask == full


# -----------------------------------------------------------
# Demo: sample inputs & outputs
# -----------------------------------------------------------
def demo() -> None:
    sol = Solution()
    cases = [
        ("Bawds jog, flick quartz, vex nymph", True),   # classic pangram
        ("TheQuickBrownFoxJumpsOverTheLazyDog", True),  # another pangram
        ("sdfs", False),                                 # too short / missing letters
        ("aaaaaaaaaaaaaaaaaaaaaaaaaa", False),           # only 'a's
    ]
    print("=== Sample Runs (Pangram Checking) ===")
    for s, expected in cases:
        out = sol.checkPangram(s)  # O(n)
        print(f"Input: {s!r}\nOutput: {out} | Expected: {expected}\n" + "-" * 60)


# -----------------------------------------------------------
# Benchmark with timeit (measures full function runtime)
# -----------------------------------------------------------
def _bench_once(strings: List[str], solver) -> None:
    # Evaluate a batch; total cost is O(sum(len(s))) across batch.
    for s in strings:
        solver.checkPangram(s)

def benchmark() -> None:
    rng = random.Random(2025)

    # Build a batch of random strings, length ~120; sprinkle some pangrams.
    def make_random_string() -> str:
        # Mostly letters + spaces to mimic natural text
        chars = string.ascii_letters + "     "
        return "".join(rng.choice(chars) for _ in range(120))

    batch = [make_random_string() for _ in range(15_000)]  # batch size
    # Insert a few known pangrams to ensure True cases are present
    pangrams = [
        "Sphinx of black quartz, judge my vow",
        "Pack my box with five dozen liquor jugs",
        "The quick onyx goblin jumps over the lazy dwarf"
    ]
    for i, p in enumerate(pangrams):
        batch[i] = p

    runs = 10

    # Benchmark set-based solution
    total_set = timeit.timeit(lambda: _bench_once(batch, Solution()), number=runs)

    # Benchmark bitmask solution
    total_bit = timeit.timeit(lambda: _bench_once(batch, SolutionBit()), number=runs)

    print("=== Benchmark (higher is slower) ===")
    print(f"Batch size : {len(batch)}")
    print(f"Runs       : {runs}")
    print(f"Set-based  : total {total_set:.6f}s | avg/run {total_set / runs:.6f}s")
    print(f"Bitmask    : total {total_bit:.6f}s | avg/run {total_bit / runs:.6f}s")
    print("-" * 60)


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------
def main() -> None:
    demo()
    benchmark()

if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **Content quality gates**
   Quickly verify that practice sentences or language-learning exercises contain **all letters** to ensure broad coverage of glyphs.

2. **Font/rendering smoke tests**
   Pangram lines (e.g., “The quick brown fox…”) are used to **validate fonts** and layout engines—checking that all alphabetic glyphs render.

3. **Keyboard & IME diagnostics**
   Use pangram prompts to confirm **all keys/input mappings** work (especially in kiosk or embedded devices).

4. **Data normalization**
   In OCR or transcription pipelines, pangram checks help flag lines meant to test **character coverage** versus normal prose for specialized handling.
