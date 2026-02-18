
---

# 🔥 Maximum Number of Overlapping Intervals

**Difficulty:** Hard
**Accuracy:** 49.41%
**Submissions:** 16K+
**Points:** 8

---

## 📝 Problem Statement

You are given an array of intervals `arr[][]`, where each interval is represented by two integers `[start, end]` (**inclusive**).

Return the **maximum number of intervals that overlap at any point in time**.

---

## 📚 Examples

### Example 1

```
Input:  arr[][] = [[1, 2], [2, 4], [3, 6]]
Output: 2
```

**Explanation:**
The maximum overlapping intervals are 2

* (between (1, 2) and (2, 4))
* or between (2, 4) and (3, 6))

(Overlapping of two intervals illustrated in timeline diagram.)

---

### Example 2

```
Input:  arr[][] = [[1, 8], [2, 5], [5, 6], [3, 7]]
Output: 4
```

**Explanation:**
The maximum overlapping intervals are 4
(between (1, 8), (2, 5), (5, 6) and (3, 7))

---

## 🔒 Constraints

* `2 ≤ arr.size() ≤ 2 * 10^4`
* `1 ≤ arr[i][0] < arr[i][1] ≤ 4 * 10^6`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## 🏷 Topic Tags

* prefix-sum
* Sorting
* Arrays
* Data Structures
* Hash

---

## 📖 Related Articles

* Maximum Number Of Overlapping Intervals

---

---

## 2) Explanation (Core Idea)

We need the **maximum number of intervals overlapping at any single time**.

Because intervals are **inclusive** (`[start, end]` includes both ends), the tricky part is:

* If one interval ends at time `t` and another starts at time `t`, they **DO overlap** at time `t`.

So we should treat:

* **start at `t`** as `+1`
* **end at `t`** as `-1` but only **after `t`** (i.e., at `t+1`) to preserve inclusivity.

This naturally leads to a **sweep-line / prefix sum (difference array)** approach.

---

## Step-by-step Dry Run

### Example 1

`arr = [[1,2], [2,4], [3,6]]` (inclusive)

Create events using **diff**:

* For `[s,e]`: `diff[s] += 1`, `diff[e+1] -= 1`

Events:

* [1,2] → `+1 at 1`, `-1 at 3`
* [2,4] → `+1 at 2`, `-1 at 5`
* [3,6] → `+1 at 3`, `-1 at 7`

Now accumulate in time order:

| time | diff change | active overlaps |
| ---- | ----------: | --------------: |
| 1    |          +1 |               1 |
| 2    |          +1 |     2 ✅ (max=2) |
| 3    |   -1 +1 = 0 |             2 ✅ |
| 4    |           0 |               2 |
| 5    |          -1 |               1 |
| 7    |          -1 |               0 |

Answer = **2**

---

### Example 2

`arr = [[1,8], [2,5], [5,6], [3,7]]`

Events:

* [1,8] → +1 at 1, -1 at 9
* [2,5] → +1 at 2, -1 at 6
* [5,6] → +1 at 5, -1 at 7
* [3,7] → +1 at 3, -1 at 8

Accumulate (key times):

* time 1: active=1
* time 2: active=2
* time 3: active=3
* time 5: active=4 ✅ max=4
  So answer = **4**

---

## 3) Python Codes (Brute + Interview-Expected Optimized)

### A) Brute Force (easy baseline)

Check overlap count at each interval’s start point (or all endpoints).
**Time:** `O(n^2)`
**Space:** `O(1)`

```python
class Solution:
    def overlapInt(self, arr):
        # Brute force: for each interval start, count how many intervals cover it.
        # Inclusive overlap: [s,e] covers time t if s <= t <= e.
        # Time: O(n^2), Space: O(1)
        
        n = len(arr)
        max_overlap = 0

        for i in range(n):
            check_time = arr[i][0]  # pick a candidate time
            current_overlap = 0

            for j in range(n):
                start, end = arr[j]
                if start <= check_time <= end:
                    current_overlap += 1

            max_overlap = max(max_overlap, current_overlap)

        return max_overlap
```

---

### B) Interview-Expected (Sweep line with events) ✅

Works perfectly with **inclusive** endpoints by processing **start before end** at same time.
We can do this by creating events:

* `(start, +1)`
* `(end, -1)` but ensure **start processed first** when times equal:

  * Sort by `(time, type)` where `+1` comes before `-1`

**Time:** `O(n log n)`
**Space:** `O(n)`

```python
class Solution:
    def overlapInt(self, arr):
        # Sweep line using events.
        # Inclusive intervals: if one ends at t and another starts at t -> they overlap.
        # So for same time, process START (+1) before END (-1).
        #
        # Time: O(n log n) due to sorting events
        # Space: O(n) for events list

        events = []

        for start, end in arr:
            events.append((start, +1))  # meeting starts -> add one active interval
            events.append((end, -1))    # meeting ends -> remove one (after counting at end time)

        # Sort by time; for tie: start(+1) should come before end(-1)
        # We can enforce this by sorting by (time, -delta) because +1 should be earlier than -1
        events.sort(key=lambda x: (x[0], -x[1]))

        active_intervals = 0
        max_overlap = 0

        for time, delta in events:
            active_intervals += delta
            max_overlap = max(max_overlap, active_intervals)

        return max_overlap
```

---

### C) Prefix-sum / Difference Map (handles inclusive with end+1) ✅

This is very clean and intuitive for inclusive intervals:

* `diff[start] += 1`
* `diff[end+1] -= 1`

**Time:** `O(n log n)` (sorting unique keys)
**Space:** `O(n)`

```python
class Solution:
    def overlapInt(self, arr):
        # Difference map + prefix sum.
        # For inclusive [s,e]: add +1 at s, remove at e+1.
        #
        # Time: O(n log n) (sort unique times)
        # Space: O(n)

        diff = {}

        for start, end in arr:
            diff[start] = diff.get(start, 0) + 1
            diff[end + 1] = diff.get(end + 1, 0) - 1

        active_intervals = 0
        max_overlap = 0

        for time in sorted(diff.keys()):
            active_intervals += diff[time]
            max_overlap = max(max_overlap, active_intervals)

        return max_overlap
```

> Note: The problem screenshot says expected `O(n)` time, which is achievable only if times are small enough for direct array prefix (not here since end ≤ 4e6, still maybe feasible with array but memory heavy in Python). Interviewers usually accept `O(n log n)` sweep-line.

---

## 4) Quick Interview Recall + Expected Q&A

### 10-second Mnemonic

**“E+A: Events → Accumulate”**
or
**“Sort points, walk line, track active”**

### 5-line skeleton (rebuild in any language)

```text
events = []
for each [s,e]: add (s,+1), add (e,-1)
sort events by (time, start before end)
active = 0, best = 0
for each event: active += delta, best = max(best, active)
return best
```

---

## Interview Q&A (common)

**Q1. Why sorting events works?**
A1. As we sweep time from left to right, `active` equals how many intervals are currently covering that time. The max of `active` over the sweep is the answer.

**Q2. Inclusive endpoints: what changes?**
A2. If an interval ends at time `t` and another starts at time `t`, they overlap at `t`. So at the same timestamp, we must process **start before end**, or use the `end+1` trick in a diff map.

**Q3. What is the overlap condition conceptually?**
A3. Overlap count at any time = (#starts up to time) − (#ends before time). Sweep-line maintains this dynamically.

**Q4. Complexity?**
A4. Building events is `O(n)`, sorting is `O(n log n)`, scan is `O(n)`. Space `O(n)`.

**Q5. Can this be O(n)?**
A5. Only if time values are bounded small enough to use a direct array difference/prefix without sorting (counting sort style). With large coordinates, sorting is needed.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Conference room / resource utilization peak**

* Find the **maximum number of rooms needed** at any time to avoid double-booking.

2. **Server/GPU capacity planning**

* Jobs have start–end runtimes; max overlap = **peak concurrent jobs** → how many GPUs/instances you must provision.

3. **Customer support / call center staffing**

* Each ticket/call session occupies an agent for a time window; max overlap = **minimum agents required** at peak time.

4. **Network bandwidth / streaming sessions**

* Sessions overlap in time; max overlap estimates **peak concurrent streams**, helping with bandwidth allocation.

---

## 6) Full Python Program (timed end-to-end + sample I/O)

* Uses **Sweep Line with Events** (interview-expected)
* Correct for **inclusive** intervals by processing **start before end** when time ties.
* Competitive style input using `input()`

### ✅ Input Format (for this program)

```
t
n
s1 e1
s2 e2
...
sn en
(repeat for t test cases)
```

### ✅ Sample Input

```
2
3
1 2
2 4
3 6
4
1 8
2 5
5 6
3 7
```

### ✅ Sample Output

```
2
4
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time

class Solution:
    def overlapInt(self, arr):
        """
        Return maximum number of overlapping intervals at any point in time.
        Intervals are inclusive: [start, end].

        Approach (Interview-Expected): Sweep Line with Events
        - Convert each interval to two events: (start, +1), (end, -1)
        - For inclusive intervals, if start == end_time of another interval,
          they overlap at that time. So at same time, process START before END.

        Time Complexity:
          - Build events: O(n)
          - Sort events: O(n log n)
          - Sweep scan: O(n)
          => Total: O(n log n)

        Auxiliary Space:
          - Events list: O(n)
        """

        # Edge case
        # Time: O(1), Space: O(1)
        if not arr:
            return 0

        # Step 1: Build events
        # Time: O(n), Space: O(n)
        events = []
        for start_time, end_time in arr:
            events.append((start_time, +1))  # interval starts -> +1 active
            events.append((end_time, -1))    # interval ends   -> -1 active (after counting overlap at end)

        # Step 2: Sort events
        # Time: O(n log n)
        # Tie-break rule for inclusivity:
        #   same time => start(+1) should come before end(-1)
        # Using key (time, -delta): +1 becomes -1, -1 becomes +1 => +1 comes first.
        events.sort(key=lambda x: (x[0], -x[1]))

        # Step 3: Sweep and compute maximum active intervals
        # Time: O(n), Space: O(1)
        active_intervals = 0
        max_overlap = 0

        for time_point, delta in events:
            active_intervals += delta
            if active_intervals > max_overlap:
                max_overlap = active_intervals

        return max_overlap


def main():
    # Measure total program runtime (includes I/O + solving)
    program_start = time.perf_counter()  # Time: O(1)

    t = int(input().strip())  # Time: O(1)
    solver = Solution()

    # Process each test case
    # Total across tests: sum of O(n log n)
    for _ in range(t):
        n = int(input().strip())  # Time: O(1)

        # Read intervals
        # Time: O(n), Space: O(n)
        intervals = []
        for _ in range(n):
            start_time, end_time = map(int, input().split())
            intervals.append([start_time, end_time])

        # Compute answer
        # Time: O(n log n)
        result = solver.overlapInt(intervals)

        # Output per test case
        print(result)

    program_end = time.perf_counter()
    print(f"Total runtime (seconds): {program_end - program_start:.8f}")


if __name__ == "__main__":
    main()
```

