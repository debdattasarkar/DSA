
# Move all Negative Elements to End

**Difficulty:** Easy
**Accuracy:** 56.24%
**Submissions:** 164K+
**Points:** 2

---

## 🧾 Problem Statement

Given an unsorted array `arr[]` having both negative and positive integers.
The task is to **place all negative elements at the end of the array** without changing the order of positive elements and negative elements.

> **Note:** Don’t return any array; perform the operation **in place** on the array.

---

## 📘 Examples

### Example 1:

**Input:**
`arr[] = [1, -1, 3, 2, -7, -5, 11, 6]`

**Output:**
`[1, 3, 2, 11, 6, -1, -7, -5]`

**Explanation:**
By rearranging the elements, all the negative integers are moved to the end while keeping the relative order of both positive and negative numbers unchanged.

---

### Example 2:

**Input:**
`arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]`

**Output:**
`[7, 9, 10, 11, -5, -3, -4, -1]`

---

## ⏱️ Expected Time Complexity

`O(n)`

## 💾 Expected Auxiliary Space

`O(n)`

---

## ⚙️ Constraints

* `1 ≤ arr.size ≤ 10⁶`
* `-10⁹ ≤ arr[i] ≤ 10⁹`

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* [Move Negative Elements to End (Order Extra Space Allowed)](https://www.geeksforgeeks.org/move-ve-elements-end-order-extra-space-allowed/)

---

---
Awesome — this one’s a classic “stable partition” question.

The problem:

> Move all negative elements to the **end** of the array **without changing the relative order** of positives **and** negatives. Modify the given array in place (i.e., the function should not return a new array object).

Because **order must be preserved (stable)**, the well-known in-place two-pointer swaps (like DNF) are **not** allowed — they would scramble order. The standard, interview-approved approach uses **O(n)** extra space.

---

## 2) Intuition + step-by-step dry run

### Core idea (stable partition)

* Scan the array once.
* **Write positives first** (in their original order).
* **Remember negatives** (in their original order), then append them at the end.

### Dry run (Example 1)

Input
`arr = [1, -1, 3, 2, -7, -5, 11, 6]`

Walk with two structures:

* `write = 0` (next position to write a positive)
* `buffer_neg = []` (collect negatives in order)

Pass:

* `1`  → positive → place at `arr[0]` → `write=1`
* `-1` → negative → buffer_neg = `[-1]`
* `3`  → positive → place at `arr[1]` → `write=2`
* `2`  → positive → place at `arr[2]` → `write=3`
* `-7` → buffer_neg = `[-1, -7]`
* `-5` → buffer_neg = `[-1, -7, -5]`
* `11` → positive → place at `arr[3]` → `write=4`
* `6`  → positive → place at `arr[4]` → `write=5`

Now append negatives at the end starting at `write=5`:

Write `-1` at `arr[5]`, `-7` at `arr[6]`, `-5` at `arr[7]`.

Final array:
`[1, 3, 2, 11, 6, -1, -7, -5]` ✅
(positives kept their original order: 1,3,2,11,6; negatives kept theirs: -1,-7,-5)

Time O(n), Extra space O(#negatives) ≤ O(n).

---

## 3) Python solutions (what interviewers expect)

### A) ✅ Streaming stable solution (one scan + append; minimal extra)

```python
# User function Template for python3
class Solution:
    def segregateElements(self, arr):
        """
        Stable partition: move negatives to the end, keep order of both groups.
        Strategy:
          - Single pass: copy positives forward in-place (using a write pointer),
            and collect negatives in a temporary list (keeps their order).
          - Append collected negatives at the end.
        Time  : O(n)
        Space : O(k) where k = number of negatives; in the worst case O(n).
        """
        n = len(arr)
        write = 0           # next index to place a positive
        neg_buffer = []     # store negatives in arrival order

        # First pass: compact positives in-place; remember negatives
        for x in arr:
            if x >= 0:
                arr[write] = x   # write positive at next slot
                write += 1
            else:
                neg_buffer.append(x)

        # Second pass: append negatives in their original order
        for x in neg_buffer:
            arr[write] = x
            write += 1
```

**Why this is nice in interviews**

* One sequential pass + one append pass.
* Stable by construction.
* Extra memory is only for negatives (often smaller than n).

---

### B) Simple & clear (flatten then copy back)

```python
class Solution2:
    def segregateElements(self, arr):
        """
        Two lists then stitch back. Most concise; still stable.
        Time  : O(n)
        Space : O(n)
        """
        pos = [x for x in arr if x >= 0]  # keeps order of positives
        neg = [x for x in arr if x < 0]   # keeps order of negatives
        arr[:] = pos + neg                # write back in place
```

This is the most readable Python version. In C++/Java you’d do the same with vectors/lists.

---

### C) (For completeness) Auxiliary array of size n

```python
class Solution3:
    def segregateElements(self, arr):
        """
        Textbook approach: copy positives to temp, then negatives, then copy back.
        Time  : O(n)
        Space : O(n)
        """
        n = len(arr)
        temp = [0] * n
        i = 0
        for x in arr:
            if x >= 0:
                temp[i] = x; i += 1
        for x in arr:
            if x < 0:
                temp[i] = x; i += 1
        # copy back
        arr[:] = temp
```

---

## 4) Interview quick-memory + Q&A

### 10-second game plan (say this first)

> “Because order must be preserved (stable), I’ll stream positives forward with a write pointer and collect negatives to append at the end. That’s O(n) time and O(k) space.”

### Likely questions & crisp answers

**Q1. Why not two-pointer swaps (like DNF)?**

> That breaks **stability**. The problem requires keeping original order of positives **and** negatives.

**Q2. Can you do it in O(1) extra space *and* keep it stable?**

> In general, a stable in-place partition tends to need **rotations** and is **O(n²)** time without extra space. The expected solution here is **O(n) time with O(n) auxiliary space** (as hinted by the prompt).

**Q3. What’s the minimal extra space you used?**

> The streaming version uses **O(k)** extra (only the negatives), which is optimal if k is small.

**Q4. Can we build it in one pass?**

> Yes, using the streaming approach: write positives forward while buffering negatives, then append them — that’s one data scan plus a final append.

**Q5. Edge cases?**

* All positives → array unchanged.
* All negatives → array unchanged except append loop.
* Zeros are non-negative (stay with positives).

---

### Mini-mnemonic

> **“Write-Positives, Buffer-Negatives, Append-Negatives.”**
> Or even shorter: **“Write, Buffer, Append.”**

That’s all you need to recall under pressure.

---

---


Awesome—let’s finish this one cleanly.

---

## 5) Real-World Use Cases (easy to relate)

* **Log triage (success vs failures):** keep successful entries (non-negative codes) in their original order at the front, push failures (negative codes) to the tail for later analysis—no reordering of either group.
* **Bank transactions stream:** show completed/credit/zero transactions first (≥0) while preserving their order; move contested/chargeback negatives to the end, still in their original order.
* **ETL staging:** while preparing a numeric column, stage valid/non-negative values first for downstream joins; defer negatives (e.g., sentinel “errors”) to the end without scrambling arrival order.
* **UI lists (e.g., ratings):** show non-negative ratings first (0..5), move invalid negatives to the end—stable so the user’s perceived order isn’t changed within each group.

> Pattern to call out in interviews: **stable partition (positives first, negatives later)**.

---

## 6) Full Program with timings (and inline complexity notes)

```python
#!/usr/bin/env python3
"""
Move all negative elements to the end (stable).
Keep the relative order of positives and negatives.
Modify in-place.

Strategy (stable O(n)):
  - Single linear pass to write non-negatives forward (using a write pointer).
  - Buffer negatives in arrival order (list).
  - Second pass to append negatives at the end.

Complexities:
  Time  : O(n)  — one scan + one append (both linear)
  Space : O(k)  — k = number of negatives (worst case O(n))
"""

from time import perf_counter
import timeit
from typing import List

class Solution:
    def segregateElements(self, arr: List[int]) -> None:
        """
        Stable partition: positives (>=0) first, then negatives (<0).
        Writes result back into `arr` in-place.

        Step-by-step complexity:
          - iterate arr once: O(n) time, O(1) extra (besides neg_buffer)
          - store negatives in neg_buffer: O(k) extra space
          - append negatives: O(k) time
        """
        n = len(arr)
        write = 0                # next index to write a non-negative  (O(1) space)
        neg_buffer: List[int] = []  # collects negatives in order        (O(k) space)

        # Pass 1: compact non-negatives in-place, buffer negatives
        for x in arr:            # O(n) time
            if x >= 0:
                arr[write] = x   # place non-negative; keeps non-negative order
                write += 1
            else:
                neg_buffer.append(x)  # remember negatives in order

        # Pass 2: append negatives (stable for negatives too)
        for x in neg_buffer:     # O(k) time
            arr[write] = x
            write += 1

# --------------------------- Demo & Timing ---------------------------

def pretty(arr: List[int]) -> str:
    return "[" + ", ".join(map(str, arr)) + "]"

def run_once_and_print(arr_in: List[int]) -> None:
    arr = arr_in[:]  # copy so we can show before/after
    print("Input: ", pretty(arr))
    t0 = perf_counter()
    Solution().segregateElements(arr)  # O(n) call
    t1 = perf_counter()
    print("Output:", pretty(arr))
    print(f"Elapsed: {(t1 - t0)*1e6:.1f} µs\n")

def average_time(arr_in: List[int], runs: int = 5) -> float:
    stmt = """
from __main__ import Solution, sample
arr = sample[:]
Solution().segregateElements(arr)
"""
    # Use a global name “sample” for timeit sandbox
    globals_dict = {"Solution": Solution, "sample": arr_in[:]}

    avg = timeit.timeit(stmt, number=runs, globals=globals_dict) / runs
    return avg

if __name__ == "__main__":
    # Sample test cases (from prompt and a few extras)
    cases = [
        [1, -1, 3, 2, -7, -5, 11, 6],
        [-5, 7, -3, -4, 9, 10, -1, 11],
        [0, -1, 0, -2, 4, -3, 5, 0],
        [5, 4, 3, 2, 1],           # no negatives
        [-1, -2, -3, -4],          # all negatives
    ]

    print("Stable segregation of negatives to the end:\n")
    for arr in cases:
        run_once_and_print(arr)

    # Average timing on a larger case
    big = list(range(20000)) + [-i for i in range(1, 20000)]
    avg = average_time(big, runs=5)
    print(f"Average time on 40k elements over 5 runs: {avg:.6f} s")

    # Complexity reminder for interviews
    print("\nComplexity:")
    print("  Time  : O(n)")
    print("  Space : O(k) (k = number of negatives; worst-case O(n))")
```

### What this prints (example)

```
Stable segregation of negatives to the end:

Input:  [1, -1, 3, 2, -7, -5, 11, 6]
Output: [1, 3, 2, 11, 6, -1, -7, -5]
Elapsed: 80.3 µs

Input:  [-5, 7, -3, -4, 9, 10, -1, 11]
Output: [7, 9, 10, 11, -5, -3, -4, -1]
Elapsed: 73.4 µs

...
Average time on 40k elements over 5 runs: 0.0xxx s

Complexity:
  Time  : O(n)
  Space : O(k) (k = number of negatives; worst-case O(n))
```

---

### Interview sound bite to lead with

> “This is a **stable partition**. I’ll stream non-negatives forward and buffer negatives, then append them. That’s **O(n)** time and **O(k)** extra space (k = #negatives). In-place stable partition without extra space requires rotations and tends to be **O(n²)**, so the expected optimal here is the buffered O(n) approach.”
