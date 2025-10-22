
---

# 🧩 Nearly Sorted

**Difficulty:** Medium
**Accuracy:** 75.25%
**Submissions:** 80K+
**Points:** 4
**Average Time:** 30m

---

## 📜 Problem Statement

Given an array **arr[]**, where each element is at most **k positions away** from its correct position in the sorted order.
Your task is to **restore the sorted order** of `arr[]` by rearranging the elements **in place**.

---

> **Note:** Don’t use any built-in `sort()` method.

---

## 🧠 Examples

### Example 1

**Input:**

```
arr[] = [2, 3, 1, 4], k = 2
```

**Output:**

```
[1, 2, 3, 4]
```

**Explanation:**
All elements are at most `k = 2` positions away from their correct positions.

* Element 1 moves from index 2 → 0
* Element 2 moves from index 0 → 1
* Element 3 moves from index 1 → 2
* Element 4 stays at index 3

---

### Example 2

**Input:**

```
arr[] = [7, 9, 14], k = 1
```

**Output:**

```
[7, 9, 14]
```

**Explanation:**
All elements are already stored in the sorted order.

---

## ⚙️ Constraints

| Parameter              | Constraint |
| ---------------------- | ---------- |
| `1 ≤ arr.size() ≤ 10⁶` |            |
| `0 ≤ k < arr.size()`   |            |
| `1 ≤ arr[i] ≤ 10⁶`     |            |

---

## 🧮 Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log k) |
| **Auxiliary Space** | O(k)       |

---

## 🏢 Company Tags

* Google

---

## 🧵 Topic Tags

* Sorting
* Arrays
* Priority Queue

---

## 📚 Related Articles

* [**Nearly Sorted Algorithm**](https://www.geeksforgeeks.org/nearly-sorted-algorithm/)

---

---

## 2) Intuition + step-by-step dry run

**Given:** every element is at most **k** positions away from where it would appear in the fully sorted array.

**Key fact:**
At index `i` of the final sorted array, the correct element must be among indices `[i, i+k]` of the current array (can’t be farther left than `i` and can’t be more than `k` places to the right).

**Greedy with a min-heap (priority queue):**

1. Put the first `k+1` elements into a **min-heap** (the smallest among them belongs at position `0`).
2. Repeatedly:

   * Pop the heap’s min and write it to the next output position.
   * Push the next unseen array element (keeps the heap representing the next window of size `k+1`).
3. After the input is exhausted, pop out all remaining heap items.

Because each element is at most `k` away, the correct item for position `i` will **always** be in that heap.

### Dry run

`arr = [2, 3, 1, 4]`, `k = 2`

* Build heap from first `k+1 = 3` elements: heap = `[1, 3, 2]` (min at top = 1)
* i = 0: pop → `1`, write to `arr[0]`; push next element `4`
  heap becomes `[2, 3, 4]`, array now `[1, 3, 1, 4]` (we’re overwriting in place by index)
* i = 1: pop → `2`, write to `arr[1]`; (no next element to push yet)
  heap becomes `[3, 4]`, array `[1, 2, 1, 4]`
* i = 2: pop → `3`, write to `arr[2]` → `[1, 2, 3, 4]`, heap `[4]`
* i = 3: pop → `4`, write to `arr[3]` → `[1, 2, 3, 4]`, heap `[]`

Sorted, and every heap operation touched only `k+1` candidates.

---

## 3) Optimized Python solutions (interview-favorite + easy brute)

### A) ✅ Min-heap (optimal, expected by interviewers)

```python
import heapq

class Solution:
    def nearlySorted(self, arr, k):
        """
        Min-heap of size k+1
        Time  : O(n log k)   (each of n pushes/pops is log(k+1))
        Space : O(k)         (heap only)
        """
        n = len(arr)
        if n <= 1 or k <= 0:
            return arr  # already sorted or trivial

        # 1) Build heap from first k+1 elements
        heap = arr[:k+1]
        heapq.heapify(heap)        # O(k)

        write = 0                  # next position to place smallest element

        # 2) For remaining elements, push new, pop min to 'write'
        for read in range(k+1, n):
            smallest = heapq.heapreplace(heap, arr[read])  # pop min + push arr[read]
            arr[write] = smallest
            write += 1

        # 3) Drain the heap
        while heap:
            arr[write] = heapq.heappop(heap)
            write += 1

        return arr
```

### B) 🟡 Simple “selection over window” (easy to remember, O(n·k))

Pick the minimum from the next `k+1` window and swap to the current position.

```python
class Solution:
    def nearlySorted(self, arr, k):
        """
        Windowed selection: for each i, find min in arr[i : i+k+1] and swap to i.
        Time  : O(n * k)      (scan up to k+1 items per position)
        Space : O(1) extra
        Good when k is tiny and you want the simplest code without heaps.
        """
        n = len(arr)
        for i in range(n):
            # search the range [i, min(i+k, n-1)]
            end = min(i + k, n - 1)
            min_idx = i
            for j in range(i+1, end+1):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
```

> Either solution rearranges **in place** (the array itself becomes sorted).

---

## 4) Interview quick-recall + likely Q&A

### 5-line pseudo-code (say this first)

```
push first k+1 items to min-heap
for each remaining item:
    pop min → write next position
    push current item
drain heap popping to array
```

**Mnemonic:** **“Heap k+1 → Pop/Push → Drain.”**

### Typical questions

* **Why heap size `k+1`?**
  Because any element can be at most `k` to the right of its sorted position; therefore the correct item for position `i` must be within indices `[i, i+k]` → at most `k+1` candidates.

* **Complexity?**
  `O(n log k)` time, `O(k)` extra space.

* **Can you do it without extra space?**
  Strictly `O(1)` auxiliary while still `O(n log k)` is hard; the heap is the standard approach. A windowed selection is `O(nk)` time but `O(1)` space.

* **What if `k = 0` or `k = 1`?**
  `k=0` → already sorted; `k=1` → either already sorted or single local swap suffices; heap still works.

---

### Bonus: Modified insertion sort (also O(n·k))

You can mention: “Because elements move at most `k` places left, insertion sort that shifts at most `k` elements per iteration runs in `O(nk)`.”

---

---

Awesome—here are a few **high-impact, easy-to-explain real-world uses** plus a **complete, runnable Python program** for the “Nearly Sorted (k-sorted) array” problem with inline complexity notes and timings.

---

## 5) Real-World Use Cases (why this problem exists)

* **Streaming logs / telemetry ordered by time with bounded jitter (k):**
  Network delays and batching make events arrive slightly out of order (each event at most `k` places from its correct time). A **min-heap of size k+1** reorders them online in `O(n log k)`.

* **Merge phase of external sorting / k-way merge buffers:**
  When records are pulled from multiple nearly ordered buffers, the global stream becomes **k-sorted**. A small heap restores full order efficiently.

* **Task scheduling / priority queues with bounded skew:**
  Tasks come roughly sorted by priority or deadline, but each is off by ≤ `k`. Heap-based reordering gives a ready-to-execute, fully sorted list.

* **Sensor fusion / time-series alignment:**
  Packets from multiple sensors arrive nearly in order; reorder them cheaply without a full `O(n log n)` sort.

---

## 6) Full Program (heap-based optimal + simple O(nk) fallback)

Includes: inline time/space comments, sample I/O, and timing with `perf_counter` & `timeit`.

```python
#!/usr/bin/env python3
"""
Nearly Sorted (k-sorted) Array
------------------------------
Each element is at most k positions away from its sorted position.
Goal: sort in-place without using built-in sort().

Approach A (Optimal, Interview Favorite): Min-Heap of size k+1
  Time  : O(n log k) — every push/pop is log(k+1)
  Space : O(k)       — heap only

Approach B (Simple fallback): Windowed selection (find min in next k+1 and swap)
  Time  : O(n * k)
  Space : O(1)
"""

from typing import List
import heapq
from time import perf_counter
import timeit
import random


class Solution:
    # ---------- A) Min-Heap (Optimal) ----------
    def nearlySorted(self, arr: List[int], k: int) -> List[int]:
        """
        Min-heap keeps the next k+1 candidates for the current output slot.
        Steps:
          1) Push first k+1 items to heap               -> O(k)
          2) For each remaining item:
                pop-min to current write index          -> O(log k)
                push new item                           -> O(log k)
          3) Drain the heap                             -> O(k log k)

        Overall Time  : O(n log k)
        Aux Space     : O(k)

        Returns the same list 'arr' sorted in-place.
        """
        n = len(arr)
        if n <= 1 or k <= 0:
            return arr  # Already sorted or trivial input

        # 1) Build the initial heap with first k+1 elements
        heap = arr[:k + 1]                # O(k) space
        heapq.heapify(heap)               # O(k) time

        write = 0                         # Next position to write the smallest

        # 2) Slide through the array, maintaining heap of size k+1
        for read in range(k + 1, n):      # O(n - (k+1)) iterations
            # Pop the smallest and place it at 'write' (final position)
            smallest = heapq.heapreplace(heap, arr[read])  # O(log k)
            arr[write] = smallest
            write += 1

        # 3) Drain any remaining items in heap into arr
        while heap:                       # <= k elements left
            arr[write] = heapq.heappop(heap)  # O(log k)
            write += 1

        return arr

    # ---------- B) Windowed Selection (O(nk), O(1) space) ----------
    def nearlySorted_slow(self, arr: List[int], k: int) -> List[int]:
        """
        For each i, pick the minimum in arr[i : i+k+1] and swap to i.

        Time  : O(n * k) (scan up to k+1 elements per i)
        Space : O(1)
        """
        n = len(arr)
        for i in range(n):
            end = min(i + k, n - 1)
            min_idx = i
            for j in range(i + 1, end + 1):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr


# --------------------------- Demonstration & Timings ---------------------------

def demo_once(arr: List[int], k: int, use_slow: bool = False) -> None:
    s = Solution()
    label = "heap O(n log k)" if not use_slow else "window O(nk)"
    data = arr[:]                            # copy for fair run

    t0 = perf_counter()
    out = s.nearlySorted_slow(data, k) if use_slow else s.nearlySorted(data, k)
    t1 = perf_counter()

    print(f"Input : {arr}, k={k}  [{label}]")
    print(f"Output: {out}")
    print(f"Time  : {(t1 - t0) * 1e6:.1f} µs\n")


def avg_time(arr: List[int], k: int, method: str = "heap", runs: int = 5) -> float:
    s = Solution()
    if method == "heap":
        stmt = "s.nearlySorted(data, k)"
    else:
        stmt = "s.nearlySorted_slow(data, k)"
    setup = (
        "from __main__ import s, data, k\n"
    )
    # copy arr each run to simulate identical work
    def _runner():
        data[:] = arr
        return eval(stmt, {"s": s, "data": data, "k": k})
    # timeit wrapper
    return timeit.timeit(_runner, number=runs) / runs


if __name__ == "__main__":
    print("Nearly Sorted (k-sorted) — Demo & Timings\n")

    # --- Small sanity checks (match the prompt) ---
    demo_once([2, 3, 1, 4], k=2)       # -> [1, 2, 3, 4]
    demo_once([7, 9, 14], k=1)         # -> [7, 9, 14]
    demo_once([2, 3, 1, 4], k=2, use_slow=True)

    # --- Larger randomized test to see scaling ---
    random.seed(42)
    n = 50_000
    k = 20
    base = list(range(n))
    # produce a k-sorted array by shuffling each position within a window of size ~k
    arr_large = base[:]
    for i in range(n):
        j = min(n - 1, i + random.randint(0, k))
        arr_large[i], arr_large[j] = arr_large[j], arr_large[i]

    # average timings (few runs)
    heap_avg = avg_time(arr_large[:], k, method="heap", runs=3)
    slow_avg = avg_time(arr_large[:], k, method="slow", runs=1)  # slow can be heavy; 1 run

    print(f"Average times on n={n}, k={k}:")
    print(f"  heap (O(n log k)) : {heap_avg:.4f} s")
    print(f"  window (O(nk))    : {slow_avg:.4f} s")
    print("\nComplexity summary:")
    print("  Heap:   Time O(n log k), Space O(k)")
    print("  Window: Time O(nk),      Space O(1)")
```

### What you’ll see

* Correct outputs for the sample inputs.
* Timing comparisons that clearly show **heap beats O(nk)** for moderate/large `n` or `k`.

### One-liner to say in the interview

> “Because each element is at most `k` away, the correct value for position `i` must be among the next `k+1` elements. I keep a **min-heap of size k+1**, pop the smallest into place, and push the next element—this sorts in **O(n log k)** time and **O(k)** space. If I needed the simplest code, I could do a **windowed selection** in **O(nk)** time.”
