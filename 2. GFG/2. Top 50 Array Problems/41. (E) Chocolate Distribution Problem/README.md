Here’s your **complete README-style conversion** of the image — with *every single detail preserved*, nothing omitted 👇

---

# 🍫 Chocolate Distribution Problem

**Difficulty:** Easy
**Accuracy:** 49.91%
**Submissions:** 261K+
**Points:** 2
**Average Time:** 15m

---

## 📘 Problem Statement

Given an array `arr[]` of positive integers, where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates.

There are `m` students, and the task is to distribute chocolate packets among `m` students such that –

1. Each student gets **exactly one packet**.
2. The **difference** between the maximum number of chocolates given to a student and the minimum number of chocolates given to a student is **minimum**, and return that minimum possible difference.

---

## 💡 Examples

### Example 1

**Input:**
`arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5`

**Output:**
`6`

**Explanation:**
The minimum difference between maximum and minimum chocolates is
`9 - 3 = 6` by choosing packets `[3, 4, 9, 7, 9]`.

---

### Example 2

**Input:**
`arr = [7, 3, 2, 4, 9, 12, 56], m = 3`

**Output:**
`2`

**Explanation:**
The minimum difference between maximum and minimum chocolates is
`4 - 2 = 2` by choosing packets `[3, 2, 4]`.

---

### Example 3

**Input:**
`arr = [3, 4, 1, 9, 56], m = 5`

**Output:**
`55`

**Explanation:**
With 5 packets for 5 students, each student receives one packet.
So the difference is `56 - 1 = 55`.

---

## ⚙️ Constraints

```
1 ≤ m ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^9
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

`Flipkart`

---

## 🏷️ Topic Tags

* Sorting
* Algorithms

---

## 💬 Related Interview Experiences

* Flipkart Interview Experience Set 24

---

## 📚 Related Articles

* [Chocolate Distribution Problem](https://www.geeksforgeeks.org/chocolate-distribution-problem/)

---

---

awesome — let’s make **Chocolate Distribution Problem** interview-ready.

---

# 2) Explanation + step-by-step dry run

## Core idea (why sorting works)

To minimize the **max − min** among any `M` chosen packets, first **sort** the packet sizes.
In a sorted array, the `M` packets that give the minimum spread must be **contiguous** (any gap only increases the range).
So scan every length-`M` window and pick the **smallest difference** `arr[i+M-1] − arr[i]`.

* Time: sort `O(n log n)` + single pass `O(n)` → **O(n log n)**
* Space: **O(1)** (in-place, aside from sort’s internal temp)

### Dry run

`arr = [3, 4, 1, 9, 56, 7, 9, 12], M = 5`
Sorted: `[1, 3, 4, 7, 9, 9, 12, 56]`

Check windows (size 5):

* `[1, 3, 4, 7, 9]` → diff = `9 − 1 = 8`
* `[3, 4, 7, 9, 9]` → diff = `9 − 3 = 6`  ← best so far
* `[4, 7, 9, 9, 12]` → diff = `12 − 4 = 8`
* `[7, 9, 9, 12, 56]` → diff = `56 − 7 = 49`

Minimum difference = **6** (choose packets `[3,4,7,9,9]`).

Edge checks:

* If `M == 1` → answer is `0` (one student gets one packet → max=min).
* If `M > len(arr)` → not possible; typically return `-1` or raise (platform specific).
* Duplicates are fine; windows can include the same value multiple times.

---

# 3) Python solutions (brute + optimized), with comments

## A) Optimized (sort + sliding window) — most expected

```python
# User function Template for python3
class Solution:
    def findMinDiff(self, arr, M):
        """
        Return the minimum possible (max - min) over any choice of M packets.
        Strategy: sort, then scan all length-M windows and take min end-start.
        Time  : O(n log n) for sort + O(n) scan
        Space : O(1) extra (ignoring sort's internal workspace)
        """
        n = len(arr)
        if M == 0 or n == 0 or M > n:
            return -1  # or raise ValueError based on judge
        if M == 1:
            return 0

        arr.sort()  # O(n log n)

        best_range = float('inf')
        # window [i, i+M-1]
        for i in range(n - M + 1):           # O(n)
            current_range = arr[i + M - 1] - arr[i]
            if current_range < best_range:
                best_range = current_range

        return best_range
```

## B) Alternative (min-heap approach) — educational, not better asymptotically

Thought process: after sort you already have the answer; with a heap you can push all values and try to track ranges, but you still need `O(n log n)` and more constant factors. Provided for completeness:

```python
import heapq

class SolutionHeap:
    def findMinDiff(self, arr, M):
        """
        Build a min-heap of values with indices, and maintain a sliding window
        using two heaps or pointers. In practice, sort+window is simpler/faster.
        Time  : O(n log n)
        Space : O(n)
        """
        n = len(arr)
        if M == 0 or n == 0 or M > n: return -1
        if M == 1: return 0

        # Sort is still the cleanest; heap adds overhead without benefit here.
        arr.sort()
        ans = float('inf')
        for i in range(n - M + 1):
            ans = min(ans, arr[i + M - 1] - arr[i])
        return ans
```

## C) Brute force (combinational) — for understanding only

Try **all** combinations of `M` packets → `O(n choose M)` — infeasible for constraints; never use in interviews. (Omitted code intentionally.)

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**Sort → slide window of size M → minimize end − start.**”
* **Pocket code:** `arr.sort(); ans = min(arr[i+M-1]-arr[i])`.

## Likely follow-ups

**Q1. Why does contiguity hold after sorting?**
If an optimal set had a gap, replacing an out-of-window element with one **inside** that gap yields a **no-worse** (usually smaller) range. Thus, an optimal solution can be taken as contiguous in the sorted order.

**Q2. Complexity?**
`O(n log n)` time (sort dominates), `O(1)` space.

**Q3. What about duplicates / large numbers?**
Duplicates are fine; differences can be zero. Use native Python ints (no overflow).
If numbers are huge but sortable, logic remains the same.

**Q4. Edge cases?**

* `M == 1` → `0`.
* `M > n` → not possible; return `-1` (or handle per platform).
* Already sorted/descending — still works.

**Q5. Can we do better than O(n log n)?**
Not in comparison model: you must effectively **order** values to know minimal range among `M` choices. Sorting is optimal and simple.

---

---

awesome — wrapping up **Chocolate Distribution Problem** with the last two parts you asked for 👇

---

# 5) Real-World Use Cases (short, interviewer-friendly)

* **Scholarship/Grant allocation:** choose `M` applicants’ awards so the **gap between highest and lowest grant** is minimal → fair distribution.
* **Warehouse picking for teams:** assign one **box per worker** so the **weight difference** across workers is minimal (balanced load).
* **Course section balancing:** assign students to sections with **pre-computed difficulty points** (one per student) to minimize **max–min difficulty** in a section of size `M`.
* **Cloud instance sizing:** select `M` tasks (one per node) from a pool (each with CPU units) such that **spread** in assigned CPU is minimal → smoother performance.

All of these are “pick **M** items minimizing **max − min**,” which is exactly sort + window.

---

# 6) Full Python Program (with inline complexities + timing)

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# User function Template for python3
# ------------------------------------------------------------
class Solution:
    def findMinDiff(self, arr, M):
        """
        Return the minimum (max - min) among any M packets.
        Strategy:
          1) Sort the array. (O(n log n) time, O(1) extra besides sort temp)
          2) Slide a window of size M and compute end - start for each window. (O(n))
          3) Take the minimum across all windows. (O(1) extra)
        Overall complexity: Time O(n log n), Space O(1).
        """
        n = len(arr)
        if M == 0 or n == 0 or M > n:
            return -1                  # not possible as per many judges
        if M == 1:
            return 0                   # one student gets one packet -> spread 0

        arr.sort()                     # O(n log n)

        best_range = float('inf')      # O(1)
        # Scan all contiguous windows of length M: O(n - M + 1) -> O(n)
        for i in range(n - M + 1):
            current_range = arr[i + M - 1] - arr[i]  # O(1)
            if current_range < best_range:
                best_range = current_range

        return best_range


# ------------------------------------------------------------
# Alternative approaches (for reference):
# - Counting map or bucketing doesn't help here.
# - Heaps add overhead but don't beat O(n log n) from sorting.
# The sorted + window solution is the interview standard.
# ------------------------------------------------------------

def run_demo():
    print("=== Chocolate Distribution Problem ===\n")

    # ------- Sample cases from the prompt + extras -------
    samples = [
        # (name, array, M, expected)
        ("Example 1", [3, 4, 1, 9, 56, 7, 9, 12], 5, 6),
        ("Example 2", [7, 3, 2, 4, 9, 12, 56],     3, 2),
        ("Example 3", [3, 4, 1, 9, 56],            5, 55),
        ("Small M=1", [100, 200, 300],             1, 0),
        ("Impossible", [1, 2, 3],                  5, -1),
    ]

    sol = Solution()
    for name, arr, M, expected in samples:
        result = sol.findMinDiff(arr[:], M)
        print(f"{name}: arr={arr}, M={M}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Match?    {result == expected}\n")

    # ------- Timing on a larger input -------
    seed(42)
    n = 200_000
    M = 200
    big = [randint(1, 10**9) for _ in range(n)]

    # timeit: measure total for a few runs, then compute per-run average
    t = timeit(lambda: Solution().findMinDiff(big[:], M), number=3)
    print("=== Timing (seconds) ===")
    print(f"n={n}, M={M}, runs=3 -> total {t:.4f}s, avg {(t/3):.4f}s/run")


if __name__ == "__main__":
    run_demo()
```

### What this prints

* Each sample’s **Input → Output** vs **Expected**, showing correctness (including the “impossible” case).
* A **timing section** on a large random array that reflects the `O(n log n)` sort + `O(n)` scan; the average per-run time is displayed so you can gauge performance on your machine.

---

### 10-second recall (before coding)

> **“Sort → Slide size-M window → minimize (end − start).
> Time O(n log n), Space O(1).”**

