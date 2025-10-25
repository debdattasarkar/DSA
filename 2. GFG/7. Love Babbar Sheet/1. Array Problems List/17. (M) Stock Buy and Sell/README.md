
---

# 🧩 Stock Buy and Sell

**Difficulty:** Medium
**Accuracy:** 29.18%
**Submissions:** 287K+
**Points:** 4
**Average Time:** 20m

---

## 📘 Problem Statement

Given an array `arr[]` denoting the cost of stock on each day, the task is to find the **maximum total profit** if we can buy and sell the stocks **any number of times**.

> **Note:**
> We can only sell a stock which we have bought earlier, and we cannot hold multiple stocks on any day.

---

## 💡 Examples

### Example 1:

**Input:**
`arr[] = [100, 180, 260, 310, 40, 535, 695]`

**Output:**
`865`

**Explanation:**
Buy the stock on day 0 and sell it on day 3
→ `310 - 100 = 210`
Buy the stock on day 4 and sell it on day 6
→ `695 - 40 = 655`

**Maximum Profit = 210 + 655 = 865**

---

### Example 2:

**Input:**
`arr[] = [4, 2, 2, 2, 4]`

**Output:**
`2`

**Explanation:**
Buy the stock on day 3 and sell it on day 4
→ `4 - 2 = 2`

---

### Example 3:

**Input:**
`arr[] = [4, 2]`

**Output:**
`0`

**Explanation:**
Don't buy the stock.

---

## ⚙️ Constraints

```
2 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] ≤ 10^6
```

---

## 🧮 Expected Complexities

* **Time Complexity:** O(n)
* **Auxiliary Space:** O(n)

---

## 🏢 Company Tags

`Paytm`, `Flipkart`, `Accolite`, `Amazon`, `Microsoft`, `D-E-Shaw`,
`MakeMyTrip`, `Ola Cabs`, `Oracle`, `Walmart`, `Goldman Sachs`, `Directi`,
`Intuit`, `Google`, `Quikr`, `Salesforce`, `Pubmatic`, `Sapient`,
`Swiggy`, `Media.net`

---

## 🏷️ Topic Tags

* Arrays
* Dynamic Programming
* Greedy
* Data Structures
* Algorithms

---

## 💬 Related Interview Experiences

* Ola Interview Experience Set 7 for SDE 1
* Accolite Interview Experience Set 4 On Campus
* Directi Interview Set 1
* Intuit Interview Set 4 SSE
* One97 Paytm Interview Experience
* Paytm Interview Experience Set 4 Walk-In Drive
* Walmart Lab Interview Experience Set 8 Off Campus (3 Years Experience)
* MakeMyTrip Interview Experience Set 7 On Campus
* Directi Interview Experience Set 22 Pool Campus

---

## 📚 Related Articles

* [Stock Buy Sell](https://www.geeksforgeeks.org/stock-buy-sell/)

---

---

awesome—here’s a clean, interview-ready pack tailored to your requested format and the judge that expects a **single integer = total profit**.

---

# 2) Text explanation + step-by-step dry run

## Problem in one line

You may buy and sell the stock **many times** but can hold **at most one** share at a time. Return the **maximum total profit**.

## Key insight (greedy)

Every time price goes **up** from day `i-1` to `i`, if you had bought at `i-1` and sold at `i`, you’d lock in `arr[i] - arr[i-1]`. Summing **all positive day-to-day increases** equals buying at every **valley** and selling at the next **peak**—this is optimal with unlimited, fee-less transactions.

### Why optimal?

* A whole upward run (valley→peak) yields profit `peak - valley`.
* That equals the sum of its daily rises: `(a2-a1) + (a3-a2) + …`.
* Splitting or merging transactions in a rising run doesn’t change total profit, and there’s no penalty for multiple transactions ⇒ just add all positive deltas.

## Dry run (main sample)

`arr = [100, 180, 260, 310, 40, 535, 695]`

| Day | Price | Delta vs prev | Take? | Profit So Far |
| --- | ----- | ------------- | ----- | ------------- |
| 0   | 100   | —             | —     | 0             |
| 1   | 180   | +80           | yes   | 80            |
| 2   | 260   | +80           | yes   | 160           |
| 3   | 310   | +50           | yes   | 210           |
| 4   | 40    | −270          | no    | 210           |
| 5   | 535   | +495          | yes   | 705           |
| 6   | 695   | +160          | yes   | **865**       |

Final answer = **865**.

Edge checks:

* `[4,2,2,2,4]` → deltas `-2,0,0,+2` ⇒ profit `2`.
* `[4,2]` → delta `-2` ⇒ profit `0`.

---

# 3) Python solutions (multiple ways), same signature, interview-friendly comments

### A) Greedy (sum of rises) — simplest & fastest (what most interviewers expect)

```python
class Solution:
    # Function to find the days of buying and selling stock for max profit.
    # Returns TOTAL PROFIT as an integer (judge's expected output).
    def stockBuySell(self, arr):
        total_profit = 0
        # Add every positive day-to-day rise
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                total_profit += arr[i] - arr[i - 1]
        return total_profit
```

**Complexity:** `O(n)` time, `O(1)` space.

---

### B) “Valley→Peak scan” (explicit runs). Still O(n), but more mechanical

> Same profit, but walks to find each rising run (useful to explain *why* greedy works).

```python
class SolutionScan:
    # Same signature; returns TOTAL PROFIT (sum over all valley->peak runs)
    def stockBuySell(self, arr):
        n = len(arr)
        i = 0
        total_profit = 0

        while i < n - 1:
            # 1) Find next valley (strictly lower than next or equal handled)
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:  # no valley => no more profit
                break
            buy_price = arr[i]
            i += 1

            # 2) Climb to the next peak (non-decreasing)
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell_price = arr[i - 1]

            total_profit += sell_price - buy_price

        return total_profit
```

**Complexity:** `O(n)` time, `O(1)` space.

---

### C) DP (hold/cash states) — great for follow-ups (fees, cooldown)

```python
class SolutionDP:
    # Returns TOTAL PROFIT using 2-state DP (hold, cash).
    def stockBuySell(self, arr):
        if not arr:
            return 0

        # hold: best profit when holding 1 share after today's action
        # cash: best profit when holding 0 shares after today's action
        hold = -arr[0]
        cash = 0

        for price in arr[1:]:
            # Option to buy today or keep holding
            hold = max(hold, cash - price)
            # Option to sell today or keep not holding
            cash = max(cash, hold + price)

        return cash
```

**Complexity:** `O(n)` time, `O(1)` space.
Note: For unlimited, fee-less trades this equals greedy.

---

### (Bonus) If a platform instead expects **intervals** (buy/sell days)

```python
def intervals(arr):
    n = len(arr)
    ans = []
    i = 0
    while i < n - 1:
        while i < n - 1 and arr[i + 1] <= arr[i]:
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1
        while i < n and arr[i] >= arr[i - 1]:
            i += 1
        sell = i - 1
        ans.append([buy, sell])
    return ans  # e.g., [[0,3],[4,6]]
```

---

# 4) Interview quick-recall + expected Q&A

## Speed rules to remember

* **Mantra:** *Add every positive climb.*
* **One-liner:** `profit += max(0, arr[i]-arr[i-1])`
* **Picture:** buy at each **valley**, sell at the next **peak**.

## Likely questions & crisp answers

**Q1. Why does summing positive differences give the optimum?**
A: Any optimal strategy decomposes into disjoint increasing runs (valley→peak). Each run’s profit equals the sum of its daily rises. With unlimited, fee-less trades, splitting/merging doesn’t change profit, so summing all rises attains the maximum.

**Q2. What are the complexities?**
A: Greedy/scan/DP are all `O(n)` time, `O(1)` extra space.

**Q3. What if prices are flat or strictly decreasing?**
A: Flats contribute `0`; strictly decreasing yields profit `0`. The code naturally handles both.

**Q4. Can we hold multiple shares?**
A: No—constraint is at most one share at a time. Our approaches respect that.

**Q5. How would you add a transaction fee `f`?**
A: Use DP with fee on sell:
`hold = max(hold, cash - price)`
`cash = max(cash, hold + price - f)`.

**Q6. How about a 1-day cooldown after selling?**
A: Extend the DP with an extra state (or keep yesterday’s `cash`) to block immediate buy after sell.

**Q7. If the judge wanted **intervals** instead of profit?**
A: Use the valley→peak scan to output `[buy_day, sell_day]` pairs; multiplying them out equals the same total profit.

**Q8. Edge cases to mention before coding?**
A: `n < 2`, large `n` (need O(n)), duplicates/flat segments, all decreasing.

---

---

awesome—wrapping it up with the last two pieces you asked for.

---

# 5) Real-World Use Cases (a few, interview-relatable)

* **High-frequency/retail trading backtests (no fees model):**
  Baseline “upper bound” P&L by summing all positive ticks; then add constraints (fees, slippage, cooldown) to approach reality. Interviewers like hearing this as a *sanity ceiling* for strategies.

* **Currency/crypto arbitrage simulators:**
  When fees are negligible on certain venues/pairs, the same “sum of rises” provides the best-case profit for a single-unit trader switching between cash and the asset.

* **Inventory resale with daily catalog prices:**
  If you can carry at most one unit (capital bound) and may buy/sell any day, maximizing profit is identical to chaining all upward price moves between restocks.

* **Energy storage arbitrage (toy model):**
  With a battery that can be either “charged or not” and no round-trip loss/fees, the optimal policy is to buy (charge) before rising prices and sell (discharge) after—mathematically the same as summing positive deltas.

---

# 6) Full Python Program (with inline complexity notes + timing)

> This program includes three implementations: **Greedy**, **Valley→Peak Scan**, and **DP**.
> It prints the **maximum profit** for provided inputs and uses `timeit` to measure runtime.

```python
from timeit import timeit

class Solution:
    # Function to find the days of buying and selling stock for max profit.
    # Returns TOTAL PROFIT (integer), as most platforms expect.
    #
    # Idea: Sum every positive day-to-day rise.
    #
    # Time Complexity:
    #   - Single pass over the array: O(n)
    # Space Complexity:
    #   - Only a few scalars: O(1)
    def stockBuySell(self, arr):
        total_profit = 0  # O(1) space
        # O(n) loop: each step is O(1)
        for i in range(1, len(arr)):
            # Checking arr[i] > arr[i-1] is O(1)
            if arr[i] > arr[i - 1]:
                total_profit += arr[i] - arr[i - 1]  # O(1)
        # Return final accumulated profit: O(1)
        return total_profit


class SolutionScan:
    # Explicit valley->peak scan; computes the same total profit.
    #
    # Time Complexity:  O(n)   (each index visited at most twice)
    # Space Complexity: O(1)
    def stockBuySell(self, arr):
        n = len(arr)
        i = 0
        total_profit = 0

        # Outer loop advances i monotonically: O(n)
        while i < n - 1:
            # Find next valley (skip non-increasing segment): amortized O(1) per element
            while i < n - 1 and arr[i + 1] <= arr[i]:
                i += 1
            if i == n - 1:
                break
            buy_price = arr[i]
            i += 1

            # Climb to peak (consume non-decreasing segment): amortized O(1) per element
            while i < n and arr[i] >= arr[i - 1]:
                i += 1
            sell_price = arr[i - 1]

            total_profit += sell_price - buy_price  # O(1)

        return total_profit


class SolutionDP:
    # 2-state DP (hold/cash). Good template for fees/cooldown variants.
    #
    # Time Complexity:  O(n)
    # Space Complexity: O(1)
    def stockBuySell(self, arr):
        if not arr:
            return 0

        # hold: max profit holding 1 share after today's action
        # cash: max profit holding 0 shares after today's action
        hold = -arr[0]  # buy on day 0 as a possible starting state
        cash = 0

        # Loop once: O(n)
        for price in arr[1:]:
            # Each update is O(1)
            hold = max(hold, cash - price)  # buy or keep holding
            cash = max(cash, hold + price)  # sell or keep cash

        return cash


def run_demo():
    # -------- Input values (feel free to add your own) --------
    samples = [
        ("Case 1", [100, 180, 260, 310, 40, 535, 695], 865),
        ("Case 2", [4, 2, 2, 2, 4], 2),
        ("Case 3", [4, 2], 0),
        ("Flat",   [5, 5, 5, 5], 0),
        ("AllUp",  [1, 2, 3, 4, 5], 4),
        ("AllDown",[9, 7, 5, 3, 1], 0),
    ]

    # Instantiate solutions
    greedy = Solution()
    scan = SolutionScan()
    dp = SolutionDP()

    # Print header
    print("=== Maximum Profit for Multiple Transactions (One Share at a Time) ===\n")

    for name, arr, expected in samples:
        # Compute outputs using three approaches (O(n) each)
        out_greedy = greedy.stockBuySell(arr)
        out_scan   = scan.stockBuySell(arr)
        out_dp     = dp.stockBuySell(arr)

        # Show results
        print(f"{name}:")
        print(f"  Input:    {arr}")
        print(f"  Greedy:   {out_greedy}")
        print(f"  Scan:     {out_scan}")
        print(f"  DP:       {out_dp}")
        print(f"  Expected: {expected}")
        print(f"  Match?    {out_greedy == out_scan == out_dp == expected}\n")

    # -------- Timing with timeit (whole-program style micro-bench) --------
    # We time each method on a bigger array to get a stable number.
    big_arr = list(range(1, 10000)) + list(range(10000, 0, -1))  # up then down

    # Prepare callables so timeit can measure only the function body.
    greedy_timer = lambda: greedy.stockBuySell(big_arr)
    scan_timer   = lambda: scan.stockBuySell(big_arr)
    dp_timer     = lambda: dp.stockBuySell(big_arr)

    # Each run repeats the function N times; adjust N for your machine.
    N = 200

    t_greedy = timeit(greedy_timer, number=N)
    t_scan   = timeit(scan_timer,   number=N)
    t_dp     = timeit(dp_timer,     number=N)

    print("=== Timing (timeit) on a larger input ===")
    print(f"Array length: {len(big_arr)}, repetitions per method: {N}")
    print(f"Greedy (sum of rises):  {t_greedy:.6f} s")
    print(f"Valley→Peak scan:       {t_scan:.6f} s")
    print(f"DP (hold/cash):         {t_dp:.6f} s")


if __name__ == "__main__":
    run_demo()
```

### What you’ll see when you run it

* For each sample case, the three methods print the **same profit** and a boolean `Match? True`.
* At the end, the `timeit` section prints total seconds for each method on a larger synthetic array—on most machines, all three should be within the same O(n) ballpark, with the greedy often a hair faster/simpler.
