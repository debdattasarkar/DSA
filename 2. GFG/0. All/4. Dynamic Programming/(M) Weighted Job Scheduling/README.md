

---

# 💼 Weighted Job Scheduling

### Difficulty: Medium

**Accuracy:** 70.5%
**Submissions:** 5K+
**Points:** 4

---

## 🧠 Problem Statement

Given a 2D array **jobs[][]** of size **n × 3**, where each row represents a single job with the following details:

* **jobs[i][0]**: Start time of the job
* **jobs[i][1]**: End time of the job
* **jobs[i][2]**: Profit earned by completing the job

Find the **maximum profit** you can earn by scheduling **non-overlapping jobs**.

---

### Note:

Two jobs are said to be **non-overlapping** if the end time of one job is less than or equal to the start time of the next job.
If a job ends at time X, another job can start **exactly at time X**.

---

## 🧩 Examples

### Example 1

**Input:**

```
jobs[][] = [[1, 2, 50],
            [3, 5, 20],
            [6, 19, 100],
            [2, 100, 200]]
```

**Output:**

```
250
```

**Explanation:**
The first and fourth jobs with the time ranges **[1, 2]** and **[2, 100]** can be chosen to give a maximum profit of **50 + 200 = 250**.

---

### Example 2

**Input:**

```
jobs[][] = [[1, 3, 60],
            [2, 5, 50],
            [4, 6, 70],
            [5, 7, 30]]
```

**Output:**

```
130
```

**Explanation:**
The first and third jobs with the time ranges **[1, 3]** and **[4, 6]** can be chosen to give a maximum profit of **60 + 70 = 130**.

---

## ⚙️ Constraints

* ( 1 \leq jobs.size() \leq 10^5 )
* ( 1 \leq jobs[i][0] < jobs[i][1] \leq 10^9 )
* ( 1 \leq jobs[i][2] \leq 10^4 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n log n)
* **Auxiliary Space:** O(n)

---

## 🏷️ Topic Tags

* Dynamic Programming
* Binary Search
* Recursion

---

## 📚 Related Articles

* [**Weighted Job Scheduling**](https://www.geeksforgeeks.org/weighted-job-scheduling/)

---

---

awesome — basing this squarely on the **bottom-up DP + binary search** approach you referenced.

# 2) Explanation + step-by-step dry run

## Problem in one line

Each job is `(start, end, profit)`. Pick a subset of **non-overlapping** jobs (a job may start exactly when a previous one ends) to **maximize total profit**.

## Key idea (Weighted Interval Scheduling)

1. **Sort jobs by end time**.
2. For each job `i`, find the number of jobs that finish **≤ start[i]** among those before it. That count is `j` and represents the prefix you’re allowed to combine with job `i`. We find `j` with **binary search** on the sorted end times.
3. DP over prefixes:

```
dp[i] = max profit using the first i jobs in end-time order (i = 0..n)
Transition for job i (1-based in dp, 0-based in jobs):
    j = count of jobs ending ≤ start of jobs[i-1]
    dp[i] = max( dp[i-1],   profit[i-1] + dp[j] )
Answer = dp[n]
```

Intuition: either **skip** job `i-1` (carry `dp[i-1]`) or **take** it (earn `profit[i-1]` + best compatible prefix `dp[j]`).

### Dry run on Example

```
jobs = [(1,3,60),(2,5,50),(4,6,70),(5,7,30)]
1) Sort by end:
    idx  job        ends[]
     0   (1,3,60)    3
     1   (2,5,50)    5
     2   (4,6,70)    6
     3   (5,7,30)    7
2) DP (dp size = n+1 = 5; dp[0]=0)

i=1 (job (1,3,60)):
  start=1 → j = count of ends ≤ 1 among first 0 jobs = 0
  take = 60 + dp[0] = 60
  skip = dp[0] = 0
  dp[1] = 60

i=2 (job (2,5,50)):
  start=2 → ends ≤ 2 among first 1 end [3]? none → j=0
  take = 50 + dp[0] = 50
  skip = dp[1] = 60
  dp[2] = 60

i=3 (job (4,6,70)):
  start=4 → in ends [3,5] among first 2 → last ≤ 4 is 3 → j=1
  take = 70 + dp[1]=70+60=130
  skip = dp[2]=60
  dp[3] = 130

i=4 (job (5,7,30)):
  start=5 → in ends [3,5,6] among first 3 → last ≤5 is 5 → j=2
  take = 30 + dp[2]=30+60=90
  skip = dp[3]=130
  dp[4] = 130

Answer dp[4] = **130** (choose jobs (1,3,60) and (4,6,70)).
```

---

# 3) Python solutions (brute ➜ memo ➜ bottom-up)

All match your required signature:

```python
class Solution: 
    def maxProfit(self, jobs):
        # code here
```

### A) Brute force (include/skip) — teaching aid, exponential

```python
class Solution:
    def maxProfit(self, jobs):
        """
        Try all subsets by include/skip.
        Time:  O(2^n)
        Space: O(n) recursion depth
        Only for understanding; not for large n.
        """
        # Sort by start to make "next non-overlap" search simpler
        jobs.sort(key=lambda x: x[0])
        n = len(jobs)

        def next_index(i):
            # first j > i with jobs[j].start >= jobs[i].end
            end_i = jobs[i][1]
            j = i + 1
            while j < n and jobs[j][0] < end_i:
                j += 1
            return j

        from functools import lru_cache
        @lru_cache(None)
        def solve(i):
            if i == n:
                return 0
            skip = solve(i + 1)
            take = jobs[i][2] + solve(next_index(i))
            return max(skip, take)

        return solve(0)
```

### B) Top-down DP + binary search on **end times** — O(n log n)

```python
from bisect import bisect_right

class Solution:
    def maxProfit(self, jobs):
        """
        Memoized recursion over end-sorted jobs.
        dp(i) = best profit using jobs up to index i (0..i)
        Time:  O(n log n)   (sort + per-call predecessor via binary search)
        Space: O(n)         (memo + arrays)
        """
        jobs.sort(key=lambda x: x[1])           # sort by end
        ends = [e for _, e, _ in jobs]

        from functools import lru_cache
        @lru_cache(None)
        def best(i):
            if i < 0:
                return 0                         # base: no job
            s, e, p = jobs[i]
            j = bisect_right(ends, s) - 1        # last end ≤ start
            take = p + best(j)                   # take job i
            skip = best(i - 1)                   # skip job i
            return take if take > skip else skip

        return best(len(jobs) - 1)
```

### C) **Bottom-up DP + binary search (recommended)** — O(n log n)

*(This is the exact style you referenced; iterative so it can’t blow the stack.)*

```python
from bisect import bisect_right

class Solution:
    def maxProfit(self, jobs):
        """
        Iterative DP on end-sorted jobs.
        dp[i] = max profit using the first i jobs (i = 0..n)
        Transition with job k = i-1:
            j = count of jobs that finish ≤ start[k] among first (i-1)
            dp[i] = max(dp[i-1], profit[k] + dp[j])
        Time:  O(n log n)
        Space: O(n)
        """
        jobs.sort(key=lambda x: x[1])            # 1) sort by end
        n = len(jobs)
        ends = [e for _, e, _ in jobs]           # for binary search on predecessors
        dp = [0] * (n + 1)                       # dp[0] = 0 (no job)

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]                # current job (0-based)
            # among the first (i-1) jobs (ends[:i-1]), count those with end ≤ s
            j = bisect_right(ends, s, 0, i - 1)  # predecessor prefix length
            take = p + dp[j]                     # take job → add best up to j jobs
            skip = dp[i - 1]                     # skip job
            dp[i] = take if take > skip else skip

        return dp[n]
```

> Implementation detail: we used `bisect_right(ends, start)` (not `bisect_left`) because **equality is allowed** (`end ≤ next start`).

---

# 4) Interview quick-recall + Q&A

## 5-line skeleton (write this on your scratchpad)

```
sort jobs by end
ends = [end times]
for each job i in 1..n:
    j = rightmost end ≤ start[i-1]    # bisect_right
    dp[i] = max(dp[i-1], profit[i-1] + dp[j])
return dp[n]
```

**Mnemonic:** **“Sort-End → Prev-Bin → Max(Skip, Take)”**

* Sort by **End**
* find **Prev** index via **Bin**ary search
* choose **Max** of **Skip** or **Take**

## Likely questions & crisp answers

**Q1. Why sort by end time?**
So that any compatible predecessor of job `i` lies in the already processed prefix, enabling DP and binary search.

**Q2. Why `bisect_right`?**
Because non-overlap allows equality (`end ≤ next start`). `bisect_right(ends, start)` returns the **count** of jobs with `end ≤ start`.

**Q3. Define your DP state.**
`dp[i]` = maximum profit using the **first i end-sorted jobs**. Transition: `dp[i] = max(dp[i-1], profit[i-1] + dp[j])`.

**Q4. Time/space complexity?**
Sorting `O(n log n)`, each of `n` iterations does one binary search `O(log n)` → overall **O(n log n)** time; **O(n)** space.

**Q5. How to reconstruct the chosen set of jobs?**
Keep a `choose[i]` flag when setting `dp[i]`. If `dp[i] == dp[i-1]`, skip; else record job `i-1` and move `i ← j`.

**Q6. What if jobs must start strictly after previous ends (no equality)?**
Use `j = bisect_left(ends, start) - 1` (or equivalently use `bisect_left` for the count and adjust).

**Q7. My recursive version crashed—why?**
Without correct memoization/base, recursion depth and repeated work explode. The bottom-up iterative version avoids recursion entirely.

You’re set — explain the recurrence, cite the binary search predecessor, and code the bottom-up DP in a few lines.

---

---

great — here are the sharp, interviewer-friendly extras you asked for.

# 5) Real-World Use Cases (quick + relatable)

* **Ad slot selection on a single page/app view:** Each ad campaign runs for a time window and pays a profit. Choose non-overlapping campaigns to maximize revenue. (Equality allowed → one can start exactly when another ends.)
* **Meeting room with paid sessions:** A trainer gets paid per session; pick sessions that don’t overlap to maximize total pay.
* **Cloud batch jobs on a single VM:** Each job blocks the VM during its interval and yields profit on completion. Schedule a subset to maximize total profit.
* **Runway / dock allocation:** Each arrival/departure reserves the runway/dock for a window and generates fees; schedule to maximize fees without conflicts.
* **Freelancer gigs:** Projects have start/end and pay. Choose a non-overlapping set to maximize income.

All map directly to the weighted interval scheduling DP: **sort by end → choose max of skip vs take(prev-compatible + profit).**

---

# 6) Full Python Program (timed, with inline time/space notes)

* Uses the **bottom-up DP + binary search** approach (iterative; no recursion depth risk).
* Includes two sample inputs (those from the prompt) and prints outputs + per-run timings.

```python
"""
Weighted Job Scheduling — Full Program
--------------------------------------
Given jobs = [(start, end, profit)], select a set of non-overlapping jobs
(end <= next start allowed) that maximizes total profit.

Approach (DP over end-sorted jobs):
    1) Sort jobs by end time.                         # O(n log n) time, O(1) extra
    2) For each job i, find j = count of jobs that
       end <= start[i] using binary search.           # O(log n) per i
    3) dp[i] = max(dp[i-1], profit[i-1] + dp[j])      # O(1) per i
Overall:
    Time:  O(n log n)
    Space: O(n) for dp array
"""

from bisect import bisect_right
import timeit

class Solution:
    def maxProfit(self, jobs):
        """
        Iterative DP on end-sorted jobs.

        Args:
            jobs: List[Tuple[int,int,int]] -> (start, end, profit)

        Returns:
            int: maximum achievable profit.

        Complexity (step-by-step):
            - Sort by end time:        O(n log n) time, O(1) extra
            - Build ends list:         O(n) time, O(n) space
            - Loop i=1..n:
                * Binary search prev:  O(log n) time
                * Transition compute:  O(1) time
              Total loop:              O(n log n) time
            - DP array size:           O(n) space
        """
        # ----- Step 1: sort by end time (critical for DP predecessor logic) -----
        jobs.sort(key=lambda x: x[1])                   # O(n log n)

        n = len(jobs)
        if n == 0:
            return 0

        # ----- Step 2: precompute end times for binary search -----
        ends = [e for _, e, _ in jobs]                  # O(n) time, O(n) space

        # dp[i] = best profit using first i jobs (i from 0..n), dp[0] = 0
        dp = [0] * (n + 1)                              # O(n) space

        # ----- Step 3: fill DP iteratively -----
        for i in range(1, n + 1):                       # runs n times
            s, e, p = jobs[i - 1]

            # Among the first (i-1) jobs, how many end <= s?
            # bisect_right returns that count directly.
            j = bisect_right(ends, s, 0, i - 1)         # O(log n)

            # Option A: take job i-1 → earn p + best up to j jobs
            take_profit = p + dp[j]                     # O(1)

            # Option B: skip job i-1 → keep dp[i-1]
            skip_profit = dp[i - 1]                     # O(1)

            # Best for first i jobs
            dp[i] = take_profit if take_profit > skip_profit else skip_profit  # O(1)

        return dp[n]


# --------------------------- Demo + Timing ---------------------------
if __name__ == "__main__":
    # Example 1 from prompt
    jobs1 = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
    # Example 2 from prompt
    jobs2 = [(1, 3, 60), (2, 5, 50), (4, 6, 70), (5, 7, 30)]

    sol = Solution()

    # Time each evaluation exactly once with timeit
    t1 = timeit.timeit(lambda: sol.maxProfit(jobs1.copy()), number=1)
    res1 = sol.maxProfit(jobs1.copy())

    t2 = timeit.timeit(lambda: sol.maxProfit(jobs2.copy()), number=1)
    res2 = sol.maxProfit(jobs2.copy())

    print("Input 1:", jobs1)
    print("Maximum Profit 1:", res1)
    print(f"Run Time 1: {t1:.8f} s")
    print()
    print("Input 2:", jobs2)
    print("Maximum Profit 2:", res2)
    print(f"Run Time 2: {t2:.8f} s")
```

### Sample output (what you should see)

```
Input 1: [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
Maximum Profit 1: 250
Run Time 1: 0.00000xx s

Input 2: [(1, 3, 60), (2, 5, 50), (4, 6, 70), (5, 7, 30)]
Maximum Profit 2: 130
Run Time 2: 0.00000xx s
```

**Why this is interview-ready**

* You clearly explain **state**, **transition**, and **why binary search works** (end ≤ start).
* The code is iterative (**can’t** blow the stack), `O(n log n)` time, `O(n)` space.
* The driver prints **inputs**, **answers**, and **timings**, demonstrating end-to-end correctness and performance.
