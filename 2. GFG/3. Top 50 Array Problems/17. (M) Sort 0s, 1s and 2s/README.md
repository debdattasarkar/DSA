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

Here’s the interview-ready breakdown for **Sort 0s, 1s and 2s** (aka the *Dutch National Flag* problem).

---

## 2) Intuition + Step-by-step dry run

### What we need

Array has only `0, 1, 2`. Sort **in place** with **O(1)** extra space and **O(n)** time.

### Two classic ways

1. **Counting (2 passes)**: count #0, #1, #2, then overwrite the array accordingly.
2. **Dutch National Flag (DNF, 1 pass)**: keep three regions using pointers:

   * `[0 .. low-1]` → all 0s
   * `[low .. mid-1]` → all 1s
   * `[high+1 .. n-1]` → all 2s
   * Examine `arr[mid]` and expand/shrink regions by swapping/incrementing.

### DNF Dry Run

Input: `arr = [2, 0, 2, 1, 1, 0]`
Start: `low=0, mid=0, high=5`

| Step | arr                 | low | mid | high | Action / Invariant                                                            |
| ---: | ------------------- | --: | --: | ---: | ----------------------------------------------------------------------------- |
|    1 | \[2, 0, 2, 1, 1, 0] |   0 |   0 |    5 | arr\[mid]=2 → swap(mid,high) → \[0,0,2,1,1,2], high=4 (mid stays to re-check) |
|    2 | \[0, 0, 2, 1, 1, 2] |   0 |   0 |    4 | arr\[mid]=0 → swap(mid,low) (same idx) → low=1, mid=1                         |
|    3 | \[0, 0, 2, 1, 1, 2] |   1 |   1 |    4 | arr\[mid]=0 → swap(mid,low) (same idx) → low=2, mid=2                         |
|    4 | \[0, 0, 2, 1, 1, 2] |   2 |   2 |    4 | arr\[mid]=2 → swap(mid,high) → \[0,0,1,1,2,2], high=3                         |
|    5 | \[0, 0, 1, 1, 2, 2] |   2 |   2 |    3 | arr\[mid]=1 → mid=3                                                           |
|    6 | \[0, 0, 1, 1, 2, 2] |   2 |   3 |    3 | arr\[mid]=1 → mid=4 (> high) stop.                                            |

Result: `[0, 0, 1, 1, 2, 2]`.

Key DNF rules:

* `arr[mid] == 0`: swap with `low`, then `low++, mid++`
* `arr[mid] == 1`: `mid++`
* `arr[mid] == 2`: swap with `high`, then `high--` (do **not** increment `mid`, because the new `arr[mid]` is unseen)

---

## 3) Python solutions (brute + optimal), with interview-level comments

### A) Optimal — Dutch National Flag: **O(n) time, O(1) space, 1 pass**

```python
class Solution:
    def sort012(self, arr):
        """
        Dutch National Flag (DNF) partitioning.
        Invariants during the loop:
          [0..low-1]   -> 0s
          [low..mid-1] -> 1s
          [mid..high]  -> unknown
          [high+1..n-1]-> 2s

        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if arr[mid] == 0:
                # put 0 into the 0s region, expand both low and mid
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                # 1 is in the correct middle region; just advance
                mid += 1
            else:  # arr[mid] == 2
                # put 2 into the 2s region, shrink high
                # DON'T advance mid; the swapped-in value is unprocessed
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
```

### B) Easy & reliable — Counting (2 passes): **O(n) time, O(1) space**

```python
class SolutionCount:
    def sort012(self, arr):
        """
        Count #0, #1, #2 in one pass; overwrite in a second pass.

        Time:  O(n)
        Space: O(1) extra (writes are in-place)
        """
        c0 = c1 = c2 = 0
        for x in arr:              # O(n)
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1

        # Overwrite in-place in O(n)
        i = 0
        for _ in range(c0):
            arr[i] = 0; i += 1
        for _ in range(c1):
            arr[i] = 1; i += 1
        for _ in range(c2):
            arr[i] = 2; i += 1
```

### C) Brute (for completeness) — Bubble/Selection sort: **O(n²)** time

> Not recommended; just a baseline if asked “what’s the naive approach?”

```python
class SolutionBrute:
    def sort012(self, arr):
        """
        Plain bubble sort; avoids built-in sort but is O(n^2).
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

## 4) Common interview Q\&A

**Q1. Why doesn’t DNF increment `mid` when swapping with `high`?**
Because the value swapped in from `high` is **unseen**—it could be 0/1/2. We must examine it next, so keep `mid` to re-check.

**Q2. Is DNF stable?**
No. Relative order of equal elements can change. Stability is irrelevant since values are identical and only 0/1/2 appear.

**Q3. Counting vs DNF—when to prefer which?**

* **DNF**: one pass, minimal writes, in-place, O(1) space; often preferred in interviews.
* **Counting**: super simple and safe; two passes but still O(n). Good if the domain is tiny and fixed.

**Q4. What if the array contains values other than 0,1,2?**
Both DNF and counting assume only {0,1,2}. If other values may appear, validate or extend to multi-bucket counting.

**Q5. Edge cases?**
Empty array, all same elements (\[0,0,...] etc.), already sorted, reverse sorted—DNF handles them all.

**Q6. Why is this called the Dutch National Flag?**
Because we partition into three bands (0,1,2), analogous to the three colors (stripes) of the Dutch flag.

---

**Tip:** In interviews, lead with the DNF approach, mention counting as an alternative, and explicitly state the loop invariants—they’re often what the interviewer is looking for.


---

---

Below is a complete, runnable Python script that:

* Implements **Dutch National Flag (DNF)** — one-pass, O(n) time, O(1) space (optimal)
* Implements **Counting** — two-pass, O(n) time, O(1) space (simple & reliable)
* Runs both on a few **sample inputs**, checks correctness, and **times** each run using `timeit`
* Includes **inline complexity notes** for each step and prints the outputs

---

```python
from typing import List
import timeit
import random

# ============================================================
# Sort 0s, 1s, and 2s
# ============================================================

class SolutionDNF:
    def sort012(self, arr: List[int]) -> None:
        """
        Dutch National Flag (DNF) in-place partitioning.

        Loop invariants at any time:
          [0 .. low-1]   -> all 0s            (size = low)
          [low .. mid-1] -> all 1s            (size = mid - low)
          [mid .. high]  -> unknown           (to be processed)
          [high+1 .. n-1]-> all 2s            (size = n-1 - high)

        Time Complexity:
          - The while loop visits each element at most a constant number of times -> O(n)
        Space Complexity:
          - Uses a handful of pointers and temp swaps -> O(1)
        """
        n = len(arr)                      # O(1)
        low, mid, high = 0, 0, n - 1      # O(1)

        while mid <= high:                # O(n) iterations overall
            if arr[mid] == 0:
                # Place 0 into the 0s region by swapping with low
                arr[low], arr[mid] = arr[mid], arr[low]   # O(1)
                low += 1                                   # O(1)
                mid += 1                                   # O(1)
            elif arr[mid] == 1:
                # 1 already in the middle region
                mid += 1                                   # O(1)
            else:  # arr[mid] == 2
                # Place 2 into the 2s region by swapping with high
                arr[mid], arr[high] = arr[high], arr[mid]  # O(1)
                high -= 1                                  # O(1)
                # NOTE: do NOT mid += 1 here; the swapped-in item at mid is unprocessed.


class SolutionCount:
    def sort012(self, arr: List[int]) -> None:
        """
        Counting solution: count #0, #1, #2 (one pass) then overwrite (second pass).

        Time Complexity:
          - Count pass: O(n)
          - Overwrite pass: O(n)
          -> Overall: O(n)
        Space Complexity:
          - A few integer counters and index variable -> O(1)
        """
        c0 = c1 = c2 = 0                  # O(1)
        for x in arr:                     # O(n)
            if x == 0: c0 += 1
            elif x == 1: c1 += 1
            else: c2 += 1

        i = 0                              # O(1)
        for _ in range(c0):                # O(c0)
            arr[i] = 0; i += 1
        for _ in range(c1):                # O(c1)
            arr[i] = 1; i += 1
        for _ in range(c2):                # O(c2)
            arr[i] = 2; i += 1


# ---------------- Demo / main with timing ----------------
def run_and_time(method_name: str, sorter, arr: List[int]) -> List[int]:
    """
    Helper to copy input, run sorter.sort012, and time it.
    Returns the sorted list and prints timing.
    """
    data = arr[:]  # copy input so both algorithms see the same input
    t0 = timeit.default_timer()
    sorter.sort012(data)
    t1 = timeit.default_timer()
    print(f"{method_name:>14}: output={data}  time={(t1 - t0):.6f}s")
    return data


def main():
    print("=== Sort 0s, 1s, and 2s — Demo & Timing ===\n")

    dnf = SolutionDNF()
    cnt = SolutionCount()

    # ---------- Example test cases (with inputs & outputs) ----------
    tests = [
        [0, 1, 2, 0, 1, 2],
        [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 1],
        [2, 0, 2, 1, 1, 0],
        [2, 2, 2, 1, 1, 0, 0, 0],
        [1, 1, 1, 1],
        [0],
    ]

    for idx, arr in enumerate(tests, 1):
        print(f"-- Case {idx}: input={arr}")
        out_dnf = run_and_time("DNF (1-pass)", dnf, arr)
        out_cnt = run_and_time("Counting",     cnt, arr)
        assert out_dnf == out_cnt, "Mismatch between DNF and Counting results!"
        print("-" * 80)

    # ---------- Larger benchmark to show scaling ----------
    print("\n-- Larger benchmark --")
    random.seed(42)
    big = [random.choice((0, 1, 2)) for _ in range(300000)]  # 300k elements
    _ = run_and_time("DNF (1-pass)", dnf, big)
    _ = run_and_time("Counting",     cnt, big)

if __name__ == "__main__":
    start_all = timeit.default_timer()
    main()
    end_all = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end_all - start_all):.6f} seconds")
```

---

## 6) Real-World Use Cases (important ones)

* **Priority bucketing (3 levels):** Fast, in-place grouping for systems that treat requests or tasks as **low / normal / high** priority.
* **Triage/queue segregation:** Segregate incidents (e.g., **P0 / P1 / P2**) to process highest urgency first with O(1) memory.
* **Image/label preprocessing:** Many pipelines store small-class labels (e.g., **background / edge / foreground = 0/1/2**)—quickly reorder or compact by label using DNF.

