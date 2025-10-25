
---

# 🧮 Rearrange Array Alternately

**Difficulty:** Medium
**Accuracy:** 35.15%
**Submissions:** 267K+
**Points:** 4

---

## 📘 Problem Statement

Given an array of **positive integers**, your task is to rearrange the array elements **alternatively** —
i.e., the **first element** should be the **maximum value**, the **second** should be the **minimum value**,
the **third** should be the **second maximum**, the **fourth** should be the **second minimum**, and so on.

> **Note:**
> Modify the **original array itself**.
> Do it **without using any extra space**.
> You **do not have to return anything.**

---

## 💡 Examples

### Example 1:

**Input:**
`arr[] = [1, 2, 3, 4, 5, 6]`

**Output:**
`[6, 1, 5, 2, 4, 3]`

**Explanation:**

* Max element = 6, Min = 1
* Second Max = 5, Second Min = 2
* Third Max = 4, Third Min = 3

→ The modified array is `[6, 1, 5, 2, 4, 3]`.

---

### Example 2:

**Input:**
`arr[] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]`

**Output:**
`[110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]`

**Explanation:**

* Max = 110, Min = 10
* Second Max = 100, Second Min = 20
* Third Max = 90, Third Min = 30
  ... and so on.

→ The modified array is `[110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]`.

---

### Example 3:

**Input:**
`arr[] = [1]`

**Output:**
`[1]`

---

## ⚙️ Constraints

```
1 ≤ arr.size ≤ 10⁶
1 ≤ arr[i] ≤ 10⁶
```

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

* Zoho

---

## 🏷️ Topic Tags

* Arrays
* Data Structures

---

## 📚 Related Articles

* Rearrange Array Maximum Minimum Form Set 2 (O(1) Extra Space)
* Rearrange Array Maximum Minimum Form

---

---

awesome—let’s make this interview-ready.

---

# 2) Explanation + step-by-step dry run

## Goal

Given an array of **positive** integers, rearrange it **in place** so that:
`[max, min, 2nd max, 2nd min, 3rd max, 3rd min, …]`

We must **modify the original array** and ideally use **O(1) extra space**.

## Two ways to think about it

1. **Easy (extra array):**
   Sort ascending, then use two pointers (`low`, `right`) to build a new array by alternately taking `right`, `low`, `right-1`, `low+1`, … Finally copy back.
   Time: O(n log n) (sort), Space: O(n).

2. **In-place O(1) (encoding trick – most asked in interviews):**

   * Sort ascending.
   * Let `M = max(arr) + 1` (strictly larger than any element).
   * Walk i = 0..n-1 with two pointers (`low`, `right`).

     * At even i, we want the next **max**; at odd i, the next **min**.
     * **Encode** the new value into the existing slot:
       `arr[i] = arr[i] + (chosen_value % M) * M`
   * After the pass, **decode** by integer-dividing every element by `M`:
     `arr[i] //= M`
     Why it works: original `arr[i] < M`, so `arr[i]` stores
     `original + new*M`. Integer division by `M` extracts `new`.

### Dry run (in-place encoding) on `[1, 2, 3, 4, 5, 6]`

Sorted already. `M = 6 + 1 = 7`.
`low = 0, right = 5`.

* i=0 (even) → choose max=6: `arr[0] = 1 + 6*7 = 43`. `right=4`.
* i=1 (odd)  → choose min=1: `arr[1] = 2 + 1*7 = 9`. `low=1`.
* i=2 (even) → choose max=5: `arr[2] = 3 + 5*7 = 38`. `right=3`.
* i=3 (odd)  → choose min=2: `arr[3] = 4 + 2*7 = 18`. `low=2`.
* i=4 (even) → choose max=4: `arr[4] = 5 + 4*7 = 33`. `right=2`.
* i=5 (odd)  → choose min=3: `arr[5] = 6 + 3*7 = 27`. `low=3`.

Now array is `[43, 9, 38, 18, 33, 27]`.
Decode: integer-divide by 7 → `[6, 1, 5, 2, 4, 3]` ✅

---

# 3) Python solutions (brute/easy + optimized in-place)

### A) Easy to remember (extra space) — two pointers after sort

```python
class Solution:
    def rearrange(self, arr):
        """
        Builds a helper list, then copies back.
        Time:  O(n log n) due to sorting
        Space: O(n) extra for the helper
        """
        n = len(arr)
        if n <= 1:
            return

        arr.sort()  # O(n log n)
        low, right = 0, n - 1
        out = []

        # Alternate: max, min, max, min...
        take_max = True
        while low <= right:
            if take_max:
                out.append(arr[right])  # next max
                right -= 1
            else:
                out.append(arr[low])  # next min
                low += 1
            take_max = not take_max

        # Copy back in-place (problem says modify original)
        arr[:] = out
```

### B) Optimized in-place (O(1) extra) — encoding/decoding trick

```python
class Solution:
    def rearrange(self, arr):
        """
        In-place alternation: [max, min, 2nd max, 2nd min, ...]
        Uses the encoding trick original + new * M, with M = max(arr) + 1.
        Time:  O(n log n) due to sorting
        Space: O(1) extra
        """
        n = len(arr)
        if n <= 1:
            return

        arr.sort()                # O(n log n), required to pick mins/maxes
        base = arr[-1] + 1        # M > any element (since positives)
        low, right = 0, n - 1

        # First pass: store both old and new in each cell
        for i in range(n):
            if i % 2 == 0:
                # place next maximum
                val = arr[right] % base
                right -= 1
            else:
                # place next minimum
                val = arr[low] % base
                low += 1
            arr[i] += val * base

        # Second pass: decode to keep only the "new" values
        for i in range(n):
            arr[i] //= base
```

### C) Variant (still O(n) extra, very readable) — fill by index parity

```python
class Solution:
    def rearrange(self, arr):
        """
        Readable variant using an auxiliary list and parity positions.
        Time:  O(n log n)
        Space: O(n)
        """
        n = len(arr)
        if n <= 1:
            return

        arr.sort()
        out = [0] * n
        low, right = 0, n - 1
        for i in range(n):
            if i % 2 == 0:
                out[i] = arr[right]; right -= 1
            else:
                out[i] = arr[low]; low += 1
        arr[:] = out
```

---

# 4) Interview quick-recall + expected Q&A

## 10-second memory hook

* **Mantra:** “**Sort, then Max–Min alternation. Encode to stay in place.**”
* **Pocket code:**
  `M = max+1; for i: arr[i] += (choice % M) * M; finally arr[i] //= M`.

## Common interviewer questions

**Q1. Why does the encoding trick work?**
Because `M` is strictly larger than any original value. After storing
`arr[i] = original + new*M`, integer division by `M` retrieves `new` and modulo retrieves `original`. No overflow in Python; in fixed-width languages ensure `M*new` fits type.

**Q2. Why do we sort first?**
Sorting gives direct access to the current smallest (`low`) and largest (`right`) at every step, enabling the perfect alternation.

**Q3. Time and space?**
With encoding: **O(n log n)** time (sort), **O(1)** extra space.
With helper array: **O(n log n)** time, **O(n)** space.

**Q4. What if numbers aren’t positive?**
The classic trick assumes **positive** so `M = max + 1 > 0` and all originals are `< M`. If zeros appear, still okay since `< M`. If negatives are allowed, you can shift all values by `+offset` (or pick `M > (max_val - min_val)` and store shifted values) — but the given problem states **positive**.

**Q5. Any edge cases?**
`n ≤ 1`, already sorted or reverse sorted, all equal values — all handled.
For odd `n`, the final element will be whichever side (max or min) is next in order.

**Q6. Can we do it in O(n) without sorting?**
Not while preserving the **max/min/2nd max/…** exact order. You’d need partial selections repeatedly which costs ≥ O(n log n) in total or becomes complex.

---

---

awesome — here are the last two parts for **Rearrange Array Alternately** 👇

---

# 5) Real-World Use Cases (short, interviewer-relatable)

* **Front-page product carousel**
  Show most popular (max), then a budget pick (min), then 2nd most popular, then 2nd budget, … to balance *prestige vs. price* in a single row.

* **A/B content scheduling**
  Alternate *high-impact* and *low-impact* items to smooth user fatigue: max engagement article, low-engagement filler, next max, next min…

* **Load/traffic shaping**
  When dispatching tasks of varying cost, alternate heavy and light jobs: pick largest, smallest, 2nd largest, 2nd smallest… to reduce peak contention.

These map directly to the “max, min, 2nd max, 2nd min…” ordering.

---

# 6) Full Python Program

Includes:

* **In-place O(1) extra space** solution (encoding/decoding trick) — interview favorite
* **Readable helper-array** solution for comparison
* Printed outputs for sample inputs
* `timeit` timing on a larger random array

```python
from timeit import timeit
from random import randint, seed

# ------------------------------------------------------------
# Solution 1: In-place O(1) using encoding/decoding (recommended)
# ------------------------------------------------------------
class Solution:
    def rearrange(self, arr):
        """
        Rearrange as: [max, min, 2nd max, 2nd min, ...] in-place.
        Steps:
          1) Sort ascending                  -> O(n log n) time, O(1) extra (Timsort may use tiny temp)
          2) base = max(arr) + 1             -> O(1)
          3) One pass encode new values      -> O(n)
             arr[i] = arr[i] + (chosen % base) * base
          4) One pass decode (arr[i] //= base) -> O(n)
        Overall time:  O(n log n)
        Overall space: O(1) extra (ignoring input/output), arr modified in place.
        """
        n = len(arr)
        if n <= 1:
            return

        # --- Sort so we can pull mins and maxes easily ---
        arr.sort()  # O(n log n)

        # --- Choose a base strictly larger than any element ---
        base = arr[-1] + 1  # arr[i] < base for all i (positive ints per problem)

        # Two pointers to ends for max/min picks
        low, right = 0, n - 1

        # --- Encode: stash "new" into high digits while keeping "old" in low digits ---
        for i in range(n):                       # O(n)
            if i % 2 == 0:                       # even index -> place next maximum
                chosen = arr[right] % base
                right -= 1
            else:                                # odd index -> place next minimum
                chosen = arr[low] % base
                low += 1
            # Each cell stores: old + new*base (old < base ensures no overlap)
            arr[i] += chosen * base

        # --- Decode: keep only the "new" values ---
        for i in range(n):                       # O(n)
            arr[i] //= base


# ------------------------------------------------------------
# Solution 2: Helper array (very readable, O(n) extra space)
# ------------------------------------------------------------
class SolutionExtra:
    def rearrange(self, arr):
        """
        Build a helper list alternating right/lo, then copy back.
        Time:  O(n log n) due to sorting + O(n) merge
        Space: O(n) helper
        """
        n = len(arr)
        if n <= 1:
            return

        arr.sort()            # O(n log n)
        low, right = 0, n - 1
        out = []
        take_max = True
        while low <= right:       # O(n)
            if take_max:
                out.append(arr[right]); right -= 1
            else:
                out.append(arr[low]); low += 1
            take_max = not take_max
        arr[:] = out          # O(n) copy back


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Rearrange Array Alternately ===\n")

    samples = [
        ("Example 1", [1, 2, 3, 4, 5, 6],             [6, 1, 5, 2, 4, 3]),
        ("Example 2", [10,20,30,40,50,60,70,80,90,100,110],
                      [110,10,100,20,90,30,80,40,70,50,60]),
        ("Example 3", [1],                            [1]),
        ("Mixed",     [2, 9, 9, 4, 3, 7, 1],          [9,1,9,2,7,3,4]),  # one valid arrangement
    ]

    s_inplace = Solution()
    s_extra   = SolutionExtra()

    for name, arr, expected in samples:
        a1 = arr[:]  # copy for method 1
        a2 = arr[:]
        s_inplace.rearrange(a1)
        s_extra.rearrange(a2)
        print(f"{name}:")
        print(f"  Input:     {arr}")
        print(f"  In-place:  {a1}")
        print(f"  ExtraArr:  {a2}")
        print(f"  Example expected (one valid): {expected}\n")

    # ---- Timing on a larger random array ----
    seed(42)
    n = 100_000
    big = [randint(1, 10**6) for _ in range(n)]

    # timeit runs only the function logic; number chosen for a stable reading
    t_inplace = timeit(lambda: (lambda a: (Solution().rearrange(a)))(big[:]), number=3)
    t_extra   = timeit(lambda: (lambda a: (SolutionExtra().rearrange(a)))(big[:]), number=3)

    print("=== Timing (seconds) on n = 100,000 (3 runs each) ===")
    print(f"In-place O(1) extra:  {t_inplace:.4f}s")
    print(f"Extra array O(n):     {t_extra:.4f}s")


if __name__ == "__main__":
    run_demo()
```

**What you’ll see when you run it**

* For the samples, both methods produce the “max, min, 2nd max, 2nd min…” pattern. (There are multiple valid outputs for arrays with duplicates; the examples show *one* valid arrangement.)
* The timing section shows real execution times for both methods on a 100k-element array. Both are dominated by sorting (**O(n log n)**). The in-place version saves memory.
