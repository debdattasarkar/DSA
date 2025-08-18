
---

# Find H-Index

**Difficulty:** Medium
**Accuracy:** 53.4%
**Submissions:** 49K+
**Points:** 4

---

## Problem Statement

You are given an array **citations\[]**, where each element `citations[i]` represents the number of citations received by the `i`ᵗʰ paper of a researcher. You have to calculate the researcher's **H-index**.

The **H-index** is defined as the maximum value `H`, such that the researcher has published at least `H` papers, and all those papers have citation values greater than or equal to `H`.

---

## Examples

**Example 1:**

```
Input: citations[] = [3, 0, 5, 3, 0]  
Output: 3  
Explanation: There are at least 3 papers with citation counts of 3, 5, and 3, all having citations greater than or equal to 3.
```

**Example 2:**

```
Input: citations[] = [5, 1, 2, 4, 1]  
Output: 2  
Explanation: There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations.  
However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.
```

**Example 3:**

```
Input: citations[] = [0, 0]  
Output: 0  
Explanation: The H-index is 0 because there are no papers with at least 1 citation.
```

---

## Constraints

* $1 \leq citations.size() \leq 10^6$
* $0 \leq citations[i] \leq 10^6$

---

## Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## Topic Tags

* Sorting
* Arrays
* Binary Search

---

## Related Articles

* [What Is H Index](https://www.geeksforgeeks.org/what-is-h-index/)

---

---

Here you go — crisp explanation, a careful dry run, and interview-ready solutions (both brute/easy and optimized), followed by common interviewer Q\&A.

---

# 2) Intuition + Step-by-Step Dry Run

## What is H-index?

The **H-index** is the largest integer `H` such that there are **at least H papers** with **citations ≥ H**.

Think of it as: “How big a threshold can I set so that at least that many papers meet or exceed the threshold?”

---

## Dry run 1

**Input:** `citations = [3, 0, 5, 3, 0]`

### Sorted view (descending)

`[5, 3, 3, 0, 0]`
Walk with `i` starting from 1:

* `i=1`: is `sorted[0] (=5) ≥ 1`? yes → h could be 1
* `i=2`: is `sorted[1] (=3) ≥ 2`? yes → h could be 2
* `i=3`: is `sorted[2] (=3) ≥ 3`? yes → h could be 3
* `i=4`: is `sorted[3] (=0) ≥ 4`? no → stop

**Answer = 3**

Interpretation: there are 3 papers with ≥ 3 citations (5,3,3).

---

## Dry run 2

**Input:** `citations = [5, 1, 2, 4, 1]`

### Sorted view (descending)

`[5, 4, 2, 1, 1]`

* `i=1`: 5 ≥ 1 → ok
* `i=2`: 4 ≥ 2 → ok
* `i=3`: 2 ≥ 3 → **no** → stop

**Answer = 2**
There are only 2 papers with ≥ 2 citations (5,4). For `H=3` you'd need 3 papers with ≥3 citations; only two exist (5,4).

---

# 3) Solutions in Python (Interview-style)

## A) Easy / Brute(ish) approach — Sort then scan (O(n log n) time, O(1) extra space)

Idea: Sort in **descending** order and find the largest index where `cit[i] ≥ i+1`.

```python
class Solution:
    def hIndex(self, citations):
        # Time: O(n log n) for sorting
        # Space: O(1) or O(n) depending on sort implementation (Python Timsort uses O(n) worst-case auxiliary)
        citations.sort(reverse=True)  # highest first
        
        h = 0  # best H found so far
        for i, c in enumerate(citations):  # i = 0..n-1
            # We are checking if at least i+1 papers have ≥ i+1 citations.
            if c >= i + 1:
                h = i + 1
            else:
                break  # further elements will be smaller; can't raise H anymore
        return h
```

### Why it works

If the list is descending, the condition “**at least H papers have ≥ H citations**” is the same as “the `(H-1)`th value (0-based) is ≥ H”.

---

## B) Optimal approach — Counting/Bucket (O(n) time, O(n) space)

When citations can be large (up to 1e6), **we cap all values above n at n** because having more than `n` citations doesn’t help you get `H > n` (you only have `n` papers).

**Algorithm**

1. Let `n = len(citations)`. Create `bucket[0..n] = 0`.
2. For each `c`:

   * if `c >= n`: `bucket[n] += 1`
   * else: `bucket[c] += 1`
3. Walk `h` from `n` down to `0`, maintaining a running `papers` count of how many papers have at least `h` citations:

   * `papers += bucket[h]`
   * if `papers >= h`, return `h`.

```python
class Solution:
    def hIndex(self, citations):
        # Time: O(n)
        # Space: O(n)
        n = len(citations)
        bucket = [0] * (n + 1)
        
        # Count how many papers have exactly c citations (capped at n)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        
        # Suffix accumulation to find largest h such that
        # at least h papers have >= h citations
        papers = 0
        for h in range(n, -1, -1):   # n, n-1, ..., 0
            papers += bucket[h]
            if papers >= h:
                return h
        return 0
```

### Why it works

By capping counts at `n`, we avoid huge arrays and the suffix sum `papers` tells us how many papers have citations ≥ current `h`. The first time `papers ≥ h` (scanning from high to low), that’s the maximum valid H.

---

### Edge cases to keep in mind

* All zeros → `h = 0`
* Single paper → `h = 1` if citations ≥ 1 else `0`
* Many large numbers → `h ≤ n` anyway (bucket cap handles it)
* Non-sorted input (no assumption of order)

---

# 4) Interview Q\&A

**Q1. Why can we cap citations at `n` in the counting approach?**
Because H-index cannot exceed the number of papers `n`. If a paper has `10^9` citations, it still contributes at most 1 to the count of papers with ≥ `h` for any `h ≤ n`. Thus, counting all `c ≥ n` in `bucket[n]` preserves correctness.

**Q2. What’s the time/space complexity of the two main approaches?**

* Sort & scan: **O(n log n)** time, **O(1)** extra (or O(n) aux by implementation).
* Bucket counting: **O(n)** time, **O(n)** space.

**Q3. Can H-index be computed with binary search on a sorted array?**
Yes, if you first sort ascending you can binary search for the smallest index `i` such that `citations[i] ≥ n-i`, making the H `= n - i`. But sorting still costs **O(n log n)**.

**Q4. Why break early in the sorted scan?**
Once you find an index `i` where `citations[i] < i+1`, all following elements are ≤ this value (since sorted descending), so the H can’t increase.

**Q5. What if all papers have citations ≥ n?**
Then `h = n`. The bucket approach returns `n` because `bucket[n]` will accumulate to `n` and `papers ≥ n` at `h = n`.

**Q6. Is there any scenario where bucket beats sort in practice?**
For very large `n` (up to 10^6 per constraints), bucket is often faster than sort and uses linear time. It also avoids comparison overhead and can be more cache-friendly.

---

---

Awesome — here’s a complete, runnable program for the H-Index problem with:

* Clear, inline complexity notes at each step,
* A tiny “main” that feeds inputs, prints outputs, and measures end-to-end time with `timeit`,
* Two implementations (sorted scan and bucket/linear),
* A short list of practical, real-world uses.

---

```python
#!/usr/bin/env python3
"""
H-Index — Full Program with Timing & Inline Complexity Notes
------------------------------------------------------------

Problem:
Given an array citations[], return the researcher's H-index:
largest H such that at least H papers have ≥ H citations.

This file exposes two approaches and a main harness.

Approach A (Easy):  Sort-desc + scan
  Time:  O(n log n)    (sorting dominates)
  Space: O(1) aux      (Python’s Timsort may use extra; conceptually constant)

Approach B (Optimized): Bucket counting (cap values at n)
  Time:  O(n)
  Space: O(n)

We time the “overall program run” (build inputs → call function → print) via timeit.
"""

from timeit import timeit


class Solution:
    # -------------------------
    # A) Sort + scan (easy)
    # -------------------------
    def hIndex_sort_scan(self, citations):
        """
        Steps:
        1) Sort citations in descending order.  Time O(n log n)
        2) Linearly scan and find largest i s.t. citations[i] >= i+1.  Time O(n)
        Total time: O(n log n), space: O(1) aux (ignoring Python's internal)
        """
        citations.sort(reverse=True)  # O(n log n)
        h = 0
        for i, c in enumerate(citations):  # O(n)
            # invariant check: at least (i+1) papers need >= (i+1) citations
            if c >= i + 1:
                h = i + 1
            else:
                break  # later values only smaller → cannot improve H
        return h

    # -------------------------
    # B) Bucket counting (optimized)
    # -------------------------
    def hIndex_bucket(self, citations):
        """
        Steps:
        1) Make buckets[0..n], cap all c > n into buckets[n].  Time O(n), Space O(n)
        2) Walk h from n..0, keep running count of papers with ≥ h citations.  Time O(n)
        Return first h where running_count ≥ h.  That's the maximum H by construction.
        """
        n = len(citations)
        bucket = [0] * (n + 1)  # Space O(n)

        # Count frequencies (cap at n). Time O(n)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        # Accumulate from high to low to find largest feasible h. Time O(n)
        papers = 0
        for h in range(n, -1, -1):
            papers += bucket[h]  # papers with ≥ h citations so far
            if papers >= h:
                return h
        return 0  # fallback (won’t really hit: h=0 always works)

    # Expose one as default (use the optimized one)
    def hIndex(self, citations):
        return self.hIndex_bucket(citations)


def run_once(label, func, *args, **kwargs):
    """
    Helper to run `func(*args, **kwargs)` exactly once and print input & output.
    This is I/O (O(n) to print list), not part of asymptotic algorithmic cost.
    """
    print(f"\n--- {label} ---")
    print("Input citations:", args[0])
    out = func(*args, **kwargs)
    print("H-index:", out)
    return out


def main():
    sol = Solution()

    # Sample inputs (from the prompt / typical cases)
    inputs = [
        [3, 0, 5, 3, 0],      # expected 3
        [5, 1, 2, 4, 1],      # expected 2
        [0, 0],               # expected 0
        [10, 8, 5, 4, 3],     # expected 4
        [25, 8, 5, 3, 3, 3],  # expected 3
    ]

    # Choose which method to demo/time
    target_method = sol.hIndex  # uses optimized bucket version internally
    label = "Optimized (Bucket O(n))"

    # Time the full program run (inputs → function calls → prints)
    # We wrap the whole block in a small callable to pass into timeit.
    def demo():
        for arr in inputs:
            # Copy if method mutates (sort version mutates). bucket version does not.
            # We’ll copy to be safe if you switch implementations.
            run_once(label, target_method, arr[:])

    # Single run just to show outputs now
    demo()

    # Measure the full demo block N times
    N = 5
    t = timeit(stmt=demo, number=N)
    print(f"\nTotal time for running the full demo block {N} times: {t:.6f} seconds")
    print("(Includes Python print I/O; algorithm alone is faster.)")


if __name__ == "__main__":
    main()
```

### Example Output (illustrative)

```
--- Optimized (Bucket O(n)) ---
Input citations: [3, 0, 5, 3, 0]
H-index: 3

--- Optimized (Bucket O(n)) ---
Input citations: [5, 1, 2, 4, 1]
H-index: 2

--- Optimized (Bucket O(n)) ---
Input citations: [0, 0]
H-index: 0

--- Optimized (Bucket O(n)) ---
Input citations: [10, 8, 5, 4, 3]
H-index: 4

--- Optimized (Bucket O(n)) ---
Input citations: [25, 8, 5, 3, 3, 3]
H-index: 3

Total time for running the full demo block 5 times: 0.00xxxx seconds
(Includes Python print I/O; algorithm alone is faster.)
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Academic impact scoring**
   H-index is a widely used bibliometric metric to assess a researcher’s sustained influence (balances productivity and impact).

2. **Hiring & promotion dashboards**
   Universities and R\&D labs summarize candidate impact via H-index, alongside publication venues and total citations.

3. **Portfolio & product analytics**
   For a set of features/products with “adoption” counts, an H-like index shows “how many features have at least that many adopters,” emphasizing the breadth of strong performers.

4. **Content / creator platforms**
   For posts or creators with views/likes, an H-style index can indicate a creator’s sustained performance: “how many posts with at least H thousand views,” reducing the effect of one-hit wonders.

