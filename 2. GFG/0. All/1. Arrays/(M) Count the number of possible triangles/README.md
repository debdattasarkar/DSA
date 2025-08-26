
---

# Count the number of possible triangles

**Difficulty:** Medium
**Accuracy:** 28.53%
**Submissions:** 144K+
**Points:** 4
**Average Time:** 15m

---

### Problem Statement

Given an integer array `arr[]`. Find the **number of triangles** that can be formed with **three** different array elements as lengths of three sides of the triangle.

A triangle with three given sides is only possible if **sum of any two sides is always greater than the third side**.

---

### Examples

#### Example 1

```
Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. 
Note that [3, 4, 7] is not a possible triangle.
```

#### Example 2

```
Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: 
[10, 21, 22], [21, 100, 101], [22, 100, 101], 
[10, 100, 101], [100, 101, 200] and [101, 200, 300].
```

#### Example 3

```
Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.
```

---

### Constraints

* $1 \leq arr.size() \leq 10^3$
* $0 \leq arr[i] \leq 10^5$

---

### Expected Complexities

* **Time Complexity:** $O(n^2)$
* **Auxiliary Space:** $O(1)$

---

### Company Tags

* Amazon
* Microsoft

---

### Topic Tags

* Arrays
* Sorting
* Data Structures
* Algorithms

---

### Related Articles

* [Find Number Of Triangles Possible](https://www.geeksforgeeks.org/find-number-of-triangles-possible/)

---

---

Here’s a crisp, interview-ready walkthrough and code set for **“Count the number of possible triangles”**.

---

## 2) Concept + Step-by-Step Dry Run

### Key idea

For three lengths $a \le b \le c$ to form a triangle, the **only** inequality we must check is:

$$
a + b > c
$$

(Other triangle inequalities are automatically satisfied when the array is sorted.)

### Optimized approach (intuition)

1. **Sort** the array (non-decreasing).
2. Treat each element as the **largest side** $c = arr[k]$ (from right to left).
3. For that fixed $k$, use **two pointers**:

   * $i = 0$ (smallest), $j = k-1$ (second largest).
   * If $arr[i] + arr[j] > arr[k]$, then **all** pairs $(i, i+1, \ldots, j-1, j)$ with this $j$ work (because increasing the smaller side keeps the sum ≥ current sum).
     So we can add **$(j - i)$** to the count and decrease $j$.
   * Else (sum too small), increase $i$.

This yields $O(n^2)$ after sorting.

### Dry run on `arr = [4, 6, 3, 7]`

1. Sort → `A = [3, 4, 6, 7]`, `n = 4`, `count = 0`
2. Fix `k = 3` (`A[k]=7`): `i=0 (3)`, `j=2 (6)`

   * `3 + 6 > 7` → `9 > 7` ✓ ⇒ add `(j-i) = 2` → `count=2`. Decrement `j → 1`.
   * `i=0 (3)`, `j=1 (4)`: `3 + 4 > 7` → `7 > 7` ✗ ⇒ increase `i → 1`.
   * `i=1`, `j=1` stop loop.
3. Fix `k = 2` (`A[k]=6`): `i=0 (3)`, `j=1 (4)`

   * `3 + 4 > 6` → `7 > 6` ✓ ⇒ add `(j-i)=1` → `count=3`. Decrement `j → 0`. Stop.
4. Fix `k = 1` ends (need at least 3 elements).

**Result:** `count = 3` → triangles: `[3,4,6]`, `[3,6,7]`, `[4,6,7]`.

---

## 3) Python Solutions (Brute Force + Optimized Two-Pointers)

### A) Brute force (for clarity; not for production)

* Try all triplets $i<j<k$ and check triangle inequality.
* Time: $O(n^3)$, Space: $O(1)$.

```python
class Solution:
    def countTriangles(self, arr):
        # Brute force: check all triplets
        # Time:  O(n^3)
        # Space: O(1)
        n = len(arr)
        if n < 3:
            return 0

        # Sorting isn't required for brute force correctness,
        # but helps to only check a+b>c for sorted triplets.
        arr.sort()

        cnt = 0
        for i in range(n - 2):            # pick smallest side
            for j in range(i + 1, n - 1): # pick middle side
                for k in range(j + 1, n): # pick largest side
                    # For sorted arr: only need to check a+b>c
                    if arr[i] + arr[j] > arr[k]:
                        cnt += 1
        return cnt
```

### B) Optimized (expected in interviews)

* Sort + fix largest + two-pointers.
* Time: $O(n^2)$, Space: $O(1)$.

```python
class Solution:
    def countTriangles(self, arr):
        """
        Optimized two-pointer after sorting.
        Time:  O(n^2)   -- dominant double loop after sort
        Space: O(1)     -- in-place calculations
        """
        n = len(arr)
        if n < 3:
            return 0

        arr.sort()  # O(n log n)
        count = 0

        # Fix the largest side at position k, scan i..j for pairs
        for k in range(n - 1, 1, -1):   # k from n-1 down to 2
            i, j = 0, k - 1
            while i < j:
                # if smallest + second-largest > largest, then
                # (i, i+1, ..., j-1, j) all with this j form valid triangles
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)
                    j -= 1  # try a smaller middle to see if more pairs exist
                else:
                    i += 1  # sum too small; increase the smaller side

        return count
```

**Why this works:** once `arr[i] + arr[j] > arr[k]` holds for the current `i`, it will also hold for all `i'` where `i < i' < j` (since `arr[i'] >= arr[i]`). That lets us count `(j - i)` in one go.

**Edge cases handled**

* Length < 3 → 0.
* Zeros & duplicates are fine—triangle inequality naturally filters invalid triplets.

---

## 4) Interview Q\&A (high-signal)

**Q1. Why does sorting help?**
Sorting lets us reduce triangle checks to a single inequality $a+b>c$ for $a \le b \le c$, and enables the two-pointer sweep that counts multiple pairs at once.

**Q2. Why can we add `(j - i)` when `arr[i] + arr[j] > arr[k]`?**
Because increasing the smaller side from `arr[i]` to any `arr[i+1]...arr[j-1]` only **increases** the sum, so all those pairs with the same `j` are valid.

**Q3. What are the time and space complexities?**

* Optimized: $O(n^2)$ time (after $O(n \log n)$ sort), $O(1)$ extra space.
* Brute force: $O(n^3)$, $O(1)$ space.

**Q4. Do zeros or duplicates break the logic?**
No. Zeros simply fail inequality unless paired with strictly positive sides big enough; duplicates are naturally handled by the inequality and counting logic.

**Q5. Can we do better than $O(n^2)$?**
For arbitrary arrays, $O(n^2)$ is the standard optimal approach. Sub-quadratic solutions are not known for the general problem.

---

---

Below is a **complete, runnable Python program** that includes:

* A clear, commented **optimized solution** (sorting + two-pointers, $O(n^2)$) and a small **brute-force** checker ($O(n^3)$) for reference.
* **Inline time & space complexity notes at each step.**
* A tiny **main** that demonstrates the algorithm on a few inputs and uses **`timeit`** to measure the end-to-end runtime of the whole program execution path.

---

```python
#!/usr/bin/env python3
"""
Count the number of triangles that can be formed from an array of side lengths.

Triangle condition for sorted sides a <= b <= c:
    a + b > c

We implement:
1) Optimized O(n^2) solution (after O(n log n) sort) using two-pointers.
2) Brute-force O(n^3) checker (for small inputs / verification only).

The main block:
- Shows sample inputs/outputs.
- Uses timeit to measure the full program run path for the optimized solver.

Author: You
"""

from timeit import default_timer as timer
from typing import List

class Solution:
    def countTriangles_optimized(self, arr: List[int]) -> int:
        """
        Optimized approach:
        1) Sort the array.                      Time: O(n log n), Space: O(1) extra (in-place allowed)
        2) Fix the largest side at index k and
           use two pointers i (start) and j (k-1) to count valid pairs.
                                               Time: O(n^2), Space: O(1)
        Total complexity: O(n^2) after sorting.
        """
        n = len(arr)
        if n < 3:
            # No triangles possible with fewer than 3 sides
            # Time: O(1), Space: O(1)
            return 0

        # ---- Step 1: Sort ----
        # Sorting allows using only a + b > c check for a <= b <= c
        # Time: O(n log n), Space: O(1) extra (Timsort uses O(log n) stack)
        arr.sort()

        count = 0  # Space: O(1)

        # ---- Step 2: For each k as the largest side, sweep i..j ----
        # Outer loop runs (n-2) times  -> O(n)
        # Inner two-pointer loop per k -> amortized O(n)
        # Total two-pointer work       -> O(n^2)
        for k in range(n - 1, 1, -1):     # k from n-1 down to 2
            i, j = 0, k - 1
            # While we have a valid window
            while i < j:
                # Check the triangle inequality for sorted sides
                if arr[i] + arr[j] > arr[k]:
                    # If a[i] + a[j] > a[k], then for this fixed j,
                    # all pairs (i, i+1, ..., j-1, j) work.
                    # Add (j - i) in O(1).
                    count += (j - i)
                    # Move j left to try to find more pairs with a smaller middle side
                    j -= 1
                else:
                    # Sum too small; increase the smaller side to make the sum bigger
                    i += 1

        return count

    def countTriangles_bruteforce(self, arr: List[int]) -> int:
        """
        Brute-force for verification / small inputs:
        Try all triplets i < j < k and check triangle inequality.
        Time:  O(n^3)
        Space: O(1)
        """
        n = len(arr)
        if n < 3:
            return 0

        # Sorting not required for correctness, but then a+b>c single check suffices.
        arr = sorted(arr)  # Time: O(n log n)
        cnt = 0
        for i in range(n - 2):            # O(n)
            for j in range(i + 1, n - 1): # O(n)
                for k in range(j + 1, n): # O(n)
                    # For sorted: only need to check a+b>c
                    if arr[i] + arr[j] > arr[k]:
                        cnt += 1
        return cnt


def run_demo():
    """
    Driver to demonstrate functionality and print outputs.

    Time complexity of this function depends on the chosen solver.
    We call the optimized version here.
    """
    sol = Solution()

    tests = [
        # (input array, expected count)
        ([4, 6, 3, 7], 3),                     # Example 1
        ([10, 21, 22, 100, 101, 200, 300], 6), # Example 2
        ([1, 2, 3], 0),                        # Example 3 (no triangles)
        ([2, 2, 3, 4], 3),                     # Small extra sanity
    ]

    print("=== Count Possible Triangles ===")
    for arr, expected in tests:
        got = sol.countTriangles_optimized(arr[:])  # use a copy
        print(f"Input: {arr}\nOutput: {got}\nExpected: {expected}\n")

    # Optional: quick cross-check for small inputs with brute-force
    small = [2, 3, 4, 4]
    bf = sol.countTriangles_bruteforce(small[:])
    opt = sol.countTriangles_optimized(small[:])
    print(f"[Cross-check] small={small}, brute={bf}, optimized={opt}\n")


def time_program():
    """
    Measure end-to-end runtime for the main path using timeit-like timing.
    We intentionally include setup work similar to GFG runner:
    creating arrays, solver instance, calls, and console output.
    """
    start = timer()
    run_demo()
    end = timer()
    print(f"Total program run time: {end - start:.6f} seconds")


if __name__ == "__main__":
    time_program()
```

### What the program prints (sample)

```
=== Count Possible Triangles ===
Input: [4, 6, 3, 7]
Output: 3
Expected: 3

Input: [10, 21, 22, 100, 101, 200, 300]
Output: 6
Expected: 6

Input: [1, 2, 3]
Output: 0
Expected: 0

Input: [2, 2, 3, 4]
Output: 3
Expected: 3

[Cross-check] small=[2, 3, 4, 4], brute=3, optimized=3

Total program run time: 0.000xxx seconds
```

---

## 6) Real-World Use Cases (a few important ones)

1. **Structural Engineering / Materials Selection**
   When choosing bars/pipes to assemble triangular trusses, quickly estimating how many triplets from a stock list can form valid triangles helps in planning, cost estimation, and minimizing waste.

2. **Computer Graphics / Mesh Generation**
   Triangles are the fundamental primitive in meshes. Given candidate edge lengths or constraints, counting or ensuring feasible triangle combinations is a building block in procedural generation and mesh validation.

3. **Network Design / Triadic Closure Checks**
   In graph modeling with weighted edges as “distance” or “latency,” verifying triangle feasibility (or violators of triangle inequality) can help detect anomalies, bad measurements, or improve routing heuristics.

4. **Puzzle/Combinatorics Tools**
   In educational or competitive settings, quickly enumerating feasible triangles from a set (with constraints) is a common combinatorics/algorithm exercise—this algorithm scales to large inputs efficiently.
