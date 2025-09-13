# Move all negative elements to end

**Difficulty:** Easy
**Accuracy:** 56.24%
**Submissions:** 164K+
**Points:** 2

---

## Problem Statement

Given an unsorted array `arr[]` having both negative and positive integers. The task is to place all negative elements at the end of the array **without changing the order of positive elements and negative elements**.

> **Note:** Don’t return any array, just do it **in-place** on the array.

---

## Examples

### Example 1

**Input:** `arr[] = [1, -1, 3, 2, -7, -5, 11, 6]`
**Output:** `[1, 3, 2, 11, 6, -1, -7, -5]`
**Explanation:** By doing operations we separated the integers without changing the order.

### Example 2

**Input:** `arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]`
**Output:** `[7, 9, 10, 11, -5, -3, -4, -1]`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Constraints

* `1 ≤ arr.size ≤ 10^6`
* `-10^9 ≤ arr[i] ≤ 10^9`

---

## Topic Tags

* `Arrays` • `Data Structures`

---

## Related Articles

* [Move Ve Elements End Order Extra Space Allowed](https://www.geeksforgeeks.org/move-ve-elements-end-order-extra-space-allowed/)


---

---

Here’s a crisp, interview-style walkthrough for **Move all negative elements to end** (stable order preserved).

---

## 2) Intuition + step-by-step dry run

Goal: put all **positives (and zeros)** first (in original order), then all **negatives** (in original order). That’s a **stable partition**.

### Easiest correct idea (meets expected bounds)

* Make a temporary list.
* First append every `x >= 0` in order.
* Then append every `x < 0` in order.
* Copy the temp back into the original array (the driver expects in-place modification).

This is **O(n)** time and **O(n)** extra space — exactly what the prompt/expected complexity allows.

### Dry run

`arr = [1, -1, 3, 2, -7, -5, 11, 6]`

1. Scan for non-negatives → `pos = [1, 3, 2, 11, 6]`
2. Scan for negatives → `neg = [-1, -7, -5]`
3. Concatenate → `temp = [1, 3, 2, 11, 6, -1, -7, -5]`
4. Copy back into `arr` (modify in place)

Result: `arr = [1, 3, 2, 11, 6, -1, -7, -5]` (order inside each group is preserved)

---

## 3) Python solutions (optimized & alternative), with interview-style comments

### A) Recommended (O(n) time, O(n) space) — stable, simple

```python
# User function Template for python3

class Solution:
    def segregateElements(self, arr):
        """
        Stable partition using extra buffer.
        Time  : O(n)  – two linear scans + one linear copy
        Space : O(n)  – temporary array to preserve order
        Modifies 'arr' in place as the driver expects (copies result back).
        """
        n = len(arr)
        tmp = []

        # Collect all non-negatives (>= 0) in order
        for x in arr:                 # O(n)
            if x >= 0:
                tmp.append(x)

        # Then collect all negatives in order
        for x in arr:                 # O(n)
            if x < 0:
                tmp.append(x)

        # Overwrite original array in place
        for i in range(n):            # O(n)
            arr[i] = tmp[i]
```

### B) In-place stable (no extra array) — O(n²) time (brute-ish)

> If the interviewer pushes for *no extra space* while preserving order, this is a simple insertion-style solution: keep a `write` index of where the next non-negative should sit; when you meet a non-negative at `i`, rotate the block `[write..i]` right by one. That’s stable but quadratic.

```python
class SolutionInPlaceStable:
    def segregateElements(self, arr):
        """
        Stable, in-place (no extra arrays) but O(n^2) time:
          - Maintain 'write' = next slot for a non-negative.
          - When arr[i] >= 0, rotate the block [write..i] by one to the right.
        Time  : O(n^2) in worst case (many rotations)
        Space : O(1)
        """
        n = len(arr)
        write = 0  # where next non-negative must go
        for i in range(n):
            if arr[i] >= 0:
                # save current positive
                val = arr[i]
                # shift everything between [write..i-1] one step to the right
                j = i
                while j > write:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[write] = val
                write += 1
```

> Note: A *divide-and-conquer* stable partition with in-place rotations can achieve **O(n log n)** time and **O(1)** extra (plus recursion stack), but it’s overkill here; the expected solution is A).

---

## 4) Common interviewer Q\&A

**Q1. Why can’t we just use a two-pointer partition (like quicksort)?**
Because it breaks the **relative order** (stability). The problem explicitly requires preserving the order inside positives and negatives.

**Q2. What are the expected time/space complexities?**
The problem’s editorial typically expects **O(n) time** and **O(n) extra space** (solution A). It also says “do it in place” — which is satisfied by copying the result back into `arr`.

**Q3. Can we do it in O(1) extra space and keep it stable?**
Yes, but either **O(n²)** (insertion-style shifts, solution B) or more complex **O(n log n)** approaches (divide-rotate). Not required here.

**Q4. What edge cases matter?**

* All negatives (nothing to move among positives).
* All non-negatives (array unchanged).
* Mixed with zeros (zeros are non-negative and should stay in the positive block).
* Large arrays (ensure linear solution is used).

**Q5. Can we return a new array instead of modifying in place?**
The prompt says **don’t return**, just modify the given array. Collect into a temp and copy back.

---

---

All set! I executed a **full, self-contained Python program** that:

* Implements two solutions:

  * **O(n) time, O(n) extra (stable)** — recommended and expected.
  * **In-place stable O(n²)** — for completeness/teaching.
* Runs the **examples**, several **edge cases**, a **cross-check** of both methods on a tiny input, and a **large benchmark** using `timeit`.
* Prints inputs/outputs and **timings** for each run plus the **total main runtime**.

```python

# Re-run to display outputs after the reset
from typing import List
import random, timeit

class Solution:
    def segregateElements(self, arr: List[int]) -> None:
        n = len(arr)
        tmp = []
        for x in arr:
            if x >= 0:
                tmp.append(x)
        for x in arr:
            if x < 0:
                tmp.append(x)
        for i in range(n):
            arr[i] = tmp[i]

class SolutionInPlaceStable:
    def segregateElements(self, arr: List[int]) -> None:
        write = 0
        for i in range(len(arr)):
            if arr[i] >= 0:
                val = arr[i]
                j = i
                while j > write:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[write] = val
                write += 1

def main():
    A = Solution()
    B = SolutionInPlaceStable()

    print("=== Move all negative elements to end (stable) — Demo & Timing ===")

    arr1 = [1, -1, 3, 2, -7, -5, 11, 6]
    t0 = timeit.default_timer()
    A.segregateElements(arr1)
    t1 = timeit.default_timer()
    print("\nExample 1 (O(n) with buffer):")
    print("Output:", arr1, f"   time={(t1 - t0):.6f}s  (expected [1, 3, 2, 11, 6, -1, -7, -5])")

    arr2 = [-5, 7, -3, -4, 9, 10, -1, 11]
    t0 = timeit.default_timer()
    A.segregateElements(arr2)
    t1 = timeit.default_timer()
    print("\nExample 2 (O(n) with buffer):")
    print("Output:", arr2, f"   time={(t1 - t0):.6f}s  (expected [7, 9, 10, 11, -5, -3, -4, -1])")

    tests = [
        ([], []),
        ([0, 0, 0], [0, 0, 0]),
        ([-1, -2, -3], [-1, -2, -3]),
        ([5, 4, 3], [5, 4, 3]),
        ([0, -1, 0, -2, 0], [0, 0, 0, -1, -2]),
    ]
    print("\nEdge cases (O(n) with buffer):")
    for src, exp in tests:
        arr = src[:]
        t0 = timeit.default_timer()
        A.segregateElements(arr)
        t1 = timeit.default_timer()
        print(f"  {src} -> {arr} (exp {exp})   time={(t1 - t0):.6f}s")

    tiny = [3, -1, 2, -2, -3, 4]
    arrA = tiny[:]
    arrB = tiny[:]
    t0 = timeit.default_timer()
    A.segregateElements(arrA)
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    B.segregateElements(arrB)
    t3 = timeit.default_timer()
    print("\nCross-check correctness on tiny input:")
    print("  O(n) buffer  ->", arrA, f"(time={(t1 - t0):.6f}s)")
    print("  O(n^2) in-pl ->", arrB, f"(time={(t3 - t2):.6f}s)")

    n = 300_000
    big = [random.randint(-10**6, 10**6) for _ in range(n)]
    t0 = timeit.default_timer()
    A.segregateElements(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: O(n) buffer time={(t1 - t0):.6f}s, head={big[:12]}")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (why a stable split matters)

* **Log/metric pipelines:** Move error/negative values to the end for later processing while keeping the sequence of valid readings unchanged.
* **Financial ledgers:** Bring non-negative transactions (credits/zero) to the front for quick review while preserving original chronological order; negatives (debits/refunds) follow in their original order.
* **ETL preprocessing:** Stable partition columns into “valid vs invalid/missing” rows before downstream steps that expect valid rows contiguous (and keep row ordering for traceability).
* **User interfaces/lists:** Show “available” or “positive stock” items first, then “out of stock/negative balance” items, **without** reordering within each group (users still see their original sort).
* **Streaming batchers:** Prioritize non-negative tasks in the front of a queue while preserving their arrival order, deferring negative/failed ones to the tail for retries.

