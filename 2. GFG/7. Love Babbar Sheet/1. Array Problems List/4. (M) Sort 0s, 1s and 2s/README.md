# Sort 0s, 1s and 2s

**Difficulty:** Medium
**Accuracy:** 50.58%
**Submissions:** 778K+
**Points:** 4
**Average Time:** 10m

---

## Problem Statement

Given an array `arr[]` containing only **0s, 1s, and 2s**, sort the array in ascending order.

You need to solve this problem **without** utilizing the built-in sort function.

---

## Examples

### Example 1

**Input:** `arr[] = [0, 1, 2, 0, 1, 2]`
**Output:** `[0, 0, 1, 1, 2, 2]`
**Explanation:** 0s, 1s, and 2s are segregated into ascending order.

### Example 2

**Input:** `arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1]`
**Output:** `[0, 0, 0, 0, 1, 1, 1, 1, 2, 2]`
**Explanation:** 0s, 1s, and 2s are segregated into ascending order.

**Follow up:** Could you come up with a **one-pass** algorithm using only **constant extra space**?

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 2`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

Paytm • Flipkart • Morgan Stanley • Amazon • Microsoft • OYO Rooms • Samsung • Snapdeal • Hike • MakeMyTrip • Ola Cabs • Walmart • MAQ Software • Adobe • Yatra.com • SAP Labs • Qualcomm

---

## Topic Tags

Arrays • Sorting • Data Structures • Algorithms

---

## Related Interview Experiences

* Paytm Interview Experience Set 14 For Senior Android Developer
* Ola Cabs Interview Experience Set 4 For SDE 2
* Paytm Interview Experience Set 5 Recruitment Drive
* Amazon Interview Experience For SDE Internship

---

## Related Articles

* [Sort An Array Of 0s 1s And 2s](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)

---

---
got it — let’s make “Sort 0s, 1s and 2s” interview-ready.

---

## 2) Explanation + step-by-step dry run

### Problem recap

Array contains only **0, 1, 2**. Sort in **ascending order** without using built-in sort.
Goal: **O(n) time**, **O(1) extra space**, ideally **one pass**.

### Two classic approaches

1. **Counting (brute but simple)**

   * Count how many 0s, 1s, 2s; then overwrite the array.
   * Time `O(n)`, Space `O(1)` (3 counters). Two passes over the array.

2. **Dutch National Flag (DNF) — one pass, in-place (most expected)**
   Maintain three regions using pointers:

   * `low`   : boundary after the last 0
   * `mid`   : current element under inspection
   * `high`  : boundary before the first 2 (from the right)

   Invariant at any moment:

   ```
   [ 0s | 1s/unknown | unknown | 2s ]
     0..low-1      low..mid-1    mid..high      high+1..end
   ```

   Rules while `mid <= high`:

   * `arr[mid] == 0` → swap `arr[low]`↔`arr[mid]`, ++low, ++mid
   * `arr[mid] == 1` → just ++mid
   * `arr[mid] == 2` → swap `arr[mid]`↔`arr[high]`, --high (do **not** ++mid; the new `arr[mid]` must be inspected)

#### Dry run (DNF)

Input: `arr = [0, 1, 2, 0, 1, 2]`

Start: `low=0, mid=0, high=5`

| Step | arr                | low | mid | high | action                                                                |
| ---: | ------------------ | --: | --: | ---: | --------------------------------------------------------------------- |
|    1 | [0, 1, 2, 0, 1, 2] |   0 |   0 |    5 | arr[mid]=0 → swap mid↔low (no change), low=1, mid=1                   |
|    2 | [0, 1, 2, 0, 1, 2] |   1 |   1 |    5 | arr[mid]=1 → mid=2                                                    |
|    3 | [0, 1, 2, 0, 1, 2] |   1 |   2 |    5 | arr[mid]=2 → swap mid↔high → [0,1,2,0,1,2] (2 swapped with 2), high=4 |
|    4 | [0, 1, 1, 0, 2, 2] |   1 |   2 |    4 | arr[mid]=2 → swap mid↔high → [0,1,1,0,2,2], high=3                    |
|    5 | [0, 0, 1, 1, 2, 2] |   1 |   2 |    3 | arr[mid]=1 → mid=3                                                    |
|    6 | [0, 0, 1, 1, 2, 2] |   1 |   3 |    3 | arr[mid]=1 → mid=4 > high stop                                        |

Result: `[0, 0, 1, 1, 2, 2]`

---

## 3) Python solutions (brute + optimal, with interview-style comments)

```python
class Solution:
    def sort012(self, arr):
        """
        Dutch National Flag (single pass, in-place).
        Time  : O(n)   -- each index visited at most once
        Space : O(1)   -- constant extra pointers
        """
        low, mid, high = 0, 0, len(arr) - 1

        # Maintain invariants:
        # 0..low-1   -> all 0s
        # low..mid-1 -> all 1s
        # mid..high  -> unknown
        # high+1..n-1-> all 2s
        while mid <= high:
            if arr[mid] == 0:
                # put 0 into the 0s region, expand both low and mid
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # correct region, just advance
                mid += 1
            else:  # arr[mid] == 2
                # put 2 into the 2s region; do NOT advance mid yet
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr  # returning for convenience; in many platforms in-place is enough
```

### Alternative A) Counting (two passes, simplest to explain)

```python
class SolutionCounting:
    def sort012(self, arr):
        """
        Count 0s, 1s, 2s then overwrite.
        Time  : O(n)   (count) + O(n) (rewrite) -> O(n)
        Space : O(1)   (three counters)
        """
        cnt0 = cnt1 = cnt2 = 0
        for x in arr:           # O(n)
            if x == 0:   cnt0 += 1
            elif x == 1: cnt1 += 1
            else:        cnt2 += 1

        i = 0
        for _ in range(cnt0):   # O(cnt0)
            arr[i] = 0; i += 1
        for _ in range(cnt1):   # O(cnt1)
            arr[i] = 1; i += 1
        for _ in range(cnt2):   # O(cnt2)
            arr[i] = 2; i += 1
        return arr
```

### Alternative B) Three-pointer variant with `while` safety note

Same as the main DNF solution; the key interview gotcha: **after swapping a 2 to the end, don’t increment `mid`** until you examine the new `arr[mid]`.

---

## 4) Interviewer-style Q&A

**Q1. Why not just sort?**
Sorting is `O(n log n)`. With only three distinct values we can do **O(n)** and **O(1)** space via DNF or counting.

**Q2. Prove one-pass correctness for DNF.**
Maintain the invariant:

* `[0..low-1]` are all 0s,
* `[low..mid-1]` are all 1s,
* `[mid..high]` unknown,
* `[high+1..n-1]` all 2s.
  Each rule (0,1,2 case) **shrinks** the unknown window while keeping other regions valid.

**Q3. Why not advance `mid` after swapping with `high`?**
Because the element swapped into `mid` is **unprocessed**; it could be 0/1/2. We must re-check it.

**Q4. Stability required?**
No. The task is just to group 0s, 1s, 2s; order within groups is irrelevant.

**Q5. When is counting preferable?**
When readability trumps single-pass, or when multiple passes are acceptable; also convenient if you later need counts anyway.

**Q6. Edge cases?**
Already sorted arrays, reverse sorted, all same values, and tiny arrays (size 1–2). DNF handles all.

---

---

awesome — here’s a **complete, runnable Python program** for **Sort 0s, 1s and 2s** that:

* reads the array from stdin (space-separated 0/1/2),
* runs **Dutch National Flag (one pass, O(n), O(1))** and **Counting (two pass, O(n), O(1))**,
* prints the sorted array for each,
* and **times** each method (single wall-clock + `timeit` average),
* with **inline comments** noting time/space at each step.

---

## Full Program

```python
#!/usr/bin/env python3
"""
Sort 0s, 1s and 2s (a.k.a. Dutch National Flag problem)

- Input : one line of space-separated integers (each is 0, 1 or 2)
- Output: sorted arrays from two approaches + timings

Approaches:
  A) Dutch National Flag (DNF)  -> single pass, in-place, O(n) time, O(1) space
  B) Counting                  -> two passes, O(n) time, O(1) space
"""

from time import perf_counter
import timeit
import sys


# -------------------------------------------------------------------
# Approach A: Dutch National Flag (one pass, O(1) space)
# -------------------------------------------------------------------
def sort012_dnf(arr):
    """
    In-place DNF.
    Invariant:
      0..low-1   -> all 0s
      low..mid-1 -> all 1s
      mid..high  -> unknown
      high+1..n-1-> all 2s

    Time  : O(n)    (each index examined at most once)
    Space : O(1)    (three pointers)
    """
    low, mid, high = 0, 0, len(arr) - 1  # O(1)

    # Main loop shrinks [mid..high] unknown region -> O(n) total
    while mid <= high:
        if arr[mid] == 0:
            # put 0 to the front region
            arr[low], arr[mid] = arr[mid], arr[low]  # O(1)
            low += 1                                  # O(1)
            mid += 1                                  # O(1)
        elif arr[mid] == 1:
            # already in correct middle region
            mid += 1                                  # O(1)
        else:  # arr[mid] == 2
            # put 2 to the back region; DO NOT advance mid yet
            arr[mid], arr[high] = arr[high], arr[mid] # O(1)
            high -= 1                                  # O(1)
    return arr  # in-place but return for convenience


# -------------------------------------------------------------------
# Approach B: Counting (two passes, still O(n), O(1) extra)
# -------------------------------------------------------------------
def sort012_counting(arr):
    """
    Count zeros/ones/twos then overwrite.

    Time  : O(n) to count + O(n) to write -> O(n)
    Space : O(1) (three integer counters)
    """
    cnt0 = cnt1 = cnt2 = 0  # O(1)
    for x in arr:           # O(n)
        if x == 0:   cnt0 += 1
        elif x == 1: cnt1 += 1
        else:        cnt2 += 1

    i = 0
    for _ in range(cnt0):   # O(cnt0)
        arr[i] = 0; i += 1
    for _ in range(cnt1):   # O(cnt1)
        arr[i] = 1; i += 1
    for _ in range(cnt2):   # O(cnt2)
        arr[i] = 2; i += 1
    return arr


# ------------------------------ timing utils ------------------------------
def time_single_run(func, *args, **kwargs):
    """Single wall-clock timing using perf_counter."""
    t0 = perf_counter()
    result = func(*args, **kwargs)
    t1 = perf_counter()
    return result, (t1 - t0)

def time_with_timeit(callable_stmt, number=5):
    """Average runtime over `number` runs using timeit."""
    total = timeit.timeit(callable_stmt, number=number)
    return total / number


# --------------------------------- main -----------------------------------
def main():
    # ---------- Input ----------
    # Example input: 0 1 2 0 1 2
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        print("No input provided. Example:\n  0 1 2 0 1 2")
        return

    arr = list(map(int, tokens))   # O(n) parse
    if not all(x in (0, 1, 2) for x in arr):
        print("Input must contain only 0, 1, or 2.")
        return

    print("Original:", arr)

    # ---------- A) DNF ----------
    arr_a = arr.copy()
    out_a, t_a = time_single_run(sort012_dnf, arr_a)
    avg_a = time_with_timeit(lambda: sort012_dnf(arr.copy()), number=5)
    print("\nSorted (DNF, one pass):", out_a)
    print(f"  Single-run time : {t_a:.8f} s")
    print(f"  Avg over 5 runs : {avg_a:.8f} s")

    # ---------- B) Counting ----------
    arr_b = arr.copy()
    out_b, t_b = time_single_run(sort012_counting, arr_b)
    avg_b = time_with_timeit(lambda: sort012_counting(arr.copy()), number=5)
    print("\nSorted (Counting):     ", out_b)
    print(f"  Single-run time : {t_b:.8f} s")
    print(f"  Avg over 5 runs : {avg_b:.8f} s")

    # Complexity recap
    print("\nComplexity Summary:")
    print("  DNF      : Time O(n), Space O(1)")
    print("  Counting : Time O(n), Space O(1) (two passes)")

if __name__ == "__main__":
    """
    Example:
      echo "0 1 2 0 1 2" | python3 sort012.py
    """
    main()
```

### Example Run

**Input**

```
0 1 2 0 1 2
```

**Output** (times vary per machine)

```
Original: [0, 1, 2, 0, 1, 2]

Sorted (DNF, one pass): [0, 0, 1, 1, 2, 2]
  Single-run time : 0.0000xx s
  Avg over 5 runs : 0.0000xx s

Sorted (Counting):      [0, 0, 1, 1, 2, 2]
  Single-run time : 0.0000xx s
  Avg over 5 runs : 0.0000xx s

Complexity Summary:
  DNF      : Time O(n), Space O(1)
  Counting : Time O(n), Space O(1) (two passes)
```

---

## 6) Real-World Use Cases (high-impact)

* **Streaming telemetry bucketing:** Fast in-place bucketing of states (e.g., OK/WARN/ALERT = 0/1/2) before aggregation.
* **Color quantization / label grouping:** Grouping a small, fixed set of labels (e.g., three classes) efficiently without sort.
* **Network packet prioritization:** Partition queues into *low/medium/high* priority (0/1/2) in a single pass for scheduling.

> In interviews, prefer **DNF** (one pass, O(1) space). Mention **Counting** as a simple alternative and call out the key gotcha: **after swapping a 2 to the end, don’t advance `mid` until you re-check the new element**.
