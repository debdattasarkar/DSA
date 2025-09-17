# License Key Formatting

**Difficulty:** Easy
**Accuracy:** 47.72%
**Submissions:** 29K+
**Points:** 2

---

## Problem Statement

Given a string `S` that consists of only alphanumeric characters and dashes. The string is separated into `N + 1` groups by `N` dashes. Also given an integer `K`.

We want to reformat the string `S`, such that **each group contains exactly `K` characters**, except for the **first group**, which could be shorter than `K` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and **you should convert all lowercase letters to uppercase**.

Return the reformatted string.

---

## Examples

### Example 1

**Input:**
`S = "5F3Z-2e-9-w", K = 4`
**Output:**
`"5F3Z-2E9W"`
**Explanation:**
The string `S` has been split into two parts, each part has 4 characters. Note that two extra dashes are not needed and can be removed.

---

### Example 2

**Input:**
`S = "2-5g-3-J", K = 2`
**Output:**
`"2-5G-3J"`
**Explanation:**
The string `s` has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`ReFormatString()`** which takes a string `S` and an integer `K` as input and returns the reformatted string.

---

## Expected Complexities

* **Time Complexity:** `O(N)`
* **Auxiliary Space:** `O(N)`

---

## Constraints

* `1 ≤ S.length() ≤ 10^5`
* `1 ≤ K ≤ 10^4`

---

## Company Tags

* `Google`

---

## Topic Tags

* `Strings`, `Data Structures`

---

## Related Articles

* [License Key Formatting](https://www.geeksforgeeks.org/license-key-formatting/)

---

---

Here’s an interview-ready solution set for **License Key Formatting**.

---

## 2) Intuition + step-by-step dry run

### Problem recap

Given a string `S` with alphanumerics and dashes, and an integer `K`, reformat so that:

* All letters become **uppercase**.
* All **dashes are removed**, then reinserted to separate groups.
* Groups from **left→right** contain exactly **K** chars, **except the first group**, which may be shorter (but ≥1).

### Key idea

It’s easiest to:

1. **Strip dashes** and **uppercase** → `clean`.
2. Let `n = len(clean)`. The first group’s length is
   `first = n % K` (if `first == 0` and `n > 0`, use `first = K`).
3. Return: `clean[:first]` + `-` + each `K`-sized chunk of the rest.

This avoids reversing characters and keeps the first group potentially short.

### Dry run

`S = "5F3Z-2e-9-w"`, `K = 4`

1. Remove dashes + uppercase → `clean = "5F3Z2E9W"`, `n = 8`.
2. `first = n % K = 8 % 4 = 0` ⇒ use `first = 4`.
3. Build:

   * First group: `"5F3Z"`
   * Remaining in chunks of 4: `"2E9W"`
4. Join with dashes: **`"5F3Z-2E9W"`**.

Another: `S = "2-5g-3-J"`, `K=2`
`clean="25G3J" (n=5)`, `first = 5%2=1` → groups: `"2"`, `"5G"`, `"3J"` → **`"2-5G-3J"`**.

---

## 3) Python solutions (two common ways)

### A) Slice by remainder (most common / very clean)

```python
#User function Template for python3

class Solution:
    def ReFormatString(self, S: str, K: int) -> str:
        """
        Time  : O(n)  – one pass to clean, one pass to slice/join
        Space : O(n)  – cleaned string + output
        """
        # 1) Remove dashes, uppercase
        clean = S.replace("-", "").upper()   # O(n)

        n = len(clean)
        if n == 0:
            return ""                        # nothing to format

        # 2) Determine first group length
        first = n % K
        if first == 0:
            first = K

        # 3) Collect groups
        parts = [clean[:first]]              # first group (1..K)
        # subsequent groups of exactly K chars
        for i in range(first, n, K):
            parts.append(clean[i:i+K])

        # 4) Join with dashes
        return "-".join(parts)
```

### B) Backward scan collecting groups of K (no modulus)

Build from the end in groups of `K`, then reverse the groups; useful if you prefer not computing the remainder.

```python
class Solution:
    def ReFormatString(self, S: str, K: int) -> str:
        """
        Time  : O(n)
        Space : O(n)
        """
        clean = S.replace("-", "").upper()   # O(n)
        n = len(clean)
        if n == 0:
            return ""

        groups = []
        i = n
        # Take K-sized slices from the end
        while i > 0:
            start = max(0, i - K)
            groups.append(clean[start:i])
            i = start

        groups.reverse()                     # restore left→right order
        return "-".join(groups)
```

> Both are O(n) time/space and are fine for interviews. Version **A** is the simplest and most common; version **B** shows you can avoid computing the remainder and still satisfy the “first group may be shorter” rule naturally.

---

## 4) Interviewer Q\&A

**Q1. Why group from the left with a shorter first group?**
Because the problem mandates that **all groups except the first** must be length `K`. Computing `first = n % K` makes the remainder the first group; if `n % K == 0`, the first group is of size `K`.

**Q2. Complexity?**

* **Time:** O(n) to clean + O(n) to build groups and join → O(n).
* **Space:** O(n) for the cleaned string and result.

**Q3. Edge cases?**

* All dashes: `"---"` → `""`.
* `K = 1`: every character separated by dashes.
* `S` already formatted or `K > len(clean)`: result is just the uppercase `clean` (single group).
* Mixed case letters: all must become uppercase.

**Q4. Why not build character by character?**
Repeated string concatenation can degrade to O(n²). Using list of parts and a final `"".join()` (or `"-".join(...)`) keeps it linear.

**Q5. Can it be done in-place?**
Not in Python (strings are immutable). In lower-level languages you could rewrite in-place on a char buffer, but you still need to remove dashes and possibly shift characters, which is simpler to do with a new buffer.

**Q6. What if there are non-alphanumeric characters?**
The problem guarantees only alphanumerics and dashes, so you don’t need extra validation.

---

---

Here’s a complete, runnable **License Key Formatting** program with:

* The required `class Solution.ReFormatString(self, S, K)` method
* Inline **time/space complexity** notes at each step
* Sample **inputs → outputs**
* A simple **timeit** benchmark for the whole run

---

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
License Key Formatting

Given a string S (alphanumerics and '-') and integer K, reformat so that:
- All letters are uppercase.
- Dashes are removed, then reinserted to separate groups.
- From left to right, each group has exactly K characters,
  EXCEPT the first group which may be shorter (but >= 1).

Let n = len(S).
Overall target complexities:
  Time  : O(n)   (one pass to clean + one pass to slice/join)
  Space : O(n)   (cleaned string + output)
"""

from __future__ import annotations
import timeit
from typing import List


# ------------------------------------------------------------
# Core solution (slice-by-remainder; most common and clean)
# ------------------------------------------------------------
class Solution:
    def ReFormatString(self, S: str, K: int) -> str:
        """
        Time per step:
          - replace("-", ""):  O(n)
          - upper():           O(n)
          - join on parts:     O(n) over total length
          - slicing to collect groups: O(n) total
        Space:
          - 'clean' string:    O(n)
          - 'parts' list:      O(n) total characters before join
          - output string:     O(n)
        """
        # 1) Remove dashes and uppercase (two linear passes) -> O(n)
        clean = S.replace("-", "").upper()

        n = len(clean)  # O(1)
        if n == 0:
            return ""   # Edge case: all dashes → empty

        # 2) Determine the size of the first group (remainder rule)
        #    first in [1..K] if n>0
        first = n % K    # O(1)
        if first == 0:
            first = K

        # 3) Collect groups: first group size 'first', then K-sized chunks
        parts: List[str] = [clean[:first]]     # O(first) slice; total slicing O(n)
        for i in range(first, n, K):           # O(n/K) iterations
            parts.append(clean[i:i+K])         # each slice O(K); total O(n)

        # 4) Join with dashes — O(n)
        return "-".join(parts)


# ------------------------------------------------------------
# Demo: sample inputs & outputs
# ------------------------------------------------------------
def demo() -> None:
    sol = Solution()
    samples = [
        ("5F3Z-2e-9-w", 4),   # -> "5F3Z-2E9W"
        ("2-5g-3-J", 2),     # -> "2-5G-3J"
        ("---", 3),          # -> ""
        ("a", 5),            # -> "A"
        ("abcd-ef", 3),      # -> "AB-CD-EF" (first=2, then K=3, but only 2+2 left)
        ("abcde", 1),        # -> "A-B-C-D-E"
        ("a-bC-dEf-ghIj", 3) # -> "A-BC-DEF-GHIJ"
    ]

    print("=== Sample Runs ===")
    for S, K in samples:
        print(f"in : S={S!r}, K={K}")
        out = sol.ReFormatString(S, K)
        print(f"out: {out}")
        print("-" * 40)


# ------------------------------------------------------------
# Benchmark with timeit (full-program style)
# ------------------------------------------------------------
def _bench_once(batch: List[tuple[str, int]]) -> None:
    sol = Solution()
    fmt = sol.ReFormatString
    for S, K in batch:
        fmt(S, K)

def benchmark() -> None:
    # Build a mixed batch (short + longer strings)
    base = [
        ("5F3Z-2e-9-w", 4),
        ("2-5g-3-J", 2),
        ("----a----b----c----d----e----f----", 4),
        ("abc-def-ghi-jkl-mno-pqr-stu-vwx-yz", 5),
        ("zzzz-zzzz-zzzz-zzzz-zzzz-zzzz", 3),
        ("a" * 5000 + "-" + "b" * 5000, 4),          # long
        ("12ab-34cd-56ef-78gh-90ij", 4),
        ("Aa-Bb-Cc-Dd-Ee-Ff-Gg-Hh-Ii-Jj", 2),
    ]
    # Repeat to get stable timing
    batch = base * 200

    runs = 5
    total = timeit.timeit(lambda: _bench_once(batch), number=runs)

    print("=== Benchmark (timeit) ===")
    print(f"Batch size : {len(batch)}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f}s")
    print(f"Avg / run  : {total / runs:.6f}s")
    print("-" * 40)


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

## 6) Real-World Use Cases (high-impact)

1. **Product/License Keys & Activation Codes**
   Formatting raw keys into readable blocks (e.g., `XXXX-XXXX-XXXX`) reduces typing errors and improves UX, while normalizing case and dash positions server-side.

2. **Coupon / Voucher Codes & Gift Cards**
   Consistent chunking and uppercase normalization for printable or SMS-delivered codes makes manual entry more reliable.

3. **Inventory / Serial Numbers on Labels**
   When printing or displaying alphanumeric identifiers, grouping into fixed-size blocks improves legibility for scanning or manual transcription.

4. **API Keys / Tokens Display (masked)**
   When partially revealing tokens to users (e.g., last 4 segments), formatting the visible portion in grouped blocks is clearer while keeping the actual value canonical internally.

5. **Data Hygiene Pipelines**
   Normalizing case and separators for identifiers before storing/indexing ensures deduplication and consistent search behavior.
