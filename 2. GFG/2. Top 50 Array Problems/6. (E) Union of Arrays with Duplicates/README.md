# Union of Arrays with Duplicates

**Difficulty:** Easy
**Accuracy:** 42.22%
**Submissions:** 460K+
**Points:** 2
**Average Time:** 10m

---

## Problem Statement

You are given two arrays `a[]` and `b[]`, return the **Union** of both the arrays in **any order**.

The **Union** of two arrays is a collection of **all distinct elements** present in either of the arrays. If an element appears more than once in one or both arrays, it should be included **only once** in the result.

**Notes:**

* Elements of `a[]` and `b[]` are **not necessarily distinct**.
* You can return the union in any order, but the driver code will print the result in **sorted order** only.

---

## Examples

### Example 1

**Input:** `a[] = [1, 2, 3, 2, 1],  b[] = [3, 2, 2, 3, 3, 2]`
**Output:** `[1, 2, 3]`
**Explanation:** Union set of both arrays is `1, 2, 3`.

### Example 2

**Input:** `a[] = [1, 2, 3],  b[] = [4, 5, 6]`
**Output:** `[1, 2, 3, 4, 5, 6]`
**Explanation:** Union set of both arrays will be `1, 2, 3, 4, 5, 6`.

### Example 3

**Input:** `a[] = [1, 2, 1, 1, 2],  b[] = [2, 2, 1, 2, 1]`
**Output:** `[1, 2]`
**Explanation:** Union set of both arrays will be `1` and `2`.

---

## Constraints

* `1 ≤ a.size(), b.size() ≤ 10^6`
* `0 ≤ a[i], b[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n + m)`
* **Auxiliary Space:** `O(n + m)`

---

## Company Tags

Zoho • Rockstand

---

## Topic Tags

* Hash
* Data Structures
* Algorithms
* Arrays

---

## Related Articles

* [Union Of Two Arrays](https://www.geeksforgeeks.org/Union%20of%20Two%20Arrays/)

---

---
Awesome — let’s lock in the **correct approach** and make it interview-ready.

---

## 2) Intuition + step-by-step dry run

**Goal:** Return the **union** of two arrays `a` and `b`: every distinct value should appear **exactly once** (order usually doesn’t matter; most judges finally print in sorted order).

### Why the two-pointer method?

If we **sort** both arrays first, we can **merge** them like the merge step of merge-sort while skipping duplicates. This is linear after sorting and needs only a few pointers.

### Dry run on the failing case

```
a = [10, 2, 6, 3]
b = [2, 10, 10, 8]
```

1. Sort copies:
   `a -> [2, 3, 6, 10]`
   `b -> [2, 8, 10, 10]`

2. Merge with de-dup:

* `i=0 (2), j=0 (2)` → equal → take `2`, advance both → res = `[2]`
* `i=1 (3), j=1 (8)` → `3<8` → take `3` → res = `[2,3]`
* `i=2 (6), j=1 (8)` → `6<8` → take `6` → res = `[2,3,6]`
* `i=3 (10), j=1 (8)` → `8<10` → take `8` → res = `[2,3,6,8]`
* `i=3 (10), j=2 (10)` → equal → take `10`, advance both → res = `[2,3,6,8,10]`
* drain: `b` still has `10` but equals `last=10` → skip

**Final union:** `[2, 3, 6, 8, 10]` ✅

Edge notes:

* If one array ends, just **drain** the other while skipping same-as-last.
* If inputs are already sorted, skip the sorting step (still correct).

---

## 3) Python solutions (what interviewers expect)

### A) Two-pointer on sorted arrays (most robust for judges)

```python
class Solution:    
    def findUnion(self, a, b):
        """
        Two-pointer union:
          - Sort both arrays (if not already sorted).
          - Merge while skipping duplicates via 'last'.
        Time:  O((n+m) log(n+m)) if sorting;  O(n+m) if pre-sorted
        Space: O(1) extra (besides output)
        """
        # If inputs aren't guaranteed sorted, sort copies (not in-place to be safe)
        a = sorted(a)
        b = sorted(b)

        i = j = 0
        res = []
        last = None  # last value appended to res

        # Merge step with de-duplication
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                x = a[i]; i += 1
            elif b[j] < a[i]:
                x = b[j]; j += 1
            else:  # equal
                x = a[i]; i += 1; j += 1
            if x != last:           # append only if it's a new value
                res.append(x)
                last = x

        # Drain any remaining elements (still skipping duplicates)
        while i < len(a):
            if a[i] != last:
                res.append(a[i]); last = a[i]
            i += 1

        while j < len(b):
            if b[j] != last:
                res.append(b[j]); last = b[j]
            j += 1

        return res
```

### B) Hash-set union (simplest when order doesn’t matter)

```python
class Solution:
    def findUnion(self, a, b):
        """
        Use a set to dedupe and return sorted union for determinism.
        Time:  O(n + m) average (hashing)
        Space: O(n + m)
        """
        return sorted(set(a) | set(b))
```

### C) Counting / bitset (when values are small non-negative, per constraints `0..1e5`)

This avoids hashing overhead and keeps `O(n+m)` time, `O(U)` space where `U = maxVal+1`.

```python
class Solution:
    def findUnion(self, a, b):
        """
        Counting-based union for bounded non-negative integers.
        Time:  O(n + m + U), Space: O(U)
        """
        if not a and not b: 
            return []

        maxv = 10**5  # from constraints; or compute max(a+b) if desired
        seen = [False] * (maxv + 1)

        for x in a:
            seen[x] = True
        for x in b:
            seen[x] = True

        # Return ascending
        return [v for v, flag in enumerate(seen) if flag]
```

> In most interviews, propose **A** (if they require sorted output) or **B** (quickest to code). Mention **C** only if the value range constraint is relevant.

---

## 4) Likely interviewer Q\&A

**Q1. Why did your earlier attempt fail with `[2, 2, 3, 6, 8, 10, 10]`?**
Because that’s **not a union**—it still has duplicates (`2` and `10`). Union must include **each value once**.

**Q2. Complexity of each method?**

* **Two-pointer (sorted):** `O((n+m) log(n+m))` with sorting; `O(n+m)` if already sorted. Space `O(1)`.
* **Set union:** `O(n+m)` average time, `O(n+m)` space.
* **Counting:** `O(n+m+U)` time, `O(U)` space.

**Q3. Which would you choose in production?**

* If arrays are already sorted or must be returned sorted **without extra memory**, choose **two-pointer**.
* If not sorted and memory is fine, **set union** is simplest and fastest to implement.
* If values are bounded non-negative and performance matters, **counting** can be fastest.

**Q4. How do you preserve “first-seen order” instead of sorted?**
Track a `seen` set and build the output by scanning `a` then `b`, appending only when a value is first encountered.

**Q5. Any pitfalls?**

* Forgetting to dedupe while merging.
* Returning unsorted union when the judge expects sorted.
* Using `set(a+b)` in languages that don’t dedupe cross-array correctly (Python is fine, but always ensure it’s a true union).

---

---

Done! I executed a **full inline Python program** that:

* Implements `findUnion` using the **two-pointer** approach (sort + merge with de-dup) and also includes two alternatives: **set union** and **counting**.
* Prints **inputs and outputs** for sample cases, your previously failing case, edge cases, and a **large benchmark**.
* Shows the **TOTAL MAIN RUNTIME** using `timeit`.

```python

# Re-run to display outputs after the state reset
from typing import List
import random, timeit

class Solution:    
    def findUnion(self, a: List[int], b: List[int]) -> List[int]:
        a = sorted(a)
        b = sorted(b)
        i = j = 0
        res = []
        last = None
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                x = a[i]; i += 1
            elif b[j] < a[i]:
                x = b[j]; j += 1
            else:
                x = a[i]; i += 1; j += 1
            if x != last:
                res.append(x); last = x
        while i < len(a):
            if a[i] != last:
                res.append(a[i]); last = a[i]
            i += 1
        while j < len(b):
            if b[j] != last:
                res.append(b[j]); last = b[j]
            j += 1
        return res

    def findUnion_set(self, a: List[int], b: List[int]) -> List[int]:
        return sorted(set(a) | set(b))

    def findUnion_counting(self, a: List[int], b: List[int], max_value: int = 10**5) -> List[int]:
        seen = [False]*(max_value+1)
        for x in a: seen[x] = True
        for x in b: seen[x] = True
        return [v for v, flag in enumerate(seen) if flag]

def main():
    sol = Solution()
    print("=== Union of Two Arrays with Duplicates — Demo & Timing ===")
    a1 = [1, 2, 3, 2, 1]
    b1 = [3, 2, 2, 3, 3, 2]
    t0 = timeit.default_timer()
    out1 = sol.findUnion(a1, b1)
    t1 = timeit.default_timer()
    print("\nInput 1:")
    print("a =", a1)
    print("b =", b1)
    print("Output (two-pointer):", out1, f"   time={(t1 - t0):.6f}s")
    a2 = [10, 2, 6, 3]
    b2 = [2, 10, 10, 8]
    t0 = timeit.default_timer()
    out2 = sol.findUnion(a2, b2)
    t1 = timeit.default_timer()
    print("\nInput 2 (previously failing):")
    print("a =", a2)
    print("b =", b2)
    print("Output (two-pointer):", out2, f"   time={(t1 - t0):.6f}s")
    print("\nCross-check for Input 2:")
    print("Output (set union):     ", sol.findUnion_set(a2, b2))
    print("Output (counting):      ", sol.findUnion_counting(a2, b2, max_value=max(a2+b2)))
    e1_a, e1_b = [], [5,5,5]
    e2_a, e2_b = [7,7,7], []
    e3_a, e3_b = [1], [1]
    print("\nEdge 1 (empty + non-empty):", sol.findUnion(e1_a, e1_b))
    print("Edge 2 (non-empty + empty):", sol.findUnion(e2_a, e2_b))
    print("Edge 3 (all same value):   ", sol.findUnion(e3_a, e3_b))
    n = 200_000; m = 200_000
    rand_a = [random.randint(0, 100_000) for _ in range(n)]
    rand_b = [random.randint(0, 100_000) for _ in range(m)]
    t0 = timeit.default_timer()
    out_big = sol.findUnion(rand_a, rand_b)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}, m={m}: union size={len(out_big)}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-impact)

* **Log aggregation / analytics:** Merge distinct event IDs from multiple sources to build de-duplicated dashboards.
* **Permissions / ACLs:** Compute the union of allowed actions from multiple roles for a user.
* **Search / recommendations:** Union of item IDs returned from several models or shards before ranking.
* **Data import / ETL:** De-duplicate keys gathered from several files/streams before joins.
* **Monitoring / alerting:** Combine unique incident codes from multiple systems to avoid duplicate alerts.
