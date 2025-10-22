
---

# 🧩 Array Duplicates

**Difficulty**: Easy
**Accuracy**: 18.95%
**Submissions**: 823K+
**Points**: 2
**Average Time**: 20m

---

## 📝 Problem Statement

Given an array `arr` of integers, find all the elements that occur more than once in the array. If no element repeats, return an empty array.

---

## 📥 Examples

### Example 1:

```
Input:  arr[] = [2, 3, 1, 2, 3]
Output: [2, 3]
Explanation: 2 and 3 occur more than once in the given array.
```

### Example 2:

```
Input:  arr[] = [0, 3, 1, 2]
Output: []
Explanation: There is no repeating element in the array, so the output is empty.
```

### Example 3:

```
Input:  arr[] = [2]
Output: []
Explanation: There is single element in the array. Therefore output is empty.
```

---

## 📌 Constraints

* $1 \leq \text{arr.size()} \leq 10^6$
* $0 \leq \text{arr[i]} \leq 10^6$

---

## ⚙️ Expected Complexities

* **Time Complexity**: $O(n)$
* **Auxiliary Space**: $O(n)$

---

## 🏷️ Company Tags

* Paytm
* Zoho
* Flipkart
* Amazon
* D-E Shaw
* Qualcomm

---

## 🧠 Topic Tags

* Arrays
* Data Structures

---

## 💼 Related Interview Experiences

* One97 Interview Experience Set 3 Backend Node JS Developer

---

---

Let’s make “Array Duplicates” crisp and interview-ready.

---

## 2) Intuition + step-by-step dry run

**Task:** return all elements that occur **more than once** in the array. If none repeat, return an empty array.
(Problem statement examples show returning duplicates **once each**, not with multiplicity.)

### Dry run

`arr = [2, 3, 1, 2, 3]`

* Use a frequency map (hash table).

  * See 2 → count 1
  * See 3 → count 1
  * See 1 → count 1
  * See 2 → count 2 → 2 is a duplicate
  * See 3 → count 2 → 3 is a duplicate
* Duplicates (unique) → `[2, 3]`.

If you need a deterministic order, return them **in ascending** or **first-appearance** order (state your choice).

---

## 3) Python solutions (multiple, interview-friendly)

All follow your required signature:

```python
class Solution:
    def findDuplicates(self, arr):
        # code here
```

### A) Hash map (Counter) — simplest & most common

```python
from collections import Counter

class Solution:
    def findDuplicates(self, arr):
        """
        Count each value, collect those with count > 1.
        Time  : O(n)
        Space : O(n)   (at most one entry per distinct value)
        Order : returns values in ascending order (change if needed)
        """
        freq = Counter(arr)                       # O(n)
        # choose output order; here ascending for determinism
        return sorted([x for x, c in freq.items() if c > 1])
```

### B) Sorting + single pass — no extra hash map

```python
class Solution:
    def findDuplicates(self, arr):
        """
        Sort then scan adjacent pairs.
        Time  : O(n log n)  (sort)
        Space : O(1) extra (ignoring sort's in-place/stack details)
        """
        if not arr: 
            return []
        arr.sort()                                 # O(n log n)
        dupes = []
        i = 1
        while i < len(arr):
            if arr[i] == arr[i-1]:
                # add once, then skip the whole equal block
                dupes.append(arr[i])
                val = arr[i]
                while i < len(arr) and arr[i] == val:
                    i += 1
            else:
                i += 1
        return dupes
```

### C) Set-based pass — minimal code, O(n) time

```python
class Solution:
    def findDuplicates(self, arr):
        """
        Track seen elements; when seen again, add to 'dupes'.
        Time  : O(n)
        Space : O(n)
        Order : returns in first-appearance order of the second time
        """
        seen, dupes = set(), set()
        for x in arr:
            if x in seen:
                dupes.add(x)         # set keeps each duplicate once
            else:
                seen.add(x)
        # choose order; here ascending
        return sorted(dupes)
```

### D) In-place index marking (only when values are in a tight index range)

> Use **only if** interviewer states values are in **1..n** (or **0..n-1**) and you may mutate the array. Otherwise this is **unsafe** for general ranges like up to 10^6.

```python
class Solution:
    def findDuplicates(self, arr):
        """
        Works ONLY if values are in 1..n (or adapt to 0..n-1).
        Marks presence by negating the value at the mapped index.
        Time  : O(n)
        Space : O(0) extra
        """
        n = len(arr)
        dupes = set()
        for i in range(n):
            idx = abs(arr[i]) - 1        # for 1..n
            if idx < 0 or idx >= n:
                # values not in 1..n -> bail out or choose another method
                # Fallback to hash if needed; but for the template, assume 1..n
                continue
            if arr[idx] < 0:
                dupes.add(idx + 1)
            else:
                arr[idx] = -arr[idx]
        # Optional: restore array by abs pass
        # for i in range(n): arr[i] = abs(arr[i])
        return sorted(dupes)
```

> In interviews: **ask** whether values are in 1..n and if in-place mutation is allowed before choosing D.

---

## 4) Interview quick-recall + Q&A

### 5-line pseudo-code (hash map version)

```
count = {}                           # value -> frequency
for x in arr: count[x] = count.get(x,0) + 1
ans = [x for x,c in count.items() if c > 1]
return sorted(ans)                   # or keep original encounter order
```

**Mnemonic:** **“Count → Filter (>1) → Return (ordered).”**

### Likely questions

* **Q:** Why choose a hash map?
  **A:** It’s O(n) time and simple; good when values are large/unbounded and we can’t index into an array directly.

* **Q:** Can you do it with O(1) extra space?
  **A:** Only if values are guaranteed in **1..n** (or 0..n-1) and we may mutate the array; then use **in-place index marking** (negation/offset trick).

* **Q:** How do you avoid listing an element multiple times?
  **A:** Use a `set` or, in the sort approach, add once and skip the whole equal block.

* **Q:** What order should duplicates be returned in?
  **A:** The prompt doesn’t force an order; I’ll return ascending (deterministic). I can change to input encounter order if required.

* **Q:** Space/time trade-offs?

  * **Hash map / set:** **O(n) time, O(n) space** (fastest without assumptions).
  * **Sort:** **O(n log n) time, O(1) extra space** (if in-place sort).
  * **In-place marking:** **O(n) time, O(1) space**, but requires tight value range and mutation.

---

### Pick the approach based on constraints

* Unknown / large value range → **Hash map (A)**.
* Memory tight or asked “no extra structure” → **Sort (B)**.
* Values 1..n and mutation allowed → **In-place (D)**.

That’s all you need to quickly explain, choose, and implement under interview time.

---

---

Great pick! Here are **real-world use cases** plus a **complete, runnable Python program** (multiple methods, inline complexity notes, sample I/O, and timings) for **Array Duplicates**.

---

## 5) Real-World Use Cases (easy to relate)

* **Data quality / dedup before joins**
  Find repeated IDs/emails/order numbers so you can clean rows or investigate upstream duplication.

* **Logging / telemetry sanity checks**
  Detect repeated event IDs or request IDs that should be unique (helps catch retries/loops).

* **Cache keys / API idempotency**
  Verify unexpected duplicate keys in a batch of ops that were assumed unique.

* **Security & fraud**
  Repeated device IDs / transaction IDs within a short window may indicate replay/fraud.

---

## 6) Full Program (3 approaches + timings)

* **Method A (default): Hash map/Counter** → **O(n) time, O(n) space**
* **Method B: Sorting** → **O(n log n) time, O(1) extra space**
* **Method C: In-place index marking** (only if values ∈ **1..n** & mutation allowed) → **O(n) time, O(1) space**

```python
#!/usr/bin/env python3
"""
Array Duplicates — return all values that occur more than once (each value once).
Includes:
  A) Counter/Hash (O(n), O(n))
  B) Sort + scan (O(n log n), O(1) extra)
  C) In-place marking for values in 1..n (O(n), O(1))  <-- only if that constraint holds

We demo each, print outputs, and time them.
"""

from collections import Counter
from time import perf_counter
import timeit
from typing import List


class Solution:
    # ---------- A) Counter / HashMap ----------
    def findDuplicates_hash(self, arr: List[int]) -> List[int]:
        """
        Time  : O(n)
        Space : O(n)
        Returns duplicates once, sorted ascending for deterministic output.
        """
        freq = Counter(arr)  # O(n)
        return sorted([x for x, c in freq.items() if c > 1])

    # ---------- B) Sorting + single pass ----------
    def findDuplicates_sort(self, arr: List[int]) -> List[int]:
        """
        Time  : O(n log n) due to sort
        Space : O(1) extra (ignoring sort's internal details)
        Strategy:
          - Sort array
          - Scan and add each duplicate value once (skip equal block)
        """
        if not arr:
            return []
        arr.sort()  # O(n log n)
        dupes = []
        i, n = 1, len(arr)
        while i < n:
            if arr[i] == arr[i - 1]:
                dupes.append(arr[i])
                val = arr[i]
                while i < n and arr[i] == val:
                    i += 1
            else:
                i += 1
        return dupes

    # ---------- C) In-place index marking (only if values in 1..n) ----------
    def findDuplicates_inplace(self, arr: List[int]) -> List[int]:
        """
        Time  : O(n)
        Space : O(1)
        PRECONDITIONS:
          - len(arr) = n
          - every value v satisfies 1 <= v <= n
          - allowed to mutate arr
        Idea:
          - For each value v, map to index v-1.
          - Flip sign at that index to mark seen; if already negative → duplicate.
        """
        n = len(arr)
        dupes = set()
        for i in range(n):
            v = abs(arr[i])
            if v < 1 or v > n:
                # If this precondition fails, abort or use hash method instead.
                # We'll quietly skip here; in production, raise or fallback.
                continue
            idx = v - 1
            if arr[idx] < 0:
                dupes.add(v)
            else:
                arr[idx] = -arr[idx]
        # Optional: restore array
        for i in range(n):
            arr[i] = abs(arr[i])
        return sorted(dupes)


# ----------------------------- Demo & Timings -----------------------------

def demo_case(arr: List[int]) -> None:
    sol = Solution()

    def run(label: str, fn, data: List[int]) -> None:
        a = data[:]  # copy so each method sees the same input
        t0 = perf_counter()
        out = fn(a)
        t1 = perf_counter()
        print(f"{label:<18} -> {out}   ({(t1 - t0) * 1e6:.1f} µs)")

    print(f"\nInput: {arr}")
    run("Hash O(n)", sol.findDuplicates_hash, arr)
    run("Sort O(n log n)", sol.findDuplicates_sort, arr)

    # In-place method only meaningful if values in 1..n
    if all(1 <= x <= len(arr) for x in arr):
        run("In-place O(n)", sol.findDuplicates_inplace, arr)
    else:
        print("In-place O(n)     -> (skipped: values not all in 1..n)")

def avg_time(arr: List[int], method: str, runs: int = 5) -> float:
    sol = Solution()
    if method == "hash":
        stmt = "sol.findDuplicates_hash(a[:])"
    elif method == "sort":
        stmt = "sol.findDuplicates_sort(a[:])"
    else:
        stmt = "sol.findDuplicates_inplace(a[:])"
    glb = {"sol": sol, "a": arr}
    return timeit.timeit(stmt, number=runs, globals=glb) / runs


if __name__ == "__main__":
    print("Array Duplicates — demo & timings")

    # Small examples (from style of prompt)
    demo_case([2, 3, 1, 2, 3])           # -> [2, 3]
    demo_case([0, 3, 1, 2])              # -> []
    demo_case([2])                       # -> []

    # Example for in-place-friendly range (values in 1..n)
    demo_case([1, 3, 2, 3, 5, 4, 2])     # -> [2, 3]

    # Larger random-ish test
    import random
    random.seed(7)
    n = 200_000
    # create some duplicates deliberately
    base = [random.randint(0, 300_000) for _ in range(n)]
    base[1000:1010] = [42] * 10
    base[50000:50040] = [777777] * 40

    print("\nAverage times on large input (n=200k, 3 runs):")
    print(f"  hash : {avg_time(base, 'hash', 3):.4f} s")
    print(f"  sort : {avg_time(base, 'sort', 3):.4f} s")
    # in-place needs values in 1..n, so we skip on this arbitrary large array

    print("\nComplexity summary:")
    print("  Hash      : Time O(n),       Space O(n)")
    print("  Sort      : Time O(n log n), Space O(1) extra")
    print("  In-place  : Time O(n),       Space O(1)  (requires values in 1..n & mutation)")
```

### Sample output (illustrative)

```
Array Duplicates — demo & timings
Input: [2, 3, 1, 2, 3]
Hash O(n)           -> [2, 3]   (75.1 µs)
Sort O(n log n)     -> [2, 3]   (85.3 µs)
In-place O(n)       -> (skipped: values not all in 1..n)

Input: [1, 3, 2, 3, 5, 4, 2]
Hash O(n)           -> [2, 3]   (78.2 µs)
Sort O(n log n)     -> [2, 3]   (91.7 µs)
In-place O(n)       -> [2, 3]   (63.9 µs)

Average times on large input (n=200k, 3 runs):
  hash : 0.08xx s
  sort : 0.13xx s
```

---

### What to say in the interview (quick)

> “I’ll use a **hash map** to count occurrences in **O(n)** and collect values with count > 1 (return them once, sorted for determinism).
> If memory is tight, I can **sort** and scan in **O(n log n)** and **O(1)** extra space.
> If values are guaranteed in **1..n** and mutation is allowed, I can do **in-place index marking** in **O(n)** time and **O(1)** space.”

