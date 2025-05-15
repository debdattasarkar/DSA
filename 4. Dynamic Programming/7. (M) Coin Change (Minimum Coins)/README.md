
# Coin Change (Minimum Coins)

## Introduction

The **Coin Change (Minimum Coins)** problem is a classic algorithmic challenge where you're given an array of coin denominations and a target sum. The objective is to determine the **minimum number of coins** required to achieve the target sum using any number of coins. If it’s not possible to reach the sum with the given denominations, the function should return `-1`.

This problem is often solved using **Dynamic Programming** and is frequently asked in technical interviews.

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

You are given an array `coins[]`, where each element represents a coin of a **different denomination**, and a target value `sum`.

* You have an **unlimited supply** of each coin type.
* Your task is to determine the **minimum number of coins** needed to obtain the target `sum`.
* If it is **not possible** to form the sum using the given coins, return `-1`.

---

## Examples

### Example 1

```
Input: coins[] = [25, 10, 5], sum = 30  
Output: 2  
Explanation: Minimum 2 coins needed, 25 and 5
```

### Example 2

```
Input: coins[] = [9, 6, 5, 1], sum = 19  
Output: 3  
Explanation: 19 = 9 + 9 + 1
```

### Example 3

```
Input: coins[] = [5, 1], sum = 0  
Output: 0  
Explanation: For 0 sum, we do not need a coin
```

### Example 4

```
Input: coins[] = [4, 6, 2], sum = 5  
Output: -1  
Explanation: Not possible to make the given sum
```

---

## Constraints

* `1 ≤ sum * coins.length ≤ 10^6`
* `0 ≤ sum ≤ 10^4`
* `1 ≤ coins[i] ≤ 10^4`
* `1 ≤ coins.length ≤ 10^3`

---

## Expected Complexity

* **Time Complexity**: O(coins.length × sum)
* **Auxiliary Space**: O(sum)

---

## Tags

### Company Tags

`Paytm`, `Morgan Stanley`, `Accolite`, `Amazon`, `Microsoft`, `Samsung`, `Snapdeal`, `Oracle`, `Visa`, `Google`, `Synopsys`

### Topic Tags

`Dynamic Programming`, `Algorithms`

---

## Related Content

* **Interview Experience**: Accolite Interview Experience Set 6 On Campus
* **Article**: Find Minimum Number Of Coins That Make A Change

---

Here’s a step-by-step explanation with **dry run**, followed by **code in Python, C++, and JavaScript** for the **Coin Change (Minimum Coins)** problem from GeeksforGeeks.

---

## 💡 Problem Summary:

You are given:

* A list of coin denominations `coins[]`.
* A target sum `S`.

Your task is to find the **minimum number of coins** needed to make sum `S`. If it's not possible, return `-1`.

---

## 🧠 Core Logic (Dynamic Programming)

We use **bottom-up DP**:

* `dp[i]` = minimum number of coins needed to make sum `i`.
* Initialize `dp[0] = 0`, rest as `inf` (or a large number).
* For each `coin`, for every `j` from `coin` to `sum`:

  * Update: `dp[j] = min(dp[j], dp[j - coin] + 1)`

---

### 🧪 Dry Run Example

**Input:** coins = \[9, 6, 5, 1], sum = 11

```
dp[0] = 0
dp[1] = 1          # 1
dp[2] = 2          # 1+1
dp[5] = 1          # 5
dp[6] = 1          # 6
dp[9] = 1          # 9
dp[10] = 2         # 9+1
dp[11] = 2         # 6+5 or 9+1+1
```

Output = 2 ✅

---

## ✅ Python Code

```python
class Solution:
    def minCoins(self, coins, sum):
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0  # 0 coins to make sum 0

        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[sum] if dp[sum] != float('inf') else -1
```

---

## ✅ C++ Code

```cpp
class Solution {
  public:
    int minCoins(vector<int> &coins, int sum) {
        vector<int> dp(sum + 1, INT_MAX);
        dp[0] = 0;

        for (int coin : coins) {
            for (int i = coin; i <= sum; i++) {
                if (dp[i - coin] != INT_MAX)
                    dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }

        return dp[sum] == INT_MAX ? -1 : dp[sum];
    }
};
```

---

## ✅ JavaScript Code

```javascript
class Solution {
    minCoins(coins, sum) {
        let dp = Array(sum + 1).fill(Infinity);
        dp[0] = 0;

        for (let coin of coins) {
            for (let i = coin; i <= sum; i++) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        return dp[sum] === Infinity ? -1 : dp[sum];
    }
}
```

---

## 🕒 Time & Space Complexity:

* **Time:** `O(n * sum)` where `n = coins.length`
* **Space:** `O(sum)`

Let me know if you'd like a **recursive memoized solution** or if you want to trace a specific test case!
