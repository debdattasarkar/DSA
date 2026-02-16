
---

# 🏢 Meeting Rooms

**Difficulty:** Easy
**Accuracy:** 65.12%
**Submissions:** 34K+
**Points:** 2

---

## 📝 Problem Statement

Given a 2D array `arr[][]`, where:

* `arr[i][0]` is the **starting time** of the *i<sup>th</sup>* meeting
* `arr[i][1]` is the **ending time** of the *i<sup>th</sup>* meeting

The task is to check if it is possible for a person to attend **all the meetings** such that he can attend **only one meeting at a particular time**.

---

## 📌 Note

A person can attend a meeting **if its starting time is greater than or equal to the previous meeting's ending time**.

---

## 📚 Examples

### Example 1

```
Input:  arr[][] = [[1, 4], [10, 15], [7, 10]]
Output: true
```

**Explanation:**
Since all the meetings are held at different times, it is possible to attend all the meetings.

---

### Example 2

```
Input:  arr[][] = [[2, 4], [9, 12], [6, 10]]
Output: false
```

**Explanation:**
Since the second and third meeting overlap, a person cannot attend all the meetings.

---

## 🔒 Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 2 * 10^6`

---

## ⏱ Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## 🏷 Company Tags

* NPCI

---

## 🧩 Topic Tags

* Sorting
* Greedy
* Arrays

---

## 📖 Related Articles

* Meeting Rooms Check If A Person Can Attend All Meetings

---

---

## 2) Explanation (Idea)

You can attend **all** meetings only if **no two meetings overlap**.

**Key observation:**
If we sort meetings by **start time**, then we only need to check **adjacent meetings**:

* After sorting, if `current_start < previous_end` ⇒ **overlap** ⇒ answer **False**
* Otherwise continue. If no overlaps found ⇒ **True**

Why adjacent-only works:
Once sorted by start time, any overlap must happen with the immediately previous meeting (because it’s the one that ends closest before the current starts).

---

## Step-by-step Dry Run

### Example 1

`arr = [[1,4],[10,15],[7,10]]`

1. Sort by start time → `[[1,4],[7,10],[10,15]]`
2. Compare:

   * prev = `[1,4]`, curr = `[7,10]`

     * `7 >= 4` ✅ no overlap → update prev_end = 10
   * prev_end = 10, curr = `[10,15]`

     * `10 >= 10` ✅ allowed (equal is fine)
3. No overlaps → **True**

---

### Example 2

`arr = [[2,4],[9,12],[6,10]]`

1. Sort → `[[2,4],[6,10],[9,12]]`
2. Compare:

   * prev_end = 4, curr `[6,10]` → `6 >= 4` ✅
   * prev_end = 10, curr `[9,12]` → `9 < 10` ❌ overlap found
3. Return **False**

---

## 3) Python Codes (Brute + Interview-Optimized)

### A) Brute Force (Check every pair) — Easy to explain

**Time:** `O(n^2)` (too slow for `1e5`, but good for correctness baseline)
**Space:** `O(1)`

```python
class Solution:
    def canAttend(self, arr):
        # Brute force: check all pairs for overlap
        # Time: O(n^2), Space: O(1)
        n = len(arr)

        for i in range(n):
            start1, end1 = arr[i]
            for j in range(i + 1, n):
                start2, end2 = arr[j]

                # Two intervals overlap if they intersect in time
                # Non-overlap condition: end1 <= start2 OR end2 <= start1
                # So overlap occurs when NOT(non-overlap):
                if not (end1 <= start2 or end2 <= start1):
                    return False

        return True
```

---

### B) Optimized (Most Expected in Interviews) — Sort + single pass

**Time:** `O(n log n)` due to sorting
**Space:** `O(1)` auxiliary (sorting may use extra memory depending on language/runtime)

```python
class Solution:
    def canAttend(self, arr):
        # Sort by start time, then check adjacent meetings
        # Time: O(n log n), Space: O(1) auxiliary (ignoring sort internals)
        arr.sort(key=lambda interval: interval[0])

        # Track the end time of the last meeting we attended
        previous_end_time = arr[0][1]

        for i in range(1, len(arr)):
            current_start_time, current_end_time = arr[i]

            # Overlap condition
            if current_start_time < previous_end_time:
                return False

            # Update the end time boundary
            previous_end_time = current_end_time

        return True
```

---

### C) Optimized Variant (No sorting of pairs) — Sort starts and ends separately

This is a popular variant:
If the **next start** is earlier than the **current end**, overlap exists.

**Time:** `O(n log n)`
**Space:** `O(n)` (extra arrays)

```python
class Solution:
    def canAttend(self, arr):
        # Variant: separate start/end arrays
        # Time: O(n log n), Space: O(n)
        starts = sorted(interval[0] for interval in arr)
        ends = sorted(interval[1] for interval in arr)

        # After sorting, check if any next start is before current end
        for i in range(1, len(arr)):
            if starts[i] < ends[i - 1]:
                return False
        return True
```

---

## 4) Interview Memory + Expected Q&A

### 10-second Recall Mnemonic

**“Sort then Scan”**

1. Sort by start
2. Keep `prevEnd`
3. If `start < prevEnd` ⇒ overlap ⇒ False
4. Else update `prevEnd`

### 5-line pseudo-code template (memorize)

```
sort intervals by start
prevEnd = first.end
for each (s,e) from second:
    if s < prevEnd: return false
    prevEnd = e
return true
```

---

## Common Interview Questions & Answers

**Q1. Why do we sort by start time?**
A1. Sorting ensures meetings are in chronological order; then only adjacent meetings can overlap, so we can detect conflicts in one linear pass.

**Q2. What is the overlap condition exactly?**
A2. After sorting: if `current_start < previous_end`, meetings overlap.
Equality (`current_start == previous_end`) is allowed by the problem.

**Q3. Complexity? Why is this optimal?**
A3. Sorting costs `O(n log n)` and scanning is `O(n)`. With arbitrary intervals, sorting (or equivalent ordering) is necessary to reliably detect overlaps.

**Q4. Can we do it in O(n) time?**
A4. Only if time range is small enough to use counting/bucketing or if meetings are already sorted by start time. Otherwise, comparison-based lower bound implies `O(n log n)`.

**Q5. What edge cases should we handle?**
A5.

* `n = 0 or 1` ⇒ always true
* same start times: `[1,3]` and `[1,2]` ⇒ overlap
* touching intervals: `[1,2]` and `[2,3]` ⇒ allowed
* unsorted input ⇒ must sort first

---

---

## 5) Real-World Use Cases (interviewer-relatable)

1. **Calendar scheduling / meeting planner**
   Before accepting a new meeting invite, check if it conflicts with existing meetings.

2. **Room / resource booking** (conference room, MRI machine, lab equipment)
   Ensure a single room/resource isn’t double-booked during overlapping time windows.

3. **CPU/GPU job scheduling (single machine / single GPU)**
   If only one job can run at a time, validate that scheduled jobs don’t overlap.

4. **Interview slot management / appointment booking** (doctor, salon, customer support)
   Confirm a person/agent can attend all booked appointments sequentially without collisions.

---

## 6) Full Program (with timing + sample I/O)

* Uses the **interview-expected** solution: **sort + scan**
* Prints **True/False**
* Prints **runtime** for the whole program
* Competitive style: reads from `input()` (supports multiple test cases)

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

### ✅ Example Input

```
2
3
1 4
10 15
7 10
3
2 4
9 12
6 10
```

### ✅ Example Output

```
true
false
Total runtime (seconds): 0.0000xxxx
```

---

```python
import time

class Solution:
    def canAttend(self, arr):
        """
        Check if all meetings can be attended without overlap.

        Approach: Sort by start time, then scan adjacent intervals.
        Time Complexity:
            - Sorting: O(n log n)
            - Single pass check: O(n)
            => Total: O(n log n)
        Auxiliary Space Complexity:
            - O(1) extra (ignoring Python sort internal memory)
        """

        # If 0 or 1 meeting, always possible
        # Time: O(1), Space: O(1)
        if len(arr) <= 1:
            return True

        # Sort meetings by start time
        # Time: O(n log n), Space: O(1) aux (practically Python uses extra internally)
        arr.sort(key=lambda interval: interval[0])

        # Track end time of previous meeting
        # Time: O(1), Space: O(1)
        previous_end_time = arr[0][1]

        # Scan remaining meetings and detect overlap
        # Time: O(n), Space: O(1)
        for i in range(1, len(arr)):
            current_start_time, current_end_time = arr[i]

            # Overlap if current starts before previous ends
            # Time: O(1)
            if current_start_time < previous_end_time:
                return False

            # Update boundary
            previous_end_time = current_end_time

        return True


def main():
    start_time = time.perf_counter()  # Start total timing (high-resolution)

    # Read number of test cases
    # Time: O(1)
    t = int(input().strip())

    solver = Solution()

    # Process each test case
    # Total Time across all test cases: sum(O(n log n))
    for _ in range(t):
        n = int(input().strip())

        # Read meetings
        # Time: O(n), Space: O(n) to store input intervals
        meetings = []
        for _ in range(n):
            s, e = map(int, input().split())
            meetings.append([s, e])

        # Solve
        # Time: O(n log n)
        ans = solver.canAttend(meetings)

        # Print in the same style as examples: true/false
        print("true" if ans else "false")

    end_time = time.perf_counter()
    print(f"Total runtime (seconds): {end_time - start_time:.8f}")


if __name__ == "__main__":
    main()
```

---

---

