
---

# 📍 K Closest Points to Origin

**Difficulty:** Medium
**Accuracy:** 62.4%
**Submissions:** 25K+
**Points:** 4

---

## 🧩 Problem Statement

Given an integer `k` and an array of points `points[][]`, where each point is represented as `points[i] = [xi, yi]` on the X–Y plane.
Return the **k closest points to the origin (0, 0)**.

The distance between two points on the X–Y plane is the **Euclidean distance**, defined as:

[
distance = \sqrt{(x2 - x1)^2 + (y2 - y1)^2}
]

---

> **Note:**
> You can return the k closest points in any order; the driver code will print them in sorted order.
> Test cases are generated such that there will be a unique answer.

---

## 🧮 Examples

### Example 1

**Input:**

```
k = 2
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
```

**Output:**

```
[[-2, 2], [0, 1]]
```

**Explanation:**
The Euclidean distances from the origin are:

* Point (1, 3) → √10
* Point (-2, 2) → √8
* Point (5, 8) → √89
* Point (0, 1) → √1

The two closest points to the origin are **[-2, 2]** and **[0, 1]**.

---

### Example 2

**Input:**

```
k = 1
points = [[2, 4], [-1, -1], [0, 0]]
```

**Output:**

```
[[0, 0]]
```

**Explanation:**
The Euclidean distances from the origin are:

* Point (2, 4) → √20
* Point (-1, -1) → √2
* Point (0, 0) → √0

The closest point to the origin is **(0, 0)**.

---

## ⚙️ Constraints

| Parameter                     | Constraint |
| ----------------------------- | ---------- |
| `1 ≤ k ≤ points.size() ≤ 10⁵` |            |
| `-3×10⁴ ≤ xi, yi ≤ 3×10⁴`     |            |

---

## ⏱️ Expected Complexities

| Type                | Complexity |
| ------------------- | ---------- |
| **Time Complexity** | O(n log k) |
| **Auxiliary Space** | O(k)       |

---

## 🏷️ Topic Tags

* Sorting
* Heap
* Mathematical
* Priority Queue
* Divide and Conquer
* Geometric
* Arrays

---

## 🔗 Related Articles

* [**Find K Closest Points to the Origin**](https://www.geeksforgeeks.org/find-k-closest-points-to-the-origin/)

---

---

Let’s nail **K Closest Points to Origin** in an interview-ready way: intuition, a clear dry run, and three Python solutions (heap, sort, quickselect) with crisp comments.

---

## 2) Intuition + Step-by-Step Dry Run

**Goal:** return any order of the `k` points with the **smallest Euclidean distance** to `(0,0)`.

**Key trick:** You don’t need `sqrt(x²+y²)` — comparing **squared distance** `d = x*x + y*y` preserves order and avoids floating-point work.

### Why a heap of size k?

As we scan points, we only need to keep the **k best seen so far**. Use a **max-heap** of size `k` keyed by distance (store negative distance in Python’s min-heap).

* If the new point is **closer** than the **farthest** in the heap → pop the farthest and push the new one.
* Result is O(n log k) time, O(k) extra space — exactly what the prompt “Expected Complexities” suggests.

### Dry Run (Example 1)

```
k = 2
points = [(1,3), (-2,2), (5,8), (0,1)]
dist^2:   10       8        89     1
```

* push (10, (1,3)) → heap=[10]
* push ( 8,(-2,2)) → heap=[10,8] (size==k)
* next (89,(5,8)): 89 > max(10) → ignore (worse than current top-2)
* next ( 1,(0,1)): 1 < max(10) → pop 10, push 1 → heap=[8,1]
  Return points in heap → **[(-2,2), (0,1)]** ✅

---

## 3) Optimized Python solutions (3 ways)

All follow your requested signature. I’ll make the **heap** version the default (most expected), then show **sort** and **quickselect** variants.

### A) Max-heap of size k (recommended; O(n log k), O(k))

```python
import heapq

class Solution:
    def kClosest(self, points, k):
        """
        Keep k closest points in a max-heap (store negative distances to use Python min-heap).
        Time  : O(n log k)
        Space : O(k)
        """
        # Max-heap via negatives: ( -dist2, x, y )
        heap = []
        for x, y in points:
            dist2 = x*x + y*y  # squared distance is enough
            if len(heap) < k:
                heapq.heappush(heap, (-dist2, x, y))  # push until size k
            else:
                # If current point is closer than the farthest in heap → replace
                if -dist2 > heap[0][0]:              # compare to current max (-dist2 larger => closer)
                    heapq.heapreplace(heap, (-dist2, x, y))
                # else: ignore; it's farther than the current top-k
        # Extract the k points from heap (any order is fine)
        return [[x, y] for _, x, y in heap]
```

### B) Sort by squared distance (simple; O(n log n), O(1) extra)

```python
class Solution:
    def kClosest(self, points, k):
        """
        Sort all points by squared distance and take first k.
        Time  : O(n log n)
        Space : O(1) extra (ignoring Python sort overhead)
        """
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])  # sort ascending by dist^2
        return points[:k]
```

### C) Quickselect / nth_element style (average O(n), worst O(n^2))

```python
import random

class Solution:
    def kClosest(self, points, k):
        """
        Quickselect partitions points so first k positions are the k smallest distances.
        Expected Time: O(n), Worst: O(n^2) (mitigated by random pivot)
        Space        : O(1) extra (in-place)
        """
        def dist2(i):  # squared distance of points[i]
            x, y = points[i]
            return x*x + y*y

        def partition(lo, hi, pivot_idx):
            pivot_dist = dist2(pivot_idx)
            # Move pivot to end
            points[pivot_idx], points[hi] = points[hi], points[pivot_idx]
            store = lo
            for i in range(lo, hi):
                if dist2(i) < pivot_dist:
                    points[store], points[i] = points[i], points[store]
                    store += 1
            # Move pivot to final place
            points[store], points[hi] = points[hi], points[store]
            return store

        lo, hi = 0, len(points) - 1
        target = k - 1  # index of last item we want in the low partition
        while lo <= hi:
            pivot_idx = random.randint(lo, hi)
            mid = partition(lo, hi, pivot_idx)
            if mid == target:
                break
            elif mid < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return points[:k]
```

> **Which one to choose?**
>
> * If interviewer hints **O(n log k)** (as in the prompt), go **heap**.
> * If they want the easiest code, use **sort**.
> * If they ask for **linear expected time**, use **quickselect**.

---

## 4) Interview “quick recall” + Q&A

### 5-line pseudo-code (heap way)

```
heap = []                          # max-heap via negative distances
for each point (x,y):
    d2 = x*x + y*y
    if heap size < k: push(-d2, x, y)
    else if -d2 > heap[0].key: replace top with (-d2, x, y)
return points in heap
```

**Mnemonic:** **“Square → Keep K → Replace Farther.”**

### Likely questions

* **Why squared distance?**
  `sqrt` is monotonic; comparing `x²+y²` gives the same ordering and avoids floating point cost/precision issues.

* **Why a *max*-heap of size k (not min-heap)?**
  We want to quickly drop the **farthest** among the kept `k`. A max-heap gives `O(1)` access to the farthest to compare/replace.

* **Complexity of heap approach?**
  Each of the `n` points may cause an `O(log k)` heap operation → **O(n log k)** time, **O(k)** space.

* **When is quickselect better?**
  When you want **average O(n)** time and are okay with worst-case O(n²) (random pivot usually mitigates).

* **Stability / ties?**
  Any order is acceptable; test cases guarantee a unique set of `k` closest.

* **Edge cases?**

  * `k == len(points)` → return all.
  * Duplicated points are fine; squared distance handles them.
  * Large coordinates: squared distance fits in Python int (arbitrary precision).

---

### One-liner you can say before you code

> “I’ll compute **squared distances**, keep a **size-k max-heap**, and for each point replace the farthest if the new point is closer. That’s **O(n log k) time** and **O(k) space**, matching the expected complexity.”

---

---

Absolutely — here are practical ways this shows up plus a clean, runnable script (with timings) you can paste into any editor.

---

## 5) Real-World Use Cases (easy to relate)

* **Location services / maps**: show the **k nearest restaurants/ATMs** to the user’s current GPS location.
* **Recommendation / search**: find **k most similar vectors** (embeddings) to a query in an index.
* **Robotics / path planning**: choose **k nearest obstacles** to plan local avoidance.
* **Anomaly / outlier triage**: fetch **k closest normal points** to understand why a new data point isn’t an outlier.

> Pattern to say: “We maintain the k best (closest) candidates while scanning — a max-heap lets us drop the farthest in O(log k).”

---

## 6) Full Program (heap default + sort + quickselect)

Includes inline complexity notes, sample I/O, and timings using `perf_counter` and `timeit`.

```python
#!/usr/bin/env python3
"""
K Closest Points to Origin
--------------------------------
Three approaches:
  A) Max-heap of size k (recommended)      → Time O(n log k), Space O(k)
  B) Sort by squared distance (simplest)   → Time O(n log n), Space O(1) extra
  C) Quickselect (avg linear)              → Time O(n) avg / O(n^2) worst, Space O(1)

We use squared distance d2 = x*x + y*y (no sqrt) — order is preserved.
"""

from typing import List
import heapq
import random
from time import perf_counter
import timeit


class Solution:
    # ---------- A) Max-heap of size k (recommended) ----------
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Maintain the k closest points in a max-heap.
        We store (-dist2, x, y) because Python's heapq is a min-heap.
        Time  : O(n log k) over n points (each push/pop is log k)
        Space : O(k)
        """
        heap: List[tuple[int, int, int]] = []
        for x, y in points:
            d2 = x * x + y * y  # O(1)
            if len(heap) < k:
                heapq.heappush(heap, (-d2, x, y))  # O(log k) after the first k pushes
            else:
                # If this point is closer than current farthest (top of max-heap)
                if -d2 > heap[0][0]:
                    # pop+push in one step keeps heap size k
                    heapq.heapreplace(heap, (-d2, x, y))  # O(log k)
        # Any order is fine per prompt
        return [[x, y] for _, x, y in heap]

    # ---------- B) Sort all points by distance ----------
    def kClosest_sort(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Sort points by d2 ascending and return first k.
        Time  : O(n log n)
        Space : O(1) extra (ignoring sort's internal)
        """
        pts = points[:]  # avoid mutating caller
        pts.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return pts[:k]

    # ---------- C) Quickselect (nth_element style) ----------
    def kClosest_quickselect(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Partition points so first k have the smallest squared distances.
        Expected Time: O(n), Worst: O(n^2) (mitigated by random pivot)
        Space       : O(1) extra (in-place)
        """
        pts = points[:]  # work on a copy

        def d2(i: int) -> int:
            x, y = pts[i]
            return x * x + y * y

        def partition(lo: int, hi: int, pivot_idx: int) -> int:
            """ Lomuto partition by distance; returns final index of pivot. """
            pivot_dist = d2(pivot_idx)
            pts[pivot_idx], pts[hi] = pts[hi], pts[pivot_idx]
            store = lo
            for i in range(lo, hi):
                if d2(i) < pivot_dist:   # strictly closer goes left
                    pts[store], pts[i] = pts[i], pts[store]
                    store += 1
            pts[store], pts[hi] = pts[hi], pts[store]
            return store

        lo, hi = 0, len(pts) - 1
        target = k - 1
        while lo <= hi:
            p = random.randint(lo, hi)
            m = partition(lo, hi, p)
            if m == target:
                break
            elif m < target:
                lo = m + 1
            else:
                hi = m - 1
        return pts[:k]


# ------------------------------ Demo & Timings ------------------------------

def demo_once(points: List[List[int]], k: int) -> None:
    sol = Solution()

    def run(label: str, fn):
        data = points[:]  # copy for fairness
        t0 = perf_counter()
        out = fn(data, k) if fn is not sol.kClosest_quickselect else fn(data, k)
        t1 = perf_counter()
        print(f"{label:<18} -> {out}   ({(t1 - t0) * 1e6:.1f} µs)")

    print(f"Input points: {points}, k={k}")
    run("heap O(n log k)", sol.kClosest)
    run("sort O(n log n)", sol.kClosest_sort)
    run("quickselect ~O(n)", sol.kClosest_quickselect)
    print()

def avg_time(points: List[List[int]], k: int, method: str, runs: int = 5) -> float:
    sol = Solution()
    if method == "heap":
        stmt = "sol.kClosest(pts, k)"
    elif method == "sort":
        stmt = "sol.kClosest_sort(pts, k)"
    else:
        stmt = "sol.kClosest_quickselect(pts, k)"
    glb = {"sol": sol, "pts": points, "k": k}
    return timeit.timeit(stmt, number=runs, globals=glb) / runs


if __name__ == "__main__":
    print("K Closest Points to Origin — Demo & Timings\n")

    # Sample cases (match the prompt style)
    demo_once([[1, 3], [-2, 2], [5, 8], [0, 1]], k=2)   # expected two: [-2,2] and [0,1]
    demo_once([[2, 4], [-1, -1], [0, 0]], k=1)          # expected [[0,0]]

    # Larger randomized case to feel scaling
    random.seed(42)
    n = 100_000
    k = 50
    big = [[random.randint(-30_000, 30_000), random.randint(-30_000, 30_000)] for _ in range(n)]

    print("Average times on n=100k, k=50 (3 runs):")
    print(f"  heap        : {avg_time(big, k, 'heap', 3):.4f} s")
    print(f"  sort        : {avg_time(big, k, 'sort', 3):.4f} s")
    print(f"  quickselect : {avg_time(big, k, 'quick', 3):.4f} s\n")

    print("Complexity summary:")
    print("  heap        : Time O(n log k), Space O(k)")
    print("  sort        : Time O(n log n), Space O(1) extra")
    print("  quickselect : Time ~O(n) avg / O(n^2) worst, Space O(1)")
```

### What you’ll see

* Correct results for the small inputs.
* Average timings on a 100k dataset so you can compare **heap vs sort vs quickselect**.

### What to say in the interview (10 seconds)

> “I’ll compare **squared distances** and maintain a **max-heap of size k**; drop the farthest when a closer point arrives. That’s **O(n log k)** time and **O(k)** space, which matches the expected complexity. If needed, I can also do the simple sort (O(n log n)) or quickselect for average O(n).”
