
---

# 📊 Median of an Array

**Difficulty:** Basic
**Accuracy:** 44.57%
**Submissions:** 148K+
**Points:** 1

---

## 📘 Problem Statement

Given an array `arr[]` of integers, calculate the **median**.

---

## 💡 Examples

### Example 1

**Input:**
`arr[] = [90, 100, 78, 89, 67]`

**Output:**
`89`

**Explanation:**
After sorting the array, the middle element is the median.

---

### Example 2

**Input:**
`arr[] = [56, 67, 30, 79]`

**Output:**
`61.5`

**Explanation:**
In case of even number of elements, the **average of two middle elements** is the median.

---

### Example 3

**Input:**
`arr[] = [1, 2]`

**Output:**
`1.5`

**Explanation:**
The average of both elements will result in `1.5`.

---

## ⚙️ Constraints

```
1 ≤ arr.size() ≤ 10^5  
1 ≤ arr[i] ≤ 10^5
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

`Accolite` · `Amazon` · `Samsung` · `FactSet`

---

## 🏷️ Topic Tags

* Mathematical
* Divide and Conquer
* Algorithms

---

## 📚 Related Articles

* [*Median of an Unsorted Array in Linear Time O(n)*](https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/)

---

---

awesome — let’s make **Median of an Array** interview-ready.

---

## 2) Explanation + step-by-step dry run

**Median definition (unsorted array):**

* Sort the numbers.
* If `n` is odd → median is the element at index `n//2` (0-based).
* If `n` is even → median is the average of the two middle elements:
  `(a[n//2 - 1] + a[n//2]) / 2`.

### Why sorting works

Sorting places elements in non-decreasing order, so the middle position(s) split the set into two halves of equal size (or off by one), exactly matching the median definition.

### Dry run 1 (odd)

`arr = [90, 100, 78, 89, 67]`
Sorted → `[67, 78, 89, 90, 100]`
`n=5` (odd) → index `2` → **89** ✅

### Dry run 2 (even)

`arr = [56, 67, 30, 79]`
Sorted → `[30, 56, 67, 79]`
`n=4` → middle indices `1` and `2` → `(56 + 67) / 2 = 61.5` ✅

---

## 3) Python solutions (most expected + alternatives)

### A) Sorting (most expected; simplest & reliable)

```python
class Solution:
    def findMedian(self, arr):
        """
        Sort the array, then pick middle (or average of middles).
        Time  : O(n log n) for sort
        Space : O(1) extra if sort in-place
        """
        n = len(arr)
        arr.sort()  # in-place sort, O(n log n)

        mid = n // 2
        if n % 2 == 1:
            return float(arr[mid])                  # ensure float if needed
        else:
            # average of two middles; use .0 to keep float behavior
            return (arr[mid - 1] + arr[mid]) / 2.0
```

### B) Quickselect (average O(n), worst O(n²)) — when you need linear expected time

We select the **k-th smallest** without fully sorting.

```python
import random

class SolutionQuickSelect:
    def findMedian(self, arr):
        """
        Quickselect for median.
        Avg Time : O(n)
        Worst    : O(n^2) (rare; randomized pivot mitigates)
        Space    : O(1) average (in-place partition)
        """
        n = len(arr)
        # Helper: k-th smallest (0-based) using randomized Quickselect
        def quickselect(lo, hi, k):
            while True:
                if lo == hi:
                    return arr[lo]
                pivot_idx = random.randint(lo, hi)
                pivot = arr[pivot_idx]
                # 3-way partition: < pivot, == pivot, > pivot
                i, lt, gt = lo, lo, hi
                while i <= gt:
                    if arr[i] < pivot:
                        arr[i], arr[lt] = arr[lt], arr[i]; i += 1; lt += 1
                    elif arr[i] > pivot:
                        arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
                    else:
                        i += 1
                # Now [lo..lt-1] < pivot, [lt..gt] == pivot, [gt+1..hi] > pivot
                if k < lt:
                    hi = lt - 1
                elif k > gt:
                    lo = gt + 1
                else:
                    return arr[k]

        mid = n // 2
        if n % 2 == 1:
            return float(quickselect(0, n - 1, mid))
        else:
            # Need both middle values; compute the two k-ths
            left = quickselect(0, n - 1, mid - 1)
            right = quickselect(0, n - 1, mid)
            return (left + right) / 2.0
```

### C) Two Heaps (streaming / online median) — when numbers arrive one by one

Maintain:

* Max-heap for the lower half
* Min-heap for the upper half
  Heaps differ in size by at most 1. Median is either top of bigger heap (odd) or average of two tops (even).

```python
import heapq

class StreamingMedian:
    """
    For streaming inputs; call add(x) repeatedly and get median() anytime.
    Time per op: O(log n) (heap push/pop)
    Space: O(n)
    """
    def __init__(self):
        self.low = []   # max-heap via negatives
        self.high = []  # min-heap

    def add(self, x):
        if not self.low or x <= -self.low[0]:
            heapq.heappush(self.low, -x)
        else:
            heapq.heappush(self.high, x)

        # Rebalance
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
```

> In a typical DS interview for this prompt, solution **A** is what they expect.
> Use **B** if they push for better-than-sort time, or **C** if it’s a streaming follow-up.

---

## 4) Interview quick-recall + common Q&A

### 10-second memory hook

* **Mantra:** “Sort → odd: middle; even: avg of middles.”
* **If asked for faster:** “Quickselect for expected O(n).”
* **If streaming:** “Two heaps: max-low & min-high.”

### Common follow-ups (snappy answers)

**Q1. Complexity of the sort approach?**
`O(n log n)` time to sort; `O(1)` extra space if in-place.

**Q2. Can we do better than `O(n log n)`?**
Yes, **Quickselect** gets **expected O(n)** time (but worst `O(n²)`), or **Median of Medians** guarantees linear time (more complex to implement).

**Q3. What about integer overflow when averaging?**
In Python, ints are arbitrary precision and `/ 2.0` yields float. In other languages, cast to 64-bit or double before adding and dividing.

**Q4. Do we need to return a float for even `n`?**
Yes—median may be fractional. The examples show `61.5` and `1.5`.

**Q5. Stability / order preservation?**
Not required; we only compute a value.

**Q6. What if the array is already sorted?**
Then just pick middle(s) in `O(1)` after verifying sortedness (or assume it).

**Q7. Streaming data?**
Use **two heaps**. Maintain balance; median is top(s).

---

### Tiny “5 lines” you can say out loud before coding

```
sort(a)
n = len(a); m = n//2
if n%2: return a[m]
else:   return (a[m-1] + a[m]) / 2
```

That’s the whole plan you can rebuild in **under 30 seconds** in any language.

---

---

you got it—here are the final two pieces for **Median of an Array** 👇

---

## 5) Real-World Use Cases (quick, relatable)

* **Analytics dashboards:** median page-load time / transaction latency (robust to outliers).
* **Compensation benchmarking:** median salary in a market/role (less skew than mean).
* **QoS & SLOs:** median (P50) request duration as a baseline; compare with P90/P99.
* **A/B testing:** median conversion lag (time-to-first-purchase) to reduce skew from a few extreme users.

All map to “get the central value” from an (often unsorted) sample. In memory, sort; for large/streaming, use quickselect or two-heaps.

---

## 6) Full Python Program (with inline complexity notes + timing)

```python
from timeit import timeit
import heapq
import random

# ------------------------------------------------------------
# Approach A: Sort (most expected in interviews)
# ------------------------------------------------------------
class Solution:
    def findMedian(self, arr):
        """
        Sort then pick middle (or average of two middles).
        Time  : O(n log n)  -- sorting dominates
        Space : O(1) extra  -- in-place sort; Python may use small temp buffers
        """
        n = len(arr)
        arr.sort()                      # O(n log n)
        m = n // 2
        if n % 2:                       # odd size
            return float(arr[m])
        else:                           # even size
            return (arr[m - 1] + arr[m]) / 2.0


# ------------------------------------------------------------
# Approach B: Quickselect (expected O(n), worst O(n^2))
# ------------------------------------------------------------
class SolutionQuickSelect:
    def findMedian(self, arr):
        """
        Randomized quickselect for k-th order statistics.
        Avg Time : O(n)
        Worst    : O(n^2) (rare w/ random pivot)
        Space    : O(1) extra (in-place partitioning)
        """
        def quickselect(lo, hi, k):
            while True:
                if lo == hi:
                    return arr[lo]
                pivot = arr[random.randint(lo, hi)]
                # 3-way partition (Dutch National Flag)
                i, lt, gt = lo, lo, hi
                while i <= gt:
                    if arr[i] < pivot:
                        arr[i], arr[lt] = arr[lt], arr[i]; i += 1; lt += 1
                    elif arr[i] > pivot:
                        arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
                    else:
                        i += 1
                if k < lt:   # in left block
                    hi = lt - 1
                elif k > gt: # in right block
                    lo = gt + 1
                else:        # in middle block
                    return arr[k]

        n = len(arr)
        m = n // 2
        if n % 2:
            return float(quickselect(0, n - 1, m))
        else:
            left = quickselect(0, n - 1, m - 1)
            right = quickselect(0, n - 1, m)
            return (left + right) / 2.0


# ------------------------------------------------------------
# (Bonus) Streaming median: Two heaps (if interviewer asks)
# ------------------------------------------------------------
class StreamingMedian:
    """
    Maintain running median.
    Ops: add(x) -> O(log n), median() -> O(1)
    Space: O(n)
    """
    def __init__(self):
        self.low = []   # max-heap via negative values
        self.high = []  # min-heap

    def add(self, x):
        if not self.low or x <= -self.low[0]:
            heapq.heappush(self.low, -x)
        else:
            heapq.heappush(self.high, x)
        # Rebalance to size diff <= 1
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


# ------------------------------------------------------------
# Demo + Timing
# ------------------------------------------------------------
def run_demo():
    print("=== Median of an Array ===\n")

    samples = [
        ("Odd",  [90, 100, 78, 89, 67], 89.0),
        ("Even", [56, 67, 30, 79],       61.5),
        ("Tiny", [1, 2],                  1.5),
        ("One",  [42],                   42.0),
    ]

    s_sort = Solution()
    s_qsel = SolutionQuickSelect()

    for name, arr, expected in samples:
        out_sort = s_sort.findMedian(arr[:])
        out_qsel = s_qsel.findMedian(arr[:])
        print(f"{name}: arr={arr}")
        print(f"  Sort O(n log n) : {out_sort}")
        print(f"  QSelect O(n)avg : {out_qsel}")
        print(f"  Expected        : {expected}")
        print(f"  Match?          : {abs(out_sort-expected) < 1e-9 and abs(out_qsel-expected) < 1e-9}\n")

    # -------- Timing on larger random arrays --------
    import random
    random.seed(123)
    n = 300_000
    big = [random.randint(1, 100_000) for _ in range(n)]

    # timeit measures total time for the given number of runs
    t_sort = timeit(lambda: Solution().findMedian(big[:]), number=3)
    t_qsel = timeit(lambda: SolutionQuickSelect().findMedian(big[:]), number=3)

    print("=== Timing (seconds) ===")
    print(f"n={n}, runs=3 each")
    print(f"Sort        O(n log n): total {t_sort:.4f}s | avg {(t_sort/3):.4f}s/run")
    print(f"Quickselect O(n) avg  : total {t_qsel:.4f}s | avg {(t_qsel/3):.4f}s/run")

    # -------- Streaming example (bonus) --------
    stream = StreamingMedian()
    for x in [5, 15, 1, 3]:
        stream.add(x)
    print("\nStreaming sequence [5,15,1,3] -> running median:", stream.median())

if __name__ == "__main__":
    run_demo()
```

**What you’ll see when you run it**

* Correctness for the sample arrays (both sort and quickselect agree with the expected median).
* Timing comparison: sort vs. quickselect on a large random array.
* A tiny streaming demo showing how two-heaps exposes the median at any time.

---

### 10-second recall (pre-coding)

> “**Sort → middle or average.** If asked faster: **Quickselect**. If streaming: **two heaps**.”
