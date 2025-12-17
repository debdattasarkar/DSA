
---

# 🧩 Overlapping Intervals

**Difficulty:** Medium
**Accuracy:** 57.41%
**Submissions:** 103K+
**Points:** 4

---

## 📝 Problem Statement

Given an array of intervals `arr[][]`, where `arr[i] = [startᵢ, endᵢ]`,
the task is to **merge all of the overlapping intervals**.

---

## 🧮 Examples

### Example 1

**Input:**

```
arr = [[1,3], [2,4], [6,8], [9,10]]
```

**Output:**

```
[[1,4], [6,8], [9,10]]
```

**Explanation:**
In the given intervals, there are only two overlapping intervals:

* `[1,3]` and `[2,4]` overlap and merge into `[1,4]`.

So the final list of merged intervals becomes `[[1,4], [6,8], [9,10]]`.

---

### Example 2

**Input:**

```
arr = [[6,8], [1,9], [2,4], [4,7]]
```

**Output:**

```
[[1,9]]
```

**Explanation:**
In this case, all the intervals overlap with `[1,9]`,
so merging all of them gives one single interval — `[1,9]`.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10⁵  
0 ≤ startᵢ ≤ endᵢ ≤ 10⁵
```

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(1)       |

---

## 🏢 Company Tags

Amazon · Microsoft · Google · Nutanix · Zoho

---

## 🧠 Topic Tags

Arrays · Hash · Sorting · Data Structures · Algorithms

---

## 🔗 Related Articles

* [Merging Intervals](https://www.geeksforgeeks.org/merging-intervals/)

---

---

Let’s go step by step and make this super interview-friendly.

---

## 2. Explanation of the logic + step-by-step dry run

### Problem in simple words

You’re given a list of intervals `arr`, where each interval is `[start, end]`.

> You must **merge all intervals that overlap** and return the resulting list of non-overlapping intervals.

Intervals **overlap** if:

```text
next_start <= current_end
```

(assuming we process them in order of increasing `start`).

### High-level approach (optimized)

1. **Sort** the intervals by `start` (and `end` if you want to be precise).
2. Keep a `current` interval (`[cur_start, cur_end]`).
3. Scan the sorted intervals from left to right:

   * If the `next` interval’s `start` is **≤** `cur_end`, they overlap → extend `cur_end = max(cur_end, next_end)`.
   * Else, they don’t overlap → push `[cur_start, cur_end]` into answer and start a new `current` interval.
4. After the loop, push the last `current` interval.

Time:

* Sorting: `O(n log n)`
* Scan/merge: `O(n)`
  → `O(n log n)` overall.

Space:

* Answer list + maybe a few variables → `O(1)` extra (if we’re allowed to modify in place).

---

### Dry run 1

Input from problem:

```text
arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
```

Step 1 – Sort by `start`:

```text
Sorted: [[1, 3], [2, 4], [6, 8], [9, 10]]
```

Step 2 – Initialize:

```text
current = [1, 3]
result = []
```

Step 3 – Process each remaining interval:

* **Next = [2, 4]**

  * next_start = 2, current_end = 3
  * 2 <= 3 → they **overlap**
  * Merge: `current_end = max(3, 4) = 4`
  * `current = [1, 4]`

* **Next = [6, 8]**

  * next_start = 6, current_end = 4
  * 6 > 4 → **no overlap**
  * Append current: `result = [[1, 4]]`
  * Start new `current = [6, 8]`

* **Next = [9, 10]**

  * next_start = 9, current_end = 8
  * 9 > 8 → **no overlap**
  * Append current: `result = [[1, 4], [6, 8]]`
  * New `current = [9, 10]`

End of loop → append last current:

```text
result = [[1, 4], [6, 8], [9, 10]]
```

Matches expected output.

---

### Dry run 2

Input from statement:

```text
arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
```

Step 1 – Sort by start:

```text
Sorted: [[1, 9], [2, 4], [4, 7], [6, 8]]
```

Step 2:

```text
current = [1, 9]
result = []
```

Step 3 – Process:

* **Next = [2, 4]**

  * 2 <= 9 → overlap
  * current_end = max(9, 4) = 9 → `current` stays `[1, 9]`
* **Next = [4, 7]**

  * 4 <= 9 → overlap
  * current_end = max(9, 7) = 9
* **Next = [6, 8]**

  * 6 <= 9 → overlap
  * current_end = max(9, 8) = 9

No non-overlap found → at the end:

```text
result = [[1, 9]]
```

Matches expected `[[1, 9]]`.

---

## 3. Python solutions (brute + optimized)

Required signature:

```python
class Solution:
    def mergeOverlap(self, arr):
        # Code here
```

We’ll give:

1. A **brute-ish** solution (sort + mark + scan) for understanding.
2. The **clean optimized** sort-and-merge solution (what you should present in interviews).

### 3.1 “Brute” idea (still sorts, but less elegant)

You could:

1. Sort intervals.
2. Use an auxiliary array to store merged output.
3. Always compare with the **last merged interval**.

(It’s basically the optimized algo, just written slightly more verbose—so I’ll jump right to the clean version, since anything truly O(n²) isn’t needed here.)

### 3.2 Optimized, clean Python solution (expected in interviews)

```python
from typing import List

class Solution:
    def mergeOverlap(self, arr: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Parameters:
            arr: List of intervals [start, end].

        Returns:
            A new list of non-overlapping intervals sorted by start,
            where any overlapping intervals have been merged.

        Overall Complexity:
            Let n = len(arr).

            - Sorting intervals: O(n log n)
            - Single pass to merge: O(n)
            => Time  : O(n log n)
            - Extra space (besides result): O(1) if we sort arr in-place,
                                            O(n) for the output list itself.
        """
        n = len(arr)
        if n == 0:
            return []

        # 1) Sort intervals by their start time.
        #    Time: O(n log n), Space: O(1) extra (in-place sort).
        arr.sort(key=lambda interval: interval[0])

        merged: List[List[int]] = []

        # 2) Initialize the current interval to the first one.
        current_start, current_end = arr[0]

        # 3) Iterate over the remaining intervals and merge overlapping ones.
        #    Single pass: O(n).
        for i in range(1, n):
            next_start, next_end = arr[i]

            if next_start <= current_end:
                # Overlap: extend the current interval's end if needed.
                # O(1) operation.
                current_end = max(current_end, next_end)
            else:
                # No overlap: push the finished current interval to result,
                # and start a new current interval.
                merged.append([current_start, current_end])
                current_start, current_end = next_start, next_end

        # 4) Append the last remaining current interval.
        merged.append([current_start, current_end])

        return merged
```

This is exactly the textbook “merge intervals” solution: sort + sweep + merge.

---

## 4. Interview: how to remember it + likely Q&A

### Tiny memory hook

Think:

> **“Sort by start, then sweep and extend until gap.”**

Or as 5-line pseudo-code you can keep in your head:

```text
sort intervals by start
current = first interval
for each next interval:
    if next.start <= current.end: current.end = max(current.end, next.end)
    else: add current to answer; current = next
add current to answer
```

If you remember that, you can rebuild the full solution in any language in under a minute.

---

### Typical interview questions & solid answers

---

**Q1. What’s the brute-force way to do this and why is it bad?**

**A:**
Brute force:

* For each interval, compare it to all others, merge overlaps, and repeat until nothing changes.
* That can be `O(n²)` or worse depending on implementation (nested loops or repeated merging).
* With up to `10^5` intervals, `O(n²)` is too slow, so we must do better.

---

**Q2. Why do you sort first?**

**A:**
Sorting by start time guarantees that:

* When we process intervals from left to right, any interval that overlaps the current one will appear **contiguously** after it.
* Once we encounter an interval whose `start > current_end`, we know that **no later interval** can overlap `current` (because starts only increase).
* This lets us merge in a single linear pass after sorting.

---

**Q3. What’s the time and space complexity of your solution?**

**A:**

* Sorting: `O(n log n)`.
* Single pass merge: `O(n)`.
* Overall time: **`O(n log n)`**.
* Extra space:

  * Sorting in-place → `O(1)` auxiliary.
  * We store merged intervals in a result list → `O(k)` where `k ≤ n`.

So auxiliary space is `O(1)` beyond the output list itself.

---

**Q4. How do you detect overlap between two intervals?**

**A:**
For intervals `[a_start, a_end]` and `[b_start, b_end]` with `a_start <= b_start` (ensured by the sort):

* They overlap iff `b_start <= a_end`.
* If so, the merged interval is `[a_start, max(a_end, b_end)]`.

If `b_start > a_end`, they don’t overlap and can’t be merged further.

---

**Q5. What edge cases do you consider?**

**A:**

* Empty list of intervals → return empty list.
* Single interval → return it as is.
* Intervals fully contained in others, e.g. `[1, 10]` and `[2, 3]` → after sort, `[1,10]` first, and we simply extend `current_end` to `max(10, 3) = 10`, so result stays `[1,10]`.
* Intervals touching at borders, e.g. `[1,3]` and `[3,5]`:

  * Problem statement usually considers `start ≤ end` and “overlap or touch” as merge condition `next_start <= current_end`. If they want strictly disjoint, we’d use `<` instead.

---

If you keep the phrase:

> **“Sort by start; sweep: overlapping → extend; gap → push & reset.”**

in your head, you’ll recall the logic and code comfortably under interview pressure.

---

---

Nice, let’s wrap this one fully.

---

## 5. Real-World Use Cases (easy to explain in interviews)

Keep a few **clear, concrete** examples in mind:

1. **Calendar / Meeting Scheduling**

   * Each meeting is an interval `[startTime, endTime]`.
   * To see when a room is busy, you merge overlapping meetings first → get a set of **non-overlapping busy blocks**.
   * Then you can easily find free slots, total busy time, etc.

2. **CPU / Resource Usage Timelines**

   * A server logs time windows where it’s under high load.
   * These windows often overlap. Merging intervals gives the total time the CPU was “hot”.
   * Same idea for network usage, disk I/O, etc.

3. **Video Editing / Subtitles / Ads**

   * Subtitle or ad intervals might overlap if multiple are scheduled around the same time.
   * Merging gives a clean list of continuous segments where something is on screen.

4. **Reservation Systems (rooms, cars, bikes)**

   * A car rental might have several bookings that touch or overlap.
   * Merging intervals is used to compute **availability** or **total booked time** without double-counting overlaps.

In an interview you can say:

> “Anytime you store time ranges or numeric ranges (bookings, CPU usage, availability), you almost always normalize them by merging overlaps—exactly what this function does.”

---

## 6. Full Python Program with Timing & Detailed Complexity Comments

This script:

* Reads number of intervals.
* Reads each interval.
* Calls `mergeOverlap` (O(n log n)).
* Prints merged intervals and total runtime.

```python
import time
from typing import List


class Solution:
    def mergeOverlap(self, arr: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        arr: List of [start, end] intervals.

        Overall complexity overview:
            Let n = len(arr).
            - Sorting intervals:  O(n log n)
            - Single scan & merge: O(n)
            => Total Time:  O(n log n)
            => Extra Space: O(1) auxiliary (besides output list),
                           because we sort in-place and keep only a few variables.
        """
        n = len(arr)

        # Edge case: no intervals or single interval
        # Time: O(1)  |  Space: O(1)
        if n <= 1:
            return arr

        # 1) Sort intervals by start time.
        #    Python's sort is Timsort, average/worst: O(n log n).
        #    Space: O(1) auxiliary (in-place).
        arr.sort(key=lambda interval: interval[0])

        merged: List[List[int]] = []

        # 2) Initialize current interval with the first interval.
        #    Time: O(1)  |  Space: O(1)
        current_start, current_end = arr[0]

        # 3) Iterate over the remaining intervals and merge if overlapping.
        #    Loop runs (n-1) times => O(n) time.
        for i in range(1, n):
            next_start, next_end = arr[i]  # O(1)

            # Case A: Overlap -> extend the current interval.
            # Overlap condition: next_start <= current_end
            if next_start <= current_end:
                # Update end with max to cover both intervals.
                # Time: O(1)
                current_end = max(current_end, next_end)
            else:
                # Case B: No overlap -> push current interval and reset.
                # Append is O(1) amortized.
                merged.append([current_start, current_end])
                # Start a new current interval.
                current_start, current_end = next_start, next_end

        # 4) Append the final current interval.
        #    Time: O(1)
        merged.append([current_start, current_end])

        # merged holds all non-overlapping, merged intervals.
        # Space used by 'merged' is O(k), where k <= n (output size).
        return merged


# --------------------------- Driver with timing --------------------------- #

def main():
    """
    Driver for local testing.

    Input format (simple):

        n
        start1 end1
        start2 end2
        ...
        startn endn

    Example input:
        4
        1 3
        2 4
        6 8
        9 10

    Example output:
        Merged intervals:
        1 4
        6 8
        9 10

        Total elapsed time (seconds): 0.0000xx
    """
    print("Enter number of intervals n:")
    first_line = input().strip()
    if not first_line:
        print("No input provided.")
        return

    n = int(first_line)

    print(f"Enter {n} intervals as 'start end' on each line:")
    intervals: List[List[int]] = []

    # Reading n lines: O(n) time, O(n) space for storing intervals.
    for _ in range(n):
        parts = input().split()
        # Basic defensive handling if user types extra columns.
        start = int(parts[0])
        end = int(parts[1])
        intervals.append([start, end])

    solver = Solution()

    # Start timing just before the algorithm.
    start_time = time.perf_counter()

    # Core algorithm: O(n log n) time, O(1) auxiliary space.
    merged = solver.mergeOverlap(intervals)

    # Stop timing right after.
    end_time = time.perf_counter()

    print("\nMerged intervals:")
    for s, e in merged:
        print(s, e)

    print(f"\nTotal elapsed time (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

### How a sample run looks (mentally)

Input:

```text
4
1 3
2 4
6 8
9 10
```

Output:

```text
Enter number of intervals n:
4
Enter 4 intervals as 'start end' on each line:
1 3
2 4
6 8
9 10

Merged intervals:
1 4
6 8
9 10

Total elapsed time (seconds): 0.0000xx
```

You can paste this into `merge_intervals.py` and run it directly.
In a coding interview / platform, you’d only submit the `Solution` class with `mergeOverlap`, but this full script is great for practicing and benchmarking.

