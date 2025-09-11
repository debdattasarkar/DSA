# Two sum - Pairs with 0 Sum

**Difficulty:** Easy
**Accuracy:** 31.49%
**Submissions:** 483K+
**Points:** 2
**Average Time:** 20m

---

## Problem Statement

Given an integer array `arr`, return **all the unique pairs** `[arr[i], arr[j]]` such that `i != j` and `arr[i] + arr[j] == 0`.

**Note:**

* The pairs must be returned in **sorted order**,
* The **solution array should also be sorted**,
* The answer must **not contain any duplicate pairs**.

---

## Examples

### Example 1

**Input:** `arr = [-1, 0, 1, 2, -1, -4]`
**Output:** `[[-1, 1]]`
**Explanation:** `arr[0] + arr[2] = (-1) + 1 = 0`.
`arr[2] + arr[4] = 1 + (-1) = 0`.
The **distinct** pair is `[-1, 1]`.

---

### Example 2

**Input:** `arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`
**Output:** `[[-6, 6], [-1, 1]]`
**Explanation:** The distinct pairs are `[-1, 1]` and `[-6, 6]`.

---

## Expected Time & Space

* **Expected Time Complexity:** `O(n log n)`
* **Expected Auxiliary Space:** `O(n)`

---

## Constraints

* `3 ≤ arr.size ≤ 10^5`
* `-10^5 ≤ arr[i] ≤ 10^5`

---

## Company Tags

Flipkart • Accolite • Amazon • FactSet • Hike • MakeMyTrip • Goldman Sachs • Adobe • Salesforce

---

## Topic Tags

* Arrays
* Sorting
* two-pointer-algorithm

---

## Related Interview Experiences

* Makemytrip Interview Experience For Software Engineer

---

## Related Articles

* [2 Sum Find All Pairs With Zero Sum](https://www.geeksforgeeks.org/2-sum-find-all-pairs-with-zero-sum/)
* [Given An Array Arr Find The Maximum J I Such That Arrj Arri](https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/)

---

---

Here’s an interview-ready pack for **“Two sum – pairs with 0 sum (return all unique pairs)”**.

---

## 2) Intuition + step-by-step dry run

**Goal:** from `arr`, return every **distinct** pair `[x, y]` with `x + y = 0`, **no duplicates**, the **pairs sorted** (i.e., `[-6, 6]` not `[6, -6]`) and the **list of pairs sorted** (by first, then second).

**Most reliable idea:**
Sort the array and use **two pointers** (`i` from left, `j` from right).

* If `arr[i] + arr[j] < 0` → we need a larger sum → move `i += 1`.
* If `> 0` → we need a smaller sum → move `j -= 1`.
* If `== 0` → record the pair, then **skip duplicates** on both sides, and continue.

This naturally produces pairs in sorted order and avoids duplicate pairs.

### Dry run (Example 1)

`arr = [-1, 0, 1, 2, -1, -4]`
Sort → `[-4, -1, -1, 0, 1, 2]`
`i=0 (-4), j=5 (2)` → sum = -2 < 0 → `i=1`
`i=1 (-1), j=5 (2)` → sum = 1 > 0 → `j=4`
`i=1 (-1), j=4 (1)` → sum = 0 ✅ add `[-1, 1]`
Skip dups: move `i` past all `-1`s → `i=3`; `j` past all `1`s → `j=3`
Stop (i >= j).
Result: `[[-1, 1]]`.

**Zero case:** Include `[0, 0]` only if there are **at least two zeros**.

---

## 3) Python solutions (brute & optimized) with interview-style comments

### A) Sort + Two Pointers (the expected approach)

```python
# User function Template for python3

class Solution:
    def getPairs(self, arr):
        """
        Return all unique pairs [x, y] such that x + y == 0.
        Requirements satisfied:
          - Each pair sorted (x <= y).
          - Pairs are unique (skip duplicates).
          - Output list sorted by the first element (thanks to sorting + two pointers).

        Time:  O(n log n) due to sorting
        Space: O(1) extra (ignoring output), since we sort in-place or on a copy
        """
        if not arr:
            return []

        arr.sort()                    # O(n log n)
        i, j = 0, len(arr) - 1
        ans = []

        while i < j:
            s = arr[i] + arr[j]
            if s < 0:
                i += 1                # need a bigger sum
            elif s > 0:
                j -= 1                # need a smaller sum
            else:
                # s == 0 -> record a unique pair
                ans.append([arr[i], arr[j]])

                # skip duplicates of arr[i]
                left_val = arr[i]
                while i < j and arr[i] == left_val:
                    i += 1

                # skip duplicates of arr[j]
                right_val = arr[j]
                while i < j and arr[j] == right_val:
                    j -= 1

        return ans
```

### B) Hash map counting (linear time, easy to reason about)

```python
from collections import Counter

class Solution:
    def getPairs(self, arr):
        """
        Count occurrences, then form pairs:
          - For each negative x with count[-x] > 0, include [x, -x].
          - If count[0] >= 2, include [0, 0].
        Finally sort pairs for required output order.

        Time:  O(n) to count + O(U) to iterate keys (≤ n); sort pairs is small
        Space: O(n) for counts
        """
        if not arr:
            return []

        cnt = Counter(arr)
        pairs = []

        # Handle negative/positive pairs
        for x in cnt:
            if x < 0 and cnt.get(-x, 0) > 0:
                pairs.append([x, -x])

        # Handle zeros specially (need at least two zeros)
        if cnt.get(0, 0) >= 2:
            pairs.append([0, 0])

        # Ensure solution array is sorted as required
        pairs.sort()     # sorts by first element (then second)
        return pairs
```

### C) Brute force (for completeness; rarely expected)

```python
class Solution:
    def getPairs(self, arr):
        """
        Check every pair; de-duplicate via a set of tuples.
        Time:  O(n^2)
        Space: O(k) for the set of unique pairs
        """
        seen = set()
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == 0:
                    a, b = sorted((arr[i], arr[j]))  # ensure pair order
                    seen.add((a, b))
        return [list(p) for p in sorted(seen)]
```

---

## 4) Likely interviewer Q\&A

**Q1. How do you ensure no duplicate pairs?**

* **Two pointers:** after recording a zero-sum pair, **skip all duplicates** of both values before continuing.
* **Hash counting:** consider each negative `x` once (with `-x`), and add `[0,0]` only if zeros ≥ 2.

**Q2. Why sort + two pointers instead of hash set?**
Sorting gives a very clean **O(n log n)** solution that **naturally outputs sorted pairs** and makes deduplication easy. A counting/hash approach can be **O(n)** but you must still **sort the resulting pairs** for the final requirement.

**Q3. How do you handle zeros?**
Include `[0, 0]` **only if** zero occurs at least twice.

**Q4. What about very large arrays?**

* Two pointers: **O(n log n)** time, **O(1)** extra space.
* Counting/hash: **O(n)** time, **O(n)** space. Choice depends on memory/time trade-offs and output order needs.

**Q5. What if the array is guaranteed already sorted?**
You can use the **two-pointer** method directly in **O(n)** time.

**Q6. Do you return indices or values?**
This problem returns **pairs of values**. If indices were required, two-pointers on sorted *values* would need careful handling (or use a hash map mapping value → list of indices).

**Q7. Are pairs like `[6, -6]` acceptable?**
The problem asks for **sorted pairs**; present as `[-6, 6]`.

---

---

All set — you’ve got a complete, runnable program that:

* Implements **two-pointer** (sorted) and **hash-counting** approaches,
* Prints outputs for examples + edge cases,
* Benchmarks a large input and prints the **TOTAL MAIN RUNTIME** using `timeit`.

```python

# Re-run to display outputs after the reset
from typing import List
from collections import Counter
import random
import timeit

class Solution:
    def getPairs_twoptr(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        a = sorted(arr)
        i, j = 0, len(a) - 1
        out: List[List[int]] = []
        while i < j:
            s = a[i] + a[j]
            if s < 0:
                i += 1
            elif s > 0:
                j -= 1
            else:
                out.append([a[i], a[j]])
                left, right = a[i], a[j]
                while i < j and a[i] == left:
                    i += 1
                while i < j and a[j] == right:
                    j -= 1
        return out

    def getPairs_hash(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        cnt = Counter(arr)
        out = []
        for x in cnt:
            if x < 0 and cnt.get(-x, 0) > 0:
                out.append([x, -x])
        if cnt.get(0, 0) >= 2:
            out.append([0, 0])
        out.sort()
        return out

    def getPairs(self, arr: List[int]) -> List[List[int]]:
        return self.getPairs_twoptr(arr)

def main():
    sol = Solution()
    print("=== Two sum — Pairs with 0 sum (unique pairs) — Demo & Timing ===")
    arr1 = [-1, 0, 1, 2, -1, -4]
    t0 = timeit.default_timer()
    out1 = sol.getPairs(arr1)
    t1 = timeit.default_timer()
    print("\nInput 1:", arr1)
    print("Output 1 (two-pointer):", out1, f"   time={(t1 - t0):.6f}s")
    arr2 = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
    t0 = timeit.default_timer()
    out2 = sol.getPairs(arr2)
    t1 = timeit.default_timer()
    print("\nInput 2:", arr2)
    print("Output 2 (two-pointer):", out2, f"   time={(t1 - t0):.6f}s")
    print("\nCross-check with hash-counting:")
    print("Input 1 ->", Solution().getPairs_hash(arr1))
    print("Input 2 ->", Solution().getPairs_hash(arr2))
    edges = [
        [0, 0, 0],
        [1, 2, 3],
        [-2, -2, 2, 2],
        [],
        [5, -5],
    ]
    print("\nEdge cases:")
    for e in edges:
        print(f"{e} -> {sol.getPairs(e)}")
    n = 250_000
    big = [random.randint(-100_000, 100_000) for _ in range(n)]
    t0 = timeit.default_timer()
    out_big = sol.getPairs(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: pairs_found={len(out_big)}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (where “pairs summing to zero” shows up)

* **Offsetting transactions / reconciliations:** Find credit/debit entries that net to zero for accounting cleanup.
* **Market order matching:** Identify opposing orders (buy/sell quantities with opposite signs) that cancel out.
* **Error correction in telemetry:** Pair positive/negative drift readings that neutralize each other to isolate real signal.
* **Inventory adjustments:** Match stock additions/removals that balanced to zero to detect redundant operations.
* **Algorithm sanity checks:** In simulations, detect symmetric injections/removals (e.g., +x and −x impulses) that cancel.
