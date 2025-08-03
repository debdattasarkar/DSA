
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

Here’s a step-by-step explanation with **dry run**, followed by **code in Python, C++, and JavaScript** for the **Coin Change (Minimum Coins)** problem.

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

---

Here's the **Python code** for the **Coin Change (Minimum Coins)** problem using **dynamic programming** with a clear explanation:

---

### ✅ Problem Summary

You are given:

* A list of coin denominations `coins[]`
* A target value `sum`

You must find the **minimum number of coins** needed to make the target `sum`.
You have **unlimited supply** of each coin.

Return `-1` if the target sum **cannot be formed**.

---

### 🧠 Logic (Dynamic Programming)

We use a 1D `dp` array where `dp[i]` will hold the **minimum number of coins** required to get sum = `i`.

* Initialize:

  ```python
  dp = [float('inf')] * (sum + 1)
  dp[0] = 0   # 0 coins to make sum = 0
  ```

* Transition:
  For each coin in `coins`:

  ```python
  for coin in coins:
      for s in range(coin, sum + 1):
          dp[s] = min(dp[s], 1 + dp[s - coin])
  ```

---

### 🐍 Python Code with Inline Comments

```python
#User function Template for python3
class Solution:
    def minCoins(self, coins, target_sum):
        # Initialize the dp array
        dp = [float('inf')] * (target_sum + 1)
        dp[0] = 0  # Base case: 0 coins needed to make sum 0

        # Fill the dp table
        for coin in coins:
            for s in range(coin, target_sum + 1):
                if dp[s - coin] != float('inf'):
                    dp[s] = min(dp[s], 1 + dp[s - coin])

        # If the value is still infinity, it means sum can't be formed
        return -1 if dp[target_sum] == float('inf') else dp[target_sum]
```

---

### 🧪 Dry Run (Example)

#### Input:

```python
coins = [25, 10, 5]
sum = 30
```

#### Steps:

* `dp[0] = 0`
* Try coin = 5, update dp\[5], dp\[10], ..., dp\[30]
* Then try coin = 10, then 25...

Eventually, `dp[30] = 2` using \[25, 5].

---

### ⌛ Time & Space Complexity

* **Time:** `O(sum * len(coins))`
* **Space:** `O(sum)`

---

Absolutely! Let’s walk through a **visual dry run** of the **Coin Change (Minimum Coins)** problem using the dynamic programming approach.

---

## 🔍 Example

### Input:

```python
coins = [1, 3, 4]
target_sum = 6
```

Our task is to find the **minimum number of coins** to make sum = 6.

---

## 📦 Step-by-Step Table (`dp` array)

We define `dp[i]` as the **minimum number of coins** needed to get a sum of `i`.

### Initial Setup:

```python
dp = [0, ∞, ∞, ∞, ∞, ∞, ∞]   # indices 0 to 6
```

Only `dp[0] = 0` because it takes 0 coins to make sum 0.

---

### 🪙 Process coin = 1:

We iterate from `1 to 6`:

```text
dp[1] = min(dp[1], 1 + dp[0]) → 1
dp[2] = min(dp[2], 1 + dp[1]) → 2
dp[3] = min(dp[3], 1 + dp[2]) → 3
dp[4] = min(dp[4], 1 + dp[3]) → 4
dp[5] = min(dp[5], 1 + dp[4]) → 5
dp[6] = min(dp[6], 1 + dp[5]) → 6
```

```python
dp = [0, 1, 2, 3, 4, 5, 6]
```

---

### 🪙 Process coin = 3:

```text
dp[3] = min(3, 1 + dp[0]) → 1
dp[4] = min(4, 1 + dp[1]) → 2
dp[5] = min(5, 1 + dp[2]) → 3
dp[6] = min(6, 1 + dp[3]) → 2
```

```python
dp = [0, 1, 2, 1, 2, 3, 2]
```

---

### 🪙 Process coin = 4:

```text
dp[4] = min(2, 1 + dp[0]) → 1
dp[5] = min(3, 1 + dp[1]) → 2
dp[6] = min(2, 1 + dp[2]) → 2
```

```python
dp = [0, 1, 2, 1, 1, 2, 2]
```

---

### ✅ Final Result:

`dp[6] = 2`

That means the **minimum number of coins to make 6** is `2`.

### 💡 Possible Combinations:

* 3 + 3
* 2 + 4
* 1 + 1 + 4 (not optimal)
* 1 + 1 + 1 + 3 (not optimal)

Best: **3 + 3** or **4 + 2**

---

## 🧠 Intuition Recap

* We build up solutions for every smaller amount.
* For each coin, we try to improve the answer for every sum from `coin` to `target_sum`.
* Result is stored in `dp[target_sum]`.

---

Great! Here's a **grid layout** (table-style) dry run for the Coin Change problem using:

```
coins = [1, 3, 4]
target_sum = 6
```

We’ll construct a 1D `dp` array step-by-step for each coin.

---

### 🧮 Initialization

| Index (Sum) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - | - |
| `dp`        | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |

> We use `0` for sum = 0 and `∞` (infinity) as placeholder for uncalculated values.

---

### 💰 Coin = 1

For every sum `s` from 1 to 6, try using coin `1`:

```
dp[s] = min(dp[s], dp[s - 1] + 1)
```

| Index (Sum) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - | - |
| `dp`        | 0 | 1 | 2 | 3 | 4 | 5 | 6 |

---

### 💰 Coin = 3

Update `dp[s] = min(dp[s], dp[s - 3] + 1)` where `s >= 3`

| Index (Sum) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - | - |
| `dp`        | 0 | 1 | 2 | 1 | 2 | 3 | 2 |

* `dp[3] = min(3, dp[0]+1) = 1`
* `dp[4] = min(4, dp[1]+1) = 2`
* `dp[5] = min(5, dp[2]+1) = 3`
* `dp[6] = min(6, dp[3]+1) = 2`

---

### 💰 Coin = 4

Update `dp[s] = min(dp[s], dp[s - 4] + 1)` where `s >= 4`

| Index (Sum) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - | - |
| `dp`        | 0 | 1 | 2 | 1 | 1 | 2 | 2 |

* `dp[4] = min(2, dp[0]+1) = 1`
* `dp[5] = min(3, dp[1]+1) = 2`
* `dp[6] = min(2, dp[2]+1) = 2`

---

### ✅ Final `dp` Array:

| Index (Sum) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----------- | - | - | - | - | - | - | - |
| `dp`        | 0 | 1 | 2 | 1 | 1 | 2 | 2 |

➡️ `dp[6] = 2` → Answer = **2 coins needed to make 6**

---

### 📦 Summary

This **grid-style layout** shows how the solution evolves:

* Coin by coin
* Sum by sum
* Value changes only if we find a better (smaller) count
