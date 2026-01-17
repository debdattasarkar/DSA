
# Minimum Number of Workers

**Difficulty:** Medium
**Accuracy:** 59.11%
**Submissions:** 9K+
**Points:** 4

---

## Problem Statement

You are given an array **arr[]**, where `arr[i]` denotes the range of working hours a person at position `i` can cover.

* If `arr[i] != -1`, the person at index `i` can work and cover the time interval
  **[i - arr[i], i + arr[i]]**.
* If `arr[i] == -1`, the person is unavailable and cannot cover any time.

The task is to find the **minimum number of people** required to cover the **entire working day from `0` to `n - 1`**.

If it is **not possible** to fully cover the day, return **-1**.

---

## Examples

### Example 1

**Input:**
`arr[] = [1, 2, 1, 0]`

**Output:**
`1`

**Explanation:**
The person at index `1` can cover the interval `[-1, 3]`.
After adjusting to valid bounds, this becomes `[0, 3]`, which fully covers the entire working day `0` to `n-1`.
Therefore, only **1 person** is required.

---

### Example 2

**Input:**
`arr[] = [2, 3, 4, -1, 2, 0, 0, -1, 0]`

**Output:**
`-1`

**Explanation:**
Persons up to index `2` cover the interval `[0, 6]`, but working hour `7` cannot be covered since `arr[7] = -1`.
As the full working day cannot be covered, the answer is **-1**.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `-1 ≤ arr[i] ≤ arr.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* Greedy
* Sorting
* Arrays

---

## Related Articles

* [**Minimum Sprinklers Required To Be Turned On To Water The Plants**](https://www.geeksforgeeks.org/minimum-sprinkers-required-to-be-turned-on-to-water-the-plants/)

---

---

I’ll explain the greedy interval-cover idea with a dry run, then give brute + interview-standard optimized Python (with comments), plus a quick mnemonic and interviewer Q&A.


## 2) Text explanation (what’s really happening)

Each worker `i` (if `arr[i] != -1`) can cover an interval:

* **left = i - arr[i]**
* **right = i + arr[i]**

But working hours are only valid in **[0, n-1]**, so clamp:

* `left = max(0, left)`
* `right = min(n-1, right)`

Now the problem becomes:

✅ **Minimum number of intervals to cover the entire line [0 .. n-1]**
If impossible → return **-1**

This is the classic **minimum interval cover** greedy:

### Greedy rule (most expected)

1. Sort intervals by `left`.
2. Start from `current_end = 0`
3. Among all intervals with `left <= current_end`, pick the one with **maximum right** (extends farthest).
4. Jump `current_end = farthest_right + 1`, count++.
5. If you cannot extend further → impossible.

---

## Step-by-step Dry Run

### Example 1

`arr = [1, 2, 1, 0]`, `n=4`, target = cover `[0..3]`

Build intervals:

* i=0, r=1 → [0-1, 0+1] = [-1,1] → clamp → **[0,1]**
* i=1, r=2 → [1-2, 1+2] = [-1,3] → clamp → **[0,3]**
* i=2, r=1 → [1,3] → **[1,3]**
* i=3, r=0 → [3,3] → **[3,3]**

Sort by left:
`[0,1], [0,3], [1,3], [3,3]`

Greedy cover:

* need cover from `current_end=0`
* consider intervals with `left<=0`: `[0,1]`, `[0,3]` → farthest right = 3
* pick `[0,3]`, count=1 → now covered up to 3 → done ✅

Answer = **1**

---

### Example 2

`arr = [2,3,4,-1,2,0,0,-1,0]`, `n=9`, target `[0..8]`

Intervals (clamped):

* i=0 r=2 → [0,2]
* i=1 r=3 → [0,4]
* i=2 r=4 → [0,6]
* i=3 -1 → skip
* i=4 r=2 → [2,6]
* i=5 r=0 → [5,5]
* i=6 r=0 → [6,6]
* i=7 -1 → skip
* i=8 r=0 → [8,8]

Greedy:

* start `current_end=0` → best among left<=0 is `[0,6]` → covered to 6
* next need `current_end=7`
* now find interval with `left<=7` that extends to >=7

  * available: [2,6], [5,5], [6,6] … all end <= 6
  * none reaches 7 → stuck ❌

Return **-1**

---

## 3) Python solutions (brute + interview-expected optimized)

### A) Brute (try all subsets) — only for concept, not feasible

This is exponential `O(2^n)` so it’s not usable for `n=1e5`. Mention it only as “baseline idea”.

---

### B) Most expected (Intervals + Sort + Greedy) ✅

**Time:** `O(n log n)` (sorting)
**Space:** `O(n)` (store intervals)

```python
class Solution:
    def minMen(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Build coverage intervals for all available workers
        # Time: O(n), Space: O(n)
        intervals = []
        for i, radius in enumerate(arr):
            if radius == -1:
                continue
            left = max(0, i - radius)
            right = min(n - 1, i + radius)
            intervals.append((left, right))

        # If no intervals, can't cover anything
        if not intervals:
            return -1

        # Sort by start time
        # Time: O(n log n)
        intervals.sort()

        workers_used = 0
        idx = 0
        current_hour = 0  # we need to cover from this hour onward

        while current_hour <= n - 1:
            farthest_reach = -1

            # Among all intervals that start at/before current_hour,
            # pick the one that reaches farthest right.
            # Total scanning across the loop is O(n)
            while idx < len(intervals) and intervals[idx][0] <= current_hour:
                farthest_reach = max(farthest_reach, intervals[idx][1])
                idx += 1

            # If we can't extend coverage, impossible
            if farthest_reach < current_hour:
                return -1

            # We choose one worker (the best reach found)
            workers_used += 1

            # Next uncovered hour is farthest_reach + 1
            current_hour = farthest_reach + 1

        return workers_used
```

---

### C) Alternative (convert to “max reach starting at left” + linear greedy)

Still needs building an array of best reach per left, then greedy like “jump game”.

**Time:** `O(n)` after preprocessing, but preprocessing is also `O(n)`
**Space:** `O(n)`

```python
class Solution:
    def minMen(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # best_right_at_left[l] = maximum right endpoint among intervals starting at l
        # Time: O(n), Space: O(n)
        best_right_at_left = [-1] * n

        for i, radius in enumerate(arr):
            if radius == -1:
                continue
            left = max(0, i - radius)
            right = min(n - 1, i + radius)
            best_right_at_left[left] = max(best_right_at_left[left], right)

        workers_used = 0
        current_end = -1     # coverage end of chosen workers
        farthest = -1        # farthest we can reach while scanning
        i = 0

        # Greedy scan across hours (like minimum jumps)
        # Time: O(n), Space: O(1) extra
        while i < n:
            # Extend farthest reach using intervals that start at i
            farthest = max(farthest, best_right_at_left[i])

            # If we reached the end of current chosen coverage, we must "choose" a worker
            if i > current_end:
                if farthest < i:
                    return -1
                workers_used += 1
                current_end = farthest

                if current_end >= n - 1:
                    return workers_used

            i += 1

        return workers_used
```

---

## 4) Interview: quick recall + expected Q&A

### 5-line pseudo-code template (memorize)

```
intervals = build [max(0,i-a[i]), min(n-1,i+a[i])] for a[i]!=-1
sort intervals by left
cur = 0; i = 0; ans = 0
while cur <= n-1: take max_right among intervals with left<=cur; if none -> -1
ans++; cur = max_right + 1
```

### Mnemonic

**“Cover line like meetings: START ≤ current, pick FARTHEST END.”**
(“Start before me, choose farthest reach”)

### 60-second recall script

1. “Convert each worker to an interval of hours they can cover.”
2. “Now it’s minimum intervals to cover [0..n-1].”
3. “Sort by start, greedily pick the interval that starts before current hour and ends farthest.”
4. “Jump current hour to farthest+1; count workers.”
5. “If stuck at any point → return -1.”

---

### Expected interviewer questions & answers

**Q1. Why greedy works?**
A. At any uncovered point `cur`, picking the interval with the farthest reach among those that can start now is always safe: any other choice covers less and can’t reduce the number of intervals needed.

**Q2. What if multiple intervals start before `cur`?**
A. We don’t pick immediately; we scan all starts ≤ `cur` and choose the maximum right.

**Q3. Complexity?**
A. Build intervals O(n). Sort O(n log n). Greedy scan O(n). Total **O(n log n)** time, **O(n)** space.

**Q4. Edge cases?**
A. All `-1` → -1. First hour not covered by any interval → -1. Already covered by one interval → 1.

---

---


## 5) Real-World Use Cases (few, very relatable)

1. **Shift scheduling / minimum staff to cover the whole day**

   * Each worker can cover a time range around their preferred slot. Find the minimum workers needed to cover all hours of operation.

2. **Network coverage / minimum access points**

   * Each router/AP placed at position `i` covers a radius of units. Need minimum devices to cover the full corridor/road from 0 to n−1.

3. **Security patrol / CCTV placement**

   * Each camera at location `i` covers `[i-r, i+r]`. Choose minimum active cameras to cover all segments.

4. **Irrigation sprinklers (exact same pattern)**

   * Sprinkler `i` covers a radius; minimum sprinklers needed to water the entire line of plants. (This is exactly the related-article mapping.)

---

## 6) Full Program (timed run + inline complexity + sample input/output)

This runnable program:

* Reads `arr` (space-separated)
* Computes minimum workers using **interval + sort + greedy** (most expected)
* Prints input and output
* Prints total runtime using `time.perf_counter()`

### Input format (stdin)

If you provide stdin:

* Line 1: `arr` values space-separated
  Example:
  `1 2 1 0`

If no stdin, demo uses Example 1: `[1, 2, 1, 0]` → output `1`

```python
import sys
import time


class Solution:
    def minMen(self, arr):
        """
        Interval cover with greedy.
        Time: O(n log n) due to sorting intervals
        Aux Space: O(n) for storing intervals
        """
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: Build intervals for available workers
        # Time: O(n), Space: O(n)
        intervals = []
        for i, radius in enumerate(arr):
            if radius == -1:
                continue
            left = max(0, i - radius)
            right = min(n - 1, i + radius)
            intervals.append((left, right))

        if not intervals:
            return -1

        # Step 2: Sort intervals by start
        # Time: O(n log n)
        intervals.sort()

        # Step 3: Greedy cover from hour 0 to n-1
        # Time: O(n) scanning intervals once
        workers_used = 0
        idx = 0
        current_hour = 0

        while current_hour <= n - 1:
            farthest_reach = -1

            # Consider all intervals that can start covering at/before current_hour
            while idx < len(intervals) and intervals[idx][0] <= current_hour:
                farthest_reach = max(farthest_reach, intervals[idx][1])
                idx += 1

            # If none can cover current_hour, impossible
            if farthest_reach < current_hour:
                return -1

            # We "choose" one worker (the one that gives farthest reach)
            workers_used += 1

            # Next uncovered hour begins after farthest_reach
            current_hour = farthest_reach + 1

        return workers_used


def main():
    # Measure total program runtime (parse + solve + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [1, 2, 1, 0]
    else:
        # ---------------- INPUT MODE ----------------
        # Time: O(n) parsing, Space: O(n) storing arr
        arr = list(map(int, data.split()))

    # Solve
    # Time: O(n log n), Space: O(n)
    answer = solver.minMen(arr)

    print("Input:")
    print("arr =", arr)

    print("\nOutput:")
    print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Demo Output (expected)

**Input:** `arr = [1, 2, 1, 0]`
**Output:** `1` (+ runtime)

---
