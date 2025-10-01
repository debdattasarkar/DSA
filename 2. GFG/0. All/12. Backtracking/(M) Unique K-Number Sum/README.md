
---

# Unique K-Number Sum

**Difficulty:** Medium
**Accuracy:** 78.51%
**Submissions:** 400+
**Points:** 4

---

## Problem Statement

Given two integers **n** and **k**, the task is to find all valid combinations of **k numbers** that add up to **n** based on the following conditions:

* Only numbers from the range **[1, 9]** are used.
* Each number can only be used **at most once**.

**Note:**
You can return the combinations in any order, the driver code will print them in sorted order.

---

## Examples

### Example 1

**Input:**

```
n = 9, k = 3
```

**Output:**

```
[[1, 2, 6], [1, 3, 5], [2, 3, 4]]
```

**Explanation:**
There are three valid combinations of 3 numbers that sum to 9:

* [1, 2, 6]
* [1, 3, 5]
* [2, 3, 4]

---

### Example 2

**Input:**

```
n = 3, k = 3
```

**Output:**

```
[]
```

**Explanation:**
It is not possible to pick 3 distinct numbers from 1 to 9 that sum to 3, so no valid combinations exist.

---

## Constraints

* ( 1 \leq n \leq 50 )
* ( 1 \leq k \leq 9 )

---

## Expected Complexities

* **Time Complexity:** ( O(k \times 2^9) )
* **Auxiliary Space:** ( O(k) )

---

## Company Tags

* Bloomberg
* Google
* Amazon

---

## Topic Tags

* Backtracking
* Arrays
* Recursion

---

## Related Articles

* [Generate All Possible Combinations Of K Numbers That Sums To N](https://www.geeksforgeeks.org/generate-all-possible-combinations-of-k-numbers-that-sums-to-n/)

---

---

awesome — let’s make this interview-ready.

# 2) Approach & step-by-step dry run

## Core idea (what the interviewer expects)

We must pick exactly **k** distinct numbers from **1..9** whose sum equals **n**.
This screams **backtracking** (a DFS that builds a partial combination and backtracks when it can’t possibly reach the target).

### State we track

* `start`: next number we’re allowed to try (to keep numbers unique and increasing).
* `remain`: how much sum is still needed.
* `k_left`: how many numbers we still must pick.
* `path`: the current combination.

### Powerful pruning (why it’s fast)

1. **Not enough numbers left:** if `k_left > 9 - start + 1` → impossible.
2. **Arithmetic lower bound:** the smallest sum we can still add using `k_left` numbers starting at `start` is
   `min_possible = start + (start+1) + … + (start + k_left - 1) = k_left * (2*start + (k_left-1)) / 2`.
   If `remain < min_possible` → prune.
3. **Arithmetic upper bound:** the largest sum from any `k_left` numbers in `1..9` is
   `max_possible = 9 + 8 + … + (10 - k_left) = k_left * (19 - k_left) / 2`.
   If `remain > max_possible` → prune.
4. **Monotonic break:** in the for-loop, once `i > remain` we can break (later `i` only get larger).

These few lines of math often cut 90%+ of the search.

---

## Dry run (n = 9, k = 3)

I’ll show the key recursive frames; each line is `(start, k_left, remain, path)`.

1. Start: `(1, 3, 9, [])`

   * Try `i = 1` → `(2, 2, 8, [1])`

     * Try `i = 2` → `(3, 1, 6, [1,2])`

       * Loop i=3..9:

         * i=3 → remain becomes 3, k_left becomes 0 → not 0 → discard
         * i=4 → remain 2, k_left 0 → discard
         * i=5 → remain 1, k_left 0 → discard
         * i=6 → remain **0**, k_left **0** → **record [1,2,6]**
         * i=7 (> remain initially 6) → break
     * Backtrack to `[1]`, try `i = 3` → `(4, 1, 5, [1,3])`

       * i=4 → remain 1, k_left 0 → discard
       * i=5 → remain **0**, k_left **0** → **record [1,3,5]**
       * i=6 (> remain 5) → break
     * Try `i = 4` → `(5, 1, 4, [1,4])`

       * **Lower bound prune**: with k_left=1 and start=5, min_possible=5 > remain=4 → prune whole branch.
   * Back to root, try `i = 2` → `(3, 2, 7, [2])`

     * `i = 3` → `(4, 1, 4, [2,3])`

       * `i = 4` → remain **0**, k_left **0** → **record [2,3,4]**
       * `i = 5` (> remain 4) → break
     * `i = 4` → `(5, 1, 3, [2,4])`

       * **Lower bound prune**: need one number ≥5 but remain=3 → prune
   * Try `i = 3` at root → `(4, 2, 6, [3])`

     * **Lower bound prune**: min_possible with k_left=2 from start=4 is 4+5=9 > remain=6 → prune

Collected answers: `[[1,2,6], [1,3,5], [2,3,4]]`.

---

# 3) Python solutions (interview-ready)

### A) Backtracking with tight pruning (optimal & most expected)

```python
class Solution:
    def combinationSum(self, n, k):
        # Results will hold all valid combinations
        res, path = [], []

        # Arithmetic helpers for pruning
        def min_sum(start, r):
            # Sum of r smallest numbers starting from `start`
            # = r/2 * [2*start + (r-1)]
            return r * (2 * start + (r - 1)) // 2

        def max_sum(r):
            # Sum of r largest numbers from 1..9
            # = r/2 * [9 + (10 - r)] = r/2 * (19 - r)
            return r * (19 - r) // 2

        def dfs(start, k_left, remain):
            # If we've picked k numbers, check if the sum hits exactly
            if k_left == 0:
                if remain == 0:
                    res.append(path.copy())
                return

            # 1) Not enough numbers left in 1..9 (from 'start' onward)
            if k_left > 10 - start:
                return

            # 2) Lower bound prune
            if remain < min_sum(start, k_left):
                return

            # 3) Upper bound prune
            if remain > max_sum(k_left):
                return

            # Try each next number once, in increasing order
            for x in range(start, 10):  # numbers 1..9
                if x > remain:
                    break  # 4) monotonic break
                path.append(x)
                dfs(x + 1, k_left - 1, remain - x)
                path.pop()  # backtrack

        dfs(1, k, n)
        return res
```

**Complexity:**
Worst-case search size is `C(9, k)` nodes; each push/pop costs O(1).
So **time ≈ O(C(9,k) * k)** (k to copy/emit a solution), **space O(k)** recursion depth.

---

### B) Clean brute force (using `itertools.combinations`) — shortest to write

```python
from itertools import combinations

class Solution:
    def combinationSum(self, n, k):
        # Try every k-combination from 1..9; keep those that sum to n
        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]
```

**When to mention:** Great as a baseline or when the interviewer allows library use.
**Time:** `O(C(9,k) * k)` to sum each combination. **Space:** O(k) per combo.

---

### C) Bitmask enumeration (explicit brute force; shows comfort with bits)

```python
class Solution:
    def combinationSum(self, n, k):
        res = []
        # Masks over 9 bits represent a subset of {1..9}
        for mask in range(1, 1 << 9):  # 1..511
            if mask.bit_count() != k:  # Python 3.8+: use bin(mask).count('1')
                continue
            total, combo, ok = 0, [], True
            for i in range(9):  # bit i corresponds to number i+1
                if (mask >> i) & 1:
                    v = i + 1
                    total += v
                    combo.append(v)
                    if total > n:  # early stop for this mask
                        ok = False
                        break
            if ok and total == n:
                res.append(combo)
        return res
```

**Time:** `O(2^9 * 9)` = small because domain is tiny, but conceptually brute force.
**Space:** O(k).

---

# 4) Interview Q&A you’re likely to get

**Q1. Why backtracking here?**
A1. We must choose a subset of fixed size k from a tiny, ordered set (1..9) with an exact sum. Backtracking naturally explores combinations once each (in increasing order) and prunes infeasible branches early.

**Q2. How do you avoid duplicates?**
A2. Always iterate `x` from `start` upward and recurse with `start = x + 1`. That forces strictly increasing sequences, so `[1,3,5]` is generated once.

**Q3. What are your pruning rules?**
A3. (1) If `k_left > 9 - start + 1` not enough numbers remain.
(2) Arithmetic **lower bound**: minimal achievable sum with `k_left` numbers is `r*(2*start + r - 1)/2`.
(3) Arithmetic **upper bound**: maximal achievable sum with `k_left` numbers in `1..9` is `r*(19 - r)/2`.
(4) Break when current `x > remain`.

**Q4. Complexity?**
A4. The search space is combinations, so **time ~ O(C(9,k) * k)**; **space O(k)** recursion depth.

**Q5. Could you solve without recursion?**
A5. Yes—either iterate all `itertools.combinations(range(1,10), k)` and filter by sum, or simulate recursion with an explicit stack.

**Q6. Do you need to sort anything?**
A6. No; the domain is already ordered (1..9). We build increasing paths.

**Q7. What pitfalls cause TLE or WA?**
A7. Forgetting early pruning, double-counting due to not enforcing order, allowing reuse of numbers, or not stopping when `x > remain`.

**Q8. How would you generalize?**
A8. Replace the fixed domain `1..9` with any sorted list `A` and the same DFS. Bounds become `min_sum` from consecutive elements of `A` and `max_sum` from the largest remaining `k_left` elements. With large `A`, additional heuristics or DP meet-in-the-middle may help.

**Q9. If repetition were allowed?**
A9. Then it becomes a variant of Combination Sum (with unlimited picks). We would recurse with `dfs(x, k_left-1, remain-x)` (keep `x` allowed again) and drop the “not enough numbers” prune.

**Q10. How do you ensure results are in sorted order?**
A10. Paths are constructed in increasing order; most drivers will print sorted. If a strict output order is required, sort the final `res`.

**Q11. Can this overflow?**
A11. Not in Python; in languages with fixed ints, sums are tiny anyway (max 9+…+1).

**Q12. Quick sanity checks?**
A12. Impossible when `n < 1+2+…+k` or `n > 9+8+…+(10-k)`. If either holds, return `[]` immediately.

---

---

sweet — here’s the final piece with a **runnable, interview-style full program**, timings, and crisp real-world uses.

---

# 5) Full Python Program (with inline complexity notes + timings)

```python
"""
Unique K-Number Sum
Pick exactly k distinct numbers from 1..9 whose sum is n.

This file includes:
- Optimized backtracking with arithmetic pruning (primary solution)
- Two alternative brutes (itertools + bitmask) for completeness
- A small test harness that prints outputs and uses `timeit` to measure runtime

All steps are annotated with time/space complexity notes you can quote in interviews.
"""

from itertools import combinations
import timeit


class Solution:
    # ----------------------------
    # A) OPTIMIZED BACKTRACKING
    # ----------------------------
    def combinationSum(self, n, k):
        """
        Returns all k-combinations from 1..9 that sum to n.

        Complexity (tight, expected answer in interviews):
        - Search space: choose k from 9 => ~ C(9, k) nodes explored in practice (<< 2^9 due to pruning)
        - Time: O(C(9, k) * k)  [k to emit/copy each valid combo]
        - Space: O(k) recursion depth + O(#answers * k) to store results
        """
        res, path = [], []

        # --- helpers for PRUNING ---
        # Sum of r consecutive ints starting at 'start':
        # start + (start+1) + ... + (start+r-1) = r * (2*start + r - 1) / 2
        def min_sum(start, r):
            # O(1) time, O(1) space
            return r * (2 * start + (r - 1)) // 2

        # Sum of r largest numbers in 1..9:
        # 9 + 8 + ... + (10-r) = r * (19 - r) / 2
        def max_sum(r):
            # O(1) time, O(1) space
            return r * (19 - r) // 2

        def dfs(start, k_left, remain):
            """
            DFS/backtrack over increasing numbers in [start..9].

            Each call:
            - O(1) work outside the loop (bound checks)
            - Up to 9 - start + 1 iterations (bounded constant), but heavily pruned
            - Space: O(1) local, plus path stack O(k)
            """
            # Base: selected k numbers
            if k_left == 0:  # O(1)
                if remain == 0:  # O(1)
                    res.append(path.copy())  # O(k) to copy
                return

            # Prune: not enough numbers left to fill k_left
            if k_left > 10 - start:  # O(1)
                return

            # Prune: arithmetic lower bound (can't reach remain)
            if remain < min_sum(start, k_left):  # O(1)
                return

            # Prune: arithmetic upper bound (remain too large even with 9.. downwards)
            if remain > max_sum(k_left):  # O(1)
                return

            # Try each next candidate once
            for x in range(start, 10):  # up to 9 iterations (constant)
                if x > remain:  # if x already exceeds remain, later x only larger
                    break
                path.append(x)               # O(1)
                dfs(x + 1, k_left - 1, remain - x)  # recurse with tighter state
                path.pop()                   # O(1) undo (backtrack)

        dfs(1, k, n)
        return res


# ----------------------------
# B) BRUTE (cleanest) – itertools
# ----------------------------
class SolutionCombinations:
    def combinationSum(self, n, k):
        """
        Try every k-combination from 1..9, filter by sum.
        - Time: O(C(9, k) * k) due to summing each tuple of length k
        - Space: O(k) per tuple + O(#answers * k) to store final lists
        """
        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]


# ----------------------------
# C) BRUTE (explicit) – bitmask
# ----------------------------
class SolutionBitmask:
    def combinationSum(self, n, k):
        """
        Enumerate all subsets of {1..9} via bitmasks.
        - Time: O(2^9 * 9) ~ small in absolute terms but conceptually brute force
        - Space: O(k) to build each subset
        """
        res = []
        for mask in range(1, 1 << 9):  # 1..511
            # popcount check
            if mask.bit_count() != k:  # Python 3.8: use bin(mask).count('1')
                continue
            total, combo, ok = 0, [], True
            # accumulate numbers per set bit
            for i in range(9):  # 9 iterations
                if (mask >> i) & 1:
                    v = i + 1
                    total += v  # O(1)
                    combo.append(v)
                    if total > n:  # early breakout for this mask
                        ok = False
                        break
            if ok and total == n:
                res.append(combo)
        return res


# ----------------------------
# Tiny benchmark utility using timeit
# ----------------------------
def bench(func, *args, number=10000):
    """
    Measure average runtime over `number` runs.
    - Uses timeit.timeit which isolates overheads reasonably well.
    - Prints micro-benchmarks; do not over-interpret for very fast functions.
    """
    t = timeit.timeit(lambda: func(*args), number=number)
    avg = t / number
    print(f"[timeit] {func.__qualname__} with args={args}, runs={number} -> avg {avg:.8f}s")


# ----------------------------
# Main runner: sample inputs, outputs, and timings
# ----------------------------
if __name__ == "__main__":
    # Example test cases (from prompt + a couple extras)
    tests = [
        (9, 3),  # Expected: [[1,2,6],[1,3,5],[2,3,4]]
        (3, 3),  # Expected: []
        (7, 3),  # Expected: [[1,2,4]]
        (15, 5), # Another valid sum with 5 numbers
    ]

    sol_opt = Solution()
    sol_comb = SolutionCombinations()
    sol_mask = SolutionBitmask()

    print("=== Unique K-Number Sum ===")
    for n, k in tests:
        print(f"\nInput: n={n}, k={k}")
        ans_opt = sol_opt.combinationSum(n, k)
        print("Optimized Backtracking Output:", ans_opt)

        # (Optional) show outputs from other methods to confirm parity
        ans_lib = sol_comb.combinationSum(n, k)
        ans_bm  = sol_mask.combinationSum(n, k)

        # Sort for display parity (driver on platforms usually does this)
        ans_opt_sorted = sorted(ans_opt)
        ans_lib_sorted = sorted(ans_lib)
        ans_bm_sorted  = sorted(ans_bm)

        print("itertools.combinations Output:", ans_lib_sorted)
        print("Bitmask Enumeration Output  :", ans_bm_sorted)
        print("All methods match?          :", ans_opt_sorted == ans_lib_sorted == ans_bm_sorted)

    # --------------- Timings ---------------
    # Measure for a representative input (n=9, k=3)
    print("\n=== Timings (n=9, k=3) ===")
    bench(sol_opt.combinationSum, 9, 3, number=20000)   # optimized backtracking
    bench(sol_comb.combinationSum, 9, 3, number=20000)  # itertools brute
    bench(sol_mask.combinationSum, 9, 3, number=20000)  # bitmask brute

    # For a slightly bigger branch factor (still tiny domain)
    print("\n=== Timings (n=15, k=5) ===")
    bench(sol_opt.combinationSum, 15, 5, number=5000)
    bench(sol_comb.combinationSum, 15, 5, number=5000)
    bench(sol_mask.combinationSum, 15, 5, number=5000)

    print("\nNote: Actual numbers depend on your machine & Python version.")
```

**What this prints (example):**

* For each `(n, k)` pair, it prints the output from:

  * Optimized backtracking
  * `itertools.combinations` brute
  * Bitmask brute
* Then it confirms that all methods match.
* Finally it shows **`timeit`** averages for each approach over many runs.

---

# 6) Real-World Use Cases (the important ones)

1. **Resource Allocation / Budgeting with Limits**
   Choose exactly **k** projects/items from a small candidate set (e.g., 9 pre-screened initiatives) whose costs sum to a fixed budget. No repetition, each item at most once.

2. **Team Formation under Headcount and Score Constraints**
   Pick exactly **k** people (from a small roster) where individual “scores” (skills/credits) must total **n** (e.g., capstone teams, hackathon rosters) — ensuring uniqueness and exactly-k membership.

3. **Game/Quiz Design with Fixed Score Targets**
   Assemble exactly **k** questions from difficulty scores 1..9 to reach a target total **n**, avoiding repeats and guaranteeing balanced sets for multiple players.

4. **Test Case Generation / Data Sampling**
   When synthesizing combinations of bounded categorical features (1..9 scales) with exact aggregate constraints (sum == n) and exactly k selections, e.g., controlled experiments or A/B configurations.

---
