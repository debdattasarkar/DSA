# Minimum time to fulfill all orders

**Difficulty:** Hard
**Accuracy:** 63.04%
**Submissions:** 14K+
**Points:** 8

---

## Problem Statement

Geek is organizing a party at his house. For the party, he needs exactly **n donuts** for the guests. Geek decides to order the donuts from a nearby restaurant, which has **m chefs**, and each chef has a **rank r**.

A chef with rank **r** can make:

* **1 donut in the first r minutes**
* **1 more donut in the next 2r minutes**
* **1 more donut in the next 3r minutes**, and so on.

That is, the time taken by a chef with rank `r` to make `k` donuts is:

```
r * (1 + 2 + 3 + ... + k)
```

For example, a chef with rank `2`:

* 1 donut → 2 minutes
* 2 donuts → 2 + 4 = 6 minutes
* 3 donuts → 2 + 4 + 6 = 12 minutes

A chef can move on to making the next donut **only after completing the previous one**.
**All the chefs can work simultaneously.**

Since it’s time for the party, Geek wants to know the **minimum time** required to complete **n donuts**.

Return an integer denoting the **minimum time**.

---

## Examples

### Example 1

**Input:**

```
n = 10
rank[] = [1, 2, 3, 4]
```

**Output:**

```
12
```

**Explanation:**

* Chef with rank 1 can make 4 donuts in time:
  `1 + 2 + 3 + 4 = 10 minutes`
* Chef with rank 2 can make 3 donuts in time:
  `2 + 4 + 6 = 12 minutes`
* Chef with rank 3 can make 2 donuts in time:
  `3 + 6 = 9 minutes`
* Chef with rank 4 can make 1 donut in time:
  `4 minutes`

Total donuts = `4 + 3 + 2 + 1 = 10`
Minimum time required = **12 minutes**

---

### Example 2

**Input:**

```
n = 8
rank[] = [1, 1, 1, 1, 1, 1, 1, 1]
```

**Output:**

```
1
```

**Explanation:**
All chefs have rank 1, so each chef can make 1 donut in 1 minute.

Total donuts = `1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8`
Minimum time required = **1 minute**

---

## Constraints

* 1 ≤ n ≤ 10³
* 1 ≤ m ≤ 10⁴
* 1 ≤ rank[i] ≤ 100

---

## Expected Complexities

* **Time Complexity:** `O(m * log n)`
* **Auxiliary Space:** `O(1)`

---

## Topic Tags

* Binary Search
* Algorithms

---

## Related Articles

* **Minimum Time To Fulfill All Orders**

---

---

## 2) Explanation (core idea)

Each chef with rank `r` makes donuts with increasing time:

* 1st donut: `r`
* 2nd donut: `2r`
* 3rd donut: `3r`
  So time for `k` donuts:
  [
  r(1+2+\dots+k) = r \cdot \frac{k(k+1)}{2}
  ]

We need **minimum time T** such that **all chefs together can make at least `n` donuts** in `T`.

This is a classic **“minimize time” → binary search on answer** problem:

* If in time `T` we can make `>= n` donuts → `T` is feasible → try smaller
* Else → need more time → try larger

### Feasibility check for a chef

Given `T` and rank `r`, find max `k` such that:
[
r \cdot \frac{k(k+1)}{2} \le T
]
We can compute `k` by:

* either loop adding `r,2r,3r...` (k is small since n ≤ 1000)
* or solve quadratic (faster math)

Since constraints are small for `n`, the **loop-per-chef** is super interview-friendly and fast enough.

---

## Step-by-step Dry Run (Example 1)

**n = 10, ranks = [1,2,3,4]**

We binary search `T`.

### Upper bound idea

Worst case: fastest chef rank=1 makes all `10` donuts:
Time = `1*(1+2+...+10) = 55`
So search range: `low=0, high=55`

### Check T = 27 (mid of 0..55)

For each chef, count donuts until next donut exceeds T.

* rank 1: times 1,2,3,4,5,6... cumulative:
  1 (1), 3 (2), 6 (3), 10 (4), 15 (5), 21 (6), 28 (7) → exceeds at 7
  ✅ makes 6 donuts
* rank 2: 2,4,6,8... cumulative:
  2 (1), 6 (2), 12 (3), 20 (4), 30 (5) exceeds at 5
  ✅ makes 4 donuts
* rank 3: 3,6,9... cumulative:
  3 (1), 9 (2), 18 (3), 30 (4) exceeds
  ✅ makes 3 donuts
* rank 4: 4,8,12... cumulative:
  4 (1), 12 (2), 24 (3), 40 (4) exceeds
  ✅ makes 3 donuts

Total = 6+4+3+3 = 16 ≥ 10 → **feasible**, try smaller → `high = 27`

### Check T = 13 (mid of 0..27)

* rank 1: 1+2+3+4=10 (4 donuts), next +5 => 15 > 13 → 4
* rank 2: 2+4=6 (2), next +6 => 12 (3), next +8 => 20 > 13 → 3
* rank 3: 3+6=9 (2), next +9 => 18 > 13 → 2
* rank 4: 4+8=12 (2), next +12 => 24 > 13 → 2

Total = 4+3+2+2 = 11 ≥ 10 → feasible → `high = 13`

### Check T = 6 (mid of 0..13)

* rank 1: 1+2+3=6 → 3 donuts
* rank 2: 2+4=6 → 2 donuts
* rank 3: 3 → 1 donut, next +6 exceeds
* rank 4: 4 → 1 donut
  Total = 3+2+1+1 = 7 < 10 → not feasible → `low = 7`

Continue… eventually answer becomes **12** (matches sample).

---

# 3) Python Solutions (Brute + Optimized)

## A) Brute force on time (too slow conceptually, but simple)

Try increasing `T` from 0 upward until feasible.
Not recommended, but good to explain baseline.

**Time:** can be large, not acceptable.
**Space:** O(1)

```python
class Solution:
    def minTime(self, ranks, n):
        # Brute idea: keep increasing time until we can make n donuts
        # Not efficient for large time range

        def can_make(time_limit):
            total = 0
            for r in ranks:
                current_time = 0
                next_donut = 1
                # Keep making donuts until time would exceed time_limit
                while True:
                    needed = r * next_donut
                    if current_time + needed > time_limit:
                        break
                    current_time += needed
                    total += 1
                    next_donut += 1
                    if total >= n:
                        return True
            return total >= n

        time_limit = 0
        while True:
            if can_make(time_limit):
                return time_limit
            time_limit += 1
```

---

## B) Optimized (Most expected): Binary Search on Time + loop feasibility

This is the standard interview answer.

**Time:** `O(m * log(ans))` (m = number of chefs)
**Space:** `O(1)`

```python
class Solution:
    def minTime(self, ranks, n):
        # Edge case
        if n == 0:
            return 0

        # ---------- Feasibility check ----------
        # Time: O(m * donuts_per_chef) but donuts_per_chef <= n (n<=1000)
        # Space: O(1)
        def can_make_in_time(time_limit):
            total_donuts = 0

            for rank in ranks:
                time_spent = 0
                donut_number = 1

                # Each chef makes donuts until time exceeds limit
                while True:
                    next_time = rank * donut_number
                    if time_spent + next_time > time_limit:
                        break
                    time_spent += next_time
                    total_donuts += 1
                    donut_number += 1

                    if total_donuts >= n:  # early stop
                        return True

            return total_donuts >= n

        # ---------- Binary search bounds ----------
        # Low: 0
        low = 0

        # High: fastest chef makes all n donuts
        # Time = r_min * (1+2+...+n) = r_min * n*(n+1)/2
        fastest_rank = min(ranks)
        high = fastest_rank * n * (n + 1) // 2

        # ---------- Binary Search on answer ----------
        # Time: O(log high)
        while low < high:
            mid = (low + high) // 2
            if can_make_in_time(mid):
                high = mid
            else:
                low = mid + 1

        return low
```

---

## C) Optimized variant: Feasibility using math (quadratic) instead of loop

This is faster per chef (nice if m is huge), but slightly more “mathy”.

We need max `k` such that:
`r * k*(k+1)/2 <= T`

**Time:** `O(m log(ans))` with small constant
**Space:** `O(1)`

```python
import math

class Solution:
    def minTime(self, ranks, n):
        if n == 0:
            return 0

        def donuts_by_chef(rank, time_limit):
            # Solve k(k+1)/2 <= time_limit / rank
            # k^2 + k - 2*(time_limit/rank) <= 0
            value = (2 * time_limit) // rank
            # k ≈ floor( (-1 + sqrt(1 + 4*value)) / 2 )
            k = int((math.isqrt(1 + 4 * value) - 1) // 2)
            return k

        def can_make_in_time(time_limit):
            total = 0
            for r in ranks:
                total += donuts_by_chef(r, time_limit)
                if total >= n:
                    return True
            return total >= n

        low = 0
        fastest_rank = min(ranks)
        high = fastest_rank * n * (n + 1) // 2

        while low < high:
            mid = (low + high) // 2
            if can_make_in_time(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

---

# 4) Interview memory + Q&A

## 10-second approach pitch

“Minimum time + monotonic feasibility ⇒ **binary search on time**.
For a given time, compute donuts each chef can make (either incremental loop or quadratic).
Sum donuts; if ≥ n, time works.”

## Mnemonic to remember

**“TIME → CHECK → COUNT → CUT”**

* Binary search **TIME**
* **CHECK** if possible
* **COUNT** donuts in that time
* **CUT** search space (left if possible, right if not)

Or 1-liner:
**“BS on time, count donuts, shrink.”**

---

## Expected interviewer questions + crisp answers

**Q1. Why binary search works here?**
A. Because feasibility is monotonic: if we can make `n` donuts in time `T`, we can also make them in any time `> T`.

**Q2. How do you compute donuts made by one chef in time T?**
A. Chef with rank `r` needs `r*(1+2+...+k)=r*k*(k+1)/2` for `k` donuts.
Find largest `k` satisfying it (loop or quadratic).

**Q3. What bounds do you use for time?**
A. `low=0`. `high = min_rank * n*(n+1)/2` (fastest chef makes all donuts).

**Q4. Complexity?**
A. `O(m * log(high))`. With loop-based check, each chef makes at most `n` donuts so it’s still fast for `n<=1000`.

**Q5. Can you early-stop in feasibility?**
A. Yes, once total donuts ≥ n, return True immediately.

**Q6. What if ranks had duplicates or large m?**
A. Duplicates are fine. For large m, use the quadratic count per chef to keep feasibility `O(m)` with small constant.

---

---

## 5) Real-World Use Cases (few, very relatable)

1. **Kitchen / Cloud “auto-scaling” capacity planning**
   Multiple workers (or servers) get slower per extra job (warm-up / queue / context switching). Question: *minimum time to finish N jobs with M workers*.

2. **Manufacturing line with fatigue / setup overhead**
   Each next unit takes longer (tool heating, calibration, operator fatigue). Find minimum shift time to complete a target.

3. **Batch processing / ETL pipelines**
   Multiple machines process batches; each subsequent batch takes longer due to I/O contention. Need minimum time window to finish K batches.

4. **Delivery / order fulfillment**
   Pickers/packers slow down as orders accumulate (walking distance / sorting overhead). Find minimum time to fulfill N orders with available staff.

---

## 6) Full Program (timed end-to-end + sample input/output + inline complexity)

This full program uses the **most expected approach**:
✅ **Binary search on time** + ✅ **feasibility check (count donuts in time T)**

**Input format supported (simple):**

* Line1: `n`  (donuts needed)
* Line2: ranks list (space-separated), e.g. `1 2 3 4`

If no stdin is provided, it runs **demo mode** using the sample.

```python
import sys
import time


class Solution:
    def minTime(self, ranks, n):
        """
        Binary search on time.

        Time Complexity:
            - Feasibility check: O(m * k) where k is donuts per chef in given time,
              but overall k <= n and n <= 1000 -> fast in practice.
            - Binary search iterations: O(log(high))
            => Total ~ O(m * n * log(high)) worst-case, but with n<=1000 it is acceptable.
              (Commonly stated as O(m * log(high)) with optimized counting.)

        Space Complexity:
            O(1) extra space.
        """

        # Edge case
        if n <= 0:
            return 0

        # ---------- Feasibility check: can we make >= n donuts in time_limit? ----------
        # Time: O(m * donuts_made_per_chef) (each chef increments donut count)
        # Space: O(1)
        def can_make_in_time(time_limit):
            total_donuts = 0

            for rank in ranks:
                time_spent = 0
                donut_number = 1  # making the 1st, 2nd, 3rd... donut

                # Each next donut takes rank * donut_number minutes
                while True:
                    next_donut_time = rank * donut_number
                    if time_spent + next_donut_time > time_limit:
                        break
                    time_spent += next_donut_time
                    total_donuts += 1
                    donut_number += 1

                    # Early exit saves time
                    if total_donuts >= n:
                        return True

            return total_donuts >= n

        # ---------- Binary search bounds ----------
        # low = 0 minutes
        low = 0

        # high = fastest chef (min rank) makes all n donuts alone:
        # time = r * (1 + 2 + ... + n) = r * n*(n+1)/2
        fastest_rank = min(ranks)  # Time: O(m)
        high = fastest_rank * n * (n + 1) // 2  # Time: O(1)

        # ---------- Binary Search on answer ----------
        # Time: O(log(high))
        while low < high:
            mid = (low + high) // 2
            if can_make_in_time(mid):
                high = mid
            else:
                low = mid + 1

        return low


def main():
    # Measure total runtime of the whole program (parse + compute + print)
    program_start = time.perf_counter()

    data = sys.stdin.read().strip()
    solver = Solution()

    if not data:
        # ---------------- DEMO MODE ----------------
        n = 10
        ranks = [1, 2, 3, 4]

        answer = solver.minTime(ranks, n)

        print("Input:")
        print("n =", n)
        print("ranks =", ranks)
        print("\nOutput:")
        print(answer)

    else:
        # ---------------- INPUT MODE ----------------
        # Expected input:
        # n
        # r1 r2 r3 ... rm
        lines = [line.strip() for line in data.splitlines() if line.strip()]

        # Parse n
        n = int(lines[0])

        # Parse ranks
        ranks = list(map(int, lines[1].split()))

        answer = solver.minTime(ranks, n)
        print(answer)

    program_end = time.perf_counter()
    total_runtime_ms = (program_end - program_start) * 1000.0
    print(f"\n[Total program runtime: {total_runtime_ms:.3f} ms]")


if __name__ == "__main__":
    main()
```

### Example demo output (when run without stdin)

For `n=10`, `ranks=[1,2,3,4]` → Output should be **12**, plus runtime.

