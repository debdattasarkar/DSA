# Skip the work

**Difficulty:** Medium
**Accuracy:** 48.19%
**Submissions:** 13K+
**Points:** 4

---

Given an array `A[]` denoting the time taken to complete `N` tasks, determine the minimum amount of time required to finish the tasks considering that you can skip any task, **but skipping two consecutive tasks is forbidden**.

---

## Example 1

**Input:**
`N = 2`
`A[] = [10, 20]`
**Output:** `10`
**Explanation:** we can take time of 10 units and skip 20 units time.

---

## Example 2

**Input:**
`N = 4`
`A[] = [10, 5, 7, 10]`
**Output:** `12`
**Explanation:** we can skip both the tens and pick 5 and 7 only.

---

## Your Task

You don't need to read input or print anything. Your task is to complete the function `minAmount()` which accepts array `A[]` and its size `N` as input parameter and returns minimum amount of time required to finish the tasks.

---

## Expected Complexities

* **Expected Time Complexity:** `O(N)`
* **Expected Auxiliary Space:** `O(1)`

---

## Constraints

* `1 ≤ N ≤ 10^6`

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Articles

* Minimum Time To Finish Tasks Without Skipping Two Consecutive

---

---

awesome—let’s nail this like an interview.

# 2) Explanation + step-by-step dry run

**Problem.** You have `N` tasks with times `A[i]`. You may **skip** tasks, but **you can’t skip two consecutive tasks**. Find the minimum total time you must spend.

### Two equivalent ways to think about it

1. **Direct two-state DP (minimize done time).**
   Keep two values after processing up to index `i`:

   * `do`  = minimum time if you **do** task `i`
   * `skip`= minimum time if you **skip** task `i` (only allowed if `i-1` was done)

   Transitions for the next task `i` with cost `A[i]`:

   ```
   new_do   = min(do, skip) + A[i]   # do i (previous may be done or skipped)
   new_skip = do                     # skip i (previous must be done)
   ```

   Initialize at `i=0`: `do = A[0]`, `skip = 0`.
   Answer: `min(do, skip)` after the last index.

2. **Complement trick (House Robber).**
   Minimizing **done** time ≡ `total_sum(A) - (maximum sum of times you can **skip**)`
   with the restriction “no two skipped are adjacent”.
   That second part is exactly the classic **House Robber**: choose non-adjacent elements to **maximize** their sum.

Both run in **O(N) time** and **O(1) space**.

---

## Dry run on the samples

### Example 1

`A = [10, 20]`

* Start: `do=10`, `skip=0`
* i=1 (20):
  `new_do = min(10,0)+20 = 20`
  `new_skip = 10`
  → `do=20`, `skip=10`
  Answer `min(20,10)=10`. (Do task 0, skip task 1.)

### Example 2

`A = [10, 5, 7, 10]`

* Start: `do=10`, `skip=0`
* i=1 (5):  `new_do=min(10,0)+5=5`, `new_skip=10` → `do=5`, `skip=10`
* i=2 (7):  `new_do=min(5,10)+7=12`, `new_skip=5` → `do=12`, `skip=5`
* i=3 (10): `new_do=min(12,5)+10=15`, `new_skip=12` → `do=15`, `skip=12`
  Answer `min(15,12)=12` → take 5 and 7, skip both 10s (not consecutive skips).

---

# 3) Python solutions (interview-friendly)

### A) O(N) time, O(1) space — two-state DP (most expected)

```python
#User function Template for python3

class Solution:
    def minAmount(self, A, n): 
        # Edge case: no tasks
        if n == 0:
            return 0
        
        # Initialize for i = 0
        # do  : minimum time if we DO task 0  -> pay A[0]
        # skip: minimum time if we SKIP task 0 -> 0 (skipping a single task is allowed)
        do = A[0]
        skip = 0
        
        # Iterate tasks 1..n-1; each step is O(1), total O(N)
        for i in range(1, n):
            # If we do task i, previous can be do or skip; take the cheaper
            new_do = min(do, skip) + A[i]
            # If we skip task i, previous MUST have been done (can't skip twice)
            new_skip = do
            
            do, skip = new_do, new_skip
        
        # Final answer: can end by doing or skipping the last task
        # Space used is O(1) (only a few scalars).
        return min(do, skip)
```

**Complexities:** Time `O(N)` (single pass), Space `O(1)`.

---

### B) O(N) using the **complement → House Robber** trick

```python
#User function Template for python3

class Solution:
    def minAmount(self, A, n):
        # total time if we did everything
        total = sum(A)
        
        # bestSkip = maximum sum of non-adjacent elements (House Robber)
        # rob = best sum including A[i] as the last taken (skip i)
        # norob = best sum not taking A[i]
        rob = 0
        norob = 0
        for x in A:
            new_rob = norob + x      # take x (so previous cannot be taken)
            new_norob = max(norob, rob)  # skip x (take the best so far)
            rob, norob = new_rob, new_norob
        
        bestSkip = max(rob, norob)
        # Minimum done time = total - best possible skipped time
        return total - bestSkip
```

**Complexities:** Time `O(N)`, Space `O(1)`.

---

### C) Recursive + memo (educational “brute → optimized”)

Good to show reasoning; still `O(N)` states × `O(1)` transition.

```python
#User function Template for python3

class Solution:
    def minAmount(self, A, n):
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def solve(i, prev_skipped):
            """
            Minimum time from index i..n-1
            prev_skipped = 1 if i-1 was skipped, else 0
            """
            if i == n:
                return 0
            
            INF = 10**18
            
            # Option 1: do A[i]
            do_cost = A[i] + solve(i + 1, 0)
            
            # Option 2: skip A[i] (only if previous wasn't skipped)
            skip_cost = solve(i + 1, 1) if not prev_skipped else INF
            
            return min(do_cost, skip_cost)
        
        return solve(0, 0)
```

**Complexities:** Time `O(N)` (2 states per index), Space `O(N)` for recursion + memo.

---

# 4) Likely interviewer Q&A

**Q1. Derive the DP recurrence.**
Keep two states at `i`: `do_i` and `skip_i`.
`do_i = min(do_{i-1}, skip_{i-1}) + A[i]`, `skip_i = do_{i-1}`.
Answer `min(do_{n-1}, skip_{n-1})`.

**Q2. Why does the House Robber complement work?**
You either **do** or **skip** each task. The constraint applies to **skips** (no two adjacent). So maximize total time you can legally **skip**, then subtract from the total to get the minimum **done** time.

**Q3. What are the complexities and memory guarantees?**
Both methods run in `O(N)` time. We can do it in `O(1)` extra space (keep just a couple of scalars), which is crucial for `N` up to `10^6`.

**Q4. What happens for `N=1`?**
You may skip the single task since the rule forbids only **two consecutive** skips.
Answer is `min(A[0], 0)` → both methods return `0`.

**Q5. What if some `A[i]` were zero or negative?**
Problem states times as nonnegative (typical). If negatives existed, the DP formulas still hold; you’d tend to **do** negative-time tasks because they reduce the total.

**Q6. Can you reconstruct which tasks to do/skip?**
Yes—store choices while updating DP (e.g., keep a parent pointer or recompute by walking backward comparing `do/skip` transitions).

**Q7. Relation to classic problems?**

* Direct DP is a standard **finite-state** linear DP.
* Complement method is exactly **House Robber** on the array of times.

---

---

awesome — here’s a clean, runnable package with timing, plus a couple of solution variants.

---

## Full program (with timing + inline complexity notes)

```python
#!/usr/bin/env python3
"""
Skip the work — minimize total time while you may skip tasks but NOT two in a row.

Two equivalent O(N) / O(1) approaches are implemented:

1) Two-state DP (most expected in interviews)
   State after processing i: 
      do  = min time if we DO task i
      skip= min time if we SKIP task i (means i-1 must have been done)
   Transitions:
      new_do   = min(do, skip) + A[i]
      new_skip = do
   Answer: min(do, skip) at the end

2) Complement trick (House Robber):
   Min done time = sum(A) - (max time that can be SKIPPED with no adjacent skips)

The driver runs a small suite and times the total program run using timeit.default_timer().
"""

from timeit import default_timer as timer


# ------------------------------------------------------------
# User function Template for python3  — Two-state DP (O(N) time, O(1) space)
# ------------------------------------------------------------
class Solution:
    def minAmount(self, A, n): 
        """
        Time:  O(N)  — single pass, each iteration O(1)
        Space: O(1)  — only a couple of scalars
        """
        if n == 0:
            return 0

        # i = 0 initialization:
        # do   : we do task 0 -> pay A[0]
        # skip : we skip task 0 -> pay 0 (skipping a single task is allowed)
        do = A[0]
        skip = 0

        # Process tasks 1..n-1
        for i in range(1, n):
            # If we DO task i, previous could be either done or skipped — take cheaper
            new_do = min(do, skip) + A[i]    # O(1)

            # If we SKIP task i, previous MUST have been done (no two skips)
            new_skip = do                    # O(1)

            # Roll states (O(1) space)
            do, skip = new_do, new_skip

        # Either end by doing or skipping the last task
        return min(do, skip)


# ------------------------------------------------------------
# Variant: Complement / House-Robber view (O(N) time, O(1) space)
# ------------------------------------------------------------
class SolutionComplement:
    def minAmount(self, A, n):
        """
        Min done time = total - bestSkip,
        where bestSkip is the maximum sum of NON-ADJACENT tasks we can skip.
        House Robber DP:
            rob   = best sum when we DO skip current item
            norob = best sum when we DON'T skip current item
        Time:  O(N)
        Space: O(1)
        """
        total = sum(A)  # O(N)

        rob = 0     # taking current skip
        norob = 0   # not taking current skip
        for x in A:                 # O(N) iterations
            new_rob = norob + x     # skip current -> previous must be not skipped
            new_norob = max(norob, rob)  # don't skip current -> take best so far
            rob, norob = new_rob, new_norob

        bestSkip = max(rob, norob)
        return total - bestSkip


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def main():
    tests = [
        # (A, expected)
        ([10, 20], 10),               # sample 1
        ([10, 5, 7, 10], 12),         # sample 2
        ([5], 0),                     # single task -> allowed to skip it
        ([0, 0, 0], 0),               # zero times
        ([3, 2, 5, 10, 7], 9),        # choose 2 + 7 (skip 3,5,10 alternately) -> 9
        ([1, 100, 1, 100, 1], 2),     # do the cheap 1's (cannot skip two 100s consecutively)
    ]

    s1 = Solution()
    s2 = SolutionComplement()

    print("Skip the work — Minimum total time with no two consecutive skips\n")

    t0 = timer()  # start timer for the WHOLE run

    for arr, expected in tests:
        out1 = s1.minAmount(arr, len(arr))
        out2 = s2.minAmount(arr, len(arr))
        print(f"A = {arr}")
        print(f"  Output (Two-state DP): {out1}")
        print(f"  Output (Complement)  : {out2}")
        print(f"  Expected             : {expected}")
        print("-" * 56)

    t1 = timer()  # stop timer

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

---

## 6) Real-World Use Cases (a few high-value ones)

* **Quality/Safety pipelines:** In build/test/deploy pipelines with layered checks, policy may forbid skipping two consecutive gates. Pick the cheapest subset of checks while never skipping two adjacent ones.

* **Operational staffing/maintenance:** When at least one of any two consecutive shifts or maintenance windows must be staffed/executed, choose the minimum-time/effort plan without leaving two adjacent windows unserved.

* **Sensor sampling under constraints:** To save energy/time you can drop samples, but specifications may forbid missing two in a row. Choose which reads to perform to minimize total acquisition time while respecting continuity.
