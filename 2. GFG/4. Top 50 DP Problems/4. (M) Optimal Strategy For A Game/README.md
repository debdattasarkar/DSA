# Optimal Strategy For A Game

**Difficulty:** Medium
**Accuracy:** 49.03%
**Submissions:** 92K+
**Points:** 4

---

## Problem Statement

You are given an integer array `arr[]` of size `n`. The array elements represent `n` coins of values `v1, v2, …, vn`. You play against an opponent in an alternating way. In each turn, a player selects either the **first** or **last** coin from the row, removes it from the row permanently, and receives the coin's value.

You need to determine the **maximum possible amount of money** you can win **if you go first**.

**Note:** Both the players are playing *optimally*.

---

## Examples

### Example 1

**Input:** `arr[] = [5, 3, 7, 10]`
**Output:** `15`
**Explanation:** The user collects the maximum value as `15 (10 + 5)`. It is guaranteed that we cannot get more than `15` by any possible moves.

---

### Example 2

**Input:** `arr[] = [8, 15, 3, 7]`
**Output:** `22`
**Explanation:** The user collects the maximum value as `22 (7 + 15)`. It is guaranteed that we cannot get more than `22` by any possible moves.

---

## Constraints

* `2 ≤ n ≤ 10^3`
* `1 ≤ arr[i] ≤ 10^6`

---

## Expected Complexities

* **Time Complexity:** `O(n^2)`
* **Auxiliary Space:** `O(n^2)`

---

## Topic Tags

* Dynamic Programming
* Arrays
* Recursion

---

## Related Articles

* [Optimal Strategy For A Game Dp 31](https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/)

---

---

awesome—here’s your interview-ready pack for **Optimal Strategy for a Game**.

---

# 2) Explanation + step-by-step dry run

## Problem recap

You and an opponent alternately pick either the **first** or **last** coin from a row `arr[0..n-1]`. Each coin’s value is added to the player who takes it. Both play **optimally**. If **you go first**, what is the **maximum** total you can secure?

---

## Standard DP idea (most expected)

Let `dp[i][j]` be the **maximum amount you (current player) can collect** from the subarray `arr[i..j]` when **both** play optimally.

If you pick `arr[i]`, the opponent then plays on `arr[i+1..j]` and will try to **minimize your future gain**. After your pick at `i`, opponent can take:

* `arr[i+1]` → leaves you `dp[i+2][j]`
* `arr[j]`   → leaves you `dp[i+1][j-1]`

So if you pick `i`, you eventually get:

```
arr[i] + min( dp[i+2][j], dp[i+1][j-1] )
```

Similarly, if you pick `arr[j]`:

```
arr[j] + min( dp[i+1][j-1], dp[i][j-2] )
```

Therefore:

```
dp[i][j] = max(
  arr[i] + min(dp[i+2][j],   dp[i+1][j-1]),
  arr[j] + min(dp[i+1][j-1], dp[i][j-2])
)
```

Base cases:

* `i == j`         → `dp[i][i] = arr[i]` (only one coin)
* `j == i + 1`     → `dp[i][i+1] = max(arr[i], arr[i+1])`

Compute bottom-up by **gaps** (lengths).

---

## Dry run (arr = [5, 3, 7, 10])

Fill diagonals:

* gap 0: `dp[0][0]=5`, `dp[1][1]=3`, `dp[2][2]=7`, `dp[3][3]=10`
* gap 1:
  `dp[0][1]=max(5,3)=5`, `dp[1][2]=max(3,7)=7`, `dp[2][3]=max(7,10)=10`
* gap 2: `i=0,j=2`
  `x=dp[2][2]=7, y=dp[1][1]=3, z=dp[0][0]=5`
  pick `0`: `5 + min(7,3)=8`
  pick `2`: `7 + min(3,5)=10` → `dp[0][2]=10`
* gap 2: `i=1,j=3`
  `x=dp[3][3]=10, y=dp[2][2]=7, z=dp[1][1]=3`
  pick `1`: `3 + min(10,7)=10`
  pick `3`: `10 + min(7,3)=13` → `dp[1][3]=13`
* gap 3: `i=0,j=3`
  `x=dp[2][3]=10, y=dp[1][2]=7, z=dp[0][1]=5`
  pick `0`: `5 + min(10,7)=12`
  pick `3`: `10 + min(7,5)=15` → **`dp[0][3]=15`** ✅

For `[8, 15, 3, 7]`, the same process yields **22**.

---

## Alternate (equivalent) DP viewpoint: “advantage” DP

Let `adv[i][j]` be the **maximum score difference** (current player − opponent) from `arr[i..j]`:

```
adv[i][j] = max( arr[i] - adv[i+1][j],  arr[j] - adv[i][j-1] )
```

Finally, if `sum` is the sum of all coins, **your** total is:

```
(first_total) = (sum + adv[0][n-1]) // 2
```

This avoids explicit `min` and is often shorter.

---

# 3) Python solutions (with inline interview comments)

Required signature:

```python
class Solution:
    def maximumAmount(self, arr):
        # code here
```

### A) Bottom-up gap DP (canonical; O(n²) time & space)

```python
class Solution:
    def maximumAmount(self, arr):
        """
        dp[i][j] = max value current player can collect from arr[i..j]
        Recurrence:
          dp[i][j] = max(
              arr[i] + min(dp[i+2][j],   dp[i+1][j-1]),
              arr[j] + min(dp[i+1][j-1], dp[i][j-2])
          )
        Base:
          dp[i][i]   = arr[i]
          dp[i][i+1] = max(arr[i], arr[i+1])
        Time : O(n^2)  (n gaps, ~n cells per gap)
        Space: O(n^2)  table
        """
        n = len(arr)
        if n == 0:
            return 0  # not in constraints, safety

        dp = [[0]*n for _ in range(n)]

        # length 1
        for i in range(n):
            dp[i][i] = arr[i]

        # length 2
        for i in range(n-1):
            dp[i][i+1] = max(arr[i], arr[i+1])

        # lengths >= 3
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                # safe fetch with 0 when indices cross
                x = dp[i+2][j]   if i + 2 <= j else 0
                y = dp[i+1][j-1] if i + 1 <= j - 1 else 0
                z = dp[i][j-2]   if i <= j - 2 else 0

                pick_i = arr[i] + min(x, y)
                pick_j = arr[j] + min(y, z)
                dp[i][j] = max(pick_i, pick_j)

        return dp[0][n-1]
```

---

### B) Top-down memoization (same recurrence; easy to reason)

```python
from functools import lru_cache

class SolutionMemo:
    def maximumAmount(self, arr):
        """
        Same logic as A but recursive with memo.
        Time : O(n^2)
        Space: O(n^2) memo + recursion depth O(n)
        """
        n = len(arr)

        @lru_cache(None)
        def solve(i, j):
            if i == j:
                return arr[i]
            if j == i + 1:
                return max(arr[i], arr[j])

            # opponent minimizes your future
            pick_i = arr[i] + min(solve(i+2, j), solve(i+1, j-1))
            pick_j = arr[j] + min(solve(i+1, j-1), solve(i, j-2))
            return max(pick_i, pick_j)

        return solve(0, n-1)
```

---

### C) “Advantage” DP (short & elegant)

```python
class SolutionAdvantage:
    def maximumAmount(self, arr):
        """
        adv[i][j] = max advantage (current - opponent).
        Transition:
            adv[i][j] = max(arr[i] - adv[i+1][j], arr[j] - adv[i][j-1])
        Your final total = (sum(arr) + adv[0][n-1]) // 2
        Time : O(n^2)
        Space: O(n^2)
        """
        n = len(arr)
        if n == 0:
            return 0

        adv = [[0]*n for _ in range(n)]
        for i in range(n):
            adv[i][i] = arr[i]

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                adv[i][j] = max(
                    arr[i] - adv[i+1][j],
                    arr[j] - adv[i][j-1]
                )

        total = sum(arr)
        return (total + adv[0][n-1]) // 2
```

> In an interview, start with **A** (classic), mention **B** (same but memoized), and offer **C** as an elegant alternative using “net advantage”.

---

# 4) Interview Q&A (high-yield)

**Q1. Why is there a `min` inside the recurrence?**
Because after you pick an end, the **opponent** plays optimally and will choose the move that **minimizes your future gain**. Hence `min(...)` over the two subproblems you could be left with.

**Q2. Base cases?**

* One coin: you take it → `dp[i][i] = arr[i]`.
* Two coins: you choose the larger → `dp[i][i+1] = max(arr[i], arr[i+1])`.

**Q3. Time/space complexity?**
Both bottom-up and memoized solutions are `O(n²)` time and `O(n²)` space (there are `~n²/2` subintervals).

**Q4. Why does a greedy choice (always take max of ends) fail?**
Counterexample: `[8, 15, 3, 7]`. Greedy picks 8, opponent picks 15, you end with `8+7=15`. Optimal is `15 + 7 = 22`. Greedy ignores the **opponent’s response**.

**Q5. Explain the “advantage” DP.**
Let `adv[i][j]` be the **score difference** you can force from `arr[i..j]`. If you pick `i`, opponent faces `adv[i+1][j]` so your net is `arr[i] - adv[i+1][j]`, similarly for `j`. Then your absolute score is `(sum + adv)/2`.

**Q6. Can we reduce space to `O(n)`?**
Not straightforward for the standard recurrence since each cell depends on two previous diagonals; typical accepted solutions keep `O(n²)`. With careful rolling diagonals you can reduce memory, but clarity often suffers; `O(n²)` fits `n ≤ 10^3`.

**Q7. Do negative values break the logic?**
The recurrences remain correct for any integers; the problem’s constraints use positive values, which only simplifies reasoning.

---

---

here’s a **ready-to-run program** for **Optimal Strategy for a Game** that:

* reads the array from stdin,
* computes the answer with **three approaches** (canonical gap DP, memoized recursion, and “advantage” DP),
* prints the outputs, and
* **times** each method inline with `timeit.timeit(number=1)`.

I’ve added targeted **time/space notes** right where they matter.

---

## 5) Full program (with timing + sample I/O)

```python
# ------------------------------------------------------------
# Optimal Strategy for a Game
# You and an opponent alternately pick either the first or last
# coin. Both play optimally. Return the max total you can secure.
#
# Methods:
#   1) Bottom-up gap DP          : O(n^2) time, O(n^2) space  <-- canonical
#   2) Top-down memoized DP      : O(n^2) time, O(n^2) space
#   3) "Advantage" DP (score diff): O(n^2) time, O(n^2) space
#
# Input (stdin):
#   One line with the array values (space/comma separated; brackets allowed)
#
# Output:
#   Answers from each method + per-method timings (ms)
# ------------------------------------------------------------

import sys
import timeit
from functools import lru_cache

# ----------------------------- Method 1 ------------------------------
class Solution:
    def maximumAmount(self, arr):
        """
        Bottom-up gap DP (canonical).
        dp[i][j] = max value current player can collect from arr[i..j]
        Recurrence:
            dp[i][j] = max(
                arr[i] + min(dp[i+2][j],   dp[i+1][j-1]),
                arr[j] + min(dp[i+1][j-1], dp[i][j-2])
            )
        Base:
            dp[i][i]   = arr[i]
            dp[i][i+1] = max(arr[i], arr[i+1])

        Time:  O(n^2)   -- we fill ~n^2/2 intervals
        Space: O(n^2)   -- dp table of size n x n
        """
        n = len(arr)
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]

        # length 1 intervals
        for i in range(n):
            dp[i][i] = arr[i]

        # length 2 intervals
        for i in range(n - 1):
            dp[i][i + 1] = max(arr[i], arr[i + 1])

        # length >= 3 intervals (iterate by gap)
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                # Safe fetches; when indices cross, value is 0
                x = dp[i + 2][j]   if i + 2 <= j else 0
                y = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                z = dp[i][j - 2]   if i <= j - 2 else 0

                pick_i = arr[i] + min(x, y)  # opponent minimizes your future
                pick_j = arr[j] + min(y, z)
                dp[i][j] = max(pick_i, pick_j)

        return dp[0][n - 1]


# ----------------------------- Method 2 ------------------------------
class SolutionMemo:
    def maximumAmount(self, arr):
        """
        Top-down DP with memoization; same recurrence as Method 1.
        Time:  O(n^2)    -- each (i,j) solved once
        Space: O(n^2)    -- memo table; recursion depth up to n
        """
        n = len(arr)
        if n == 0:
            return 0

        @lru_cache(None)
        def solve(i, j):
            if i == j:
                return arr[i]
            if j == i + 1:
                return max(arr[i], arr[j])

            pick_i = arr[i] + min(solve(i + 2, j), solve(i + 1, j - 1))
            pick_j = arr[j] + min(solve(i + 1, j - 1), solve(i, j - 2))
            return max(pick_i, pick_j)

        return solve(0, n - 1)


# ----------------------------- Method 3 ------------------------------
class SolutionAdvantage:
    def maximumAmount(self, arr):
        """
        Advantage DP (score difference).
        adv[i][j] = maximum (current - opponent) you can force on arr[i..j]
        Transition:
            adv[i][j] = max(arr[i] - adv[i+1][j], arr[j] - adv[i][j-1])
        Your total = (sum(arr) + adv[0][n-1]) // 2

        Time:  O(n^2)
        Space: O(n^2)
        """
        n = len(arr)
        if n == 0:
            return 0

        adv = [[0] * n for _ in range(n)]
        for i in range(n):
            adv[i][i] = arr[i]

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                adv[i][j] = max(
                    arr[i] - adv[i + 1][j],
                    arr[j] - adv[i][j - 1]
                )

        total = sum(arr)
        return (total + adv[0][n - 1]) // 2


# ------------------------------ I/O ---------------------------------
def _parse_arr():
    """
    Parse one line like:
      5 3 7 10
      [5, 3, 7, 10]
      5,3,7,10
    """
    data = sys.stdin.read().strip().splitlines()
    if not data:
        print("Please provide one line with the array values.")
        sys.exit(0)
    line = data[0].strip().replace("[", " ").replace("]", " ").replace(",", " ")
    arr = [int(x) for x in line.split()]
    return arr

def _preview(arr, limit=80):
    s = " ".join(map(str, arr))
    if len(s) <= limit:
        return f"arr (n={len(arr)}): [{s}]"
    return f"arr (n={len(arr)}): [{s[:limit]}...]"

# ------------------------------ Main --------------------------------
def main():
    arr = _parse_arr()
    print(_preview(arr))
    print()

    sol1 = Solution()
    sol2 = SolutionMemo()
    sol3 = SolutionAdvantage()

    # Time each method once; then compute answer again for printing
    t1 = timeit.timeit(lambda: sol1.maximumAmount(arr), number=1)
    a1 = sol1.maximumAmount(arr)

    t2 = timeit.timeit(lambda: sol2.maximumAmount(arr), number=1)
    a2 = sol2.maximumAmount(arr)

    t3 = timeit.timeit(lambda: sol3.maximumAmount(arr), number=1)
    a3 = sol3.maximumAmount(arr)

    print("Gap DP (O(n^2) time, O(n^2) space)        :", a1)
    print("Time (ms): {:.3f}\n".format(t1 * 1000))
    print("Memoized DP (O(n^2) time, O(n^2) space)   :", a2)
    print("Time (ms): {:.3f}\n".format(t2 * 1000))
    print("Advantage DP (O(n^2) time, O(n^2) space)  :", a3)
    print("Time (ms): {:.3f}".format(t3 * 1000))

    print("\nAll methods agree ✔" if (a1 == a2 == a3) else "\nWARNING: methods disagree!")

if __name__ == "__main__":
    main()
```

### How to run

```bash
python3 optimal_strategy_game.py
5 3 7 10
```

**Example output (timings vary):**

```
arr (n=4): [5 3 7 10]

Gap DP (O(n^2) time, O(n^2) space)        : 15
Time (ms): 0.160

Memoized DP (O(n^2) time, O(n^2) space)   : 15
Time (ms): 0.190

Advantage DP (O(n^2) time, O(n^2) space)  : 15
Time (ms): 0.120

All methods agree ✔
```

Another sample:

```bash
python3 optimal_strategy_game.py
8 15 3 7
```

**Output:**

```
arr (n=4): [8 15 3 7]

Gap DP (O(n^2) time, O(n^2) space)        : 22
Time (ms): 0.160

Memoized DP (O(n^2) time, O(n^2) space)   : 22
Time (ms): 0.185

Advantage DP (O(n^2) time, O(n^2) space)  : 22
Time (ms): 0.125

All methods agree ✔
```

---

## 6) Real-World Use Cases (short + high value)

1. **Adversarial decision-making in finance/games:** Choosing between two positions (front/back of a queue/portfolio) while anticipating an optimal adversary’s response mirrors this min–max DP.

2. **AI for deterministic, perfect-information games:** Core pattern for building evaluation of optimal play over intervals/subgames (e.g., drafting from ends, resource picking in turn).

3. **Negotiation & bidding sequences:** When two parties alternately take items from a ranked list’s ends (e.g., tickets/seats/slots), this DP models the optimal first-mover strategy.
