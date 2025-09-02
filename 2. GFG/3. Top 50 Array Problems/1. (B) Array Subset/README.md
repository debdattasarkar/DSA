
---

# Array Subset

* **Difficulty:** Basic
* **Accuracy:** 44.05%
* **Submissions:** 446K+
* **Points:** 1
* **Average Time:** 20m

## Problem

Given two arrays **a\[]** and **b\[]**, your task is to determine whether **b\[]** is a subset of **a\[]**.

## Examples

**Example 1**

```
Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
```

**Example 2**

```
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
```

**Example 3**

```
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
```

## Constraints

* 1 <= a.size(), b.size() <= 10^5
* 1 <= a\[i], b\[i] <= 10^6

## Expected Complexities

* **Time Complexity:** O(n + m)
* **Auxiliary Space:** O(n)

## Company Tags

Accolite, Qualcomm, GE

## Topic Tags

Arrays, Searching, Hash, Binary Search, Data Structures, Algorithms

## Related Interview Experiences

* Qualcomm Interview Experience Set 11 Campus
* Ge Interview Experience Set 5 Campus Ge Digital

## Related Articles

* Find Whether An Array Is Subset Of Another Array Set 1


---

---

Awesome—let’s nail this like a GFG interview prompt.

# 2) Problem explanation + step-by-step dry run

**Task (as on the prompt):** check whether **b\[] is a subset of a\[]** (including multiplicities—i.e., duplicates matter).
If an element appears `k` times in `b`, it must appear **at least** `k` times in `a`.

### Why sets alone are not enough

A plain `set(b) ⊆ set(a)` ignores counts.
Example: `a = [1,1]`, `b = [1,1,1]` → sets would say subset, but it’s **false** under multiset rules.

---

## Dry run 1 (Example 1)

```
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
```

**Counting in `a`:**

* 11:1, 7:2, 1:1, 13:1, 21:1, 3:2

Process elements of `b` one by one and decrement the count in `a`:

* Need 11 → `cnt[11]` = 1 → use it → now 0
* Need 3  → `cnt[3]`  = 2 → use it → now 1
* Need 7  → `cnt[7]`  = 2 → use it → now 1
* Need 1  → `cnt[1]`  = 1 → use it → now 0
* Need 7  → `cnt[7]`  = 1 → use it → now 0

All elements of `b` found → **true**.

---

## Dry run 2 (Example 3)

```
a = [10, 5, 2, 23, 19]
b = [19, 5, 3]
```

**Counting in `a`:**

* 10:1, 5:1, 2:1, 23:1, 19:1

Process `b`:

* Need 19 → `cnt[19]` = 1 → use it → now 0
* Need 5  → `cnt[5]`  = 1 → use it → now 0
* Need 3  → `cnt[3]`  **not present / 0** → fail early → **false**.

---

# 3) Python solutions (brute → optimal), interview-style

> **Note:** The original GFG text says “check if **b** is a subset of **a**.”
> The template comment says “check if **a** is a subset of **b**.”
> Below code **follows the prompt**: we check **b ⊆ a**.

---

## A) Optimal & most common (Hash/Counter) — **O(n + m) time, O(n) space**

```python
#User function Template for python3
from collections import Counter

class Solution:
    # Function to check if b is a subset of a (multiplicity-aware).
    def isSubset(self, a, b):
        # Early pruning: if b has more elements than a, it can't be a multiset subset.
        if len(b) > len(a):
            return False

        # Count frequencies of elements in 'a'
        freq = Counter(a)  # O(n)

        # For every element in 'b', consume one count from 'a'
        for x in b:        # O(m)
            if freq[x] <= 0:
                # 'x' missing or not enough occurrences left in 'a'
                return False
            freq[x] -= 1

        # All elements of 'b' were matched
        return True
```

**Why interviewers like it**

* Linear time, linear auxiliary space.
* Correct for duplicates.
* Easy to reason about; short-circuits early on failure.

---

### A-alt) Pythonic one-liner with `Counter` subtraction (same complexity)

```python
#User function Template for python3
from collections import Counter

class Solution:
    def isSubset(self, a, b):
        # Counter subtraction keeps only positive deficits.
        # If any count in b exceeds that in a, (Counter(b) - Counter(a)) will be non-empty.
        return not (Counter(b) - Counter(a))
```

**Talking point:** `Counter(b) - Counter(a)` drops zeros/negatives and keeps only missing amounts; empty ⇒ subset.

---

## B) Sorting + Two Pointers — **O((n + m) log(n + m)) time, O(1) extra space**

Useful when you want to save hash memory or when arrays are nearly sorted.

```python
#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        # Sort both. Sorting cost dominates.
        a.sort()
        b.sort()

        i = j = 0
        n, m = len(a), len(b)

        # Walk both arrays
        while i < n and j < m:
            if a[i] == b[j]:
                # Found one occurrence for b[j]; move both
                i += 1
                j += 1
            elif a[i] < b[j]:
                # Current a[i] is too small; skip it
                i += 1
            else:
                # a[i] > b[j] => the needed b[j] doesn't exist in 'a'
                return False

        # If we've matched all of b, it's a subset
        return j == m
```

**Why it works for duplicates:**
Matching advances both pointers only when equal. Multiple equal values in `b` require multiple equal matches in `a`.

---

## C) Simple Brute Force (visited flags) — **O(n·m) time, O(n) space**

Good to describe first in interviews, then improve.

```python
#User function Template for python3

class Solution:
    def isSubset(self, a, b):
        n = len(a)
        used = [False] * n  # mark matched positions in 'a' to respect multiplicity

        for val in b:  # For each value we need
            found = False
            # Scan 'a' to find an unused equal value
            for i in range(n):
                if not used[i] and a[i] == val:
                    used[i] = True
                    found = True
                    break
            if not found:
                return False  # couldn't find a required occurrence

        return True
```

**When to mention it:** Baseline correctness; then discuss why it times out at 1e5 scale and pivot to A or B.

---

### Complexity Summary

* **Counter (A / A-alt):** Time `O(n + m)`, Space `O(n)`
* **Sort + two pointers (B):** Time `O((n + m) log(n + m))`, Space `O(1)` extra
* **Brute (C):** Time `O(n·m)`, Space `O(n)`

---

# 4) Interviewer-style Q\&A

**Q1. Why can’t we just do `set(b) <= set(a)`?**
**A.** That ignores multiplicities. If `b` requires 3 copies of `x` and `a` has only 1, sets still say subset. We need multiset logic (counts).

**Q2. Which approach is optimal here and why?**
**A.** Hash counting using `Counter` → **O(n + m)** time, **O(n)** space, and it respects duplicates naturally. It also short-circuits when a deficit appears.

**Q3. When would you prefer sorting + two pointers?**
**A.** If memory is tight or arrays are read-only in a system that discourages hashing overhead. Sorting gives a clean **O(1)** extra-space scan (beyond sort’s stack), with predictable cache-friendly sequential access.

**Q4. How do you prove correctness for the two-pointer method with duplicates?**
**A.** After sorting, equal values are contiguous. We advance both pointers only on equality, so each required instance in `b` is matched with a distinct instance in `a`. If at any point `a[i] > b[j]`, the smallest available `a` element already exceeds `b[j]` ⇒ `b[j]` cannot be present → fail.

**Q5. Any early exits or quick checks you’d add?**
**A.** Yes: if `len(b) > len(a)` return `False` (multiset logic). During counting, return immediately on any missing/zero count. In two-pointer, return `False` when `a[i] > b[j]`.

**Q6. What about negatives, zeros, or large values?**
**A.** All methods handle any hashable integers. Constraints say values up to `1e6`, but the algorithms don’t rely on that.

**Q7. Could we do `O(m log n)` without extra space?**
**A.** Yes: sort `a` only and for each `b[j]` binary-search in `a` for the next unused position (track a moving lower bound). But managing duplicates cleanly is trickier than the two-pointer variant that sorts both.

**Q8. What’s the behavior for empty arrays?**
**A.** If `b` is empty, it’s vacuously a subset → `True`. If `a` is empty but `b` isn’t → `False`.

**Q9. How would you handle streaming/huge arrays?**
**A.** Maintain a rolling count for `a` from chunks and decrement for `b`. If `b` is also streaming, buffer its counts first or process in passes. If memory is a concern, sort externally and then use the two-pointer merge-like scan.

**Q10. Pitfalls you’d warn about in Python?**
**A.** Using sets and forgetting multiplicities; modifying lists while iterating; forgetting early exits; and not considering `len(b) > len(a)` quick fail.

---

---

Got it—here’s a full, interview-ready program plus timing, with heavy inline complexity notes, and then a few high-impact real-world uses.

---

## Full Python program (with timing + inline complexities)

```python
# ------------------------------------------------------------
# Array Subset (b ⊆ a, multiplicity-aware)
# ------------------------------------------------------------
# We check whether every element in b occurs in a at least as
# many times (i.e., duplicates matter).
#
# This script includes:
#   - A Solution class with:
#       * isSubset(...)  -> Optimal Counter-based solution
#       * isSubset_sort(...) -> Sorting + two-pointers alternative
#       * isSubset_bruteforce(...) -> Simple baseline (for learning)
#   - A main_run() that executes multiple test cases.
#   - A timeit measurement for the full run.
#   - Printed inputs and outputs for clarity.
# ------------------------------------------------------------

from collections import Counter
import timeit

# -----------------------
# User function Template
# -----------------------
class Solution:
    # Function to check if b is a subset of a (multiplicity-aware).
    # NOTE: The original prompt says "b[] is a subset of a[]".
    def isSubset(self, a, b):
        """
        Optimal: Hash counting (Counter)
        Time:
          - Build Counter(a): O(n)
          - Scan b and decrement: O(m)
          => Total O(n + m)
        Space:
          - Counter stores up to unique elements of a: O(u) <= O(n)
        """
        # Quick fail: if b is longer than a, it can't be a multiset subset.
        # Time: O(1) | Space: O(1)
        if len(b) > len(a):
            return False

        # Build frequency map of array a
        # Time: O(n) to count all elements
        # Space: O(u) for unique elements
        freq = Counter(a)

        # For each element in b, ensure we have at least one in freq
        # Time: O(m) across the loop
        # Space: O(1) extra
        for x in b:
            if freq[x] <= 0:
                return False
            freq[x] -= 1

        # If we never failed, b is a subset of a
        # Time: O(1) | Space: O(1)
        return True

    # ---- Alternative 1: Sorting + Two Pointers ----
    def isSubset_sort(self, a, b):
        """
        Sorting + two pointers
        Time:
          - sort(a):  O(n log n)
          - sort(b):  O(m log m)
          - merge-like scan: O(n + m)
          => Total O((n + m) log (n + m))
        Space:
          - Sorting in Python Timsort uses O(log n + log m) stack (ignorable),
            otherwise O(1) extra outside of the sorted arrays.
        """
        a = sorted(a)  # Time: O(n log n) | Space: O(1) extra beyond in-place/stack
        b = sorted(b)  # Time: O(m log m) | Space: O(1) extra

        i = j = 0
        n, m = len(a), len(b)

        # Merge-scan to match every b[j] in a
        # Time: O(n + m) | Space: O(1)
        while i < n and j < m:
            if a[i] == b[j]:
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                # a[i] > b[j] => smallest remaining a is already too big,
                # so b[j] doesn't exist in a.
                return False

        return j == m

    # ---- Alternative 2: Simple Brute Force (educational) ----
    def isSubset_bruteforce(self, a, b):
        """
        Brute force with 'used' flags.
        Time:
          - For each element of b (m), scan up to n in a => O(n * m)
        Space:
          - 'used' array of size n => O(n)
        """
        n = len(a)
        used = [False] * n  # mark matched positions in a

        for val in b:  # O(m)
            found = False
            for i in range(n):  # O(n) per val
                if not used[i] and a[i] == val:
                    used[i] = True
                    found = True
                    break
            if not found:
                return False
        return True


# -----------------------
# Demonstration + Timing
# -----------------------

def main_run():
    """
    Runs multiple test cases and prints inputs/outputs.

    Complexity of this driver:
      - Calls the function on each test: dominated by the chosen algorithm inside.
      - Printing and formatting are O(total input size).
    """
    sol = Solution()

    # Test cases (input values)
    tests = [
        # Example 1
        {
            "a": [11, 7, 1, 13, 21, 3, 7, 3],
            "b": [11, 3, 7, 1, 7],
            "expected": True
        },
        # Example 2
        {
            "a": [1, 2, 3, 4, 4, 5, 6],
            "b": [1, 2, 4],
            "expected": True
        },
        # Example 3
        {
            "a": [10, 5, 2, 23, 19],
            "b": [19, 5, 3],
            "expected": False
        },
        # Duplicate-sensitivity demo
        {
            "a": [1, 1],
            "b": [1, 1, 1],
            "expected": False
        },
    ]

    print("=== Checking if b is a subset of a (multiplicity-aware) ===\n")
    for idx, t in enumerate(tests, 1):
        a, b, exp = t["a"], t["b"], t["expected"]

        # Choose the method you want to time/verify:
        #   sol.isSubset(...)        -> Counter-based (Optimal)
        #   sol.isSubset_sort(...)   -> Sorting + two-pointers
        #   sol.isSubset_bruteforce(...)-> Brute force
        ans = sol.isSubset(a, b)

        print(f"Test {idx}:")
        print(f"  a = {a}")
        print(f"  b = {b}")
        print(f"  Output  : {str(ans).lower()}")
        print(f"  Expected: {str(exp).lower()}")
        print("  Result  :", "PASS ✅" if ans == exp else "FAIL ❌", end="\n\n")


# Time the *entire* program run (the main_run call) once.
# timeit.timeit executes the callable and returns the total seconds for 'number' runs.
total_seconds = timeit.timeit(stmt=main_run, number=1)
print(f"\nTotal runtime (timeit, 1 run): {total_seconds * 1000:.3f} ms")
```

**How to run:** copy the whole script into a file (e.g., `subset_check.py`) and run it.
It will print each test’s input and output, plus a single `timeit` runtime for the full run.

---

## Real-World Use Cases (a few important ones)

* **Access control / permissions:** Ensure all required user permissions (`b`) are present in an account’s permission set (`a`), including counts/quotas when needed.
* **Inventory / order fulfillment:** Check if requested items (with quantities) in an order (`b`) are fully available in warehouse stock (`a`).
* **Dependency validation:** Confirm an environment’s installed packages (`a`) satisfy a job’s or service’s dependency list (`b`) including repeated resources or versions.
* **Data reconciliation:** Verify a daily subset of transactions (`b`) exists in the master ledger (`a`) without losing duplicate entries.
