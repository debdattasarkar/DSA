# Smallest Positive Integer that can not be represented as Sum

**Difficulty:** Hard
**Accuracy:** 35.8%
**Submissions:** 43K+
**Points:** 8
**Average Time:** 30m

---

## Problem Statement

Given an array of size `N`, find the smallest positive integer value **that is either not presented in the array or cannot be represented as a sum (coz sum means you are adding two or more elements)** of some elements from the array.

---

## Example 1

**Input:**
`N = 6`
`array[] = {1, 10, 3, 11, 6, 15}`

**Output:**
`2`

**Explanation:**
`2` is the smallest integer value that cannot be represented as sum of elements from the array.

---

## Example 2

**Input:**
`N = 3`
`array[] = {1, 1, 1}`

**Output:**
`4`

**Explanation:**
`1` is present in the array.
`2` can be created by combining two `1`s.
`3` can be created by combining three `1`s.
`4` is the smallest integer value that cannot be represented as sum of elements from the array.

---

## Your Task

You don't need to read input or print anything. Complete the function `smallestpositive()` which takes the array and `N` as input parameters and returns the smallest positive integer value that cannot be represented as the sum of some elements from the array.

---

## Expected Time Complexity

`O(N * Log(N))`

## Expected Auxiliary Space

`O(1)`

---

## Constraints

* `1 ≤ N ≤ 10^6`
* `1 ≤ array[i] ≤ 10^9`
  The array may contain duplicates.

---

## Topic Tags

Arrays, Mathematical, Sorting, Data Structures, Algorithms

---

## Related Articles

* [Find Smallest Value Represented Sum Subset Given Array](https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/)

---

---

You pasted the stock function signature by mistake. I’ll use the correct one for this problem:
`smallestpositive(arr, n) → int`. (I also include a tiny wrapper with your name for convenience.)

---

# 2) Explanation + step-by-step dry run

## Problem

Given positive integers `arr` (size `n`), find the smallest **positive** integer that **cannot** be formed as the sum of **some** elements of `arr` (each element can be used at most once).
Classic greedy fact: after sorting, keep a running **coverage** `reach`, meaning **all** sums in `[1 … reach]` are representable.

* Initialize `reach = 0`.
* Scan numbers in **nondecreasing** order.

  * If the next number `x` is `≤ reach + 1`, we can extend coverage to `reach += x`.
    (Because combining `x` with any sum in `[0 … reach]` fills `[x … reach + x]`, hence we now cover `[1 … reach+x]`.)
  * If `x > reach + 1`, then `reach + 1` **cannot** be formed → that’s the answer.

Return `reach + 1`.

### Dry run 1

`arr = [1, 10, 3, 11, 6, 15]` → sort → `[1, 3, 6, 10, 11, 15]`
`reach = 0`

* `x=1` ≤ `0+1` → `reach=1` (we can make `{1}`)
* `x=3` ≤ `1+1=2`? **No** → answer is `reach+1 = 2`.

### Dry run 2

`arr = [1, 1, 1]` → already sorted
`reach=0`

* `x=1` ≤ 1 → `reach=1`  (cover `[1]`)
* `x=1` ≤ 2 → `reach=2`  (cover `[1..2]`)
* `x=1` ≤ 3 → `reach=3`  (cover `[1..3]`)
  End → answer `reach+1 = 4`.

Key edge: if the **first** number > 1, immediately return 1.

---

# 3) Python solutions (with interview-style comments)

### A) Optimized Greedy (Sort + Single Pass) — **most expected**

```python
class Solution:
    # Correct API for this problem:
    def smallestpositive(self, arr, n):
        """
        Greedy coverage.
        Time:  O(n log n)  -> due to sort
        Space: O(1)        -> in-place sort (or O(n) if you count sorting aux)
        """
        arr.sort()              # O(n log n)
        reach = 0               # we can form all sums in [1 .. reach]
        for x in arr:           # O(n)
            if x > reach + 1:   # gap found: reach+1 is not representable
                return reach + 1
            reach += x          # extend coverage to [1 .. reach+x]
        return reach + 1        # after all numbers, next integer is the answer

    # (Optional) small wrapper matching the name you pasted by mistake:
    # Not used by judges for this problem, but provided for convenience.
    def stockBuySell(self, arr):
        # Delegate to the correct function when n is len(arr)
        return self.smallestpositive(arr, len(arr))
```

### B) Same Greedy but using an iterator over unique values & counts (micro-optimization)

This doesn’t change complexity; it just skips repeated comparisons when many duplicates exist.

```python
from itertools import groupby

class SolutionCounted:
    def smallestpositive(self, arr, n):
        """
        Group equal values to possibly cut constant factors when duplicates abound.
        Time:  O(n log n) for the initial sort, O(k) groups pass afterward
        Space: O(1) extra (beyond sort)
        """
        arr.sort()
        reach = 0
        for val, grp in groupby(arr):
            # If there's a gap before `val`, stop
            if val > reach + 1:
                return reach + 1
            # We can add up to cnt copies of `val`
            cnt = sum(1 for _ in grp)
            reach += val * cnt
        return reach + 1
```

### C) Brute Force (for learning only; works for very small n)

Maintain a set of reachable sums; stop at the first gap. (Exponential-ish growth of states.)

```python
class SolutionBrute:
    def smallestpositive(self, arr, n):
        """
        Build all subset sums with a set and find the smallest missing positive.
        Time:  O(n * S) in practice where S is # of distinct sums (can be huge)
        Space: O(S)
        Only for tiny inputs to illustrate correctness.
        """
        reachable = {0}
        for x in arr:
            # add x to all existing sums
            new = {s + x for s in reachable}
            reachable |= new

        # find smallest positive not in reachable
        target = 1
        while target in reachable:
            target += 1
        return target
```

---

# 4) Interviewer-style Q\&A

**Q1. Why does the greedy `reach` argument work?**
**A.** By induction. Suppose we can make every sum in `[1..reach]`. If the next number `x ≤ reach+1`, then combining `x` with any `[0..reach]` (including 0 via “use nothing else”) yields coverage up to `reach + x`. If `x > reach+1`, then `reach+1` is unattainable: all sums using only earlier numbers are `≤ reach`, and any sum using `x` is at least `x ≥ reach+2`, leaving a gap at `reach+1`.

**Q2. Why must the array be processed in nondecreasing order?**
**A.** We need to meet the precondition that **all** numbers used so far are `≤ reach+1`; sorting ensures when we encounter a large `x > reach+1` we can safely stop—no later number can be smaller to bridge the gap.

**Q3. How do duplicates affect correctness?**
**A.** They only **increase** coverage (we can add `val` multiple times). The proof above still applies; grouping duplicates simply bumps `reach` by `val * count`.

**Q4. What if there’s a zero in the array?**
**A.** Zeros don’t change reachable sums; the algorithm still works (after sorting, zeros come first; they keep `reach` unchanged).

**Q5. Can we do better than `O(n log n)` time?**
**A.** Only if the input is already sorted (`O(n)`) or if values are small enough to count-sort. With arbitrary values up to `1e9`, comparison sorting gives `O(n log n)` lower bound.

**Q6. Space complexity?**
**A.** `O(1)` auxiliary beyond in-place sort; we only track `reach`.

**Q7. Relation to subset sum / coin problems?**
**A.** This is the classic “smallest unformable sum” for a **set of coins used at most once**. If coins were **unlimited**, the structure differs (it becomes the Frobenius/coin problem variant).

---

---

You got it! Here’s a **full, runnable Python program** for
**“Smallest Positive Integer that cannot be represented as Sum”** (using the classic greedy method). It:

* prints outputs for **sample inputs** (input → output),
* includes **inline time & space complexity** notes for every step,
* and **benchmarks** the core algorithm with `timeit` right inside `main`.

```python
#!/usr/bin/env python3
"""
Smallest Positive Integer that cannot be represented as Sum
- Given an array of positive integers, find the smallest positive integer
  value that is either not present in the array OR cannot be represented as a sum
  (sum means using two or more elements) of array elements.

Core idea (Greedy, interview-standard):
  Sort the array. Track the smallest value we cannot currently form, 'miss'.
  Maintain the invariant: after processing some prefix, we can form all values in [1, miss).
  If the next value x <= miss, we can extend coverage to [1, miss + x) (since x can pair with all sums < miss).
  If x > miss, we have a gap at 'miss' and that is the answer.

Complexities:
  Sorting dominates: O(n log n) time. One linear scan: O(n).
  Auxiliary space: O(1) extra (in-place sort + a few scalars).
"""

from __future__ import annotations
import random
import timeit
from typing import List


class Solution:
    def smallestpositive(self, array: List[int], n: int) -> int:
        """
        Greedy coverage with 'miss'.

        Steps:
          1) Sort the array (in-place).
             Time:  O(n log n)   Space: O(1) extra (Python's Timsort is in-place)
          2) Initialize miss = 1 (smallest positive not yet representable).
             Time:  O(1)         Space: O(1)
          3) Single pass over array:
                if x > miss:      -> gap found; return miss
                else: miss += x   -> extend coverage
             Time:  O(n)          Space: O(1)
          4) Return miss at the end.
             Time:  O(1)          Space: O(1)
        """
        # --- Step 1: Sort (O(n log n) time, O(1) extra space) ---
        array.sort()

        # --- Step 2: Start with the smallest missing sum as 1 (O(1)/O(1)) ---
        miss = 1

        # --- Step 3: Linear scan to extend coverage (O(n)/O(1)) ---
        for x in array:
            # Skip non-positives if they ever appear; problem constraints say array[i] >= 1
            if x <= 0:
                continue

            if x > miss:
                # Cannot create 'miss' from any subset: gap found
                return miss

            # Extend coverage from [1, miss) -> [1, miss + x)
            miss += x

        # --- Step 4: If no gaps, the smallest missing is 'miss' (O(1)/O(1)) ---
        return miss


# Optional: tiny brute-force (exponential) to sanity-check tiny arrays.
# Not used in benchmark; educational only.
class SolutionBrute:
    def smallestpositive(self, array: List[int], n: int) -> int:
        """
        Enumerate all subset sums (educational only).
        Time:  O(2^n)  Space: O(2^n)
        """
        sums = {0}
        for x in array:
            new = set()
            for s in sums:
                new.add(s + x)
            sums |= new

        ans = 1
        while ans in sums:
            ans += 1
        return ans


def demo_on_samples() -> None:
    """
    Show correctness on the examples and a couple of extra cases.
    Overall:
      Time:  O(total length * log(total length)) due to sorts inside calls
      Space: O(1) extra (besides the arrays themselves)
    """
    samples = [
        ( [1, 10, 3, 11, 6, 15], 6, 2 ),    # example 1 -> 2
        ( [1, 1, 1],               3, 4 ),  # example 2 -> 4
        ( [2, 3, 4],               3, 1 ),  # no 1 present, answer 1
        ( [1, 2, 5, 10, 20, 40],   6, 4 ),  # classic case -> 4
        ( [1, 2, 3, 4, 5, 6],      6, 22 ), # full coverage through 21 -> next is 22
    ]

    sol = Solution()

    print("=== Sample Runs (Input → Output) ===")
    for arr, n, expected in samples:
        inp = list(arr)  # keep original for printing
        ans = sol.smallestpositive(arr, n)
        print(f"Input : {inp}")
        print(f"Output: {ans}    (Expected: {expected})")
        print("-" * 60)


# Helper for timeit: keep the algorithm-only work inside the timed function
def _bench_once(arr_large: List[int]) -> None:
    Solution().smallestpositive(arr_large, len(arr_large))


def benchmark() -> None:
    """
    Benchmark the optimized solution with timeit.

    Prep (outside timing):
      - Build a random positive array of size SIZE: O(SIZE) time/space.

    Timed region (_bench_once):
      - Sort + scan: O(n log n) time, O(1) extra space.
    """
    SIZE = 200_000  # Large but reasonable for a quick run; adjust as you like
    rng = random.Random(2025)

    # Build positive integers in [1, 1e6] (constraints allow up to 1e9)
    # O(SIZE) time, O(SIZE) space
    arr_large = [rng.randrange(1, 10**6) for _ in range(SIZE)]

    runs = 3
    total = timeit.timeit(lambda: _bench_once(list(arr_large)), number=runs)
    # NOTE: we pass a fresh list each run so sort cost is measured fairly.

    print("=== Benchmark (Greedy O(n log n)) ===")
    print(f"Array size : {SIZE}")
    print(f"Runs       : {runs}")
    print(f"Total time : {total:.6f} s")
    print(f"Avg / run  : {total / runs:.6f} s")
    print("-" * 60)


def main() -> None:
    # 1) Print outputs for sample inputs (includes inputs and outputs)
    demo_on_samples()

    # 2) Benchmark the core solution with timeit
    benchmark()


if __name__ == "__main__":
    main()
```

---

## Real-World Use Cases (short & important)

1. **Currency / Denomination Design**
   Given a set of coin/bill denominations, this finds the **smallest payable amount that’s impossible**—critical for ensuring coverage of small transactions or for stress-testing proposed denomination sets.

2. **Prepaid Balances / Gift Cards / Loyalty Points**
   For a catalog of fixed point values or vouchers, determine the **smallest value a customer cannot assemble**, guiding adjustments to denominations so customers can reach any target up to a threshold.

3. **Resource Chunking / Storage Blocks**
   With allowed block sizes, identify the **smallest request size that cannot be composed** from available chunks, informing system design to minimize internal fragmentation and support more granular allocations.
