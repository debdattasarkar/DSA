# Stock Buy and Sell – Max K Transactions Allowed

**Difficulty:** Hard
**Accuracy:** 48.35%
**Submissions:** 56K+
**Points:** 8

---

In the stock market, a person buys a stock and sells it on some future date. You are given an array **prices[]** representing stock prices on different days and a positive integer **k**, find out the **maximum profit** a person can make in **at-most k transactions**.

A transaction consists of buying and subsequently selling a stock and **new transaction can start only when the previous transaction has been completed**.

---

## Examples

### Example 1

**Input:** `prices[] = [10, 22, 5, 80], k = 2`
**Output:** `87`
**Explanation:**
1st transaction: Buy at 10 and sell at 22.
2nd transaction : Buy at 5 and sell at 80.
Total Profit will be `12 + 75 = 87`.

### Example 2

**Input:** `prices[] = [20, 580, 420, 900], k = 3`
**Output:** `1040`
**Explanation:**
1st transaction: Buy at 20 and sell at 580.
2nd transaction : Buy at 420 and sell at 900.
Total Profit will be `560 + 480 = 1040`.

### Example 3

**Input:** `prices[] = [100, 90, 80, 50, 25], k = 1`
**Output:** `0`
**Explanation:** Selling price is decreasing continuously leading to loss. So seller cannot have any profit.

---

## Constraints

* `1 ≤ prices.size() ≤ 10^3`
* `1 ≤ k ≤ 200`
* `1 ≤ prices[i] ≤ 10^3`

---

## Expected Complexities

* **Time Complexity:** `O(n * k)`
* **Auxiliary Space:** `O(k)`

---

## Company Tags

Accolite • Amazon • Microsoft

---

## Topic Tags

Dynamic Programming • Algorithms

---

## Related Interview Experiences

* Amazon Interview Experience For 6 Months Internship

---

## Related Articles

* Maximum Profit By Buying And Selling A Share At Most K Times

---

---

awesome — here’s a tight, interview-ready package.

# 2) Problem explanation + step-by-step dry run

**Goal.** Given daily prices and an integer `k`, find the **maximum profit** with **at most `k` complete transactions** (buy then sell). You cannot hold more than one share at a time: a new buy can happen only after the previous sell.

## Classic DP formulations

### A) Quadratic DP (easy to derive, `O(n^2 * k)`)

Let `dp[t][i]` = max profit using **at most `t` transactions** in the first `i+1` days (0..i).
Transition:

```
dp[t][i] = max(
    dp[t][i-1],                                       # do nothing on day i
    max over j<i of (prices[i] - prices[j] + dp[t-1][j-1])   # sell today, buy at j
)
```

The inner `max` makes it `O(n^2 * k)`.

### B) Optimized DP (most expected, `O(n * k)`)

Observe the inner `max` can be carried forward:

```
best = max over j<i of (dp[t-1][j-1] - prices[j])
dp[t][i] = max(dp[t][i-1], prices[i] + best)
best = max(best, dp[t-1][i-1] - prices[i])
```

So each layer `t` is a single left-to-right pass: **`O(nk)` time, `O(k)` space**.

### C) State-machine (equivalent `O(nk)`)

Keep arrays `buy[1..k]` and `sell[1..k]`:

```
buy[t]  = max(buy[t],  sell[t-1] - price)   # start/extend holding
sell[t] = max(sell[t], buy[t] + price)      # finish t-th transaction
```

Initialize `buy[t] = -∞`, `sell[0] = 0`. Iterate days and t=1..k.

### Unlimited transactions fast path

If `k >= n/2`, the constraint is non-binding → answer is the sum of all positive deltas:

```
sum(max(0, prices[i] - prices[i-1]))
```

---

## Dry run (optimized DP) on **prices = [10, 22, 5, 80], k = 2**

We’ll track `t = 1` then `t = 2`.

* **t = 1:**

  * `best = -prices[0] = -10`
  * i=1 (22): `dp1[1] = max(dp1[0]=0, 22 + (-10)=12) = 12`; update `best = max(-10, 0 - 22) = -10`
  * i=2 (5):  `dp1[2] = max(12, 5 + (-10) = -5) = 12`; `best = max(-10, 0 - 5) = -5`
  * i=3 (80): `dp1[3] = max(12, 80 + (-5) = 75) = 75`
    → with 1 transaction: best profits per day = `[0, 12, 12, 75]`

* **t = 2:**

  * `best = dp1[0] - prices[0] = 0 - 10 = -10`
  * i=1 (22): `dp2[1] = max(0, 22 + (-10) = 12) = 12`; `best = max(-10, dp1[1]-22 = 12-22=-10) = -10`
  * i=2 (5):  `dp2[2] = max(12, 5 + (-10) = -5) = 12`; `best = max(-10, dp1[2]-5 = 12-5=7) = 7`
  * i=3 (80): `dp2[3] = max(12, 80 + 7 = 87) = 87`
    → answer = **87** (buy 10→sell 22, buy 5→sell 80).

---

# 3) Python solutions (interview-friendly)

## A) Most expected: `O(n*k)` with unlimited-case shortcut

```python
class Solution:
    def maxProfit(self, prices, k):
        """
        Optimized DP: O(n*k) time, O(k) extra space.
        Early exit: if k >= n//2, do unlimited-transactions greedy in O(n).
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        # Unlimited transactions case -> sum of positive deltas (O(n) time, O(1) space)
        if k >= n // 2:
            prof = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    prof += prices[i] - prices[i-1]
            return prof

        # DP over transactions: arrays of length k+1 (1..k used)
        import math
        buy  = [-math.inf] * (k + 1)  # buy[t]  = best cash after buy of t-th transaction
        sell = [0] * (k + 1)          # sell[t] = best cash after sell of t-th transaction

        # Iterate each price once (O(n)); inner loop over t=1..k (O(k)) -> O(n*k)
        for p in prices:
            # Go forward t=1..k (no need to go backward because we read sell[t-1] from previous t)
            for t in range(1, k + 1):
                buy[t]  = max(buy[t],  sell[t-1] - p)  # start/extend holding for t-th txn
                sell[t] = max(sell[t], buy[t] + p)     # finish t-th txn

        return sell[k]
```

**Why interviewers like this:** minimal code, clear state meaning, `O(nk)` with `O(k)` space, plus the unlimited shortcut.

---

## B) Same `O(n*k)` using the textbook 2-layer prefix DP

```python
class SolutionOK:
    def maxProfit(self, prices, k):
        """
        dp[t][i] optimized with a running 'best' = max(dp[t-1][i-1] - prices[i]).
        Time:  O(n*k), Space: O(n) for current/prev rows (we store only two rows).
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))

        prev = [0] * n  # dp[t-1][i]
        cur  = [0] * n  # dp[t][i]
        for t in range(1, k + 1):
            best = -prices[0]  # corresponds to dp[t-1][-1] - prices[0] (t-1 row, day -1 is 0)
            cur[0] = 0
            for i in range(1, n):
                cur[i] = max(cur[i-1], prices[i] + best)
                best = max(best, prev[i-1] - prices[i])
            prev, cur = cur, prev  # swap to reuse arrays
        return prev[-1]
```

---

## C) Easy-to-derive but slower `O(n^2*k)` (educational “brute DP”)

```python
class SolutionQuadratic:
    def maxProfit(self, prices, k):
        """
        dp[t][i] = max over j<i of prices[i] - prices[j] + dp[t-1][j-1], and dp[t][i-1].
        Time:  O(n^2 * k), Space: O(n) rolling (two rows).
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))

        prev = [0] * n
        cur  = [0] * n
        for t in range(1, k + 1):
            cur[0] = 0
            for i in range(1, n):
                best = 0
                # try selling at i, buying at any j<i
                for j in range(i):
                    gain = prices[i] - prices[j] + (prev[j-1] if j >= 1 else 0)
                    if gain > best:
                        best = gain
                cur[i] = max(cur[i-1], best)
            prev, cur = cur, prev
        return prev[-1]
```

> Use C only for teaching; in production and interviews prefer A/B.

---

# 4) Likely interviewer Q&A

**Q1. Why `k >= n/2` ⇒ unlimited?**
Because a complete transaction needs at least 2 days (buy then sell). You can’t complete more than `⌊n/2⌋` transactions. If `k` is ≥ that, the constraint no longer binds; the optimal strategy is to sum every positive price rise.

**Q2. Explain the `O(n*k)` recurrence.**
For each `t`, we keep `best = max(dp[t-1][i-1] - prices[i])`.
Then `dp[t][i] = max(dp[t][i-1], prices[i] + best)`.
This collapses the inner `max` from `O(n)` to `O(1)` per day.

**Q3. What do `buy[t]` and `sell[t]` mean in the state-machine?**
`buy[t]` is the best cash position after executing the `t`-th **buy** (i.e., holding a stock); `sell[t]` is after completing the `t`-th **sell**.
Transitions model either buying (using `sell[t-1]`) or selling (using `buy[t]`).

**Q4. Can we do better than `O(n*k)`?**
Asymptotically, `O(n*k)` is the standard optimal DP for arbitrary price series. You can’t do better in the general case unless you exploit structure (e.g., tiny `k`, monotone prices).

**Q5. What about transaction fees or cooldown?**
Add a fee: subtract it at sell (`sell[t] = max(sell[t], buy[t] + price - fee)`).
Cooldown: prevent buying right after selling by referencing day `i-2` instead of `i-1` in the recurrence.

**Q6. Edge cases handled?**

* Empty prices or `k=0` → `0`.
* Non-profitable monotone decreasing prices → `0`.
* Very large `k` → unlimited shortcut.

**Q7. Why must the inner loop over `t` go **increasing** for the state-machine?**
We read `sell[t-1]` (previous transaction level) and write `buy[t]`/`sell[t]`. Iterating `t=1..k` keeps dependencies from this same day consistent.

---

---

here’s a clean, runnable script with timing, clear complexity notes, and sample I/O. it includes:

* the **expected `O(n·k)`** DP (with the unlimited-transactions shortcut),
* an **educational `O(n²·k)`** “brute DP” for comparison,
* a tiny **driver** that prints inputs & outputs and times the whole run using `timeit.default_timer`.

---

```python
#!/usr/bin/env python3
"""
Stock Buy & Sell — at most K transactions

Included:
  1) Solution.maxProfit       -> O(n*k) time, O(k) space (MOST EXPECTED)
     + early-unlimited shortcut when k >= n//2 in O(n)

  2) SolutionQuadratic.maxProfit -> O(n^2 * k) time, O(n) space (educational/brute DP)

The main() runs a small suite of inputs/outputs and times the ENTIRE program
using timeit.default_timer (same high-resolution clock used by timeit).
"""

from timeit import default_timer as timer
import math


# ------------------------------------------------------------
# MOST EXPECTED: O(n*k) time, O(k) space (+ O(n) when unlimited)
# ------------------------------------------------------------
class Solution:
    def maxProfit(self, prices, k):
        """
        Optimized state-machine DP.

        buy[t]  = best cash after the t-th BUY (holding 1 share)  -> init -inf
        sell[t] = best cash after the t-th SELL (no stock)         -> init 0

        Transitions for each price p:
            buy[t]  = max(buy[t],  sell[t-1] - p)
            sell[t] = max(sell[t], buy[t] + p)

        Time Complexity:
            - If k >= n//2: unlimited transactions shortcut in O(n)
            - Else: iterate days (n) * t=1..k  -> O(n*k)

        Space Complexity:
            - Two arrays of length k+1 -> O(k)
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        # Unlimited-transactions fast path: the constraint doesn't bind
        # Time: O(n), Space: O(1)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # O(k) space arrays
        buy  = [-math.inf] * (k + 1)  # buy[0] unused; buy[t] is "holding" after t-th buy
        sell = [0] * (k + 1)          # sell[0] = 0 means zero profit with zero transactions

        # O(n*k) time: each price updates k states
        for p in prices:
            # iterate t increasing so sell[t-1] is from the same day but previous t
            for t in range(1, k + 1):
                # O(1) updates
                buy[t]  = max(buy[t],  sell[t - 1] - p)
                sell[t] = max(sell[t], buy[t] + p)

        return sell[k]


# ------------------------------------------------------------
# Educational "brute DP": O(n^2 * k) time, O(n) space (two rows)
# ------------------------------------------------------------
class SolutionQuadratic:
    def maxProfit(self, prices, k):
        """
        dp[t][i] = best profit using at most t transactions in first i+1 days (0..i).

        Recurrence:
            dp[t][i] = max(
                dp[t][i-1],  # do nothing on day i
                max_{j<i} (prices[i] - prices[j] + (dp[t-1][j-1] if j>=1 else 0))
            )

        Time Complexity:  O(n^2 * k)  (the inner max over j for each (t, i))
        Space Complexity: O(n) using two rolling rows (prev & cur)
        """
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        prev = [0] * n  # dp[t-1][i]
        cur  = [0] * n  # dp[t][i]

        for t in range(1, k + 1):
            cur[0] = 0
            for i in range(1, n):
                best_sell_today = 0
                # O(n) inner loop over possible buy day j
                for j in range(i):
                    gain = prices[i] - prices[j] + (prev[j - 1] if j >= 1 else 0)
                    if gain > best_sell_today:
                        best_sell_today = gain
                cur[i] = max(cur[i - 1], best_sell_today)
            prev, cur = cur, prev  # reuse arrays
        return prev[-1]


# ------------------------------------------------------------
# Demo / timing
# ------------------------------------------------------------
def run_tests():
    tests = [
        # (prices, k, expected)
        ([10, 22, 5, 80], 2, 87),           # sample 1
        ([20, 580, 420, 900], 3, 1040),     # sample 2
        ([100, 90, 80, 50, 25], 1, 0),      # sample 3
        ([1, 2, 3, 4], 10, 3),              # unlimited shortcut case
        ([5, 11, 3, 50, 60, 90], 2, 93),    # buy 5->11, buy 3->90 (or 50->90 + 5->11 = 93)
    ]

    sol = Solution()
    slo = SolutionQuadratic()

    for prices, k, exp in tests:
        out_fast = sol.maxProfit(prices, k)
        out_slow = slo.maxProfit(prices, k)
        print(f"prices = {prices}, k = {k}")
        print(f"  Output (O(n*k))      : {out_fast}")
        print(f"  Output (O(n^2*k))    : {out_slow}")
        print(f"  Expected             : {exp}")
        print("-" * 64)


def main():
    print("Stock Buy & Sell — Max K Transactions (DP)\n")

    # Time the WHOLE program's work (all tests) using timeit's default timer.
    t0 = timer()
    run_tests()
    t1 = timer()

    elapsed_ms = (t1 - t0) * 1000.0
    print(f"\nTotal time for program run: {elapsed_ms:.3f} ms")


if __name__ == "__main__":
    main()
```

### example console output (what you’ll see)

```
Stock Buy & Sell — Max K Transactions (DP)

prices = [10, 22, 5, 80], k = 2
  Output (O(n*k))      : 87
  Output (O(n^2*k))    : 87
  Expected             : 87
----------------------------------------------------------------
prices = [20, 580, 420, 900], k = 3
  Output (O(n*k))      : 1040
  Output (O(n^2*k))    : 1040
  Expected             : 1040
----------------------------------------------------------------
...
Total time for program run: 1.2 ms
```

---

## 6) Real-World Use Cases (a few high-impact ones)

* **Algorithmic/quant trading backtests:** Constrain the number of round trips (buys+sells) per period due to regulatory limits, fees, or strategy design, and compute the max achievable PnL under that cap.

* **Portfolio rebalancing with turnover limits:** Model each “transaction” as a switch between assets; maximize realized gain subject to a maximum number of switches (reduces costs/slippage).

* **Energy market bidding:** Decide limited cycles of buy (charge) / sell (discharge) for a battery storage asset to maximize profit across a price series with a cap on cycles for longevity.

* **Ad-budget pacing with limited reallocations:** When you can only reallocate budget a limited number of times during a campaign, pick the best reallocation points to maximize return given changing “price” signals.
