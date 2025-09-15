# Equal 0, 1 and 2

**Difficulty:** Medium
**Accuracy:** 49.75%
**Submissions:** 14K+
**Points:** 4

---

## Problem Statement

Given a string **str** of length **N** which consists of only `0`, `1` or `2`s, count the number of substrings which have **equal number of 0s, 1s and 2s**.

---

## Examples

### Example 1

**Input:** `str = "0102010"`
**Output:** `2`
**Explanation:** Substring `str[2, 4] = "102"` and substring `str[4, 6] = "201"` has equal number of `0`, `1` and `2`.

### Example 2

**Input:** `str = "11100022"`
**Output:** `0`
**Explanation:** There is no substring with equal number of `0`, `1` and `2`.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function **`getSubstringWithEqual012()`** which takes a single string `str` as input and returns the answer.

---

## Expected Complexities

* **Time Complexity:** `O(N)`
* **Auxiliary Space:** `O(N)`

---

## Constraints

* `1 ≤ N ≤ 10^5`

---

## Topic Tags

* `Hash`, `Strings`, `Data Structures`

---

## Related Articles

* [Substring Equal Number 0 1 2](https://www.geeksforgeeks.org/substring-equal-number-0-1-2/)

---

---

Here’s a compact, interview-ready bundle for **“Equal 0, 1 and 2”** (count substrings that contain equal numbers of `0`, `1`, and `2`).

---

## 2) Explanation + step-by-step dry run

### Key idea (prefix differences + hashmap)

Let `c0, c1, c2` be counts of `0/1/2` from the start up to current index `i`.
For any two indices `i < j`, the substring `(i+1 … j)` has equal `0/1/2` **iff** the *differences* are unchanged:

```
(c0 - c1,  c0 - c2) at j  ==  (c0 - c1,  c0 - c2) at i
```

Why? If both pairs match, then between `i+1` and `j` we have:

```
(c0[j]-c1[j]) - (c0[i]-c1[i]) = 0  ⇒ Δ0 = Δ1
(c0[j]-c2[j]) - (c0[i]-c2[i]) = 0  ⇒ Δ0 = Δ2
⇒ Δ0 = Δ1 = Δ2  ⇒ counts added for 0,1,2 are equal.
```

So as we scan, maintain `(d1, d2) = (c0 - c1, c0 - c2)`.
Keep a hashmap `freq[(d1, d2)] = how many times we’ve seen this pair so far`.
Every time the same pair reappears at position `i`, it forms **as many valid substrings** ending at `i` as the frequency we’ve seen before.

Initialize with `freq[(0,0)] = 1` to count substrings starting at index `0`.

### Dry run on `"0102010"`

(0-based indices; start `c0=c1=c2=0`, `freq{(0,0):1}`, `ans=0`)

| i | ch | c0 c1 c2 | (d1,d2)=(c0−c1,c0−c2) | freq before | ans inc | ans |
| - | -- | -------- | --------------------- | ----------- | ------: | --: |
| 0 | 0  | 1  0  0  | (1,1)                 | 0           |       0 |   0 |
| 1 | 1  | 1  1  0  | (0,1)                 | 0           |       0 |   0 |
| 2 | 0  | 2  1  0  | (1,2)                 | 0           |       0 |   0 |
| 3 | 2  | 2  1  1  | (1,1)                 | 1           |  **+1** |   1 |
| 4 | 0  | 3  1  1  | (2,2)                 | 0           |       0 |   1 |
| 5 | 1  | 3  2  1  | (1,2)                 | 1           |  **+1** |   2 |
| 6 | 0  | 4  2  1  | (2,3)                 | 0           |       0 |   2 |

Answer = **2** (substrings `"102"` and `"201"`).

---

## 3) Python solutions (optimized + brute)

### A) Hashmap on prefix differences — **O(N) time, O(N) space** (most expected)

```python
# User function Template for python3
from collections import defaultdict

class Solution:
    def getSubstringWithEqual012(self, Str: str) -> int:
        """
        Count substrings with equal #0, #1, #2 using prefix-difference hashing.
        Let d1 = c0 - c1, d2 = c0 - c2. Same (d1,d2) seen earlier ⇒
        substring between positions has Δ0=Δ1=Δ2.
        Time : O(N)  (single pass; O(1) dict ops amortized)
        Space: O(N)  (map stores up to N distinct pairs)
        """
        c0 = c1 = c2 = 0
        freq = defaultdict(int)
        freq[(0, 0)] = 1     # empty prefix
        ans = 0

        for ch in Str:
            if ch == '0':
                c0 += 1
            elif ch == '1':
                c1 += 1
            else:  # '2'
                c2 += 1

            d1 = c0 - c1
            d2 = c0 - c2

            # All earlier occurrences of (d1,d2) form a valid substring ending here
            ans += freq[(d1, d2)]
            freq[(d1, d2)] += 1

        return ans
```

### B) Brute force with prefix counts — **O(N²) time, O(N) space** (educational)

Precompute prefix counts of 0/1/2; test each `(l, r)` in `O(1)`.

```python
class SolutionBrute:
    def getSubstringWithEqual012(self, Str: str) -> int:
        """
        Prefix counts + check every substring.
        Time : O(N^2)
        Space: O(N)
        """
        n = len(Str)
        pre0 = [0]*(n+1)
        pre1 = [0]*(n+1)
        pre2 = [0]*(n+1)
        for i, ch in enumerate(Str, 1):
            pre0[i] = pre0[i-1] + (ch == '0')
            pre1[i] = pre1[i-1] + (ch == '1')
            pre2[i] = pre2[i-1] + (ch == '2')

        ans = 0
        for l in range(n):
            for r in range(l, n):
                c0 = pre0[r+1] - pre0[l]
                c1 = pre1[r+1] - pre1[l]
                c2 = pre2[r+1] - pre2[l]
                if c0 == c1 == c2:
                    ans += 1
        return ans
```

> In interviews, implement **A**. Mention **B** as a baseline or for small `N`.

---

## 4) Interviewer-style Q\&A

**Q1. Why do we store `(c0−c1, c0−c2)` instead of the raw triple `(c0,c1,c2)`?**
Because equal substrings correspond to **unchanged deltas**; the absolute counts keep growing, but equal deltas mean the increments of 0/1/2 over the interval are equal. Two numbers suffice (the third is implied).

**Q2. Why does “same pair seen before” add `freq[pair]` to the answer?**
If the current pair equals a previously seen pair at indices `i1, i2, …`, each of those earlier indices forms one valid substring ending here. Combinatorially it’s the count of earlier equal states.

**Q3. Why initialize `freq[(0,0)] = 1`?**
To count substrings that start at index `0`. When the current `(d1,d2)` is `(0,0)`, the substring from the start is valid.

**Q4. What are the complexities?**

* Optimized hashing: **O(N)** time, **O(N)** space (in worst case number of distinct pairs ≈ N).
* Brute with prefix: **O(N²)** time, **O(N)** space.

**Q5. Any pitfalls?**

* Forgetting the base state `(0,0)` → you’ll miss substrings starting at index 0.
* Using three deltas instead of two (one is redundant).
* Assuming there are only substrings of length multiple of 3 — that’s necessary but not sufficient; the hashmap approach handles correctness cleanly.

**Q6. Can this generalize beyond digits `0/1/2`?**
Yes. For `k` categories, maintain `k−1` independent deltas against a reference (e.g., `c0−c1, c0−c2, …`) and hash the `(k−1)`-tuple.

---

---

Here’s a **full, runnable Python program** for **“Equal 0, 1 and 2”** that:

* implements the **optimal O(N)** prefix-difference + hashmap method,
* shows **inputs → outputs** on sample cases,
* and **benchmarks** the implementation using `timeit` right in `main`.

I’ve added **inline comments** describing time/space complexity for each step.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Equal 0, 1 and 2 — count substrings with equal # of '0', '1', '2'.

Core idea (prefix differences + hashmap):
  Let c0, c1, c2 be prefix counts up to index i.
  For each i compute a pair (d1, d2) = (c0 - c1, c0 - c2).
  If the same (d1, d2) has appeared before at indices j1, j2, ...
  then each such index forms a valid substring (ji+1 .. i) with equal
  numbers of 0/1/2. So we add freq[(d1, d2)] to the answer and then
  increment the frequency.

Complexities (N = len(Str)):
  • Time  : O(N) — single pass; each dict op amortized O(1).
  • Space : O(N) — hashmap can hold up to N distinct (d1,d2) keys.
"""

from __future__ import annotations
from collections import defaultdict
import random
import timeit
from typing import Dict


# -----------------------------------------------------------------------------
# Optimal solution: prefix-difference hashmap (O(N) time, O(N) space)
# -----------------------------------------------------------------------------
class Solution:
    def getSubstringWithEqual012(self, Str: str) -> int:
        """
        Count substrings with equal #0, #1, #2 using prefix-difference hashing.

        Step-by-step (with local complexity):
          A) Initialize counters c0=c1=c2=0, map freq with base state (0,0)=1.
             Time O(1), Space O(1).
          B) Scan characters once:
             - Update a single counter in O(1).
             - Compute d1=c0-c1, d2=c0-c2 in O(1).
             - ans += freq[(d1,d2)]  (O(1) average dict lookup)
             - freq[(d1,d2)] += 1     (O(1) average dict update)
             Total loop: O(N) time, up to O(N) space growth for freq.
          C) Return ans. O(1).
        """
        # A) Initial prefix counts
        c0 = c1 = c2 = 0
        freq: Dict[tuple[int, int], int] = defaultdict(int)
        freq[(0, 0)] = 1  # base: empty prefix -> allows substrings starting at 0
        ans = 0

        # B) Single pass through the string
        for ch in Str:
            # Update one of the counters — O(1)
            if ch == '0':
                c0 += 1
            elif ch == '1':
                c1 += 1
            else:  # ch == '2'; input is guaranteed to be only 0/1/2
                c2 += 1

            # Compute difference pair (two integers) — O(1)
            d1 = c0 - c1
            d2 = c0 - c2

            # All previous occurrences of this pair form valid substrings ending here
            ans += freq[(d1, d2)]   # O(1) average dict lookup
            freq[(d1, d2)] += 1     # O(1) average dict update

        # C) Final answer — O(1)
        return ans


# -----------------------------------------------------------------------------
# (Optional) Brute force using prefix counts — O(N^2) time, O(N) space
# Useful for small inputs or validation.
# -----------------------------------------------------------------------------
class SolutionBrute:
    def getSubstringWithEqual012(self, Str: str) -> int:
        n = len(Str)
        # Build prefix counts — O(N) time, O(N) space
        pre0 = [0] * (n + 1)
        pre1 = [0] * (n + 1)
        pre2 = [0] * (n + 1)
        for i, ch in enumerate(Str, 1):
            pre0[i] = pre0[i - 1] + (ch == '0')
            pre1[i] = pre1[i - 1] + (ch == '1')
            pre2[i] = pre2[i - 1] + (ch == '2')

        # Try all substrings — O(N^2) time
        ans = 0
        for l in range(n):
            for r in range(l, n):
                c0 = pre0[r + 1] - pre0[l]
                c1 = pre1[r + 1] - pre1[l]
                c2 = pre2[r + 1] - pre2[l]
                if c0 == c1 == c2:
                    ans += 1
        return ans


# -----------------------------------------------------------------------------
# Demo: run on sample inputs (shows input values and outputs)
# -----------------------------------------------------------------------------
def demo_on_samples() -> None:
    samples = [
        ("0102010", 2),   # from prompt: "102" and "201"
        ("11100022", 0),  # from prompt
        ("012012", 7),    # many balanced substrings
        ("0", 0),
        ("012", 1),       # the whole string
    ]
    sol = Solution()
    print("=== Sample Runs (Optimal O(N) solution) ===")
    for s, expected in samples:
        out = sol.getSubstringWithEqual012(s)
        print(f"Str = {s!r} -> Output: {out}, Expected: {expected}")
    print("-" * 60)


# -----------------------------------------------------------------------------
# Benchmark with timeit (measures full function runtime)
# -----------------------------------------------------------------------------
def _bench_once(s: str) -> None:
    Solution().getSubstringWithEqual012(s)

def benchmark() -> None:
    """
    Build a large random test string (within constraints)
    and time the optimal O(N) algorithm using timeit.

    Data generation: O(N). Not part of timed region.
    Timed region:   each run is O(N).
    """
    rng = random.Random(2025)
    N = 100_000  # max per constraints
    # Generate a random string of '0','1','2' — O(N)
    s = "".join(rng.choice("012") for _ in range(N))

    runs = 5
    total = timeit.timeit(lambda: _bench_once(s), number=runs)

    print("=== Benchmark (O(N) solution) ===")
    print(f"N         : {N}")
    print(f"Runs      : {runs}")
    print(f"Total (s) : {total:.6f}")
    print(f"Avg/run s : {total / runs:.6f}")
    print("-" * 60)


# -----------------------------------------------------------------------------
# Main — executes demo and benchmark
# -----------------------------------------------------------------------------
def main() -> None:
    # 1) Show outputs for explicit inputs (includes the inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the optimized method with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (the most important ones)

1. **Balanced event windows in logs/streams**
   Detect contiguous periods where three event types (e.g., *INFO*, *WARN*, *ERROR*) occur **equally often**—useful for anomaly detection or load diagnostics.

2. **Traffic shaping / load balancing**
   In a request stream labeled by three classes (e.g., *gold/silver/bronze*), find windows where service distribution is **perfectly balanced**.

3. **A/B/C experiment exposure**
   On user timelines, find segments where exposures to three variants are **equal**, ensuring fairness before analyzing outcomes.

4. **Telemetry ratios**
   For tri-state sensor readings, identify contiguous time spans with equal counts—can help spot calibration windows or drift-free periods.

