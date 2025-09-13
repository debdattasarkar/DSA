# Minimum Platforms

**Difficulty:** Medium
**Accuracy:** 26.84%
**Submissions:** 561K+
**Points:** 4

---

## Problem Statement

You are given the arrival times `arr[]` and departure times `dep[]` of all trains that arrive at a railway station on the same day. Your task is to determine the **minimum number of platforms** required at the station to ensure that **no train is kept waiting**.

At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. Therefore, when two trains arrive at the same time, or when one arrives before another departs, **additional platforms** are required to accommodate both trains.

---

## Examples

### Example 1

**Input:** `arr[] = [900, 940, 950, 1100, 1500, 1800]`, `dep[] = [910, 1200, 1120, 1130, 1900, 2000]`
**Output:** `3`
**Explanation:** There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.

### Example 2

**Input:** `arr[] = [900, 1235, 1100]`, `dep[] = [1000, 1240, 1200]`
**Output:** `1`
**Explanation:** All train times are mutually exclusive. So we need only one platform.

### Example 3

**Input:** `arr[] = [1000, 935, 1100]`, `dep[] = [1200, 1240, 1130]`
**Output:** `3`
**Explanation:** All 3 trains have to be there from 11:00 to 11:30.

---

## Constraints

* `1 ≤ number of trains ≤ 50000`
* `0000 ≤ arr[i] ≤ dep[i] ≤ 2359`

**Note:** Time intervals are in the **24-hour format (HHMM)**, where the first two characters represent hours (between 00 to 23) and the last two characters represent minutes (this will be ≤ 59 and ≥ 0).

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Paytm • Amazon • Microsoft • D-E-Shaw • Hike • Walmart • Adobe • Google • Boomerang Commerce • Zillious • Atlassian

---

## Topic Tags

Arrays • Greedy • Sorting • Binary Search • Data Structures • Algorithms

---

## Related Interview Experiences

* Walmart Labs Interview Experience Set 2 On Campus
* Walmart Labs Interview Experience Set 3 On Campus
* Adobe Interview Experience For Member Of Technical Staff 2
* Adobe Interview Experience On Campus For Internship
* Adobe Interview Questions Computer Scientist
* Atlassian Interview Experience For Full Time Software Engineer Bangalore On Campus

---

## Related Articles

* Minimum Number Platforms Required Railwaybus Station Set 2 Map Based Approach
* Minimum Number Platforms Required Railwaybus Station

---

---

Here’s a crisp, interview-ready guide to **Minimum Platforms**.

---

## 2) Intuition + Step-by-step dry run

### What are we minimizing?

At any instant, the number of **simultaneously present** trains at the station. That number is exactly the **minimum platforms** needed so that none waits.

### Classic observation

* You only care about **event order** (arrivals vs departures).
* If an arrival happens **before or at** a departure (same minute counts as overlap), you need a **new platform**.
* If a departure happens **before** the next arrival, you can **free** a platform.

This gives the well-known **two-sorted-arrays / two-pointers** solution.

### Dry run on Example 1

```
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910,1200,1120, 1130, 1900, 2000]
Sort each (already sorted here)

i = 0 (arrival idx), j = 0 (departure idx)
curr = 0 (current platforms), maxp = 0

1) arr[0]=900 <= dep[0]=910  -> arrival first
   curr = 1, maxp = 1, i=1

2) arr[1]=940 <= dep[0]=910  -> NO (arrival after dep)  departure first
   curr = 0, j=1

3) arr[1]=940 <= dep[1]=1200 -> arrival first
   curr = 1, maxp = 1, i=2

4) arr[2]=950 <= dep[1]=1200 -> arrival first
   curr = 2, maxp = 2, i=3

5) arr[3]=1100 <= dep[1]=1200 -> arrival first
   curr = 3, maxp = 3, i=4

6) arr[4]=1500 <= dep[1]=1200 -> NO  departure
   curr = 2, j=2

7) arr[4]=1500 <= dep[2]=1120 -> NO  departure
   curr = 1, j=3

8) arr[4]=1500 <= dep[3]=1130 -> NO  departure
   curr = 0, j=4

9) arr[4]=1500 <= dep[4]=1900 -> arrival
   curr = 1, maxp = 3, i=5

10) arr[5]=1800 <= dep[4]=1900 -> arrival
    curr = 2, maxp = 3, i=6 (done arrivals)

Answer = maxp = 3
```

Key tie-break rule: **arrival at time T needs a free platform if the earliest departure is also at T** → treat **arr\[i] <= dep\[j]** as “arrival uses a platform”.

---

## 3) Python solutions (brute & optimal), with interview-style comments

### A) Optimal – Two-pointers on sorted arrival/departure (O(n log n) time, O(1) extra)

```python
class Solution:    
    def minPlatform(self, arr, dep):
        """
        Two-pointer sweep after sorting arrival and departure times.

        Time:  O(n log n) for sorting
        Space: O(1) extra (if we can sort in place)  [ignoring sort's stack]
        """
        n = len(arr)
        if n == 0:
            return 0

        arr.sort()  # O(n log n)
        dep.sort()  # O(n log n)

        i = j = 0          # i -> next arrival, j -> next departure
        curr = maxp = 0

        # Traverse both lists
        while i < n and j < n:             # O(n)
            if arr[i] <= dep[j]:
                # Arrival needs a platform (<= handles same-time overlap)
                curr += 1
                maxp = max(maxp, curr)
                i += 1
            else:
                # Earliest departure frees a platform
                curr -= 1
                j += 1

        return maxp
```

### B) Also optimal – Event sweep (same complexity; sometimes easier to reason about)

Turn each time into an “event”: `(time, +1)` for arrival, `(time, -1)` for departure.
Important tie-break: **arrivals first** at equal time.

```python
class SolutionEvents:
    def minPlatform(self, arr, dep):
        """
        Sweep-line over combined events.

        Time:  O(n log n) (sort 2n events)
        Space: O(n) to store events
        """
        events = []
        for t in arr:
            events.append((t,  1))  # arrival adds a platform
        for t in dep:
            events.append((t, -1))  # departure frees a platform

        # Sort by time; for same time, arrivals (+1) must come before departures (-1)
        # so reverse the second key (put +1 first). One way: sort by (time, -type)
        events.sort(key=lambda e: (e[0], -e[1]))

        curr = maxp = 0
        for _, delta in events:
            curr += delta
            maxp = max(maxp, curr)
        return maxp
```

### C) Brute force (for completeness) – Check overlaps per train (O(n²))

Count how many trains overlap each arrival time; take the maximum.

```python
class SolutionBrute:
    def minPlatform(self, arr, dep):
        """
        Quadratic check: for each train, count overlapping trains.
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        ans = 0
        for i in range(n):
            curr = 1  # train i is present
            for j in range(i + 1, n):
                # overlap if one starts before the other ends (with equality as overlap)
                if not (dep[i] < arr[j] or dep[j] < arr[i]):
                    curr += 1
            ans = max(ans, curr)
        return ans
```

---

## 4) Common Interview Q\&A

**Q1. Why do we use `arr[i] <= dep[j]` (and not `<`) in the two-pointer method?**
Because a train **arriving at the same minute** another departs **cannot reuse** that platform in this problem statement. Using `<=` forces allocating a new platform for ties.

**Q2. What’s the complexity and why?**
Sorting the two lists dominates: **O(n log n)** time, **O(1)** extra space aside from sort. The sweep itself is linear.

**Q3. Do we need to convert `HHMM` to minutes?**
You can sort `HHMM` as integers directly since their numeric ordering matches time ordering. Converting to minutes is fine too and can help if you later do arithmetic (e.g., add durations).

**Q4. What if arrivals can be after midnight (wrap to next day)?**
Then `HHMM` as integers is insufficient (00:10 is “less” than 23:50). You’d need timestamps with dates or normalize by adding 24h to “wrapped” times.

**Q5. Can we do it in O(n) without sorting?**
Only if time is **bounded and small** (e.g., minutes in a day); then you can use counting/bucketing. With general times, sorting is needed.

**Q6. How do you prove correctness of the two-pointer sweep?**
You process the **chronological order of events**; maintaining the running number of trains present is exactly the number of platforms in use. The maximum over time is the minimum number needed.

**Q7. Alternative with a min-heap?**
Yes: sort by arrival; keep a min-heap of departure times (platforms in use). Pop while the earliest departure < current arrival; push current departure; track heap size. It’s also **O(n log n)**.

---

---

Here’s a complete, runnable Python script that solves **Minimum Platforms** using the optimal **two-pointer sweep after sorting**. It includes:

* Inline comments that state the **time & space complexity** of each step
* A couple of sample inputs (from the prompt) with **printed outputs**
* **Timing** of each call and the **total program time** using `timeit`

```python
from typing import List
import timeit
import random

class Solution:    
    def minPlatform(self, arr: List[int], dep: List[int]) -> int:
        """
        Compute minimum number of platforms so that no train waits.

        Algorithm: sort both arrival and departure arrays and sweep
        with two pointers:
          - If next arrival <= next departure -> need one more platform (curr++)
          - Else a train leaves -> free one platform (curr--)

        Time complexity:
          - Sorting arrivals:  O(n log n)
          - Sorting departures: O(n log n)
          - Linear sweep:       O(n)
          => Overall:           O(n log n)

        Space complexity:
          - O(1) extra (if sorting in place; Python's list sort uses Timsort, which is in-place)
        """
        n = len(arr)                       # O(1)
        if n == 0:                         # O(1)
            return 0

        arr.sort()                         # O(n log n) time, O(1) extra (in-place)
        dep.sort()                         # O(n log n) time, O(1) extra (in-place)

        i = j = 0                          # O(1) pointers: i->arrival index, j->departure index
        curr = maxp = 0                    # O(1) current platforms and maximum seen

        # Sweep both arrays once: O(n)
        while i < n and j < n:
            # Treat arrival at the same minute as a needed platform (<=)
            if arr[i] <= dep[j]:           # O(1) comparison
                curr += 1                  # O(1) allocate platform
                if curr > maxp:            # O(1)
                    maxp = curr            # O(1) update maximum
                i += 1                     # O(1) advance arrival
            else:
                curr -= 1                  # O(1) free a platform (departure)
                j += 1                     # O(1) advance departure
        return maxp                        # O(1)


# ---------------------- Demo / Timing Harness ---------------------- #
def run_case(name: str, arr: List[int], dep: List[int], solver: Solution) -> None:
    """Run one case, print answer and time. O(n log n) due to sorting."""
    arr_copy = arr[:]                      # O(n) copy so original is preserved for fairness
    dep_copy = dep[:]                      # O(n) copy
    t0 = timeit.default_timer()
    ans = solver.minPlatform(arr_copy, dep_copy)
    t1 = timeit.default_timer()
    print(f"{name}:")
    print(f"  arr = {arr}")
    print(f"  dep = {dep}")
    print(f"  min platforms = {ans}")
    print(f"  elapsed = {(t1 - t0):.6f}s\n")


def main():
    solver = Solution()

    print("=== Minimum Platforms — Examples & Timing ===\n")

    # Example 1 (expected 3)
    arr1 = [900, 940, 950, 1100, 1500, 1800]
    dep1 = [910, 1200, 1120, 1130, 1900, 2000]
    run_case("Example 1 (expect 3)", arr1, dep1, solver)

    # Example 2 (expected 1)
    arr2 = [900, 1235, 1100]
    dep2 = [1000, 1240, 1200]
    run_case("Example 2 (expect 1)", arr2, dep2, solver)

    # Example 3 (expected 3)
    arr3 = [1000, 935, 1100]
    dep3 = [1200, 1240, 1130]
    run_case("Example 3 (expect 3)", arr3, dep3, solver)

    # Optional: a larger random test to show O(n log n) scaling
    n = 50_000
    random.seed(0)
    # Generate valid (arr, dep) pairs in HHMM-like integers within the range [0, 2359]
    # Ensure arr_i <= dep_i
    big_arr = []
    big_dep = []
    for _ in range(n):
        a = random.randint(0, 2359)
        d = random.randint(a, 2359)
        big_arr.append(a)
        big_dep.append(d)

    t0 = timeit.default_timer()
    _ = solver.minPlatform(big_arr[:], big_dep[:])   # copy to avoid in-place sort side effects
    t1 = timeit.default_timer()
    print(f"Large test n={n}: elapsed = {(t1 - t0):.6f}s (O(n log n) expected)\n")


if __name__ == "__main__":
    total_start = timeit.default_timer()
    main()
    total_end = timeit.default_timer()
    print("==== TOTAL PROGRAM TIME ====")
    print(f"{(total_end - total_start):.6f}s")
```

---

## 6) Real-World Use Cases (a few vital ones)

* **Airport gate allocation:** Exactly the same as platforms—gates must handle overlapping arrivals/departures of flights.
* **Meeting room scheduling:** Minimum number of rooms needed so that no meetings collide; identical sweep logic.
* **Thread pool / resource slots:** Minimum number of identical resources to serve overlapping jobs (start/end times), ensuring no job waits.
* **Parking lot design:** Minimum number of spots to accommodate overlapping car arrivals/departures within a time window.
