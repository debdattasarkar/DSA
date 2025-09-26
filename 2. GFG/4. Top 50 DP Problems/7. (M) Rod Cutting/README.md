# Rod Cutting

**Difficulty:** Medium
**Accuracy:** 60.66%
**Submissions:** 190K+
**Points:** 4
**Average Time:** 20m

---

## Problem Statement

Given a rod of length `n` inches and an array `price[]`, where `price[i]` denotes the value of a piece of length `i`. Your task is to determine the **maximum value** obtainable by **cutting up** the rod and selling the **pieces**.

**Note:**

* `n = size of price`
* `price[]` is **1-indexed** array.

---

## Example

### Example 1

**Input:** `price[] = [1, 5, 8, 9, 10, 17, 17, 20]`
**Output:** `22`
**Explanation:** The maximum obtainable value is `22` by cutting in two pieces of lengths `2` and `6`, i.e., `5 + 17 = 22`.

### Example 2

**Input:** `price[] = [3, 5, 8, 9, 10, 17, 17, 20]`
**Output:** `24`
**Explanation:** The maximum obtainable value is `24` by cutting the rod into `8` pieces of length `1`, i.e., `8*price[1] = 8*3 = 24`.

### Example 3

**Input:** `price[] = [3]`
**Output:** `3`
**Explanation:** There is only `1` way to pick a piece of length `1`.

---

## Constraints

* `1 ≤ price.size() ≤ 10^3`
* `1 ≤ price[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n)`

---

## Company Tags

* Google

---

## Topic Tags

* Arrays
* Dynamic Programming
* Data Structures
* Algorithms

---

## Related Articles

* [Cutting A Rod DP 13](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/)

---

---

awesome—here’s everything you need for **Rod Cutting**.

---

# 2) Explanation (what & why) + step-by-step dry run

## Problem recap

* You have a rod of length `n`.
* `price[i]` = value of a piece of **length i** (array is conceptually 1-indexed; in Python you’ll get it 0-indexed, i.e. `price[i-1]`).
* Cut the rod into any number of pieces (including zero cuts).
* Goal: **maximize total value**.

This is the classic **unbounded knapsack** with:

* item “types” = piece lengths `1..n`
* value of type `i` = `price[i]`
* weight of type `i` = `i`
* capacity = `n`
* unbounded = you can use each length any number of times

## Most-used recurrence

Let `best[L]` be the maximum revenue for a rod of length `L`.

```
best[0] = 0
best[L] = max over 1≤cut≤L of ( price[cut] + best[L - cut] )
```

Why it works: the **first cut** is length `cut`, yielding `price[cut]`, and the remainder `L−cut` is solved optimally by `best[L-cut]`. Try all `cut`.

Time `O(n^2)`, Space `O(n)`.

---

## Dry run (Example 1)

`price = [1, 5, 8, 9, 10, 17, 17, 20]`  (so `n = 8`)

We compute `best[L]` for `L = 0..8`.

* `best[0]=0`
* `best[1]=max(1+best0)=1`
* `best[2]=max(1+best1=2, 5+best0=5)=5`
* `best[3]=max(1+5=6, 5+1=6, 8+0=8)=8`
* `best[4]=max(1+8=9, 5+5=10, 8+1=9, 9+0=9)=10`
* `best[5]=max(1+10=11, 5+8=13, 8+5=13, 9+1=10, 10+0=10)=13`
* `best[6]=max(1+13=14, 5+10=15, 8+8=16, 9+5=14, 10+1=11, 17+0=17)=17`
* `best[7]=max(1+17=18, 5+13=18, 8+10=18, 9+8=17, 10+5=15, 17+1=18, 17+0=17)=18`
* `best[8]=max(1+18=19, 5+17=22, 8+13=21, 9+10=19, 10+8=18, 17+5=22, 17+1=18, 20+0=20)=**22**`

Answer = `22` (e.g., cut as 2 + 6 → 5 + 17).

---

# 3) Python solutions (brute → memo → bottom-up)

All snippets follow the requested signature:

```python
#User function Template for python3
class Solution:
    def cutRod(self, price):
        # code here
```

### A) Brute force (exponential; for teaching only)

```python
#User function Template for python3
class SolutionBrute:
    def cutRod(self, price):
        """
        Try all first cuts recursively.
        Time  : Exponential (~O(2^n))
        Space : O(n) recursion
        """
        n = len(price)

        def f(L):
            if L == 0:
                return 0
            best = 0
            # try first cut of length cut (1..L)
            for cut in range(1, L + 1):
                best = max(best, price[cut - 1] + f(L - cut))
            return best

        return f(n)
```

---

### B) Top-down + memoization (optimal O(n²), easy to explain)

```python
from functools import lru_cache

class SolutionMemo:
    def cutRod(self, price):
        """
        Memoize the brute force.
        Time  : O(n^2) -- for each length we try up to n first-cuts once
        Space : O(n)   -- memo + recursion depth
        """
        n = len(price)

        @lru_cache(None)
        def f(L):
            if L == 0:
                return 0
            best = 0
            for cut in range(1, L + 1):
                best = max(best, price[cut - 1] + f(L - cut))
            return best

        return f(n)
```

---

### C) Bottom-up 1-D DP (recommended; clean & fast)

```python
#User function Template for python3
class Solution:
    def cutRod(self, price):
        """
        Unbounded knapsack / rod cutting.
        best[L] = max_{1<=cut<=L} (price[cut-1] + best[L-cut])

        Time  : O(n^2)
        Space : O(n)
        """
        n = len(price)
        best = [0] * (n + 1)   # best[0]=0

        for L in range(1, n + 1):           # increasing length
            max_val = 0
            # try first cut of every allowable length
            for cut in range(1, L + 1):     # O(L)
                max_val = max(max_val, price[cut - 1] + best[L - cut])
            best[L] = max_val

        return best[n]
```

---

### D) (Optional) 2-D “Knapsack style” DP

```python
class Solution2D:
    def cutRod(self, price):
        """
        2-D DP: dp[i][L] = max value using piece lengths 1..i to fill length L (unbounded).
        Transition:
            dp[i][L] = max( dp[i-1][L], price[i-1] + dp[i][L - i] ) if L>=i
        Time  : O(n^2)
        Space : O(n^2)
        """
        n = len(price)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for L in range(1, n+1):
                dp[i][L] = dp[i-1][L]
                if L >= i:
                    dp[i][L] = max(dp[i][L], price[i-1] + dp[i][L-i])
        return dp[n][n]
```

---

# 4) Interview Q&A (the ones that come up a lot)

**Q1. Why is this unbounded knapsack?**
Because you may use each length any number of times (e.g., eight pieces of length 1), just like taking an item repeatedly in unbounded knapsack.

**Q2. State the recurrence.**
`best[L] = max_{1≤cut≤L} ( price[cut] + best[L − cut] )` with `best[0]=0`.
(If coding 0-indexed: `price[cut-1]`.)

**Q3. Complexity of the standard DP?**
`O(n^2)` time (for each `L` you scan `cut=1..L`), `O(n)` space (1-D array).

**Q4. Do we need to cut at least once?**
No—“cutting up and selling the pieces” allows **no cut**; the DP already considers taking the full piece of length `n` (cut = `n`).

**Q5. Edge cases?**

* `n=1` → return `price[0]`.
* Prices can be non-monotonic; DP still handles it (e.g., it may be better to make many small cuts).
* Ensure you use `price[cut-1]` if the input is 0-indexed.

**Q6. How to reconstruct the actual cuts?**
Keep a `take[L]` pointer storing the `cut` that achieved `best[L]`. Then backtrack: while `L>0`, emit `take[L]` and set `L -= take[L]`.

**Q7. Why not greedy (always choose the best `price[i]/i`)?**
Counterexamples exist; local density doesn’t guarantee global optimality. The DP checks all splits.

---

---

here’s a **ready-to-run program** for **Rod Cutting** that:

* reads the `price[]` line from stdin (space/comma/brackets allowed),
* solves it **three ways** (bottom-up 1D DP, top-down memo, 2D knapsack-style),
* prints the input and **outputs**, and
* **times** each method inline using `timeit.timeit(number=1)`.

I added tight, interview-style comments noting **time/space complexity** exactly where they apply.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Rod Cutting
# price[i] = value of a piece of length (i+1)  [0-indexed input]
# Goal: maximize total value for rod of length n = len(price).
#
# Methods:
#   1) Bottom-up 1D DP (recommended)      : O(n^2) time, O(n) space
#   2) Top-down DP with memoization       : O(n^2) time, O(n) space
#   3) 2D Unbounded-Knapsack-style DP     : O(n^2) time, O(n^2) space
#
# Input (stdin):
#   One line: the price array (space/comma separated; [] allowed)
#
# Output:
#   - Echo of parsed input
#   - Answer from each method
#   - Per-method timing (ms) using timeit.timeit(number=1)
# ------------------------------------------------------------

import sys
import timeit
from functools import lru_cache

# --------------------------- Method 1 ---------------------------
class Solution:
    def cutRod(self, price):
        """
        Bottom-up 1D DP (classic)
        best[L] = max_{1<=cut<=L} ( price[cut-1] + best[L-cut] )

        Time  : O(n^2)   -- for each length L, we scan all 'cut' = 1..L
        Space : O(n)     -- single 1D array 'best'
        """
        n = len(price)
        best = [0] * (n + 1)  # best[0] = 0

        # For each target length L = 1..n
        for L in range(1, n + 1):           # executes n times
            max_val = 0
            # Try making the first cut at every length 'cut' in 1..L
            for cut in range(1, L + 1):     # executes ~L times -> sum_L O(n^2)
                # price[cut-1] is value of piece of length 'cut'
                # best[L-cut] reuses the precomputed optimal remainder
                max_val = max(max_val, price[cut - 1] + best[L - cut])
            best[L] = max_val
        return best[n]


# --------------------------- Method 2 ---------------------------
class SolutionMemo:
    def cutRod(self, price):
        """
        Top-down recursion with memoization (same recurrence).
        Time  : O(n^2) -- at most n states, each tries up to n first-cuts
        Space : O(n)   -- memo size + recursion depth
        """
        n = len(price)

        @lru_cache(None)
        def f(L):
            if L == 0:
                return 0
            best = 0
            # Try first cut = 1..L
            for cut in range(1, L + 1):     # up to L iterations per state
                best = max(best, price[cut - 1] + f(L - cut))
            return best

        return f(n)


# --------------------------- Method 3 ---------------------------
class Solution2D:
    def cutRod(self, price):
        """
        2D DP (unbounded knapsack view):
        dp[i][L] = max value using piece lengths 1..i to fill length L.

        Transition:
          dp[i][L] = max( dp[i-1][L],  price[i-1] + dp[i][L - i] ) if L >= i
                      (skip piece i)      (take piece i again)

        Time  : O(n^2)  -- i in 1..n, L in 1..n
        Space : O(n^2)  -- table (n+1) x (n+1)
        """
        n = len(price)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # i = piece length, L = target length
        for i in range(1, n + 1):           # O(n)
            for L in range(1, n + 1):       # O(n)
                dp[i][L] = dp[i - 1][L]     # skip using piece length i
                if L >= i:
                    # take piece length i (value price[i-1]) and stay at i (unbounded)
                    dp[i][L] = max(dp[i][L], price[i - 1] + dp[i][L - i])
        return dp[n][n]


# ------------------------------ I/O ------------------------------
def _parse_prices():
    """
    Parse a single line with price array:
      e.g. "1 5 8 9 10 17 17 20" or "[1,5,8,9,10,17,17,20]"
    """
    data = sys.stdin.read().strip()
    if not data:
        print("Please provide one line with price array (e.g. '1 5 8 9').")
        sys.exit(0)
    line = data.replace("[", " ").replace("]", " ").replace(",", " ")
    price = [int(x) for x in line.split()]
    return price

def _preview(price, limit=80):
    s = " ".join(map(str, price))
    if len(s) <= limit:
        return f"price (n={len(price)}): [{s}]"
    return f"price (n={len(price)}): [{s[:limit]}...]"

# ------------------------------ Main -----------------------------
def main():
    price = _parse_prices()
    print(_preview(price))
    print()

    sol1 = Solution()
    sol2 = SolutionMemo()
    sol3 = Solution2D()

    # Time each method once (number=1) and compute result for printing
    t1 = timeit.timeit(lambda: sol1.cutRod(price), number=1)
    a1 = sol1.cutRod(price)

    t2 = timeit.timeit(lambda: sol2.cutRod(price), number=1)
    a2 = sol2.cutRod(price)

    t3 = timeit.timeit(lambda: sol3.cutRod(price), number=1)
    a3 = sol3.cutRod(price)

    print("Bottom-up 1D DP     (O(n^2) time, O(n)   space) :", a1)
    print("Time (ms): {:.3f}\n".format(t1 * 1000.0))
    print("Top-down + memo     (O(n^2) time, O(n)   space) :", a2)
    print("Time (ms): {:.3f}\n".format(t2 * 1000.0))
    print("2D Unbounded-Knapsack (O(n^2) time, O(n^2) space):", a3)
    print("Time (ms): {:.3f}".format(t3 * 1000.0))

    print("\nAll methods agree ✔" if (a1 == a2 == a3) else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 rod_cutting.py
1 5 8 9 10 17 17 20
```

**Example output (timings vary by machine):**

```
price (n=8): [1 5 8 9 10 17 17 20]

Bottom-up 1D DP     (O(n^2) time, O(n)   space) : 22
Time (ms): 0.170

Top-down + memo     (O(n^2) time, O(n)   space) : 22
Time (ms): 0.210

2D Unbounded-Knapsack (O(n^2) time, O(n^2) space): 22
Time (ms): 0.250

All methods agree ✔
```

---

## 6) Real-World Use Cases (compact + important)

1. **Steel/wood/cable cutting for sales:** Decide how to cut raw stock (rods, boards, wire) to maximize revenue given market prices for different lengths.

2. **Telecom & fiber deployment:** Cutting fiber reels into customer-ordered lengths while maximizing value (or minimizing waste in the variant with costs).

3. **Manufacturing & logistics planning:** A core pattern for **unbounded knapsack** problems where items can be repeated—e.g., packing, resource allocation, ribbon/fabric cutting.

4. **Pricing strategy simulation:** Evaluate how changing the price list for standard lengths affects optimal cuts and total revenue.
