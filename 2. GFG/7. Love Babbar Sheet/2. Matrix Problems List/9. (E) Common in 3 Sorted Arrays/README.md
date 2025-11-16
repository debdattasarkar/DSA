
---

# 🧩 Common in 3 Sorted Arrays

**Difficulty:** Easy
**Accuracy:** 22.16%
**Submissions:** 431K+
**Points:** 2

---

## 📘 Problem Statement

Given three sorted arrays in **non-decreasing order**, print all **common elements** in non-decreasing order across these arrays.
If there are no such elements, return an empty array.
In this case, the output will be `-1`.

> **Note:**
> Can you handle duplicates **without using any additional Data Structure**?

---

## 💡 Examples

### Example 1:

**Input:**
`arr1 = [1, 5, 10, 20, 40, 80]`
`arr2 = [6, 7, 20, 80, 100]`
`arr3 = [3, 4, 15, 20, 30, 70, 80, 120]`

**Output:**
`[20, 80]`

**Explanation:**
`20` and `80` are the only common elements in `arr`, `brr`, and `crr`.

---

### Example 2:

**Input:**
`arr1 = [1, 2, 3, 4, 5]`
`arr2 = [6, 7]`
`arr3 = [8, 9, 10]`

**Output:**
`[-1]`

**Explanation:**
There are no common elements in `arr`, `brr`, and `crr`.

---

### Example 3:

**Input:**
`arr1 = [1, 1, 1, 2, 2, 2]`
`arr2 = [1, 1, 2, 2, 2]`
`arr3 = [1, 1, 1, 2, 2, 2, 2]`

**Output:**
`[1, 2]`

**Explanation:**
We do not need to consider duplicates.

---

## ⚙️ Constraints

```
1 <= arr1.size(), arr2.size(), arr3.size() <= 10^5
-10^5 <= arr1[i], arr2[i], arr3[i] <= 10^5
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

`VMWare`, `Microsoft`, `MAQ Software`

---

## 🏷️ Topic Tags

* Searching
* Algorithms

---

## 💬 Related Interview Experiences

* Microsoft Interview Experience Set 58 For Software Engineer

---

## 📚 Related Articles

* [Find Common Elements Three Sorted Arrays](https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/)

---

---

awesome — here’s an interview-ready pack for **“Common Elements in 3 Sorted Arrays”** with clear logic, dry run, and multiple Python solutions in your requested format.

---

# 2) Explanation + Step-by-Step Dry Run

## Problem in one line

Given **three non-decreasing arrays**, return **all distinct values** that appear in **all three**.
If none exist, return `[-1]`.

## Key idea (most expected in interviews)

Use **three pointers** (`i, j, k`) walking the arrays **once**.
At each step compare `arr1[i], arr2[j], arr3[k]`:

* If all three are **equal**, it’s a common element → record it, then **advance all three** (and **skip duplicates** in each array).
* Else, **advance the pointer** that has the **smallest** value (to catch up to the others).
* Repeat until any pointer reaches its array’s end.

This is linear time in total lengths and **O(1)** extra space (ignoring output).

### Why skipping duplicates works

Arrays are sorted. Once you output value `x`, advancing over any repeated `x` in each array ensures you never output `x` again.

---

## Dry run (from the prompt)

`arr1 = [1, 5, 10, 20, 40, 80]`
`arr2 = [6, 7, 20, 80, 100]`
`arr3 = [3, 4, 15, 20, 30, 70, 80, 120]`

Start: `i=j=k=0`
Result `R = []`

|  i | a1 |  j | a2 |  k | a3 | Min? | Action                                     |
| -: | -: | -: | -: | -: | -: | :--: | :----------------------------------------- |
|  0 |  1 |  0 |  6 |  0 |  3 |   1  | advance `i` (1 is smallest)                |
|  1 |  5 |  0 |  6 |  0 |  3 |   3  | advance `k` (3 is smallest)                |
|  1 |  5 |  0 |  6 |  1 |  4 |   4  | advance `k`                                |
|  1 |  5 |  0 |  6 |  2 | 15 |   5  | advance `i`                                |
|  2 | 10 |  0 |  6 |  2 | 15 |   6  | advance `j`                                |
|  2 | 10 |  1 |  7 |  2 | 15 |   7  | advance `j`                                |
|  2 | 10 |  2 | 20 |  2 | 15 |  10  | advance `i`                                |
|  3 | 20 |  2 | 20 |  2 | 15 |  15  | advance `k`                                |
|  3 | 20 |  2 | 20 |  3 | 20 |   —  | **equal ⇒ add 20; skip dups; i=4,j=3,k=4** |
|  4 | 40 |  3 | 80 |  4 | 30 |  30  | advance `k`                                |
|  4 | 40 |  3 | 80 |  5 | 70 |  40  | advance `i`                                |
|  5 | 80 |  3 | 80 |  5 | 70 |  70  | advance `k`                                |
|  5 | 80 |  3 | 80 |  6 | 80 |   —  | **equal ⇒ add 80; skip dups; i=6 (end)**   |

Result: `R = [20, 80]`

---

# 3) Python solutions (multiple ways)

## A) Three-Pointer (recommended/optimal) — **O(n1+n2+n3) time, O(1) space**

```python
# User function Template for python3
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        """
        Return distinct elements common to all three sorted arrays.
        If none exist, return [-1].

        Time:  O(n1 + n2 + n3)  -> single pass with three pointers
        Space: O(1) extra       -> only indices and output list
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        answer = []

        # Walk the three arrays simultaneously
        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]

            # Case 1: common value found
            if a == b == c:
                # Add once (distinct output)
                answer.append(a)

                # Move all three pointers forward while skipping duplicates
                current = a
                while i < n1 and arr1[i] == current:  # O(#dups1)
                    i += 1
                while j < n2 and arr2[j] == current:  # O(#dups2)
                    j += 1
                while k < n3 and arr3[k] == current:  # O(#dups3)
                    k += 1

            else:
                # Case 2: advance the smallest to catch up
                smallest = min(a, b, c)
                if a == smallest:
                    # Skip duplicates of arr1[i] while advancing
                    val = a
                    while i < n1 and arr1[i] == val:
                        i += 1
                elif b == smallest:
                    val = b
                    while j < n2 and arr2[j] == val:
                        j += 1
                else:  # c is smallest
                    val = c
                    while k < n3 and arr3[k] == val:
                        k += 1

        return answer if answer else [-1]
```

> Skipping duplicates during both the “equal” and “advance smallest” steps keeps the result distinct **without extra data structures**.

---

## B) Hash/Set intersection (simple to explain) — **O(n1+n2+n3) avg., O(n) space**

```python
class SolutionSet:
    def commonElements(self, arr1, arr2, arr3):
        """
        Uses sets for clarity (NOT the in-place DS-free variant).
        Time:  O(n1 + n2 + n3) on average
        Space: O(n1 + n2 + n3)
        """
        s1 = set(arr1)        # unique values from arr1
        s2 = set(arr2)        # unique values from arr2
        s3 = set(arr3)        # unique values from arr3
        common = sorted(s1 & s2 & s3)  # intersection, sorted
        return common if common else [-1]
```

**When to mention this:** as a quick alternative if the interviewer allows extra memory or when arrays may not be sorted.

---

## C) Binary Search approach (hybrid) — **O(n1 log n2 + n1 log n3)**

Scan the **shortest** array and binary-search each value in the other two arrays. De-duplicate as you go.

```python
import bisect

class SolutionBinarySearch:
    def commonElements(self, arr1, arr2, arr3):
        """
        Iterate the smallest array; binary-search in the other two.
        Time:  O(m log n + m log p) where m is smallest length
        Space: O(1) extra
        """
        arrays = sorted([arr1, arr2, arr3], key=len)  # smallest first
        a, b, c = arrays

        result = []
        prev = None  # to avoid duplicates from 'a'

        for x in a:
            if x == prev:  # skip dup in the driver array
                continue
            prev = x

            # binary-search x in b and c
            j = bisect.bisect_left(b, x)
            k = bisect.bisect_left(c, x)
            found_in_b = j < len(b) and b[j] == x
            found_in_c = k < len(c) and c[k] == x

            if found_in_b and found_in_c:
                result.append(x)

        return result if result else [-1]
```

---

# 4) Interview “fast recall” + expected Q&A

## 10-second memory hook

* **Mantra:** “**Three pointers, advance the smallest; when equal, record & skip dups.**”
* **Pocket code:**
  `while i<… and j<… and k<…:`
  `if a==b==c: add; i++; j++; k++; (skip dups)`
  `else: advance min(a,b,c) (skip its dups)`

## Likely follow-ups & crisp answers

**Q1. Why does advancing the smallest pointer work?**
Because arrays are sorted. If `a < b` or `c`, `a` can never match `b` and `c` at current positions; only by moving `a` forward can it possibly meet them.

**Q2. How do you ensure distinct output without extra DS?**
Whenever you add a value `x`, **skip all repeats of `x`** in **each** array. Also, whenever you advance the smallest value, skip its duplicates before the next comparison.

**Q3. Complexity?**
Three-pointer: **O(n1+n2+n3)** time, **O(1)** extra space.
Set-based: **O(n)** time avg., **O(n)** space.
Binary-search hybrid: **O(m log n + m log p)** time, **O(1)** space.

**Q4. What if arrays are not sorted?**
Either **sort them first** (then use three-pointer) → O(n log n), or use **hash sets** to intersect in O(n) expected time with extra space.

**Q5. Edge cases?**

* One or more arrays empty.
* Heavy duplicates (e.g., many repeated `1`s).
* No common elements → return `[-1]`.
* All elements common (e.g., identical arrays).

**Q6. Can we generalize to K sorted arrays?**
Yes: extend the idea by keeping a pointer per array and advancing the **minimum** each time, or repeatedly intersect two arrays at a time.

---

---

awesome — here are the last two parts for **Common Elements in 3 Sorted Arrays** 👇

---

# 5) Real-World Use Cases (short, interviewer-relatable)

* **Log/Telemetry Reconciliation across Systems**
  Find event IDs present in **all three** logs (e.g., client app, API gateway, DB write log) to isolate requests that fully traversed the stack.

* **Master Data Intersection**
  Identify customers/products that simultaneously exist in **CRM**, **Billing**, and **Support** systems for reliable cohort analyses.

* **Security/Access Audits**
  Compute users who appear in **HR roster**, **SSO directory**, and **privileged group** to validate least-privilege access.

* **ETL Data Quality Checks**
  Cross-verify keys present in **raw**, **staged**, and **modeled** tables to ensure pipeline completeness before downstream reporting.

These examples map cleanly to “intersection of multiple sorted (or sort-able) lists.”

---

# 6) Full Python Program

(includes: three-pointer optimal, set-based alternative, binary-search variant; prints outputs for sample inputs and uses `timeit` to measure runtime)

```python
from timeit import timeit
import bisect
from collections import Counter
from random import randint, seed

# ------------------------------------------------------------
# User function Template for python3 (MOST-EXPECTED IN INTERVIEWS)
# ------------------------------------------------------------
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        """
        Three-pointer linear scan on sorted arrays.
        Returns distinct common elements, or [-1] if none.

        Time:  O(n1 + n2 + n3)  -> single pass; each index advances monotonically
        Space: O(1) extra       -> indices + output list (ignoring output size)
        """
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        out = []

        while i < n1 and j < n2 and k < n3:
            a, b, c = arr1[i], arr2[j], arr3[k]  # O(1)

            if a == b == c:
                # Found a common value once (distinct output)
                out.append(a)  # O(1)

                # Skip duplicates of this value in all arrays; amortized O(#dups)
                val = a
                while i < n1 and arr1[i] == val:
                    i += 1
                while j < n2 and arr2[j] == val:
                    j += 1
                while k < n3 and arr3[k] == val:
                    k += 1

            else:
                # Advance the pointer with the smallest value to "catch up"
                smallest = min(a, b, c)
                if a == smallest:
                    # Skip duplicates of arr1[i] while moving forward
                    v = a
                    while i < n1 and arr1[i] == v:
                        i += 1
                elif b == smallest:
                    v = b
                    while j < n2 and arr2[j] == v:
                        j += 1
                else:
                    v = c
                    while k < n3 and arr3[k] == v:
                        k += 1

        return out if out else [-1]


# ------------------------------------------------------------
# Alternative 1: Set-based (simple, uses extra memory)
# ------------------------------------------------------------
class SolutionSet:
    def commonElements(self, arr1, arr2, arr3):
        """
        Set intersection of unique values (arrays need not be sorted).

        Time:  O(n1 + n2 + n3) average -> build three sets and intersect
        Space: O(n1 + n2 + n3)         -> store sets
        """
        s1, s2, s3 = set(arr1), set(arr2), set(arr3)  # O(n)
        inter = sorted(s1 & s2 & s3)                  # O(n log n) for sort
        return inter if inter else [-1]


# ------------------------------------------------------------
# Alternative 2: Binary-Search Hybrid
# ------------------------------------------------------------
class SolutionBinarySearch:
    def commonElements(self, arr1, arr2, arr3):
        """
        Iterate the smallest array; binary-search in the other two.

        Time:  O(m log n + m log p)  where m is the length of the smallest array
        Space: O(1) extra
        """
        arrays = sorted([arr1, arr2, arr3], key=len)  # O(1) comparisons
        a, b, c = arrays

        result = []
        prev = None
        for x in a:                 # O(m)
            if x == prev:           # de-dup driver array
                continue
            prev = x
            j = bisect.bisect_left(b, x)  # O(log n)
            k = bisect.bisect_left(c, x)  # O(log p)
            if j < len(b) and b[j] == x and k < len(c) and c[k] == x:
                result.append(x)
        return result if result else [-1]


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Common Elements in 3 Sorted Arrays ===\n")

    # ---- Inputs (from prompt + a few extras) ----
    samples = [
        ("Example 1",
         [1, 5, 10, 20, 40, 80],
         [6, 7, 20, 80, 100],
         [3, 4, 15, 20, 30, 70, 80, 120],
         [20, 80]),

        ("No Common",
         [1, 2, 3, 4, 5],
         [6, 7],
         [8, 9, 10],
         [-1]),

        ("Many Dups",
         [1, 1, 1, 2, 2, 2],
         [1, 1, 2, 2, 2],
         [1, 1, 1, 2, 2, 2, 2],
         [1, 2]),

        ("All Common",
         [2, 2, 3, 4, 5],
         [2, 3, 3, 4, 5, 5],
         [2, 2, 3, 4, 5, 5],
         [2, 3, 4, 5]),
    ]

    # Instantiate solutions
    sol_tp = Solution()
    sol_set = SolutionSet()
    sol_bs = SolutionBinarySearch()

    # ---- Print outputs for samples ----
    for name, a1, a2, a3, expected in samples:
        print(f"{name}:")
        print(f"  arr1 = {a1}")
        print(f"  arr2 = {a2}")
        print(f"  arr3 = {a3}")
        out_tp  = sol_tp.commonElements(a1, a2, a3)
        out_set = sol_set.commonElements(a1, a2, a3)
        out_bs  = sol_bs.commonElements(a1, a2, a3)
        print(f"  Three-Pointer:     {out_tp}")
        print(f"  Set Intersection:  {out_set}")
        print(f"  Binary-Search:     {out_bs}")
        print(f"  Expected:          {expected}")
        print(f"  Match? {out_tp == expected}\n")

    # ---- Timing on larger generated arrays ----
    seed(11)
    n1 = n2 = n3 = 50_000  # adjust as you like
    # Build non-decreasing arrays with overlaps and duplicates
    base1 = sorted(randint(-50_000, 50_000) for _ in range(n1))
    base2 = sorted(randint(-50_000, 50_000) for _ in range(n2))
    base3 = sorted(randint(-50_000, 50_000) for _ in range(n3))

    # Wrap callables for timeit (so it measures only the function body)
    t_tp  = timeit(lambda: sol_tp.commonElements(base1, base2, base3), number=3)
    t_set = timeit(lambda: sol_set.commonElements(base1, base2, base3), number=3)
    t_bs  = timeit(lambda: sol_bs.commonElements(base1, base2, base3), number=3)

    print("=== Timing (seconds) on ~50k each (3 runs) ===")
    print(f"Three-Pointer (O(n1+n2+n3)): {t_tp:.4f}s")
    print(f"Set-based     (O(n) avg.):   {t_set:.4f}s")
    print(f"Binary-Search (hybrid):      {t_bs:.4f}s")


if __name__ == "__main__":
    run_demo()
```

### What this program does

* Prints results for several **sample inputs** (including the problem’s examples) using all three approaches and shows whether they match the expected output.
* Generates larger random **sorted** arrays and measures runtimes with `timeit`, giving a practical feel for performance:

  * **Three-Pointer** is linear in total length and uses **O(1)** extra memory.
  * **Set-based** is often fast too but uses **extra memory**.
  * **Binary-Search** is useful when one array is **much smaller** than the others.
