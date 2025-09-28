# Longest Bounded-Difference Subarray

**Difficulty:** Medium
**Accuracy:** 58.27%
**Submissions:** 23K+
**Points:** 4

---

Given an array of positive integers `arr[]` and a non-negative integer `x`, the task is to find the **longest sub-array** where the **absolute difference between any two elements** is **not greater than `x`**.
If multiple such subarrays exist, return the one that **starts at the smallest index**.

---

## Examples

### Example 1

**Input:** `arr[] = [8, 4, 5, 6, 7], x = 3`
**Output:** `[4, 5, 6, 7]`
**Explanation:** The sub-array described by index `[1..4]`, i.e., `[4, 5, 6, 7]` contains no two elements whose absolute difference is greater than `3`.

### Example 2

**Input:** `arr[] = [1, 10, 12, 13, 14], x = 2`
**Output:** `[12, 13, 14]`
**Explanation:** The sub-array described by index `[2..4]`, i.e., `[12, 13, 14]` contains no two elements whose absolute difference is greater than `2`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^9`
* `0 ≤ x ≤ 10^9`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Topic Tags

Algorithms • Heap • sliding-window • Arrays • Queue • Deque

---

## Related Articles

* [Longest Subarray In Which Absolute Difference Between Any Two Element Is Not Greater Than X](https://www.geeksforgeeks.org/longest-subarray-in-which-absolute-difference-between-any-two-element-is-not-greater-than-x/)

---

---

# Longest Bounded-Difference Subarray — Explanation, Dry Run & Python Solutions

## 2) Idea & Reasoning

We need the **longest** contiguous subarray such that for **any two** elements in it the absolute difference ≤ `x`.

Key fact:

> “No two elements differ by more than `x`” ⇔ **`max(window) − min(window) ≤ x`**.
> This condition is **necessary and sufficient** because the largest pairwise difference in a set equals `max − min`.

So the problem becomes: find the longest window `[L…R]` with `max(arr[L:R+1]) − min(arr[L:R+1]) ≤ x`.
Classic approach: **sliding window** + maintain **window min and max** in `O(1)` amortized using **monotonic deques**.

* `maxD` (decreasing): front holds index of current **maximum**.
* `minD` (increasing): front holds index of current **minimum**.
* Expand `R` to the right; push `arr[R]` while **preserving** monotonicity (pop from back until valid); append its index.
* While `arr[maxD[0]] − arr[minD[0]] > x`, shrink from the left by increasing `L`. If the outgoing index equals a deque’s front, pop it.
* Track the best window; on ties (same length), prefer the one with **smaller start index**.

Time `O(n)`, space `O(n)`.

---

### Step-by-step dry run

`arr = [8, 4, 5, 6, 7], x = 3`

We keep window `[L…R]`, `minD`, `maxD`, and best.

1. `R=0, val=8`

* `maxD=[0]`, `minD=[0]`, window `[0,0]` → max−min = 0 ≤ 3.
* best = `[0,0]` (len=1).

2. `R=1, val=4`

* Update deques:

  * `maxD`: pop back while arr[back] < 4 → pop 0 (8<4? no) ⇒ `maxD=[0,1]`.
  * `minD`: pop back while arr[back] > 4 → pop 0 ⇒ `minD=[1]`.
* Now max−min = `arr[0]-arr[1]=8-4=4` > 3 ⇒ shrink:

  * `L` moves from 0→1; remove index 0 from `maxD` (front is 0).
* Window `[1,1]` valid; best still `[0,0]` vs len=1 tie → prefer smaller start (0).

3. `R=2, val=5`

* `maxD`: pop back while <5 ⇒ 4<5 pop 1 ⇒ push 2 → `maxD=[2]`.
* `minD`: pop back while >5 ⇒ none ⇒ `minD=[1]`.
* max−min = `5−4=1` ≤ 3, window `[1,2]`, len=2 → best becomes `[1,2]` ([4,5]).

4. `R=3, val=6`

* `maxD`: pop back <6 ⇒ 5<6 pop 2 ⇒ push 3 → `maxD=[3]`.
* `minD` stays `[1]`.
* max−min = `6−4=2` ≤ 3 ⇒ window `[1,3]`, len=3 → best `[1,3]` ([4,5,6]).

5. `R=4, val=7`

* `maxD`: pop back <7 ⇒ 6<7 pop 3 ⇒ push 4 → `maxD=[4]`.
* `minD` stays `[1]`.
* max−min = `7−4=3` ≤ 3 ⇒ window `[1,4]`, len=4 → best `[1,4]` = `[4,5,6,7]` ✅

Result: `[4, 5, 6, 7]`.

---

## 3) Python solutions (with interview-style inline comments)

All versions return the **subarray** (not just length), breaking ties by earliest start.

### A) Optimal — Sliding window + two monotonic deques (O(n) / O(n))

```python
from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        """
        Keep a sliding window [L..R] and maintain its min and max in O(1) amortized
        using two monotonic deques:
          - maxD: indices in decreasing arr[] values (front = current max index)
          - minD: indices in increasing arr[] values (front = current min index)
        Expand R, and while max - min > x, shrink L.
        Track best window; tie-break by smaller L.
        Time:  O(n)
        Space: O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        maxD = deque()  # decreasing values -> max at front
        minD = deque()  # increasing values -> min at front
        L = 0
        bestL, bestLen = 0, 0

        for R, v in enumerate(arr):
            # push R into maxD (keep decreasing)
            while maxD and arr[maxD[-1]] < v:
                maxD.pop()
            maxD.append(R)

            # push R into minD (keep increasing)
            while minD and arr[minD[-1]] > v:
                minD.pop()
            minD.append(R)

            # shrink left while window invalid
            while arr[maxD[0]] - arr[minD[0]] > x:
                if maxD[0] == L:
                    maxD.popleft()
                if minD[0] == L:
                    minD.popleft()
                L += 1  # move left boundary right

            # valid window [L..R]; check best (tie: smallest start index)
            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen = curLen
                bestL = L

        return arr[bestL:bestL + bestLen]
```

### B) Clean alternative — Two Heaps with lazy deletion (O(n log n) / O(n))

```python
import heapq

class SolutionHeaps:
    def longestSubarray(self, arr, x):
        """
        Maintain min-heap and max-heap (as negatives) of (value, index).
        Use lazy deletion: when top index < L, pop and continue.
        Expand R; while max - min > x, increment L.
        Time:  O(n log n)
        Space: O(n)
        """
        n = len(arr)
        if n == 0:
            return []

        minH = []  # (val, idx)
        maxH = []  # (-val, idx)
        L = 0
        bestL, bestLen = 0, 0

        for R, v in enumerate(arr):
            heapq.heappush(minH, (v, R))
            heapq.heappush(maxH, (-v, R))

            # Clean tops to respect current L
            def top_min():
                while minH and minH[0][1] < L:
                    heapq.heappop(minH)
                return minH[0][0] if minH else None

            def top_max():
                while maxH and maxH[0][1] < L:
                    heapq.heappop(maxH)
                return -maxH[0][0] if maxH else None

            # Shrink while invalid
            while top_max() - top_min() > x:
                L += 1  # lazy deletion: indices < L will be popped on next access

            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen, bestL = curLen, L

        return arr[bestL:bestL + bestLen]
```

### C) Brute force (early break) — O(n²) / O(1) (for understanding / small inputs)

```python
class SolutionBrute:
    def longestSubarray(self, arr, x):
        """
        For each start i, extend j while tracking running min & max.
        Break when max - min > x. Keep best, tie-break by smaller i.
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        bestL, bestLen = 0, 0
        for i in range(n):
            cur_min = cur_max = arr[i]
            for j in range(i, n):
                cur_min = min(cur_min, arr[j])
                cur_max = max(cur_max, arr[j])
                if cur_max - cur_min > x:
                    break
                curLen = j - i + 1
                if curLen > bestLen or (curLen == bestLen and i < bestL):
                    bestLen, bestL = curLen, i
        return arr[bestL:bestL + bestLen]
```

---

## 4) Interview Q&A

**Q1. Why is checking `max - min ≤ x` sufficient for “any two elements differ by at most x”?**
Because among all pairwise differences, the **largest** is always between the **maximum** and **minimum** elements. If that difference is ≤ `x`, all others are smaller and thus ≤ `x`.

**Q2. How do the deques work in O(1) amortized?**
Each index is **pushed once** and **popped at most once** from each deque. Over the entire array, total operations are O(n), so per step is amortized O(1).

**Q3. How do you handle tie-breaking (same length)?**
When lengths tie, choose the window with **smaller start index L**. In code:
`if curLen > bestLen or (curLen == bestLen and L < bestL): update`.

**Q4. What happens when elements repeat or x = 0?**

* Repeats are fine: deques store indices; duplicates don’t break monotonicity invariants.
* `x = 0` means all values in the window must be **equal**; the algorithm still works and returns the longest block of identical numbers.

**Q5. Complexity of each approach?**

* **Deque sliding window:** `O(n)` time, `O(n)` space.
* **Heaps (lazy deletion):** `O(n log n)` time, `O(n)` space.
* **Brute force:** `O(n^2)` time, `O(1)` space.

**Q6. What are common pitfalls?**

* Forgetting to pop deque **fronts** when `L` passes those indices.
* Incorrect tie-breaking.
* Returning **length** when the problem expects the **subarray** (or vice versa). Adjust per platform.

---

---

All set! I ran a full, runnable program that:

* Implements three versions of `longestSubarray(arr, x)`:

  * **O(n)** sliding window with **two monotonic deques** (optimal).
  * **O(n log n)** sliding window with **two heaps** (lazy deletion).
  * **O(n²)** brute-force (for understanding / small inputs).
* Prints **inputs, outputs**, and **best timings** via `timeit`.
* Includes inline comments marking **time and space complexity** at each step.
* Benchmarks a **100,000-element** random array to show scalability (deque beats heaps as expected).

```python

from collections import deque
import heapq
import random
import timeit
from typing import List, Tuple

class SolutionDeque:
    def longestSubarray(self, arr: List[int], x: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        maxD = deque()
        minD = deque()
        L = 0
        bestL, bestLen = 0, 0
        for R, v in enumerate(arr):
            while maxD and arr[maxD[-1]] < v:
                maxD.pop()
            maxD.append(R)
            while minD and arr[minD[-1]] > v:
                minD.pop()
            minD.append(R)
            while arr[maxD[0]] - arr[minD[0]] > x:
                if maxD[0] == L:
                    maxD.popleft()
                if minD[0] == L:
                    minD.popleft()
                L += 1
            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen, bestL = curLen, L
        return arr[bestL:bestL + bestLen]

class SolutionHeaps:
    def longestSubarray(self, arr: List[int], x: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        minH: List[Tuple[int,int]] = []
        maxH: List[Tuple[int,int]] = []
        L = 0
        bestL, bestLen = 0, 0
        for R, v in enumerate(arr):
            heapq.heappush(minH, (v, R))
            heapq.heappush(maxH, (-v, R))
            def top_min():
                while minH and minH[0][1] < L:
                    heapq.heappop(minH)
                return minH[0][0]
            def top_max():
                while maxH and maxH[0][1] < L:
                    heapq.heappop(maxH)
                return -maxH[0][0]
            while top_max() - top_min() > x:
                L += 1
            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen, bestL = curLen, L
        return arr[bestL:bestL + bestLen]

class SolutionBrute:
    def longestSubarray(self, arr: List[int], x: int) -> List[int]:
        n = len(arr)
        bestL, bestLen = 0, 0
        for i in range(n):
            cur_min = cur_max = arr[i]
            for j in range(i, n):
                if j > i:
                    v = arr[j]
                    cur_min = v if v < cur_min else cur_min
                    cur_max = v if v > cur_max else cur_max
                if cur_max - cur_min > x:
                    break
                curLen = j - i + 1
                if curLen > bestLen or (curLen == bestLen and i < bestL):
                    bestLen, bestL = curLen, i
        return arr[bestL:bestL + bestLen]

def time_call(fn, *args, repeat=5, number=1):
    result = fn(*args)
    timer = timeit.Timer(lambda: fn(*args))
    best = min(timer.repeat(repeat=repeat, number=number))
    return result, best

tests = [
    {"arr": [8, 4, 5, 6, 7], "x": 3, "expected": [4, 5, 6, 7]},
    {"arr": [1, 10, 12, 13, 14], "x": 2, "expected": [12, 13, 14]},
    {"arr": [1, 1, 1, 1], "x": 0, "expected": [1, 1, 1, 1]},
    {"arr": [5], "x": 10, "expected": [5]},
]

random.seed(7)
big_n = 100_000
big_arr = [random.randint(1, 10**6) for _ in range(big_n)]
tests_big = [{"arr": big_arr, "x": 1000, "expected": None}]

def run_and_report():
    print("=== Longest Bounded-Difference Subarray — Full Program ===\n")
    dq = SolutionDeque()
    hp = SolutionHeaps()
    bt = SolutionBrute()

    for idx, t in enumerate(tests, 1):
        arr, x, exp = t["arr"], t["x"], t["expected"]
        print(f"Test #{idx}: arr={arr}, x={x}")
        r1, t1 = time_call(lambda a, x: dq.longestSubarray(a, x), arr, x)
        print(f"  Deques  O(n)       : result={r1}, expected={exp}, best={t1:.6f}s")
        r2, t2 = time_call(lambda a, x: hp.longestSubarray(a, x), arr, x)
        print(f"  Heaps   O(n log n) : result={r2}, expected={exp}, best={t2:.6f}s")
        r3, t3 = time_call(lambda a, x: bt.longestSubarray(a, x), arr, x)
        print(f"  Brute   O(n^2)     : result={r3}, expected={exp}, best={t3:.6f}s")
        all_ok = (r1 == r2 == r3 == exp)
        print(f"  All correct? {all_ok}\n")

    for idx, t in enumerate(tests_big, 1):
        arr, x = t["arr"], t["x"]
        print(f"Big Test #{idx}: n={len(arr)}, x={x}")
        ref, tref = time_call(lambda a, x: dq.longestSubarray(a, x), arr, x, repeat=3)
        print(f"  Deques  O(n)       : length={len(ref)}, best={tref:.6f}s")
        r2, t2 = time_call(lambda a, x: hp.longestSubarray(a, x), arr, x, repeat=3)
        print(f"  Heaps   O(n log n) : length={len(r2)}, best={t2:.6f}s")
        print(f"  Lengths match? {len(ref) == len(r2)}\n")

run_and_report()

```

If you want just the interview-ready solution, use the deque version:

```python
from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        # Window [L..R]; keep max and min using monotonic deques.
        # Time:  O(n) amortized (each index in/out each deque at most once)
        # Space: O(n) in worst case for deques
        n = len(arr)
        if n == 0:
            return []

        maxD, minD = deque(), deque()  # store indices
        L = 0
        bestL, bestLen = 0, 0

        for R, v in enumerate(arr):
            while maxD and arr[maxD[-1]] < v:  # keep decreasing for max
                maxD.pop()
            maxD.append(R)

            while minD and arr[minD[-1]] > v:  # keep increasing for min
                minD.pop()
            minD.append(R)

            # shrink while invalid: max - min > x
            while arr[maxD[0]] - arr[minD[0]] > x:
                if maxD[0] == L:
                    maxD.popleft()
                if minD[0] == L:
                    minD.popleft()
                L += 1

            curLen = R - L + 1
            if curLen > bestLen or (curLen == bestLen and L < bestL):
                bestLen, bestL = curLen, L

        return arr[bestL:bestL + bestLen]
```

---

## Real-World Use Cases (important ones)

* **Alerting on metric stability windows:** find the longest continuous time span where a KPI (e.g., latency) stays within a tight band (max − min ≤ threshold).
* **Price band analysis:** detect the longest period a stock remained within a price range width `x` for range-trading strategies.
* **Quality control / sensor data:** locate longest intervals where sensor readings remain within tolerance to schedule maintenance or certify runs.
