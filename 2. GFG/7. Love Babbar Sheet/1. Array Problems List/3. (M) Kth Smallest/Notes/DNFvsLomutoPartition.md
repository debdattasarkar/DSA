
```python
# User function Template for python3
import random
import heapq
from typing import List

class Solution:
    def kthSmallest_DNF(self, arr: List[int], k: int) -> int:
        """
        Version 1 = 3-way (Dutch National Flag) partition.
        Quickselect with 3-way partition (Dutch National Flag).
        Average time: O(n), worst-case: O(n^2) -- mitigated by random pivot
        Space: O(1) extra (in-place)
        """
        n = len(arr)
        if not (1 <= k <= n):
            raise ValueError("k out of bounds")

        # We want 0-based index
        target = k - 1
        low, high = 0, n - 1

        while True:
            if low == high:
                return arr[low]

            # --- choose a random pivot to avoid adversarial worst cases
            pivot_idx = random.randint(low, high)
            pivot = arr[pivot_idx]

            # 3-way partition around pivot: < pivot | == pivot | > pivot
            left, i, right = low, low, high
            while i <= right:
                if arr[i] < pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1; i += 1
                elif arr[i] > pivot:
                    arr[i], arr[right] = arr[right], arr[i]
                    right -= 1
                else:  # equal
                    i += 1

            # Now:
            # arr[low:left]   < pivot
            # arr[left:right+1] == pivot
            # arr[right+1:high+1] > pivot

            if target < left:
                high = left - 1                 # go left
            elif target > right:
                low = right + 1                 # go right
            else:
                return arr[target]          # inside the equal block → done

    # ---------- Primary: Quickselect (average O(n), in-place O(1) space) ----------
    def kthSmallest_LP(self, arr: List[int], k: int) -> int:
        """
        Version 2 = 2-way (Lomuto) partition.
        Randomized Quickselect to find k-th smallest (1-indexed).
        Time : Average O(n), Worst O(n^2) (mitigated by random pivot)
        Space: O(1) auxiliary (iterative)
        """
        if not arr or k < 1 or k > len(arr):
            raise ValueError("k out of bounds")

        target_index = k - 1            # O(1)
        left, right = 0, len(arr) - 1   # O(1)

        # Iterative quickselect keeps memory O(1)
        while left <= right:            # Expected O(n) total work
            # --- choose a random pivot to avoid adversarial inputs (O(1)) ---
            pivot_index = random.randint(left, right)
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # move pivot to end (O(1))

            # --- Lomuto partition around pivot_value in one linear pass ---
            pivot_value = arr[right]    # O(1)
            store_index = left          # where next smaller element goes
            for i in range(left, right):           # O(right-left+1) per iteration
                if arr[i] < pivot_value:
                    arr[i], arr[store_index] = arr[store_index], arr[i]  # O(1)
                    store_index += 1

            # put pivot into its final sorted location
            arr[store_index], arr[right] = arr[right], arr[store_index]  # O(1)

            # --- Decide which side to continue searching (O(1)) ---
            if store_index == target_index:
                return arr[store_index]
            elif store_index < target_index:
                left = store_index + 1
            else:
                right = store_index - 1

        # If k valid, we must have returned
        raise RuntimeError("Unexpected state in quickselect")

```


Both are **Quickselect**, but they differ in how they **partition** the array around the pivot.

---

## TL;DR

* **Version 1 = 3-way (Dutch National Flag) partition.**
  Keeps three zones: `< pivot | == pivot | > pivot`.
  **Best when duplicates are common** — if `k` falls inside the `==` block you return immediately, and the next search interval can shrink a lot faster.

* **Version 2 = 2-way (Lomuto) partition.**
  Keeps two zones: `< pivot | >= pivot` (pivot ends up at `store_index`).
  **Simpler** and often a hair faster on distinct data, but can do extra work when there are many duplicates because it treats `== pivot` as part of the “right” side and keeps partitioning them again.

Both: expected **O(n)** time, worst **O(n²)** (mitigated by random pivot), **O(1)** extra space.

---

## What’s different, precisely?

### 1) Partition scheme & invariants

**3-way DNF (Version 1)**

* Indices: `left, i, right`.
* Invariant while scanning `i`:

  * `arr[low:left]   <  pivot`
  * `arr[left:i]     == pivot`
  * `arr[i:right+1]  unknown`
  * `arr[right+1:hi] >  pivot`
* After one pass you have a **contiguous equal block** `[left … right]`.
* Decision:

  * if `target < left` → search left side
  * if `target > right` → search right side
  * else target lies in the equal block → **return immediately**.

**Lomuto (Version 2)**

* Moves pivot to end, scans once, places pivot at `store_index`.
* Invariant during scan:

  * `arr[left:store_index] < pivot`
  * `arr[store_index:i]    >= pivot` (not explicitly separated)
* After partition, only **one pivot position** is fixed.
* Decision by comparing `store_index` with `target_index`.

### 2) Handling duplicates

* **3-way**: collapses *all* `== pivot` values in one go. With many repeats, the search space can shrink from `n` to **0 instantly** if `k` falls inside that equal block. This keeps the expected O(n) very robust.
* **Lomuto**: all `== pivot` end up on the “right” side (with `>= pivot`), so if there are lots of equal keys you may keep repartitioning them — more iterations than necessary.

### 3) Swaps / comparisons

* **3-way**: can do more swaps per element (because of the `right` boundary swaps when `arr[i] > pivot`), but it **avoids repeated passes** over equal keys.
* **Lomuto**: code is short; one forward pass + 1 final swap. Often slightly faster on **distinct** data due to fewer branches.

### 4) Pivot placement

* **3-way**: pivot value is just a **value**; it’s not pinned to a specific index (it can move as we swap). That’s OK because all comparisons are with the **value**.
* **Lomuto**: explicitly puts the pivot at the end, then returns it to its final sorted index.

### 5) Termination condition

* **3-way**: if `target` falls inside `[left … right]`, return immediately; otherwise narrow to one side.
* **Lomuto**: stop when `store_index == target_index`; otherwise narrow to one side.

---

## Which should I choose?

* Expect **many duplicates** or unknown distribution → **use 3-way DNF** (Version 1).
  More robust; fewer iterations when lots of equal values.

* Expect **mostly distinct values** and want simplest code → **use Lomuto** (Version 2).
  Very readable; often a tiny bit faster in practice on distinct data.

In both, keep **random pivots** (or median-of-three) to avoid adversarial worst cases.

---

## Tiny example where 3-way wins big

```
arr = [5,5,5,5,5,5,5,5,5,5], k = 7
```

* **3-way**: One pass → equal block is the whole array → target is inside → **return in O(n)** with **1 iteration**.
* **Lomuto**: Still O(n), but you keep picking a pivot and partitioning; you’ll land the pivot somewhere, then loop termination hits when `store_index == target_index`. No big-O difference, but more book-keeping and iterations than the 3-way early exit.

---

## Bottom line

* **Version 1 (3-way)** = better handling of duplicates, more robust partitioning; great for general use.
* **Version 2 (Lomuto)** = simpler, concise, perfectly fine for distinct data; still average O(n).

If an interviewer asks which you’d ship:

> “I’d choose 3-way partition for robustness with duplicates; keep randomized pivot. If performance profiling on mostly distinct data suggests Lomuto is faster in our workload, I’d switch — both remain average O(n) and O(1) extra space.”



Interview-ready comparison of **Dutch National Flag (DNF) 3-way partition** vs **Lomuto 2-way partition**—what each guarantees, how they behave (especially with duplicates), and when to use which.

---

# TL;DR

* **DNF (3-way)**: splits into `< pivot | == pivot | > pivot`.
  **Shines with duplicates**—collapses all equals in one pass; fewer recursive calls/iterations.
* **Lomuto (2-way)**: splits into `< pivot | [pivot_at_final_index] | ≥ pivot`.
  **Simpler code**, good for mostly distinct data; slightly fewer branches/swaps per element.

---

## 1) What each produces (post-conditions)

| Scheme             | Layout after partition                                      | Fixed elements                                                          |
| ------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| **DNF (3-way)**    | `A[lo : lt] < p`, `A[lt : gt+1] == p`, `A[gt+1 : hi+1] > p` | **All equals grouped**; no single “pivot index” but a whole equal block |
| **Lomuto (2-way)** | `A[lo : store) < p`, `A[store] = p`, `(store : hi] ≥ p`     | **Pivot at `store`** is at its final position                           |

*(lo/hi inclusive/exclusive vary with convention; idea is the same.)*

---

## 2) Invariants while scanning

**DNF (Edsger Dijkstra)**

```
lt = lo, i = lo, gt = hi
while i <= gt:
  if A[i] < p: swap(A[lt], A[i]); lt += 1; i += 1
  elif A[i] > p: swap(A[i], A[gt]); gt -= 1       # i not advanced here
  else: i += 1
```

* Maintains 4 zones:

  1. `< p`  (lo .. lt-1)
  2. `== p` (lt .. i-1)
  3. unknown (i .. gt)
  4. `> p`  (gt+1 .. hi)

**Lomuto**

```
swap(A[pivot], A[hi])              # move pivot to end
store = lo
for i in range(lo, hi):
  if A[i] < A[hi]:
    swap(A[i], A[store]); store += 1
swap(A[store], A[hi])              # pivot lands at store
```

* Maintains:

  * `< p` in `A[lo:store)`
  * `≥ p` in `A[store:i]`
  * pivot ends at `store`

---

## 3) Duplicates handling

| Aspect                           | DNF                                                                                                                        | Lomuto                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Equals to pivot                  | Collected into a single middle block in one pass                                                                           | Stay on the “right” side (≥ p) and often get re-partitioned in subsequent calls |
| Effect on recursion / iterations | **Major win**—if k lies inside equal block, Quickselect returns immediately; Quicksort recurses on strictly smaller ranges | Can need more recursion / iterations because equals are not eliminated en masse |

---

## 4) Cost profile (comparisons, swaps, branches)

* **DNF**

  * May perform **more swaps** (particularly when many `> p` items because `i` doesn’t advance on those swaps).
  * But **fewer recursive calls/iterations** when duplicates are common (big practical win).
* **Lomuto**

  * One forward pass with a tight inner loop; **fewer branches**; often **a hair faster** on **distinct** data.
  * Simple to reason about and implement.

Both are linear passes: **O(n)** per partition. Overall complexity for Quickselect/Quicksort depends on pivot quality.

---

## 5) Typical use in algorithms

| Algorithm                   | Preferred partition                                      | Why                                                                                 |
| --------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Quickselect (k-th)**      | **DNF** when duplicates are common; **Lomuto** otherwise | DNF can terminate immediately if k falls in equal block; Lomuto is fine and simpler |
| **Quicksort**               | **DNF** often preferred when data has many duplicates    | Greatly reduces depth on equal runs (3-way Quicksort)                               |
| **Educational/simple code** | **Lomuto**                                               | Very concise and clear                                                              |

*(Hoare’s partition is a third option—fewer swaps on average, but postconditions are trickier and pivot is not at a fixed final index.)*

---

## 6) Stability, space, worst-case

* **Stability**: Neither is stable (they both swap elements around).
* **Extra space**: In-place, **O(1)** auxiliary.
* **Worst-case time**: With adversarial pivots, **O(n²)** for both Quickselect/Quicksort; use **randomized pivots** or **median-of-three**; many libraries use **introsort** (Quicksort with heapsort fallback).

---

## 7) Pseudocode (copy-ready)

### DNF (3-way) partition (good for duplicates)

```python
def dnf_partition(A, lo, hi, pivot_value):
    lt, i, gt = lo, lo, hi
    while i <= gt:
        if A[i] < pivot_value:
            A[lt], A[i] = A[i], A[lt]
            lt += 1; i += 1
        elif A[i] > pivot_value:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1              # i stays to inspect the swapped-in element
        else:
            i += 1
    # returns the equal block bounds
    return lt, gt
```

### Lomuto partition (simple & common)

```python
def lomuto_partition(A, lo, hi):     # pivot chosen at hi
    pivot = A[hi]
    store = lo
    for i in range(lo, hi):
        if A[i] < pivot:
            A[i], A[store] = A[store], A[i]
            store += 1
    A[store], A[hi] = A[hi], A[store]
    return store                      # pivot's final index
```

---

## 8) When to pick which (sound bite for interviews)

* **“If there are **many duplicates**, use **3-way DNF**: it groups equals and shrinks the problem faster.”**
* **“If data is **mostly distinct** and I want **minimal code**, I use **Lomuto**.”**
* Always **randomize the pivot** (or median-of-three) to keep expected O(n).

---

## 9) Micro example highlighting difference

`A = [5, 5, 5, 5, 5], k = 3, pivot = 5`

* **DNF**: one pass ⇒ equal block is whole array ⇒ k inside ⇒ **done** immediately.
* **Lomuto**: one partition places a single 5 at `store`; still okay, but you needed the index check route—no big-O change, just more mechanical steps over identical values.

---

**Bottom line:**

* Prefer **DNF** for robustness (especially with duplicates) in Quickselect/Quicksort.
* Prefer **Lomuto** for its simplicity when data is mostly distinct or when teaching/whiteboarding.
