# Max sum path in two arrays

**Difficulty:** Medium
**Accuracy:** 30.9%
**Submissions:** 78K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given two **sorted** arrays of **distinct** integers `arr1` and `arr2`. Each array may have some elements in common with the other array. Find the **maximum sum of a path** from the beginning of **any array** to the end of **any array**. You can switch from one array to another **only at the common elements**.

**Note:** When we switch from one array to the other, we need to consider the common element **only once** in the result.

---

## Examples

### Example 1

**Input:**
`arr1 = [2, 3, 7, 10, 12]` , `arr2 = [1, 5, 7, 8]`
**Output:** `35`
**Explanation:** The path will be `1 + 5 + 7 + 10 + 12 = 35`, where `1` and `5` come from `arr2` and then `7` is common so we switch to `arr1` and add `10` and `12`.

---

### Example 2

**Input:**
`arr1 = [1, 2, 3]` , `arr2 = [3, 4, 5]`
**Output:** `15`
**Explanation:** The path will be `1 + 2 + 3 + 4 + 5 = 15`.

---

## Expected Complexities

* **Time Complexity:** `O(m + n)`
* **Auxiliary Space:** `O(1)`

---

## Constraints

* `1 ≤ arr1.size(), arr2.size() ≤ 10^4`
* `1 ≤ arr1[i], arr2[i] ≤ 10^5`

---

## Company Tags

Amazon

---

## Topic Tags

Arrays • Data Structures

---

## Related Articles

* [Maximum Sum Path Across Two Arrays](https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/)

---

---

Here’s a tight, interview-ready walkthrough for **Max sum path in two arrays**.

---

## 2) Intuition + step-by-step dry run

You have two **sorted** arrays `arr1`, `arr2` (distinct within each array). You can walk from left to right, starting in either array, and **you may switch only at common elements**. The goal is to maximize the total sum of visited elements, counting a common element **once** when you switch there.

### Key observation

Between two consecutive common elements (or from the start to the first common, or last common to the end), you must stay within a single array. So for each such **segment**, just pick the **larger segment sum** and add it to the answer; at a common element, add that common value once, then continue.

### Two-pointer sweep (constant extra space)

Keep two indices `i, j` and two running partial sums `s1, s2` for the current segments in `arr1` and `arr2`.

* If `arr1[i] < arr2[j]`, add `arr1[i]` to `s1`, advance `i`.
* If `arr2[j] < arr1[i]`, add `arr2[j]` to `s2`, advance `j`.
* If they’re equal (a **switch point**): add `max(s1, s2) + arr1[i]` to the answer, reset both sums to zero, and advance both pointers (we “switch” here if beneficial; the `max` handles the choice).

At the end, add `max(s1, s2)` for the tail segment.

#### Dry run on Example 1

```
arr1 = [2, 3, 7, 10, 12]
arr2 = [1, 5, 7, 8]

i=0, j=0, ans=0, s1=0, s2=0

arr1[i]=2 < 1? no -> arr2[j]=1 < 2
  s2 += 1 => s2=1, j=1
arr1[i]=2 < arr2[j]=5 -> s1+=2 => s1=2, i=1
arr1[i]=3 < 5 -> s1+=3 => s1=5, i=2
arr1[i]=7 vs arr2[j]=5 -> s2+=5 => s2=6, j=2
arr1[i]=7 == arr2[j]=7 (common)
  ans += max(s1,s2)+7 = max(5,6)+7 = 13
  ans=13, s1=s2=0, i=3, j=3

arr1[i]=10 vs arr2[j]=8 -> s2+=8 => s2=8, j=4 (arr2 done)
Tail: add remaining from arr1
  s1 += 10 + 12 => s1=22
Finally ans += max(s1,s2) = 22
Total ans = 13 + 22 = 35 ✅
```

---

## 3) Python solutions (with interview-grade comments)

### A) Optimal (two-pointers, O(m+n) time, O(1) extra)

```python
# Your task is to complete this function
# Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        """
        Two-pointer sweep accumulating segment sums until a common element,
        then take the larger segment sum + the common value, once.

        Time:  O(m + n)  (single pass)
        Space: O(1)      (constant extra)
        """
        i = j = 0
        s1 = s2 = 0          # running sums for current segments
        ans = 0
        m, n = len(arr1), len(arr2)

        # Walk both arrays
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            elif arr2[j] < arr1[i]:
                s2 += arr2[j]
                j += 1
            else:
                # switch point (same value). Count it once.
                ans += max(s1, s2) + arr1[i]
                s1 = s2 = 0
                i += 1
                j += 1

        # Add leftover tail from the unfinished array
        while i < m:
            s1 += arr1[i]
            i += 1
        while j < n:
            s2 += arr2[j]
            j += 1

        ans += max(s1, s2)
        return ans
```

### B) “Brute but simple” (prefix sums + hash indices, O(m+n) time, O(m+n) space)

This version first maps positions of the smaller array and builds prefix sums for both arrays; then it walks through common points using these prefix sums to measure segment sums. It’s not asymptotically worse than the optimal, but uses **extra memory** and is more verbose—fine as a first attempt in interviews.

```python
class SolutionPrefix:
    def maxPathSum(self, arr1, arr2):
        """
        Prefix-sum + hash approach:
        - Build prefix sums p1, p2.
        - Hash positions of elements of arr2.
        - Scan arr1, whenever you find a common element:
            add max( segmentSum1, segmentSum2 ) + common once.
        - Finally add the larger tail segment.

        Time:  O(m + n)
        Space: O(m + n)
        """
        m, n = len(arr1), len(arr2)
        # prefix sums with p[0]=0
        p1 = [0] * (m + 1)
        for i in range(m):
            p1[i+1] = p1[i] + arr1[i]

        p2 = [0] * (n + 1)
        for j in range(n):
            p2[j+1] = p2[j] + arr2[j]

        # map value -> index in arr2
        pos2 = {v: j for j, v in enumerate(arr2)}

        i = 0
        j_prev = -1  # last cut in arr2
        i_prev = -1  # last cut in arr1
        ans = 0

        while i < m:
            v = arr1[i]
            if v in pos2:
                j = pos2[v]
                # segment sums: (i_prev, i] and (j_prev, j] inclusive of current index
                seg1 = p1[i] - p1[i_prev+1]         # sum arr1[i_prev+1 .. i-1]
                seg2 = p2[j] - p2[j_prev+1]         # sum arr2[j_prev+1 .. j-1]
                ans += max(seg1, seg2) + v          # add bigger segment + common once
                i_prev = i
                j_prev = j
            i += 1

        # add tails after last common
        seg1_tail = p1[m] - p1[i_prev+1]
        seg2_tail = p2[n] - p2[j_prev+1]
        ans += max(seg1_tail, seg2_tail)
        return ans
```

---

## 4) Common Interview Q\&A

**Q1. Why is it safe to choose the larger segment sum between two common elements?**
Because you can only walk within one array between switch points; picking the larger segment yields the best contribution for that region. Switching is only allowed at the common value, which we add once.

**Q2. What if there are no common elements?**
Then the answer is simply the larger of the two total sums: `max(sum(arr1), sum(arr2))`. The two-pointer code naturally does this via tail addition.

**Q3. Do we ever double-count the common element?**
No. At a match we add `max(s1, s2) + common` and reset both partial sums, counting the common once.

**Q4. Are negative numbers or zeros an issue?**
The logic still works for any integers as long as arrays are **sorted** and you can switch **only** at equal values; the “take max segment” principle holds.

**Q5. What changes if arrays aren’t sorted or have duplicates inside each array?**

* If **not sorted**, you can’t use two pointers; you’d need to preprocess (e.g., sort with original indices) or use a different graph/path DP, which complicates things.
* If there are **duplicates within one array**, the notion of “switch only at common elements” needs a well-defined interpretation (e.g., switching at each occurrence). The classical problem assumes distinct values in each array.

**Q6. Time/space of the optimal approach?**
`O(m+n)` time and `O(1)` extra space (just counters and pointers).

**Q7. Can we start from the middle?**
No. The path must go left→right; maximizing is achieved by local choices at each segment (greedy) thanks to sorted order and switch-only-at-equals rule.

---

---

Below is a **complete, runnable Python program** for **Max Sum Path in Two Arrays** using the optimal **two-pointer** sweep. I’ve included **inline time/space complexity comments** at each step, sample inputs/outputs, and a small **timeit** harness so you can see how long the program run took.

```python
from typing import List
import timeit
import random

# ============================================================
# Max Sum Path in Two Arrays — Optimal O(m+n), O(1) extra
# ============================================================

class Solution:
    def maxPathSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Two-pointer sweep accumulating partial sums until we hit a common element.
        At each common element, we add:
            max(sum(segment in arr1), sum(segment in arr2)) + common_value
        (count the common once), reset both partial sums, and continue.

        Overall Time:  O(m + n)  — single linear scan
        Extra Space:   O(1)      — only a handful of counters/pointers
        """
        m, n = len(arr1), len(arr2)   # O(1)
        i = j = 0                     # O(1) two pointers
        s1 = s2 = 0                   # O(1) partial sums of current segments
        ans = 0                       # O(1) final answer accumulator

        # Walk both arrays simultaneously — O(m + n)
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                # Part of current segment on arr1 side
                s1 += arr1[i]         # O(1)
                i += 1                # O(1)
            elif arr2[j] < arr1[i]:
                # Part of current segment on arr2 side
                s2 += arr2[j]         # O(1)
                j += 1                # O(1)
            else:
                # Switch point (common element). Count it once.
                # Add the larger segment we have accumulated + the common value.
                ans += max(s1, s2) + arr1[i]  # O(1)
                s1 = s2 = 0                   # reset segments — O(1)
                i += 1
                j += 1

        # Add any leftover tail (one array may still have elements) — O(remaining)
        while i < m:
            s1 += arr1[i]
            i += 1
        while j < n:
            s2 += arr2[j]
            j += 1

        ans += max(s1, s2)             # O(1)
        return ans


# (Optional) Brute for tiny validation only — O(m*n) worst case
class SolutionBrute:
    def maxPathSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Brute idea: explore segments split by commons using sets and linear passes.
        (Shown for validation on small arrays. Do NOT use on big inputs.)
        Time:  O(m + n + c * (m + n)) ~ O(m*n) in worst cases
        Space: O(m + n)
        """
        s1 = set(arr1)                 # O(m)
        s2 = set(arr2)                 # O(n)
        commons = sorted(s1 & s2)      # O(m + n + c log c)

        # helper to sum between indices inclusive in sorted arrays
        # we’ll do linear passes; simple but not optimal
        i = j = 0
        ans = 0
        last = None

        def consume_until_val(A, start, stop_val):
            """sum A[start:idx] until A[idx]==stop_val, return (sum, next_index)"""
            s = 0
            k = start
            while k < len(A) and A[k] != stop_val:
                s += A[k]
                k += 1
            return s, k

        for c in commons:
            # sum up to c (exclusive) on both arrays
            add1, i = consume_until_val(arr1, i, c)
            add2, j = consume_until_val(arr2, j, c)
            ans += max(add1, add2) + c
            i += 1  # skip c
            j += 1

        # tails
        ans += max(sum(arr1[i:]), sum(arr2[j:]))
        return ans


# ---------------------- Demo / Timing Harness ---------------------- #

def run_case(name: str, arr1: List[int], arr2: List[int], solver) -> None:
    """
    Print input, output and timing for a single test case.

    For the optimal solver:
    - Time per call:  O(m + n)
    - Extra space:    O(1)
    """
    t0 = timeit.default_timer()
    ans = solver.maxPathSum(arr1, arr2)
    t1 = timeit.default_timer()
    print(f"{name}:")
    print("  arr1:", arr1)
    print("  arr2:", arr2)
    print("  Max path sum:", ans)
    print(f"  Elapsed: {(t1 - t0):.6f}s\n")


def main():
    print("=== Max Sum Path in Two Arrays — Examples & Timing ===\n")

    fast = Solution()
    slow = SolutionBrute()  # for small validation only

    # ----- Examples from problem -----
    arr1 = [2, 3, 7, 10, 12]
    arr2 = [1, 5, 7, 8]
    run_case("Example 1 (optimal)", arr1, arr2, fast)  # expected 35
    run_case("Example 1 (brute)",   arr1, arr2, slow)

    arr1b = [1, 2, 3]
    arr2b = [3, 4, 5]
    run_case("Example 2 (optimal)", arr1b, arr2b, fast) # expected 15
    run_case("Example 2 (brute)",   arr1b, arr2b, slow)

    # ----- Quick random validation (tiny sizes) -----
    def rand_sorted_distinct(n, lo=1, hi=50):
        # Create sorted unique integers — O(n log n) due to sampling/sort (demo-purpose)
        return sorted(random.sample(range(lo, hi), n))

    arrA = rand_sorted_distinct(8, 1, 40)
    arrB = rand_sorted_distinct(7, 1, 40)
    ans_fast = fast.maxPathSum(arrA, arrB)
    ans_slow = slow.maxPathSum(arrA, arrB)
    print("Random tiny arrays validation:")
    print("  arrA:", arrA)
    print("  arrB:", arrB)
    print("  optimal:", ans_fast, " brute:", ans_slow, " -> equal?", ans_fast == ans_slow, "\n")

    # ----- Larger performance demo (optimal only) -----
    # We build two sorted, distinct arrays with some overlap to mimic production conditions.
    # Note: building these arrays costs O(m log m + n log n) due to sampling/sort — not part of algorithm time.
    m, n = 100_000, 120_000
    base = random.sample(range(1, 2_000_000), m + n // 10)  # pool with potential overlap
    arr_large1 = sorted(base[:m])
    arr_large2 = sorted(base[m - n // 20:m - n // 20 + n])  # overlapping slice

    t0 = timeit.default_timer()
    _ = fast.maxPathSum(arr_large1, arr_large2)   # O(m + n)
    t1 = timeit.default_timer()
    print(f"Large input (m={m}, n={n}) optimal elapsed: {(t1 - t0):.6f}s")


if __name__ == "__main__":
    prog_start = timeit.default_timer()
    main()
    prog_end = timeit.default_timer()
    print("\n==== TOTAL PROGRAM TIME ====")
    print(f"{(prog_end - prog_start):.6f}s")
```

---

## 6) Real-World Use Cases (just the essentials)

* **Merging two revenue streams with shared milestones:** When two product lines share release checkpoints (common dates/IDs), choose the path that maximizes cumulative revenue contribution between checkpoints and count shared milestones once.

* **Dual sensor tracks with common synchronization points:** Two sorted telemetry streams (timestamps) with shared synchronization markers; maximize cumulative “quality” or “signal strength” while switching only at sync points.

* **Two roads with shared junctions:** Given toll/bonus along two sorted routes with common junctions, find the maximum-sum route by switching only at shared junctions and not paying/claiming a junction twice.

* **Data pipeline branches with merge keys:** Two sorted job streams keyed by IDs; selecting the cost/benefit-maximizing branch between equal IDs (merge keys), counting the key once when branches meet.
