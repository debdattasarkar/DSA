
---

# Container With Most Water

**Difficulty:** Medium
**Accuracy:** 53.84%
**Submissions:** 88K+
**Points:** 4
**Average Time:** 30m

---

## Problem Statement

Given an array **arr\[]** of non-negative integers, where each element **arr\[i]** represents the height of the **vertical lines**, find the **maximum amount of water** that can be contained between any two lines, together with the x-axis.

**Note:**
In the case of a single vertical line, it will not be able to hold water.

---

## Examples

**Example 1:**

```
Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base is 2. 
Height of container = min(5, 3) = 3. 
So, total area to hold water = 3 * 2 = 6.
```

---

**Example 2:**

```
Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are 4 distance apart. 
So the size of the base is 4. 
Height of container = min(5, 3) = 3. 
So, the total area to hold water = 4 * 3 = 12.
```

---

**Example 3:**

```
Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. 
So the size of the base is 5. 
Height of container = min(8, 5) = 5. 
So, the total area to hold water = 5 * 5 = 25.
```

---

## Constraints

* $1 \leq arr.size() \leq 10^5$
* $0 \leq arr[i] \leq 10^4$

---

## Expected Complexities

* **Time Complexity:** $O(n)$
* **Auxiliary Space:** $O(1)$

---

## Company Tags

* Flipkart
* Amazon
* Google

---

## Topic Tags

* Arrays
* Mathematical
* two-pointer-algorithm

---

## Related Articles

* [Container With Most Water](https://www.geeksforgeeks.org/container-with-most-water/)

---

---

Here’s a crisp, interview-ready walkthrough and solutions for **Container With Most Water**.

---

# 2) Intuition + Step-by-Step Dry Run

## Core idea

Pick two lines (indices `i < j`) and the water they can contain is

```
area = min(height[i], height[j]) * (j - i)
```

To **maximize** this, you want a **large width** and **tall walls**.
A classic trick is the **two-pointer** approach:

* Start with the **widest** container: `i = 0`, `j = n-1`.
* Compute area.
* Move the pointer at the **shorter** line inward, because the area is limited by the shorter wall:

  * If you move the taller wall inward, width shrinks and the limiting height doesn’t improve → area cannot increase.
  * If you move the shorter wall, height might improve to a taller wall while width shrinks, which could increase area.

Repeat until `i >= j`.

This greedy move guarantees the optimal answer in **O(n)**.

---

## Dry run (example)

`arr = [2, 1, 8, 6, 4, 6, 5, 5]` (answer should be `25`)

```
i=0 (2), j=7 (5)
area = min(2,5)*(7-0) = 2*7 = 14, best = 14
shorter is 2 → move i

i=1 (1), j=7 (5)
area = min(1,5)*(7-1) = 1*6 = 6, best = 14
shorter is 1 → move i

i=2 (8), j=7 (5)
area = min(8,5)*(7-2) = 5*5 = 25, best = 25
shorter is 5 → move j

i=2 (8), j=6 (5)
area = min(8,5)*(6-2) = 5*4 = 20, best = 25
shorter is 5 → move j

i=2 (8), j=5 (6)
area = min(8,6)*(5-2) = 6*3 = 18, best = 25
shorter is 6 → move j

i=2 (8), j=4 (4)
area = min(8,4)*(4-2) = 4*2 = 8, best = 25
shorter is 4 → move j

i=2 (8), j=3 (6)
area = min(8,6)*(3-2) = 6*1 = 6, best = 25
shorter is 6 → move j

stop (i >= j)
```

Maximum area = **25**.

Edge cases:

* `n < 2` → 0
* All heights zero → 0
* Multiple pairs yielding same max area → return that area (not the indices).

---

# 3) Python solutions (brute & optimized)

## A) Brute force (easy to explain, O(n²))

```python
class Solution:
    def maxWater(self, arr):
        # Brute force: Try all pairs (i, j), i < j
        # Time: O(n^2), Space: O(1)
        n = len(arr)
        if n < 2:
            return 0
        
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Width is (j - i), height is limited by the shorter wall
                area = min(arr[i], arr[j]) * (j - i)
                if area > best:
                    best = area
        return best
```

**Why it’s acceptable in an interview:** demonstrates problem understanding; then you must improve it.

---

## B) Optimal two-pointer (O(n), the expected interview answer)

```python
class Solution:
    def maxWater(self, arr):
        # Two-pointer greedy
        # Time: O(n), Space: O(1)
        n = len(arr)
        if n < 2:
            return 0
        
        i, j = 0, n - 1
        best = 0
        
        while i < j:
            # Current area using the shorter boundary as height
            h = arr[i] if arr[i] < arr[j] else arr[j]
            area = h * (j - i)
            if area > best:
                best = area
            
            # Move the pointer at the shorter wall to try to find a taller wall
            if arr[i] < arr[j]:
                i += 1
            elif arr[i] > arr[j]:
                j -= 1
            else:
                # Equal heights: moving either is fine; move both to prune width
                i += 1
                j -= 1
        
        return best
```

**Key reasoning for correctness:**
At any step with `i < j`, the area is `min(arr[i], arr[j]) * (j - i)`. The only chance to improve the limiting height is to move the pointer at the shorter height inward; moving the taller one cannot increase the minimum height and only reduces width.

---

# 4) Likely Interview Q\&A

**Q1. Why does moving the shorter pointer make sense?**
Because the area is limited by the shorter wall. Shrinking width while keeping the same limiting height can’t help; you need a potentially taller wall to compensate for the reduced width.

**Q2. What if both heights are equal?**
Moving either is fine. A common optimization is to move both inward to prune width faster (it won’t skip the optimal answer).

**Q3. Can the two-pointer method miss the optimal pair?**
No. If the optimal pair involved the current taller wall, moving the shorter wall inward is the only way to possibly increase the limiting height and reach that optimal pair.

**Q4. What’s the time and space complexity?**

* Two-pointer: **O(n)** time, **O(1)** extra space.
* Brute force: **O(n²)** time, **O(1)** space.

**Q5. What if the input has less than two lines?**
Return `0`. You need at least two lines to form a container.

**Q6. Do negative heights occur?**
Not per constraints (heights are non-negative). If they did, you’d clamp at 0 or reject as invalid input per problem statement.

**Q7. Are we required to return the indices as well?**
No, only the maximum area. If asked, you can easily track `(i, j)` when updating `best`.

**Q8. What if all heights are zero?**
The result is `0`—no container can hold water.

**Q9. Could a stack or DP help here?**
They’re unnecessary; the greedy two-pointer is optimal and simpler.

**Q10. How would you test edge cases?**

* `[]`, `[5]` → `0`
* `[0,0,0]` → `0`
* Increasing heights, decreasing heights, plateaus, duplicates
* Very large `n` to confirm O(n) performance.

---

---

Awesome — here’s a complete, interview-ready package for **Container With Most Water** that includes:

* a clean explanation baked into code comments,
* both **Brute Force (O(n²))** and **Two-Pointer (O(n))** solutions,
* a **main** that prints inputs/outputs,
* and a tiny **timeit** benchmark.

---

## 5) Full Python program (with inline complexity notes + timeit)

```python
#!/usr/bin/env python3
"""
Container With Most Water — Full Program

Two implementations:
1) Brute Force: O(n^2) time, O(1) space
2) Two-Pointer (Optimal): O(n) time, O(1) space

The program prints answers and measures runtime using timeit.
"""

from timeit import timeit

class Solution:
    def maxWater_bruteforce(self, arr):
        """
        Brute force:
        - Try all pairs (i, j), i < j
        - Area = min(arr[i], arr[j]) * (j - i)

        Time:  O(n^2) — double loop over i,j
        Space: O(1)   — constant extra memory
        """
        n = len(arr)
        if n < 2:
            return 0

        best = 0
        # Outer loop over left index
        for i in range(n):  # O(n)
            # Inner loop over right index
            for j in range(i + 1, n):  # O(n)
                # Compute area with width (j - i) and height limited by shorter wall
                # O(1) per pair
                h = arr[i] if arr[i] < arr[j] else arr[j]
                area = h * (j - i)
                if area > best:
                    best = area
        return best

    def maxWater(self, arr):
        """
        Two-pointer greedy (optimal):
        - Start with widest container (i=0, j=n-1)
        - Compute area and move the pointer at the SHORTER line inward.
          Rationale: area is limited by shorter height; moving the taller one
          cannot increase the limiting height and only reduces width.

        Time:  O(n)  — each pointer moves inward at most n steps
        Space: O(1)  — two pointers, constant extra memory
        """
        n = len(arr)
        if n < 2:
            return 0

        i, j = 0, n - 1
        best = 0

        while i < j:                 # O(n) loop overall
            # Current area using shorter boundary as height
            # O(1) work per step
            if arr[i] < arr[j]:
                h = arr[i]
                area = h * (j - i)
                if area > best:
                    best = area
                i += 1               # move shorter wall
            elif arr[i] > arr[j]:
                h = arr[j]
                area = h * (j - i)
                if area > best:
                    best = area
                j -= 1               # move shorter wall
            else:
                # Equal heights: compute once and advance both to prune width
                h = arr[i]           # same as arr[j]
                area = h * (j - i)
                if area > best:
                    best = area
                i += 1
                j -= 1

        return best


def main():
    sol = Solution()

    # ---------- Sample Inputs ----------
    samples = [
        # (array, expected)
        ([1, 5, 4, 3], 6),
        ([3, 1, 2, 4, 5], 12),
        ([2, 1, 8, 6, 4, 6, 5, 5], 25),
        ([1, 1], 1),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([0, 0, 0, 0], 0),
    ]

    print("=== Container With Most Water ===")
    for arr, expected in samples:
        ans_brute = sol.maxWater_bruteforce(arr)
        ans_opt   = sol.maxWater(arr)
        print(f"arr = {arr}")
        print(f"  Brute  : {ans_brute}")
        print(f"  Optimal: {ans_opt}  (expected: {expected})")
        print(f"  OK?    : {ans_opt == expected and ans_brute == expected}")
        print("-" * 50)

    # ---------- Timing ----------
    # Use a larger random-like input for meaningful timing (fixed here for determinism)
    big_arr = [i % 1000 for i in range(100000)]  # length=100k

    # Wrap calls for timeit
    def run_brute():
        sol.maxWater_bruteforce(big_arr)

    def run_opt():
        sol.maxWater(big_arr)

    # NOTE: Brute force on 100k is too slow; time a smaller slice for fairness
    brute_slice = big_arr[:1200]  # ~1.4M pairs
    def run_brute_small():
        sol.maxWater_bruteforce(brute_slice)

    # Warmup + measure
    t_opt = timeit(run_opt, number=3)  # run optimal 3 times
    t_brute = timeit(run_brute_small, number=1)

    print("\n=== Timing (seconds) ===")
    print(f"Optimal (O(n)) on n=100000, 3 runs total: {t_opt:.6f}s")
    print(f"Brute (O(n^2)) on n=1200, 1 run:         {t_brute:.6f}s")
    print("(Note how O(n) scales much better.)")


if __name__ == "__main__":
    main()
```

**What the program prints (illustrative):**

* For each sample, it outputs the brute-force result, the optimal result, and whether they match the expected value.
* Timing summary comparing the optimal method on 100k elements vs. a smaller brute-force run.

---

## 6) Real-World Use Cases (a few important ones)

1. **Reservoir/Container Planning**
   Modeling the maximum capacity between two walls/dams along a cross-section to estimate storage potential given wall heights.

2. **Signal/Charting Envelopes**
   Given vertical line intensities (e.g., a histogram of measured power), finding farthest two supports that maximize a bounded area — useful in coarse bounding of signals or charts.

3. **Data Visualization / UI Layout**
   When placing two vertical elements with variable heights, find a pair that maximizes the area of content that can fit between them (e.g., a banner/hero region between two columns).

4. **Image Processing (Column Projections)**
   Treat columns as vertical bars (e.g., text column projections) and compute a maximal bounded region to isolate content blocks.

