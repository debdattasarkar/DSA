# Stock Buy and Sell – Max K Transactions Allowed

## Introduction

The **Stock Buy and Sell – Max K Transactions Allowed** problem is a dynamic programming challenge where the goal is to determine the **maximum profit** that can be achieved by performing at most `k` stock transactions.

A transaction is defined as **buying and then selling** one share of stock. A new transaction can only start after the previous one is completed.

---

## Table of Contents

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Examples](#examples)
* [Constraints](#constraints)
* [Expected Complexity](#expected-complexity)
* [Tags](#tags)

---

## Problem Statement

You are given:

* An array `prices[]` where `prices[i]` represents the stock price on day `i`.
* An integer `k` representing the maximum number of transactions allowed.

Your task is to **maximize profit** by choosing at most `k` transactions such that no overlapping transactions occur.

---

## Examples

### Example 1

```
Input: prices[] = [10, 22, 5, 80], k = 2  
Output: 87  
Explanation:
  1st transaction: Buy at 10 and sell at 22 → Profit = 12  
  2nd transaction: Buy at 5 and sell at 80 → Profit = 75  
  Total Profit = 12 + 75 = 87
```

### Example 2

```
Input: prices[] = [20, 580, 420, 900], k = 3  
Output: 1040  
Explanation:
  1st transaction: Buy at 20 and sell at 580 → Profit = 560  
  2nd transaction: Buy at 420 and sell at 900 → Profit = 480  
  Total Profit = 560 + 480 = 1040
```

### Example 3

```
Input: prices[] = [100, 90, 80, 50, 25], k = 1  
Output: 0  
Explanation: Selling prices decrease continuously. No profit can be made.
```

---

## Constraints

* `1 ≤ prices.length ≤ 10^3`
* `1 ≤ k ≤ 200`
* `1 ≤ prices[i] ≤ 10^3`

---

## Expected Complexity

* **Time Complexity**: O(n × k)
* **Auxiliary Space**: O(k)

---

## Tags

### Company Tags

`Accolite`, `Amazon`, `Microsoft`

### Topic Tags

`Dynamic Programming`, `Algorithms`

---

## Related Content

* **Interview Experience**: Amazon Interview Experience For 6 Months Internship
* **Article**: Maximum Profit By Buying And Selling A Share At Most K Times

---

Here is a detailed explanation and implementation of the **Stock Buy and Sell – Max K Transactions Allowed** problem.

---

## 🧠 Problem Summary

You are given:

* An array `prices[]` representing the price of a stock on each day.
* An integer `k`, the maximum number of allowed transactions.

**Task:** Maximize profit with at most `k` buy-sell transactions.

**Rules:**

* One transaction = buy + sell.
* You cannot hold more than one stock at a time.
* Must sell before buying again.

---

## 🧪 Dry Run Example

**Input:**
`prices = [10, 22, 5, 80]`, `k = 2`
**Explanation:**

* Buy at 10, sell at 22 → Profit = 12
* Buy at 5, sell at 80 → Profit = 75
  **Total Profit = 12 + 75 = 87 ✅**

---

## 💡 Approach (Dynamic Programming)

Let `dp[t][d]` represent the **maximum profit up to day `d` with at most `t` transactions**.

**Transition Formula:**

```python
dp[t][d] = max(dp[t][d - 1], prices[d] - prices[m] + dp[t - 1][m])
```

Optimized version (using rolling max):

```python
dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
max_diff = max(max_diff, dp[t - 1][d] - prices[d])
```

---

## ✅ Python Code (O(k \* n))

```python
class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # Optimization for large k
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int maxProfit(vector<int>& prices, int k) {
        int n = prices.size();
        if (n == 0 || k == 0) return 0;

        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; ++i)
                if (prices[i] > prices[i-1]) profit += prices[i] - prices[i-1];
            return profit;
        }

        vector<vector<int>> dp(k+1, vector<int>(n, 0));

        for (int t = 1; t <= k; ++t) {
            int max_diff = -prices[0];
            for (int d = 1; d < n; ++d) {
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff);
                max_diff = max(max_diff, dp[t-1][d] - prices[d]);
            }
        }

        return dp[k][n-1];
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    maxProfit(prices, k) {
        const n = prices.length;
        if (n === 0 || k === 0) return 0;

        if (k >= Math.floor(n / 2)) {
            let profit = 0;
            for (let i = 1; i < n; i++)
                if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
            return profit;
        }

        const dp = Array.from({ length: k + 1 }, () => Array(n).fill(0));

        for (let t = 1; t <= k; t++) {
            let maxDiff = -prices[0];
            for (let d = 1; d < n; d++) {
                dp[t][d] = Math.max(dp[t][d - 1], prices[d] + maxDiff);
                maxDiff = Math.max(maxDiff, dp[t - 1][d] - prices[d]);
            }
        }

        return dp[k][n - 1];
    }
}
```

---

## 🧮 Time and Space Complexity

* **Time:** `O(k * n)`
* **Space:** `O(k * n)` (can be optimized to O(n))
