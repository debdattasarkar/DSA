
---

# 🧩 Count Inversions

**Difficulty:** Medium
**Accuracy:** 16.93%
**Submissions:** 672K+
**Points:** 4

---

## 🧠 Problem Statement

Given an array of integers **arr[]**, find the **Inversion Count** in the array.

Two elements **arr[i]** and **arr[j]** form an inversion if:

> arr[i] > arr[j] and i < j

---

### 🧾 Definition

**Inversion Count:**
For an array, inversion count indicates how far (or close) the array is from being sorted.

* If the array is already sorted, then the inversion count is **0**.
* If the array is sorted in reverse order, then the inversion count is the **maximum**.

---

## 🧮 Examples

### Example 1

**Input:**
`arr[] = [2, 4, 1, 3, 5]`

**Output:**
`3`

**Explanation:**
The sequence `[2, 4, 1, 3, 5]` has three inversions:

* (2, 1)
* (4, 1)
* (4, 3)

---

### Example 2

**Input:**
`arr[] = [2, 3, 4, 5, 6]`

**Output:**
`0`

**Explanation:**
As the sequence is already sorted, there is no inversion count.

---

### Example 3

**Input:**
`arr[] = [10, 10, 10]`

**Output:**
`0`

**Explanation:**
All elements are the same, so there is no inversion count.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^5  
1 ≤ arr[i] ≤ 10^4
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

`Flipkart` `Amazon` `Microsoft` `MakeMyTrip` `Adobe` `BankBazaar` `Myntra`

---

## 🧰 Topic Tags

`Arrays` `Divide and Conquer` `Sorting` `Data Structures` `Algorithms`

---

## 💼 Related Interview Experiences

* Makemytrip Interview Experience for SDE On Campus
* Flipkart Interview Experience Set 22 for SDE 2

---

## 📚 Related Articles

* [*Inversion Count in Array Using Merge Sort*](https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/)

---

---

Absolutely! Here’s an interview-ready package for **Count Inversions**: intuition, a clear dry run, two Python solutions (brute force and optimal merge-sort), and a compact recall/Q&A kit.

---

## 2) Intuition + Step-by-Step Dry Run

### What is an inversion?

For indices `i < j`, pair `(arr[i], arr[j])` is an **inversion** if `arr[i] > arr[j]`.
The total number of such pairs is the **inversion count**—a measure of “how far” an array is from being sorted.

### Two ways to count

1. **Brute force**: check every pair → `O(n^2)`.
2. **Merge sort trick (Divide & Conquer)**:

   * While merging two **sorted** halves, if `left[i] > right[j]`, then `left[i]` and **all** remaining elements `left[i..]` form inversions with `right[j]`.
   * Count them in one go: `inversions += (len(left) - i)`.
   * This yields `O(n log n)`.

---

### Dry Run (merge-sort method)

`arr = [2, 4, 1, 3, 5]`

1. Split → `[2,4,1]` and `[3,5]`
2. Split `[2,4,1]` → `[2,4]` and `[1]`

   * Merge `[2]` & `[4]` → `[2,4]`, inversions = 0
   * Merge `[2,4]` & `[1]`:

     * Compare 2 vs 1: `2 > 1` → inversion(s) with the **remaining elements in left**: two elements `[2,4]`.
       Add `2` → count = 2, merged `[1]`, then append `[2,4]` → `[1,2,4]`.
3. Merge left `[1,2,4]` with right `[3,5]`:

   * 1 ≤ 3 → no inversion
   * 2 ≤ 3 → no inversion
   * 4 > 3 → inversions with remaining in left: only `[4]` → add `1`
   * Append rest: final `[1,2,3,4,5]`
4. Total inversions = `2 + 1 = 3`.

Matches the example pairs: (2,1), (4,1), (4,3).

> Duplicates? If `left[i] <= right[j]`, we take `left[i]` **without** adding inversions (because `<=` is not an inversion). This keeps the count correct and stable.

---

## 3) Python Solutions (your requested signature)

### A) Optimal – Merge Sort Counting (`O(n log n)`, `O(n)` extra)

```python
class Solution:
    def inversionCount(self, arr):
        """
        Count inversions using merge-sort based counting.
        Time:  O(n log n)
        Space: O(n) extra for temp arrays
        """
        n = len(arr)
        if n <= 1:
            return 0

        # Helper: merge two sorted slices arr[l:m+1] and arr[m+1:r], count cross inversions
        def merge_and_count(a, l, m, r, buf):
            i, j, k = l, m + 1, l  # i->left, j->right, k->buf index
            inv = 0

            # Merge in ascending order; count inversions when left[i] > right[j]
            while i <= m and j <= r:
                if a[i] <= a[j]:
                    buf[k] = a[i]
                    i += 1
                else:
                    # a[i] > a[j] → all remaining left elements [i..m] are > a[j]
                    buf[k] = a[j]
                    inv += (m - i + 1)   # add how many are left in left half
                    j += 1
                k += 1

            # Copy leftovers (no new inversions because halves are sorted)
            while i <= m:
                buf[k] = a[i]; i += 1; k += 1
            while j <= r:
                buf[k] = a[j]; j += 1; k += 1

            # Write merged back to original array slice
            for t in range(l, r + 1):
                a[t] = buf[t]

            return inv

        # Recursive divide & conquer
        def sort_and_count(a, l, r, buf):
            if l >= r:
                return 0
            m = (l + r) // 2
            inv = 0
            inv += sort_and_count(a, l, m, buf)        # left inversions
            inv += sort_and_count(a, m + 1, r, buf)    # right inversions
            inv += merge_and_count(a, l, m, r, buf)    # cross inversions during merge
            return inv

        buffer = [0] * n  # O(n) temp
        return sort_and_count(arr, 0, n - 1, buffer)
```

### B) Brute Force – Double Loop (`O(n^2)`, `O(1)` extra)

```python
class Solution:
    def inversionCount(self, arr):
        """
        Brute force: check all pairs (i < j) and count arr[i] > arr[j].
        Time : O(n^2)
        Space: O(1)
        """
        n = len(arr)
        inv = 0
        for i in range(n):
            ai = arr[i]
            for j in range(i + 1, n):
                if ai > arr[j]:
                    inv += 1
        return inv
```

> In interviews, **always lead with the merge-sort solution**; briefly mention brute force as the baseline.

---

## 4) Interview Memory Hook + Q&A

### 5-Line Pseudocode (memorize this)

```
function sort_and_count(a):
    if len(a) <= 1: return 0
    split into left, right
    inv = sort_and_count(left) + sort_and_count(right)
    inv += merge_and_count(left, right)  # when left[i] > right[j], add (len(left)-i)
    return inv
```

### One-liner to say

> “Use merge sort. While merging two sorted halves, if `left[i] > right[j]`, then `left[i..]` are all inversions with `right[j]`, so add `(mid - i + 1)`. Total is `O(n log n)`.”

### Common interviewer questions

* **Q: Why does `(mid - i + 1)` work?**
  **A:** The halves are individually sorted. If `left[i] > right[j]`, then **every** element from `left[i]` to `left[mid]` is ≥ `left[i]` and thus > `right[j]`. That’s exactly `(mid - i + 1)` elements.

* **Q: What about equal elements?**
  **A:** Inversions require strict `>`. If `left[i] <= right[j]`, we place `left[i]` with **no** inversions added.

* **Q: Time/Space complexity?**
  **A:** `O(n log n)` time, `O(n)` extra space for the merge buffer (unless you do very careful in-place tricks; typical interview answer is `O(n)`).

* **Q: Edge cases to consider?**

  * Already sorted → `0`
  * Reverse sorted → maximum inversions `n*(n-1)/2`
  * All equal → `0`
  * Large `n` up to `1e5` → must use `O(n log n)` method.

* **Q: Can we do it in `O(n log n)` with Fenwick/Segment Tree?**
  **A:** Yes (coordinate compression + BIT/Segment Tree). It’s another valid approach but merge-sort counting is the **most expected**.

---

---

Awesome—let’s wrap **Count Inversions** with (5) crisp, relatable **use cases** and (6) a **full, runnable Python program** that times both the optimal merge-sort method and the brute-force baseline. Everything is annotated with time/space complexity inline.

---

## 5) Real-World Use Cases (easy to pitch)

* **Sorting “distance” / quality metric**
  Inversion count measures how far a sequence is from being sorted. Used to evaluate sorting progress, ranking disagreements, or “disorder” in data.

* **Kendall tau distance (rank correlation)**
  Inversion count equals the number of discordant pairs between two rankings (after mapping one ranking to indices of the other). Used in information retrieval, recommender systems, and social choice.

* **Genome sequence comparison**
  When comparing permutations of genes, inversions quantify how many pairwise order disagreements exist (a proxy for evolutionary distance).

* **UI list reordering / drag-and-drop analytics**
  After a user reorders a list, inversions vs. a canonical order indicate effort/error or how “off” the initial ordering was.

* **Network/message out-of-order analysis**
  For packets/events that should be increasing, inversions measure the degree of reordering introduced by the system.

---

## 6) Full Program (with timing + inline complexity notes)

```python
#!/usr/bin/env python3
"""
Count Inversions in an array.

We include:
  1) Optimal O(n log n) merge-sort based counter (expected in interviews)
  2) Brute O(n^2) baseline for comparison
  3) A small demo + timing using timeit

All steps are commented with time/space complexities.
"""

from time import perf_counter
import timeit
from typing import List


class Solution:
    # -------- Optimal: Merge-sort based O(n log n), O(n) extra -------- #
    def inversionCount_merge(self, arr: List[int]) -> int:
        """
        Count inversions using merge sort.

        Idea:
          While merging two sorted halves [l..m], [m+1..r]:
            if left[i] <= right[j]: take left[i] (no inversions added)
            else left[i] > right[j]:
                 all remaining elements left[i..m] are > right[j]
                 add (m - i + 1) inversions in O(1)

        Time  : O(n log n)  (each level merges in O(n); log n levels)
        Space : O(n) for a temporary buffer (standard stable merge)
        """
        n = len(arr)
        if n <= 1:
            return 0

        tmp = [0] * n  # O(n) extra for merges

        def merge_and_count(a, l, m, r) -> int:
            """Merge a[l..m] and a[m+1..r] (both sorted) and count cross inversions."""
            i, j, k = l, m + 1, l
            inv = 0
            while i <= m and j <= r:
                if a[i] <= a[j]:
                    tmp[k] = a[i]   # a[i] is not greater → no new inversions
                    i += 1
                else:
                    tmp[k] = a[j]   # a[i] > a[j] → all left[i..m] invert with a[j]
                    inv += (m - i + 1)
                    j += 1
                k += 1

            # Copy leftovers (no new inversions; halves are sorted)
            while i <= m:
                tmp[k] = a[i]; i += 1; k += 1
            while j <= r:
                tmp[k] = a[j]; j += 1; k += 1

            # Write merged back to a
            for t in range(l, r + 1):
                a[t] = tmp[t]

            return inv

        def sort_and_count(a, l, r) -> int:
            if l >= r:
                return 0
            m = (l + r) // 2
            inv = 0
            inv += sort_and_count(a, l, m)      # inversions wholly in left
            inv += sort_and_count(a, m + 1, r)  # inversions wholly in right
            inv += merge_and_count(a, l, m, r)  # cross inversions (left vs right)
            return inv

        # We may mutate arr during counting; copy if you need original kept.
        return sort_and_count(arr, 0, n - 1)

    # -------- Brute: O(n^2), O(1) extra (for sanity check / small n) -------- #
    def inversionCount_bruteforce(self, arr: List[int]) -> int:
        """
        Double loop counting pairs (i < j) with arr[i] > arr[j].
        Time  : O(n^2)
        Space : O(1)
        """
        n = len(arr)
        inv = 0
        for i in range(n):
            ai = arr[i]
            for j in range(i + 1, n):
                if ai > arr[j]:
                    inv += 1
        return inv


# --------------------------- Demo & Timing --------------------------- #
def run_demo():
    sol = Solution()

    tests = [
        ([2, 4, 1, 3, 5], 3),
        ([2, 3, 4, 5, 6], 0),
        ([10, 10, 10], 0),
        ([5, 4, 3, 2, 1], 10),  # n=5 → 5*4/2 = 10 (max)
        ([1, 3, 2, 3, 1], 4),
    ]

    print("=== Sample I/O ===")
    for arr, expect in tests:
        a1 = arr[:]  # copy for merge-sort
        a2 = arr[:]  # copy for brute force

        # Time merge approach (µs)
        start = perf_counter()
        inv_merge = sol.inversionCount_merge(a1)
        t_merge = (perf_counter() - start) * 1e6

        # Time brute approach (µs)
        start = perf_counter()
        inv_brute = sol.inversionCount_bruteforce(a2)
        t_brute = (perf_counter() - start) * 1e6

        print(f"arr = {arr}")
        print(f"  merge-sort: {inv_merge} (expected {expect})  [{t_merge:.1f} µs]")
        print(f"  brute     : {inv_brute} (expected {expect})  [{t_brute:.1f} µs]")
        print("-" * 60)

    # Larger timing to show the difference
    import random
    random.seed(7)
    n_big = 100_000
    big = list(range(n_big))
    random.shuffle(big)  # worst-ish on average

    # Average over 3 runs for stability
    avg_merge = timeit.timeit(
        "sol.inversionCount_merge(big[:])",
        number=3,
        globals={"sol": sol, "big": big}
    ) / 3.0
    print(f"Average merge-sort time over 3 runs for n={n_big}: {avg_merge:.3f} s")

    # The brute-force would take O(n^2) → ~1e10 ops for 1e5; we won't run it.


if __name__ == "__main__":
    run_demo()
```

### What you’ll see (illustrative)

```
=== Sample I/O ===
arr = [2, 4, 1, 3, 5]
  merge-sort: 3 (expected 3)  [xx.x µs]
  brute     : 3 (expected 3)  [yy.y µs]
------------------------------------------------------------
arr = [2, 3, 4, 5, 6]
  merge-sort: 0 (expected 0)  [...]
  brute     : 0 (expected 0)  [...]
...
Average merge-sort time over 3 runs for n=100000: 0.xxx s
```

**Complexity recap (to say in the interview):**

* **Optimal (merge-based)**: `O(n log n)` time; `O(n)` extra space for the merge buffer.
* **Brute**: `O(n^2)` time; `O(1)` space—ok only for very small `n`.
