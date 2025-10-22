
---

# 🔢 Top K Frequent in Array

**Difficulty:** Medium
**Accuracy:** 40.23%
**Submissions:** 101K+
**Points:** 4
**Average Time:** 30m

---

## 🧩 Problem Statement

Given a **non-empty integer array** `arr[]`, your task is to find and return the **top k elements** which have the **highest frequency** in the array.

---

### 📝 Note

If two numbers have the **same frequency**, the **larger number** should be given the **higher priority**.

---

## 🧠 Examples

### Example 1

#### Input:

```
arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
```

#### Output:

```
[4, 1]
```

#### Explanation:

* Frequency of 4 = 2
* Frequency of 1 = 2
  These two have the maximum frequency.
  Since both have the same frequency, **4 > 1**, hence **4** appears first.

---

### Example 2

#### Input:

```
arr[] = [7, 10, 11, 5, 2, 5, 7, 11, 8, 9], k = 4
```

#### Output:

```
[5, 11, 7, 10]
```

#### Explanation:

* Frequency of 5 → 3
* Frequency of 11 → 2
* Frequency of 7 → 2
* Frequency of 10 → 1

Hence, the **top 4 frequent elements** in descending order of frequency and tie-break by value are:
**[5, 11, 7, 10]**

---

## ⚙️ Constraints

| Parameter                             | Constraint |
| ------------------------------------- | ---------- |
| `1 ≤ arr.size() ≤ 10⁵`                |            |
| `1 ≤ arr[i] ≤ 10⁵`                    |            |
| `1 ≤ k ≤ number of distinct elements` |            |

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log n) |
| **Auxiliary Space** | O(n)       |

---

## 💼 Company Tags

* Amazon
* Microsoft

---

## 🧵 Topic Tags

* Arrays
* Hash
* Sorting
* Data Structures
* Algorithms

---

## 🔗 Related Articles

* [Find K Numbers Occurrences Given Array](https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/)

---

---

Let’s make “Top-K Frequent Elements (tie → larger value first)” interview-ready: clear intuition, a quick dry run, and three Python solutions that cover the usual interview paths (sort, heap, bucket).

---

## 2) Intuition + Step-by-Step Dry Run

**Goal:** return the `k` numbers with **highest frequency**.
**Tie rule:** if two numbers have the **same frequency**, the **larger number** comes first.

Natural plan:

1. Count each number’s frequency (hash map).
2. Select top-k by a ranking key: **(frequency desc, value desc)**.

### Dry run (Example 1)

`arr = [3, 1, 4, 4, 5, 2, 6, 1], k = 2`

1. Frequency map:

* 1 → 2, 4 → 2, 2 → 1, 3 → 1, 5 → 1, 6 → 1

2. Sort keys by (freq desc, value desc):

* (2,4), (2,1), (1,6), (1,5), (1,3), (1,2)

3. Pick first `k=2` → **[4, 1]** ✅ (tie on freq=2 → 4 > 1)

### Dry run (Example 2)

`arr = [7,10,11,5,2,5,7,11,8,9], k=4`
freq: 5→3, 11→2, 7→2, 10→1, 8→1, 9→1, 2→1
Order by (freq desc, value desc):

* (3,5), (2,11), (2,7), (1,10), (1,9), (1,8), (1,2)
  Top 4 → **[5, 11, 7, 10]** ✅

---

## 3) Python solutions (all with the exact signature)

All three respect the tie rule “larger value first”.

### A) Counter + Sort (simple & most common)

```python
from collections import Counter

class Solution:
    def topKFreq(self, arr, k):
        """
        1) Count frequencies
        2) Sort unique values by (-freq, -value) to honor:
           - higher frequency first
           - on ties, larger value first
        Time  : O(n log m) where m = #distinct (≤ n)
        Space : O(m)
        """
        freq = Counter(arr)                                # O(n)
        ranked = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))  # O(m log m)
        return [val for val, _ in ranked[:k]]
```

### B) Size-k Min-Heap (great when k ≪ n)

```python
import heapq
from collections import Counter

class Solution:
    def topKFreq(self, arr, k):
        """
        Maintain a size-k min-heap where the 'worst' kept element is at top.
        Heap key = (freq, value). We want to KEEP larger freq; on ties, KEEP larger value.
        So if incoming (f, v) > heap[0], it's better and replaces the top.
        Time  : O(n + m log k)
        Space : O(m + k)
        """
        freq = Counter(arr)                                # O(n)
        heap = []                                          # min-heap of (freq, value)
        for v, f in freq.items():                          # O(m)
            item = (f, v)
            if len(heap) < k:
                heapq.heappush(heap, item)                 # O(log k)
            else:
                if item > heap[0]:                         # better: higher freq; tie→larger value
                    heapq.heapreplace(heap, item)          # O(log k)

        # heap has k best (freq, value); sort descending to match tie rule order if needed
        heap.sort(key=lambda x: (-x[0], -x[1]))            # O(k log k)
        return [v for f, v in heap]
```

### C) Bucket Sort by Frequency (linear time)

```python
from collections import Counter

class Solution:
    def topKFreq(self, arr, k):
        """
        Bucket frequencies: bucket[f] holds all values that occur f times.
        Then scan buckets from high freq down; inside each bucket sort values DESC
        to satisfy 'larger value wins on ties'.
        Time  : O(n + m + n') where n' spent in inner sorts; in practice near O(n)
        Space : O(n)
        """
        freq = Counter(arr)                                # O(n)
        max_f = max(freq.values())                         # ≤ n
        buckets = [[] for _ in range(max_f + 1)]
        for val, f in freq.items():
            buckets[f].append(val)

        ans = []
        for f in range(max_f, 0, -1):                      # high → low
            if not buckets[f]:
                continue
            buckets[f].sort(reverse=True)                  # larger value first on ties
            for v in buckets[f]:
                ans.append(v)
                if len(ans) == k:
                    return ans
        return ans
```

**Which to choose?**

* If you want **cleanest** and fast to code → **Counter + Sort**.
* If **k is small** relative to distinct elements → **Heap**.
* If asked to hit **O(n)** average complexity → **Bucket**.

---

## 4) Interview quick-memory + Q&A

### 5-line pseudo-code (what to say first)

```
count with hashmap
rank by (-freq, -value)
return first k
```

### 60-second recall

* Build `freq` map.
* Choose one:

  * **Sort** by `(-freq, -value)` → O(n log n).
  * **Heap** keep k best using `(freq, value)` → compare with top, replace if better.
  * **Bucket** values by frequency; walk from high to low, sort bucket desc for tie rule.
* Return first `k`.

### Likely questions

**Q: Why `(-freq, -value)` in sort?**
A: We want descending frequency, and on ties descending value (larger first). Sorting ascending on the negatives achieves that.

**Q: How do you enforce the tie in the heap approach?**
A: Keep a **min-heap** of `(freq, value)` so the smallest tuple is “worst.” A candidate `(f,v)` is **better** if `(f,v) > heap[0]` (higher freq; on tie, larger value).

**Q: Complexity?**

* Hashing: O(n).
* Sort: O(m log m) with m distinct.
* Heap: O(m log k).
* Bucket: O(n + m) plus per-bucket sort (typically tiny).

**Q: Stability / order of final k?**
If the platform requires a specific order, return in `(freq desc, value desc)`. Otherwise any order is fine—examples usually show that priority.

---

### Tiny mnemonic

> **“Count → Rank → Pick k.”**
> (“Rank” means order by `(-freq, -value)`.)

That’s everything you need to explain, choose, and implement the solution under interview pressure.

---

---

Love it — let’s wrap this one with practical context + a clean, runnable script (with timings) you can drop into any editor.

---

## 5) Real-World Use Cases (easy to relate)

* **Log analytics / observability**: surface the most frequent error/status codes; tie-break by larger code (e.g., HTTP 500 before 404 if both have the same count).
* **Search/query ranking**: show top-k most-issued query IDs or intent IDs (bigger ID = more recent schema/version → tie rule helps).
* **E-commerce & content**: most viewed product/article IDs; when two products are viewed equally often, prefer the newer/higher ID.
* **Security / telemetry**: most frequent alert signatures or event IDs; tie-break on larger signature ID.

> Pattern to say in interviews: **“Count → Rank → Pick k”**. Rank is by **(frequency desc, value desc)** to satisfy the tie rule.

---

## 6) Full Program (with inline complexity comments + timings)

```python
#!/usr/bin/env python3
"""
Top K Frequent Elements (tie → larger value first)

Three approaches inside Solution:
  - method="sort"   : Counter + global sort          → O(n log m), space O(m)
  - method="heap"   : size-k min-heap                → O(n + m log k), space O(m + k)
  - method="bucket" : bucket frequencies (near O(n)) → O(n + m + k log b), space O(n)

n = len(arr), m = #distinct values (m ≤ n), b = max bucket size used in inner sorts.

The driver at the bottom:
  * runs each method on a few inputs,
  * prints outputs,
  * times them using perf_counter (single run) and timeit (averages).
"""

from collections import Counter
import heapq
from time import perf_counter
import timeit
from typing import List


class Solution:
    def topKFreq(self, arr: List[int], k: int, method: str = "bucket") -> List[int]:
        """
        Choose one of: 'sort', 'heap', 'bucket' (default).
        Returns k values ordered by:
          1) higher frequency first
          2) on ties, larger value first
        """
        if method == "sort":
            return self._by_sort(arr, k)
        elif method == "heap":
            return self._by_heap(arr, k)
        else:
            return self._by_bucket(arr, k)

    # ---------- A) Counter + Sort ----------
    def _by_sort(self, arr: List[int], k: int) -> List[int]:
        """
        Steps:
          1) Count occurrences (hash map)  → O(n) time, O(m) space
          2) Sort (value, freq) by (-freq, -value)  → O(m log m)
          3) Take first k  → O(k)
        Overall: O(n + m log m), Space: O(m)
        """
        freq = Counter(arr)  # O(n)
        ranked = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))  # O(m log m)
        return [val for val, _ in ranked[:k]]

    # ---------- B) Size-k Min-Heap ----------
    def _by_heap(self, arr: List[int], k: int) -> List[int]:
        """
        Maintain a size-k min-heap keyed by (freq, value).
        'Worse' is smaller freq; on tie, smaller value is worse.
        For a new (f,v), replace top if (f,v) > heap[0].

        Counting: O(n)
        Heap maintenance: O(m log k)
        Final sort of k answers for presentation (optional): O(k log k)
        Overall: O(n + m log k), Space: O(m + k)
        """
        freq = Counter(arr)  # O(n)
        heap: List[tuple[int, int]] = []  # (freq, value)

        for v, f in freq.items():  # O(m)
            if len(heap) < k:
                heapq.heappush(heap, (f, v))  # O(log k)
            else:
                if (f, v) > heap[0]:          # better candidate
                    heapq.heapreplace(heap, (f, v))  # O(log k)

        # present in the same order rule (freq desc, value desc)
        heap.sort(key=lambda t: (-t[0], -t[1]))  # O(k log k)
        return [v for f, v in heap]

    # ---------- C) Bucket by Frequency ----------
    def _by_bucket(self, arr: List[int], k: int) -> List[int]:
        """
        Buckets: bucket[f] holds values seen exactly f times.
        Then scan f from high to low; inside each bucket sort DESC
        to satisfy 'larger value wins on ties'.

        Counting: O(n)
        Building buckets: O(m)
        Scan buckets: O(n) average; inner sorts cost sum over buckets (usually small).
        Overall: near O(n) in practice; Space: O(n)
        """
        freq = Counter(arr)                     # O(n)
        max_f = max(freq.values())              # ≤ n
        buckets: List[List[int]] = [[] for _ in range(max_f + 1)]
        for val, f in freq.items():             # O(m)
            buckets[f].append(val)

        ans: List[int] = []
        for f in range(max_f, 0, -1):           # O(max_f)
            if not buckets[f]:
                continue
            buckets[f].sort(reverse=True)       # tie rule: larger first
            for v in buckets[f]:
                ans.append(v)
                if len(ans) == k:
                    return ans
        return ans


# ------------------------------ Demo & Timing ------------------------------

def run_case(arr: List[int], k: int, method: str) -> None:
    sol = Solution()
    print(f"Input: {arr}, k={k}, method='{method}'")

    t0 = perf_counter()
    out = sol.topKFreq(arr, k, method=method)
    t1 = perf_counter()
    print(f"Output: {out}")
    print(f"Elapsed (single run): {(t1 - t0) * 1e6:.1f} µs\n")


def avg_time(arr: List[int], k: int, method: str, runs: int = 5) -> float:
    stmt = "sol.topKFreq(arr, k, method=method)"
    glb = {"sol": Solution(), "arr": arr, "k": k, "method": method}
    return timeit.timeit(stmt, number=runs, globals=glb) / runs


if __name__ == "__main__":
    print("Top-K Frequent Elements (tie → larger value first)\n")

    # Example cases from prompt
    arr1, k1 = [3, 1, 4, 4, 5, 2, 6, 1], 2   # expected [4, 1]
    arr2, k2 = [7, 10, 11, 5, 2, 5, 7, 11, 8, 9], 4  # expected [5, 11, 7, 10]

    for m in ("sort", "heap", "bucket"):
        run_case(arr1, k1, m)
        run_case(arr2, k2, m)

    # Average timing on a larger input
    import random
    random.seed(0)
    n = 100_000
    # generate many repeats to create frequencies
    big = [random.randint(1, 50_000) for _ in range(n)]
    K = 20

    print("Average times on a larger array (n=100k, K=20, 3 runs each):")
    for m in ("sort", "heap", "bucket"):
        avg = avg_time(big, K, m, runs=3)
        print(f"  {m:<6} : {avg:.4f} s")

    print("\nComplexity summary:")
    print("  sort   → O(n log m) time, O(m) space")
    print("  heap   → O(n + m log k) time, O(m + k) space")
    print("  bucket → near O(n) time (avg), O(n) space")
```

### How to read the timings

* **Single run** via `perf_counter` → quick sanity check for each method and input.
* **Average** via `timeit` on a **100k** array → feel for scalability.

### What to say out loud in the interview

> “I’ll **count with a hashmap**, then either **sort by (-freq, -value)** for simplicity, or keep a **size-k min-heap** keyed by `(freq, value)` if k ≪ n, or do a **bucket-by-frequency** pass for near-linear time. All enforce the tie rule by choosing **larger value** first when frequencies are equal.”