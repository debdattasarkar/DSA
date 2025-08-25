

---

# Maximize Median After Doing K Addition Operation

**Difficulty:** Medium
**Accuracy:** 37.72%
**Submissions:** 6K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given an array **arr\[]** consisting of positive integers and an integer **k**.
You are allowed to perform **at most k operations**, where in each operation, you can increment **any one element** of the array by 1.

Determine the **maximum possible median** of the array that can be achieved after performing at most **k** such operations.

---

### Note:

* The median of a sorted array is:

  * The **middle element** if the size is odd.
  * The **average of the two middle elements** if the size is even.

---

## Examples

### Example 1

**Input:**
`arr[] = [1, 3, 4, 5], k = 3`

**Output:**
`5`

**Explanation:**
We can add +2 to the second element and +1 to the third element to get the array `[1, 5, 5, 5]`.
After sorting, the array remains `[1, 5, 5, 5]`.
Since the length is even, the median is `(5 + 5) / 2 = 5`.

---

### Example 2

**Input:**
`arr[] = [1, 3, 6, 4, 2], k = 10`

**Output:**
`7`

**Explanation:**
After applying operations optimally, we can transform the array to `[1, 3, 7, 7, 7]` (one possible way).
Sorted array becomes `[1, 3, 7, 7, 7]`.
Since the length is odd, the median is the middle element → `7`.

---

## Constraints:

* $1 \leq arr.size() \leq 10^5$
* $0 \leq arr[i], k \leq 10^9$

---

## Expected Complexities:

* **Time Complexity:** $O(n \cdot \log k)$
* **Auxiliary Space:** $O(1)$

---

## Topic Tags:

* Binary Search
* Algorithms

---

## Related Articles:

* [Maximize Median After Doing K Addition Operation On The Array](https://www.geeksforgeeks.org/maximize-median-after-doing-k-addition-operation-on-the-array/)

---

---

Got it—let’s lock in your working solution and make it interview‑ready.

# What the solution does (in plain English)

* Sort the array.
* We want to **maximize the median** after at most `k` unit increments.
* Only the **right half** (from the current median to the end) matters, because increasing any element left of the median can’t raise the median as cheaply as increasing elements on/after the median.
* Use **binary search on the answer** (the target median `T`):

  * For a candidate `T`, compute the **minimum total increments** needed to make all elements in the right half at least `T`.
  * If that cost ≤ `k`, `T` is feasible → move search upward; else, downward.
* Special handling for **even `n`**: the median is `(a+b)/2` where `a=arr[n/2-1]` and `b=arr[n/2]`.

  * First, check if we can satisfy `a+b ≥ 2*T` using ≤ `k` operations.
  * If `b−a ≥ delta` where `delta = 2*T − (a+b)`, we can push only the smaller of the two middles to reach the target median cheaply and skip scanning the tail.
  * Otherwise, fall back to the general “raise the right half” sum.

# Why it’s correct

* After sorting, increasing any value **left** of index `(n−1)//2` cannot change the median without also raising elements on the right; hence, the cheapest path is to spend all ops on the **right half**.
* For **odd `n`**, raising just the middle and elements to its right to ≥ `T` is sufficient and minimal.
* For **even `n`**, the median condition is `arr[n/2−1]+arr[n/2] ≥ 2*T`.
  The optimization checks whether this can be achieved by spending `delta` only on the smaller middle. If not, we compute the usual sum of deficits in the right half.

# Time & space complexity

* Sorting: `O(n log n)`.
* Binary search range is at most `arr[-1] + k − arr[(n−1)//2]`, giving `O(log k)` steps.
* Each feasibility check (`ok`) scans at most the right half: `O(n)`.
* **Total**: `O(n log n + n log k)` time, `O(1)` extra space (in‑place sort).

# Annotated version (same logic, lightly commented)

```python

class Solution:
    def maximizeMedian(self, arr, k):
        # Sort to reason about the median and right half
        n = len(arr)
        arr.sort()

        # Check if target median 'median' is achievable with ≤ k increments
        def ok(median: int) -> bool:
            start = (n - 1) // 2  # index of middle for odd; left-middle for even

            # Even-length optimization: try to satisfy a+b >= 2*median cheaply
            if n % 2 == 0:
                a, b = arr[start], arr[start + 1]
                delta = median * 2 - (a + b)  # extra sum we must add to a and/or b
                if delta > k:
                    return False
                # If pushing only the smaller middle (a) is enough, we're done
                if b - a >= delta:
                    return True
                # Otherwise continue to general accumulation below

            # General case: raise all elements in the right half to >= median
            needed = 0
            for i in range(start, n):
                if arr[i] >= median:
                    break
                needed += median - arr[i]
                if needed > k:        # early stop
                    return False
            return needed <= k

        # Binary search the maximum feasible median
        lo = arr[(n - 1) // 2]       # current floor median
        hi = arr[-1] + k             # absolute max we could push to
        while lo < hi:
            mid = hi - (hi - lo) // 2  # upper mid for "max feasible" search
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

# Quick dry run (even `n`)

`arr = [4, 6, 10, 10, 4, 10], k = 2` → sorted: `[4, 4, 6, 10, 10, 10]`, `n=6`, `start=2` (`a=6`, `b=10`).

* Try `T=9`: `delta = 18 - (6+10) = 2` ≤ `k`. `b-a = 4 ≥ 2` ⇒ we can increase only `a` by 2 → feasible.
* Try `T=10`: `delta = 20 - 16 = 4` > `k` ⇒ not feasible.
* Answer = `9`.

# Common interviewer follow‑ups (and crisp answers)

1. **Why not raise elements on the left half?**
   Because the median is determined by the right half after sorting; pushing left elements doesn’t move the pivot index and is never cheaper than pushing the necessary right elements.

2. **Why binary search on the value instead of greedy/DP?**
   Feasibility (`can we reach T?`) is monotonic in `T`, so binary search on `T` + linear check gives `O(n log k)` after sorting—optimal and simple.

3. **Edge cases?**

* `k = 0` → returns current median.
* All elements equal → returns that value.
* Very large `k` → capped by `arr[-1] + k`.

---

---

Here are a few high‑impact, real‑world places where “maximize the median with ≤ k unit increases” shows up:

1. **Fair budget top‑ups (resource allocation)**
   You’re given current department budgets and a limited “raise” pool `k`. Boosting the **median** (not the mean) ensures at least half of teams reach a healthier baseline without being skewed by a couple of huge budgets. The algorithm tells you the highest median you can guarantee.

2. **Income support / welfare disbursement**
   With a fixed amount of aid to distribute, policymakers might want to raise the **typical** (median) household income rather than the average, which is sensitive to outliers. The model answers: “What median can we reach if we add at most `k` total dollars across households?”

3. **Quality‑of‑service leveling**
   In cloud or network ops, each service has a reliability/latency score. You have `k` “improvement credits” (e.g., extra replicas, priority bandwidth). Spend them to push the **median** SLO up, guaranteeing that at least half the services meet a higher bar.

4. **Education/skills uplift**
   Schools or teams have test scores or skill ratings; training hours are limited to `k`. The plan that maximizes the **median** score lifts the “typical learner,” reducing systemic underperformance rather than chasing top scorers.

5. **Manufacturing yield improvement**
   Each line has a yield metric; process tweaks cost effort points and increase yield by 1 per point. Maximizing the **median** yield ensures at least half of lines clear a higher quality threshold, which often matters for contractual SLAs.

6. **Compensation normalization**
   HR wants to bring pay to a fairer baseline with a limited adjustment budget `k`. Maximizing the **median** salary (rather than average) is a principled way to correct compression or under‑market pay for a broad set of employees.

7. **Healthcare access benchmarks**
   Clinics have access scores (e.g., appointment wait days). With `k` improvement actions (extended hours, staffing), maximize the **median** access score so that a typical patient sees better service, not just a few clinics.

These all share the same structure: sorted “current levels,” limited additive improvements, and a goal to **lift the typical case** robustly—exactly what your algorithm optimizes.
