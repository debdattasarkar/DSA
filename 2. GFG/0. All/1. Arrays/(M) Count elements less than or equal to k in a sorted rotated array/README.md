# Count elements less than or equal to **k** in a sorted rotated array

**Difficulty:** Medium
**Accuracy:** 55.71%
**Submissions:** 744+
**Points:** 4
**Average Time:** 15m

---

## Problem Statement

Given a **sorted array `arr[]` containing distinct positive integers** that has been **rotated at some unknown pivot**, and a value **x**, your task is to **count the number of elements in the array that are less than or equal to `x`**.

The solution is expected to run in **O(log n)** time.

---

## Examples

### Example 1

**Input:**

```
arr[] = [4, 5, 8, 1, 3]
x = 6
```

**Output:**

```
4
```

**Explanation:**
The elements `1, 3, 4, 5` are less than or equal to `6`.
So, the count of all elements less than `6` is **4**.

---

### Example 2

**Input:**

```
arr[] = [6, 10, 12, 15, 2, 4, 5]
x = 14
```

**Output:**

```
6
```

**Explanation:**
All elements except `15` are less than or equal to `14`.
So, the count of all elements less than `14` is **6**.

---

## Constraints

* 1 ≤ `arr.size()` ≤ 10<sup>5</sup>
* 0 ≤ `arr[i]`, `x` ≤ 10<sup>9</sup>

---

## Expected Complexities

* **Time Complexity:** `O(log n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Binary Search
* Arrays
* Algorithms

---

## Related Articles

* **Count Elements Less Equal Given Value Sorted Rotated Array**

---

---

## Intuition (what we need)

Array is **sorted + rotated**, and has **distinct** elements.
We need **count of elements ≤ x** in **O(log n)**.

Key trick:

1. **Find pivot** (index of minimum element) in `O(log n)`
2. Do **binary search (upper_bound)** in the correct sorted part(s)

Because after rotation, array becomes two sorted segments:

* `arr[pivot .. n-1]` (smallest to biggest)
* `arr[0 .. pivot-1]` (bigger tail)

---

## Step-by-step Dry Run

### Example 1

`arr = [4, 5, 8, 1, 3]`, `x = 6`

#### Step 1: Find pivot (min element index)

We binary search for smallest:

* low=0, high=4, mid=2 → arr[mid]=8, arr[high]=3
  since 8 > 3 → pivot is on right → low=3
* low=3, high=4, mid=3 → arr[mid]=1, arr[high]=3
  since 1 <= 3 → pivot is at mid or left → high=3
* low=3, high=3 → pivot = 3 (value 1)

Now segments:

* right sorted: `[1,3]` (indices 3..4)
* left sorted: `[4,5,8]` (indices 0..2)

#### Step 2: Count ≤ 6 using upper_bound in each segment

* In `[1,3]`, all ≤ 6 → count = 2
* In `[4,5,8]`, elements ≤ 6 are `[4,5]` → count = 2
  Total = 2 + 2 = **4**

✅ Answer: 4

---

### Example 2

`arr = [6,10,12,15,2,4,5]`, `x=14`

Pivot found at index 4 (value 2)
Segments:

* `[2,4,5]` and `[6,10,12,15]`

Count ≤ 14:

* `[2,4,5]` → 3
* `[6,10,12,15]` → 3 (6,10,12)
  Total = **6**

---

# Approaches

## A) Brute Force (easy, not O(log n))

**Time:** O(n)
**Space:** O(1)

```python
class Solution:
    def countLessEqual(self, arr, x):
        # Brute: scan all elements and count <= x
        count = 0
        for value in arr:
            if value <= x:
                count += 1
        return count
```

---

## B) Optimized (Most expected): Pivot + Binary Search

**Time:** O(log n)
**Space:** O(1)

Idea:

1. Find `pivot` (index of minimum)
2. Count ≤ x in the two sorted ranges using upper_bound-like binary search

### Helper: upper_bound on a subarray [l..r]

Returns index of first element `> x` within that subarray, so count is `(pos - l)`.

```python
class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0

        # ---------- Step 1: Find pivot (min element index) ----------
        # Time: O(log n), Space: O(1)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low  # smallest element index

        # ---------- Step 2: Count <= x in sorted segments ----------
        # upper_bound in [left..right] => count of <= x in that segment
        def upper_bound_in_range(left, right, target):
            if left > right:
                return 0
            lo, hi = left, right
            ans = right + 1  # default: all <= target
            while lo <= hi:
                m = (lo + hi) // 2
                if arr[m] > target:
                    ans = m
                    hi = m - 1
                else:
                    lo = m + 1
            return ans - left

        # Segment1: [pivot .. n-1]
        count_right = upper_bound_in_range(pivot, n - 1, x)
        # Segment2: [0 .. pivot-1]
        count_left = upper_bound_in_range(0, pivot - 1, x)

        return count_left + count_right
```

---

## C) Optimized Variant (shorter): Find pivot + decide one side only (sometimes)

If you want even more concise interview talk:

* If `x < min(arr)` → 0
* If `x >= max(arr)` → n
  But since max is split across rotation, you still need care; the “two segments + upper_bound” is the safest clean solution.

---

# How to remember it quickly (interview recall)

### 5-line mental template

1. **Find pivot (min index) with binary search**
2. Array becomes **two sorted parts**
3. **upper_bound** on part1 for `x`
4. **upper_bound** on part2 for `x`
5. **sum counts**

### Mnemonic

**“Pivot → Two sorted halves → UpperBound + UpperBound → Add.”**

---

# Interview Q&A (expected)

**Q1. Why can we do this in O(log n)?**
A. Rotated sorted array still has structure: we can find pivot in `O(log n)` and then binary search counts in sorted segments in `O(log n)`.

**Q2. How do you find the pivot?**
A. Use binary search comparing `arr[mid]` with `arr[high]`:

* if `arr[mid] > arr[high]`, pivot on right
* else pivot at mid or left

**Q3. Why do we need two binary searches after pivot?**
A. Rotation splits the sorted array into two sorted subarrays; to count ≤ x we can upper_bound in each independently and sum.

**Q4. What if the array was not distinct (had duplicates)?**
A. Pivot search becomes trickier; when `arr[mid] == arr[high]` you may need `high -= 1` which can degrade to O(n) in worst case.

**Q5. Edge cases?**
A.

* `n=0` → 0
* `pivot=0` (already sorted) → only one segment meaningful
* `x` very small → 0, very large → n

---

---

## 5) Real-World Use Cases (few + interviewer-relatable)

1. **Inventory / Demand thresholds (Retail)**

   * You store SKU sales counts in a “sorted-then-rotated” circular buffer (day starts at an offset).
   * Query: “How many SKUs sold **≤ x** units today?” (fast threshold count).

2. **Monitoring / Ops (SRE)**

   * Latency buckets stored in a rotated list (because logs roll over).
   * Query: “How many requests had latency **≤ x ms**?” (SLO/SLA reporting).

3. **Finance / Trading**

   * Prices in a rotated structure by session boundary (market opens at pivot).
   * Query: “How many trades happened at price **≤ x**?” (quick distribution checks).

4. **IoT / Manufacturing tolerances**

   * Sensor readings in a ring buffer (rotated due to wrap-around).
   * Query: “How many readings are **≤ x**?” to detect drift/outliers quickly.

---

## 6) Full Program (with timing + inline complexity + sample input/output)

This program implements the **expected O(log n)** solution:

* **Find pivot** (index of minimum) in `O(log n)`
* **Upper bound** in both sorted parts in `O(log n)`
* Total: `O(log n)` per call (really `~3 log n`), **Aux Space O(1)**

It supports:

* **Demo mode** (no stdin) → runs the sample from the prompt
* **Input mode** (stdin) → format:

  * `n`
  * `n integers` (arr)
  * `x`

```python
import sys
import time


class Solution:
    def countLessEqual(self, arr, x):
        """
        Count elements <= x in a sorted rotated array with distinct values.

        Steps:
        1) Find pivot (index of minimum) using binary search.
           Time: O(log n), Space: O(1)
        2) Do upper_bound (first > x) in both sorted segments and sum counts.
           Time: O(log n) + O(log n), Space: O(1)

        Total Time: O(log n)
        Aux Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0

        # ---------- Step 1: Find pivot (min element index) ----------
        # Time: O(log n), Space: O(1)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            # If mid element is greater than rightmost, min is on right side
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low  # index of smallest element

        # ---------- Step 2: upper_bound on a subarray [left..right] ----------
        # Returns count of elements <= x in that subarray
        # Time per call: O(log n), Space: O(1)
        def count_leq_in_sorted_range(left, right, target):
            if left > right:
                return 0
            lo, hi = left, right
            first_greater = right + 1  # if all <= target, stays right+1

            while lo <= hi:
                m = (lo + hi) // 2
                if arr[m] > target:
                    first_greater = m
                    hi = m - 1
                else:
                    lo = m + 1

            # elements <= target are from left to first_greater-1
            return first_greater - left

        # Two sorted segments after pivot:
        # [pivot .. n-1] and [0 .. pivot-1]
        count_right = count_leq_in_sorted_range(pivot, n - 1, x)
        count_left = count_leq_in_sorted_range(0, pivot - 1, x)

        return count_left + count_right


def main():
    # Measure total runtime for full program (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        arr = [4, 5, 8, 1, 3]
        x = 6

        result = solver.countLessEqual(arr, x)

        print("Input:")
        print("arr =", arr)
        print("x   =", x)
        print("\nOutput:")
        print(result)

    else:
        # ---------------- INPUT MODE ----------------
        # Expected stdin format:
        # n
        # n integers (arr)
        # x
        tokens = list(map(int, data.split()))
        idx = 0

        n = tokens[idx]
        idx += 1

        arr = tokens[idx:idx + n]
        idx += n

        x = tokens[idx]

        result = solver.countLessEqual(arr, x)
        print(result)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Example (Demo Mode) Output

For `arr = [4, 5, 8, 1, 3]`, `x = 6`
Output should be: `4` (since 1,3,4,5 are ≤ 6)

---
