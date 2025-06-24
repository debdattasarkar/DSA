Here is the README-style explanation, dry run, and full code in **Python**, **C++**, and **JavaScript** for **Leetcode 122 – Best Time to Buy and Sell Stock II**.

---

# 💹 Best Time to Buy and Sell Stock II (Leetcode #122)

### 🟡 Difficulty: Medium

**Tags**: `Array`, `Dynamic Programming`, `Greedy`

---

## 📘 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

On each day, you can:

* **Buy and/or Sell**
* But **hold at most one share at a time**

You can **buy and sell on the same day**.

### Goal:

Return the **maximum profit** you can achieve.

---

## 🧪 Examples

### Example 1

```
Input:  prices = [7,1,5,3,6,4]
Output: 7
Explanation:
  Buy at 1, sell at 5 → profit = 4
  Buy at 3, sell at 6 → profit = 3
Total profit = 4 + 3 = 7
```

### Example 2

```
Input:  prices = [1,2,3,4,5]
Output: 4
Explanation: Buy at 1, sell at 5 → profit = 4 (or make daily profit)
```

---

## 🔍 Dry Run (Greedy Strategy)

**Input:** `[1, 5, 3, 6, 4]`

* Day 0 to 1: profit = 5 - 1 = 4 ✅
* Day 1 to 2: 3 - 5 = -2 ❌
* Day 2 to 3: 6 - 3 = 3 ✅
* Day 3 to 4: 4 - 6 = -2 ❌

**Total Profit = 4 + 3 = 7**

---

## ✅ Greedy Strategy

Buy and sell **every time there's an increase**:

```text
if prices[i] > prices[i-1], then profit += prices[i] - prices[i-1]
```

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]  # Sell on profit
        return profit
```

---

## 💠 C++ Code

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];  // Sell at profit
            }
        }
        return profit;
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
    let profit = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];  // Add profit from local rise
        }
    }
    return profit;
};
```

---

## ✅ Summary

| Metric           | Value                    |
| ---------------- | ------------------------ |
| Time Complexity  | `O(n)`                   |
| Space Complexity | `O(1)`                   |
| Greedy Strategy  | ✅ Maximize local profits |
| In-place         | ✅ Yes                    |

---

Great! Let’s walk through the **DP Table Version** of **Leetcode 122 – Best Time to Buy and Sell Stock II**.

---

# 📊 DP Table – Best Time to Buy and Sell Stock II

This is the foundation for solving more complex stock trading problems like:

* \[123] At most 2 transactions
* \[309] With cooldown
* \[714] With transaction fee

---

## 🧠 State Definition

Define:

* `dp[i][0]` = Max profit on day `i` when you **hold stock**
* `dp[i][1]` = Max profit on day `i` when you **do not hold stock**

---

## 🔁 Recurrence Relations

At each day `i`:

* `dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])`
  → Hold from yesterday, or buy today

* `dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])`
  → Stay idle, or sell today

---

## 🎯 Base Case (Day 0)

```text
dp[0][0] = -prices[0]   # Bought stock
dp[0][1] = 0            # Did nothing
```

---

## 🐍 Python Code (DP Table)

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = -prices[0]  # Bought stock
        dp[0][1] = 0           # No stock

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])  # Hold or Buy
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])  # Idle or Sell

        return dp[n-1][1]  # Profit without holding on last day
```

---

## 🧠 Space-Optimized Version (O(1) DP)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, cash = -prices[0], 0

        for i in range(1, len(prices)):
            hold = max(hold, cash - prices[i])   # Hold or buy
            cash = max(cash, hold + prices[i])   # Idle or sell

        return cash
```

---

## 💠 C++ Code (Space-Optimized)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int hold = -prices[0], cash = 0;

        for (int i = 1; i < prices.size(); ++i) {
            hold = max(hold, cash - prices[i]);     // Buy or hold
            cash = max(cash, hold + prices[i]);     // Sell or hold
        }

        return cash;
    }
};
```

---

## 🌐 JavaScript Code (Space-Optimized)

```javascript
var maxProfit = function(prices) {
    let hold = -prices[0], cash = 0;

    for (let i = 1; i < prices.length; i++) {
        hold = Math.max(hold, cash - prices[i]);   // Buy or hold
        cash = Math.max(cash, hold + prices[i]);   // Sell or hold
    }

    return cash;
};
```

---

## ✅ Summary

| State        | Meaning                           |
| ------------ | --------------------------------- |
| `dp[i][0]`   | Max profit holding stock at i     |
| `dp[i][1]`   | Max profit not holding stock at i |
| Final answer | `dp[n-1][1]`                      |

| Complexity        | Value  |
| ----------------- | ------ |
| Time              | `O(n)` |
| Space (Table)     | `O(n)` |
| Space (Optimized) | `O(1)` |

---

