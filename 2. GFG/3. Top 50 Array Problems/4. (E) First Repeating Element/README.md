# First Repeating Element

**Difficulty:** Easy
**Accuracy:** 32.57%
**Submissions:** 302K+
**Points:** 2
**Average Time:** 15m

---

## Problem Statement

Given an array `arr[]`, find the **first repeating element**. The element should occur **more than once** and the **index of its first occurrence** should be the **smallest**.

**Note:** The position you return should be according to **1-based indexing**.

---

## Examples

### Example 1

**Input:** `arr[] = [1, 5, 3, 4, 3, 5, 6]`
**Output:** `2`
**Explanation:** `5` appears twice and its first appearance is at index `2`, which is less than `3` whose first occurring index is `3`.

---

### Example 2

**Input:** `arr[] = [1, 2, 3, 4]`
**Output:** `-1`
**Explanation:** All elements appear only once so the answer is `-1`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

Amazon • Oracle

---

## Topic Tags

* Arrays
* Hash
* Data Structures

---

## Related Articles

* *[Find First Repeating Element Array Integers](https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/)*

---

---

Here’s an interview-ready guide for **First Repeating Element** (return the **1-based** index of the **earliest position** among values that occur ≥ 2 times; return **-1** if all are unique).

---

## 2) Intuition + step-by-step dry run

### Idea

To know whether an element is “repeating”, we need its **frequency**. The cleanest way:

1. **Count** occurrences of each value.
2. **Scan from left to right**; the first position whose value has frequency > 1 is our answer.

This guarantees the **smallest index** among repeating values.

### Dry run on Example

`arr = [1, 5, 3, 4, 3, 5, 6]`

**Pass 1 (count):**

* counts → {1:1, 5:2, 3:2, 4:1, 6:1}

**Pass 2 (left→right):**

* i=0 (1) → freq=1 → skip
* i=1 (5) → freq=2 → **answer = 1+1 = 2** ✅

If `arr = [1,2,3,4]` → all freqs = 1 → return **-1**.

---

## 3) Python solutions (what interviewers expect)

### A) Hash frequency then left scan (simple & standard)

```python
class Solution:
    def firstRepeated(self, arr):
        """
        Return 1-based index of the earliest position whose value repeats later.
        Time:  O(n)
        Space: O(n)   (hash map of frequencies)
        """
        from collections import Counter
        freq = Counter(arr)                  # O(n)
        for i, x in enumerate(arr):         # O(n)
            if freq[x] > 1:
                return i + 1                # 1-based index
        return -1
```

### B) Reverse scan with a set (one pass, also O(n)/O(n))

> Walk from **right to left**; add each value to a `seen` set.
> If we see a value already in `seen`, that index becomes a **candidate**.
> The **last candidate found while moving left** is the **smallest index** of a repeating value.

```python
class Solution:
    def firstRepeated(self, arr):
        """
        Reverse-scan trick: the last index we set while moving left is
        the smallest index of a repeating value.
        Time:  O(n)
        Space: O(n)
        """
        seen = set()
        ans = -1
        for i in range(len(arr) - 1, -1, -1):  # right -> left
            if arr[i] in seen:
                ans = i + 1                    # 1-based
            else:
                seen.add(arr[i])
        return ans
```

### C) Single-pass tracking first index + best answer (still O(n)/O(n))

> Keep a map to the first position where each value appeared; each time you see a value again, update the **minimum first index**.

```python
class Solution:
    def firstRepeated(self, arr):
        """
        Track first index for each value; update best (minimum) when a duplicate appears.
        Time:  O(n)
        Space: O(n)
        """
        first_pos = {}          # value -> first index (0-based)
        best = float('inf')
        for i, x in enumerate(arr):
            if x in first_pos:
                if first_pos[x] < best:
                    best = first_pos[x]
            else:
                first_pos[x] = i
        return (best + 1) if best != float('inf') else -1
```

### D) (Optional) Array count instead of dict (when values are bounded)

If `0 ≤ arr[i] ≤ 10^6` (as in constraints), you can use a **list of size 10^6+1** for counts, which saves hashing overhead and is memory-OK (\~8 MB):

```python
class Solution:
    def firstRepeated(self, arr):
        nmax = 10**6 + 1
        freq = [0] * nmax                     # O(U) init; acceptable under constraints
        for x in arr:
            freq[x] += 1
        for i, x in enumerate(arr):
            if freq[x] > 1:
                return i + 1
        return -1
```

> In interviews, start with **A** (cleanest). Mention **B** as an elegant one-pass variant and **D** when values are small & non-negative.

---

## 4) Likely interviewer Q\&A

**Q1. What exactly is “first repeating element” here?**
It’s the **smallest index i** such that `arr[i]` appears **again** somewhere after `i`. Return `i+1` (1-based). It’s **not** “the first element that becomes a duplicate while scanning” (those differ for some arrays).

**Q2. Time & space complexity?**
All given solutions run in **O(n)** time.
Space is **O(n)** for maps/sets; the array-count variant uses **O(U)** where `U` is the value range (here up to 10^6).

**Q3. Why not sort?**
Sorting is `O(n log n)` and would lose original positions unless we store indices; it’s slower and more complex than the `O(n)` hash solutions.

**Q4. What if numbers can be negative or very large?**
Use a **hash map** (`dict`/`Counter`), not an indexed array. The array-count trick only works when values are small non-negative integers within a known bound.

**Q5. How to adapt for “first non-repeating element”?**
Still do a frequency pass; then return the first index with frequency `== 1`.

**Q6. Any pitfalls?**

* Remember to return **1-based** index.
* Ensure you’re returning the **earliest index among repeating values**, not the earliest repeated pair encountered.

---

---

All set! I executed a **complete inline Python program** that:

* Implements `firstRepeated` (Counter + left scan, `O(n)`/`O(n)`), plus two alternatives:

  * reverse-scan with a set,
  * first-index tracking map.
* Prints results for the samples and several edge cases.
* Benchmarks a large array (`n=300,000`) and prints the **TOTAL MAIN RUNTIME** using `timeit`.

```python

from typing import List
from collections import Counter
import timeit

class Solution:
    def firstRepeated(self, arr: List[int]) -> int:
        freq = Counter(arr)
        for i, x in enumerate(arr):
            if freq[x] > 1:
                return i + 1
        return -1

    def firstRepeated_reverse(self, arr: List[int]) -> int:
        seen = set()
        ans = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] in seen:
                ans = i + 1
            else:
                seen.add(arr[i])
        return ans

    def firstRepeated_firstpos(self, arr: List[int]) -> int:
        first_pos = {}
        best = float('inf')
        for i, x in enumerate(arr):
            if x in first_pos:
                if first_pos[x] < best:
                    best = first_pos[x]
            else:
                first_pos[x] = i
        return (best + 1) if best != float('inf') else -1

def main():
    sol = Solution()
    print("=== First Repeating Element — Demo & Timing ===\n")
    arr1 = [1, 5, 3, 4, 3, 5, 6]
    print("Input 1 :", arr1)
    t0 = timeit.default_timer()
    out1 = sol.firstRepeated(arr1)
    t1 = timeit.default_timer()
    print("Output 1 (Counter+scan):", out1, f"   time={(t1 - t0):.6f}s")
    print("Alt (reverse set):     ", sol.firstRepeated_reverse(arr1))
    print("Alt (first-pos map):   ", sol.firstRepeated_firstpos(arr1))
    arr2 = [1, 2, 3, 4]
    print("\nInput 2 :", arr2)
    t0 = timeit.default_timer()
    out2 = sol.firstRepeated(arr2)
    t1 = timeit.default_timer()
    print("Output 2 (Counter+scan):", out2, f"   time={(t1 - t0):.6f}s")
    print("Alt (reverse set):     ", sol.firstRepeated_reverse(arr2))
    print("Alt (first-pos map):   ", sol.firstRepeated_firstpos(arr2))
    arr3 = [7]
    arr4 = []
    arr5 = [2,2,2]
    print("\nEdge 1 :", arr3, "->", sol.firstRepeated(arr3))
    print("Edge 2 :", arr4, "->", sol.firstRepeated(arr4))
    print("Edge 3 :", arr5, "->", sol.firstRepeated(arr5))
    n = 300_000
    big = list(range(n))
    big[n // 2] = big[0]
    t0 = timeit.default_timer()
    out_big = sol.firstRepeated(big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: result={out_big}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")

```

---

## 6) Real-World Use Cases (high-impact)

* **Data validation / deduping:** Quickly detect the first value that occurs more than once in event streams or logs to flag bad ingestion records.
* **Transaction / ID pipelines:** Identify the earliest duplicated transaction ID or order number to prevent double processing.
* **Compiler / parser passes:** Find the first repeated token/symbol in a sequence where earliest reappearance matters (e.g., shadowed variable names).
* **User analytics:** First repeated click/action in a session to trigger heuristics (e.g., rage-click detection).
* **Cache / DB keys:** Detect early repeated keys in batch loads to decide conflict resolution strategies.
