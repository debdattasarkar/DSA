
---

# 💹 Stock Buy and Sell with Cooldown

### Difficulty: Medium

**Accuracy:** 51.65%
**Submissions:** 11K+
**Points:** 4
**Average Time:** 20 minutes

---

## 🧠 Problem Statement

Given an array **arr[]**, where the *i-th* element of `arr[i]` represents the price of a stock on the *i-th* day (all prices are non-negative integers).
Find the **maximum profit** you can make by buying and selling stocks such that after selling a stock, you **cannot buy again on the next day** (i.e., there is a **one-day cooldown**).

---

## 🧩 Examples

### Example 1

**Input:**

```
arr[] = [0, 2, 1, 2, 3]
```

**Output:**

```
3
```

**Explanation:**
You first buy on day 1, sell on day 2, then cool down, then buy on day 4, and sell on day 5.
Total profit earned = (2 - 0) + (3 - 2) = **3**, which is the maximum achievable profit.

---

### Example 2

**Input:**

```
arr[] = [3, 1, 6, 1, 2, 4]
```

**Output:**

```
7
```

**Explanation:**
You first buy on day 2 and sell on day 3, then cool down, then again buy on day 5 and sell on day 6.
Clearly, the total profit earned = (6 - 1) + (4 - 2) = **7**, which is the maximum achievable profit.

---

## ⚙️ Constraints

* ( 1 \leq arr.size() \leq 10^5 )
* ( 1 \leq arr[i] \leq 10^4 )

---

## ⏱️ Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(1)

---

## 🏷️ Topic Tags

* Dynamic Programming

---

## 📚 Related Articles

* [**Maximizing Stock Profit with Cooldown**](https://www.geeksforgeeks.org/maximizing-stock-profit-with-cooldown/)

---

---

awesome — let’s nail **Stock Buy & Sell with 1-day Cooldown** the interview way.

---

# 2) Explanation + step-by-step dry run

## Problem in one line

Given daily prices `arr[i]`, you may buy and sell multiple times, but **after a sell you must cooldown for 1 day** (no buy the next day). Maximize profit.

## State thinking (classic 3-state DP)

For each day `i`, track the best profit if you end the day in one of these states:

1. **hold** — you **currently hold** a stock

   * Either you already held it yesterday, or you buy today from the `rest` state:
     `hold[i] = max(hold[i-1], rest[i-1] - price[i])`

2. **sold** — you **just sold** today

   * Must have held yesterday:
     `sold[i] = hold[i-1] + price[i]`

3. **rest** — you **hold nothing and didn’t just sell today** (free to buy)

   * Either you were already resting yesterday, or you are cooling down after a sell:
     `rest[i] = max(rest[i-1], sold[i-1])`

Answer at the end: **max(sold[n-1], rest[n-1])** (you never want to end while holding).

Base:

```
hold[0] = -price[0]   (buy on day 0)
sold[0] = -inf        (cannot sell on day 0)
rest[0] = 0           (do nothing)
```

### Dry run on Example 1: arr = [0, 2, 1, 2, 3]

Let `-∞` = very negative.

| day | price | hold                | sold       | rest             |
| --- | ----: | ------------------- | ---------- | ---------------- |
| 0   |     0 | max(-∞, 0-0)=**-0** | -∞         | 0                |
| 1   |     2 | max(-0, 0-2)=**0**  | -0+2=**2** | max(0, -∞)=**0** |
| 2   |     1 | max(0, 0-1)=**0**   | 0+1=**1**  | max(0, 2)=**2**  |
| 3   |     2 | max(0, 2-2)=**0**   | 0+2=**2**  | max(2, 1)=**2**  |
| 4   |     3 | max(0, 2-3)=**0**   | 0+3=**3**  | max(2, 2)=**2**  |

Result = max(sold, rest) = **max(3, 2) = 3** ✅
Strategy implied: buy at 0 → sell at 2 (cooldown) → buy at 2 → sell at 3.

---

# 3) Python solutions (from brute → memo → optimal O(1)-space)

All follow your required signature:

```python
class Solution:
    def maxProfit(self, arr):
        # code here
```

### A) Brute recursion (include/skip decisions) — exponential (teaching aid)

```python
class Solution:
    def maxProfit(self, arr):
        """
        Brute-force DFS over decisions (buy/sell/skip).
        Time:  O(2^n)  (at each day we branch)
        Space: O(n)    recursion depth
        """
        n = len(arr)

        def dfs(i, can_buy):
            # i = day index, can_buy = 1 if we are allowed to buy now
            if i >= n:
                return 0
            # Option 1: skip today
            best = dfs(i + 1, can_buy)
            if can_buy:
                # Option 2: buy today -> pay arr[i]
                best = max(best, -arr[i] + dfs(i + 1, 0))
            else:
                # Option 2: sell today -> earn arr[i], then cooldown 1 day
                best = max(best, arr[i] + dfs(i + 2, 1))
            return best

        return dfs(0, 1)
```

### B) Top-down DP with memo (linear time)

```python
class Solution:
    def maxProfit(self, arr):
        """
        DFS + memo on (i, can_buy).
        Time:  O(n)      (each state once)
        Space: O(n)      (memo + recursion)
        """
        from functools import lru_cache
        n = len(arr)

        @lru_cache(None)
        def dp(i, can_buy):
            if i >= n:
                return 0
            # Skip
            best = dp(i + 1, can_buy)
            if can_buy:
                # Buy -> move to 'holding' (can't buy next day)
                best = max(best, -arr[i] + dp(i + 1, 0))
            else:
                # Sell -> cooldown next day
                best = max(best, arr[i] + dp(i + 2, 1))
            return best

        return dp(0, 1)
```

### C) Iterative 3-state DP (most expected; O(1) space)

```python
class Solution:
    def maxProfit(self, arr):
        """
        3-state DP with O(1) space:
            hold: max profit holding a stock at end of day i
            sold: max profit just sold today
            rest: max profit holding nothing & not selling today
        Time:  O(n)   (single pass)
        Space: O(1)   (three scalars)
        """
        if not arr:
            return 0

        NEG_INF = -10**18
        hold = -arr[0]     # buy on day 0
        sold = NEG_INF     # cannot sell on day 0
        rest = 0           # do nothing day 0

        for price in arr[1:]:
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            # hold: keep holding OR buy today from resting state
            hold = max(prev_hold, prev_rest - price)

            # sold: must have held yesterday, sell today
            sold = prev_hold + price

            # rest: either keep resting or just cooled down after a sell
            rest = max(prev_rest, prev_sold)

        # End profit must be without a stock in hand
        return max(sold, rest)
```

---

# 4) Interview quick-recall + Q&A

## 5-line pseudo (memorize this)

```
hold = -price0; sold = -inf; rest = 0
for p in prices[1:]:
    new_hold = max(hold, rest - p)
    new_sold = hold + p
    new_rest = max(rest, sold)
    hold, sold, rest = new_hold, new_sold, new_rest
return max(sold, rest)
```

**Mnemonic:** **“H-S-R: Hold, Sold, Rest → update in that order.”**
Or say: **“Hold from Rest, Sold from Hold, Rest from (Rest or Sold).”**

## Likely questions (with crisp answers)

**Q1. Why three states?**
Cooldown only constrains the **buy** after a **sell**. Splitting “no stock” into `sold` (just sold, forced cooldown) and `rest` (free to buy) models this perfectly.

**Q2. Transition intuition?**

* `hold = max(hold, rest - p)` (either keep holding or buy today)
* `sold = hold + p` (you can sell only if you held)
* `rest = max(rest, sold)` (either keep resting or you are cooling down after selling)

**Q3. Base cases?**
`hold=-price[0]`, `sold=-∞`, `rest=0`.

**Q4. Why return `max(sold, rest)` and not include `hold`?**
Ending with a stock unrealizes profit; optimal strategy finishes **not holding**.

**Q5. Complexity?**
Single pass, constant memory → **O(n) time, O(1) space**.

**Q6. Multiple transactions allowed?**
Yes; the DP naturally supports unlimited transactions subject to the cooldown.

**Q7. Can you derive it from the (buy,sell) recurrence with cooldown?**
Yes—this 3-state version is an algebraic simplification of the standard two arrays with an extra “cooldown” dependency.

---

### Tiny sanity check

* If prices strictly increase, strategy buys once and sells at end — DP yields `prices[-1]-prices[0]`.
* If prices strictly decrease, DP returns `0` (never buys).

You’re set—explain the states in one sentence, write the O(1) DP in ~10 lines, and you’ll look sharp.

---

---

great — closing this out with sharp, relatable use cases and a complete, timed program.

# 5) Real-World Use Cases (short & relatable)

* **Retail trading with T+1 lock or risk rule:** After you close a position, your broker/risk engine forces a **one-day cooldown** before you can open a new one. Optimize profit under this policy.
* **Ad bidding with cool-off windows:** After selling an ad impression (committing budget) your system must skip the next auction window to prevent over-exposure; decide buy/sell across days with a cooldown.
* **Inventory promos with blackout day:** After a “sell” (flash sale), policy mandates a no-promo day to stabilize demand; plan purchase (stocking) and sell windows to maximize revenue.
* **Thermal throttling tasks:** Completing a high-power task (sell) forces a cool-down slot where you cannot launch another heavy task (buy). Schedule tasks to maximize throughput/value.

All map directly to the DP: after **sell** you must pass **one idle day** before another **buy**.

---

# 6) Full Python Program (with inline complexity notes + timing)

```python
"""
Stock Buy & Sell with 1-day Cooldown — Full Program
---------------------------------------------------
We have daily prices arr[i]. We can buy/sell multiple times, but after a SELL
we must COOL DOWN for 1 day (cannot buy the next day).

3-state DP (O(1) space):
    hold: max profit ending day i HOLDING a stock
    sold: max profit ending day i having JUST SOLD today
    rest: max profit ending day i with NO stock and NOT selling today

Transitions per day (O(1) each):
    new_hold = max(hold, rest - price)   # keep holding or buy from rest
    new_sold = hold + price              # sell what we held
    new_rest = max(rest, sold)           # keep resting or cool down after sell

Overall complexity:
    Time:  O(n)  (single pass over days)
    Space: O(1)  (3 scalars), excluding the input
"""

import timeit

class Solution:
    def maxProfit(self, arr):
        """
        Args:
            arr: List[int] - price per day
        Returns:
            int - maximum profit under 1-day cooldown

        Step-by-step complexity:
            - Initialization: O(1)
            - For-loop across n-1 days: O(n)
            - Each iteration does O(1) arithmetic and assignments
            => Total Time: O(n), Space: O(1)
        """
        if not arr:
            return 0

        NEG_INF = -10**18
        # Day 0 base states (O(1))
        hold = -arr[0]   # buy on day 0
        sold = NEG_INF   # cannot have sold yet
        rest = 0         # do nothing

        # Single pass O(n)
        for price in arr[1:]:
            # keep previous values to compute new states (O(1))
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            # Update states (each O(1))
            hold = max(prev_hold, prev_rest - price)  # hold from rest by buying, or keep holding
            sold = prev_hold + price                  # sell today (must have held yesterday)
            rest = max(prev_rest, prev_sold)          # either keep resting or cooldown after yesterday's sell

        # End without stock in hand (O(1))
        return max(sold, rest)


# -------------------- Demo + Timing --------------------
if __name__ == "__main__":
    tests = [
        ("Example 1", [0, 2, 1, 2, 3], 3),
        ("Example 2", [3, 1, 6, 1, 2, 4], 7),
        # a couple of extra sanity checks
        ("Monotone up", [1, 2, 3, 4, 5], 4),   # buy day1, sell day5
        ("Monotone down", [9, 7, 5, 3, 1], 0)  # never buy
    ]

    solver = Solution()
    for name, prices, expected in tests:
        # Time the full call exactly once (includes all DP work)
        elapsed = timeit.timeit(lambda: solver.maxProfit(prices), number=1)
        result = solver.maxProfit(prices)
        print(f"{name}:")
        print(f"  Input     : {prices}")
        print(f"  Output    : {result}  (expected: {expected})")
        print(f"  Run time  : {elapsed:.8f} s\n")
```

### What you’ll see when running

```
Example 1:
  Input     : [0, 2, 1, 2, 3]
  Output    : 3  (expected: 3)
  Run time  : 0.00000xx s

Example 2:
  Input     : [3, 1, 6, 1, 2, 4]
  Output    : 7  (expected: 7)
  Run time  : 0.00000xx s

Monotone up:
  Input     : [1, 2, 3, 4, 5]
  Output    : 4  (expected: 4)
  Run time  : 0.00000xx s

Monotone down:
  Input     : [9, 7, 5, 3, 1]
  Output    : 0  (expected: 0)
  Run time  : 0.00000xx s
```

**Interview-ready takeaways**

* State meaning in one line each (Hold/Sold/Rest).
* Update mantra: **“Hold from Rest, Sold from Hold, Rest from Rest/Sold”**.
* Complexity: **O(n) time, O(1) space**; returns `max(sold, rest)` (never end holding).
