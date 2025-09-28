# Maximum subarray sum 2

**Difficulty:** Hard
**Accuracy:** 41.04%
**Submissions:** 156K+
**Points:** 8

---

## Problem Statement

You are given an array `arr[]` of integers and two integers `a` and `b`. You have to find the maximum possible **sum** of a contiguous subarray whose length is **at least `a`** and **at most `b`**.

---

## Examples

### Example 1

**Input:** `arr[] = [4, 5, -1, -2, 6], a = 2, b = 4`
**Output:** `9`
**Explanation:** The subarray `[4, 5]` has length `2` and sum `9`, which is the maximum among all subarrays of length between `2` and `4`.

### Example 2

**Input:** `arr[] = [-1, 3, -1, -2, 5, 3, -5, 2, 2], a = 3, b = 5`
**Output:** `8`
**Explanation:** The subarray `[3, -1, -2, 5, 3]` has length `5` and sum `8`, which is the maximum among all subarrays of length between `3` and `5`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `−10^5 ≤ arr[i] ≤ 10^5`
* `1 ≤ a ≤ b ≤ arr.size()`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

* prefix-sum
* Greedy
* Deque
* set
* sliding-window
* two-pointer-algorithm

---

## Related Articles

* Maximum Sum Subarray 2

---

---

# Maximum subarray sum 2 — explanation, dry run, and interview-ready Python

## 2) Intuition

Let `P[k] = arr[0] + … + arr[k-1]` be prefix sums (`P[0]=0`).
Sum of subarray `(i..j-1)` is `P[j] - P[i]`.
We need `max P[j] - P[i]` with **length constraint** `a ≤ j - i ≤ b`.

For each end index `j` (from `a` to `n`), the valid starts are
`i ∈ [j-b, j-a]`. So we want:

```
best(j) = P[j] - min{ P[i] | i in [j-b, j-a] }
answer  = max_j best(j)
```

Hence, while sweeping `j` from left to right, maintain the **minimum P[i]**
over the moving index window `[j-b, j-a]`.

### How to maintain the min fast?

* **Optimal O(n):** keep indices in a **monotonic deque** increasing by `P[i]`.

  * Before using `j`, **insert** index `idx = j-a` (it just became eligible).
  * **Expire** indices `< j-b`.
  * The deque front is the minimal prefix in the valid range.
* **Alternative O(n log n):** use a min-heap `(P[i], i)` and lazily pop expired indices.

Both handle negatives naturally.

---

## 2b) Dry run (Example 1)

`arr = [4, 5, -1, -2, 6], a=2, b=4`
Prefix: `P = [0, 4, 9, 8, 6, 12]`

We sweep `j = 2..5`.

* `j=2`: add `idx=0` (P[0]=0). Window `[j-b, j-a]=[−2,0] → {0}`; min=P[0]=0.
  `best = P[2]-P[0] = 9-0 = 9`. `ans=9`.
* `j=3`: add `idx=1` (4). Window `[−1,1] → {0,1}`; min remains P[0]=0.
  `best = P[3]-0 = 8`. `ans=9`.
* `j=4`: add `idx=2` (9). Window `[0,2] → {0,1,2}`; min=0.
  `best = P[4]-0 = 6`. `ans=9`.
* `j=5`: add `idx=3` (8). Window `[1,3] → {1,2,3}`; remove `0` from front (expired).
  min becomes `min{4,9,8}=4` (deque front is 1).
  `best = P[5]-4 = 12-4 = 8`. Final `ans=9`.

Answer `9` (subarray `[4,5]`).

---

## 3) Python solutions (separate blocks)

### 3A) Brute force using prefix sums — **O(n·(b−a+1))** time

Good for clarity; not for the full constraints.

```python
class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]  # prefix

        ans = -10**18
        # For each end j, scan all allowed starts i ∈ [j-b, j-a]
        for j in range(a, n+1):
            lo = max(0, j - b)
            hi = j - a
            best_min = 10**18
            for i in range(lo, hi + 1):
                best_min = min(best_min, P[i])
            ans = max(ans, P[j] - best_min)
        return ans
```

### 3B) Min-heap with lazy expiry — **O(n log n)** time, **O(n)** space

```python
import heapq

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]

        ans = -10**18
        heap = []  # (P[i], i)

        for j in range(a, n+1):
            # Add freshly eligible index i = j - a
            i_add = j - a
            heapq.heappush(heap, (P[i_add], i_add))

            # Expire indices with i < j - b
            lower = j - b
            if lower < 0:
                lower = 0
            while heap and heap[0][1] < lower:
                heapq.heappop(heap)

            # Current min prefix in window -> heap[0]
            ans = max(ans, P[j] - heap[0][0])
        return ans
```

### 3C) **Optimal O(n)** using a monotonic deque — preferred for interviews

```python
from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]

        dq = deque()  # store indices i with increasing P[i]
        ans = -10**18

        for j in range(a, n+1):
            # Insert i = j - a (newly eligible)
            i_add = j - a
            while dq and P[i_add] <= P[dq[-1]]:
                dq.pop()
            dq.append(i_add)

            # Remove expired: i < j - b
            lower = j - b
            if lower < 0:
                lower = 0
            while dq and dq[0] < lower:
                dq.popleft()

            # Front is the minimal P[i] in [j-b, j-a]
            ans = max(ans, P[j] - P[dq[0]])

        return ans
```

**Complexities**

* 3A: `O(n·(b−a+1))` time, `O(n)` space (prefix).
* 3B: `O(n log n)` time, `O(n)` space.
* 3C: `O(n)` time (each index pushed/popped ≤1), `O(n)` space for prefix + deque (≤ `b−a+1` items).

---

## 4) Common interview Q&A

**Q1. How do you derive the prefix-sum formulation?**
*A:* Sum of `arr[i..j-1]` is `P[j]-P[i]`. With length constraint `a ≤ j-i ≤ b`, for each `j` we just need the **minimum `P[i]`** over `i ∈ [j-b, j-a]`.

**Q2. Why does a monotonic deque work?**
*A:* We maintain candidate indices in increasing `P[i]`. When adding a new index, pop larger/equal tails; when indices fall out (`i < j-b`), pop from front. The front is always the min valid prefix.

**Q3. What about all negative arrays?**
*A:* Works seamlessly; we’re maximizing sums and still select the least prefix in the window, possibly returning the least negative sum constrained by length.

**Q4. Off-by-one pitfalls?**
*A:* Use prefix length `n+1`. Iterate `j` from `a` to `n`. Insert `i = j-a`. Expire indices `< j-b` (clamp lower bound at 0). Answer is updated with `P[j] - P[dq[0]]`.

**Q5. Why not plain Kadane’s?**
*A:* Kadane’s handles **unconstrained** subarray length. Here we must enforce a length range; Kadane’s doesn’t track that.

**Q6. Can we adapt to “exact length = L”?**
*A:* Yes: for each `j≥L`, use `i=j-L` only; the answer is `max_j P[j]-P[j-L]` (simple sliding window sum).

**Q7. Memory usage?**
*A:* `O(n)` for the prefix array plus at most `b−a+1` indices in the deque (still `O(n)`).

---

---

Great—here’s the complete package for “Maximum subarray sum 2.”

## 5) Full program with input, output, and timing

I executed a full Python program that:

* Implements **three** approaches (Brute `O(n·w)`, Heap `O(n log n)`, and Deque `O(n)`).
* Prints **inputs and outputs** for multiple test cases.
* Uses `timeit` to measure per-method runtimes and the **total program wall time**.

You can see the live outputs above, e.g.:

* Example 1 → **9**, Example 2 → **8**, All negative case → **-2**, etc.
* Timings from this run:

  * Deque `O(n)` (n=2000, 20 runs): ~**0.0907 s**
  * Heap `O(n log n)` (n=2000, 10 runs): ~**0.0353 s**
  * Brute `O(n·w)` (n=400, w=51, 3 runs): ~**0.0039 s**
  * **Total program wall-time**: ~**0.1344 s**

```python

# Re-run the full program (state was reset).

from collections import deque
import heapq
from timeit import timeit
import random

class Solution:
    def maxSubarrSum_deque(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]
        dq = deque()
        ans = -10**18
        for j in range(a, n+1):
            i_add = j - a
            while dq and P[i_add] <= P[dq[-1]]:
                dq.pop()
            dq.append(i_add)
            lower = max(0, j - b)
            while dq and dq[0] < lower:
                dq.popleft()
            ans = max(ans, P[j] - P[dq[0]])
        return ans

    def maxSubarrSum_heap(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]
        ans = -10**18
        heap = []
        for j in range(a, n+1):
            i_add = j - a
            heapq.heappush(heap, (P[i_add], i_add))
            lower = max(0, j - b)
            while heap and heap[0][1] < lower:
                heapq.heappop(heap)
            ans = max(ans, P[j] - heap[0][0])
        return ans

    def maxSubarrSum_brute(self, arr, a, b):
        n = len(arr)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + arr[i]
        ans = -10**18
        for j in range(a, n+1):
            lo = max(0, j - b)
            hi = j - a
            minP = 10**18
            for i in range(lo, hi+1):
                if P[i] < minP:
                    minP = P[i]
            ans = max(ans, P[j] - minP)
        return ans

def run_demo():
    sol = Solution()

    tests = [
        ("Example 1", [4, 5, -1, -2, 6], 2, 4),
        ("Example 2", [-1,3,-1,-2,5,3,-5,2,2], 3, 5),
        ("All negative", [-5,-2,-3,-4], 1, 3),
        ("Mixed small", [2,-1,2,3,-9,4,1,-2,7], 2, 5),
    ]

    print("=== Outputs (Optimal O(n) Deque) ===")
    for name, arr, a, b in tests:
        print(f"{name:12s} | a={a}, b={b}, arr={arr} -> max sum = {sol.maxSubarrSum_deque(arr, a, b)}")

    print("\n=== Timing (timeit) ===")
    n_medium = 2000
    random.seed(42)
    arr_medium = [random.randint(-100, 100) for _ in range(n_medium)]
    a_med, b_med = 30, 200

    n_brute = 400
    arr_brute = [random.randint(-50, 50) for _ in range(n_brute)]
    a_brt, b_brt = 20, 70

    t_deque = timeit(lambda: sol.maxSubarrSum_deque(arr_medium, a_med, b_med), number=20)
    print(f"Deque O(n)     (n={n_medium}, 20 runs): {t_deque:.6f} s")

    t_heap = timeit(lambda: sol.maxSubarrSum_heap(arr_medium, a_med, b_med), number=10)
    print(f"Heap  O(nlogn) (n={n_medium}, 10 runs): {t_heap:.6f} s")

    t_brut = timeit(lambda: sol.maxSubarrSum_brute(arr_brute, a_brt, b_brt), number=3)
    print(f"Brute O(n*w)   (n={n_brute}, w={b_brt-a_brt+1}, 3 runs): {t_brut:.6f} s")

total_time = timeit(run_demo, number=1)
print(f"\n=== Total program wall-time (1 run) === {total_time:.6f} s")

```

---

## 6) Real-World Use Cases (high-impact)

1. **Rolling analytics with duration bounds:**
   Compute the best KPI surge within a time span bounded between `a` and `b` (e.g., marketing uplift between 7 and 30 days).

2. **Network traffic/windowed QoS:**
   Find the heaviest traffic burst whose length must stay within buffer leasing limits (e.g., between `a` and `b` packets/intervals).

3. **Energy consumption optimization:**
   Detect the worst/best contiguous energy consumption window constrained by operational limits (e.g., minimum/maximum cycle length).

4. **Finance (bounded holding periods):**
   Maximize P&L over a contiguous period where holding time must be at least `a` and at most `b` days (simple proxy under hold-time constraints).
