
---

# 📈 Best Time to Buy and Sell Stock (Leetcode #121)

### 🟢 Difficulty: Easy

**Topics**: `Array`, `Dynamic Programming`

---

## 📘 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on the i-th day.

You want to **maximize your profit** by choosing:

* **One day to buy**
* **A future day to sell**

You **must** buy before you sell.

---

## 🧪 Examples

### Example 1:

```
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1, sell at 6 → profit = 6 - 1 = 5
```

### Example 2:

```
Input:  prices = [7,6,4,3,1]
Output: 0
Explanation: No transaction is done (prices always fall)
```

---

## ⚙️ Constraints

* `1 <= prices.length <= 10⁵`
* `0 <= prices[i] <= 10⁴`

---

## 💡 Approach (Kadane-like single pass)

We track:

* `min_price_so_far`: lowest value seen so far (buy point)
* `max_profit`: max difference between current price and `min_price_so_far`

At each step, calculate:
`profit = prices[i] - min_price_so_far`
and update `max_profit` accordingly.

---

## 📊 Dry Run

**Input:** `[7, 1, 5, 3, 6, 4]`

| i | prices\[i] | min\_price | profit    | max\_profit |
| - | ---------- | ---------- | --------- | ----------- |
| 0 | 7          | 7          | -         | 0           |
| 1 | 1          | 1          | 0         | 0           |
| 2 | 5          | 1          | 5 - 1 = 4 | 4           |
| 3 | 3          | 1          | 3 - 1 = 2 | 4           |
| 4 | 6          | 1          | 6 - 1 = 5 | **5** ✅     |
| 5 | 4          | 1          | 4 - 1 = 3 | 5           |

✅ Final answer: `5`

---

You are given an array `prices` where `prices[i]` is the price of a given stock on the `iᵗʰ` day.
You must **buy** on one day and **sell** on another **future** day to maximize your profit.

---

### 🧠 Key Insight:

We must find the maximum difference `prices[j] - prices[i]` such that `j > i`.

---

### 🔍 Step-by-Step Explanation (Greedy - Optimal)

We use a **single pass** with two variables:

* `min_price`: tracks the lowest price seen so far.
* `max_profit`: stores the maximum profit achievable at each step.

#### Dry Run Example:

```text
prices = [7, 1, 5, 3, 6, 4]
min_price = 7
max_profit = 0

Day 1: price = 7 → min_price = 7, profit = 0
Day 2: price = 1 → min_price = 1, profit = 0
Day 3: price = 5 → profit = 5 - 1 = 4 → max_profit = 4
Day 4: price = 3 → profit = 3 - 1 = 2 → max_profit = 4
Day 5: price = 6 → profit = 6 - 1 = 5 → max_profit = 5
Day 6: price = 4 → profit = 4 - 1 = 3 → max_profit = 5
```

🔚 Final answer: `5`

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize with maximum possible value
        max_profit = 0  # Start with no profit

        for price in prices:
            if price < min_price:
                min_price = price  # Update to new min price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)  # Update max profit
        
        return max_profit
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;

        for (int price : prices) {
            if (price < min_price)
                min_price = price; // Best day to buy
            else
                max_profit = max(max_profit, price - min_price); // Maximize profit
        }

        return max_profit;
    }
};
```

---

## 🌐 JavaScript Code

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        if (price < minPrice) {
            minPrice = price; // Best buy so far
        } else {
            maxProfit = Math.max(maxProfit, price - minPrice); // Maximize profit
        }
    }

    return maxProfit;
};
```

---

## ✅ Summary

| Metric           | Value                                   |
| ---------------- | --------------------------------------- |
| Time Complexity  | `O(n)`                                  |
| Space Complexity | `O(1)`                                  |
| In-place         | ✅ Yes                                   |
| Strategy         | Track min + compute profit at each step |

---

Absolutely! But let's clarify what "better" means here. For **Leetcode 121 – Best Time to Buy and Sell Stock**, the current solution is already:

* ✅ **Optimal** in time: `O(n)`
* ✅ **Optimal** in space: `O(1)`
* ✅ **Clean and readable**

So in terms of **performance**, **you can't do better**.

---

## 🔧 What Can Be Improved?

We can still refine:

* **Code clarity / style**
* **Robust naming**
* **Idiomatic patterns** for each language

Let me show you a **cleaner and slightly more elegant version** in each language.

---

### 🐍 Python (Elegant + Annotated)

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # Calculate profit if we sold today
            profit = price - min_price
            max_profit = max(max_profit, profit)
            # Update minimum price so far
            min_price = min(min_price, price)

        return max_profit
```

✅ Why better?

* Avoids float('inf')
* Skips unnecessary first comparison
* More declarative: `min(min_price, price)`

---

### 💠 C++ (Robust and Idiomatic)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int max_profit = 0;

        for (size_t i = 1; i < prices.size(); ++i) {
            max_profit = max(max_profit, prices[i] - min_price);
            min_price = min(min_price, prices[i]);
        }

        return max_profit;
    }
};
```

✅ Clear loop and avoids `INT_MAX`.

---

### 🌐 JavaScript (Succinct + ES6 Style)

```javascript
var maxProfit = function(prices) {
    let minPrice = prices[0];
    let maxProfit = 0;

    for (let i = 1; i < prices.length; i++) {
        maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        minPrice = Math.min(minPrice, prices[i]);
    }

    return maxProfit;
};
```

✅ Leverages `Math.min` / `Math.max` clearly.

---

## 📌 Summary

You can't beat the current time/space, but **writing clean, readable, idiomatic code is key for interviews**.

Here’s a **functional-style version** of the **Best Time to Buy and Sell Stock** problem (Leetcode #121) written in Python, using built-in tools like `itertools` and `functools`. It’s not *strictly* faster, but it’s elegant and Pythonic.

---

# 🧠 Functional Programming Version (Python)

```python
from typing import List
from functools import reduce
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def reducer(acc, price):
            min_price, max_profit = acc
            new_min = min(min_price, price)
            new_profit = max(max_profit, price - min_price)
            return new_min, new_profit

        _, max_profit = reduce(reducer, prices[1:], (prices[0], 0))
        return max_profit
```

---

## ✅ How It Works

* We use `functools.reduce()` to scan through the array once.
* At each step:

  * We update the `min_price` seen so far.
  * Compute `price - min_price` to get current potential profit.
  * Track the `max_profit`.

It simulates a fold/scan operation over the list and returns the best result in one pass.

---

## 📌 Notes

| Feature          | Value                                 |
| ---------------- | ------------------------------------- |
| Time Complexity  | `O(n)`                                |
| Space Complexity | `O(1)`                                |
| Libraries Used   | `reduce`, `min`, `max`                |
| Tradeoff         | Slightly harder to read for beginners |

---

Certainly! A **DP (Dynamic Programming) table version** for **Leetcode 121 – Best Time to Buy and Sell Stock** is not necessary for optimal performance (as the greedy solution is O(n) and O(1)), but it’s still useful **for learning and pattern recognition**, especially if you're preparing for more advanced stock problems like:

* \[122] Buy/Sell Multiple Times
* \[123] At Most Two Transactions
* \[188] At Most K Transactions
* \[309] Cooldown
* \[714] Transaction Fee

---

# 🧠 Dynamic Programming Table Version

### 💡 State Definition:

We define two states for each day `i`:

* `dp[i][0]`: Max profit **holding a stock** at day `i`
* `dp[i][1]`: Max profit **not holding a stock** at day `i`

### 🎯 Goal:

Return `dp[n-1][1]` → the max profit on the last day **without holding stock**

---

## ✅ Transition Relations:

* `dp[i][0] = max(dp[i-1][0], -prices[i])`
  → Either hold from yesterday or buy today (so negative price)

* `dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])`
  → Either keep not holding, or sell today

---

## 🐍 Python Code (DP Table)

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = -prices[0]  # Bought on day 0
        dp[0][1] = 0           # No stock on day 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        return dp[n-1][1]
```

---

## 🧠 Space-Optimized Version (O(1) DP)

Since we only need `i-1` state, we can compress the DP:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]  # State for holding stock
        cash = 0           # State for not holding stock

        for price in prices[1:]:
            hold = max(hold, -price)
            cash = max(cash, hold + price)

        return cash
```

---

## 📊 Summary

| Technique   | Time | Space | Notes                |
| ----------- | ---- | ----- | -------------------- |
| Greedy      | O(n) | O(1)  | Best                 |
| DP Table    | O(n) | O(n)  | Good for learning    |
| DP Compress | O(n) | O(1)  | Equivalent to Greedy |

---

## ❓ Common Interview Questions & Answers:

1. **Q: Why can't we buy and sell on the same day?**
   **A:** Because the profit must be calculated from a future sell day (`j > i`), which would result in 0 or negative profit if done on same day.

2. **Q: What's the time complexity?**
   **A:** O(n), where `n` is the number of days. Only one pass is needed.

3. **Q: Can we solve this with O(1) space?**
   **A:** Yes, we're only using two variables (`min_price` and `max_profit`), so space complexity is O(1).

4. **Q: What happens if prices are always decreasing?**
   **A:** The algorithm will return `0` as there's no profitable day to sell.

5. **Q: Can we use dynamic programming?**
   **A:** Yes, but it's overkill. Greedy is optimal here because we only need the best min-buy and max-profit relation.

---