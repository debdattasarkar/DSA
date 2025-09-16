# Longest Substring with K Uniques

**Difficulty:** Medium
**Accuracy:** 34.65%
**Submissions:** 234K+
**Points:** 4

---

## Problem Statement

You are given a string **s** consisting only of lowercase alphabets and an integer **k**. Your task is to find the **length of the longest substring** that contains **exactly k distinct characters**.

**Note:** If no such substring exists, return **-1**.

---

## Examples

### Example 1

**Input:** `s = "aabacbebebe", k = 3`
**Output:** `7`
**Explanation:** The longest substring with exactly 3 distinct characters is `"cbebebe"`, which includes `'c'`, `'b'`, and `'e'`.

### Example 2

**Input:** `s = "aaaa", k = 2`
**Output:** `-1`
**Explanation:** There's no substring with 2 distinct characters.

### Example 3

**Input:** `s = "aabbaaab", k = 2`
**Output:** `7`
**Explanation:** The entire string `"aabbaaab"` has exactly 2 unique characters `'a'` and `'b'`, making it the longest valid substring.

---

## Constraints

* `1 ≤ s.size() ≤ 10^5`
* `1 ≤ k ≤ 26`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)` (since alphabet size is constant 26; otherwise `O(k)`)

---

## Company Tags

* `Amazon`, `Google`, `SAP Labs`

---

## Topic Tags

* `two-pointer-algorithm`, `Hash`, `Strings`, `Map`, `Data Structures`, `Algorithms`

---

## Related Articles

* [Find The Longest Substring With K Unique Characters In A Given String](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)

---

---

Here’s the interview-ready pack for **Longest Substring with Exactly K Distinct Characters**.

---

## 2) Intuition + step-by-step dry run

### Core idea (Sliding window + frequency map) — O(n)

Maintain a window `[L..R]` and a frequency map `freq[char]` for characters inside the window.

Process characters from left to right:

1. Expand the right end `R` and include `s[R]` (`freq[s[R]] += 1`).
2. If the window has **more than k** distinct characters, shrink from the left:

   * Decrement `freq[s[L]]`, remove it when it drops to zero, move `L` forward.
3. Whenever the window has **exactly k** distinct characters, update the answer with its length.

This guarantees each index enters and leaves the window at most once → linear time.

### Dry run (s = `"aabacbebebe"`, k = 3)

We track `(L, R, window, distinct, best)`.

* Start: `L=0`, `best=-1`, `freq={}`
* R=0 (`'a'`): freq={a:1} → distinct=1 < k → best stays -1
* R=1 (`'a'`): freq={a:2} → distinct=1 < k
* R=2 (`'b'`): freq={a:2,b:1} → distinct=2 < k
* R=3 (`'a'`): freq={a:3,b:1} → distinct=2 < k
* R=4 (`'c'`): freq={a:3,b:1,c:1} → distinct=3 == k → best=max(-1, R-L+1=5) = **5** (`"aabac"`)
* R=5 (`'b'`): freq={a:3,b:2,c:1} → distinct=3 == k → best=max(5, 6)=**6** (`"aabacb"`)
* R=6 (`'e'`): freq={a:3,b:2,c:1,e:1} → distinct=4 > k → shrink L:

  * L=0 `'a'`→ a:2 (still >k) → L=1
  * L=1 `'a'`→ a:1 (still >k) → L=2
  * L=2 `'b'`→ b:1 (still >k) → L=3
  * L=3 `'a'`→ a:0 remove → freq={b:1,c:1,e:1} → distinct=3 == k
  * Now window is `s[4..6]="cbe"` length 3; best stays 6
* R=7 (`'b'`): freq={b:2,c:1,e:1} → distinct=3 → best=max(6, R-L+1=7-4+1=4)=6
* R=8 (`'e'`): freq={b:2,c:1,e:2} → distinct=3 → best=max(6, 8-4+1=5)=6
* R=9 (`'b'`): freq={b:3,c:1,e:2} → distinct=3 → best=max(6, 9-4+1=6)=6
* R=10 (`'e'`): freq={b:3,c:1,e:3} → distinct=3 → best=max(6, 10-4+1=7)=**7**
  Final answer: **7** (substring `"cbebebe"`).

---

## 3) Python solutions (optimized + alternatives)

### A) Sliding window with dict (most expected) — **O(n) time, O(1) space**

(Alphabet is lowercase a–z → bounded by 26)

```python
from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        """
        Sliding window with frequency map.
        Time : O(n)  — each index enters/leaves window once
        Space: O(1)  — at most 26 keys for lowercase alphabet (otherwise O(k))
        """
        n = len(s)
        if k == 0:
            return -1
        freq = defaultdict(int)
        left = 0
        best = -1

        for right, ch in enumerate(s):
            freq[ch] += 1  # include s[right]

            # shrink until we have at most k distinct
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # if exactly k distinct, update best
            if len(freq) == k:
                best = max(best, right - left + 1)

        return best
```

### B) Sliding window using a fixed-size array (faster constants) — **O(n) / O(1)**

```python
class SolutionArray:
    def longestKSubstr(self, s, k):
        """
        Same logic as A but using a 26-length counter array.
        Time : O(n)
        Space: O(1)
        """
        if k == 0:
            return -1
        cnt = [0]*26
        def idx(c): return ord(c) - 97

        left = 0
        kinds = 0
        best = -1

        for right, ch in enumerate(s):
            ci = idx(ch)
            if cnt[ci] == 0:
                kinds += 1
            cnt[ci] += 1

            while kinds > k:
                li = idx(s[left])
                cnt[li] -= 1
                if cnt[li] == 0:
                    kinds -= 1
                left += 1

            if kinds == k:
                best = max(best, right - left + 1)

        return best
```

### C) Brute force (educational baseline) — **O(n²) time, O(1) space**

Stop early when distincts exceed `k`.

```python
class SolutionBrute:
    def longestKSubstr(self, s, k):
        """
        Check every start index and extend until distinct > k.
        Time : O(n^2), Space : O(1) (26-sized array)
        """
        n = len(s)
        best = -1
        for i in range(n):
            cnt = [0]*26
            kinds = 0
            for j in range(i, n):
                t = ord(s[j]) - 97
                if cnt[t] == 0:
                    kinds += 1
                cnt[t] += 1
                if kinds == k:
                    best = max(best, j - i + 1)
                elif kinds > k:
                    break
        return best
```

> In interviews, code **A** (or **B**), mention the early-break brute (C) as baseline.

---

## 4) Interviewer-style Q\&A

**Q1. Why sliding window works here?**
Because as you expand right, the number of distinct characters **monotonically increases** or stays. If it exceeds `k`, you can move the left pointer to reduce it. Each index is moved at most once → O(n).

**Q2. What’s the difference between “exactly k” and “at most k”?**
“At most k” is easy: just track while `distinct ≤ k`. For **“exactly k”** longest length, maintain the window with `distinct ≤ k` but only update the answer when `distinct == k`. (Unlike counting substrings, you **cannot** do `atMost(k) - atMost(k-1)` for length.)

**Q3. Why is space O(1)?**
The alphabet is fixed (lowercase a–z → 26 counters). If alphabet were unbounded, space would be O(k).

**Q4. Edge cases?**

* `k > number of distinct chars in s` → return `-1`. (Handled naturally: window never reaches `k`.)
* `k == 0` → return `-1`.
* All same character and `k=1` → answer is `len(s)`.

**Q5. Can we return the substring itself?**
Yes—store the best `(start, end)` when you update `best`, then return `s[bestL:bestR+1]`. Complexity unchanged.

**Q6. How would you adapt to uppercase/Unicode?**
Use a `defaultdict(int)` or `Counter` (Solution A), not the fixed 26-array.

---

---

Here’s a **complete, runnable Python program** for **“Longest Substring with Exactly K Distinct Characters”** that

* implements the optimal **O(n)** sliding-window solution,
* prints **inputs → outputs** for sample cases,
* and **benchmarks** the solution using `timeit` right in `main`.

Inline comments call out **time & space complexity** of each step.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Longest Substring with Exactly K Distinct Characters
----------------------------------------------------
Given a lowercase string s and integer k, return the length of the longest
substring that contains exactly k distinct characters. If none, return -1.

Let n = len(s).
Overall complexities for the sliding-window solution:
  Time  : O(n)   (each index enters/leaves the window at most once)
  Space : O(1)   (at most 26 keys for lowercase alphabet; O(k) in general)
"""

from __future__ import annotations
from collections import defaultdict
import random
import string
import timeit
from typing import Dict


# ---------------------------------------------------------------------
# User function Template for python3
# ---------------------------------------------------------------------
class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        """
        Sliding window with frequency map.

        Steps & per-step complexity:
          A) Guard cases               -> O(1)
          B) Iterate right pointer     -> O(n) total
             - include s[right]        -> O(1) average dict update
             - while distinct > k:
                 shrink from left      -> Each shrinking step O(1) average
             - if distinct == k: update best -> O(1)
        Total: O(n) time, O(1) space (26 letters).
        """
        # A) Quick rejects — O(1)
        if k <= 0 or not s:
            return -1

        freq: Dict[str, int] = defaultdict(int)  # O(1) to create
        left = 0
        best = -1

        # B) Expand right in a single pass — O(n)
        for right, ch in enumerate(s):
            freq[ch] += 1  # include current char — O(1) average

            # shrink until we have at most k distinct — each char leaves once overall
            while len(freq) > k:
                left_ch = s[left]
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    del freq[left_ch]  # remove key to keep distinct count right
                left += 1

            # if exactly k distinct, try to improve answer — O(1)
            if len(freq) == k:
                best = max(best, right - left + 1)

        return best  # -1 if we never hit exactly k


# ---------------------------------------------------------------------
# (Optional) Baseline brute-force for small inputs: O(n^2) / O(1)
# ---------------------------------------------------------------------
class SolutionBrute:
    def longestKSubstr(self, s: str, k: int) -> int:
        """
        Extend each start until distinct > k, track max when distinct == k.
        Time  : O(n^2)  (nested loops)
        Space : O(1)    (26-sized counter)
        """
        n = len(s)
        best = -1
        for i in range(n):                 # O(n)
            cnt = [0] * 26                 # O(1)
            kinds = 0
            for j in range(i, n):          # O(n) in worst case
                t = ord(s[j]) - 97
                if cnt[t] == 0:
                    kinds += 1
                cnt[t] += 1
                if kinds == k:
                    best = max(best, j - i + 1)
                elif kinds > k:
                    break
        return best


# ---------------------------------------------------------------------
# Demo: explicit sample runs (prints input values and outputs)
# ---------------------------------------------------------------------
def demo_on_samples() -> None:
    samples = [
        ("aabacbebebe", 3, 7),  # from prompt: "cbebebe"
        ("aaaa", 2, -1),
        ("aabbaaab", 2, 7),
        ("abc", 1, 1),          # any single char
        ("abcabcbb", 3, 8),     # "abcabcbb" has exactly 3 uniques across whole string
    ]
    sol = Solution()
    print("=== Sample Runs (Sliding Window O(n)) ===")
    for s, k, expected in samples:
        out = sol.longestKSubstr(s, k)   # O(n)
        print(f"s={s!r}, k={k} -> Output: {out} | Expected: {expected}")
    print("-" * 60)


# ---------------------------------------------------------------------
# Benchmark with timeit (measures *full* function runtime)
# ---------------------------------------------------------------------
def _bench_once(s: str, k: int) -> None:
    Solution().longestKSubstr(s, k)      # O(n)

def benchmark() -> None:
    """
    Build a large random test string (within constraints) and time the solution.

    Data prep outside timing: O(n).
    Timed region per run:     O(n).
    """
    rng = random.Random(2025)
    n = 100_000                             # ≤ 1e5 per constraints
    alphabet = string.ascii_lowercase       # 26 letters
    s = "".join(rng.choice(alphabet) for _ in range(n))  # O(n)
    k = rng.randint(1, 26)

    runs = 5
    total = timeit.timeit(lambda: _bench_once(s, k), number=runs)

    print("=== Benchmark (Sliding Window) ===")
    print(f"n        : {n}")
    print(f"k        : {k}")
    print(f"runs     : {runs}")
    print(f"total (s): {total:.6f}")
    print(f"avg/run  : {total / runs:.6f}")
    print("-" * 60)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main() -> None:
    # 1) Show sample inputs & outputs
    demo_on_samples()

    # 2) Run benchmark
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (high-value)

1. **Rate-limiting / Throttling Windows**
   In a stream of user actions labeled by type (e.g., “read/write/delete”), find the longest span containing exactly **k** distinct types to understand behavioral variety within a session window.

2. **NLP / Token Span Mining**
   On tokenized text, identify the longest span with exactly **k** unique terms (e.g., to bound vocabulary diversity in a segment for feature extraction or readability analysis).

3. **Observability / Log Analytics**
   For traces or logs tagged with categories (service names, severity levels), detect the longest interval that engages exactly **k** unique categories—useful for incident triage and scope analysis.

4. **Security / Anomaly Detection**
   In event streams with labeled event kinds, search for long intervals with exactly **k** varieties (too little or too much diversity can be suspicious).
