# Max sum in the configuration

**Difficulty:** Medium
**Accuracy:** 36.56%
**Submissions:** 116K+
**Points:** 4
**Average Time:** 30m

---

## Problem

Given an integer array `arr[]`, find the **maximum** value of the sum of `i * arr[i]` for all `0 ≤ i < arr.size()`.
The only operation allowed is to **rotate** (clockwise or counterclockwise) the array any number of times.

---

## Examples

### Example 1

**Input:** `arr[] = [8, 3, 1, 2]`
**Output:** `29`
**Explanation:** Out of all the possible configurations by rotating the elements:
`arr[] = [3, 1, 2, 8]` gives `(3*0) + (1*1) + (2*2) + (8*3) = 29`, which is maximum.

---

### Example 2

**Input:** `arr[] = [1, 2, 3]`
**Output:** `8`
**Explanation:** Out of all the possible configurations by rotating the elements:
`arr[] = [1, 2, 3]` gives `(1*0) + (2*1) + (3*2) = 8`, which is maximum.

---

### Example 3

**Input:** `arr[] = [4, 13]`
**Output:** `13`

---

## Constraints

* `1 ≤ arr.size() ≤ 10^4`
* `1 ≤ arr[i] ≤ 20`

---

## Expected Complexities

* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Company Tags

* Amazon

---

## Topic Tags

* Arrays
* Data Structures
* Mathematical

---

## Related Articles

* [Maximum Sum `i*arr[i]` Among Rotations Given Array](https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/)

---

---

Here’s a crisp, interview-ready walkthrough for **Max sum in the configuration** (maximize $\sum_{i=0}^{n-1} i \cdot a[i]$ over all rotations).

---

## 2) Intuition + step-by-step dry run

### Key idea (famous recurrence)

Let

* $S = \sum a[i]$ (sum of elements),
* $R_0 = \sum i \cdot a[i]$ (value for the original array),
* $R_k$ be the value after **k clockwise rotations** (moving the last element to the front each time).

If the array is $[a_0, a_1, \dots, a_{n-1}]$, one clockwise rotation makes it $[a_{n-1}, a_0, a_1, \dots, a_{n-2}]$.

**Recurrence**:

$$
R_{k+1} \;=\; R_k \;+\; S \;-\; n \cdot a_{n-1-k}
$$

(we subtract $n \cdot $ the element that just moved to the front).

So we can compute all $R_k$ in **O(n)**:

1. Compute $S$ and $R_0$.
2. For $k = 0 \to n-2$, update $R_{k+1}$ using the recurrence and track the max.

> If you rotate **counter-clockwise** (left), the symmetric recurrence is
> $R_{k+1} = R_k - S + n \cdot a_k$. Either direction works; just be consistent.

### Dry run on `arr = [8, 3, 1, 2]`

* $n=4$, $S = 14$
* $R_0 = 0*8 + 1*3 + 2*1 + 3*2 = 11$

Clockwise rotations:

* $k=0 \to 1$: use $a_{n-1-0} = a_3 = 2$
  $R_1 = 11 + 14 - 4*2 = 17$  (array is `[2, 8, 3, 1]`)
* $k=1 \to 2$: use $a_{n-1-1} = a_2 = 1$
  $R_2 = 17 + 14 - 4*1 = 27$  (array is `[1, 2, 8, 3]`)
* $k=2 \to 3$: use $a_{n-1-2} = a_1 = 3$
  $R_3 = 27 + 14 - 4*3 = 29$  (array is `[3, 1, 2, 8]`) ← **maximum**

Answer = **29** ✅

---

## 3) Python solutions (brute and optimal)

### A) Optimal O(n) / O(1) extra (most expected in interviews)

```python
class Solution:
    def maxSum(self, arr):
        """
        Maximize sum(i * arr[i]) over all rotations.

        Approach:
          - Precompute S = sum(arr) and R0 = sum(i * arr[i]).
          - For k = 1..n-1 (clockwise rotations), use:
                R_next = R_curr + S - n * arr[n - k]
            Track the maximum across all R_k.

        Time:  O(n)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return 0 if n == 0 else 0  # only i=0 term

        S = sum(arr)                           # O(n)
        R0 = sum(i * arr[i] for i in range(n)) # O(n)

        best = R0
        curr = R0
        # After k clockwise rotations, the element moved to front is arr[n - k]
        for k in range(1, n):                  # O(n)
            curr = curr + S - n * arr[n - k]
            if curr > best:
                best = curr
        return best
```

### B) Brute-force O(n²) (clear but too slow for large n)

```python
class SolutionBrute:
    def maxSum(self, arr):
        """
        Try all rotations; compute sum(i * rotated[i]) each time.

        Let rotation s be s clockwise moves.
        The rotated array at index i is arr[(i - s) % n].

        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        if n <= 1:
            return 0 if n == 0 else 0

        best = float("-inf")
        for s in range(n):  # O(n) rotations
            total = 0
            for i in range(n):  # O(n) per rotation
                total += i * arr[(i - s) % n]
            best = max(best, total)
        return best
```

---

## 4) Interview Q\&A (the ones you’ll likely get)

**Q1. Derive the recurrence $R_{k+1} = R_k + S - n \cdot a_{n-1-k}$.**
When you rotate clockwise by one, every element’s index increases by 1 (mod n), so each contributes one extra copy of its value to the sum, i.e., total increase by $S$. The element moved to index 0 contributes $0 \cdot a$ instead of $n \cdot a$ it would have effectively counted in the shift, so we subtract $n \cdot a$ once. Hence $R_{k+1} = R_k + S - n \cdot a_{\text{moved to front}}$.

**Q2. What’s the time/space complexity of the optimal solution?**
**Time:** $O(n)$ — one pass to compute $S$, one for $R_0$, one for the recurrence.
**Space:** $O(1)$ — constant extra variables.

**Q3. Does the solution handle negative numbers or duplicates?**
Yes. The recurrence and summations don’t assume positivity or distinctness.

**Q4. Do we need to actually rotate the array?**
No. Index arithmetic (or the recurrence) avoids any real rotation, saving time and space.

**Q5. What if we rotate left (counter-clockwise) instead?**
Use the symmetric relation: $R_{k+1} = R_k - S + n \cdot a_k$. Both directions are fine; be consistent.

**Q6. Any implementation pitfalls?**

* Mixing up which element is subtracted in the recurrence (off-by-one).
* Recomputing sums naively per rotation (leads to $O(n^2)$).
* Overflow in fixed-width languages (use 64-bit types). Python ints are unbounded.

---

---

Below is a **complete, runnable Python program** for **“Max sum in the configuration”** that:

* Implements the **optimal O(n) / O(1)** algorithm (with a small **O(n²)** brute force for tiny validation),
* Prints **inputs and outputs** for the sample cases,
* Uses **timeit** to report **elapsed time** for each run and total program time, and
* Includes **inline comments** showing **time and space complexity** of each step.

> Recurrence used (clockwise rotation):
> If $S=\sum a[i]$ and $R_k$ is $\sum i\cdot a[i]$ after $k$ clockwise rotations, then
>
> $$
> R_{k+1} = R_k + S - n\cdot a_{n-1-k}
> $$
>
> This lets us compute all rotations in a single pass.

```python
from typing import List
import timeit
import random

# ============================================================
# Optimal O(n) / O(1) solution
# ============================================================

class Solution:
    def maxSum(self, arr: List[int]) -> int:
        """
        Maximize sum(i * arr[i]) over all rotations.

        Steps:
          1) Compute S = sum(arr)                      # Time: O(n) | Space: O(1)
          2) Compute R0 = sum(i * arr[i])              # Time: O(n) | Space: O(1)
          3) For k = 1..n-1, use recurrence            # Time: O(n) | Space: O(1)
                R_next = R_curr + S - n * arr[n - k]
             Track global maximum.

        Overall Time:  O(n)
        Overall Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 0  # only term i=0

        # 1) Sum of elements
        S = sum(arr)  # O(n) time, O(1) space

        # 2) R0 for the original configuration
        R0 = sum(i * arr[i] for i in range(n))  # O(n) time, O(1) space

        best = R0
        curr = R0

        # 3) Iterate over rotations using the recurrence (clockwise)
        # After k clockwise rotations, the element moved to the front is arr[n - k]
        for k in range(1, n):  # O(n) time, O(1) space
            curr = curr + S - n * arr[n - k]
            if curr > best:
                best = curr

        return best


# ============================================================
# Brute-force O(n^2) (for tiny validation only)
# ============================================================

class SolutionBrute:
    def maxSum(self, arr: List[int]) -> int:
        """
        Try all n rotations and compute sum(i * rotated[i]) each time.

        Time:  O(n^2)
        Space: O(1)
        """
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 0

        best = float("-inf")
        for s in range(n):  # rotate s times (clockwise conceptually)
            total = 0
            # rotated[i] = arr[(i - s) % n]
            for i in range(n):
                total += i * arr[(i - s) % n]
            if total > best:
                best = total
        return best


# ============================================================
# Timing & Demo Harness
# ============================================================

def run_case(name: str, arr: List[int], solver) -> None:
    """
    Run one case, print input, output, and timing.

    This function's overhead is O(n) because solver.maxSum is O(n) for the optimal solver.
    """
    t0 = timeit.default_timer()
    ans = solver.maxSum(arr)
    t1 = timeit.default_timer()
    print(f"{name}:")
    print("  arr:", arr)
    print("  maxSum:", ans)
    print(f"  Elapsed: {(t1 - t0):.6f}s\n")


def main():
    print("=== Max sum in the configuration — Examples & Timing ===\n")

    fast = Solution()
    slow = SolutionBrute()  # only for small validation

    # ------------------ Problem examples ------------------
    ex1 = [8, 3, 1, 2]   # expected 29
    ex2 = [1, 2, 3]      # expected 8
    ex3 = [4, 13]        # expected 13

    # Optimal runs
    run_case("Example 1 (optimal)", ex1, fast)
    run_case("Example 2 (optimal)", ex2, fast)
    run_case("Example 3 (optimal)", ex3, fast)

    # Tiny brute validations (optional)
    run_case("Example 1 (brute)", ex1, slow)
    run_case("Example 2 (brute)", ex2, slow)
    run_case("Example 3 (brute)", ex3, slow)

    # ------------------ Random tiny validation ------------------
    random.seed(7)
    tiny = [random.randint(1, 9) for _ in range(10)]  # small so brute OK
    ans_fast = fast.maxSum(tiny)
    ans_slow = slow.maxSum(tiny)
    print("Random tiny validation:")
    print("  arr:", tiny)
    print("  optimal:", ans_fast, " brute:", ans_slow, " -> equal?", ans_fast == ans_slow, "\n")

    # ------------------ Larger performance demo (optimal only) ------------------
    # Build a larger array closer to constraints (e.g., n=10_000)
    n = 10_000
    big = [random.randint(1, 20) for _ in range(n)]  # values per constraint

    t0 = timeit.default_timer()
    _ = fast.maxSum(big)   # O(n)
    t1 = timeit.default_timer()
    print(f"Large input (n={n}) optimal elapsed: {(t1 - t0):.6f}s")


if __name__ == "__main__":
    program_start = timeit.default_timer()
    main()
    program_end = timeit.default_timer()
    print("\n==== TOTAL PROGRAM TIME ====")
    print(f"{(program_end - program_start):.6f}s")
```

---

## 6) Real-World Use Cases (the most relevant ones)

* **Scheduling & Rotations:** When tasks are cyclic and have **position-based weights** (e.g., slot $i$ has weight $i$), you want the rotation of a lineup that maximizes the weighted contribution.
* **Circular Buffers / Ring Queues:** Choosing an **optimal starting point** in a cyclic data structure to maximize a linear scoring function (e.g., playback order, cache warm-up priority).
* **Manufacturing / Assembly Lines:** If stations have **indexed costs/benefits** and items can be **rotated** through positions, pick the rotation that maximizes total yield/throughput score.
* **Ad/Content Carousels:** Given a set of creatives and **position CTR weights**, find the rotation of items that **maximizes expected clicks** under a linear (index-based) position-bias model.
