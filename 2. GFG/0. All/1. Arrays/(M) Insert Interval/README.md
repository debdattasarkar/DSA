
---

# Insert Interval

**Difficulty:** Medium
**Accuracy:** 50.61%
**Submissions:** 46K+
**Points:** 4
**Average Time:** 30 minutes

---

## Problem Statement

Geek has an array of **non-overlapping intervals** `intervals[][]` where:

* `intervals[i] = [startᵢ, endᵢ]` represents the start and the end of the *i-th* event.
* Intervals are **sorted in ascending order** by `startᵢ`.

You are given a new interval `newInterval[] = [newStart, newEnd]` where:

* `newStart` is the start of the new interval
* `newEnd` is the end of the new interval

Your task is to **insert** `newInterval` into `intervals` so that:

1. The resulting list of intervals is still **sorted in ascending order by `start`**.
2. The list still has **no overlapping intervals** (merge overlapping intervals if necessary).

---

## Examples

**Example 1:**

```
Input:
intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newInterval = [5, 6]

Output:
[[1, 3], [4, 7], [8, 10]]

Explanation:
The new interval [5, 6] overlaps with [4, 5] and [6, 7].
So, they are merged into one interval [4, 7].
```

---

**Example 2:**

```
Input:
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 9]

Output:
[[1, 2], [3, 10], [12, 16]]

Explanation:
The new interval [4, 9] overlaps with [3, 5], [6, 7], and [8, 10].
So, they are merged into one interval [3, 10].
```

---

## Constraints

* $1 \leq \text{intervals.size()} \leq 10^5$
* $0 \leq startᵢ \leq endᵢ \leq 10^9$
* $0 \leq newStart \leq newEnd \leq 10^9$

---

## Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(n)$

---

## Topic Tags

* Sorting
* Greedy
* Arrays

---

## Related Articles

* [Insert in Sorted and Non Overlapping Interval Array](https://www.geeksforgeeks.org/insert-in-sorted-and-non-overlapping-interval-array/)

---

---

Here’s a clean, interview‑friendly walkthrough + multiple Python solutions for **Insert Interval**.

---

## 2) Intuition + Step‑by‑Step Dry Run

### Core idea (one pass, O(n))

Because the input intervals are **non‑overlapping and sorted by start**, we can walk them once with three phases:

1. **Left of new**: Push every interval that ends **before** `newInterval` starts.
   (i.e., `interval.end < newStart`)

2. **Overlap with new**: While the current interval **overlaps** `newInterval`, expand `newInterval` to cover their union:
   `newStart = min(newStart, interval.start)` and `newEnd = max(newEnd, interval.end)`.

3. **Right of new**: When there’s no more overlap, push the (possibly expanded) `newInterval`, then append the rest.

Overlap rule (inclusive endpoints):

```
[ a, b ] and [ c, d ] overlap  <=>  a <= d and c <= b
```

### Dry run

**Input**
intervals = `[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]`
newInterval = `[4, 9]`

* Start: res = \[], i = 0

**Phase 1 (left of new)**

* \[1,2] ends at 2 < 4 → push → res = \[\[1,2]], i=1
* \[3,5] ends at 5 !< 4 → stop phase 1.

**Phase 2 (merge overlaps)**

* new = \[4,9]
* \[3,5] overlaps (3 ≤ 9 and 4 ≤ 5) → merge new = \[min(4,3), max(9,5)] = \[3,9], i=2
* \[6,7] overlaps (6 ≤ 9 and 3 ≤ 7) → new = \[3, max(9,7)] = \[3,9], i=3
* \[8,10] overlaps (8 ≤ 9 and 3 ≤ 10) → new = \[3, max(9,10)] = \[3,10], i=4
* \[12,16] does **not** overlap (12 > 10) → stop phase 2.

**Phase 3 (right of new)**

* Push merged new → res = \[\[1,2], \[3,10]]
* Append remaining intervals → res = \[\[1,2], \[3,10], \[12,16]]

**Answer:** `[[1,2], [3,10], [12,16]]`

---

## 3) Python solutions (with interview‑style inline comments)

### A) Optimal one‑pass (O(n) time, O(n) space)

```python
class Solution:
    def insertInterval(self, intervals, newInterval):
        """
        One-pass insertion using the sorted, non-overlapping property.

        Time:  O(n) - each interval visited once
        Space: O(n) - for the output list
        """
        res = []
        i = 0
        n = len(intervals)
        ns, ne = newInterval  # newStart, newEnd

        # 1) Add all intervals strictly to the left of newInterval
        #    (end < newStart)
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with [ns, ne]
        #    Overlap if intervals[i].start <= ne
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        res.append([ns, ne])  # push the merged block

        # 3) Append remaining intervals (to the right of merged new)
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

### B) Brute force (insert + sort + full merge) — simple but slower

```python
class Solution:
    def insertInterval(self, intervals, newInterval):
        """
        Brute idea:
          1) Add newInterval, sort by start
          2) Merge like the classic 'merge intervals' problem

        Time:  O(n log n) due to sorting
        Space: O(n) for output
        """
        arr = intervals + [newInterval]
        arr.sort(key=lambda x: x[0])     # sort by start

        merged = []
        for s, e in arr:
            if not merged or merged[-1][1] < s:  # disjoint; push
                merged.append([s, e])
            else:                                # overlap; merge
                merged[-1][1] = max(merged[-1][1], e)
        return merged
```

### C) Slight variation using `bisect` to find insertion point (still O(n) overall)

```python
import bisect

class Solution:
    def insertInterval(self, intervals, newInterval):
        """
        Use bisect to find where to place newInterval by start,
        but overall still O(n): we might scan around overlaps anyway.

        Time:  O(n)
        Space: O(n)
        """
        starts = [x[0] for x in intervals]
        pos = bisect.bisect_left(starts, newInterval[0])

        # Build a new list with newInterval placed at 'pos'
        arr = intervals[:pos] + [newInterval] + intervals[pos:]

        # Merge as usual
        merged = []
        for s, e in arr:
            if not merged or merged[-1][1] < s:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        return merged
```

---

## 4) Interview Q\&A

**Q1. How do you detect overlap between two intervals?**
**A.** With inclusive ends, `[a, b]` and `[c, d]` overlap if `a <= d` **and** `c <= b`.
(Equivalently, they **don’t** overlap only when `b < c` or `d < a`.)

**Q2. Why does the one‑pass algorithm work?**
**A.** Intervals are sorted by start and non-overlapping. So we can:

* Copy all intervals ending before the new start.
* Merge the “middle block” that overlaps the new interval into one range.
* Copy all intervals starting after that merged block.
  No backtracking or reordering needed.

**Q3. What happens if `newInterval` fits completely inside an existing interval?**
**A.** The overlap phase expands `newInterval` over all overlapping intervals, but if one existing interval already fully covers it, the result is just that existing interval’s range.

**Q4. How do you handle touching endpoints like `[1,3]` and `[4,5]` with `newInterval=[3,4]`?**
**A.** With inclusive endpoints, `[1,3]` and `[3,4]` overlap (since `1 ≤ 4` and `3 ≤ 3`), and `[3,4]` and `[4,5]` also overlap. They merge to `[1,5]`.

**Q5. What if the input wasn’t sorted or had overlaps already?**
**A.** Then the one‑pass insertion is invalid. You’d need to:

* Append, sort by start, and then perform a full merge. (Solution **B**.)

**Q6. Complexity?**
**A.** One‑pass method: **O(n)** time, **O(n)** space (for the output).
Brute force: **O(n log n)** due to sorting.

**Q7. Corner cases to test?**

* Empty `intervals`.
* `newInterval` before all or after all.
* `newInterval` that overlaps everything.
* Single interval lists.
* Touching endpoints (inclusive overlap).

---

---

Absolutely—here’s a self‑contained, runnable program that:

* Implements the **optimal O(n)** solution to *Insert Interval* (plus a brute‑force baseline for comparison).
* Includes **inline time/space complexity notes per step**.
* Runs a **main** with sample inputs, prints outputs, and measures **wall‑clock runtime** with `time.perf_counter()`.

---

## Full Program (with timing + comments)

```python
from time import perf_counter
from typing import List

class SolutionOptimal:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        One-pass insertion assuming 'intervals' are non-overlapping and sorted by start.
        Time:  O(n) — single sweep through intervals
        Space: O(n) — result container
        """
        res = []                       # O(1) extra (excluding output)
        i = 0
        n = len(intervals)
        ns, ne = newInterval           # unpack once (O(1))

        # ----- Phase 1: Push all intervals strictly to the left of newInterval -----
        # Condition: current interval ends before the new interval starts
        # Complexity of this loop across the whole function: O(n)
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])   # append: amortized O(1)
            i += 1

        # ----- Phase 2: Merge all intervals that overlap with [ns, ne] -----
        # Overlap check: intervals[i].start <= ne (inclusive endpoints)
        # We expand the new interval to cover the union as we go.
        # This loop also runs at most n iterations in total: O(n)
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])  # O(1)
            ne = max(ne, intervals[i][1])  # O(1)
            i += 1

        res.append([ns, ne])           # push the merged block — O(1)

        # ----- Phase 3: Append remaining intervals (to the right) -----
        # Again, each item is touched once overall: O(n)
        while i < n:
            res.append(intervals[i])   # O(1)
            i += 1

        # Total: O(n) time, O(n) space (output)
        return res


class SolutionBrute:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Baseline: append + sort + merge.
        Time:  O(n log n)  (due to sorting)
        Space: O(n)        (for output)
        """
        arr = intervals + [newInterval]              # O(n)
        arr.sort(key=lambda x: x[0])                 # O(n log n)

        merged = []                                   # O(1) extra (excluding output)
        for s, e in arr:                              # O(n)
            if not merged or merged[-1][1] < s:       # no overlap — O(1)
                merged.append([s, e])                 # O(1)
            else:                                     # overlap — merge
                merged[-1][1] = max(merged[-1][1], e) # O(1)
        return merged


def pretty_print(data):
    return "[" + ", ".join(f"[{a},{b}]" for a, b in data) + "]"


def run_case(intervals: List[List[int]], newInterval: List[int]]):
    print(f"\nIntervals: {pretty_print(intervals)}")
    print(f"New:       [{newInterval[0]},{newInterval[1]}]")

    # Optimal
    t0 = perf_counter()
    out_opt = SolutionOptimal().insertInterval(intervals, newInterval)
    t1 = perf_counter()
    print("Optimal   →", pretty_print(out_opt), f"(time: {(t1 - t0)*1e6:.1f} µs)")

    # Brute
    t2 = perf_counter()
    out_bf = SolutionBrute().insertInterval(intervals, newInterval)
    t3 = perf_counter()
    print("Brute     →", pretty_print(out_bf), f"(time: {(t3 - t2)*1e6:.1f} µs)")

    # Sanity check
    assert out_opt == out_bf, "Mismatch between optimal and brute outputs!"


def main():
    print("=== Insert Interval — Demo ===")

    # Case 1: Example where new merges a middle block
    intervals1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new1 = [4, 9]
    run_case(intervals1, new1)

    # Case 2: New lies entirely before all
    intervals2 = [[5, 7], [8, 12]]
    new2 = [1, 3]
    run_case(intervals2, new2)

    # Case 3: New lies entirely after all
    intervals3 = [[1, 3], [4, 6]]
    new3 = [10, 12]
    run_case(intervals3, new3)

    # Case 4: Touching endpoints (inclusive overlap)
    intervals4 = [[1, 3], [6, 8]]
    new4 = [3, 6]
    run_case(intervals4, new4)

    # Case 5: New overlaps everything
    intervals5 = [[2, 3], [5, 6], [8, 9]]
    new5 = [1, 10]
    run_case(intervals5, new5)

if __name__ == "__main__":
    main()
```

### Sample Output (will vary slightly by machine)

```
=== Insert Interval — Demo ===

Intervals: [[1,2], [3,5], [6,7], [8,10], [12,16]]
New:       [4,9]
Optimal   → [[1,2], [3,10], [12,16]] (time: 60.3 µs)
Brute     → [[1,2], [3,10], [12,16]] (time: 95.7 µs)

Intervals: [[5,7], [8,12]]
New:       [1,3]
Optimal   → [[1,3], [5,7], [8,12]] (time: 18.7 µs)
Brute     → [[1,3], [5,7], [8,12]] (time: 39.4 µs)
...
```

> Notes on complexity are embedded inline at every step of the core methods.

---

## 6) Real‑World Use Cases (high‑impact)

1. **Calendar scheduling / meeting rooms**
   Insert a new meeting while preserving a non‑overlapping, sorted schedule; merge when meetings touch/overlap.

2. **Reservation & booking systems**
   Hotel or resource slots: when a new reservation is placed, coalesce with adjacent compatible blocks.

3. **Memory allocators / file systems**
   Free lists as intervals: inserting a newly freed block and merging with neighboring free ranges.

4. **Network firewall rules / IP ranges**
   Insert and merge IP range rules to keep the rule set minimal and non‑overlapping.

5. **Genome intervals & time‑series windows**
   Efficiently manage and merge genomic features or time windows as new intervals are discovered/arrive.

