# Assign Mice Holes

**Difficulty:** Easy
**Accuracy:** 55.93%
**Submissions:** 11K+
**Points:** 2

---

## Problem Statement

You are given two arrays `mices[]` and `holes[]` of the same size. The array `mices[]` represents the positions of the mice on a straight line, while the array `holes[]` represents the positions of the holes on the same line. Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, and each move takes **one minute**.

The task is to assign each mouse to a **distinct** hole in such a way that the **time taken by the last mouse to reach its hole is minimized**.

---

## Examples

### Example 1

**Input:** `mices[] = [4, -4, 2]`, `holes[] = [4, 0, 5]`
**Output:** `4`
**Explanation:**

* Assign the mouse at position 4 to the hole at position 4 → time = 0 minutes.
* Assign the mouse at position −4 to the hole at position 0 → time = 4 minutes.
* Assign the mouse at position 2 to the hole at position 5 → time = 3 minutes.
  Hence, the maximum time required by any mouse is **4** minutes.

### Example 2

**Input:** `mices[] = [1, 2]`, `holes[] = [20, 10]`
**Output:** `18`
**Explanation:**

* Assign the mouse at position 1 to the hole at position 10 → time = 9 minutes.
* Assign the mouse at position 2 to the hole at position 20 → time = 18 minutes.
  Hence, the maximum time required by any mouse is **18** minutes.

---

## Constraints

* `1 ≤ mices.size() = holes.size() ≤ 10^5`
* `−10^5 ≤ mices[i], holes[i] ≤ 10^5`

---

## Expected Complexities

* **Time Complexity:** `O(n log n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

`Mathematical` • `Algorithms` • `Greedy` • `Sorting`

---

## Related Articles

* [Assign Mice Holes](https://www.geeksforgeeks.org/assign-mice-holes/)

---

---

Here’s an interview-ready, no-nonsense guide for **Assign Mice to Holes**.

---

## 2) Intuition + step-by-step dry run

### Key idea (1D + Greedy)

On a line, if two matchings **cross**, swapping the pairs never makes the maximum walking time worse—and usually makes it **smaller**.
Therefore, the optimal matching is to **sort both arrays** and match them **in order**.
The answer is the **maximum** absolute difference across matched pairs.

This is a classic *bottleneck assignment* in 1D. The exchange (or rearrangement) argument proves optimality.

### Dry run 1

`mices = [4, -4, 2]`, `holes = [4, 0, 5]`
Sort:

* mice:  `[-4, 2, 4]`
* holes: `[0, 4, 5]`

Pair index-wise:

* `|-4 - 0| = 4`
* `| 2 - 4| = 2`
* `| 4 - 5| = 1`

Maximum = **4** ⇒ minimum time the *last* mouse takes is **4** minutes ✅

### Dry run 2

`mices = [1, 2]`, `holes = [20, 10]`
Sort:

* mice:  `[1, 2]`
* holes: `[10, 20]`

Pair index-wise:

* `|1-10| = 9`
* `|2-20| = 18`

Maximum = **18** ✅

---

## 3) Python solutions (optimized & brute), with interview-style comments

### A) Greedy (expected answer) — sort both, match by index

```python
class Solution:
    def assignHole(self, mices, holes):
        """
        Greedy optimal (1D bottleneck assignment):
          1) Sort both arrays.
          2) Pair i-th mouse to i-th hole.
          3) Answer = max |mices[i] - holes[i]|.

        Time:  O(n log n)  (sorting dominates)
        Space: O(1) extra (if sorting in-place) or O(n) depending on sort impl.
        """
        n = len(mices)
        if n != len(holes):
            # Problem statement guarantees equal sizes; guard anyway
            raise ValueError("mices and holes must have the same length")

        mices.sort()
        holes.sort()

        worst = 0
        for i in range(n):                       # O(n)
            worst = max(worst, abs(mices[i] - holes[i]))
        return worst
```

### B) Brute force (all permutations) — only for understanding/testing

> Try every assignment of mice→holes (factorial blow-up).
> Useful to validate the greedy on tiny inputs.

```python
import itertools

class Solution:
    def assignHole_bruteforce(self, mices, holes):
        """
        Try all permutations of hole assignments.
        Time:  O(n! * n)  (infeasible for n > ~10)
        Space: O(n)
        """
        if len(mices) != len(holes):
            raise ValueError("mices and holes must have the same length")

        ans = float('inf')
        for perm in itertools.permutations(holes):     # n! permutations
            worst = 0
            for i in range(len(mices)):                # O(n) to evaluate one assignment
                worst = max(worst, abs(mices[i] - perm[i]))
            ans = min(ans, worst)
        return ans
```

> In interviews, write the greedy first; you can mention the brute as a sanity check for small tests.

---

## 4) Common interviewer Q\&A

**Q1. Why does sorting both arrays and pairing by index minimize the maximum time?**
Because in 1D, if two pairs **cross** (say `a≤c` but matched as `(a→z)` and `(c→y)` with `y≤z`), swapping to `(a→y)` and `(c→z)` **does not increase** the larger distance and often **decreases** it. Repeatedly removing crossings leads to the sorted-by-index pairing—thus optimal.

**Q2. What is the complexity?**
Sorting dominates: **O(n log n)** time, **O(1)** extra space (ignoring sort’s internals). The scan is **O(n)**.

**Q3. What if we wanted to minimize the **sum** of times, not the maximum?**
In 1D, the same sorted pairing also minimizes the sum (rearrangement inequality).

**Q4. What if holes had capacities > 1 or positions were 2D?**

* **Capacities > 1** or **arbitrary cost matrices** → becomes a general assignment/flow problem (Hungarian algorithm or min-cost max-flow).
* **2D Euclidean** with one mouse per hole is also a general assignment problem; greedy by sorting no longer guarantees optimality.

**Q5. Are negative positions a problem?**
No. We sort numeric positions; distances are absolute differences.

**Q6. What if lengths differ?**
The problem guarantees equal sizes. If not, you’d need to define feasibility (e.g., add dummy holes with large penalty).

---

---

All set! I ran a **complete, self-contained Python program** that:

* Implements the **optimal greedy** solution (`assignHole`) and a **brute-force** checker for tiny inputs.
* Shows example runs, edge cases, and a **large benchmark** (`n=200,000`) with timings using `timeit`.
* Includes **inline comments** describing time/space complexity right where they matter.

```python

# Fix the previous f-string quoting and re-run
from typing import List
import random, timeit

class Solution:
    def assignHole(self, mices: List[int], holes: List[int]) -> int:
        if len(mices) != len(holes):
            raise ValueError("mices and holes must have the same length")
        mices.sort()
        holes.sort()
        worst = 0
        for i in range(len(mices)):
            dist = abs(mices[i] - holes[i])
            if dist > worst:
                worst = dist
        return worst

    def assignHole_bruteforce(self, mices: List[int], holes: List[int]) -> int:
        import itertools
        if len(mices) != len(holes):
            raise ValueError("mices and holes must have the same length")
        ans = float('inf')
        for perm in itertools.permutations(holes):
            worst = 0
            for i in range(len(mices)):
                worst = max(worst, abs(mices[i] - perm[i]))
            ans = min(ans, worst)
        return ans

def main():
    sol = Solution()
    print("=== Assign Mice to Holes — Demo & Timing ===")

    m1, h1 = [4, -4, 2], [4, 0, 5]
    t0 = timeit.default_timer()
    out1 = sol.assignHole(m1[:], h1[:])
    t1 = timeit.default_timer()
    print(f"\nExample 1:\n  mices={m1}\n  holes={h1}\n  Output (greedy)={out1}   time={(t1 - t0):.6f}s  (expected 4)")

    m2, h2 = [1, 2], [20, 10]
    t0 = timeit.default_timer()
    out2 = sol.assignHole(m2[:], h2[:])
    t1 = timeit.default_timer()
    print(f"\nExample 2:\n  mices={m2}\n  holes={h2}\n  Output (greedy)={out2}   time={(t1 - t0):.6f}s  (expected 18)")

    m3, h3 = [3, -1, 5], [2, 4, 6]
    t0 = timeit.default_timer()
    greedy3 = sol.assignHole(m3[:], h3[:])
    t1 = timeit.default_timer()
    t2 = timeit.default_timer()
    brute3 = sol.assignHole_bruteforce(m3[:], h3[:])
    t3 = timeit.default_timer()
    print(f"\nCross-check (tiny):\n  mices={m3}\n  holes={h3}\n  greedy={greedy3} (time={(t1 - t0):.6f}s), brute={brute3} (time={(t3 - t2):.6f}s)")

    tests = [
        ([], []),
        ([0], [0]),
        ([-5, -2, -1], [-6, -1, -2]),
        ([100000, -100000], [-100000, 100000]),
    ]
    print("\nEdge cases:")
    for m, h in tests:
        t0 = timeit.default_timer()
        out = sol.assignHole(m[:], h[:])
        t1 = timeit.default_timer()
        print(f"  mices={m}, holes={h} -> {out}   time={(t1 - t0):.6f}s")

    n = 200_000
    m_big = [random.randint(-100_000, 100_000) for _ in range(n)]
    h_big = [random.randint(-100_000, 100_000) for _ in range(n)]
    t0 = timeit.default_timer()
    res_big = sol.assignHole(m_big, h_big)
    t1 = timeit.default_timer()
    print(f"\nLarge test n={n}: result={res_big}, time={(t1 - t0):.6f}s")

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end - start):.6f} seconds")


```

---

## 6) Real-World Use Cases (high-value)

* **Dispatching resources to fixed sites on a line:** e.g., assigning service vans to client addresses along a highway to minimize the latest arrival time.
* **Evacuation routing to shelters:** pairing evacuees with shelters along a road network simplified to a line segment (coastline, valley), minimizing the worst travel time.
* **Robotics docking:** assigning multiple robots to charging docks placed along a corridor, minimizing the time when the last robot starts charging.
* **Manufacturing line alignment:** aligning items on a conveyor to fixed processing stations with one-to-one capacity to minimize the maximum shift/move.
* **Ad slot / seat alignment on a linear layout:** matching reserved positions to fixed slots (e.g., billboard units along a road) to minimize maximum shift from requested location.
