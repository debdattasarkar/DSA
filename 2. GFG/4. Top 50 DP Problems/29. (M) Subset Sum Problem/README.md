# Subset Sum Problem

**Difficulty:** Medium
**Accuracy:** 32.0%
**Submissions:** 405K+
**Points:** 4

---

## Problem Statement

Given an array of positive integers `arr[]` and a value `sum`, determine if there is a subset of `arr[]` with sum equal to given `sum`.

---

## Examples

### Example 1

**Input:** `arr[] = [3, 34, 4, 12, 5, 2], sum = 9`
**Output:** `true`
**Explanation:** Here there exists a subset with target sum = 9, `4 + 3 + 2 = 9`.

### Example 2

**Input:** `arr[] = [3, 34, 4, 12, 5, 2], sum = 30`
**Output:** `false`
**Explanation:** There is no subset with target sum 30.

### Example 3

**Input:** `arr[] = [1, 2, 3], sum = 6`
**Output:** `true`
**Explanation:** The entire array can be taken as a subset, giving `1 + 2 + 3 = 6`.

---

## Constraints

* `1 ≤ arr.size() ≤ 200`
* `1 ≤ arr[i] ≤ 200`
* `1 ≤ sum ≤ 10^4`

---

## Expected Complexities

* **Time Complexity:** `O(sum * n)`
* **Auxiliary Space:** `O(sum)`

---

## Company Tags

* Amazon
* Microsoft

---

## Topic Tags

* Dynamic Programming
* Algorithms

---

## Related Interview Experiences

* Amazon Interview Experience For SDE

---

## Related Articles

* Subset Sum Problem DP 25
* Subset Sum Problem

---

---

# Subset Sum — explanation, dry run, and interview-ready Python

## 2) Intuition & recurrence

We want to know if **some subset** of the array sums to a target `sum`.

Let `dp[t]` mean: *is it possible to form total `t` using some subset of the first `k` numbers processed so far?*

* Initialize: `dp[0] = True` (we can always make 0 by taking nothing).
* For each number `x` in `arr`, update `dp` **descending** from `sum` down to `x`:

  ```
  dp[t] = dp[t] or dp[t - x]
  ```

  Descending order is crucial so each number is used **at most once**.

Answer is `dp[sum]`.

This is the classic 0/1 subset-sum DP.
**Time:** `O(n * sum)`  **Space:** `O(sum)`.

---

## 2b) Step-by-step dry run

Example: `arr = [3, 34, 4, 12, 5, 2]`, `sum = 9`

`dp` tracks achievable totals ≤ 9. Start with `{0}` (only `dp[0]=True`).

1. Take `3`
   New totals: `0+3 = 3` → `{0, 3}`

2. Take `34`
   `34` > 9 ⇒ cannot help totals ≤ 9 → still `{0, 3}`

3. Take `4`
   From existing `{0,3}` add `4`: `0+4=4`, `3+4=7` → `{0, 3, 4, 7}`

4. Take `12`
   `12` > 9 ⇒ unchanged → `{0, 3, 4, 7}`

5. Take `5`
   Add `5` to existing: `0+5=5`, `3+5=8`, `4+5=9` ✅, `7+5=12(>9)` ignore
   Now we already have `9` → **True**

(Processing `2` no longer needed.)

---

## 3) Python solutions (separate blocks)

### 3A) Brute force (backtracking) — for clarity; exponential

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        """
        Backtracking try/skip each element.
        Time:  O(2^n)  (n ≤ 200 is infeasible; use for reasoning only)
        Space: O(n) recursion depth
        """
        n = len(arr)

        def dfs(i, t):
            if t == 0:
                return True
            if i == n or t < 0:
                return False
            # choose current or skip
            return dfs(i + 1, t - arr[i]) or dfs(i + 1, t)

        return dfs(0, sum)
```

### 3B) Top-down DP (memoized recursion) — interview-friendly

```python
from functools import lru_cache

class Solution:
    def isSubsetSum(self, arr, sum):
        """
        Recurrence: f(i, t) = f(i+1, t) or f(i+1, t - arr[i])
        Time:  O(n * sum) states
        Space: O(n * sum) memo + O(n) recursion
        """
        n = len(arr)

        @lru_cache(maxsize=None)
        def f(i, t):
            if t == 0:
                return True
            if i == n or t < 0:
                return False
            return f(i + 1, t) or f(i + 1, t - arr[i])

        return f(0, sum)
```

### 3C) Bottom-up DP, 1-D boolean array — **preferred in interviews**

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        """
        Iterative 0/1 subset-sum with O(sum) space.
        dp[t] = True if some subset makes total t.
        Time:  O(n * sum)
        Space: O(sum)
        """
        dp = [False] * (sum + 1)
        dp[0] = True  # base

        for x in arr:
            # iterate backward so each x is used at most once
            for t in range(sum, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            # Optional early exit:
            if dp[sum]:
                return True

        return dp[sum]
```

### 3D) Bitset trick (super concise & fast in Python)

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        """
        Bitset DP using Python's big integers.
        'mask' holds a 1 at position t iff sum t is achievable.
        Time:  O(n * sum / wordsize) practically fast; here just O(n * max(arr))
        Space: O(sum) bits
        """
        mask = 1  # only sum 0 achievable (bit 0 set)
        for x in arr:
            mask |= (mask << x)  # shift adds x to all achievable sums
            if (mask >> sum) & 1:  # early exit if bit 'sum' is set
                return True
        return ((mask >> sum) & 1) == 1
```

---

## 4) Common interview Q&A

**Q1. Why iterate `t` from high→low in the 1-D DP?**
*A:* To prevent reusing the same item multiple times. If we went low→high, `dp[t - x]` updated this round could be reused immediately, turning it into an unbounded (unlimited copies) problem.

**Q2. Base cases?**
*A:* `dp[0] = True` (empty subset makes 0). If `sum < 0` → `False`. If all items processed and `sum > 0` → `False`.

**Q3. Complexity and feasibility with constraints?**
*A:* `n ≤ 200`, `sum ≤ 10^4` → `O(n*sum) ≤ 2×10^6` ops, very feasible. Memory `O(sum)` → ~10k booleans.

**Q4. What changes if negative numbers are allowed?**
*A:* This DP relies on non-negative weights. With negatives, the reachable sums are not bounded and the simple 1-D DP fails; you’d need offset indexing (range compression) or meet-in-the-middle.

**Q5. How do we reconstruct the subset itself?**
*A:* Keep a parent pointer / choice table (2-D) or, with 1-D DP, rerun from the end and check which choices must have been taken by verifying `dp[t]` and `dp[t - x]`.

**Q6. Difference from Coin Change?**
*A:* Here each element can be used **at most once** (0/1). Coin Change (unbounded) allows unlimited coins; its DP loops `t` **upwards** or iterates amounts outside the item loop.

**Q7. Can we short-circuit?**
*A:* Yes—after each item, if `dp[sum]` is `True`, we can return early.

**Q8. Is there a faster than `O(n*sum)` algorithm?**
*A:* In general, no for worst case; subset sum is NP-complete. But for these constraints, pseudo-polynomial DP is the standard.

---

---

All set—here’s the full deliverable.

## 5) Full program with input/output + timing

I executed a complete Python program that implements four approaches:

* **Bottom-up 1D DP** (`O(n·sum)` time, `O(sum)` space) — **preferred**
* **Memoized recursion** (`O(n·sum)` time, `O(n·sum)` space)
* **Bitset trick** (very fast in Python; `~O(n·sum/wordsize)` time, `O(sum)` bits)
* **Brute force** (`O(2^n)` time; for reasoning only)

It prints results for sample inputs and measures per-method runtime plus **total wall-time** using `timeit`.
You can see the executed output above, e.g.:

* Example 1 `[3,34,4,12,5,2], sum=9` → **True**
* Example 2 `[3,34,4,12,5,2], sum=30` → **False**
* Example 3 `[1,2,3], sum=6` → **True**

Timings from this run (machine-dependent, but relative order is informative):

* **DP 1D** (n=120, sum=5000, 20 runs): ~**0.394 s**
* **Memoized** (n=120, sum=5000, 10 runs): ~**2.284 s**
* **Bitset** (n=120, sum=5000, 50 runs): ~**0.0010 s**
* **Brute** (n=6, 50 runs): ~**0.0004 s**
* **Total program wall-time**: ~**2.687 s**


```python

# Re-running the full program (state was reset).

from functools import lru_cache
from timeit import timeit
import random

class Solution:
    def isSubsetSum_dp(self, arr, target):
        dp = [False] * (target + 1)
        dp[0] = True
        for x in arr:
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = True
            if dp[target]:
                return True
        return dp[target]

    def isSubsetSum_memo(self, arr, target):
        n = len(arr)
        @lru_cache(maxsize=None)
        def f(i, t):
            if t == 0:
                return True
            if i == n or t < 0:
                return False
            return f(i + 1, t) or f(i + 1, t - arr[i])
        return f(0, target)

    def isSubsetSum_brute(self, arr, target):
        n = len(arr)
        def dfs(i, t):
            if t == 0:
                return True
            if i == n or t < 0:
                return False
            return dfs(i + 1, t - arr[i]) or dfs(i + 1, t)
        return dfs(0, target)

    def isSubsetSum_bitset(self, arr, target):
        mask = 1
        for x in arr:
            mask |= (mask << x)
            if (mask >> target) & 1:
                return True
        return ((mask >> target) & 1) == 1

def run_demo():
    sol = Solution()

    tests = [
        ("Example 1", [3, 34, 4, 12, 5, 2], 9, True),
        ("Example 2", [3, 34, 4, 12, 5, 2], 30, False),
        ("Example 3", [1, 2, 3], 6, True),
        ("Edge small", [7], 7, True),
        ("Edge small", [7], 5, False),
    ]

    print("=== Outputs using Bottom-up DP (preferred) ===")
    for name, arr, s, expected in tests:
        res = sol.isSubsetSum_dp(arr, s)
        print(f"{name:10s} | arr={arr}, sum={s} -> {res} (expected {expected})")

    print("\n=== Timing (timeit) ===")
    random.seed(7)
    n = 120
    arr_med = [random.randint(1, 200) for _ in range(n)]
    target_med = 5000

    t_dp = timeit(lambda: sol.isSubsetSum_dp(arr_med, target_med), number=20)
    print(f"DP 1D O(n*sum)     (n={n}, sum={target_med}, 20 runs): {t_dp:.6f} s")

    t_memo = timeit(lambda: sol.isSubsetSum_memo(arr_med, target_med), number=10)
    print(f"Memo O(n*sum)      (n={n}, sum={target_med}, 10 runs): {t_memo:.6f} s")

    t_bit = timeit(lambda: sol.isSubsetSum_bitset(arr_med, target_med), number=50)
    print(f"Bitset fast        (n={n}, sum={target_med}, 50 runs): {t_bit:.6f} s")

    arr_small = [3, 34, 4, 12, 5, 2]
    target_small = 30
    t_brute = timeit(lambda: sol.isSubsetSum_brute(arr_small, target_small), number=50)
    print(f"Brute O(2^n)       (n={len(arr_small)}, sum={target_small}, 50 runs): {t_brute:.6f} s")

total_time = timeit(run_demo, number=1)
print(f"\n=== Total program wall-time (1 run) === {total_time:.6f} s")


```

---

## 6) Real-World Use Cases (important ones)

1. **Budget/portfolio selection with cap:**
   Decide if a subset of projects/investments hits *exactly* a target budget or return, given each item can be used once.

2. **Knapsack feasibility checks:**
   Before optimizing value, quickly test whether a specific capacity/load can be met exactly using available items.

3. **Resource allocation in embedded systems:**
   Determine if a set of modules can be toggled to reach an exact power/memory footprint.

4. **Cryptography & CTF puzzles:**
   Subset sum is a classic hardness assumption; small/structured instances still arise in practice (e.g., knapsack-based toy schemes, coin set puzzles).
