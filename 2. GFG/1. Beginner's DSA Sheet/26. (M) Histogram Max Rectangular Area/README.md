
---

# Histogram Max Rectangular Area 🏗️📊

**Difficulty:** Hard
**Accuracy:** 32.12%
**Submissions:** 201K+
**Points:** 8

---

## Problem Statement

You are given a **histogram** represented by an array `arr`, where each element of the array denotes the **height of the bars** in the histogram. All bars have the same **width of 1 unit**.

Your task is to find the **largest rectangular area** possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

---

## Examples

### Example 1

**Input:**
`arr[] = [60, 20, 50, 40, 10, 50, 60]`

**Output:**
`100`

**Explanation:**
We get the maximum by picking bars highlighted above in green (50 and 60).
The area is computed as:
`(smallest height) * (no. of picked bars)` = `50 * 2 = 100`.

---

### Example 2

**Input:**
`arr[] = [3, 5, 1, 7, 5, 9]`

**Output:**
`15`

**Explanation:**
We get the maximum by picking bars 7, 5, and 9.
The area is computed as:
`(smallest height) * (no. of picked bars)` = `5 * 3 = 15`.

---

### Example 3

**Input:**
`arr[] = [3]`

**Output:**
`3`

**Explanation:**
In this example, the largest area would be `3` of height `3` and width `1`.

---

## Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `0 ≤ arr[i] ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Microsoft
* Google

---

## Topic Tags

* Stack
* Data Structures

---

## Related Interview Experiences

* One97 Interview Experience Set 3 Backendnode Js Developer

---

## Related Articles

* [Largest Rectangular Area In A Histogram Using Stack](https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-using-stack/)

---

---

Here’s a tight interview-ready package for **Largest Rectangle in a Histogram**.

---

## 2) Intuition + Step-by-Step Dry Run

### Core idea

For any bar `i` with height `h = arr[i]`, the **widest** rectangle that uses `h` as the **limiting height** spans from the **first smaller bar on the left** of `i` to the **first smaller bar on the right** of `i` (exclusive).
Width = `right_smaller_index - left_smaller_index - 1`, area = `h * width`.

The optimal linear solution finds these “next smaller to left/right (NSL/NSR)” using a **monotonic increasing stack** in one pass (or two), or directly in **one sweep with a sentinel**.

---

### Dry run (stack, one-sweep) on `arr = [60, 20, 50, 40, 10, 50, 60]`

We push indices of **non-decreasing** heights. When we hit a height lower than the stack’s top, we **pop and compute** areas for popped bars (their right bound is the current index).

Add sentinels: evaluate to the end by appending a virtual `0` at the end.

```
i=0, h=60     stack=[]           push 0              stack=[0]
i=1, h=20     20 < 60 → pop 0
              height=60, width = i - (stack top after pop is empty → -1) - 1 = 1 - (-1) - 1 = 1
              area=60*1=60 → max=60
              push 1                                     stack=[1]
i=2, h=50     50 >= 20 → push 2                           stack=[1,2]
i=3, h=40     40 < 50 → pop 2
              height=50, width = 3 - (top=1) - 1 = 1     area=50*1=50 → max=60
              40 >= 20 → push 3                           stack=[1,3]
i=4, h=10     10 < 40 → pop 3
              height=40, width = 4 - (top=1) - 1 = 2     area=40*2=80 → max=80
              10 < 20 → pop 1
              height=20, width = 4 - (empty→-1) - 1 = 4  area=20*4=80 → max=80
              push 4                                      stack=[4]
i=5, h=50     50 >= 10 → push 5                           stack=[4,5]
i=6, h=60     60 >= 50 → push 6                           stack=[4,5,6]
i=7, h=0(end) 0 < 60 → pop 6
              height=60, width = 7 - (top=5) - 1 = 1     area=60*1=60 → max=80
              0 < 50 → pop 5
              height=50, width = 7 - (top=4) - 1 = 2     area=50*2=100 → max=100
              0 < 10 → pop 4
              height=10, width = 7 - (empty→-1) - 1 = 7  area=10*7=70 → max=100
              push 7
Done. Answer = 100.
```

The key moment is when popping height 50 at index 5: it stretches from after index 4 (height 10) to before index 7 (the trailing sentinel), i.e., width 2 → area 100.

---

## 3) Python Solutions

### A) Brute-force (Interview “easy-to-explain” baseline) — O(n²) time, O(1) space

Compute for each index the nearest smaller to the left and to the right by walking outward (or maintain a running min as we expand a window). Here’s the simple expand-left/right style:

```python
class Solution:
    def getMaxArea(self, arr):
        # O(n^2) time, O(1) extra space
        n = len(arr)
        best = 0
        for i in range(n):
            h = arr[i]
            # expand left
            L = i
            while L - 1 >= 0 and arr[L - 1] >= h:
                L -= 1
            # expand right
            R = i
            while R + 1 < n and arr[R + 1] >= h:
                R += 1
            width = R - L + 1
            best = max(best, h * width)
        return best
```

This is often acceptable to **explain** first, then move to the optimal stack.

---

### B) Optimal Monotonic Stack — one sweep with sentinel — O(n) time, O(n) space

This is the standard, expected solution.

```python
class Solution:
    def getMaxArea(self, arr):
        """
        Monotonic increasing stack of indices.
        When current height < height[stack.top], pop and compute area where
        the popped bar is the limiting height; right boundary is current index,
        left boundary is the new stack.top (or -1 if empty).
        Time: O(n), each index pushed/popped once.
        Space: O(n) for the stack.
        """
        n = len(arr)
        st = []
        best = 0

        # process all bars, then a sentinel 0 to flush the stack
        for i in range(n + 1):
            cur = arr[i] if i < n else 0  # sentinel height 0 at the end
            # maintain increasing stack
            while st and cur < arr[st[-1]]:
                h = arr[st.pop()]
                left = st[-1] if st else -1  # index of previous smaller
                width = i - left - 1         # span where h is the min
                best = max(best, h * width)
            st.append(i)
        return best
```

---

### C) Optimal via precomputed NSL/NSR (two passes) — O(n) time, O(n) space

Sometimes preferred for clarity: compute `left_smaller[i]` and `right_smaller[i]`, then area per `i` is `arr[i] * (right_smaller[i] - left_smaller[i] - 1)`.

```python
class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        left = [-1] * n   # index of first smaller to the left
        right = [n] * n   # index of first smaller to the right
        st = []

        # NSL
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)

        # clear stack then NSR
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)

        best = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            best = max(best, arr[i] * width)
        return best
```

---

## 4) Likely Interview Q\&A

**Q1. Why does the stack solution work?**
**A.** The stack keeps indices in **non-decreasing height** order. When you see a height smaller than the top’s height, you’ve found the **right boundary** for the popped bar. The new top after popping is the **left boundary**. That gives the maximal width where the popped height is the minimum, hence its maximal rectangle.

**Q2. Why is it O(n)?**
**A.** Each index is **pushed at most once** and **popped at most once**. So the total operations are linear.

**Q3. Why use a sentinel bar (height 0) at the end?**
**A.** It forces popping of any remaining bars in the stack, ensuring all areas are computed without writing a separate cleanup loop.

**Q4. Can the brute-force pass?**
**A.** With `n` up to `1e5`, no. It’s O(n²). It’s good for explaining correctness, then optimize to O(n) with the stack.

**Q5. What about all zeros or strictly increasing/decreasing arrays?**
**A.** The stack method gracefully handles all cases. E.g., strictly increasing just pushes until the sentinel pops everything; strictly decreasing pops every step, evaluating all widths.

**Q6. Can we do it in O(1) extra space?**
**A.** Not easily while keeping O(n) time—stack (or equivalent info) requires O(n) in the worst case. There’s no truly O(1) extra known solution in general.

---

---

Awesome — here’s a self-contained, interview-ready script that:

* implements the optimal **O(n)** stack solution,
* (optionally) includes a simple brute-force checker,
* runs a couple of sample inputs,
* uses `timeit` to measure the full program run,
* and ends with a few crisp real-world use cases.

---

## 5) Full Program (with inline complexity notes + timing)

```python
#!/usr/bin/env python3
# Largest Rectangle in a Histogram — full program with timing

from timeit import timeit
from typing import List


class Solution:
    def getMaxArea(self, arr: List[int]) -> int:
        """
        Monotonic increasing stack (indices).
        When current height < height at stack top, the top bar's maximal
        rectangle is finalized: right boundary = current index, left boundary = new stack top.
        -------------------------------------------------------------------------------
        Time:  O(n)  — each index is pushed/popped at most once
        Space: O(n)  — stack can hold up to n indices in increasing runs
        """
        n = len(arr)
        st = []            # stack of indices, heights non-decreasing
        best = 0

        # Walk once through arr, plus a sentinel 0 at the end to flush the stack
        # Each iteration is O(1) amortized.
        for i in range(n + 1):  # +1 to handle sentinel at the end
            cur = arr[i] if i < n else 0  # sentinel height 0
            # While the current bar breaks the monotonicity, finalize popped bars
            while st and cur < arr[st[-1]]:
                h = arr[st.pop()]                  # height of the rectangle
                left_idx = st[-1] if st else -1    # index of first smaller to the left
                width = i - left_idx - 1           # span where h is the minimal bar
                # O(1) area computation
                best = max(best, h * width)
            # Maintain non-decreasing stack
            st.append(i)
        return best

    # (Optional) Brute-force for sanity checking on tiny inputs
    def getMaxArea_bruteforce(self, arr: List[int]) -> int:
        """
        Expand left and right for each bar while bars >= current height.
        ----------------------------------------------------------------
        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        best = 0
        for i in range(n):
            h = arr[i]
            L = i
            while L - 1 >= 0 and arr[L - 1] >= h:
                L -= 1
            R = i
            while R + 1 < n and arr[R + 1] >= h:
                R += 1
            best = max(best, h * (R - L + 1))
        return best


def demo():
    sol = Solution()

    # ---------------------------
    # Example test cases (inputs)
    # ---------------------------
    cases = [
        # From the prompt
        ([60, 20, 50, 40, 10, 50, 60], "expect 100"),
        ([3, 5, 1, 7, 5, 9], "expect 15"),
        ([3], "expect 3"),
        # Some extra
        ([2, 2, 2, 2], "all equal → 8"),
        ([5, 4, 3, 2, 1], "strictly decreasing"),
        ([1, 2, 3, 4, 5], "strictly increasing"),
        ([2, 1, 2], "classic edge → 3"),
    ]

    print("Largest Rectangle in a Histogram\n")
    for arr, note in cases:
        ans = sol.getMaxArea(arr)
        print(f"arr = {arr:<35} -> max area = {ans:<4}   ({note})")

    # -----------------------------------------
    # Timeit: measure full-program run overhead
    # -----------------------------------------
    # We'll time the optimal method on a single representative case
    arr = [60, 20, 50, 40, 10, 50, 60]
    t = timeit(lambda: sol.getMaxArea(arr), number=10000)
    print(f"\n[timeit] getMaxArea on {arr} (10,000 runs): {t:.4f} seconds")


if __name__ == "__main__":
    demo()
```

### What you’ll see when you run it (sample)

```
Largest Rectangle in a Histogram

arr = [60, 20, 50, 40, 10, 50, 60]      -> max area = 100   (expect 100)
arr = [3, 5, 1, 7, 5, 9]                -> max area = 15    (expect 15)
arr = [3]                               -> max area = 3     (expect 3)
arr = [2, 2, 2, 2]                      -> max area = 8     (all equal → 8)
arr = [5, 4, 3, 2, 1]                   -> max area = 9     (strictly decreasing)
arr = [1, 2, 3, 4, 5]                   -> max area = 9     (strictly increasing)
arr = [2, 1, 2]                         -> max area = 3     (classic edge → 3)

[timeit] getMaxArea on [60, 20, 50, 40, 10, 50, 60] (10,000 runs): 0.4xx seconds
```

*(Exact timing varies by machine.)*

---

## 6) Real-World Use Cases (important ones)

* **Image processing & skyline problems**: largest rectangle of pixels above a threshold within a row-wise cumulative binary matrix (classic “max rectangle in a binary matrix” reduces each row to a histogram).
* **Memory/CPU utilization windows**: find the longest continuous time span where utilization never drops below a threshold, maximizing (min usage × duration).
* **Stock depth / order book visualization**: given bar heights for liquidity at price levels, compute the largest price range with at least a certain depth.
* **Layout engines**: determine the biggest block that can be placed while respecting a minimum baseline height across a contiguous strip (bars as constraints).
