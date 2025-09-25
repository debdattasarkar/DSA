
---

# Longest Prefix Suffix

**Difficulty:** Hard
**Accuracy:** 27.91%
**Submissions:** 152K+
**Points:** 8

---

## Problem Statement

Given a string `s` of lowercase English alphabets, find the length of the **longest proper prefix** which is also a **suffix**.

**Note:**

* A **prefix** is the starting part of the string.
* A **suffix** is the ending part of the string.
* Prefix and suffix can be **overlapping**, but **they should not be equal to the entire string**.

---

## Examples

**Example 1:**

```
Input: s = "abab"
Output: 2
Explanation: The string "ab" is the longest prefix and suffix.
```

**Example 2:**

```
Input: s = "aabcdaabc"
Output: 4
Explanation: The string "aabc" is the longest prefix and suffix.
```

**Example 3:**

```
Input: s = "aaaa"
Output: 3
Explanation: The string "aaa" is the longest prefix and suffix.
```

---

## Constraints

* `1 ≤ s.size() ≤ 10^6`
* `s` contains only lowercase English alphabets.

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Company Tags

* Accolite
* Amazon
* Microsoft
* MakeMyTrip

---

## Topic Tags

* Strings
* Data Structures

---

## Related Interview Experiences

* Makemytrip Interview Experience Set 7 On Campus

---

## Related Articles

* [Longest Prefix Also Suffix](https://www.geeksforgeeks.org/longest-prefix-also-suffix/)

---

---

Alright, let’s crack **Longest Prefix Suffix** (LPS).
Goal: for a string `s`, return the **length** of the longest **proper** prefix that is also a suffix (can overlap, but cannot be the entire string).

---

# Intuition + Step‑by‑Step

* A *proper prefix* of `s` is any prefix not equal to `s` itself.
* We want the **longest** such prefix that is also a suffix.

This is exactly the same “prefix-function” used by the KMP algorithm. The last value of the LPS array tells us the answer.

### How the KMP LPS table works (prefix function)

`lps[i]` = length of the longest proper prefix of `s[0..i]` which is also a suffix of `s[0..i]`.

We build it in linear time by maintaining a pointer `len` for the current matched prefix length while scanning.

---

# Dry Run (KMP LPS) on `s = "aabcdaabc"`

Indices: `0 1 2 3 4 5 6 7 8`
Chars:  `a a b c d a a b c`

Initialize:

* `lps = [0]*n`
* `i = 1`, `len = 0`

Process:

1. `i=1`: `s[i]='a'`, `s[len]='a'` → match
   `len=1`, `lps[1]=1`, `i=2`

2. `i=2`: `s[i]='b'`, `s[len]='a'` → mismatch
   `len>0` so fallback: `len = lps[len-1] = lps[0] = 0`
   Now `len=0`, compare `'b'` vs `'a'` mismatch, `len==0` → `lps[2]=0`, `i=3`

3. `i=3`: `'c'` vs `'a'` mismatch, `lps[3]=0`, `i=4`

4. `i=4`: `'d'` vs `'a'` mismatch, `lps[4]=0`, `i=5`

5. `i=5`: `'a'` vs `'a'` match → `len=1`, `lps[5]=1`, `i=6`

6. `i=6`: `'a'` vs `s[len]='a'` match → `len=2`, `lps[6]=2`, `i=7`

7. `i=7`: `'b'` vs `s[len]='b'` match → `len=3`, `lps[7]=3`, `i=8`

8. `i=8`: `'c'` vs `s[len]='c'` match → `len=4`, `lps[8]=4`, `i=9` (done)

**Answer:** `lps[-1] = 4` (prefix/suffix `"aabc"`), which matches the sample.

---

# Solutions (Python)

## A) Optimized — KMP LPS in O(n) time, O(1) extra (besides output array)

```python
class Solution:
    def getLPSLength(self, s):
        # Edge cases
        n = len(s)
        if n <= 1:
            return 0

        # Build LPS (prefix-function) array
        lps = [0] * n  # lps[i] = longest proper prefix == suffix for s[:i+1]
        length = 0     # current matched prefix length
        i = 1          # current index to fill

        # Time: O(n) — every char is processed with at most one fallback per mismatch
        # Space: O(n) for the LPS array (can be reduced to O(1) if you only keep 'length')
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Fallback to the previous longest border
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # lps[-1] is the answer: longest proper prefix that's also a suffix for the whole string
        # Note: It can be equal to n only if whole string matches itself; but LPS builds proper borders, so lps[-1] <= n-1.
        return lps[-1]
```

### Why this works

The LPS table stores for each prefix the length of its longest border (proper prefix = suffix). The last entry is exactly the longest border of the entire string.

---

## B) Alternative Optimized — Z‑Algorithm (also O(n))

You can compute the longest prefix that matches a suffix by using the Z‑array (lengths of longest substring starting at i that matches the prefix). The answer is the **maximum `z[i]` such that `i + z[i] == n`**, and `< n` to keep it proper. (Generally Z is a bit more code; KMP is the standard answer in interviews.)

*Not shown in code for brevity; KMP is the go-to.*

---

## C) Brute Force — Check lengths from n‑1 down to 1 (O(n²))

```python
class Solution:
    def getLPSLength(self, s):
        # Time: O(n^2) worst-case (e.g., repeated chars), Space: O(1)
        n = len(s)
        for L in range(n - 1, 0, -1):  # proper prefix length
            # Compare s[:L] with s[n-L:]
            ok = True
            for i in range(L):
                if s[i] != s[n - L + i]:
                    ok = False
                    break
            if ok:
                return L
        return 0
```

This is clear but too slow for `n` up to 1e6.

---

# Quick sanity tests you can try

* `"abab"` → 2 (`"ab"`)
* `"aaaa"` → 3 (`"aaa"`)
* `"abcababcab"` → 5 (`"abcab"`)
* `"a"` → 0
* `"abacaba"` → 3 (`"aba"`)

---

# Interview Q\&A

**Q1. Why can prefixes and suffixes overlap?**
Because the requirement is *proper*, not *disjoint*. We only forbid using the whole string as both prefix and suffix.

**Q2. Why does KMP’s LPS array solve this?**
`lps[i]` gives the longest border of the prefix ending at `i`. For the entire string (`i = n-1`), `lps[-1]` is the longest border of the whole string, i.e., longest proper prefix that’s also a suffix.

**Q3. What’s the time/space complexity of the KMP LPS construction?**
Time **O(n)** (each character is advanced or a pointer falls back; each position is visited O(1) amortized). Space **O(n)** for the LPS array (you can compress to **O(1)** if you only need the final length by tracking just the `length` variable and not storing the whole array—but most implementations keep the array and return `lps[-1]`).

**Q4. Any pitfalls with KMP LPS?**

* Don’t advance `i` on mismatch after a fallback unless `length` drops to zero.
* Make sure you never return `n` (not possible with LPS definition because it’s proper).

**Q5. Could I do this with hashing?**
Yes—rolling hash can check prefix=suffix in O(log n) candidates with binary search or O(n) with smart precompute. But hashing brings collision caveats; KMP is collision‑free and standard.

**Q6. How is this used elsewhere?**

* Periodicity detection in strings.
* Finding minimal string to append to make it a palindrome (with LPS on `s + '#' + reverse(s)`).
* Pattern matching (KMP).
* Border arrays in string algorithms in general.

---

---
Here’s a **complete, runnable Python program** for “**Longest Prefix Suffix**”, with:

* A production‑ready O(n) KMP/LPS solution (what interviewers expect)
* (Optional) a simple O(n²) brute force for sanity checks
* **Inline time/space complexity notes at each step**
* A tiny **main** that runs a few sample inputs and uses **`timeit`** to measure the runtime of the full program call.

```python
#!/usr/bin/env python3
"""
Problem: Longest Prefix Suffix (LPS)
Return the length of the longest proper prefix of a string that is also a suffix.
A "proper" prefix is not equal to the whole string.

Primary approach: Build the KMP LPS array in O(n) time and O(n) space (amortized O(1) per step).
"""

from timeit import timeit

class Solution:
    # Time:  O(n) — each character is advanced or we fall back using lps; linear passes overall
    # Space: O(n) — for the lps array (you can reduce to O(1) if you only keep `length`)
    def getLPSLength(self, s: str) -> int:
        n = len(s)                            # O(1)
        if n <= 1:                            # O(1)
            return 0                          # Edge: no proper prefix possible

        # Step 1: allocate LPS array                   Time: O(n) to write each cell once, Space: O(n)
        lps = [0] * n

        # Step 2: build LPS with two pointers         Time: O(n) amortized
        length = 0  # current matched prefix length   Space: O(1)
        i = 1       # we start comparing from index 1 Space: O(1)

        while i < n:                                  # O(n) iterations amortized
            if s[i] == s[length]:                     # O(1) compare
                length += 1                           # O(1)
                lps[i] = length                       # O(1)
                i += 1                                # O(1)
            else:
                if length != 0:                       # O(1)
                    # Fallback to the previous border length
                    length = lps[length - 1]          # O(1)
                else:
                    lps[i] = 0                        # O(1)
                    i += 1                            # O(1)

        # Step 3: answer is the border length for the whole string
        #         (Longest proper prefix also a suffix)          Time: O(1)
        return lps[-1]

    # -------- OPTIONAL: simple brute force for validation --------
    # Time:  O(n^2) worst-case, Space: O(1)
    def getLPSLength_bruteforce(self, s: str) -> int:
        n = len(s)                                    # O(1)
        for L in range(n - 1, 0, -1):                 # up to O(n) lengths
            ok = True                                 # O(1)
            # compare s[:L] with s[n-L:]              # O(L) comparisons
            for i in range(L):
                if s[i] != s[n - L + i]:              # O(1)
                    ok = False
                    break
            if ok:
                return L
        return 0


def main():
    sol = Solution()

    tests = [
        ("abab", 2),
        ("aabcdaabc", 4),
        ("aaaa", 3),
        ("abc", 0),
        ("abababab", 6),
    ]

    print("=== Longest Prefix Suffix (KMP/LPS) ===")
    for s, expected in tests:
        ans = sol.getLPSLength(s)
        print(f"s = {s!r:12}  LPS len = {ans}  (expected {expected})")

    # (Optional) Cross‑check with brute force for small cases
    print("\nBrute‑force cross‑check on small tests:")
    for s, expected in tests:
        brute = sol.getLPSLength_bruteforce(s)
        print(f"s = {s!r:12}  brute LPS len = {brute}  (expected {expected})")

    # ----------- timeit benchmark -----------
    # Measure the time for running the KMP method several times.
    big = "abacabadabacabae" * 2000  # ~34k chars
    repeats = 5

    t = timeit(
        stmt="sol.getLPSLength(big)",
        setup="from __main__ import sol, big",
        number=repeats
    )

    print(f"\nTimeit: KMP getLPSLength on |big|={len(big)} run {repeats}x -> {t:.6f} sec total "
          f"(avg {t/repeats:.6f} sec/run)")

if __name__ == "__main__":
    main()
```

## What the program prints (example)

```
=== Longest Prefix Suffix (KMP/LPS) ===
s = 'abab'        LPS len = 2  (expected 2)
s = 'aabcdaabc'   LPS len = 4  (expected 4)
s = 'aaaa'        LPS len = 3  (expected 3)
s = 'abc'         LPS len = 0  (expected 0)
s = 'abababab'    LPS len = 6  (expected 6)

Brute‑force cross‑check on small tests:
s = 'abab'        brute LPS len = 2  (expected 2)
s = 'aabcdaabc'   brute LPS len = 4  (expected 4)
s = 'aaaa'        brute LPS len = 3  (expected 3)
s = 'abc'         brute LPS len = 0  (expected 0)
s = 'abababab'    brute LPS len = 6  (expected 6)

Timeit: KMP getLPSLength on |big|=34000 run 5x -> 0.0xxxx sec total (avg 0.0xxxx sec/run)
```

> Notes:
>
> * The **KMP/LPS** method is the one interviewers expect. It’s linear, clean, and widely used.
> * The **brute force** helper is just for validation on small inputs; don’t use it on large strings.


----

----

# 🌍 Real-World Use Cases

Here are the **most important real-world use cases** for the **Longest Prefix Suffix (LPS)** problem:

---

### 1️⃣ **String Pattern Matching (KMP Algorithm Core)**

* **Where used:** Search for a substring inside a large string efficiently.
* **Why LPS matters:**
  The KMP algorithm uses the LPS array to avoid re-checking characters when a mismatch occurs.
  Example: Finding all occurrences of `"abcab"` in a DNA sequence with millions of base pairs.
* **Impact:** Reduces search time from **O(n·m)** to **O(n + m)**.

---

### 2️⃣ **Plagiarism & Duplicate Content Detection**

* **Where used:** Detect repeated patterns in documents, code, or research papers.
* **Why LPS matters:**
  Identifies recurring sections by finding overlaps in text sequences without scanning from scratch.
* **Example:** Detecting if a section of text is repeated at both the start and end of a document.

---

### 3️⃣ **Network Packet Analysis**

* **Where used:** Searching for known byte patterns in network traffic for intrusion detection.
* **Why LPS matters:**
  Network scanning tools like Snort use LPS-like preprocessing to quickly match attack signatures in real-time streams.

---

### 4️⃣ **DNA & Protein Sequence Analysis**

* **Where used:** Bioinformatics — finding repeated genetic patterns.
* **Why LPS matters:**
  Helps detect periodic subsequences and repeated motifs, which are biologically significant.
* **Example:** Detecting `"AGCTAGCT"` as a repeating motif in a DNA sequence.

---

### 5️⃣ **Data Compression**

* **Where used:** Algorithms like LZ77 and Z-algorithms for finding repetitions.
* **Why LPS matters:**
  Detects longest repeating prefixes and suffixes, enabling better compression by storing repeated sequences once.

---
