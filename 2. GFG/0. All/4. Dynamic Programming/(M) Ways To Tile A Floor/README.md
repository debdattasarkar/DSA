
---

# 🧩 Ways To Tile A Floor

### Difficulty: Medium

**Accuracy:** 32.31%
**Submissions:** 52K+
**Points:** 4

---

## 🧠 Problem Statement

Given a floor of dimensions **2 × n** and tiles of dimensions **2 × 1**, the task is to find the **number of ways** the floor can be tiled.

A tile can either be placed:

* **Horizontally**, i.e., as a 1 × 2 tile, or
* **Vertically**, i.e., as a 2 × 1 tile.

### Note:

Two tiling arrangements are considered **different** if the placement of at least one tile differs.

---

## 🧩 Examples

### Example 1

**Input:**

```
n = 3
```

**Output:**

```
3
```

**Explanation:**
We need 3 tiles to tile the board of size 2 × 3.
We can tile in the following ways:

1. Place all 3 tiles vertically.
2. Place the first tile vertically and the remaining 2 tiles horizontally.
3. Place the first 2 tiles horizontally and the remaining tile vertically.

**Illustration:**
(Three distinct tiling arrangements are shown.)

---

### Example 2

**Input:**

```
n = 4
```

**Output:**

```
5
```

**Explanation:**
We need 4 tiles to tile the board of size 2 × 4.
We can tile in the following ways:

1. All 4 vertical.
2. All horizontal.
3. First 2 vertical, remaining 2 horizontal.
4. First 2 horizontal, remaining 2 vertical.
5. Corner 2 vertical, middle 2 horizontal.

**Illustration:**
(Five distinct tiling arrangements are shown.)

---

## ⚙️ Constraints

* ( 1 \leq n \leq 45 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏢 Company Tags

* **Amazon**

---

## 🧩 Topic Tags

* Fibonacci
* Dynamic Programming
* Recursion

---

## 📚 Related Articles

* [**Tiling Problem**](https://www.geeksforgeeks.org/tiling-problem/)

---

---

awesome — let’s make “Ways to Tile a 2×n Floor” interview-ready.

# 2) Explanation + step-by-step dry run

## Problem in one line

How many distinct ways can we tile a **2 × n** board using **2 × 1** dominoes placed **vertically** or **horizontally**?

## Key observation (why it’s Fibonacci)

Let `ways[n]` be the number of tilings for width `n`.

Consider the **rightmost column**:

* If we place **one vertical** domino there → we’re left with a `2 × (n−1)` board → `ways[n-1]` possibilities.
* If we place **two horizontal** dominoes stacked at the end → we must cover the last **two** columns together → we’re left with a `2 × (n−2)` board → `ways[n-2]` possibilities.

Therefore:

```
ways[n] = ways[n-1] + ways[n-2]
Base: ways[0] = 1  (empty board = one way)
      ways[1] = 1  (only vertical domino)
```

This is exactly the **Fibonacci** recurrence.

### Dry run for n = 4

We’ll compute iteratively.

```
ways[0]=1
ways[1]=1
i=2: ways[2]=ways[1]+ways[0]=1+1=2
i=3: ways[3]=ways[2]+ways[1]=2+1=3
i=4: ways[4]=ways[3]+ways[2]=3+2=5
Answer = 5
```

### Dry run (combinatorial intuition for n = 3)

Patterns:

* VVV (3 verticals)
* HH + V (two horizontals at left or right) → 2 ways
  Total = **3**.

---

# 3) Python solutions (from brute → optimal)

All follow your required signature:

```python
class Solution:
    def numberOfWays(self, n):
        # code here
```

### A) Brute recursion (teaching aid; exponential)

```python
class Solution:
    def numberOfWays(self, n):
        """
        Exponential recursion to illustrate the recurrence.
        Time:  O(2^n)  (recomputes subproblems)
        Space: O(n)    (recursion depth)
        """
        if n == 0 or n == 1:
            return 1
        return self.numberOfWays(n - 1) + self.numberOfWays(n - 2)
```

### B) Top-down with memoization (linear)

```python
class Solution:
    def numberOfWays(self, n):
        """
        Memoized recursion (DFS + cache).
        Time:  O(n)     (each state computed once)
        Space: O(n)     (memo + recursion stack)
        """
        from functools import lru_cache

        @lru_cache(None)
        def ways(k):
            if k == 0 or k == 1:
                return 1
            return ways(k - 1) + ways(k - 2)

        return ways(n)
```

### C) Bottom-up tabulation (simple loop)

```python
class Solution:
    def numberOfWays(self, n):
        """
        Iterative DP storing all states.
        Time:  O(n)
        Space: O(n)
        """
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for width in range(2, n + 1):
            # ways[width] = ways[width-1] + ways[width-2]
            dp[width] = dp[width - 1] + dp[width - 2]
        return dp[n]
```

### D) Space-optimized bottom-up (most expected)

```python
class Solution:
    def numberOfWays(self, n):
        """
        Rolling Fibonacci (keep previous two values).
        Time:  O(n)    (single pass)
        Space: O(1)    (two integers)
        """
        if n == 0 or n == 1:
            return 1
        prev2 = 1  # ways[0]
        prev1 = 1  # ways[1]
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current  # slide window
        return prev1
```

> With the given constraint `1 ≤ n ≤ 45`, plain integers are safe (no overflow).
> If a platform asks for modulo (e.g., `1e9+7`), just take `% MOD` at every addition.

---

# 4) Interview quick-recall + Q&A

## 5-line pseudo (memorize this)

```
ways0 = ways1 = 1
for i = 2 .. n:
    waysi = ways1 + ways0
    ways0, ways1 = ways1, waysi
return ways1
```

## Mnemonic (10 seconds)

**“Tile = Fib. Place V or HH.”**

* One **V**ertical → `n−1`
* Two **H**orizontal → `n−2`
* Sum them like Fibonacci.

## Likely questions & crisp answers

**Q1. Why Fibonacci?**
Because the last placement is either **one vertical** covering column `n` (reduce to `n−1`) or **two horizontals** covering columns `n-1..n` (reduce to `n−2`). So `ways[n]=ways[n-1]+ways[n-2]`.

**Q2. Base cases?**
`ways[0]=1` (empty board is one valid tiling), `ways[1]=1` (only vertical fits).

**Q3. Time/space of optimal solution?**
`O(n)` time, `O(1)` extra space using the rolling two-value trick.

**Q4. Can we do it with matrix exponentiation?**
Yes, `O(log n)` using Fibonacci fast doubling or matrix power; but for `n ≤ 45`, linear is simpler and perfectly fine.

**Q5. How to extend if tiles are 2×k also allowed?**
Recurrence becomes `ways[n] = ways[n-1] + ways[n-k]` (if `n ≥ k`). Same DP idea applies.

**Q6. Common pitfalls?**

* Forgetting `ways[0]=1`.
* Mixing up “arrangements” with “counts of tiles” — we count **distinct placements**, not permutations of identical tiles.

---

---

great—closing this out with (5) a few crisp, relatable use cases and (6) a fully runnable, timed Python program.

# 5) Real-World Use Cases (short & relatable)

* **Floor/wall tiling with 2×1 tiles:** Exactly the problem statement—counting distinct tiling layouts for a 2×n strip using vertical dominoes or two stacked horizontals.
* **Server rack layout / blade placement:** Slots arranged in two rows; a blade can occupy one vertical pair of slots (2×1) or two adjacent singles stacked (two 1×2s across both rows). How many distinct packing layouts fit a 2×n rack face?
* **Seating/bench design in trains/buses:** A “seat block” can be a vertical pair (two seats stacked) or a horizontal pair across both rows; how many ways to fill a 2×n carriage segment?
* **PCB component footprints:** Components that either span one column vertically (tall package) or two adjacent cells horizontally (two short packages) along a narrow board—how many legal placements exist?

Each maps cleanly to the Fibonacci recurrence: last column covered by **one vertical** (→ n−1) or **two horizontals** (→ n−2).

---

# 6) Full Program (with inline time/space notes + timing)

* Uses the **space-optimized DP** (rolling Fibonacci) in your required class signature.
* Includes a small driver that runs a few sample `n` values.
* Uses `timeit` to measure the full program call for each input.

```python
"""
Ways to Tile a 2×n Floor
------------------------
Count tilings of a 2×n board using 2×1 dominoes placed vertically or
two 1×2 dominoes stacked horizontally.

Recurrence (Fibonacci):
    ways[n] = ways[n-1] + ways[n-2]
Base:
    ways[0] = 1   (empty board)
    ways[1] = 1   (only vertical tile)

Optimal Approach:
- Bottom-up DP with O(1) space (rolling two values).
- Time O(n): single pass from 2..n
- Aux Space O(1): store only previous two results
"""

import timeit

class Solution:
    def numberOfWays(self, n):
        """
        Return the number of tilings for a 2×n board.

        Time Complexity (per call):
            - Initialization: O(1)
            - Loop runs (n-1) iterations: O(n)
            TOTAL: O(n)

        Space Complexity (auxiliary):
            - Two integers (prev2, prev1) + one temp: O(1)
        """
        # Base cases: O(1)
        if n == 0 or n == 1:
            return 1

        # prev2 = ways[n-2], prev1 = ways[n-1] as we iterate upward
        prev2, prev1 = 1, 1  # ways[0]=1, ways[1]=1

        # Main DP loop: O(n)
        for _ in range(2, n + 1):
            current = prev1 + prev2    # ways[i] = ways[i-1] + ways[i-2]
            prev2, prev1 = prev1, current  # slide window (O(1) work)

        return prev1  # ways[n]

# ---------------- Demo + Timing ----------------
if __name__ == "__main__":
    # Example inputs (you can edit this list for quick experiments)
    test_ns = [3, 4, 10, 30, 45]

    sol = Solution()
    print("Inputs (n)  ->  Number of ways")
    for n in test_ns:
        # Time the *full call* for this input once
        elapsed = timeit.timeit(lambda: sol.numberOfWays(n), number=1)
        result = sol.numberOfWays(n)
        print(f"{n:>9}  ->  {result}   (time: {elapsed:.8f} s)")
```

### What you’ll see (sample)

```
Inputs (n)  ->  Number of ways
        3  ->  3   (time: 0.00000090 s)
        4  ->  5   (time: 0.00000090 s)
       10  ->  89  (time: 0.00000110 s)
       30  ->  1346269  (time: 0.00000140 s)
       45  ->  1836311903  (time: 0.00000160 s)
```

**Why this is interview-ready**

* You clearly state **state**, **transition**, **base**, **time**, **space**.
* The code is **tight**, **readable**, and **optimal** for the problem’s constraints.
* The timing snippet shows practical runtime for various `n`.
