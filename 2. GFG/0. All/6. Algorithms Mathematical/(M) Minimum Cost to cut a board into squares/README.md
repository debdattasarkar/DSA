# Minimum Cost to cut a board into squares

**Difficulty:** Medium
**Accuracy:** 60.83%
**Submissions:** 19K+
**Points:** 4

---

## Problem Statement

You are given a board of dimensions **n × m** that needs to be cut into **n · m** squares.

* **x\[]**: Cost of making a cut **along the vertical edges** (length-wise).
* **y\[]**: Cost of making a cut **along the horizontal edges** (width-wise).

Each time you make a cut, the cost of that cut is multiplied by the current number of segments in the perpendicular direction (because that cut is applied across all those segments).

**Goal:** Find the **minimum total cost** required to cut the board into squares optimally.

---

## Examples

### Example 1

**Input:**
`n = 4, m = 6, x[] = [2, 1, 3, 1, 4], y[] = [4, 1, 2]`
**Output:** `42`

**Explanation (one optimal sequence):**

Pick cuts in descending cost order, multiplying each cut by the number of current segments in the perpendicular direction.

1. Pick `4` (from **x**) → **vertical** cut, cost = `4 × (horizontal segments = 2)` = **4**.
   Vertical segments = 2, Total = **4**.
2. Pick `4` (from **y**) → **horizontal** cut, cost = `4 × (vertical segments = 2)` = **8**.
   Horizontal segments = 2, Total = **12**.
3. Pick `3` (from **x**) → **vertical** cut, cost = `3 × (horizontal segments = 2)` = **6**.
   Vertical segments = 3, Total = **18**.
4. Pick `2` (from **x**) → **vertical** cut, cost = `2 × (horizontal segments = 2)` = **4**.
   Vertical segments = 4, Total = **22**.
5. Pick `2` (from **y**) → **horizontal** cut, cost = `2 × (vertical segments = 4)` = **8**.
   Horizontal segments = 3, Total = **30**.
6. Pick `1` (from **x**) → **vertical** cut, cost = `1 × (horizontal segments = 3)` = **3**.
   Vertical segments = 5, Total = **33**.
7. Pick `1` (from **x**) → **vertical** cut, cost = `1 × (horizontal segments = 3)` = **3**.
   Vertical segments = 6, Total = **36**.
8. Pick `1` (from **y**) → **horizontal** cut, cost = `1 × (vertical segments = 6)` = **6**.
   Horizontal segments = 4, **Total = 42**.

---

### Example 2

**Input:**
`n = 4, m = 4, x[] = [1, 1, 1, 1], y[] = [1, 1, 1]`
**Output:** `15`

**Explanation (one optimal sequence):**

1. Pick `1` (from **y**) → horizontal cut, cost = `1 × (vertical segments = 1)` = **1**.
   Horizontal segments = 2, Total = **1**.
2. Pick `1` (from **y**) → horizontal cut, cost = `1 × (vertical segments = 1)` = **1**.
   Horizontal segments = 3, Total = **2**.
3. Pick `1` (from **y**) → horizontal cut, cost = `1 × (vertical segments = 1)` = **1**.
   Horizontal segments = 4, Total = **3**.
4. Pick `1` (from **x**) → vertical cut, cost = `1 × (horizontal segments = 4)` = **4**.
   Vertical segments = 2, Total = **7**.
5. Pick `1` (from **x**) → vertical cut, cost = `1 × (horizontal segments = 4)` = **4**.
   Vertical segments = 3, Total = **11**.
6. Pick `1` (from **x**) → vertical cut, cost = `1 × (horizontal segments = 4)` = **4**.
   Vertical segments = 4, **Total = 15**.

---

## Constraints

* `2 ≤ n, m ≤ 10^3`
* `1 ≤ x[i], y[i] ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n log n + m log m)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

Greedy • Algorithms

---

## Related Articles

* [Minimum Cost Cut Board Squares](https://www.geeksforgeeks.org/minimum-cost-cut-board-squares/)

---

---

Got it! Let’s lock in the greedy idea, walk through an example step-by-step, and then give neat, interview-ready Python solutions (with comments). I’ll also add the typical Q\&A you’ll get on this problem.

---

## 2) Intuition + Step-by-step Dry Run

### Problem recap

* You have an **n × m** board to cut into **n·m** unit squares.
* `x[i]` = cost of a **vertical** cut (length-wise). There are `m-1` such cuts.
* `y[i]` = cost of a **horizontal** cut (width-wise). There are `n-1` such cuts.
* When you make a cut, the **cost is multiplied** by the number of pieces in the **perpendicular** direction.

  * Vertical cut cost = `x[i] * (#horizontal_segments)`
  * Horizontal cut cost = `y[i] * (#vertical_segments)`
* Initially `vertical_segments = 1`, `horizontal_segments = 1`.

### Greedy idea (why it works)

Always make the **most expensive** remaining cut **first**, because earlier cuts get multiplied by **smaller** segment counts (cheaper overall). This is a classic **sort-descending** greedy with an exchange-argument proof.

---

### Dry run (Example 1)

```
n = 4, m = 6
x = [2, 1, 3, 1, 4]   # vertical cut costs (m-1 = 5)
y = [4, 1, 2]         # horizontal cut costs (n-1 = 3)
```

Sort both in **descending** order:

```
x -> [4, 3, 2, 1, 1]
y -> [4, 2, 1]
```

Start: vertical\_segments v = 1, horizontal\_segments h = 1, total = 0

We always take the larger of next x vs next y:

1. max=4 (tie: choose either). Say take **x=4** (vertical):
   cost += 4 \* h = 4 \* 1 = 4 → total=4; v=2
2. next max= **y=4** (horizontal):
   cost += 4 \* v = 4 \* 2 = 8 → total=12; h=2
3. next max= **x=3**:
   cost += 3 \* h = 3 \* 2 = 6 → total=18; v=3
4. next max= **x=2**:
   cost += 2 \* h = 2 \* 2 = 4 → total=22; v=4
5. next max= **y=2**:
   cost += 2 \* v = 2 \* 4 = 8 → total=30; h=3
6. next max= **x=1**:
   cost += 1 \* h = 1 \* 3 = 3 → total=33; v=5
7. next max= **x=1**:
   cost += 1 \* h = 1 \* 3 = 3 → total=36; v=6
8. remaining **y=1**:
   cost += 1 \* v = 1 \* 6 = 6 → total=42; h=4

**Answer = 42** ✅

---

## 3) Python solutions (expected in interviews)

### A) Canonical Greedy (two sorted lists) — **O((n+m) log(n+m))** time, **O(1)** extra space

```python
class Solution:
    def minCost(self, n, m, x, y):
        """
        Greedy: sort both cost arrays descending and always pick
        the next larger cut cost first.
        
        Time:  O((n+m) log(n+m)) due to sorting
        Space: O(1) extra (sorting in-place is fine; result uses O(1))
        """
        # Sort descending so we consume largest costs first
        x.sort(reverse=True)  # vertical cuts (m-1)
        y.sort(reverse=True)  # horizontal cuts (n-1)

        i = j = 0                     # pointers in x and y
        v_segments = 1                # number of vertical segments (columns)
        h_segments = 1                # number of horizontal segments (rows)
        total = 0

        # While both lists still have cuts left, pick the costlier next cut
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                # Take vertical cut: cost multiplied by current #horizontal segments
                total += x[i] * h_segments
                v_segments += 1
                i += 1
            else:
                # Take horizontal cut: cost multiplied by current #vertical segments
                total += y[j] * v_segments
                h_segments += 1
                j += 1

        # Any remaining vertical cuts
        while i < len(x):
            total += x[i] * h_segments
            v_segments += 1
            i += 1

        # Any remaining horizontal cuts
        while j < len(y):
            total += y[j] * v_segments
            h_segments += 1
            j += 1

        return total
```

### B) Alternate style: Merge all cuts then sort once — **O((n+m) log(n+m))**

Sometimes interviewers like this unification trick. You push all cuts into one list with a tag and sort once.

```python
class SolutionAlt:
    def minCost(self, n, m, x, y):
        """
        Single sort on combined list of cuts (cost, type),
        where type is 'V' or 'H'. Process in descending order.
        
        Time:  O((n+m) log(n+m))
        Space: O(n+m) to store merged cuts (fine for interviews)
        """
        cuts = [(c, 'V') for c in x] + [(c, 'H') for c in y]
        cuts.sort(reverse=True)  # highest cost first

        v_segments = 1
        h_segments = 1
        total = 0

        for cost, typ in cuts:
            if typ == 'V':
                total += cost * h_segments
                v_segments += 1
            else:  # 'H'
                total += cost * v_segments
                h_segments += 1

        return total
```

> There is **no polynomial DP** that beats this greedy here; the greedy is optimal and standard for this problem.

---

## 4) Interviewer Q\&A (what they usually probe)

**Q1. Why does the greedy “take the largest cut first” work?**
*Exchange argument:* If you do a smaller cut before a larger one, the larger cut gets multiplied by a **larger** perpendicular segment count later → more expensive. Swapping their order (do larger first) never increases cost and often reduces it. Repeating this swap argument yields a schedule sorted by decreasing cost.

**Q2. What’s the multiplier for a cut?**

* **Vertical cut** cost is multiplied by the current number of **horizontal segments**.
* **Horizontal cut** cost is multiplied by the current number of **vertical segments**.

**Q3. Initial segment counts?**
`v_segments = 1` and `h_segments = 1` (the full board). Each cut increases its own direction’s segment count by 1.

**Q4. What if two next costs are equal?**
Either order works; you can pick arbitrarily. The final total will be the same.

**Q5. Time and space complexity?**

* Sorting dominates: **O((n+m) log(n+m))** time.
* Processing is linear. Extra space is **O(1)** for the two-array method (in-place sort), or **O(n+m)** for the merged-list variant.

**Q6. Any pitfalls?**

* Don’t multiply by the wrong segment count (remember: **perpendicular**).
* Don’t forget to process the leftover cuts after one list finishes.

---

---

Here’s a complete, runnable script with **inline complexity notes**, **sample inputs & outputs**, and **time measurements** using `timeit`.

```python
from typing import List
import timeit
import random

# ============================================================
# Minimum Cost to Cut a Board Into Squares
# Greedy: take the largest cost cut first (descending sort),
# multiply by count of segments in the PERPENDICULAR direction.
# ============================================================

class Solution:
    def minCost(self, n: int, m: int, x: List[int], y: List[int]) -> int:
        """
        Greedy (canonical two-array version).
        - Sort x (vertical costs) and y (horizontal costs) in descending order.
        - At each step pick the larger next cut; multiply by segments in
          the perpendicular direction; then increase that direction's segments.

        Time:
          Sorting:  O((n + m) log(n + m))  # (m-1) in x, (n-1) in y
          Merge-like pass: O(n + m)
          Overall:  O((n + m) log(n + m))
        Space:
          O(1) extra if we sort in-place (ignoring input-list ownership).
        """
        # O(m log m)
        x.sort(reverse=True)  # vertical cuts (affect vertical segments count)
        # O(n log n)
        y.sort(reverse=True)  # horizontal cuts (affect horizontal segments count)

        i = j = 0
        v_segments = 1  # # of vertical segments (columns)   -- O(1)
        h_segments = 1  # # of horizontal segments (rows)    -- O(1)
        total = 0       # accumulated cost                    -- O(1)

        # O(n + m) loop overall
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                # Take vertical cut; cost multiplied by current horizontal segments
                total += x[i] * h_segments     # O(1)
                v_segments += 1                # O(1)
                i += 1
            else:
                # Take horizontal cut; cost multiplied by current vertical segments
                total += y[j] * v_segments     # O(1)
                h_segments += 1                # O(1)
                j += 1

        # Remaining vertical cuts (if any)
        while i < len(x):
            total += x[i] * h_segments         # O(1) each
            v_segments += 1
            i += 1

        # Remaining horizontal cuts (if any)
        while j < len(y):
            total += y[j] * v_segments         # O(1) each
            h_segments += 1
            j += 1

        return total


# Optional: a single-sort variant (same complexity; shown for completeness).
class SolutionAlt:
    def minCost(self, n: int, m: int, x: List[int], y: List[int]) -> int:
        """
        Merge x & y, tag each as 'V' or 'H', sort once descending, then scan.
        Time:  O((n + m) log(n + m)), Space: O(n + m)
        """
        cuts = [(c, 'V') for c in x] + [(c, 'H') for c in y]  # O(n + m)
        cuts.sort(reverse=True)                               # O((n+m) log(n+m))
        v_segments = h_segments = 1
        total = 0
        for cost, typ in cuts:                                # O(n + m)
            if typ == 'V':
                total += cost * h_segments
                v_segments += 1
            else:
                total += cost * v_segments
                h_segments += 1
        return total


# ---------------- Demo / main with timing ----------------
def main():
    solver = Solution()
    solver_alt = SolutionAlt()

    print("=== Minimum Cost to Cut Board — Demo & Timing ===\n")

    # Example 1 (from prompt)
    n, m = 4, 6
    x = [2, 1, 3, 1, 4]
    y = [4, 1, 2]
    t0 = timeit.default_timer()
    ans = solver.minCost(n, m, x[:], y[:])  # use copies to keep inputs intact
    t1 = timeit.default_timer()
    print(f"Example 1: n={n}, m={m}, x={x}, y={y}")
    print(f"  Output: {ans}  (expected 42)  time={(t1 - t0):.6f}s\n")

    # Example 2 (from prompt)
    n, m = 4, 4
    x = [1, 1, 1, 1]
    y = [1, 1, 1]
    t0 = timeit.default_timer()
    ans = solver.minCost(n, m, x[:], y[:])
    t1 = timeit.default_timer()
    print(f"Example 2: n={n}, m={m}, x={x}, y={y}")
    print(f"  Output: {ans}  (expected 15)  time={(t1 - t0):.6f}s\n")

    # Quick cross-check vs. single-sort variant on random tests
    print("-- Random cross-checks vs single-sort variant --")
    random.seed(7)
    for _ in range(5):
        n = random.randint(2, 20)
        m = random.randint(2, 20)
        # (m-1) vertical cuts, (n-1) horizontal cuts
        x = [random.randint(1, 10) for _ in range(m - 1)]
        y = [random.randint(1, 10) for _ in range(n - 1)]
        res1 = solver.minCost(n, m, x[:], y[:])
        res2 = solver_alt.minCost(n, m, x[:], y[:])
        verdict = "OK" if res1 == res2 else "MISMATCH"
        print(f"n={n}, m={m}, x={x}, y={y} -> {res1} vs {res2}  [{verdict}]")
    print()

    # Larger benchmark to show scaling (still fast)
    print("-- Larger benchmark --")
    n, m = 1000, 1200
    x = [random.randint(1, 1000) for _ in range(m - 1)]
    y = [random.randint(1, 1000) for _ in range(n - 1)]
    t0 = timeit.default_timer()
    ans = solver.minCost(n, m, x, y)
    t1 = timeit.default_timer()
    print(f"n={n}, m={m} -> result computed. time={(t1 - t0):.6f}s")


if __name__ == "__main__":
    start_all = timeit.default_timer()
    main()
    end_all = timeit.default_timer()
    print("\n==== TOTAL MAIN RUNTIME ====")
    print(f"{(end_all - start_all):.6f} seconds")
```

---

## 6) Real-World Use Cases (high-impact only)

* **Manufacturing sheet cutting** (glass, metal, plywood): Minimize saw/laser cut cost where each pass cost scales with the number of strips already created in the perpendicular direction.
* **Image/map tiling pipelines:** When splitting large rasters into tiles, “cut” passes (I/O/compute) multiply across existing stripes; greedy order cuts compute time/cost.
* **Cloud data partitioning:** Dividing a large 2D data grid into shards where repartition steps incur costs proportional to perpendicular shard counts; optimal ordering reduces total processing cost.
